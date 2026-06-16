#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CATEGORY_POOL = ROOT / "category" / "category_opportunity_pool.json"
CATEGORY_MD = ROOT / "category" / "category_opportunity_pool.md"
PRODUCT_SCAN = ROOT / "products" / "scan_products.py"
PRODUCT_CONFIG = ROOT / "products" / "product_scan_config.json"
COMBINED_OUTPUT = ROOT / "products" / "combined_product_candidates.json"
TOP_OUTPUT = ROOT / "products" / "top_product_candidates.json"
INDEX_BUILDER = ROOT / "build_index.py"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def is_apparel_category(category: dict) -> bool:
    path = category.get("path", "")
    if path.startswith("Clothing, Shoes & Jewelry"):
        return True
    return "apparel_fit_return" in category.get("risk_flags", [])


def category_display(category: dict) -> str:
    name = category.get("name", "")
    name_zh = category.get("name_zh", "")
    return f"{name} / {name_zh}" if name_zh else name


def filter_category_pool(data: dict) -> tuple[dict, list[dict]]:
    target_pool = data.get("target_pool", [])
    removed = [item for item in target_pool if is_apparel_category(item)]
    kept = [item for item in target_pool if not is_apparel_category(item)]

    data = dict(data)
    data["target_pool"] = kept
    data["target_pool_count"] = len(kept)

    existing_excluded = data.get("excluded", [])
    excluded_by_path = {item.get("path"): item for item in existing_excluded}
    for item in removed:
        excluded_by_path[item["path"]] = {
            **item,
            "removed_reason": "apparel/shoes/hats removed before rescan",
        }
    data["excluded"] = list(excluded_by_path.values())
    data["excluded_count"] = len(data["excluded"])
    data["watch_count"] = len(data.get("watch", []))
    data["selection_logic"] = {
        **data.get("selection_logic", {}),
        "hard_exclusions": list(
            dict.fromkeys(
                [
                    *data.get("selection_logic", {}).get("hard_exclusions", []),
                    "apparel/shoes/hats removed for cross-border beginner selection",
                ]
            )
        ),
    }
    data["rebuild_notes"] = {
        "removed_apparel_categories": len(removed),
        "remaining_target_categories": len(kept),
    }
    return data, removed


def render_category_md(data: dict) -> str:
    target_pool = data.get("target_pool", [])
    removed = data.get("rebuild_notes", {}).get("removed_apparel_categories", 0)
    lines = []
    lines.append("# Category Opportunity Pool")
    lines.append("")
    lines.append(f"- source: `{data.get('source_json', '')}`")
    lines.append(f"- target_pool_count: `{data.get('target_pool_count', len(target_pool))}`")
    lines.append(f"- removed_apparel_categories: `{removed}`")
    lines.append("")
    lines.append("## Selection Logic")
    for item in data.get("selection_logic", {}).get("primary_factors", []):
        lines.append(f"- {item}")
    for item in data.get("selection_logic", {}).get("hard_exclusions", []):
        lines.append(f"- exclude: {item}")
    lines.append("")
    lines.append("## Target Pool")
    for idx, category in enumerate(target_pool, 1):
        risk = ", ".join(category.get("risk_flags", [])) or "-"
        score = category.get("score", "-")
        lines.append(
            f"{idx}. {category_display(category)}"
            f" | score: {score}"
            f" | risk: {risk}"
            f" | path: {category.get('path', '')}"
        )
    if removed:
        lines.append("")
        lines.append("## Removed Apparel Categories")
        for category in data.get("excluded", []):
            if category.get("removed_reason"):
                lines.append(f"- {category_display(category)} | {category.get('path', '')}")
    return "\n".join(lines) + "\n"


def run_scan(category_count: int, pages: int, wait_seconds: float) -> None:
    cmd = [
        sys.executable,
        str(PRODUCT_SCAN),
        "--combined",
        "--start",
        "1",
        "--max-categories",
        str(category_count),
        "--pages",
        str(pages),
    ]
    env = dict(**dict())
    print(f"Running combined scan for {category_count} categories across {pages} pages")
    subprocess.run(cmd, cwd=ROOT, check=True, env=None)


def parse_float(value: object) -> float | None:
    if value in (None, "", "-"):
        return None
    text = str(value).replace(",", "")
    m = re.search(r"-?\d+(?:\.\d+)?", text)
    return float(m.group(0)) if m else None


def parse_int(value: object) -> int | None:
    if value in (None, "", "-"):
        return None
    m = re.search(r"-?\d+", str(value).replace(",", ""))
    return int(m.group(0)) if m else None


