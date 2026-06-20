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
SCENARIO_DIR = ROOT / "keyword" / "scenario"
OUTPUT = ROOT / "index.html"

_SRC_LABEL = {
    "wind chime":    ("wind",  "Wind Chime",    "kw-src-wind"),
    "metal yard art":("metal", "Metal Yard Art", "kw-src-metal"),
    "patio decor":   ("patio", "Patio Decor",   "kw-src-patio"),
}


def load_keywords() -> list[dict]:
    seen: dict[str, dict] = {}
    for path in sorted(SCENARIO_DIR.glob("*mining*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        seed = data.get("seed_keyword", "")
        src_key, src_label, src_cls = _SRC_LABEL.get(seed, (seed[:5], seed, "kw-src-wind"))
        for kw in data.get("keywords", []):
            name = kw.get("keyword", "").strip().lower()
            if not name or name in seen:
                continue
            top3 = kw.get("top3") or []
            aba_top1 = top3[0]["click_share"] if top3 else None
            aba_top3 = sum(t["click_share"] for t in top3[:3]) if top3 else None
            seen[name] = {
                "keyword":       kw.get("keyword", ""),
                "keyword_zh":    kw.get("keyword_zh", ""),
                "source_seed":   seed,
                "source_label":  src_label,
                "source_cls":    src_cls,
                "ac_recommended": kw.get("ac_recommended", False),
                "monthly_searches": kw.get("monthly_searches") or 0,
                "purchase_rate": kw.get("purchase_rate"),
                "ppc_suggested": kw.get("ppc_suggested"),
                "title_density": kw.get("title_density"),
                "supply_demand_ratio": kw.get("supply_demand_ratio"),
                "competing_products": kw.get("competing_products"),
                "avg_price":     kw.get("avg_price"),
                "aba_top1":      aba_top1,
                "aba_top3":      aba_top3,
                "relevance":     kw.get("relevance"),
            }
    return sorted(seen.values(), key=lambda k: k["monthly_searches"], reverse=True)

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
    is_pick = bool(product.get("new_store_pick"))
    pick_reason = product.get("pick_reason", "")
    search_text = " ".join(
        str(value or "")
        for value in (
            asin,
            product.get("title"),
            product.get("brand"),
            product.get("leaf_category"),
            " ".join(tags),
            "推荐新店 new store pick" if is_pick else "",
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

    pick_class = " is-pick" if is_pick else ""
    pick_badge_html = (
        f'<span class="pick-badge" title="{esc(pick_reason)}">★ 推荐新店</span>'
        if is_pick else ""
    )

    return f"""
        <article class="product-card{pick_class}" data-search="{esc(search_text)}">
          <a class="thumb" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">
            {image_html}
          </a>
          <div class="product-main">
            <div class="product-topline">
              <a class="asin" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">{esc(asin)}</a>{pick_badge_html}
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
.pick-badge { display: inline-flex; align-items: center; gap: 4px; border-radius: 6px; padding: 2px 8px; font-size: 11px; font-weight: 700; background: #fdf4ff; border: 1px solid #d946ef; color: #86198f; margin-left: 6px; white-space: nowrap; cursor: help; }
.product-card.is-pick { border-color: #e879f9; box-shadow: 0 0 0 2px #fdf4ff; }
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
}
/* ── Tabs ── */
.tab-nav { display: flex; gap: 0; border-bottom: 2px solid var(--line); margin-top: 14px; }
.tab-btn { background: none; border: none; border-bottom: 3px solid transparent; margin-bottom: -2px; padding: 8px 20px; font-size: 14px; font-weight: 600; color: var(--muted); cursor: pointer; transition: color .15s, border-color .15s; }
.tab-btn:hover { color: var(--text); }
.tab-btn.active { color: var(--accent); border-bottom-color: var(--accent); }
.tab-panel { display: none; }
.tab-panel.active { display: block; }
/* ── Keyword table ── */
.kw-toolbar { display: flex; gap: 12px; align-items: center; padding: 14px 0 10px; flex-wrap: wrap; }
.kw-search { flex: 1; min-width: 220px; border: 1px solid var(--line); border-radius: 6px; padding: 9px 13px; font-size: 14px; outline: none; }
.kw-search:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(15,118,110,.12); }
.kw-count { color: var(--muted); font-size: 13px; white-space: nowrap; }
.kw-table-wrap { overflow-x: auto; }
table.kw-table { width: 100%; border-collapse: collapse; font-size: 13px; }
table.kw-table th { position: sticky; top: 0; background: #f1f5f9; border: 1px solid var(--line); padding: 8px 10px; text-align: left; white-space: nowrap; cursor: pointer; user-select: none; font-size: 12px; }
table.kw-table th:hover { background: #e2e8f0; }
table.kw-table th.sorted-asc::after { content: " ▲"; }
table.kw-table th.sorted-desc::after { content: " ▼"; }
table.kw-table td { border: 1px solid #e5e7eb; padding: 7px 10px; vertical-align: middle; }
table.kw-table tr.kw-hidden { display: none; }
table.kw-table tbody tr:hover { background: #f8fafc; }
.kw-name { font-weight: 600; color: var(--text); max-width: 260px; }
.kw-src { display: inline-block; border-radius: 999px; padding: 2px 8px; font-size: 11px; font-weight: 700; white-space: nowrap; }
.kw-src-wind  { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
.kw-src-metal { background: #fef3c7; color: #92400e; border: 1px solid #fcd34d; }
.kw-src-patio { background: #f0fdf4; color: #166534; border: 1px solid #86efac; }
.kw-num { text-align: right; font-variant-numeric: tabular-nums; }
.c-great { color: #166534; font-weight: 700; }
.c-good  { color: #0f766e; }
.c-warn  { color: #b45309; }
.c-bad   { color: #991b1b; font-weight: 700; }
.ac-yes  { color: #166534; font-weight: 700; }"""


def _fmt_pct(v) -> str:
    if v is None:
        return "—"
    return f"{float(v)*100:.1f}%"


def _fmt_ppc(v) -> str:
    if v is None or str(v).strip() == "":
        return "—"
    try:
        return f"${float(str(v).replace('$','').strip()):.2f}"
    except ValueError:
        return str(v)


def _color_pr(v) -> str:
    if v is None:
        return ""
    p = float(v) * 100
    if p >= 8:
        return "c-great"
    if p >= 5:
        return "c-good"
    if p >= 2:
        return "c-warn"
    return "c-bad"


def _color_ppc(v) -> str:
    if v is None or str(v).strip() == "":
        return ""
    try:
        p = float(str(v).replace("$", "").strip())
    except ValueError:
        return ""
    if p <= 0.45:
        return "c-great"
    if p <= 0.65:
        return "c-good"
    if p <= 0.80:
        return "c-warn"
    return "c-bad"


def _color_td(v) -> str:
    if v is None:
        return ""
    td = int(v)
    if td <= 4:
        return "c-great"
    if td <= 10:
        return "c-good"
    if td <= 20:
        return "c-warn"
    return "c-bad"


def _color_sdr(v) -> str:
    if v is None:
        return ""
    s = float(v)
    if s >= 80:
        return "c-great"
    if s >= 30:
        return "c-good"
    if s >= 10:
        return "c-warn"
    return "c-bad"


def _color_aba(v) -> str:
    if v is None:
        return ""
    a = float(v) * 100
    if a <= 20:
        return "c-great"
    if a <= 35:
        return "c-good"
    if a <= 50:
        return "c-warn"
    return "c-bad"


def render_keyword_table(keywords: list[dict]) -> str:
    rows = []
    for i, kw in enumerate(keywords):
        pr_cls   = _color_pr(kw["purchase_rate"])
        ppc_cls  = _color_ppc(kw["ppc_suggested"])
        td_cls   = _color_td(kw["title_density"])
        sdr_cls  = _color_sdr(kw["supply_demand_ratio"])
        ab1_cls  = _color_aba(kw["aba_top1"])
        ab3_cls  = _color_aba(kw["aba_top3"])
        ac_badge = '<span class="ac-yes">✓ AC</span>' if kw["ac_recommended"] else ""
        src_span = (f'<span class="kw-src {kw["source_cls"]}">'
                    f'{kw["source_label"]}</span>')
        ms = kw["monthly_searches"]
        ms_fmt = f"{ms:,}" if ms else "—"
        rows.append(
            f'<tr data-ms="{ms}" data-pr="{kw["purchase_rate"] or 0}" '
            f'data-ppc="{kw["ppc_suggested"] or 9999}" '
            f'data-td="{kw["title_density"] if kw["title_density"] is not None else 9999}" '
            f'data-sdr="{kw["supply_demand_ratio"] or 0}" '
            f'data-aba3="{kw["aba_top3"] or 1}">'
            f'<td class="kw-name">{kw["keyword"]}<br>'
            f'<small style="color:var(--muted);font-weight:400">{kw["keyword_zh"]}</small> {ac_badge}</td>'
            f'<td>{src_span}</td>'
            f'<td class="kw-num">{ms_fmt}</td>'
            f'<td class="kw-num {pr_cls}">{_fmt_pct(kw["purchase_rate"])}</td>'
            f'<td class="kw-num {ppc_cls}">{_fmt_ppc(kw["ppc_suggested"])}</td>'
            f'<td class="kw-num {td_cls}">{kw["title_density"] if kw["title_density"] is not None else "—"}</td>'
            f'<td class="kw-num {sdr_cls}">{kw["supply_demand_ratio"] if kw["supply_demand_ratio"] is not None else "—"}</td>'
            f'<td class="kw-num {ab1_cls}">{_fmt_pct(kw["aba_top1"])}</td>'
            f'<td class="kw-num {ab3_cls}">{_fmt_pct(kw["aba_top3"])}</td>'
            f'<td class="kw-num">{kw["avg_price"] or "—"}</td>'
            f'<td class="kw-num">{kw["competing_products"] if kw["competing_products"] is not None else "—"}</td>'
            f'</tr>'
        )
    rows_html = "\n".join(rows)
    return f"""
<div class="kw-toolbar">
  <input id="kwSearch" class="kw-search" type="search" placeholder="搜索关键词…" autocomplete="off">
  <span class="kw-count">共 <b id="kwCount">{len(keywords)}</b> / {len(keywords)} 个关键词</span>
</div>
<div class="kw-table-wrap">
<table class="kw-table" id="kwTable">
<thead>
<tr>
  <th data-col="name">关键词</th>
  <th data-col="src">来源</th>
  <th data-col="ms" class="sorted-desc">月搜索量</th>
  <th data-col="pr">购买率</th>
  <th data-col="ppc">PPC 建议</th>
  <th data-col="td">标题密度</th>
  <th data-col="sdr">需供比 SDR</th>
  <th data-col="aba1">ABA Top1</th>
  <th data-col="aba3">ABA Top3</th>
  <th data-col="price">均价</th>
  <th data-col="cp">竞品数</th>
</tr>
</thead>
<tbody>
{rows_html}
</tbody>
</table>
</div>"""


def render_index(products: list[dict], pool_index: list[tuple], keywords: list[dict] | None = None) -> str:
    from patch_ip_risk import assess_ip_risk
    scored_items = []
    skipped_high = 0
    for p in products:
        if not p.get("asin"):
            continue
        if assess_ip_risk(p)[0] == "high":
            skipped_high += 1
            continue
        pool_entry = match_pool(p.get("leaf_category") or "", pool_index)
        score, reasons, cautions = score_product(p, pool_entry)
        scored_items.append((p, score, reasons, cautions))
    if skipped_high:
        print(f"  Excluded {skipped_high} high-risk products from index")

    scored_items.sort(
        key=lambda item: (
            1 if item[0].get("new_store_pick") else 0,
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

    kw_list = keywords or []
    kw_section = render_keyword_table(kw_list) if kw_list else "<p style='color:var(--muted)'>暂无关键词数据</p>"
    total_kw = len(kw_list)

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
        <p class="subtitle">平铺展示全部候选商品，可按 title、ASIN、品牌、leaf category 和场景标签搜索；输入 <b>推荐新店</b> 快速筛选新店精选产品。数据源：products/manual_asins_details.json。</p>
      </div>
      <div class="summary">
        <div><b>{total_products}</b><small>候选产品</small></div>
        <div><b>{total_cats}</b><small>Leaf Categories</small></div>
        <div><b>{total_kw}</b><small>关键词</small></div>
        <div><b>{len(products)}</b><small>总观察产品</small></div>
      </div>
    </div>
    <nav class="tab-nav">
      <button class="tab-btn active" onclick="switchTab('products', this)">产品候选 ({total_products})</button>
      <button class="tab-btn" onclick="switchTab('keywords', this)">关键词机会 ({total_kw})</button>
    </nav>
  </div>
</header>
<main>
  <!-- Products tab -->
  <div id="tab-products" class="tab-panel active">
    <div style="padding: 12px 0 0">
      <div class="search-row" style="margin-top:0">
        <input id="productSearch" class="search-box" type="search" placeholder="搜索 title / ASIN / 品牌 / 类目 / 场景标签；输入「推荐新店」筛选精选产品" autocomplete="off">
        <div class="match-count"><b id="visibleCount">{total_products}</b> / {total_products} products</div>
      </div>
    </div>
    <section class="catalog">
      <div id="emptyState" class="empty-state">没有匹配的商品。</div>
      <div id="productGrid" class="product-grid">{cards_html}</div>
    </section>
  </div>
  <!-- Keywords tab -->
  <div id="tab-keywords" class="tab-panel">
    <div style="padding: 10px 0 4px">
      <p style="color:var(--muted);font-size:13px;margin:0">来源：3 个关键词挖掘文件（wind chime / metal yard art / patio decor），月搜索 ≥ 5,000，PPC ≤ $0.80。颜色含义：<span class="c-great">■ 优秀</span> <span class="c-good">■ 良好</span> <span class="c-warn">■ 注意</span> <span class="c-bad">■ 风险</span></p>
    </div>
    {kw_section}
  </div>
</main>
<script>
// ── Tab switching ──
function switchTab(name, btn) {{
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + name).classList.add('active');
  btn.classList.add('active');
}}

// ── Product search ──
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

// ── Keyword search + sort ──
const kwSearch = document.getElementById('kwSearch');
const kwCount = document.getElementById('kwCount');
const kwTable = document.getElementById('kwTable');

function applyKwSearch() {{
  if (!kwSearch || !kwTable) return;
  const term = kwSearch.value.toLowerCase().trim();
  let count = 0;
  const rows = kwTable.querySelectorAll('tbody tr');
  for (const row of rows) {{
    const text = row.textContent.toLowerCase();
    const hidden = term && !text.includes(term);
    row.classList.toggle('kw-hidden', hidden);
    if (!hidden) count++;
  }}
  if (kwCount) kwCount.textContent = count;
}}

if (kwSearch) kwSearch.addEventListener('input', applyKwSearch);

// sortable table
let sortCol = 'ms', sortDesc = true;

const colDataKey = {{
  ms: r => parseFloat(r.dataset.ms) || 0,
  pr: r => parseFloat(r.dataset.pr) || 0,
  ppc: r => parseFloat(r.dataset.ppc) || 9999,
  td: r => parseFloat(r.dataset.td) || 9999,
  sdr: r => parseFloat(r.dataset.sdr) || 0,
  aba3: r => parseFloat(r.dataset.aba3) || 1,
  name: r => r.cells[0].textContent.trim(),
  src: r => r.cells[1].textContent.trim(),
  price: r => parseFloat((r.cells[9].textContent || '0').replace(/[^0-9.]/g, '')) || 0,
  cp: r => parseFloat(r.cells[10].textContent) || 0,
  aba1: r => parseFloat(r.dataset.aba3) || 1,
}};

const colIndex = {{ms:2, pr:3, ppc:4, td:5, sdr:6, aba1:7, aba3:8, price:9, cp:10, name:0, src:1}};

function sortKwTable(col) {{
  if (!kwTable) return;
  if (sortCol === col) {{
    sortDesc = !sortDesc;
  }} else {{
    sortCol = col;
    sortDesc = ['ms','pr','sdr','price','cp'].includes(col) ? true : false;
  }}
  const ths = kwTable.querySelectorAll('thead th');
  ths.forEach(th => th.classList.remove('sorted-asc','sorted-desc'));
  const idx = colIndex[col];
  if (idx !== undefined) {{
    ths[idx].classList.add(sortDesc ? 'sorted-desc' : 'sorted-asc');
  }}
  const tbody = kwTable.querySelector('tbody');
  const rows = Array.from(tbody.querySelectorAll('tr'));
  const getter = colDataKey[col] || (r => r.textContent);
  rows.sort((a, b) => {{
    const va = getter(a), vb = getter(b);
    if (typeof va === 'string') return sortDesc ? vb.localeCompare(va) : va.localeCompare(vb);
    return sortDesc ? vb - va : va - vb;
  }});
  rows.forEach(r => tbody.appendChild(r));
}}

if (kwTable) {{
  kwTable.querySelectorAll('thead th').forEach(th => {{
    th.addEventListener('click', () => sortKwTable(th.dataset.col || 'ms'));
  }});
}}
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

    keywords = load_keywords()

    content = render_index(products, pool_index, keywords)
    # Normalise line endings
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    OUTPUT.write_text(content, encoding="utf-8")

    # Count for reporting
    cats = {p.get("leaf_category") or "UNKNOWN" for p in products if p.get("asin")}
    print(f"Wrote {OUTPUT.relative_to(ROOT)} — {len(products)} products, {len(cats)} categories")
    print("Run  python3 patch_ip_risk.py  to inject IP risk badges.")


if __name__ == "__main__":
    main()
