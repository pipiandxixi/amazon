#!/usr/bin/env python3
"""Find qualified products inside one exact SellerSprite leaf category."""

from __future__ import annotations

import argparse
import datetime
import json
import re
import time
from pathlib import Path

from scan_common import RESULTS_DIR, OpenCliError, check_browser_ready, eval_browser, extract_json_array, open_browser
from aggregate_top_picks import parse_product_file, score_product, write_top_picks

try:
    from deep_translator import GoogleTranslator as _GoogleTranslator
    def _translate_batch(texts: list[str]) -> list[str]:
        tr = _GoogleTranslator(source="en", target="zh-CN")
        return [tr.translate(t) or t for t in texts]
except ImportError:
    def _translate_batch(texts: list[str]) -> list[str]:  # type: ignore[misc]
        return [""] * len(texts)


INPUT_INDEXES = {
    "min_monthly_sales": 1,
    "max_monthly_sales": 2,
    "min_sales_growth": 7,
    "max_sales_growth": 8,
    "max_leaf_bsr": 12,
    "min_variants": 17,
    "max_variants": 18,
    "min_price": 19,
    "max_price": 20,
    "max_reviews": 24,
    "min_monthly_new_reviews": 25,
    "max_monthly_new_reviews": 26,
    "min_rating": 27,
    "max_rating": 28,
    "min_profit_margin": 33,
    "max_fba_fee": 32,
    "max_package_weight_g": 39,
    "min_sellers": 44,
    "max_sellers": 45,
}


def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


def select_category(path: list[str], only_leaf_rank: bool) -> None:
    output = eval_browser(
        """
        (() => {
          const trigger = Array.from(document.querySelectorAll('*')).find(
            x => x.children.length === 0 && x.textContent.trim() === '选择一个或多个类目和子类目'
          );
          if (!trigger) return 'category trigger not found';
          trigger.click();
          return 'opened';
        })()
        """
    )
    if "opened" not in output:
        raise ValueError(output)

    for index, category in enumerate(path):
        time.sleep(1)
        category_json = json.dumps(category)
        is_leaf = index == len(path) - 1
        output = eval_browser(
            f"""
            (() => {{
              const target = {category_json};
              const visible = Array.from(
                document.querySelectorAll('.category-tree .custom-tree-node .label')
              ).filter(
                x => x.textContent.trim().startsWith(target) && x.offsetParent !== null
              );
              if (!visible.length) return 'not found: ' + target;
              const content = visible[0].closest('.el-tree-node__content');
              if (!content) return 'row not found: ' + target;
              if ({str(is_leaf).lower()}) {{
                const checkbox = content.querySelector('input[type=checkbox]');
                if (!checkbox) return 'checkbox not found: ' + target;
                if (!checkbox.checked) checkbox.click();
              }} else {{
                const expand = content.querySelector('.el-tree-node__expand-icon');
                if (!expand) return 'expand control not found: ' + target;
                if (!expand.classList.contains('expanded')) expand.click();
              }}
              return 'clicked: ' + visible[0].textContent.trim();
            }})()
            """
        )
        if "clicked:" not in output:
            raise ValueError(
                f"Could not select category path item '{category}'. "
                "Open SellerSprite once and confirm the category tree is available."
            )

    output = eval_browser(
        """
        (() => {
          const confirm = Array.from(document.querySelectorAll('button')).find(
            x => x.innerText.includes('确认选择') && x.offsetParent !== null
          );
          if (!confirm) return 'confirm not found';
          confirm.click();
          return 'confirmed';
        })()
        """
    )
    if "confirmed" not in output:
        raise ValueError(output)
    time.sleep(2)

    if only_leaf_rank:
        eval_browser(
            """
            (() => {
              const x = document.querySelector('input[value="只看该子类目排名"]');
              if (x && !x.checked) x.click();
              return x ? x.checked : false;
            })()
            """
        )