def score_product(product: dict, category_meta: dict) -> tuple[int, list[str], list[str]]:
    sales = parse_int(product.get("monthly_sales")) or 0
    reviews = parse_int(product.get("reviews")) or 0
    rating = parse_float(product.get("rating"))
    price = parse_float(product.get("price"))
    margin = parse_float(product.get("profit_margin"))
    fba = parse_float(product.get("fba_fee"))
    sellers = parse_int(product.get("sellers")) or 0
    variants = parse_int(product.get("variants")) or 0

    score = 0.0
    reasons: list[str] = []
    cautions: list[str] = []

    score += min(sales, 3000) / 30.0
    if sales:
        reasons.append(f"月销 {sales}")

    if margin is not None:
        score += margin * 0.85
        reasons.append(f"毛利 {margin:.0f}%")

    if rating is not None:
        score += max(0.0, 4.0 - rating) * 18.0
        reasons.append(f"评分 {rating:.1f}")
    else:
        score += 4.0

    if reviews:
        score += max(0.0, 220 - reviews) / 5.0
        reasons.append(f"Reviews {reviews}")
    else:
        score += 12.0

    if price is not None:
        score += 8.0 if 20 <= price <= 60 else 3.0
        reasons.append(f"价格 ${price:.2f}")
    else:
        score += 2.0

    if sellers is not None:
        score += max(0.0, 3 - sellers) * 6.0
    if variants is not None:
        score += max(0.0, 6 - variants) * 2.5

    if fba is not None:
        score -= max(0.0, fba - 6.0) * 3.0

    risk_flags = category_meta.get("risk_flags", [])
    if risk_flags:
        cautions.append(f"类目风险: {', '.join(risk_flags)}")

    if "electronics_cert" in risk_flags:
        cautions.append("需注意电类认证与售后")
    if "bulky_watch" in risk_flags or "bulky_logistics" in risk_flags:
        cautions.append("物流和仓储成本需复核")
    if "fragile" in risk_flags:
        cautions.append("易碎品要重点看包装和退货")
    if "pool" in risk_flags:
        cautions.append("泳池/水域相关产品先核实季节性")

    score_i = int(round(score))
    return score_i, reasons[:4], cautions[:3]


def select_top_products(products: list[dict], category_pool: list[dict], top_count: int) -> list[dict]:
    meta_by_name = {item.get("name"): item for item in category_pool}
    allowed_names = set(meta_by_name)
    groups: dict[str, list[dict]] = defaultdict(list)
    scored = []
    for product in products:
        leaf = product.get("leaf_category") or "UNKNOWN"
        if leaf not in allowed_names:
            continue
        category_meta = meta_by_name.get(leaf, {})
        score, reasons, cautions = score_product(product, category_meta)
        enriched = dict(product)
        enriched["_score"] = score
        enriched["_reasons"] = reasons
        enriched["_cautions"] = cautions
        scored.append(enriched)
        groups[leaf].append(enriched)

    selected: list[dict] = []
    seen_asin: set[str] = set()

    for leaf, items in sorted(groups.items(), key=lambda item: (-len(item[1]), item[0])):
        items.sort(key=lambda item: (item.get("_score", 0), parse_int(item.get("monthly_sales")) or 0), reverse=True)
        for product in items[:2]:
            asin = product.get("asin") or product.get("parent_asin") or ""
            if not asin or asin in seen_asin:
                continue
            selected.append(product)
            seen_asin.add(asin)

    scored.sort(key=lambda item: (item.get("_score", 0), parse_int(item.get("monthly_sales")) or 0), reverse=True)
    for product in scored:
        if len(selected) >= top_count:
            break
        asin = product.get("asin") or product.get("parent_asin") or ""
        if not asin or asin in seen_asin:
            continue
        selected.append(product)
        seen_asin.add(asin)

    return selected[:top_count]


def main() -> None:
    parser = argparse.ArgumentParser(description="Filter apparel categories, rescan products, and rebuild homepage.")
    parser.add_argument("--pages", type=int, default=5, help="Pages to fetch in combined scan mode.")
    parser.add_argument("--top-count", type=int, default=80, help="How many product cards to keep on the homepage.")
    parser.add_argument("--skip-scan", action="store_true", help="Only rewrite category pool and rebuild from existing scan output.")
    args = parser.parse_args()

    category_data = load_json(CATEGORY_POOL)
    filtered, removed = filter_category_pool(category_data)
    write_json(CATEGORY_POOL, filtered)
    CATEGORY_MD.write_text(render_category_md(filtered), encoding="utf-8")
    print(f"Filtered category pool: kept {filtered['target_pool_count']} categories, removed {len(removed)} apparel categories")

    if not args.skip_scan:
        run_scan(filtered["target_pool_count"], args.pages, wait_seconds=0)

    combined = load_json(COMBINED_OUTPUT)
    top_products = select_top_products(combined.get("products", []), filtered.get("target_pool", []), args.top_count)
    top_output = {
        "source": str(COMBINED_OUTPUT.relative_to(ROOT)),
        "total_products": combined.get("product_count", len(combined.get("products", []))),
        "qualified_parseable_count": len(combined.get("products", [])),
        "top_count": len(top_products),
        "top_products": top_products,
    }
    write_json(TOP_OUTPUT, top_output)
    print(f"Wrote {TOP_OUTPUT.relative_to(ROOT)} with {len(top_products)} products")

    subprocess.run([sys.executable, str(INDEX_BUILDER)], cwd=ROOT, check=True)
    print("Rebuilt index.html")


if __name__ == "__main__":
    main()
