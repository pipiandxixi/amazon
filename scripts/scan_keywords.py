#!/usr/bin/env python3
"""Multi-mode keyword research scanner for SellerSprite (/v2/keyword-research)."""

from __future__ import annotations

import argparse
import datetime
import json
import re
import time
from pathlib import Path

from scan_common import RESULTS_DIR, OpenCliError, check_browser_ready, eval_browser, open_browser, extract_json_object

KEYWORD_RESULTS_DIR = RESULTS_DIR / "keywords"

# Actual column headers observed from /v2/keyword-research table (as of 2026-06):
#  col_0: ''                     (checkbox)
#  col_1: '#'                    (row index)
#  col_2: '关键词'               keyword (may include Chinese translation)
#  col_3: '展示10条相关产品'     action button — skip
#  col_4: '搜索量趋势'           sparkline — skip
#  col_5: '月搜索量'             monthly searches (integer)
#  col_6: '月购买量 购买率'      compound: "N,NNN\nM.M%" purchases + purchase_rate
#  col_7: '展示量 点击量'        compound: impressions + clicks — skip
#  col_8: '增长率'               recent growth rate (%)
#  col_9: '同比增长 近3月增长'   compound: "YoY%\n3m%" or values
#  col_10: 'ABA 集中度'          ABA concentration = monopoly click rate (%)
#  col_11: 'ABA 排名'            ABA rank — skip
#  col_12: '货流值'              goods flow value (%)
#  col_13: 'PPC竞价 精准 词组 精准 广泛'  compound bid prices — take first $N.NN
#  col_14: '需供比 商品数'       compound: SPR + products count
#  col_15: '市场分析'            action — skip
#  col_16: '操作'                action — skip


def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


# ---------------------------------------------------------------------------
# Page interaction
# ---------------------------------------------------------------------------

def open_keyword_page(station: str, month: str) -> None:
    """Open the keyword research page and optionally select station/month."""
    open_browser("https://www.sellersprite.com/v2/keyword-research")
    time.sleep(5)

    if station and station != "美国":
        station_js = f"""
        (() => {{
          const target = {json.dumps(station)};
          const el = Array.from(document.querySelectorAll('a, li, span, label'))
            .find(x => x.offsetParent !== null && x.innerText.trim() === target);
          if (el) {{ el.click(); return 'clicked: ' + target; }}
          return 'station not found: ' + target;
        }})()
        """
        result = eval_browser(station_js)
        print(f"  Station selection: {result}")
        time.sleep(2)

    if month:
        month_js = f"""
        (() => {{
          const target = {json.dumps(month)};
          const opts = Array.from(document.querySelectorAll(
            '.el-select-dropdown__item, option, li, span'
          )).filter(x => x.offsetParent !== null && x.innerText.trim() === target);
          if (opts.length) {{ opts[0].click(); return 'selected: ' + target; }}
          return 'month option not found: ' + target;
        }})()
        """
        # Try to open the month dropdown first
        eval_browser("""
        (() => {
          const el = Array.from(document.querySelectorAll('*'))
            .find(x => x.offsetParent !== null && x.innerText.trim().startsWith('选择月份'));
          if (el) el.click();
        })()
        """)
        time.sleep(1)
        result = eval_browser(month_js)
        print(f"  Month selection: {result}")
        time.sleep(2)


def select_departments(department_numbers: list[int]) -> None:
    """
    Check the given department checkboxes and uncheck all others.
    departments[1] is '全部类目' (any) — always uncheck it first so it
    doesn't override individual selections.
    """
    # Validate: refuse to include 1 (全部类目) — it overrides all others
    safe = [n for n in department_numbers if n != 1]
    if not safe:
        raise ValueError("departments list must contain at least one specific category (not 1=全部类目)")
    js = f"""
    (() => {{
      const enabled = new Set({json.dumps(safe)});
      let checked = 0, unchecked = 0, errors = [];
      // Always uncheck the "any" checkbox first (departments[1])
      const anyCb = document.querySelector('input[name="departments[1]"]');
      if (anyCb && anyCb.checked) {{ anyCb.click(); unchecked++; }}
      document.querySelectorAll('input[name^="departments["]').forEach(cb => {{
        const m = cb.name.match(/departments\[(\d+)\]/);
        if (!m) return;
        const n = parseInt(m[1]);
        if (n === 1) return;  // already handled above
        if (enabled.has(n) && !cb.checked) {{ cb.click(); checked++; }}
        else if (!enabled.has(n) && cb.checked) {{ cb.click(); unchecked++; }}
      }});
      const actualChecked = Array.from(
        document.querySelectorAll('input[name^="departments["]:checked')
      ).map(cb => cb.name);
      return JSON.stringify({{checked, unchecked, active: actualChecked}});
    }})()
    """
    result = eval_browser(js)
    print(f"  Departments: {result}")
    # Verify at least one specific category is selected
    try:
        data = json.loads(result[result.find('{'):result.rfind('}')+1])
        if not data.get("active"):
            raise OpenCliError("No department was successfully selected — check department numbers in config")
    except (ValueError, json.JSONDecodeError):
        pass  # JS returned non-JSON; evaluation already printed above


