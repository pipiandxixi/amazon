#!/usr/bin/env python3
"""Amazon sourcing pipeline — per-category incremental processing.

Stage 1: Market scan → merge results into results/json/categories.json
Stage 2+3: Per-category loop (products + keywords) ordered by staleness;
           categories.json and HTML are updated after each category.
"""

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
CATEGORIES_DB = "categories.json"


# ── DB helpers ───────────────────────────────────────────────────────────────

def _db_path(root: Path) -> Path:
    return root / "json" / CATEGORIES_DB


def load_db(root: Path) -> dict:
    p = _db_path(root)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def save_db(root: Path, db: dict) -> None:
    p = _db_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def merge_market_into_db(root: Path, candidates: list[dict]) -> dict:
    """Upsert Stage 1 candidates into categories.json, preserving existing products/keywords."""
    db = load_db(root)
    for cat in candidates:
        name = cat["en_name"]
        existing = db.get(name, {})
        db[name] = {
            **cat,
            "products": existing.get("products"),
            "keywords": existing.get("keywords"),
            "last_updated": existing.get("last_updated"),
        }
    save_db(root, db)
    print(f"[DB] {len(candidates)} candidates merged → {len(db)} total in {CATEGORIES_DB}")
    return db


# ── Config helper ─────────────────────────────────────────────────────────────

def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


# ── Stage 1: Market Scan ──────────────────────────────────────────────────────

def _scan_all_departments(market_config: dict) -> tuple[list[dict], dict]:
    """Run one market scan per department in scan_groups; aggregate unique results."""
    scan_groups: list[str] = values(market_config.get("scan_policy", {})).get("scan_groups", [])
    if not scan_groups:
        print("[MARKET] No scan_groups configured, running single scan")
        return market_scan.scrape_market(market_config)

    all_raw: list[dict] = []
    seen_niches: set[str] = set()
    total_pages = 0
    any_truncation = False

    for i, dept_label in enumerate(scan_groups, 1):
        print(f"\n[MARKET GROUP {i}/{len(scan_groups)}] department={dept_label!r}")
        raw, meta = market_scan.scrape_market(market_config, department_label=dept_label)
        total_pages += meta.get("pages_scanned", 0)
        if meta.get("possible_truncation"):
            any_truncation = True
        added = 0
        for item in raw:
            key = market_scan.clean_name(item.get("niche", ""))
            if key and key not in seen_niches:
                seen_niches.add(key)
                all_raw.append(item)
                added += 1
        print(f"  → {added} new unique categories (total so far: {len(all_raw)})")

    print(f"\n[MARKET] {len(scan_groups)} group scans → {len(all_raw)} unique categories total")
    combined_meta = {
        "pages_scanned": total_pages,
        "stop_reason": f"{len(scan_groups)} 批次扫描完成",
        "possible_truncation": any_truncation,
        "reported_total": None,
        "free_limit_message": False,
    }
    return all_raw, combined_meta


# ── Stage 2+3: Per-category loop ─────────────────────────────────────────────

def _priority(product: dict) -> float:
    def num(value) -> float:
        m = re.search(r"[\d,.]+", str(value or ""))
        return float(m.group(0).replace(",", "")) if m else 0.0
    return num(product.get("monthly_sales")) / (num(product.get("reviews")) + 10) + num(product.get("profit_margin")) / 10


