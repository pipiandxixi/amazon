#!/usr/bin/env python3
"""Aggregate scored product recommendations from all completed product scan files.

Usage:
    python3 scripts/aggregate_top_picks.py --run-dir results/2026_06_10_full_sweep
    python3 scripts/aggregate_top_picks.py --run-dir results/2026_06_10_full_sweep --top-n 50
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
from pathlib import Path


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

_ROW_RE = re.compile(
    r"^\|\s*\d+\s*\|\s*"
    r"\[(?P<asin>[A-Z0-9]+)\]\([^)]+\)\s*\|\s*"  # ASIN
    r"(?P<zh_name>[^|]*?)\s*\|\s*"               # Chinese name
    r"(?P<en_name>[^|]*?)\s*\|\s*"               # English name
    r"(?P<sales>\d[\d,]*)\s*/\s*(?P<growth>[^|]*?)\s*\|\s*"  # sales / growth
    r"[^|]*?\|\s*"                                # revenue (skip)
    r"\$(?P<price>[\d.]+)\s*\|\s*"               # price
    r"\$[\d.]+\s*\((?P<cogs_pct>\d+)%\)\s*\|\s*"  # cost (pct)
    r"(?P<reviews>\d[\d,]*)\s*/[^|]*\|\s*"       # reviews / monthly new
    r"(?P<rating>[\d.]+)\s*\|\s*"                # rating
    r"[^/]*?/\s*(?P<margin>\d+)%\s*\|\s*"       # FBA / margin
    r"(?P<variants>\d+)\s*\|\s*"                 # variants
    r"\d+\s*\|\s*"                               # BSR (skip)
    r"(?P<sellers>\d+)\s*\|\s*"                  # sellers
    r"[^|]*?\|\s*"                               # weight (skip)
    r"(?P<listing_date>\d{4}-\d{2}-\d{2})\s+(?P<age>[^|]+?)\s*\|",
)

_MONTHS_RE = re.compile(r"(\d+)\s*个月")
_YEARS_RE = re.compile(r"(\d+)\s*年")


def _parse_age_months(age_str: str) -> float:
    """Convert age string like '4个月' or '1年 2个月' to total months."""
    years = _YEARS_RE.search(age_str)
    months = _MONTHS_RE.search(age_str)
    total = 0.0
    if years:
        total += int(years.group(1)) * 12
    if months:
        total += int(months.group(1))
    return total or 0.5  # <1 month products get 0.5


def _parse_growth(g: str) -> float | None:
    g = g.strip().rstrip("%").replace(",", "")
    if not g or g == "-":
        return None
    try:
        return float(g)
    except ValueError:
        return None


def parse_product_file(path: Path) -> tuple[str, str, list[dict]]:
    """Return (category_en, category_zh, list_of_products)."""
    text = path.read_text(encoding="utf-8")

    # Category names
    cat_en = path.stem.replace("_", " ").title()
    zh_m = re.search(r"市场评级.*?(?:均价|$)", text)
    cat_zh = ""
    # Try to get zh from file header or market line
    header_m = re.search(r"^# (.+?) 合格产品", text, re.MULTILINE)
    if header_m:
        cat_en = header_m.group(1).strip()

    products = []
    for line in text.splitlines():
        m = _ROW_RE.match(line)
        if not m:
            continue
        g = m.groupdict()
        growth = _parse_growth(g["growth"])
        age_months = _parse_age_months(g["age"])
        try:
            products.append({
                "asin": g["asin"],
                "zh_name": g["zh_name"].strip().rstrip("…").rstrip("..."),
                "en_name": g["en_name"].strip().rstrip("…").rstrip("..."),
                "category": cat_en,
                "monthly_sales": int(g["sales"].replace(",", "")),
                "growth": growth,
                "price": float(g["price"]),
                "cogs_pct": int(g["cogs_pct"]),
                "reviews": int(g["reviews"].replace(",", "")),
                "rating": float(g["rating"]),
                "margin": int(g["margin"]),
                "variants": int(g["variants"]),
                "sellers": int(g["sellers"]),
                "age_months": age_months,
                "listing_date": g["listing_date"],
            })
        except (ValueError, KeyError):
            continue
    return cat_en, cat_zh, products


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_product(p: dict) -> float:
    s = 0.0

    # Reviews (highest weight)
    r = p["reviews"]
    if r < 30:
        s += 4
    elif r < 60:
        s += 3
    elif r < 100:
        s += 2
    elif r < 150:
        s += 1

    # Growth (highest weight)
    g = p["growth"]
    if g is None:
        s += 0.5  # no data: neutral
    elif g > 100:
        s += 4
    elif g > 50:
        s += 3
    elif g > 20:
        s += 2
    elif g > 5:
        s += 1
    elif g < -30:
        s -= 1

    # Margin
    m = p["margin"]
    if m >= 72:
        s += 3
    elif m >= 65:
        s += 2
    elif m >= 55:
        s += 1
    else:
        s -= 1

    # Sellers (competition)
    sel = p["sellers"]
    if sel == 1:
        s += 2
    elif sel == 2:
        s += 1
    elif sel >= 5:
        s -= 1

    # COGS ratio (lower = better sourcing economics)
    c = p["cogs_pct"]
    if c <= 12:
        s += 2
    elif c <= 15:
        s += 1
    elif c >= 25:
        s -= 1

    # Listing age: sweet spot 3-18 months
    age = p["age_months"]
    if 3 <= age <= 18:
        s += 1
    elif age < 1:
        s -= 0.5  # brand new, no proof yet

    # Monthly sales floor bonus
    if p["monthly_sales"] >= 300:
        s += 1
    elif p["monthly_sales"] >= 150:
        s += 0.5

    # Rating quality
    if p["rating"] >= 4.5:
        s += 0.5

    return s


# ---------------------------------------------------------------------------
# Report writing
# ---------------------------------------------------------------------------

def format_growth(g: float | None) -> str:
    if g is None:
        return "—"
    sign = "+" if g >= 0 else ""
    return f"{sign}{g:.0f}%"


def key_reason(p: dict) -> str:
    """Generate a concise reason string from the top 2-3 strongest signals."""
    parts: list[str] = []

    # Reviews (low = opportunity)
    r = p["reviews"]
    if r < 10:
        parts.append(f"{r} reviews极低竞争")
    elif r < 30:
        parts.append(f"{r} reviews低竞争")
    elif r < 60:
        parts.append(f"{r} reviews仍可入局")

    # Growth
    g = p["growth"]
    if g is not None:
        if g >= 500:
            parts.append(f"增速+{g:.0f}%爆发")
        elif g >= 100:
            parts.append(f"增速+{g:.0f}%高增长")
        elif g >= 30:
            parts.append(f"增速+{g:.0f}%")

    # Margin
    m = p["margin"]
    if m >= 72:
        parts.append(f"{m}%高毛利")
    elif m >= 65:
        parts.append(f"{m}%毛利")

    # Sellers
    if p["sellers"] == 1:
        parts.append("独家卖家")

    # Listing age
    age = p["age_months"]
    if age < 2:
        parts.append("<2个月新品")
    elif age <= 6:
        parts.append(f"{age:.0f}个月新品")

    # Monthly sales volume
    if p["monthly_sales"] >= 500:
        parts.append(f"月销{p['monthly_sales']:,}")
    elif p["monthly_sales"] >= 200:
        parts.append(f"月销{p['monthly_sales']}")

    # Keep the 3 most impactful signals
    return "；".join(parts[:3]) or "多项指标达标"


def write_top_picks(
    run_dir: Path,
    all_products: list[dict],
    scanned_cats: list[str],
    top_n: int,
    date_str: str,
    batch_label: str = "",
) -> Path:
    out_path = run_dir / "top_picks.md"

    # Deduplicate by ASIN (keep highest-scored instance)
    seen: dict[str, dict] = {}
    for p in all_products:
        asin = p["asin"]
        if asin not in seen or p["_score"] > seen[asin]["_score"]:
            seen[asin] = p
    ranked = sorted(seen.values(), key=lambda x: x["_score"], reverse=True)

    # Header
    lines = [
        f"# Amazon 综合选品推荐 ({date_str}{' — ' + batch_label if batch_label else ''})",
        "",
        "## 探索范围",
        f"本次扫描覆盖 **{len(scanned_cats)}** 个绿色子类目（全量扫描）。",
        f"去重后共 **{len(seen)}** 个候选单品，本报告取评分前 **{min(top_n, len(seen))}** 名。",
        "",
    ]

    # Table
    lines += [
        f"## Top {min(top_n, len(seen))} 推荐单品",
        "",
        "| 排名 | ASIN | 品名 | 类目 | 价格 | 月销量 | 增长率 | 毛利率 | Reviews | 卖家数 | 上架时长 | 推荐理由 |",
        "|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for i, p in enumerate(ranked[:top_n], 1):
        name = f"{p['zh_name']} / {p['en_name']}" if p["en_name"] else p["zh_name"]
        if len(name) > 45:
            name = name[:43] + "…"
        age_str = f"{p['age_months']:.0f}个月" if p["age_months"] >= 1 else "<1个月"
        lines.append(
            f"| {i} | [{p['asin']}](https://www.amazon.com/dp/{p['asin']}) "
            f"| {name} | {p['category']} "
            f"| ${p['price']:.2f} "
            f"| {p['monthly_sales']:,} | {format_growth(p['growth'])} "
            f"| {p['margin']}% | {p['reviews']} | {p['sellers']} "
            f"| {age_str} | {key_reason(p)} |"
        )

    lines += [""]

    # Detailed analysis for top 30 (or top_n if smaller)
    detail_n = min(30, top_n, len(seen))
    lines += [f"## 各产品详细分析（前 {detail_n} 名）", ""]
    for i, p in enumerate(ranked[:detail_n], 1):
        name = f"{p['zh_name']} / {p['en_name']}" if p["en_name"] else p["zh_name"]
        growth_note = f"增速 {format_growth(p['growth'])}" if p["growth"] is not None else "无增速数据"
        sellers_note = "独家卖家" if p["sellers"] == 1 else f"{p['sellers']} 个卖家"
        age_str = f"{p['age_months']:.0f}个月" if p["age_months"] >= 1 else "<1个月"
        lines += [
            f"### {i}. [{p['asin']}] {name}",
            f"**类目**: {p['category']} ｜ **月销量**: {p['monthly_sales']:,} ｜ "
            f"**{growth_note}** ｜ **毛利率**: {p['margin']}% ｜ "
            f"**Reviews**: {p['reviews']} ｜ **{sellers_note}** ｜ **上架**: {age_str}",
            "",
            f"**选入理由**: 月销 {p['monthly_sales']:,}、{p['reviews']} reviews、{sellers_note}、{p['margin']}% 毛利。",
            f"**建议下一步**: 1688 搜索核心词核实成本，目标 COGS ≤ {p['cogs_pct']}%（当前估算 {p['cogs_pct']}%）。",
            "",
        ]

    # Covered categories list
    lines += [
        "## 已覆盖类目",
        "",
        ", ".join(sorted(scanned_cats)),
        "",
    ]

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True, help="Run directory with products/ subfolder")
    parser.add_argument("--top-n", type=int, default=50, help="Number of top picks to include (default 50)")
    parser.add_argument("--date", default="", help="Date string for report header")
    parser.add_argument("--batch-label", default="", dest="batch_label", help="Batch label for header")
    args = parser.parse_args()

    run_dir = Path(args.run_dir)
    products_dir = run_dir / "products"
    date_str = args.date or datetime.date.today().strftime("%Y-%m-%d")

    md_files = sorted(f for f in products_dir.glob("*.md") if f.stem != "scan_principles")
    if not md_files:
        raise SystemExit(f"No product .md files found in {products_dir}")

    all_products: list[dict] = []
    scanned_cats: list[str] = []
    zero_result_cats: list[str] = []

    for f in md_files:
        cat_en, _, products = parse_product_file(f)
        scanned_cats.append(cat_en)
        if not products:
            zero_result_cats.append(cat_en)
            continue
        for p in products:
            p["_score"] = score_product(p)
        all_products.extend(products)

    print(f"Files read: {len(md_files)}  |  Products parsed: {len(all_products)}  |  Zero-result cats: {len(zero_result_cats)}")
    if zero_result_cats:
        print(f"Zero-result: {', '.join(zero_result_cats)}")

    out = write_top_picks(run_dir, all_products, scanned_cats, args.top_n, date_str, args.batch_label)
    print(f"Written: {out}")


if __name__ == "__main__":
    main()