def fill_and_submit(filter_params: dict) -> str:
    """Fill named filter inputs and click 开始筛选. Returns submission status."""
    params_json = json.dumps({k: str(v) for k, v in filter_params.items() if v != ""})
    js = f"""
    (() => {{
      const params = {params_json};
      const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      let filled = 0;
      Array.from(document.querySelectorAll('input[name]')).forEach(input => {{
        if (params[input.name] !== undefined) {{
          setter.call(input, String(params[input.name]));
          input.dispatchEvent(new Event('input', {{ bubbles: true }}));
          input.dispatchEvent(new Event('change', {{ bubbles: true }}));
          filled++;
        }}
      }});
      const btn = Array.from(document.querySelectorAll('button'))
        .find(b => b.innerText.includes('开始筛选') && b.offsetParent !== null);
      if (btn) {{ btn.click(); return 'submitted (filled ' + filled + ' inputs)'; }}
      return 'submit button not found';
    }})()
    """
    return eval_browser(js)


def reset_filters() -> None:
    """Click 重置条件 to clear filter state between modes."""
    js = """
    (() => {
      const btn = Array.from(document.querySelectorAll('button'))
        .find(b => b.innerText.includes('重置') && b.offsetParent !== null);
      if (btn) { btn.click(); return 'reset'; }
      return 'reset button not found';
    })()
    """
    result = eval_browser(js)
    print(f"  Reset: {result}")
    time.sleep(2)


# ---------------------------------------------------------------------------
# Scraping
# ---------------------------------------------------------------------------

_SCRAPE_PAGE_JS = """
(() => {
  const table = document.querySelector('table#table-condition-search');
  if (!table) return JSON.stringify({headers: [], rows: [], loading: false});

  const loading = !!document.querySelector(
    '.el-loading-mask, .loading, [aria-busy="true"]'
  );

  const headers = Array.from(table.querySelectorAll('thead th'))
    .map(th => th.innerText.trim().replace(/\\s+/g, ' '));

  const rows = [];
  table.querySelectorAll('tbody tr').forEach(tr => {
    const cells = Array.from(tr.querySelectorAll('td'))
      .map(td => td.innerText.trim().replace(/\\s+/g, ' '));
    if (cells.length >= 2) rows.push(cells);
  });

  return JSON.stringify({headers, rows, loading});
})()
"""


def scrape_one_page() -> tuple[list[str], list[list[str]], bool]:
    """Return (headers, rows, loading) from the current page."""
    output = eval_browser(_SCRAPE_PAGE_JS, timeout=30)
    data = extract_json_object(output)
    return data.get("headers", []), data.get("rows", []), data.get("loading", False)


def click_next_page() -> str:
    """Click the next-page button. Returns 'clicked' or 'not found'."""
    js = """
    (() => {
      const btn = document.querySelector('button.btn-next')
        || document.querySelector('.pagination .next a')
        || document.querySelector('.pagination li:last-child a');
      if (btn && !btn.disabled && !btn.classList.contains('disabled')) {
        btn.click();
        return 'clicked';
      }
      return 'not found';
    })()
    """
    return eval_browser(js)


