#!/usr/bin/env python3
"""Reverse-search one ASIN and output advertising keyword candidates."""

from __future__ import annotations

import argparse
import datetime
import json
import re
import time
from pathlib import Path

from scan_common import OpenCliError, dated_results_dir, eval_browser, extract_json_array, open_browser


SCRAPE_JS = """
(() => {
  // traffic/extend/asin page: single unified table, 17 columns
  // Col layout: 0=checkbox, 1=#, 2=keyword+translation, 3=流量占比,
  //   4=相关ASIN, 5=月搜索趋势(chart), 6=ABA周排名, 7=月搜索量,
  //   8=月购买量+购买率, 9=展示量+点击量, 10=SPR, 11=标题密度,
  //   12=需供比+商品数, 13=广告竞品数, 14=ABA集中度, 15=PPC竞价, 16=操作
  const tables = Array.from(document.querySelectorAll('table'));
  const dataTable = tables.find(t => {
    const row = t.querySelector('tbody tr');
    return row && row.querySelectorAll('td').length >= 10;
  });
  if (!dataTable) return JSON.stringify([]);
  const rows = Array.from(dataTable.querySelectorAll('tbody tr'));
  return JSON.stringify(rows.map(row => {
    const c = Array.from(row.querySelectorAll('td')).map(td => td.innerText.trim());
    const kwLines = (c[2] || '').split('\\n').filter(Boolean);
    const searchLines = (c[7] || '').split('\\n').filter(Boolean);
    const purchaseLines = (c[8] || '').split('\\n').filter(Boolean);
    const supplyLines = (c[12] || '').split('\\n').filter(Boolean);
    const ppcLines = (c[15] || '').split('\\n').filter(Boolean);
    return {
      keyword: kwLines[0] || '',
      translation: kwLines.slice(1).join(' / '),
      traffic_share: (c[3] || '').split('\\n')[0],
      aba_rank: c[6] || '',
      searches: searchLines[0] || '',
      purchases: purchaseLines[0] || '',
      purchase_rate: purchaseLines[1] || '',
      spr: c[10] || '',
      title_density: c[11] || '',
      supply_products: supplyLines[1] || supplyLines[0] || '',
      ad_competitors: c[13] || '',
      ppc_bid: ppcLines[0] || '',
      organic_rank: '',
      traffic_type: '',
    };
  }).filter(x => x.keyword));
})()
"""


def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


def open_extend_page(asins: list[str]) -> None:
    """Navigate to the traffic-extend batch page with the given ASINs pre-loaded."""
    q = ",".join(asins)
    open_browser(f"https://www.sellersprite.com/v3/traffic/extend/asin?q={q}&marketId=1&date=")


def submit_extend_query() -> str:
    """Click 立即查询 on the traffic-extend page to trigger the search."""
    return eval_browser(
        """
        (() => {
          const btn = Array.from(document.querySelectorAll('button')).find(
            x => x.innerText.includes('立即查询') && !x.disabled
          );
          if (!btn) return 'button not found';
          btn.click();
          return 'submitted';
        })()
        """
    )


def click_expand_keywords() -> str:
    """Click 用畅销变体拓词 to load the keyword results table.

    After 立即查询, the extend page shows variant-selection buttons before loading
    any keyword table. This step is required to trigger the actual keyword fetch.
    """
    return eval_browser(
        """
        (() => {
          const btn = Array.from(document.querySelectorAll('button')).find(
            x => x.innerText.includes('用畅销变体拓词') && x.offsetParent !== null
          );
          if (!btn) return 'button not found';
          btn.click();
          return 'clicked: ' + btn.innerText.trim();
        })()
        """
    )


