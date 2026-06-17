#!/usr/bin/env python3
"""Import products from a SellerSprite product XLSX export into the manual ASIN watchlist.

Usage:
    python3 import_product_xlsx.py <path-to-xlsx>

Updates:
    products/manual_asins.txt          — ASIN list (append new)
    products/manual_asins_details.json — structured product data (append new)
    products/manual_asins_details.md   — human-readable markdown table (rebuild)
"""
from __future__ import annotations

import html as htmllib
import json
import sys
from datetime import date, datetime
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent
ASINS_TXT   = ROOT / "products" / "manual_asins.txt"
DETAILS_JSON = ROOT / "products" / "manual_asins_details.json"
DETAILS_MD   = ROOT / "products" / "manual_asins_details.md"

SELLERSPRITE_URL = (
    "https://www.sellersprite.com/v3/competitor-lookup"
    "?market=US&monthName=bsr_sales_nearly&asins=%5B%22{asin}%22%5D"
    "&page=1&nodeIdPaths=%5B%5D&symbolFlag=true&size=60"
    "&order%5Bfield%5D=amz_unit&order%5Bdesc%5D=true&lowPrice=N"
)

TODAY = date(2026, 6, 17)


# ── formatters ────────────────────────────────────────────────────────────────

def fmt_int(v, default="-") -> str:
    if v is None or v == "":
        return default
    try:
        return f"{int(float(str(v))):,}"
    except (ValueError, TypeError):
        return default


def fmt_money(v, default="-") -> str:
    if v is None or v == "":
        return default
    try:
        return f"${float(str(v)):,.0f}"
    except (ValueError, TypeError):
        return default


def fmt_price(v, default="-") -> str:
    if v is None or v == "":
        return default
    try:
        return f"${float(str(v)):.2f}"
    except (ValueError, TypeError):
        return default


def fmt_pct(v, default="-") -> str:
    """Convert 0.xx float → 'xx.xx%'"""
    if v is None or v == "":
        return default
    try:
        return f"{float(str(v)) * 100:.2f}%"
    except (ValueError, TypeError):
        return default


def fmt_margin(v, default="-") -> str:
    """Convert 0.xx float → 'xx%'"""
    if v is None or v == "":
        return default
    try:
        return f"{int(float(str(v)) * 100)}%"
    except (ValueError, TypeError):
        return default


def fmt_rating(v, default="-") -> str:
    if v is None or v == "":
        return default
    try:
        return f"{float(str(v)):.1f}"
    except (ValueError, TypeError):
        return default


def fmt_str(v, default="-") -> str:
    if v is None or str(v).strip() == "":
        return default
    return str(v).strip()


def listing_age(listing_date_raw) -> str:
    """Compute human-readable age like '2年 3个月' from a date value."""
    if listing_date_raw is None:
        return "-"
    if isinstance(listing_date_raw, (datetime,)):
        d = listing_date_raw.date()
    elif isinstance(listing_date_raw, date):
        d = listing_date_raw
    else:
        try:
            d = datetime.strptime(str(listing_date_raw)[:10], "%Y-%m-%d").date()
        except ValueError:
            return "-"
    delta_days = (TODAY - d).days
    if delta_days < 0:
        return "-"
    years = delta_days // 365
    months = (delta_days % 365) // 30
    parts = []
    if years:
        parts.append(f"{years}年")
    if months or not years:
        parts.append(f"{months}个月")
    return " ".join(parts)


def listing_date_str(listing_date_raw) -> str:
    if listing_date_raw is None:
        return ""
    if isinstance(listing_date_raw, (datetime,)):
        return listing_date_raw.date().strftime("%Y-%m-%d")
    if isinstance(listing_date_raw, date):
        return listing_date_raw.strftime("%Y-%m-%d")
    s = str(listing_date_raw)[:10]
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return s
    except ValueError:
        return s


# ── Excel row → product dict ──────────────────────────────────────────────────

