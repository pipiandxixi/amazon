import argparse
import datetime
import json
import os
import re
import time

from scan_common import (
    RESULTS_DIR,
    OpenCliError,
    eval_browser,
    extract_json_array,
    extract_json_object,
    open_browser,
    wait_for_query_result,
)


SCRAPE_KEYWORDS_JS = """
(() => {
  const table = document.querySelector('table#table-condition-search');
  if (!table) return JSON.stringify([]);

  const rawHeaders = Array.from(table.querySelectorAll('thead th'));
  const firstRow = table.querySelector('tbody tr');
  const firstCellCount = firstRow ? firstRow.querySelectorAll('td').length : rawHeaders.length;
  const unrepresentedColumns = Math.max(0, firstCellCount - rawHeaders.length);
  const headers = [];
  rawHeaders.forEach(th => {
    const label = th.innerText.trim();
    headers.push(label);
    // SellerSprite renders an extra PPC range cell without declaring colspan.
    if (label.includes('PPC') && unrepresentedColumns > 0) {
      for (let i = 0; i < unrepresentedColumns; i++) headers.push(label);
    }
  });

  const findIndex = patterns => headers.findIndex(h => patterns.some(pattern => h.includes(pattern)));
  const keywordIdx = findIndex(['关键词']);
  const searchesIdx = findIndex(['月搜索量']);
  const purchasesIdx = findIndex(['月购买量']);
  const clicksIdx = findIndex(['点击量']);
  const growthIdx = findIndex(['增长率', '增速']);
  const monopolyIdx = findIndex(['集中度', '垄断']);
  const bidIdx = findIndex(['PPC', '建议竞价', '广告竞价']);
  const productsIdx = findIndex(['商品数', '搜索结果数', '相关商品']);
  const priceReviewsIdx = findIndex(['市场分析', '价格', 'Review']);

  const items = [];
  const rows = table.querySelectorAll('tbody tr');
  for (let i = 0; i < rows.length; i += 3) {
    const mainRow = rows[i];
    const detailRow = rows[i + 1];
    if (!mainRow || !detailRow) continue;
    const cells = Array.from(mainRow.querySelectorAll('td')).map(td => td.innerText.trim());
    const value = idx => idx >= 0 ? (cells[idx] || '') : '';
    items.push({
      index: cells[1] || '',
      keyword: value(keywordIdx),
      searches: value(searchesIdx),
      purchases: value(purchasesIdx),
      clicks: value(clicksIdx),
      growth: value(growthIdx),
      monopoly: value(monopolyIdx),
      products: value(productsIdx),
      bid: value(bidIdx),
      price_reviews: value(priceReviewsIdx),
      details: detailRow.innerText.trim()
    });
  }
  return JSON.stringify(items);
})()
"""


def submit_global_search(filter_params, sort_config):
    form_params = dict(filter_params)
    form_params["marketPeriod"] = "N"
    form_params["marketQuota"] = sort_config.get("field", "purchase_rate")
    form_params["quotaOrder"] = "1" if sort_config.get("descending", True) else "0"
    form_params["order.field"] = form_params["marketQuota"]
    form_params["order.desc"] = "true" if form_params["quotaOrder"] == "1" else "false"
    fill_js = """
    (() => {
      const toggle = document.querySelector('a[name=switchVisible]');
      if (toggle && toggle.innerText.includes('展开')) toggle.click();

      Array.from(document.querySelectorAll('input[name]')).forEach(input => {
        if (!['station', 'order.field', 'order.desc'].includes(input.name)) {
          input.value = '';
          input.dispatchEvent(new Event('input', { bubbles: true }));
          input.dispatchEvent(new Event('change', { bubbles: true }));
        }
      });

      const params = """ + json.dumps(form_params) + """;
      Array.from(document.querySelectorAll('input[name], select[name]')).forEach(control => {
        if (params[control.name] !== undefined) {
          control.value = params[control.name];
          control.dispatchEvent(new Event('input', { bubbles: true }));
          control.dispatchEvent(new Event('change', { bubbles: true }));
        }
      });

      const button = document.querySelector('button[type=submit]');
      if (!button) return 'submit button not found';
      button.click();
      return 'submitted';
    })()
    """
    return eval_browser(fill_js)


def first_keyword():
    output = eval_browser(
        "(() => { const r=document.querySelector('table#table-condition-search tbody tr');"
        " return JSON.stringify({firstKeyword:r ? r.innerText : ''}); })()"
    )
    return extract_json_object(output).get("firstKeyword", "")


def result_total():
    output = eval_browser(
        "(() => { const m=document.body.innerText.match(/搜索结果数:\\\\s*([^\\\\n]+)/);"
        " return JSON.stringify({total:m ? m[1] : ''}); })()"
    )
    value = extract_json_object(output).get("total", "")
    match = re.search(r"[\d,]+", value)
    return int(match.group(0).replace(",", "")) if match else 0


