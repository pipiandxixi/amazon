#!/usr/bin/env python3
"""Rank products worth reverse-keyword checking in SellerSprite.

The goal is to avoid checking all products. We start with low IP-risk,
small/light products, then rank for cheap-ish products with enough demand and
scene/gift/decor tags that may expose low-CPC, high-search keywords.
"""
from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_FILE = ROOT / "products" / "manual_asins_details.json"
JSON_OUTPUT = ROOT / "products" / "reverse_keyword_candidates.json"
MD_OUTPUT = ROOT / "products" / "reverse_keyword_candidates.md"

sys.path.insert(0, str(ROOT))
from patch_ip_risk import assess_ip_risk  # noqa: E402

REVERSE_URL = "https://www.sellersprite.com/v3/keyword-reverse/?q={asin}&marketId=1&date=&badges="

BULKY_TERMS = (
    "rug", "blanket", "curtain", "furniture", "cushion", "mattress", "playhouse",
    "tent", "table", "chair", "nightstand", "shelf", "shelves", "air mattress",
    "bean bag", "pool", "fountain", "birdbath", "banner", "flagpole",
)

COMPLIANCE_TERMS = (
    "heating pad", "massager", "facial", "skin", "supplement", "knife", "airsoft",
    "battery", "charger", "electrical", "neon", "laser", "medical", "health care",
)

SCENE_TAG_BONUS = {
    "礼品送礼": 14,
    "户外庭院": 12,
    "花园装饰": 12,
    "门廊露台": 11,
    "灯光氛围": 10,
    "桌面摆件": 10,
    "墙面悬挂": 9,
    "家居氛围": 8,
    "节日季节": 8,
    "纪念慰问": 7,
    "派对活动": 6,
}


def number(value: object) -> float:
    match = re.search(r"-?\d+(?:,\d{3})*(?:\.\d+)?|-?\d+(?:\.\d+)?", str(value or ""))
    return float(match.group(0).replace(",", "")) if match else 0.0


def parse_weight_lb(value: object) -> float | None:
    text = str(value or "").strip().lower()
    if not text or text == "-":
        return None
    amount = number(text)
    if amount <= 0:
        return None
    if "ounce" in text or re.search(r"\boz\b", text):
        return amount / 16.0
    if "gram" in text or re.search(r"\bg\b", text):
        return amount / 453.592
    if "kg" in text or "kilogram" in text:
        return amount * 2.20462
    return amount


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def score_product(product: dict) -> tuple[float, list[str], list[str]]:
    price = number(product.get("price"))
    sales = number(product.get("monthly_sales"))
    reviews = number(product.get("reviews"))
    margin = number(product.get("profit_margin"))
    weight = parse_weight_lb(product.get("package_weight"))
    tags = product.get("scene_tags") or []

    reasons: list[str] = []
    cautions: list[str] = []
    score = 0.0

    score += min(sales, 30000) / 650.0
    if sales:
        reasons.append(f"月销 {int(sales):,}")

    if 12 <= price <= 45:
        score += 22
        reasons.append(f"价格 ${price:.2f}")
    elif 45 < price <= 70:
        score += 10
        reasons.append(f"价格 ${price:.2f}")
    elif price:
        score -= 12
        cautions.append(f"价格 ${price:.2f} 不在优先区间")

    score += max(0.0, 500 - reviews) / 18.0
    if reviews:
        reasons.append(f"Reviews {int(reviews):,}")

    if margin:
        score += min(margin, 85) / 8.0
        reasons.append(f"毛利 {margin:.0f}%")

    if weight is not None:
        if weight <= 1.5:
            score += 18
            reasons.append(f"重量 {weight:.2f} lb")
        elif weight <= 2.5:
            score += 8
            reasons.append(f"重量 {weight:.2f} lb")
        else:
            score -= 25
            cautions.append(f"偏重 {weight:.2f} lb")

    tag_bonus = sum(SCENE_TAG_BONUS.get(tag, 0) for tag in tags)
    score += min(tag_bonus, 38)
    if tags:
        reasons.append("标签 " + ", ".join(tags[:4]))

    text = " ".join(
        str(product.get(key) or "")
        for key in ("title", "leaf_category", "brand")
    ).lower()
    if has_any(text, COMPLIANCE_TERMS):
        score -= 18
        cautions.append("可能涉及认证/售后/合规")
    if has_any(text, BULKY_TERMS):
        score -= 22
        cautions.append("可能偏大件")

    return round(score, 2), reasons[:5], cautions[:4]