def process_categories_loop(
    db: dict,
    root: Path,
    products_config: dict,
    keywords_config: dict,
    date_str: str,
    max_categories: int | None = None,
    skip_keywords: bool = False,
) -> None:
    """Process categories one at a time (products → keywords), saving DB + HTML after each.

    Categories are ordered by staleness: never-scanned first, then oldest last_updated.
    """
    import generate_html_report as _html_gen

    def sort_key(cat: dict) -> str:
        lu = cat.get("last_updated")
        return lu if lu else ""

    to_process = sorted(db.values(), key=sort_key)
    if max_categories:
        to_process = to_process[:max_categories]

    print(f"\n[LOOP] {len(to_process)} categories to process (ordered by staleness)")

    prod_policy = values(products_config.get("scan_policy", {}))
    prod_filters = values(products_config["filters"])
    kw_policy = values(keywords_config.get("scan_policy", {}))
    kw_filters = values(keywords_config.get("filters", {}))
    kw_weights = values(keywords_config.get("score_weights", {}))
    max_asins = int(kw_policy.get("max_asins", 20))
    kw_limit = int(kw_policy.get("max_keywords", 20))
    page_wait = float(kw_policy.get("page_wait_seconds", 8))
    prod_page_wait = float(prod_policy.get("page_wait_seconds", 5))

    open_browser("https://www.sellersprite.com/v3/product-research")
    time.sleep(prod_page_wait)

    seen_nodes: set[str] = set()
    processed = 0

    for i, cat in enumerate(to_process, 1):
        name = cat["en_name"]
        last = cat.get("last_updated", "从未")
        print(f"\n[{i}/{len(to_process)}] {name}  (上次更新: {last})")

        path = cat.get("product_path") or product_scan._parse_path(cat.get("path", ""))

        # ── Products ──────────────────────────────────────────────────────────
        products: list[dict] = []
        try:
            actual_node = product_scan.select_category(path, prod_policy.get("only_leaf_category_rank", True))
            if actual_node in seen_nodes:
                print(f"  [SKIP] nav-fallback collision: '{actual_node}' — marking as attempted")
                # Still timestamp so this category isn't repeatedly re-selected as stale
                db[name]["products"] = []
                db[name]["keywords"] = None
                db[name]["last_updated"] = datetime.datetime.now().isoformat(timespec="seconds")
                save_db(root, db)
                open_browser("https://www.sellersprite.com/v3/product-research")
                time.sleep(prod_page_wait)
                processed += 1
                continue
            seen_nodes.add(actual_node)
            product_scan.apply_filters(prod_filters)
            time.sleep(float(prod_policy.get("wait_seconds", 5)))
            if prod_policy.get("hide_variants", True):
                product_scan.hide_variants()
                time.sleep(3)
            products = product_scan.scrape_products(int(prod_policy.get("max_products", 50)))
        except ValueError as exc:
            print(f"  [PRODUCT ERROR] {exc}")

        # ── Keywords ──────────────────────────────────────────────────────────
        keywords: dict | None = None
        if products and not skip_keywords:
            asins: list[str] = []
            seen_asins: set[str] = set()
            for p in sorted(products, key=_priority, reverse=True):
                a = p.get("asin", "")
                if a and a not in seen_asins:
                    seen_asins.add(a)
                    asins.append(a)
                if len(asins) >= max_asins:
                    break

            if asins:
                preview = asins[:5]
                print(f"  Keywords for: {preview}{'...' if len(asins) > 5 else ''}")
                asin_scan.open_extend_page(asins)
                time.sleep(page_wait)
                print(f"  Query: {asin_scan.submit_extend_query()}")
                time.sleep(page_wait)
                print(f"  Expand: {asin_scan.click_expand_keywords()}")
                time.sleep(page_wait)
                print(f"  Filters: {asin_scan.apply_extend_filters(kw_filters)}")
                time.sleep(page_wait)
                raw = extract_json_array(eval_browser(asin_scan.SCRAPE_JS))
                items = asin_scan.rank_keywords(raw, kw_weights)[:kw_limit]
                keywords = {"asins": asins, "keywords": items}
                print(f"  {len(items)} keywords collected")

        # ── Persist ───────────────────────────────────────────────────────────
        db[name]["products"] = products
        db[name]["keywords"] = keywords
        db[name]["last_updated"] = datetime.datetime.now().isoformat(timespec="seconds")
        save_db(root, db)

        # ── Update HTML ───────────────────────────────────────────────────────
        _html_gen.generate_from_db(root, db, date_str)

        processed += 1

        # Navigate back for next category
        open_browser("https://www.sellersprite.com/v3/product-research")
        time.sleep(prod_page_wait)

    print(f"\n[LOOP] Done — {processed} categories updated")


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/pipeline_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument("--skip-keywords", action="store_true", help="Skip ASIN keyword lookup (Stage 3)")
    parser.add_argument("--dry-run", action="store_true", help="Validate config without opening SellerSprite")
    parser.add_argument(
        "--start-from", type=int, choices=[1, 2], default=1, metavar="{1,2}",
        help="1=full run (market scan + categories loop); 2=skip market scan, use existing categories.json",
    )
    parser.add_argument(
        "--stop-after", type=int, choices=[1, 2], default=2, metavar="{1,2}",
        help="1=stop after market scan (inspect DB before processing); 2=full run (default)",
    )
    parser.add_argument(
        "--max-categories", type=int, default=None, metavar="N",
        help="Process at most N categories per run (ordered by staleness). Omit for all.",
    )
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
        print(f"ASIN limit: {values(config['asin_keywords']['scan_policy']).get('max_asins')}")
        print("Dynamic fields validated: no product category or ASIN")
        return

    check_browser_ready()

    pipeline_start = time.time()

    def _elapsed(since: float) -> str:
        s = int(time.time() - since)
        return f"{s // 60}m{s % 60:02d}s"

    # ── Stage 1: Market Scan ─────────────────────────────────────────────────
    t1 = time.time()
    if args.start_from <= 1:
        raw_categories, scan_meta = _scan_all_departments(config["market"])
        _, candidates = market_scan.generate_report(
            config["market"], raw_categories, date_str, output_dir=root,
            scan_meta=scan_meta, return_candidates=True, write_report_file=False,
        )
        candidates = [c for c in candidates if c.get("level") in levels]
        if not candidates:
            raise ValueError("Market scan produced no candidate categories")
        db = merge_market_into_db(root, candidates)
        print(f"[HANDOFF] {len(candidates)} candidates merged into {CATEGORIES_DB}")
    else:
        db = load_db(root)
        if not db:
            raise FileNotFoundError(f"{CATEGORIES_DB} not found — run from stage 1 first")
        print(f"[RESUME] Loaded {len(db)} categories from {CATEGORIES_DB}")
    print(f"[TIMER] Stage 1 耗时: {_elapsed(t1)}  (累计 {_elapsed(pipeline_start)})")

    if args.stop_after == 1:
        scanned = sum(1 for c in db.values() if c.get("last_updated"))
        never = len(db) - scanned
        print(f"\n[PAUSE] Stage 1 完成 — {len(db)} 类目 ({never} 待扫描, {scanned} 已有数据)")
        print("检查 results/json/categories.json 后运行 --start-from 2 继续。")
        return

    # ── Stage 2+3: Per-category loop ─────────────────────────────────────────
    t2 = time.time()
    process_categories_loop(
        db, root,
        config["products"],
        config["asin_keywords"],
        date_str,
        max_categories=args.max_categories,
        skip_keywords=args.skip_keywords,
    )
    print(f"[TIMER] 类目循环耗时: {_elapsed(t2)}  (累计 {_elapsed(pipeline_start)})")
    print(f"\n[TIMER] Pipeline 总耗时: {_elapsed(pipeline_start)}")


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError, FileNotFoundError) as exc:
        raise SystemExit(f"Pipeline failed: {exc}")
