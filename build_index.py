#!/usr/bin/env python3
"""Rebuild index.html from products/manual_asins_details.json.

Scoring is computed inline from product attributes.
Category metrics come from category/category_opportunity_pool.json via
fuzzy name matching (word-overlap heuristic).
IP risk badges are injected afterwards by patch_ip_risk.py.

Usage:
    python3 build_index.py
"""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "products" / "manual_asins_details.json"
CATEGORY_POOL = ROOT / "category" / "category_opportunity_pool.json"
OUTPUT = ROOT / "index.html"

SELLERSPRITE_URL = (
    "https://www.sellersprite.com/v3/competitor-lookup"
    "?market=US&monthName=bsr_sales_nearly&asins=%5B%22{asin}%22%5D"
    "&page=1&nodeIdPaths=%5B%5D&symbolFlag=true&size=60"
    "&order%5Bfield%5D=amz_unit&order%5Bdesc%5D=true&lowPrice=N"
)

# Words to ignore when matching leaf_category to pool names.
_STOP = {
    "and", "or", "the", "a", "an", "for", "of", "in", "at", "to", "with",
    "by", "&",
    "combination", "automatic", "outdoor", "indoor", "cell", "phone",
    "handheld", "toy", "landscape", "wall", "pool", "bed", "garden",
    "solar", "led", "electric", "digital", "portable", "wireless",
}

TAG_RULES: list[tuple[str, tuple[str, ...]]] = [
    ("户外庭院", ("outdoor", "backyard", "yard", "lawn", "deck", "patio", "porch")),
    ("门廊露台", ("patio", "porch", "deck", "balcony", "front door", "entryway")),
    ("花园装饰", ("garden", "planter", "plant", "flower", "birdbath", "wind chime", "stake")),
    ("灯光氛围", ("light", "lantern", "solar", "string lights", "spotlight", "path light", "night-light")),
    ("墙面悬挂", ("hanging", "wall", "wreath", "flag", "banner", "curtain", "tapestry")),
    ("桌面摆件", ("table", "centerpiece", "vase", "bowl", "candle", "tray", "statue", "figurine")),
    ("礼品送礼", ("gift", "gifts", "present", "mom", "dad", "women", "men", "grandma", "housewarming")),
    ("纪念慰问", ("memorial", "sympathy", "remembrance", "bereavement", "condolence")),
    ("节日季节", ("christmas", "holiday", "halloween", "thanksgiving", "easter", "fall", "spring", "summer", "winter")),
    ("家居氛围", ("home decor", "room decor", "farmhouse", "boho", "rustic", "cozy", "aesthetic", "blanket", "rug")),
    ("放松疗愈", ("relief", "relax", "calm", "massage", "heating pad", "aromatherapy", "self care", "spa")),
    ("烧烤露营", ("grill", "bbq", "barbecue", "camping", "picnic", "outdoor cooking")),
    ("派对活动", ("party", "game", "balloon", "garland", "centerpiece", "birthday", "wedding")),
    ("儿童玩具", ("kids", "toy", "play", "toddler", "children", "water balloons", "walkie talkie")),
    ("宠物鸟类", ("bird", "feeder", "pet", "dog", "cat")),
    ("美妆护理", ("bath", "shower", "nail", "hair", "facial", "skin", "beauty")),
    ("工具维修", ("tool", "flashlight", "crimper", "charger", "extension cord", "hardware")),
    ("旅行出行", ("travel", "duffel", "tote", "backpack", "portable", "organizer")),
]


def _tokens(name: str) -> set[str]:
    return {w.lower() for w in re.split(r"[\s&,/]+", name) if w.lower() not in _STOP and len(w) > 1}


def build_pool_index(pool: list[dict]) -> list[tuple[str, set[str], dict]]:
    """Return [(pool_name, tokens, entry), ...] for fast lookup."""
    return [(e["name"], _tokens(e["name"]), e) for e in pool]