def include_product(product: dict) -> tuple[bool, list[str]]:
    risk, reason = assess_ip_risk(product)
    if risk != "low":
        return False, [f"IP {risk}: {reason}"]

    price = number(product.get("price"))
    weight = parse_weight_lb(product.get("package_weight"))
    sales = number(product.get("monthly_sales"))
    text = " ".join(
        str(product.get(key) or "")
        for key in ("title", "leaf_category", "brand")
    ).lower()

    rejects: list[str] = []
    if price and price > 80:
        rejects.append(f"price>{80}")
    if weight is not None and weight > 3:
        rejects.append("weight>3lb")
    if sales and sales < 500:
        rejects.append("monthly_sales<500")
    if has_any(text, BULKY_TERMS):
        rejects.append("bulky_term")
    if has_any(text, COMPLIANCE_TERMS):
        rejects.append("compliance_term")
    return not rejects, rejects


def render_md(candidates: list[dict], excluded_summary: dict[str, int]) -> str:
    lines = [
        "# Reverse Keyword Candidate Queue",
        "",
        "Purpose: prioritize low-risk, smaller products for SellerSprite reverse-keyword checks.",
        "",
        "Suggested SellerSprite keyword filters:",
        "- 月搜索量: `>= 1000`",
        "- PPC竞价: `<= 0.8`",
        "- Prefer low title density, low ad competition, and broad scene/gift/decor intent.",
        "",
        "## Exclusion Summary",
    ]
    for reason, count in sorted(excluded_summary.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {reason}: `{count}`")
    lines.extend([
        "",
        "## Top Candidates",
        "",
        "| # | Score | ASIN | Category | Price | Sales | Reviews | Weight | Tags | Notes | SellerSprite |",
        "|---:|---:|:---|:---|---:|---:|---:|:---|:---|:---|:---|",
    ])
    for idx, item in enumerate(candidates, 1):
        p = item["product"]
        asin = p.get("asin", "")
        tags = ", ".join(p.get("scene_tags") or [])
        notes = "; ".join(item["reasons"][:3])
        url = REVERSE_URL.format(asin=asin)
        lines.append(
            f"| {idx} | {item['score']:.2f} | `{asin}` | {p.get('leaf_category','')} | "
            f"{p.get('price','-')} | {p.get('monthly_sales','-')} | {p.get('reviews','-')} | "
            f"{p.get('package_weight','-')} | {tags} | {notes} | [reverse]({url}) |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    data = json.loads(PRODUCTS_FILE.read_text(encoding="utf-8"))
    products = data.get("products", [])
    candidates: list[dict] = []
    excluded_summary: dict[str, int] = {}

    for product in products:
        include, rejects = include_product(product)
        if not include:
            for reason in rejects:
                excluded_summary[reason] = excluded_summary.get(reason, 0) + 1
            continue
        score, reasons, cautions = score_product(product)
        asin = product.get("asin", "")
        candidates.append({
            "asin": asin,
            "score": score,
            "seller_sprite_reverse_url": REVERSE_URL.format(asin=asin),
            "reasons": reasons,
            "cautions": cautions,
            "product": product,
        })

    candidates.sort(key=lambda item: (item["score"], number(item["product"].get("monthly_sales"))), reverse=True)

    output = {
        "source": str(PRODUCTS_FILE.relative_to(ROOT)),
        "total_products": len(products),
        "candidate_count": len(candidates),
        "excluded_summary": excluded_summary,
        "suggested_keyword_filters": {
            "monthly_search_min": 1000,
            "ppc_bid_max": 0.8,
            "risk": "low",
            "max_weight_lb": 3,
            "max_price_usd": 80,
        },
        "candidates": candidates,
    }
    JSON_OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MD_OUTPUT.write_text(render_md(candidates[:100], excluded_summary), encoding="utf-8")

    print(f"Loaded {len(products)} products")
    print(f"Candidate products: {len(candidates)}")
    print(f"Wrote {JSON_OUTPUT.relative_to(ROOT)}")
    print(f"Wrote {MD_OUTPUT.relative_to(ROOT)}")
    print("Top 20:")
    for idx, item in enumerate(candidates[:20], 1):
        p = item["product"]
        print(f"{idx:2}. {item['score']:6.2f} {p.get('asin')} {p.get('price')} {p.get('monthly_sales')} {p.get('leaf_category')}")


if __name__ == "__main__":
    main()