COLS = {
    "asin": 0, "sku": 1, "params": 2, "brand": 3, "brand_link": 4,
    "title": 5, "pdp_link": 6, "image_url": 7, "parent_asin": 8,
    "cat_path": 9, "main_cat": 10, "main_bsr": 11, "main_bsr_delta": 12,
    "main_bsr_rate": 13, "leaf_cat": 14, "leaf_bsr": 15,
    "monthly_sales": 16, "sales_growth": 17, "monthly_revenue": 18,
    "child_sales": 19, "child_revenue": 20, "variants": 21,
    "price": 22, "prime_price": 23, "coupon": 24, "qa": 25,
    "reviews": 26, "monthly_new_reviews": 27, "rating": 28, "review_rate": 29,
    "fba": 30, "margin": 31, "grade": 32, "listing_date": 33, "listing_days": 34,
    "fulfillment": 35, "shipping": 36, "lqs": 37, "sellers": 38,
    "buybox_seller": 39, "buybox_type": 40, "seller_country": 41,
    "pkg_weight": 58,
}


def row_to_product(row: tuple) -> dict:
    c = COLS
    asin = fmt_str(row[c["asin"]], "")
    if not asin:
        return {}

    ld = row[c["listing_date"]]

    monthly_sales_raw = row[c["monthly_sales"]]
    monthly_revenue_raw = row[c["monthly_revenue"]]
    price_raw = row[c["price"]]
    fba_raw = row[c["fba"]]
    margin_raw = row[c["margin"]]
    reviews_raw = row[c["reviews"]]
    new_reviews_raw = row[c["monthly_new_reviews"]]
    rating_raw = row[c["rating"]]
    review_rate_raw = row[c["review_rate"]]
    sales_growth_raw = row[c["sales_growth"]]
    variants_raw = row[c["variants"]]
    sellers_raw = row[c["sellers"]]
    leaf_bsr_raw = row[c["leaf_bsr"]]

    # raw_metrics: construct a lightweight stub so the field exists
    raw_metrics_parts = [
        fmt_int(monthly_sales_raw), fmt_str(sales_growth_raw),
        fmt_money(monthly_revenue_raw), fmt_int(reviews_raw),
        fmt_price(price_raw), fmt_margin(margin_raw),
        fmt_str(row[c["fulfillment"]]),
    ]
    raw_metrics = " | ".join(p for p in raw_metrics_parts if p and p != "-")

    return {
        "asin": asin,
        "parent_asin": fmt_str(row[c["parent_asin"]], ""),
        "title": fmt_str(row[c["title"]], ""),
        "brand": fmt_str(row[c["brand"]], ""),
        "monthly_sales": fmt_int(monthly_sales_raw),
        "sales_growth": fmt_pct(sales_growth_raw),
        "monthly_revenue": fmt_money(monthly_revenue_raw),
        "variants": fmt_int(variants_raw),
        "price": fmt_price(price_raw),
        "reviews": fmt_int(reviews_raw),
        "monthly_new_reviews": fmt_int(new_reviews_raw),
        "rating": fmt_rating(rating_raw),
        "review_rate": fmt_pct(review_rate_raw),
        "fba_fee": fmt_price(fba_raw),
        "profit_margin": fmt_margin(margin_raw),
        "listing_date": listing_date_str(ld),
        "listing_age": listing_age(ld),
        "leaf_rank": fmt_int(leaf_bsr_raw),
        "leaf_category": fmt_str(row[c["leaf_cat"]], ""),
        "sellers": fmt_int(sellers_raw),
        "package_weight": fmt_str(row[c["pkg_weight"]], ""),
        "raw_metrics": raw_metrics,
        "image_url": fmt_str(row[c["image_url"]], ""),
        "_import_source": "xlsx",
    }


# ── Markdown render ───────────────────────────────────────────────────────────