def match_pool(leaf: str, pool_index: list[tuple]) -> dict:
    """Fuzzy-match a product leaf category to the best pool entry.
    Returns the matched entry dict, or {} if no good match."""
    leaf_tok = _tokens(leaf)
    best_score = 0.0
    best_entry: dict = {}
    for pool_name, pool_tok, entry in pool_index:
        if not pool_tok:
            continue
        overlap = len(leaf_tok & pool_tok)
        # Score = overlap / pool_token_count (reward specificity in pool name)
        score = overlap / len(pool_tok)
        if score > best_score:
            best_score = score
            best_entry = entry
    return best_entry if best_score >= 0.5 else {}


def classify_scene_tags(product: dict) -> list[str]:
    text = " ".join(
        str(product.get(key) or "")
        for key in ("title", "leaf_category", "brand", "raw_metrics")
    ).lower()
    tags: list[str] = []
    for label, patterns in TAG_RULES:
        if any(pattern in text for pattern in patterns):
            tags.append(label)
    if not tags:
        tags.append("泛生活方式")
    return tags[:6]


def ensure_scene_tags(products: list[dict]) -> bool:
    changed = False
    for product in products:
        tags = classify_scene_tags(product)
        if product.get("scene_tags") != tags:
            product["scene_tags"] = tags
            changed = True
    return changed


# ── Scoring ───────────────────────────────────────────────────────────────────

def _parse_float(value: object) -> float | None:
    if value in (None, "", "-"):
        return None
    text = str(value).replace(",", "").replace("%", "")
    m = re.search(r"-?\d+(?:\.\d+)?", text)
    return float(m.group(0)) if m else None


def _parse_int(value: object) -> int | None:
    if value in (None, "", "-"):
        return None
    m = re.search(r"-?\d+", str(value).replace(",", ""))
    return int(m.group(0)) if m else None


def score_product(product: dict, category_meta: dict) -> tuple[int, list[str], list[str]]:
    sales = _parse_int(product.get("monthly_sales")) or 0
    reviews = _parse_int(product.get("reviews")) or 0
    rating = _parse_float(product.get("rating"))
    price = _parse_float(product.get("price"))
    margin = _parse_float(product.get("profit_margin"))   # e.g. "62%" → 62.0
    fba = _parse_float(product.get("fba_fee"))
    sellers = _parse_int(product.get("sellers")) or 0
    variants = _parse_int(product.get("variants")) or 0

    score = 0.0
    reasons: list[str] = []
    cautions: list[str] = []

    score += min(sales, 3000) / 30.0
    if sales:
        reasons.append(f"月销 {sales:,}")

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
        reasons.append(f"Reviews {reviews:,}")
    else:
        score += 12.0

    if price is not None:
        score += 8.0 if 20 <= price <= 60 else 3.0
        reasons.append(f"价格 ${price:.2f}")
    else:
        score += 2.0

    score += max(0.0, 3 - sellers) * 6.0
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

    return int(round(score)), reasons[:4], cautions[:3]


# ── HTML helpers ──────────────────────────────────────────────────────────────

def esc(value) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def short(value, max_len: int = 150) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def fmt_pct(v: float | None, decimals: int = 1) -> str:
    return f"{v:.{decimals}f}%" if v is not None else "-"


def fmt_money(v: float | None) -> str:
    return f"${v:,.0f}" if v is not None else "-"


def fmt_metric(v: float | None) -> str:
    if v is None:
        return "-"
    if v == int(v):
        return f"{int(v):,}"
    return f"{v:,.2f}"


# ── Category metrics panel ────────────────────────────────────────────────────

