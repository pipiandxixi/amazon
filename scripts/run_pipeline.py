#!/usr/bin/env python3
"""Run the full Amazon sourcing pipeline with in-memory stage handoffs."""

from __future__ import annotations

import argparse
import datetime
import json
import re
import time
from pathlib import Path

import find_asin_keywords as asin_scan
import find_products as product_scan
import select_market as market_scan
from scan_common import OpenCliError, check_browser_ready, dated_results_dir, eval_browser, extract_json_array, open_browser


GREEN = "🟢 Green (Recommended)"
YELLOW = "🟡 Yellow (Cautious)"


def _stage_json_path(root: Path, stage: int, date_str: str) -> Path:
    return root / "json" / f"stage{stage}_handoff_{date_str}.json"


def _write_stage_json(root: Path, stage: int, date_str: str, data: dict) -> None:
    path = _stage_json_path(root, stage, date_str)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[STAGE {stage} JSON] {path}")


def _read_stage_json(root: Path, stage: int, date_str: str) -> dict:
    path = _stage_json_path(root, stage, date_str)
    if not path.exists():
        raise FileNotFoundError(
            f"Stage {stage} handoff file not found: {path}\n"
            f"Run from stage {stage - 1} or earlier to generate it first."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    print(f"[STAGE {stage} JSON] Loaded: {path}")
    return data


def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


def run_products(
    config: dict,
    categories: list[dict],
    date_str: str,
) -> tuple[list[dict], list[str]]:
    policy = values(config.get("scan_policy", {}))
    filters = values(config["filters"])

    open_browser("https://www.sellersprite.com/v3/product-research")
    time.sleep(float(policy.get("page_wait_seconds", 5)))

    all_products: list[dict] = []
    product_sections: list[str] = []
    for entry in categories:
        name = entry.get("en_name") or entry.get("zh_name") or "unknown"
        path = entry.get("product_path") or product_scan._parse_path(entry.get("path", ""))
        print(f"\n[PRODUCT CATEGORY] {name}")
        try:
            product_scan.select_category(path, policy.get("only_leaf_category_rank", True))
            product_scan.apply_filters(filters)
            time.sleep(float(policy.get("wait_seconds", 5)))
            if policy.get("hide_variants", True):
                product_scan.hide_variants()
                time.sleep(3)
            state = product_scan.inspect_result_state()
            products = product_scan.scrape_products(int(policy.get("max_products", 50)))
            for item in products:
                item["_category_name"] = name
            all_products.extend(products)
            product_sections.append(product_scan.format_report(
                config, products, date_str, category_name=name, category_path=path,
                batch_total=len(categories), include_principles=False,
                market_entry=entry, result_state=state,
            ))
        except ValueError as exc:
            print(f"  [ERROR] {name}: {exc}")
        open_browser("https://www.sellersprite.com/v3/product-research")
        time.sleep(float(policy.get("page_wait_seconds", 5)))
    return all_products, product_sections


def run_asin_keywords(config: dict, products: list[dict], date_str: str) -> list[str]:
    from collections import defaultdict
    policy = values(config.get("scan_policy", {}))
    limit = int(policy.get("max_keywords", 20))
    max_asins = int(policy.get("max_asins", 5))
    page_wait = float(policy.get("page_wait_seconds", 8))

    def priority(product: dict) -> float:
        def number(value) -> float:
            match = re.search(r"[\d,.]+", str(value or ""))
            return float(match.group(0).replace(",", "")) if match else 0.0
        sales = number(product.get("monthly_sales"))
        reviews = number(product.get("reviews"))
        margin = number(product.get("profit_margin"))
        return sales / (reviews + 10) + margin / 10

    by_category: dict[str, list[dict]] = defaultdict(list)
    for p in products:
        by_category[p.get("_category_name", "unknown")].append(p)

    keyword_sections: list[str] = []
    for cat_name, cat_products in by_category.items():
        seen: set[str] = set()
        asins: list[str] = []
        for p in sorted(cat_products, key=priority, reverse=True):
            asin = p.get("asin", "")
            if asin and asin not in seen:
                seen.add(asin)
                asins.append(asin)
            if len(asins) >= max_asins:
                break
        if not asins:
            continue
        print(f"\n[CATEGORY KEYWORDS] {cat_name}: {asins}")
        asin_scan.open_extend_page(asins)
        time.sleep(page_wait)
        print(f"  Query: {asin_scan.submit_extend_query()}")
        time.sleep(page_wait)
        print(f"  Expand: {asin_scan.click_expand_keywords()}")
        time.sleep(page_wait)
        filter_result = asin_scan.apply_extend_filters(values(config.get("filters", {})))
        print(f"  Filters: {filter_result}")
        time.sleep(page_wait)
        state = asin_scan.inspect_result_state()
        raw = extract_json_array(eval_browser(asin_scan.SCRAPE_JS))
        items = asin_scan.rank_keywords(raw, values(config.get("score_weights", {})))[:limit]
        keyword_sections.append(asin_scan.format_report(asins, cat_name, items, raw, config, date_str, state))
        print(f"  {len(items)} of {len(raw)} keywords collected for {cat_name}")
    return keyword_sections


def write_combined_report(
    root: Path,
    date_str: str,
    market_content: str,
    product_sections: list[str],
    keyword_sections: list[str],
) -> Path:
    """Write the single pipeline report from in-memory stage content."""
    output = root / f"pipeline_report_{date_str}.md"
    sections = [
        f"# 亚马逊选品完整流水线报告 ({date_str.replace('_', '-')})",
        "",
        "> 本文件汇总市场扫描、全部候选类目商品扫描和动态商品 ASIN 关键词反查结果。",
        "",
        "---",
        "",
        market_content.strip(),
        "",
    ]
    for content in product_sections:
        sections.extend(["---", "", content.strip(), ""])
    for content in keyword_sections:
        sections.extend(["---", "", content.strip(), ""])
    output.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    total = 1 + len(product_sections) + len(keyword_sections)
    print(f"\n[COMBINED REPORT] {total} sections -> {output}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/pipeline_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument("--skip-asin-keywords", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Validate and summarize config without opening SellerSprite")
    parser.add_argument(
        "--start-from", type=int, choices=[1, 2, 3], default=1, metavar="{1,2,3}",
        help="Resume from this stage using the previous stage's handoff JSON (default: 1 = full run)",
    )
    args = parser.parse_args()

    if args.start_from == 3 and args.skip_asin_keywords:
        raise SystemExit("Error: --start-from 3 and --skip-asin-keywords are mutually exclusive")

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    root = dated_results_dir(date_str)
    levels = set(values(config.get("pipeline", {})).get("candidate_levels", [GREEN, YELLOW]))
    if "category" in config["products"]:
        raise ValueError("Unified config must not predefine a dynamic product category")
    if args.dry_run:
        print(f"Config: {args.config}")
        print(f"Candidate levels: {sorted(levels)}")
        print(f"Product price: ${values(config['products']['filters']).get('min_price')}+")
        print(f"ASIN reverse limit: {values(config['asin_keywords']['scan_policy']).get('max_asins')}")
        print("Dynamic fields validated: no product category or ASIN")
        return

    # Browser is needed unless we skip all browser stages
    if not (args.start_from == 3 and args.skip_asin_keywords):
        check_browser_ready()

    # ── Stage 1: Market Scan ─────────────────────────────────────────────────
    if args.start_from <= 1:
        raw_categories, scan_meta = market_scan.scrape_market(config["market"])
        market_content, candidates = market_scan.generate_report(
            config["market"], raw_categories, date_str, output_dir=root,
            scan_meta=scan_meta, return_candidates=True, write_report_file=False,
        )
        candidates = [item for item in candidates if item.get("level") in levels]
        if not candidates:
            raise ValueError("Market scan produced no downstream candidate categories")
        _write_stage_json(root, 1, date_str, {
            "market_content": market_content,
            "candidates": candidates,
        })
        print(f"\n[HANDOFF] market -> products: {len(candidates)} categories in memory")
    else:
        data = _read_stage_json(root, 1, date_str)
        market_content = data["market_content"]
        candidates = data["candidates"]
        print(f"[RESUME] Stage 1: {len(candidates)} candidate categories loaded")

    # ── Stage 2: Product Scan ────────────────────────────────────────────────
    if args.start_from <= 2:
        products, product_sections = run_products(config["products"], candidates, date_str)
        if not products:
            raise ValueError("All dynamic candidate categories returned zero qualified products")
        _write_stage_json(root, 2, date_str, {
            "products": products,
            "product_sections": product_sections,
        })
        print(f"\n[HANDOFF] products -> ASIN reverse: {len(products)} products in memory")
    else:
        data = _read_stage_json(root, 2, date_str)
        products = data["products"]
        product_sections = data["product_sections"]
        print(f"[RESUME] Stage 2: {len(products)} products loaded")

    # ── Stage 3: ASIN Keyword Lookup ─────────────────────────────────────────
    keyword_sections: list[str] = []
    if not args.skip_asin_keywords:
        keyword_sections = run_asin_keywords(config["asin_keywords"], products, date_str)

    write_combined_report(root, date_str, market_content, product_sections, keyword_sections)


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Pipeline failed: {exc}")