def apply_filters(filters: dict[str, str]) -> None:
    indexed = {
        str(INPUT_INDEXES[key]): value
        for key, value in filters.items()
        if key in INPUT_INDEXES and value != ""
    }
    # Named inputs (e.g. includeKeywords) are filled by input[name=...] selector
    named = {
        key: value
        for key, value in filters.items()
        if key not in INPUT_INDEXES and key != "fulfillment" and value != ""
    }
    fba = filters.get("fulfillment") == "FBA"
    output = eval_browser(
        f"""
        (() => {{
          const indexed = {json.dumps(indexed)};
          const named = {json.dumps(named)};
          const inputs = Array.from(document.querySelectorAll('input'));
          const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
          for (const [index, value] of Object.entries(indexed)) {{
            const input = inputs[Number(index)];
            if (!input) return 'missing input index ' + index;
            setter.call(input, String(value));
            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
            input.dispatchEvent(new Event('change', {{ bubbles: true }}));
          }}
          for (const [name, value] of Object.entries(named)) {{
            const input = document.querySelector('input[name="' + name + '"]');
            if (input) {{
              setter.call(input, String(value));
              input.dispatchEvent(new Event('input', {{ bubbles: true }}));
              input.dispatchEvent(new Event('change', {{ bubbles: true }}));
            }}
          }}
          const fba = inputs.find(x => x.value === 'FBA');
          if (fba && fba.checked !== {str(fba).lower()}) fba.click();
          const submit = Array.from(document.querySelectorAll('button')).find(
            x => x.innerText.includes('开始筛选')
          );
          if (!submit) return 'submit not found';
          submit.click();
          return 'submitted';
        }})()
        """
    )
    if "submitted" not in output:
        raise ValueError(output)


def hide_variants() -> None:
    eval_browser(
        """
        (() => {
          const label = Array.from(document.querySelectorAll('label')).find(
            x => x.innerText.includes('展示所有变体')
          );
          const input = label?.querySelector('input');
          if (input?.checked) input.click();
          return input ? input.checked : null;
        })()
        """
    )


def scrape_products(limit: int) -> list[dict[str, str]]:
    output = eval_browser(
        f"""
        (() => {{
          const rows = Array.from(document.querySelectorAll('table tbody tr'));
          const products = [];
          for (let i = 0; i < rows.length && products.length < {limit}; i += 2) {{
            const main = rows[i]?.innerText || '';
            const detail = rows[i + 1]?.innerText || '';
            if (!main.includes('ASIN:')) continue;
            products.push({{ main, detail }});
          }}
          return JSON.stringify(products);
        }})()
        """
    )
    raw_products = extract_json_array(output)
    return [parse_product(item["main"], item["detail"]) for item in raw_products]


def parse_product(main: str, detail: str) -> dict[str, str]:
    lines = [line.strip() for line in main.splitlines() if line.strip()]
    asin = re.search(r"ASIN:\s*([A-Z0-9]+)", main)
    parent = re.search(r"父ASIN\s*:\s*([A-Z0-9]+)", main)
    brand = re.search(r"品牌:([^\n]+)", main)
    title_index = next((i for i, line in enumerate(lines) if "ASIN:" in line), 0)
    title = lines[title_index - 1] if title_index else ""
    brand_index = next((i for i, line in enumerate(lines) if line.startswith("品牌:")), -1)
    metrics = lines[brand_index + 1 :] if brand_index >= 0 else []
    value = lambda index: metrics[index] if len(metrics) > index else ""
    tail = lambda offset: metrics[offset] if len(metrics) >= abs(offset) else ""
    has_full_metrics = len(metrics) >= 21
    leaf_rank = re.search(r"#([\d,]+) in ([^\n]+)", detail)
    sellers = re.search(r"卖家:\s*(\d+)\s*家", detail)
    package_weight = re.search(r"包装重量:\s*(.+?)\s+包装尺寸:", detail)
    return {
        "asin": asin.group(1) if asin else "",
        "parent_asin": parent.group(1) if parent else "",
        "title": title,
        "brand": brand.group(1).strip() if brand else "",
        "monthly_sales": value(3),
        "sales_growth": value(4),
        "monthly_revenue": value(5),
        "variants": tail(-13) if has_full_metrics else value(7),
        "price": tail(-12) if has_full_metrics else value(8),
        "reviews": tail(-10) if has_full_metrics else value(10),
        "monthly_new_reviews": tail(-9) if has_full_metrics else value(11),
        "rating": tail(-8) if has_full_metrics else value(12),
        "review_rate": tail(-7) if has_full_metrics else value(13),
        "fba_fee": tail(-6) if has_full_metrics else value(14),
        "profit_margin": tail(-5) if has_full_metrics else "",
        "listing_date": tail(-4) if has_full_metrics else value(15),
        "listing_age": tail(-3) if has_full_metrics else value(16),
        "leaf_rank": leaf_rank.group(1) if leaf_rank else "",
        "leaf_category": leaf_rank.group(2).strip() if leaf_rank else "",
        "sellers": sellers.group(1) if sellers else "",
        "package_weight": package_weight.group(1).strip() if package_weight else "",
        "raw_metrics": " | ".join(metrics),
    }