def scan_global_keywords(config):
    filter_params = config.get("filter_params", {})
    sort_config = config.get("sort", {})
    policy = config.get("scan_policy", {})
    max_pages = int(policy.get("max_pages", 5))
    wait_attempts = int(policy.get("wait_attempts", 12))
    wait_interval = float(policy.get("wait_interval_seconds", 2))

    print("Opening global Keyword Research page...")
    open_browser("https://www.sellersprite.com/v2/keyword-research")
    time.sleep(4)

    previous_first = first_keyword()
    submission = submit_global_search(filter_params, sort_config)
    if "submitted" not in submission:
        raise ValueError(f"Could not submit global keyword search: {submission}")

    state = wait_for_query_result(
        "",
        previous_first_keyword=previous_first,
        attempts=wait_attempts,
        interval=wait_interval,
    )
    if not state.get("ready"):
        raise ValueError(f"Global keyword results did not load: {state}")

    total = result_total()
    results = []
    seen_pages = set()
    pages_scanned = 0
    for page in range(1, max_pages + 1):
        page_items = extract_json_array(eval_browser(SCRAPE_KEYWORDS_JS))
        signature = json.dumps(page_items, ensure_ascii=False, sort_keys=True)
        if not page_items or signature in seen_pages:
            break
        seen_pages.add(signature)
        results.extend(page_items)
        if total:
            results = results[:total]
        pages_scanned += 1
        print(f"Scraped {len(page_items)} global keywords on page {page}.")

        if page == max_pages or (total and len(results) >= total):
            break
        previous_first = first_keyword()
        click_result = eval_browser("""
        (() => {
          const button = document.querySelector('button.btn-next')
            || document.querySelector('.pagination .next a')
            || document.querySelector('.pagination li:last-child a');
          if (!button || button.disabled || button.classList.contains('is-disabled')) return 'not found';
          button.click();
          return 'clicked';
        })()
        """)
        if "clicked" not in click_result:
            break
        state = wait_for_query_result(
            "",
            previous_first_keyword=previous_first,
            attempts=wait_attempts,
            interval=wait_interval,
        )
        if not state.get("ready"):
            break

    time.sleep(wait_interval)
    final_total = result_total() or total
    if final_total:
        results = results[:final_total]
    return results, pages_scanned, final_total


def clean_cell(value):
    return str(value or "-").replace("\n", " <br> ").replace("|", "\\|").strip()


def generate_report(config_path, config, keywords, pages_scanned, total, date_str):
    params = config.get("filter_params", {})
    report_path = RESULTS_DIR / "keywords" / f"keyword_scan_report_{date_str}.md"
    os.makedirs(report_path.parent, exist_ok=True)

    md = [
        f"# 亚马逊全局关键词扫描报告 ({date_str.replace('_', '-')})\n",
        "> [!IMPORTANT]",
        f"> 本报告使用 `{config_path}` 对 SellerSprite 全局关键词库进行独立扫描，没有使用任何候选类目或种子词限制。",
        f"> 当前过滤条件共返回 **{total or len(keywords)}** 个关键词；扫描 **{pages_scanned}** 页，报告收录 **{len(keywords)}** 个。",
        f"> 排序：购买率降序。规则：一般性市场，月搜索量 ≥ {params.get('minSearches', 'N/A')}，月购买量 ≥ {params.get('minPurchases', 'N/A')}，购买率 ≥ {params.get('minPurchaseRate', 'N/A')}%，增长率 ≥ {params.get('minGrowth', 'N/A')}%，价格 ${params.get('minAvgPrice', 'N/A')}-${params.get('maxAvgPrice', 'N/A')}，商品数 ≤ {params.get('maxProducts', 'N/A')}，需供比 ≥ {params.get('minSupplyDemandRatio', 'N/A')}，最大点击集中度 ≤ {params.get('maxMonopolyClickRate', 'N/A')}%，最大 Reviews ≤ {params.get('maxAvgReviews', 'N/A')}，最大标题密度 ≤ {params.get('maxTitleDensity', 'N/A')}，最大 SPR ≤ {params.get('maxSPR', 'N/A')}，最大竞价 ≤ ${params.get('maxBid', 'N/A')}。\n",
        "| 序号 | 关键词 | 月搜索量 | 月购买量 / 购买率 | 月点击量 | 增长率 | 点击集中度 | 需供比 / 商品数 | PPC竞价 | 平均价格 / Reviews | 详情 |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for index, keyword in enumerate(keywords, 1):
        md.append(
            f"| {index} | **{clean_cell(keyword.get('keyword'))}** | "
            f"{clean_cell(keyword.get('searches'))} | {clean_cell(keyword.get('purchases'))} | "
            f"{clean_cell(keyword.get('clicks'))} | {clean_cell(keyword.get('growth'))} | "
            f"{clean_cell(keyword.get('monopoly'))} | {clean_cell(keyword.get('products'))} | "
            f"{clean_cell(keyword.get('bid'))} | {clean_cell(keyword.get('price_reviews'))} | "
            f"{clean_cell(keyword.get('details'))} |"
        )

    with report_path.open("w", encoding="utf-8") as file:
        file.write("\n".join(md))
    print(f"Report successfully written to {report_path}")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="Amazon Global Keyword Scan Script")
    parser.add_argument("--config", default="scripts/keyword_config.json")
    parser.add_argument("--date", default="", help="Date override YYYY_MM_DD")
    args = parser.parse_args()
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")

    with open(args.config, encoding="utf-8") as file:
        config = json.load(file)
    keywords, pages_scanned, total = scan_global_keywords(config)
    generate_report(args.config, config, keywords, pages_scanned, total, date_str)


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Scan failed: {exc}")