def inspect_result_state() -> dict:
    output = eval_browser(
        """
        (() => {
          const tables = Array.from(document.querySelectorAll('table'));
          const keywordTable = tables.find(t => {
            const row = t.querySelector('tbody tr');
            const cells = row ? Array.from(row.querySelectorAll('td')) : [];
            return cells.length >= 2 && /[a-zA-Z]/.test(cells[1]?.innerText || '');
          });
          const visibleItems = keywordTable?.querySelectorAll('tbody tr').length || 0;
          const text = document.body.innerText;
          const totalMatch = text.match(/(?:共|总计|总共)\\s*([\\d,]+)\\s*(?:条|个)/);
          const nextBtn = document.querySelector('button.btn-next, .pagination .next a, .el-pagination .btn-next');
          const parent = nextBtn?.closest('li, button');
          const nextAvailable = !!nextBtn && !nextBtn.disabled
            && nextBtn.getAttribute('aria-disabled') !== 'true'
            && !parent?.classList.contains('disabled');
          return JSON.stringify({
            visible_items: visibleItems,
            reported_total: totalMatch ? Number(totalMatch[1].replaceAll(',', '')) : null,
            next_available: nextAvailable,
            free_limit_message: text.includes('当前的会员版本无法查看全部结果')
              || text.includes('请升级套餐后使用'),
            metrics_available: !!tables.find(t => {
              const row = t.querySelector('tbody tr');
              return row && row.querySelectorAll('td').length >= 18 && row.innerText.includes('%');
            })
          });
        })()
        """
    )
    start = output.find("{")
    end = output.rfind("}")
    return json.loads(output[start:end + 1])


def number(value: str) -> float:
    match = re.search(r"[\d,.]+", value or "")
    return float(match.group(0).replace(",", "")) if match else 0


def last_number(value: str) -> float:
    matches = re.findall(r"[\d,.]+", value or "")
    return float(matches[-1].replace(",", "")) if matches else 0


def filter_keywords(
    items: list[dict[str, str]], filters: dict
) -> list[dict[str, str]]:
    allowed_types = set(filters.get("allowed_traffic_types", []))
    excluded = [word.lower() for word in filters.get("excluded_keywords", [])]
    filtered = []
    for item in items:
        searches = number(item["searches"])
        purchases = number(item["purchases"])
        organic_rank = number(item["organic_rank"])
        spr = number(item["spr"])
        title_density = number(item["title_density"])
        products = last_number(item["supply_products"])
        ppc_bid = last_number(item["ppc_bid"])
        keyword_lower = item["keyword"].lower()
        if any(word in keyword_lower for word in excluded):
            continue
        if filters.get("require_numeric_searches", True) and searches <= 0:
            continue
        if searches < float(filters.get("min_searches", 0)):
            continue
        if purchases < float(filters.get("min_purchases", 0)):
            continue
        if organic_rank > float(filters.get("max_organic_rank", float("inf"))):
            continue
        if spr > float(filters.get("max_spr", float("inf"))):
            continue
        if title_density > float(filters.get("max_title_density", float("inf"))):
            continue
        if products > float(filters.get("max_products", float("inf"))):
            continue
        if ppc_bid > float(filters.get("max_ppc_bid", float("inf"))):
            continue
        if allowed_types and item["traffic_type"] and item["traffic_type"] not in allowed_types:
            continue
        filtered.append(item)
    return filtered


def rank_keywords(
    items: list[dict[str, str]], weights: dict
) -> list[dict[str, str]]:
    for item in items:
        searches = number(item["searches"])
        traffic = number(item["traffic_share"])
        purchases = number(item["purchases"])
        organic_rank = number(item["organic_rank"])
        item["ad_score"] = round(
            min(searches / 1000, float(weights.get("max_search_score", 10)))
            * float(weights.get("searches_per_1000", 2))
            + min(
                traffic * float(weights.get("traffic_share", 1)),
                float(weights.get("max_traffic_score", 30)),
            )
            + min(
                purchases / 20 * float(weights.get("purchases_per_20", 1)),
                float(weights.get("max_purchase_score", 10)),
            )
            + (
                float(weights.get("top_50_organic_bonus", 10))
                if 0 < organic_rank <= 50
                else 0
            ),
            2,
        )
    return sorted(items, key=lambda x: x["ad_score"], reverse=True)