def render_cat_metrics(entry: dict) -> str:
    if not entry:
        return ""
    m = entry.get("metrics", {})
    monthly_sales = m.get("monthly_sales")
    avg_sales = m.get("avg_sales")
    avg_revenue = m.get("avg_revenue")
    price = m.get("price")
    total_products = m.get("total_products")
    rating = m.get("rating")
    reviews = m.get("reviews")
    product_conc = m.get("product_conc")
    brand_conc = m.get("brand_conc")
    seller_conc = m.get("seller_conc")
    profit = m.get("profit")
    return_rate = m.get("return_rate")
    new_ratio = m.get("new_ratio")
    spr = m.get("search_purchase_ratio")

    def row(label: str, value: str) -> str:
        return (
            f'<div class="cat-metric-item">'
            f'<span>{label}</span>'
            f'<b>{value}</b>'
            f'</div>'
        )

    def fmt_sales(total, avg) -> str:
        t = f"{int(total):,}" if total is not None else "-"
        a = f"{int(avg):,}" if avg is not None else "-"
        return f"{t} / {a}"

    def fmt_rev_price(rev, pr) -> str:
        rv = fmt_money(rev)
        pr_s = f"${pr:.2f}" if pr is not None else "-"
        return f"{rv} / {pr_s}"

    def fmt_prod_rating(tp, rt, rv) -> str:
        tp_s = f"{int(tp):,}" if tp is not None else "-"
        rt_s = f"{rt:.1f}⭐" if rt is not None else "-"
        rv_s = f"{int(rv):,} Revs" if rv is not None else "-"
        return f"{tp_s} / {rt_s} ({rv_s})"

    def fmt_conc(pc, bc, sc) -> str:
        parts = []
        for v in (pc, bc, sc):
            parts.append(fmt_pct(v, 1) if v is not None else "-")
        return " / ".join(parts)

    def fmt_profit_return(pf, rr) -> str:
        pf_s = fmt_pct(pf, 1) if pf is not None else "-"
        rr_s = fmt_pct(rr, 2) if rr is not None else "-"
        return f"{pf_s} / {rr_s}"

    def fmt_new_spr(nr, sp) -> str:
        nr_s = fmt_pct(nr, 1) if nr is not None else "-"
        sp_s = f"{sp:.2f}" if sp is not None else "-"
        return f"{nr_s} / {sp_s}"

    items = [
        row("月销量 / 均销量", fmt_sales(monthly_sales, avg_sales)),
        row("平均销售额 / 均价", fmt_rev_price(avg_revenue, price)),
        row("商品总数 / 均评分 (评论数)", fmt_prod_rating(total_products, rating, reviews)),
        row("行业集中度 (产品/品牌/卖家)", fmt_conc(product_conc, brand_conc, seller_conc)),
        row("毛利率 / 退货率", fmt_profit_return(profit, return_rate)),
        row("新品占比 / 搜索购买比", fmt_new_spr(new_ratio, spr)),
    ]
    return f'<div class="cat-metrics-panel">{"".join(items)}</div>'


# ── Product card ──────────────────────────────────────────────────────────────