_FILTER_RATIONALE: dict[str, str] = {
    "min_monthly_sales":       "确保产品有稳定市场需求，低于此销量视为市场过小",
    "max_monthly_sales":       "避开竞争过于激烈的大爆款，聚焦中等规模机会",
    "max_reviews":             "评价数低说明竞争护城河浅，新卖家仍有进入机会",
    "min_rating":              "过滤质量差评产品，只关注消费者认可的品类",
    "max_rating":              "评分上限（通常无需限制，保留作兜底）",
    "min_profit_margin":       "确保覆盖 FBA 费用、广告成本后仍有合理利润空间",
    "min_price":               "低价品利润薄、运营容错率低，过滤不符合要求的产品",
    "max_price":               "客单价过高会拉长消费者决策周期并增加资金压力",
    "max_package_weight_g":    "重量直接决定 FBA 头程和月租费，轻量化是新卖家核心竞争力",
    "max_sellers":             "卖家少说明市场未饱和，存在空白或新兴机会",
    "min_sellers":             "至少有一家卖家说明品类已有验证，排除无人做的死角",
    "min_variants":            "排除变体结构过于单一的产品",
    "max_variants":            "变体过多会拉高库存管理复杂度和资金占用",
    "max_fba_fee":             "FBA 费用直接影响毛利，设置上限保护利润",
    "max_leaf_bsr":            "小类 BSR 越小说明销量越靠前，限制范围聚焦头部产品",
    "fulfillment":             "FBA 配送是新卖家标准模式，确保物流体验和搜索权重",
}


def _explain_filters(config_filters: dict) -> list[str]:
    """Generate selection principle lines from raw config filter dict (with label/value)."""
    lines: list[str] = []
    for key, raw in config_filters.items():
        value = raw.get("value", raw) if isinstance(raw, dict) else raw
        label = raw.get("label", key) if isinstance(raw, dict) else key
        if value == "" or value is None:
            continue
        rationale = _FILTER_RATIONALE.get(key, "")
        suffix = f"　*{rationale}*" if rationale else ""
        lines.append(f"- **{label}** ≥/≤/= `{value}`{suffix}")
    return lines


_CN_NUMS = ["一", "二", "三", "四", "五", "六", "七"]


def _est_cogs(price_str: str, fba_fee_str: str, margin_str: str) -> str:
    """Estimate COGS from SellerSprite margin model: cogs = price*(1-margin) - fba_fee."""
    try:
        price = float(re.sub(r"[^0-9.]", "", price_str))
        fba = float(re.sub(r"[^0-9.]", "", fba_fee_str))
        margin = float(re.sub(r"[^0-9.]", "", margin_str)) / 100
        if price <= 0 or not (0 < margin < 1):
            return "-"
        cogs = price * (1 - margin) - fba
        ratio = cogs / price * 100
        return f"${cogs:.2f} ({ratio:.0f}%)"
    except (ValueError, ZeroDivisionError):
        return "-"