def scrape_mode(
    mode_name: str,
    max_pages: int,
    wait_seconds: float,
) -> tuple[list[str], list[dict]]:
    """
    Scrape all pages for the current mode.
    Returns (headers, keyword_rows) where each row is a dict of col→raw_text.
    """
    print(f"  Waiting {wait_seconds}s for initial load...")
    time.sleep(wait_seconds)

    all_rows: list[dict] = []
    seen_signatures: set[str] = set()
    headers: list[str] = []

    for page in range(1, max_pages + 1):
        print(f"  Scraping page {page}/{max_pages}...")

        # Poll until loading spinner disappears (up to 30s)
        hdrs, rows, loading = [], [], True
        for _ in range(15):
            hdrs, rows, loading = scrape_one_page()
            if not loading:
                break
            time.sleep(2)
        else:
            print(f"  Page {page}: loading timed out, skipping.")
            break

        if hdrs and not headers:
            headers = hdrs
            print(f"  Detected columns: {headers}")

        if not rows:
            print("  No rows found, stopping pagination.")
            break

        sig = json.dumps(rows, ensure_ascii=False, sort_keys=True)
        if sig in seen_signatures:
            print("  Duplicate page detected, stopping pagination.")
            break
        seen_signatures.add(sig)

        for row_cells in rows:
            row_dict = {"_mode": mode_name}
            for i, cell in enumerate(row_cells):
                row_dict[f"col_{i}"] = cell
                if headers and i < len(headers):
                    row_dict[headers[i]] = cell
            all_rows.append(row_dict)

        print(f"  Page {page}: +{len(rows)} rows (total {len(all_rows)})")

        if page < max_pages:
            click_res = click_next_page()
            if click_res == "not found":
                print("  No next page button, done.")
                break
            time.sleep(3)

    return headers, all_rows


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _parse_number(text: str) -> float:
    """Extract the first number (int or float) from a text string."""
    if not text:
        return 0.0
    clean = re.sub(r"[,$%]", "", text)
    m = re.search(r"\d[\d,]*(?:\.\d+)?", clean)
    if not m:
        return 0.0
    return float(m.group().replace(",", ""))


def _parse_pct(text: str) -> float:
    """Extract the first percentage value (digits before %) from a text string."""
    if not text:
        return 0.0
    m = re.search(r"([\d,]+(?:\.\d+)?)\s*%", text)
    if not m:
        return 0.0
    return float(m.group(1).replace(",", ""))


def _parse_first_dollar(text: str) -> float:
    """Extract the first $N.NN value from a text string."""
    if not text:
        return 0.0
    m = re.search(r"\$([\d,]+(?:\.\d+)?)", text)
    if not m:
        return 0.0
    return float(m.group(1).replace(",", ""))


def _col(row: dict, header: str, index: int) -> str:
    """Return cell by header name first, fall back to positional col_N."""
    return row.get(header, "") or row.get(f"col_{index}", "")


def parse_keyword_row(row: dict) -> dict:
    """
    Convert a raw row dict into a typed keyword record.
    Uses actual column layout observed from /v2/keyword-research.
    """
    raw_keyword = _col(row, "关键词", 2)
    # Strip appended Chinese translation (e.g. "yoga mat 瑜伽垫" → "yoga mat")
    keyword = re.sub(r"\s+[一-龥][^\s]*.*$", "", raw_keyword).strip()
    if not keyword:
        keyword = raw_keyword.strip()

    raw_searches = _col(row, "月搜索量", 5)

    # '月购买量 购买率': compound cell — last % is the purchase rate
    raw_purchase_cell = _col(row, "月购买量 购买率", 6)
    purchase_rate = _parse_pct(raw_purchase_cell)

    # '增长率': single growth % (recent trend)
    raw_growth_rate = _col(row, "增长率", 8)
    growth_3m_rate = _parse_pct(raw_growth_rate) if "%" in raw_growth_rate else _parse_number(raw_growth_rate)

    # '同比增长 近3月增长': compound — two numbers/percentages
    raw_growth_compound = _col(row, "同比增长 近3月增长", 9)
    growth_parts = re.findall(r"[-\d,]+(?:\.\d+)?%?", raw_growth_compound)
    growth_yoy_rate = _parse_number(growth_parts[0]) if len(growth_parts) > 0 else 0.0
    growth_3m_val = int(_parse_number(growth_parts[1])) if len(growth_parts) > 1 else 0

    # 'ABA 集中度': ABA concentration = monopoly click rate
    raw_monopoly = _col(row, "ABA 集中度", 10)
    monopoly_click_rate = _parse_pct(raw_monopoly) if "%" in raw_monopoly else _parse_number(raw_monopoly)

    # 'PPC竞价 精准 词组 精准 广泛': first dollar amount
    raw_bid_cell = _col(row, "PPC竞价 精准 词组 精准 广泛", 13)
    bid = _parse_first_dollar(raw_bid_cell) if raw_bid_cell else 0.0

    # '需供比 商品数': first number = SPR, second = products
    raw_spr_products = _col(row, "需供比 商品数", 14)
    spr_parts = re.findall(r"[\d,]+(?:\.\d+)?", raw_spr_products)
    spr = int(_parse_number(spr_parts[0])) if spr_parts else 0
    products = int(_parse_number(spr_parts[1])) if len(spr_parts) > 1 else 0

    # Word count: calculated from English keyword text
    word_count = len(keyword.split()) if keyword else 0

    return {
        "keyword": keyword,
        "monthly_searches": int(_parse_number(raw_searches)),
        "growth_3m_val": growth_3m_val,
        "growth_3m_rate": growth_3m_rate,
        "growth_yoy_rate": growth_yoy_rate,
        "purchase_rate": purchase_rate,
        "monopoly_click_rate": monopoly_click_rate,
        "spr": spr,
        "avg_price": 0.0,
        "avg_reviews": 0,
        "bid": bid,
        "word_count": word_count,
        "products": products,
        "mode": row.get("_mode", ""),
    }