def render_card(product: dict, score: int, reasons: list[str], cautions: list[str]) -> str:
    asin = product.get("asin", "")
    amazon_url = f"https://www.amazon.com/dp/{asin}"
    sprite_url = SELLERSPRITE_URL.format(asin=asin)
    image_url = product.get("image_url") or ""
    tags = product.get("scene_tags") or classify_scene_tags(product)
    tags_html = "".join(f'<span class="tag">{esc(tag)}</span>' for tag in tags)
    search_text = " ".join(
        str(value or "")
        for value in (
            asin,
            product.get("title"),
            product.get("brand"),
            product.get("leaf_category"),
            " ".join(tags),
        )
    ).lower()

    image_html = (
        f'<img src="{esc(image_url)}" alt="{esc(product.get("title", ""))}" loading="lazy">'
        if image_url
        else '<div class="no-img">No image</div>'
    )
    reasons_html = "".join(f"<li>{esc(r)}</li>" for r in reasons)
    caution_html = (
        f'<div class="cautions">{esc("；".join(cautions))}</div>' if cautions else ""
    )

    return f"""
        <article class="product-card" data-search="{esc(search_text)}">
          <a class="thumb" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">
            {image_html}
          </a>
          <div class="product-main">
            <div class="product-topline">
              <a class="asin" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">{esc(asin)}</a>
              <span class="score">Score {score}</span>
            </div>
            <h3>{esc(short(product.get("title", "")))}</h3>
            <div class="brand">{esc(product.get("brand") or "Unknown brand")}</div>
            <div class="tag-row">{tags_html}</div>
            <div class="external-links">
              <a class="link-btn amazon" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">Amazon</a>
              <a class="link-btn sprite" href="{esc(sprite_url)}" target="_blank" rel="noreferrer">卖家精灵</a>
            </div>
            <div class="metrics">
              <span><b>{esc(product.get("monthly_sales"))}</b><small>月销量</small></span>
              <span><b>{esc(product.get("monthly_revenue"))}</b><small>月销售额</small></span>
              <span><b>{esc(product.get("price"))}</b><small>价格</small></span>
              <span><b>{esc(product.get("reviews"))}</b><small>Reviews</small></span>
              <span><b>{esc(product.get("rating"))}</b><small>评分</small></span>
              <span><b>{esc(product.get("fba_fee"))}</b><small>FBA</small></span>
              <span><b>{esc(product.get("profit_margin"))}</b><small>毛利</small></span>
              <span><b>{esc(product.get("package_weight"))}</b><small>重量</small></span>
            </div>
            <div class="submetrics">
              <span>变体 {esc(product.get("variants"))}</span>
              <span>卖家 {esc(product.get("sellers"))}</span>
              <span>小类排名 #{esc(product.get("leaf_rank"))}</span>
              <span>{esc(product.get("leaf_category") or "UNKNOWN")}</span>
              <span>上架 {esc(product.get("listing_date"))} {esc(product.get("listing_age"))}</span>
            </div>
            <ul class="reasons">{reasons_html}</ul>
            {caution_html}
          </div>
        </article>"""


# ── Full HTML ─────────────────────────────────────────────────────────────────