def _market_metric_str(entry: dict) -> str:
    """Format market metrics with qualitative labels based on risk thresholds."""
    def tag_reviews(v):
        if v <= 300:  return f"均Reviews {v}（低竞争）"
        if v <= 800:  return f"均Reviews {v}（中等）"
        return               f"均Reviews {v}（高竞争）"

    def tag_weight(v):
        if v <= 1.5:  return f"重量 {v:.2f}lbs（轻）"
        if v <= 2.0:  return f"重量 {v:.2f}lbs（偏重）"
        return               f"重量 {v:.2f}lbs（重）"

    def tag_return(v):
        if v <= 5:    return f"退货率 {v}%（低）"
        if v <= 8:    return f"退货率 {v}%（中）"
        return               f"退货率 {v}%（高）"

    def tag_brand(v):
        if v <= 40:   return f"品牌集中度 {v}%（分散）"
        if v <= 65:   return f"品牌集中度 {v}%（中等）"
        return               f"品牌集中度 {v}%（垄断）"

    parts = []
    if entry.get("price") is not None:
        parts.append(f"均价 ${entry['price']:.2f}")
    if entry.get("reviews") is not None:
        parts.append(tag_reviews(entry["reviews"]))
    if entry.get("weight_lbs") is not None:
        parts.append(tag_weight(entry["weight_lbs"]))
    if entry.get("return_rate") is not None:
        parts.append(tag_return(entry["return_rate"]))
    if entry.get("brand_conc") is not None:
        parts.append(tag_brand(entry["brand_conc"]))
    if entry.get("cn_ratio") is not None:
        parts.append(f"中国卖家 {entry['cn_ratio']}%")
    return "　".join(parts) if parts else "（指标不可用）"


def _short_title(title: str, max_len: int = 65) -> str:
    """Extract core product name: first segment before spec separators."""
    for sep in [" – ", " — ", " | ", ", ", " - "]:
        idx = title.find(sep)
        if 0 < idx <= max_len:
            return title[:idx]
    return title[:max_len].rstrip() + ("…" if len(title) > max_len else "")


def write_principles_file(config: dict, output_dir: Path, date_str: str) -> Path:
    """Write a shared scan_principles.md to output_dir (batch mode only)."""
    path = output_dir / "scan_principles.md"
    md = [
        f"# 选品原则 ({date_str.replace('_', '-')})\n",
        "本文件由批量产品扫描自动生成，同批次所有品类报告共享同一套筛选条件。\n",
        "本次产品扫描依据以下量化条件筛选候选商品，每项条件均有明确的选品逻辑：\n",
    ]
    for line in _explain_filters(config["filters"]):
        md.append(line)
    path.write_text("\n".join(md) + "\n", encoding="utf-8")
    return path