def format_report(
    asins: list[str], category_name: str,
    items: list[dict[str, str]], raw_items: list[dict[str, str]], config: dict,
    date_str: str, result_state: dict,
) -> str:
    """Return the markdown content string for a category keyword report."""
    raw_count = len(raw_items)
    reported_total = result_state.get("reported_total")
    possible_truncation = (
        result_state.get("next_available", False)
        or (reported_total is not None and reported_total > raw_count)
        or result_state.get("free_limit_message", False)
    )
    asins_str = ", ".join(f"`{a}`" for a in asins)
    md = [
        f"# {category_name} 拓展流量词候选 ({date_str.replace('_', '-')})",
        "",
        f"> 查询 ASIN：{asins_str}",
        "> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，",
        "> 用于生成广告测试候选，不代表应直接使用高竞价投放。",
        f"> 筛选参数：`{json.dumps(values(config['filters']), ensure_ascii=False)}`",
        f"> 原始关键词 **{raw_count}** 个，过滤后保留 **{len(items)}** 个。",
        f"> 抓取完整性：页面可见 **{result_state.get('visible_items', 0)}** 个；"
        f"页面总数提示 **{reported_total if reported_total is not None else '未识别'}**；"
        f"下一页 **{'可用' if result_state.get('next_available') else '不可用或未识别'}**；"
        f"免费套餐截断风险：**{'可能存在' if possible_truncation else '未检测到'}**。",
        f"> 指标可用性：**{'可用' if result_state.get('metrics_available') else '不可用'}**。"
        "若指标不可用，过滤后 0 条不能解释为没有关键词机会。",
        "",
        "| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |",
        "|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|",
    ]
    for index, item in enumerate(items, 1):
        clean = {k: str(v).replace("|", "\\|").replace("\n", " / ") for k, v in item.items()}
        md.append(
            f"| {index} | **{clean['keyword']}**<br>{clean['translation']} | "
            f"{clean['traffic_share']} | {clean['traffic_type']} | {clean['organic_rank']} | "
            f"{clean['searches']} | {clean['purchases']} | {clean['spr']} | "
            f"{clean['title_density']} | {clean['supply_products']} | {clean['ppc_bid']} | "
            f"{clean['ad_score']} |"
        )
    md.extend(["", f"## 免费套餐当前可见原始关键词（查询 ASIN: {', '.join(asins)}）", ""])
    for index, item in enumerate(raw_items, 1):
        translation = item.get("translation", "").replace("\n", " / ")
        md.append(f"{index}. **{item['keyword']}**" + (f" — {translation}" if translation else ""))
    return "\n".join(md) + "\n"


def write_report(
    asins: list[str], category_name: str,
    items: list[dict[str, str]], raw_items: list[dict[str, str]], config: dict,
    date_str: str, result_state: dict,
) -> Path:
    slug = re.sub(r"[^a-z0-9]+", "_", category_name.lower()).strip("_")
    path = dated_results_dir(date_str) / f"category_keywords_{slug}_{date_str}.md"
    path.write_text(format_report(asins, category_name, items, raw_items, config, date_str, result_state), encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("asins", nargs="+", help="One or more Amazon ASINs (up to 20)")
    parser.add_argument("--category", default="", help="Category name for the output filename")
    parser.add_argument("--config", default="scripts/asin_keyword_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--wait-seconds", type=float)
    args = parser.parse_args()
    asins = [a.strip().upper() for a in args.asins]
    for a in asins:
        if not re.fullmatch(r"[A-Z0-9]{10}", a):
            raise SystemExit(f"Invalid ASIN: {a} (must be 10 letters/numbers)")
    if len(asins) > 20:
        raise SystemExit("Maximum 20 ASINs per query")
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    policy = values(config.get("scan_policy", {}))
    limit = args.limit or int(policy.get("max_keywords", 20))
    page_wait = (
        args.wait_seconds
        if args.wait_seconds is not None
        else float(policy.get("page_wait_seconds", 8))
    )
    category_name = args.category or "_".join(asins)
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")

    open_extend_page(asins)
    time.sleep(page_wait)
    print(f"Query: {submit_extend_query()}")
    time.sleep(page_wait)
    print(f"Expand: {click_expand_keywords()}")
    time.sleep(page_wait)
    result_state = inspect_result_state()
    raw_items = extract_json_array(eval_browser(SCRAPE_JS))
    filtered_items = filter_keywords(raw_items, values(config.get("filters", {})))
    items = rank_keywords(filtered_items, values(config.get("score_weights", {})))[:limit]
    report = write_report(asins, category_name, items, raw_items, config, date_str, result_state)
    print(f"Wrote {len(items)} of {len(raw_items)} keywords to {report}")


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ASIN keyword scan failed: {exc}")