CSS = """\
:root {
  --bg: #f6f7f9;
  --panel: #ffffff;
  --text: #18202a;
  --muted: #667085;
  --line: #d9dee7;
  --accent: #0f766e;
  --accent-2: #b45309;
  --good: #166534;
  --warn: #9a3412;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: var(--bg); color: var(--text); }
a { color: inherit; }
.header { background: #ffffff; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 10; }
.header-inner { max-width: 1440px; margin: 0 auto; padding: 18px 28px 14px; }
.title-row { display: flex; justify-content: space-between; gap: 20px; align-items: flex-start; }
h1 { margin: 0; font-size: 24px; line-height: 1.2; letter-spacing: 0; }
.subtitle { margin: 6px 0 0; color: var(--muted); font-size: 13px; }
.summary { display: grid; grid-template-columns: repeat(4, minmax(120px, 1fr)); gap: 10px; min-width: 520px; }
.summary div { border: 1px solid var(--line); background: #fbfcfe; padding: 10px 12px; border-radius: 6px; }
.summary b { display: block; font-size: 20px; }
.summary small { color: var(--muted); font-size: 12px; }
.search-row { display: grid; grid-template-columns: minmax(220px, 1fr) auto; gap: 12px; align-items: center; padding-top: 14px; }
.search-box { width: 100%; border: 1px solid var(--line); border-radius: 6px; padding: 11px 13px; font-size: 14px; color: var(--text); background: #fff; outline: none; }
.search-box:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.12); }
.match-count { color: var(--muted); font-size: 13px; white-space: nowrap; }
main { max-width: 1440px; margin: 0 auto; padding: 24px 28px 48px; }
.catalog-head { display: flex; justify-content: space-between; gap: 16px; align-items: flex-end; padding: 0 0 10px; border-bottom: 1px solid var(--line); }
.catalog-head p { margin: 4px 0 0; color: var(--muted); font-size: 13px; }
.empty-state { display: none; border: 1px solid var(--line); background: #fff; border-radius: 8px; padding: 18px; color: var(--muted); margin-top: 14px; }
.section-head { display: flex; justify-content: space-between; gap: 16px; align-items: flex-end; padding: 0 0 10px; border-bottom: 1px solid var(--line); }
h2 { margin: 0; font-size: 20px; letter-spacing: 0; }
.section-head p { margin: 4px 0 0; color: var(--muted); font-size: 13px; }
.back-top { color: var(--muted); text-decoration: none; font-size: 12px; }

/* Category Metrics Dashboard */
.cat-metrics-panel {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 12px;
  background: #f8fafc;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px 16px;
  margin: 10px 0 16px;
}
.cat-metric-item {
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.cat-metric-item span {
  font-size: 11px;
  color: var(--muted);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.cat-metric-item b {
  font-size: 13px;
  color: var(--text);
}

.product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(520px, 1fr)); gap: 12px; padding-top: 14px; }
.product-card { display: grid; grid-template-columns: 132px 1fr; gap: 14px; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 12px; min-height: 190px; }
.product-card.hidden { display: none; }
.thumb { display: flex; align-items: center; justify-content: center; border: 1px solid var(--line); border-radius: 6px; background: #f9fafb; aspect-ratio: 1 / 1; overflow: hidden; }
.thumb img { width: 100%; height: 100%; object-fit: contain; }
.no-img { color: var(--muted); font-size: 12px; }
.product-topline { display: flex; justify-content: space-between; gap: 12px; align-items: center; margin-bottom: 5px; }
.asin { color: var(--accent); font-weight: 700; text-decoration: none; font-size: 13px; }
.score { color: var(--accent-2); background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 3px 7px; font-size: 12px; font-weight: 700; }
.ip-risk { display: inline-flex; align-items: center; border-radius: 6px; padding: 2px 7px; font-size: 11px; font-weight: 700; margin-left: 6px; cursor: help; white-space: nowrap; }
.ip-high { color: #991b1b; background: #fef2f2; border: 1px solid #fca5a5; }
.ip-medium { color: #78350f; background: #fffbeb; border: 1px solid #fcd34d; }
.ip-low { color: #166534; background: #f0fdf4; border: 1px solid #86efac; }
h3 { margin: 0; font-size: 15px; line-height: 1.35; letter-spacing: 0; }
.brand { color: var(--muted); font-size: 12px; margin: 4px 0 8px; }
.tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 9px; }
.tag { display: inline-flex; align-items: center; min-height: 24px; border-radius: 999px; border: 1px solid #bfdbfe; background: #eff6ff; color: #1d4ed8; padding: 3px 8px; font-size: 12px; font-weight: 700; }
.external-links { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 9px; }
.link-btn { display: inline-flex; align-items: center; justify-content: center; min-height: 28px; padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 12px; font-weight: 700; border: 1px solid var(--line); }
.link-btn.amazon { color: #7c2d12; background: #fff7ed; border-color: #fed7aa; }
.link-btn.sprite { color: #065f46; background: #ecfdf5; border-color: #a7f3d0; }
.metrics { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; }
.metrics span { background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 6px; padding: 6px 7px; min-width: 0; }
.metrics b { display: block; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.metrics small { color: var(--muted); font-size: 11px; }
.submetrics { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; color: #475467; font-size: 12px; }
.submetrics span { border: 1px solid #e5e7eb; border-radius: 6px; padding: 3px 6px; background: #fff; }
.reasons { margin: 9px 0 0; padding-left: 18px; color: var(--good); font-size: 12px; line-height: 1.45; }
.cautions { margin-top: 8px; color: var(--warn); font-size: 12px; }
@media (max-width: 900px) {
  .title-row { flex-direction: column; }
  .summary { min-width: 0; width: 100%; grid-template-columns: repeat(2, 1fr); }
  .search-row { grid-template-columns: 1fr; }
  .product-grid { grid-template-columns: 1fr; }
  .cat-metrics-panel { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 560px) {
  .header-inner, main { padding-left: 14px; padding-right: 14px; }
  .product-card { grid-template-columns: 1fr; }
  .thumb { max-width: 180px; }
  .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}"""