# ---------------------------------------------------------------------------
# Merge & deduplicate
# ---------------------------------------------------------------------------

def merge_deduplicate(results_per_mode: list[list[dict]]) -> list[dict]:
    """
    Flatten all mode results, deduplicate by keyword text (case-insensitive),
    keeping the first occurrence.
    """
    seen: dict[str, dict] = {}
    for mode_results in results_per_mode:
        for kw in mode_results:
            key = kw["keyword"].lower().strip()
            if key and key not in seen:
                seen[key] = kw
    return list(seen.values())


# ---------------------------------------------------------------------------
# Risk classification
# ---------------------------------------------------------------------------

def classify_keyword(kw: dict, risk_rules: dict) -> tuple[str, list[str]]:
    """
    Returns (level, reasons) where level is one of:
      '🔴 Red (Avoid)', '🟡 Yellow (Cautious)', '🟢 Green (Recommended)'
    """
    red = risk_rules.get("red", {})
    yellow = risk_rules.get("yellow", {})

    def get_rule(rules: dict, key: str) -> float:
        v = rules.get(key, {})
        if isinstance(v, dict):
            return float(v.get("value", 0))
        return float(v) if v else 0.0

    red_reasons: list[str] = []
    yellow_reasons: list[str] = []

    # --- Red rules ---
    max_mono_red = get_rule(red, "max_monopoly_click_rate")
    if max_mono_red and kw["monopoly_click_rate"] > max_mono_red:
        red_reasons.append(f"点击集中度过高 (>{max_mono_red:.0f}%)")

    max_bid_red = get_rule(red, "max_bid")
    if max_bid_red and kw["bid"] > max_bid_red:
        red_reasons.append(f"CPC过高 (>${max_bid_red:.1f})")

    if red_reasons:
        return "🔴 Red (Avoid)", red_reasons

    # --- Yellow rules ---
    max_mono_yellow = get_rule(yellow, "max_monopoly_click_rate")
    if max_mono_yellow and kw["monopoly_click_rate"] > max_mono_yellow:
        yellow_reasons.append(f"点击集中度偏高 (>{max_mono_yellow:.0f}%)")

    max_bid_yellow = get_rule(yellow, "max_bid")
    if max_bid_yellow and kw["bid"] > max_bid_yellow:
        yellow_reasons.append(f"CPC偏高 (>${max_bid_yellow:.1f})")

    min_purchase_yellow = get_rule(yellow, "min_purchase_rate")
    if min_purchase_yellow and 0 < kw["purchase_rate"] < min_purchase_yellow:
        yellow_reasons.append(f"购买率偏低 (<{min_purchase_yellow:.1f}%)")

    if yellow_reasons:
        return "🟡 Yellow (Cautious)", yellow_reasons

    return "🟢 Green (Recommended)", []


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(
    config: dict,
    keywords: list[dict],
    mode_summaries: list[dict],
    date_str: str,
    output_dir: Path | None = None,
) -> str:
    scan_policy = values(config.get("scan_policy", {}))
    target_min = int(scan_policy.get("target_candidate_min", 15))
    target_max = int(scan_policy.get("target_candidate_max", 50))

    green = [k for k in keywords if k["level"] == "🟢 Green (Recommended)"]
    yellow = [k for k in keywords if k["level"] == "🟡 Yellow (Cautious)"]
    red = [k for k in keywords if k["level"] == "🔴 Red (Avoid)"]

    candidate_count = len(green) + len(yellow)
    if candidate_count > target_max:
        audit = (
            f"当前候选关键词有 {candidate_count} 个，超过目标上限 {target_max}。"
            "建议收紧各模式的 risk_rules 阈值，或减少启用的模式。"
        )
    elif candidate_count < target_min:
        audit = (
            f"当前候选关键词仅有 {candidate_count} 个，低于目标下限 {target_min}。"
            "建议放宽过滤参数，或增加类目覆盖范围。"
        )
    else:
        audit = f"当前候选关键词有 {candidate_count} 个，位于目标区间 {target_min}-{target_max}。"

    md: list[str] = []
    md.append(f"# 亚马逊关键词选品扫描报告 ({date_str.replace('_', '-')})\n")
    md.append("> [!IMPORTANT]")
    md.append(
        f"> 本报告基于 `scripts/keyword_config.json` 中的过滤配置与风控规则生成。"
        f"共执行 **{len(mode_summaries)}** 个扫描模式，去重后得到 **{len(keywords)}** 条关键词，"
        f"其中绿色推荐 **{len(green)}** 条。"
    )
    md.append(f"> **数量审计**：{audit}")
    md.append(
        "> 报告数据直接来自卖家精灵页面抓取，无人工猜测。"
        "可将绿色/黄色关键词复制到大模型中进一步分析选品机会。\n"
    )

    # Mode summary
    md.append("## 一、扫描模式执行摘要\n")
    md.append("| 模式 | 状态 | 抓取条数 | 说明 |")
    md.append("| :--- | :--- | ---: | :--- |")
    for s in mode_summaries:
        status_icon = "✅" if s["success"] else "⏭️ 已跳过" if not s["enabled"] else "❌ 失败"
        md.append(f"| **{s['name']}** | {status_icon} | {s['count']} | {s['note']} |")
    md.append("")

    # Overview
    md.append("## 二、风控分类结果概览\n")
    md.append(f"- **绿色通道 (推荐) 🟢**：共 **{len(green)}** 条。所有风控指标通过，建议重点关注。")
    md.append(f"- **黄色通道 (谨慎) 🟡**：共 **{len(yellow)}** 条。存在竞争偏高或 CPC 偏贵，建议深入调研。")
    md.append(f"- **红色通道 (避坑) 🔴**：共 **{len(red)}** 条。触发硬风控规则，已自动排除。\n")

    # Green summary table
    md.append("## 三、推荐与候选关键词核心列表\n")
    md.append("### 1. 🟢 绿色推荐关键词\n")
    md.append("| 序号 | 关键词 | 月搜索量 | 近3月增长率 | 购买率 | 点击集中度 | CPC | 词数 | 来源模式 |")
    md.append("| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |")
    for i, k in enumerate(green, 1):
        md.append(
            f"| {i} | **{k['keyword']}** | {k['monthly_searches']:,} | "
            f"{k['growth_3m_rate']:.1f}% | {k['purchase_rate']:.1f}% | "
            f"{k['monopoly_click_rate']:.1f}% | ${k['bid']:.2f} | {k['word_count']} | {k['mode']} |"
        )

    # Yellow summary table
    md.append("\n### 2. 🟡 黄色候选关键词\n")
    md.append("| 序号 | 关键词 | 月搜索量 | 近3月增长率 | 购买率 | 点击集中度 | CPC | 触发警示 |")
    md.append("| :--- | :--- | ---: | ---: | ---: | ---: | ---: | :--- |")
    for i, k in enumerate(yellow, 1):
        reasons = ", ".join(k["reasons"])
        md.append(
            f"| {i} | **{k['keyword']}** | {k['monthly_searches']:,} | "
            f"{k['growth_3m_rate']:.1f}% | {k['purchase_rate']:.1f}% | "
            f"{k['monopoly_click_rate']:.1f}% | ${k['bid']:.2f} | {reasons} |"
        )

    # Red summary table
    md.append("\n### 3. 🔴 红色排除关键词摘要\n")
    md.append("| 序号 | 关键词 | 月搜索量 | 排除原因 |")
    md.append("| :--- | :--- | ---: | :--- |")
    for i, k in enumerate(red, 1):
        reasons = ", ".join(k["reasons"])
        md.append(f"| {i} | **{k['keyword']}** | {k['monthly_searches']:,} | {reasons} |")

    # Detailed profiles for green + yellow
    md.append("\n## 四、候选关键词详细数据画像（供大模型分析）\n")
    md.append(
        "以下为绿色与黄色关键词的完整数据指标，可直接输入大模型（如 Claude）进行深入分析。\n"
    )

    md.append("### 🟢 绿色关键词详情\n")
    for i, k in enumerate(green, 1):
        md.append(f"#### 🏆 🟢-{i}. {k['keyword']}\n")
        md.append(f"- **来源模式**：`{k['mode']}`")
        md.append(f"- **月搜索量**：`{k['monthly_searches']:,}`")
        md.append(f"- **近3月增长值**：`{k['growth_3m_val']:,}`")
        md.append(f"- **近3月增长率**：`{k['growth_3m_rate']:.1f}%`")
        md.append(f"- **同比增长率**：`{k['growth_yoy_rate']:.1f}%`")
        md.append(f"- **购买率**：`{k['purchase_rate']:.1f}%`")
        md.append(f"- **点击集中度**：`{k['monopoly_click_rate']:.1f}%`")
        md.append(f"- **SPR**：`{k['spr']}`")
        md.append(f"- **平均价格**：`${k['avg_price']:.2f}`")
        md.append(f"- **平均评分数**：`{k['avg_reviews']}`")
        md.append(f"- **PPC竞价**：`${k['bid']:.2f}`")
        md.append(f"- **词数**：`{k['word_count']}`")
        md.append(f"- **商品数**：`{k['products']}`")
        md.append("\n---\n")

    md.append("### 🟡 黄色关键词详情\n")
    for i, k in enumerate(yellow, 1):
        md.append(f"#### 🏆 🟡-{i}. {k['keyword']}\n")
        md.append(f"- **触发警示**：`{', '.join(k['reasons'])}`")
        md.append(f"- **来源模式**：`{k['mode']}`")
        md.append(f"- **月搜索量**：`{k['monthly_searches']:,}`")
        md.append(f"- **近3月增长值**：`{k['growth_3m_val']:,}`")
        md.append(f"- **近3月增长率**：`{k['growth_3m_rate']:.1f}%`")
        md.append(f"- **同比增长率**：`{k['growth_yoy_rate']:.1f}%`")
        md.append(f"- **购买率**：`{k['purchase_rate']:.1f}%`")
        md.append(f"- **点击集中度**：`{k['monopoly_click_rate']:.1f}%`")
        md.append(f"- **SPR**：`{k['spr']}`")
        md.append(f"- **平均价格**：`${k['avg_price']:.2f}`")
        md.append(f"- **平均评分数**：`{k['avg_reviews']}`")
        md.append(f"- **PPC竞价**：`${k['bid']:.2f}`")
        md.append(f"- **词数**：`{k['word_count']}`")
        md.append(f"- **商品数**：`{k['products']}`")
        md.append("\n---\n")

    # Pipeline mode (output_dir given): no date suffix — date is in the run dir name.
    # Standalone mode: date in filename so runs in results/keywords/ don't clash.
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "keyword_scan_report.md"
        sidecar_path = output_dir / "keyword_scan_results.json"
    else:
        KEYWORD_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        report_path = KEYWORD_RESULTS_DIR / f"keyword_scan_report_{date_str}.md"
        sidecar_path = KEYWORD_RESULTS_DIR / f"keyword_scan_results_{date_str}.json"

    report_path.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"Report written to {report_path}")

    sidecar_items = [
        {"keyword": k["keyword"], "monthly_searches": k["monthly_searches"], "mode": k["mode"], "level": k["level"]}
        for k in keywords
        if k["level"] in ("🟢 Green (Recommended)", "🟡 Yellow (Cautious)")
    ]
    sidecar_path.write_text(json.dumps(sidecar_items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"JSON sidecar written to {sidecar_path}")
    return str(report_path)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/keyword_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument("--output-dir", default="", dest="output_dir",
                        help="Directory to write report and sidecar (pipeline mode); "
                             "defaults to results/keywords/ with date-stamped filenames")
    parser.add_argument("--categories-file", default="", dest="categories_file",
                        help="JSON file from market scan (list of {en_name, departments}); "
                             "overrides config departments with the union of all candidate departments")
    args = parser.parse_args()

    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))

    station = config.get("station", "美国")
    month = config.get("month", "")
    # Dept 1 = "全部类目" — always excluded by select_departments(); safe fallback uses all specific depts 2-23
    departments: list[int] = config.get("departments", list(range(2, 24)))

    if args.categories_file:
        cats_path = Path(args.categories_file)
        if not cats_path.exists():
            raise SystemExit(f"--categories-file not found: {cats_path}")
        cats_data = json.loads(cats_path.read_text(encoding="utf-8"))
        merged_depts: set[int] = set()
        for entry in cats_data:
            for d in entry.get("departments", []):
                if isinstance(d, int) and d != 1:
                    merged_depts.add(d)
        if merged_depts:
            departments = sorted(merged_depts)
            print(f"--categories-file: overriding departments with {departments}")
    scan_policy = values(config.get("scan_policy", {}))
    max_pages = int(scan_policy.get("max_pages", 3))
    wait_seconds = float(scan_policy.get("wait_seconds", 6))
    modes: list[dict] = config.get("modes", [])

    check_browser_ready()
    print(f"Opening keyword research page (station={station}, month={month or 'default'})...")
    open_keyword_page(station, month)

    all_mode_results: list[list[dict]] = []
    mode_summaries: list[dict] = []

    for mode in modes:
        mode_name = mode.get("name", "unnamed")
        enabled = mode.get("enabled", True)

        if not enabled:
            print(f"\n[SKIP] Mode: {mode_name}")
            mode_summaries.append({"name": mode_name, "enabled": False, "success": False, "count": 0, "note": "已禁用"})
            continue

        print(f"\n[MODE] {mode_name}")
        filter_params = values(mode.get("filter_params", {}))

        print("  Resetting filters...")
        reset_filters()

        print("  Selecting departments...")
        select_departments(departments)
        time.sleep(1)

        print(f"  Filling params: {filter_params}")
        submit_result = fill_and_submit(filter_params)
        print(f"  Submit: {submit_result}")

        if "not found" in submit_result.lower():
            mode_summaries.append({"name": mode_name, "enabled": True, "success": False, "count": 0, "note": "提交按钮未找到"})
            continue

        headers, raw_rows = scrape_mode(mode_name, max_pages, wait_seconds)

        parsed: list[dict] = []
        for row in raw_rows:
            kw = parse_keyword_row(row)
            if kw["keyword"]:
                parsed.append(kw)

        print(f"  Parsed {len(parsed)} keywords for mode '{mode_name}'")
        all_mode_results.append(parsed)
        mode_summaries.append({
            "name": mode_name,
            "enabled": True,
            "success": True,
            "count": len(parsed),
            "note": f"过滤参数: {json.dumps(filter_params, ensure_ascii=False)}",
        })

    print(f"\nMerging and deduplicating across {len(all_mode_results)} modes...")
    merged = merge_deduplicate(all_mode_results)
    print(f"Total unique keywords after dedup: {len(merged)}")

    # Classify using the risk rules of the first mode that produced each keyword
    # (each keyword carries its source mode name; look up rules from that mode)
    mode_rules_map = {m["name"]: m.get("risk_rules", {}) for m in modes}

    for kw in merged:
        rules = mode_rules_map.get(kw["mode"], {})
        level, reasons = classify_keyword(kw, rules)
        kw["level"] = level
        kw["reasons"] = reasons

    output_dir = Path(args.output_dir) if args.output_dir else None
    report_path = generate_report(config, merged, mode_summaries, date_str, output_dir=output_dir)
    print(f"\nDone! Report: {report_path}")
    green_count = sum(1 for k in merged if k["level"] == "🟢 Green (Recommended)")
    print(f"Summary: {green_count} green / {len(merged)} total keywords")


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Keyword scan failed: {exc}")