def write_report(
    config: dict,
    products: list[dict[str, str]],
    date_str: str,
    category_name: str | None = None,
    category_path: list[str] | None = None,
    uncovered_categories: list[dict] | None = None,
    batch_total: int = 0,
    output_dir: Path | None = None,
    include_principles: bool = True,
    market_entry: dict | None = None,
) -> Path:
    category = category_name or config["category"]["name"]
    cat_path = category_path or config["category"]["path"]
    slug = re.sub(r"[^a-z0-9]+", "_", category.lower()).strip("_")
    # Pipeline mode: filename is just the slug — date is encoded in the run directory.
    # Standalone mode: full prefix with date for disambiguation in results/.
    if output_dir:
        path = output_dir / f"{slug}.md"
    else:
        path = RESULTS_DIR / f"product_scan_{slug}_{date_str}.md"
    filters = values(config["filters"])
    short_titles = [_short_title(p["title"]) for p in products]
    print(f"  Translating {len(short_titles)} product names to Chinese...")
    zh_names = _translate_batch(short_titles)

    sec = iter(_CN_NUMS)

    md = [
        f"# {category} 合格产品扫描 ({date_str.replace('_', '-')})\n",
        f"> **所在品类路径**：`{' › '.join(cat_path)}`",
        f"> 共抓取 **{len(products)}** 个通过全部筛选条件的候选商品。\n",
    ]

    # --- 市场评估摘要（来源于市场扫描，说明为何选入此类目）---
    if market_entry:
        level = market_entry.get("level", "")
        md.append(f"> **市场评级**：{level}　{_market_metric_str(market_entry)}\n")

    # --- 选品原则 (inline in single mode; shared file referenced in batch mode) ---
    if include_principles:
        md.append(f"## {next(sec)}、选品原则\n")
        md.append("本次产品扫描依据以下量化条件筛选候选商品，每项条件均有明确的选品逻辑：\n")
        for line in _explain_filters(config["filters"]):
            md.append(line)
        md.append("")
    else:
        md.append("> 选品原则详见 [scan_principles.md](scan_principles.md)\n")

    # --- 候选商品列表 ---
    md.append(f"## {next(sec)}、候选商品列表\n")
    md += [
        "| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |",
        "|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|",
    ]
    for index, (product, short, zh) in enumerate(zip(products, short_titles, zh_names), 1):
        clean = {k: str(v).replace("|", "\\|").replace("\n", " ") for k, v in product.items()}
        short_clean = short.replace("|", "\\|")
        zh_clean = (zh or "").replace("|", "\\|")
        asin_link = f"[{clean['asin']}](https://www.amazon.com/dp/{clean['asin']})"
        cogs = _est_cogs(clean["price"], clean["fba_fee"], clean["profit_margin"])
        md.append(
            f"| {index} | {asin_link} | {zh_clean} | {short_clean} | "
            f"{clean['monthly_sales']} / {clean['sales_growth']} | {clean['monthly_revenue']} | "
            f"{clean['price']} | {cogs} | {clean['reviews']} / {clean['monthly_new_reviews']} | "
            f"{clean['rating']} | {clean['fba_fee']} / {clean['profit_margin']} | "
            f"{clean['variants']} | {clean['leaf_rank']} | {clean['sellers']} | "
            f"{clean['package_weight']} | {clean['listing_date']} {clean['listing_age']} |"
        )
    md.append("")

    # --- 完整标题 ---
    md.append(f"## {next(sec)}、完整商品标题\n")
    for index, product in enumerate(products, 1):
        asin_link = f"[{product['asin']}](https://www.amazon.com/dp/{product['asin']})"
        md.append(f"**{index}. {asin_link}** {product['title']}")
        md.append("")

    # --- 未分析类目 ---
    if uncovered_categories:
        md.append(f"## {next(sec)}、尚未分析的候选类目（共 {len(uncovered_categories)} 个）\n")
        md.append(
            "以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。"
            "可逐一修改 `product_config.json` 中的 `category.path` 后重新运行产品扫描，"
            "或使用 `find_products.py --categories-file` 批量扫描（需先确认类目路径格式与产品研究页面一致）。\n"
        )
        md.append("| 序号 | 英文名称 | 中文名称 | 完整路径 |")
        md.append("| ---: | --- | --- | --- |")
        for i, cat in enumerate(uncovered_categories, 1):
            en = cat.get("en_name", "")
            zh = cat.get("zh_name", "")
            p = cat.get("path", "")
            md.append(f"| {i} | {en} | {zh} | `{p}` |")
        md.append("")

    # --- 下一步建议 ---
    md.append(f"## {next(sec)}、下一步建议\n")
    md.append(
        "1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，"
        "在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。\n"
    )
    if batch_total > 1:
        coverage_msg = (
            f"本次批量扫描共处理 {batch_total} 个品类。"
            + (f"市场扫描还有 {len(uncovered_categories)} 个候选类目未覆盖，" if uncovered_categories else "")
            + "可增大 `pipeline.max_categories_to_products` 或重跑 pipeline 扩大覆盖范围。"
        )
    else:
        coverage_msg = (
            "本次只扫描了 1 个品类。"
            + (f"市场扫描共识别出 {len(uncovered_categories)} 个未分析的候选类目，" if uncovered_categories else "")
            + "建议按市场扫描报告中的绿色类目逐一更新 `product_config.json` → `category.path` 后重跑。"
        )
    md.append(f"2. **扩大类目覆盖**：{coverage_msg}\n")
    md.append(
        "3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，"
        "确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。\n"
    )
    md.append(
        "4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，"
        "在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。\n"
    )

    # --- 原始数值 ---
    md.append(f"## {next(sec)}、原始数值\n")
    for product in products:
        md.append(f"- `{product['asin']}`: {product['raw_metrics']}")

    path.write_text("\n".join(md) + "\n", encoding="utf-8")
    return path


