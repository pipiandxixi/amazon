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


def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


def run_products(
    config: dict,
    categories: list[dict],
    date_str: str,
    output_dir: Path,
) -> list[dict]:
    policy = values(config.get("scan_policy", {}))
    filters = values(config["filters"])

    output_dir.mkdir(parents=True, exist_ok=True)
    product_scan.write_principles_file(config, output_dir, date_str)
    open_browser("https://www.sellersprite.com/v3/product-research")
    time.sleep(float(policy.get("page_wait_seconds", 5)))

    all_products: list[dict] = []
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
            product_scan.write_report(
                config, products, date_str, category_name=name, category_path=path,
                batch_total=len(categories),
                output_dir=output_dir, include_principles=False,
                market_entry=entry, result_state=state,
            )
        except ValueError as exc:
            print(f"  [ERROR] {name}: {exc}")
        open_browser("https://www.sellersprite.com/v3/product-research")
        time.sleep(float(policy.get("page_wait_seconds", 5)))
    return all_products


def run_asin_keywords(config: dict, products: list[dict], date_str: str) -> None:
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
        report = asin_scan.write_report(asins, cat_name, items, raw, config, date_str, state)
        print(f"  Wrote {len(items)} of {len(raw)} keywords to {report}")


def write_combined_report(root: Path, date_str: str) -> Path:
    """Combine human-readable stage reports into one review file."""
    output = root / f"pipeline_report_{date_str}.md"
    market_reports = sorted(root.glob("market_scan_report*.md"))
    product_reports = sorted((root / "products").glob("*.md"))
    asin_reports = sorted(root.glob("category_keywords_*.md"))
    sources = market_reports + product_reports + asin_reports

    sections = [
        f"# 亚马逊选品完整流水线报告 ({date_str.replace('_', '-')})",
        "",
        "> 本文件汇总市场扫描、全部候选类目商品扫描和动态商品 ASIN 关键词反查结果。",
        "> 各阶段独立报告仍保留用于审计。",
        "",
    ]
    for source in sources:
        relative = source.relative_to(root)
        sections.extend([
            "---",
            "",
            f"<!-- source: {relative} -->",
            source.read_text(encoding="utf-8").strip(),
            "",
        ])
    output.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    print(f"\n[COMBINED REPORT] {len(sources)} reports -> {output}")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/pipeline_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument("--skip-asin-keywords", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Validate and summarize config without opening SellerSprite")
    args = parser.parse_args()

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

    check_browser_ready()
    raw_categories, scan_meta = market_scan.scrape_market(config["market"])
    _, candidates = market_scan.generate_report(
        config["market"], raw_categories, date_str, output_dir=root,
        scan_meta=scan_meta, return_candidates=True,
    )
    candidates = [item for item in candidates if item.get("level") in levels]
    if not candidates:
        raise ValueError("Market scan produced no downstream candidate categories")
    print(f"\n[HANDOFF] market -> products: {len(candidates)} categories in memory")
    products = run_products(config["products"], candidates, date_str, root / "products")
    print(f"\n[HANDOFF] products -> ASIN reverse: {len(products)} products in memory")
    if not products:
        raise ValueError("All dynamic candidate categories returned zero qualified products")
    if not args.skip_asin_keywords:
        run_asin_keywords(config["asin_keywords"], products, date_str)
    write_combined_report(root, date_str)


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Pipeline failed: {exc}")