def render_md(products: list[dict]) -> str:
    lines = [
        "# Manual ASIN Details Watchlist",
        "",
        f"- **Total Unique ASINs**: `{len(products)}`",
        "- **Source**: `manual competitor lookup scraper + xlsx import`",
        f"- **Last Updated**: `{TODAY.isoformat()}`",
        "",
        "| # | Image | ASIN / Brand | Title | Price | Monthly Sales / Rev | Reviews (Rating) | Margin / FBA | Age | Links |",
        "|---:|:---:|:---|:---|:---|:---|:---|:---|:---|:---|",
    ]
    for idx, p in enumerate(products, 1):
        asin = p.get("asin", "")
        title = (p.get("title") or "")[:55] + ("..." if len(p.get("title") or "") > 55 else "")
        title_escaped = htmllib.escape(title).replace("|", "\\|")
        brand = (p.get("brand") or "").replace("|", "\\|")
        image_url = p.get("image_url", "")
        img_cell = (
            f'<img src="{image_url}" width="50" height="50" style="object-fit: contain;" />'
            if image_url else ""
        )
        amazon_url = f"https://www.amazon.com/dp/{asin}"
        sprite_url = SELLERSPRITE_URL.format(asin=asin)
        links = f"[Amazon]({amazon_url})<br>[卖家精灵]({sprite_url})"
        lines.append(
            f"| {idx} | {img_cell} | `{asin}`<br>**{brand}** | {title_escaped} | "
            f"{p.get('price','-')} | {p.get('monthly_sales','-')}<br>*{p.get('monthly_revenue','-')}* | "
            f"{p.get('reviews','-')}<br>({p.get('rating','-')}⭐) | "
            f"{p.get('profit_margin','-')}<br>*{p.get('fba_fee','-')}* | "
            f"{p.get('listing_age','-')} | {links} |"
        )
    return "\n".join(lines) + "\n"


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 import_product_xlsx.py <path-to-xlsx>")
    xlsx_path = Path(sys.argv[1])
    if not xlsx_path.exists():
        sys.exit(f"File not found: {xlsx_path}")

    # Load existing data
    existing_data = json.loads(DETAILS_JSON.read_text(encoding="utf-8"))
    existing_products: list[dict] = existing_data.get("products", [])
    existing_asins: set[str] = {p.get("asin") for p in existing_products if p.get("asin")}
    print(f"Existing products: {len(existing_products)}")

    # Parse Excel
    wb = openpyxl.load_workbook(xlsx_path, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    data_rows = rows[1:]
    print(f"Excel rows (excl header): {len(data_rows)}")

    # Convert and deduplicate
    new_products: list[dict] = []
    skipped_dup: list[str] = []
    skipped_invalid: int = 0
    for row in data_rows:
        product = row_to_product(row)
        if not product:
            skipped_invalid += 1
            continue
        asin = product["asin"]
        if asin in existing_asins:
            skipped_dup.append(asin)
            continue
        new_products.append(product)
        existing_asins.add(asin)

    print(f"  New products to add: {len(new_products)}")
    print(f"  Already in watchlist (skipped): {len(skipped_dup)}")
    if skipped_dup:
        print(f"  Dup ASINs: {', '.join(skipped_dup)}")
    if skipped_invalid:
        print(f"  Invalid rows (skipped): {skipped_invalid}")

    if not new_products:
        print("Nothing to add — all ASINs already in watchlist.")
        return

    # Show summary of new products by category
    from collections import Counter
    cats = Counter(p.get("leaf_category","UNKNOWN") for p in new_products)
    print("\nNew products by leaf category:")
    for cat, n in cats.most_common():
        print(f"  {n:3} × {cat}")

    # Merge and update JSON
    all_products = existing_products + new_products
    existing_data["products"] = all_products
    existing_data["asin_count"] = len(all_products)
    existing_data["scraped_count"] = len(all_products)
    DETAILS_JSON.write_text(
        json.dumps(existing_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\nWrote {DETAILS_JSON.relative_to(ROOT)}  ({len(all_products)} total products)")

    # Update ASIN txt
    all_asins = [p["asin"] for p in all_products if p.get("asin")]
    ASINS_TXT.write_text("\n".join(all_asins) + "\n", encoding="utf-8")
    print(f"Wrote {ASINS_TXT.relative_to(ROOT)}  ({len(all_asins)} ASINs)")

    # Rebuild Markdown
    DETAILS_MD.write_text(render_md(all_products), encoding="utf-8")
    print(f"Wrote {DETAILS_MD.relative_to(ROOT)}")

    print(f"\n✅  Added {len(new_products)} new products  ({len(all_products)} total)")


if __name__ == "__main__":
    main()