def _parse_path(raw) -> list[str]:
    """Accept a path as list or ">"/›-separated string."""
    if isinstance(raw, list):
        return raw
    return [s.strip() for s in re.split(r'[>›]', str(raw)) if s.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/product_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument(
        "--output-dir", default="", dest="output_dir",
        help="Directory to write product report(s) (pipeline mode); "
             "defaults to results/ with date-stamped filenames",
    )
    parser.add_argument(
        "--keywords-file", default="", dest="keywords_file",
        help="JSON file with keyword string list; joined as includeKeywords filter",
    )
    parser.add_argument(
        "--categories-file", default="", dest="categories_file",
        help="JSON file with a list of category entries; triggers batch mode that scans "
             "each entry in sequence. Minimum fields: {en_name, path}. Pipeline mode "
             "supplies enriched entries with {product_path, departments, level} as well.",
    )
    parser.add_argument(
        "--market-sidecar", default="", dest="market_sidecar",
        help="market_scan_results JSON from select_market.py; used to compute the "
             "uncovered categories section in each report",
    )
    parser.add_argument(
        "--batch-size", type=int, default=0, dest="batch_size",
        help="Write top_picks.md after every N categories complete (0 = only at end). "
             "Requires --output-dir to be set.",
    )
    parser.add_argument(
        "--top-n", type=int, default=50, dest="top_n",
        help="Number of top picks to include in top_picks.md (default 50).",
    )
    args = parser.parse_args()
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    policy = values(config.get("scan_policy", {}))
    filters = values(config["filters"])
    output_dir = Path(args.output_dir) if args.output_dir else None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    # Load market sidecar for uncovered-categories context
    market_candidates: list[dict] = []
    if args.market_sidecar:
        ms_path = Path(args.market_sidecar)
        if ms_path.exists():
            market_candidates = json.loads(ms_path.read_text(encoding="utf-8"))

    # Apply keyword override from --keywords-file
    if args.keywords_file:
        kw_path = Path(args.keywords_file)
        if not kw_path.exists():
            raise SystemExit(f"--keywords-file not found: {kw_path}")
        kw_list: list[str] = json.loads(kw_path.read_text(encoding="utf-8"))
        filters["includeKeywords"] = ",".join(str(k) for k in kw_list if k)
        print(f"--keywords-file: includeKeywords = {filters['includeKeywords'][:80]}...")

    check_browser_ready()
    open_browser("https://www.sellersprite.com/v3/product-research")
    time.sleep(5)

    if args.categories_file:
        # Batch mode: scan each category from the file
        cats_path = Path(args.categories_file)
        if not cats_path.exists():
            raise SystemExit(f"--categories-file not found: {cats_path}")
        cats_data = json.loads(cats_path.read_text(encoding="utf-8"))
        print(f"Batch mode: {len(cats_data)} categories from {cats_path}")

        # Write shared principles file once for the whole batch
        principles_dir = output_dir if output_dir else RESULTS_DIR
        principles_path = write_principles_file(config, principles_dir, date_str)
        print(f"  Principles: {principles_path}")

        results_summary: list[str] = []
        scanned_names: set[str] = set()
        batch_total = len(cats_data)
        completed_count = 0

        def _flush_top_picks(label: str) -> None:
            if not output_dir:
                return
            md_files = sorted(f for f in output_dir.glob("*.md") if f.stem != "scan_principles")
            all_products: list[dict] = []
            cat_names: list[str] = []
            for f in md_files:
                cat_en, _, products = parse_product_file(f)
                cat_names.append(cat_en)
                for p in products:
                    p["_score"] = score_product(p)
                all_products.extend(products)
            if all_products:
                write_top_picks(output_dir.parent, all_products, cat_names, args.top_n, date_str, label)
                print(f"  [top_picks] {label}: {len(all_products)} products across {len(cat_names)} categories")

        for entry in cats_data:
            cat_name = entry.get("en_name", "") or entry.get("zh_name", "unknown")
            # Prefer pre-built product_path array (from pipeline enrichment);
            # fall back to splitting path string for standalone use.
            cat_path = entry.get("product_path") or _parse_path(entry.get("path", ""))
            if not cat_path:
                print(f"  [SKIP] No path for category: {cat_name}")
                continue
            print(f"\n[CATEGORY] {cat_name}")
            try:
                select_category(cat_path, policy.get("only_leaf_category_rank", True))
                apply_filters(filters)
                time.sleep(float(policy.get("wait_seconds", 5)))
                if policy.get("hide_variants", True):
                    hide_variants()
                    time.sleep(3)
                products = scrape_products(int(policy.get("max_products", 20)))
                scanned_names.add(cat_name.lower())
                uncovered = [
                    c for c in market_candidates
                    if c.get("en_name", "").lower() not in scanned_names
                ] if market_candidates else None
                mkt = next(
                    (c for c in market_candidates if c.get("en_name", "").lower() == cat_name.lower()),
                    None,
                )
                report = write_report(
                    config, products, date_str,
                    category_name=cat_name, category_path=cat_path,
                    uncovered_categories=uncovered, batch_total=batch_total,
                    output_dir=output_dir, include_principles=False,
                    market_entry=mkt,
                )
                print(f"  Wrote {len(products)} products to {report}")
                results_summary.append(f"  {cat_name}: {len(products)} products → {report}")
            except ValueError as exc:
                print(f"  [ERROR] {cat_name}: {exc}")
                results_summary.append(f"  {cat_name}: FAILED — {exc}")

            completed_count += 1
            if args.batch_size > 0 and completed_count % args.batch_size == 0:
                _flush_top_picks(f"第{completed_count // args.batch_size}批 {completed_count}/{batch_total}类目")

            # Reload page to reset state for next category
            open_browser("https://www.sellersprite.com/v3/product-research")
            time.sleep(5)

        # Final flush after all categories complete
        _flush_top_picks(f"{completed_count}/{batch_total}类目完成")

        print("\n=== Batch Summary ===")
        for line in results_summary:
            print(line)
    else:
        # Single category mode (original behavior)
        scanned_path = config["category"]["path"]
        select_category(scanned_path, policy.get("only_leaf_category_rank", True))
        apply_filters(filters)
        time.sleep(float(policy.get("wait_seconds", 5)))
        if policy.get("hide_variants", True):
            hide_variants()
            time.sleep(3)
        products = scrape_products(int(policy.get("max_products", 20)))
        # Uncovered = all market candidates except the one being scanned now
        scanned_name = config["category"]["name"].lower()
        uncovered = [
            c for c in market_candidates
            if c.get("en_name", "").lower() != scanned_name
        ] if market_candidates else None
        report = write_report(config, products, date_str,
                              uncovered_categories=uncovered, output_dir=output_dir)
        print(f"Wrote {len(products)} products to {report}")


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Product scan failed: {exc}")