def render_index(products: list[dict], pool_index: list[tuple]) -> str:
    scored_items = []
    for p in products:
        if not p.get("asin"):
            continue
        pool_entry = match_pool(p.get("leaf_category") or "", pool_index)
        score, reasons, cautions = score_product(p, pool_entry)
        scored_items.append((p, score, reasons, cautions))

    scored_items.sort(
        key=lambda item: (
            item[1],
            _parse_int(item[0].get("monthly_sales")) or 0,
            item[0].get("asin") or "",
        ),
        reverse=True,
    )

    total_products = len(scored_items)
    total_cats = len({p.get("leaf_category") or "UNKNOWN" for p, *_ in scored_items})
    total_tags = len({tag for p, *_ in scored_items for tag in (p.get("scene_tags") or [])})
    cards_html = "".join(render_card(*item) for item in scored_items)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Amazon 产品候选清单</title>
<style>
{CSS}
</style>
</head>
<body>
<header class="header" id="top">
  <div class="header-inner">
    <div class="title-row">
      <div>
        <h1>Amazon 产品候选清单</h1>
        <p class="subtitle">平铺展示全部候选商品，可按 title、ASIN、品牌、leaf category 和场景标签搜索。数据源：products/manual_asins_details.json。</p>
      </div>
      <div class="summary">
        <div><b>{total_products}</b><small>候选产品</small></div>
        <div><b>{total_cats}</b><small>Leaf Categories</small></div>
        <div><b>{total_tags}</b><small>场景标签</small></div>
        <div><b>{len(products)}</b><small>总观察产品</small></div>
      </div>
    </div>
    <div class="search-row">
      <input id="productSearch" class="search-box" type="search" placeholder="搜索 title / ASIN / 品牌 / 类目 / 场景标签，例如 patio、gift、户外庭院" autocomplete="off">
      <div class="match-count"><b id="visibleCount">{total_products}</b> / {total_products} products</div>
    </div>
  </div>
</header>
<main>
  <section class="catalog">
    <div class="catalog-head">
      <div>
        <h2>全部商品</h2>
        <p>按综合评分和月销量排序；每张卡片保留原始商品指标，并附加场景、情绪、用途标签。</p>
      </div>
    </div>
    <div id="emptyState" class="empty-state">没有匹配的商品。</div>
    <div id="productGrid" class="product-grid">{cards_html}</div>
  </section>
</main>
<script>
const searchInput = document.getElementById('productSearch');
const cards = Array.from(document.querySelectorAll('.product-card'));
const visibleCount = document.getElementById('visibleCount');
const emptyState = document.getElementById('emptyState');

function normalize(value) {{
  return value.toLowerCase().trim();
}}

function applySearch() {{
  const terms = normalize(searchInput.value).split(/\\s+/).filter(Boolean);
  let count = 0;
  for (const card of cards) {{
    const haystack = card.dataset.search || '';
    const matched = terms.every(term => haystack.includes(term));
    card.classList.toggle('hidden', !matched);
    if (matched) count += 1;
  }}
  visibleCount.textContent = count;
  emptyState.style.display = count ? 'none' : 'block';
}}

searchInput.addEventListener('input', applySearch);
</script>
</body>
</html>
"""


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    products: list[dict] = data.get("products", [])
    print(f"Loaded {len(products)} products from {SOURCE.relative_to(ROOT)}")
    if ensure_scene_tags(products):
        SOURCE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("Updated scene_tags in products/manual_asins_details.json")

    pool_data = json.loads(CATEGORY_POOL.read_text(encoding="utf-8"))
    pool = pool_data.get("target_pool", [])
    pool_index = build_pool_index(pool)
    print(f"Loaded {len(pool)} category pool entries")

    content = render_index(products, pool_index)
    # Normalise line endings
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    OUTPUT.write_text(content, encoding="utf-8")

    # Count for reporting
    cats = {p.get("leaf_category") or "UNKNOWN" for p in products if p.get("asin")}
    print(f"Wrote {OUTPUT.relative_to(ROOT)} — {len(products)} products, {len(cats)} categories")
    print("Run  python3 patch_ip_risk.py  to inject IP risk badges.")


if __name__ == "__main__":
    main()
