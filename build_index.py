#!/usr/bin/env python3
from __future__ import annotations

import collections
import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "products" / "top_product_candidates.json"
OUTPUT = ROOT / "index.html"


def esc(value) -> str:
    return html.escape(str(value if value is not None else ""), quote=True)


def short(value, max_len: int = 120) -> str:
    text = " ".join(str(value or "").split())
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def safe_num(value) -> float | None:
    if value in (None, "", "-"):
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", str(value).replace(",", ""))
    return float(match.group(0)) if match else None


def render_index(data: dict) -> str:
    products = data["top_products"]
    groups: dict[str, list[dict]] = collections.defaultdict(list)
    for product in products:
        groups[product.get("leaf_category") or "UNKNOWN"].append(product)
    ordered = sorted(groups.items(), key=lambda item: (-len(item[1]), item[0]))

    category_nav = "".join(
        f'<a href="#cat-{index}">{esc(name)} <span>{len(items)}</span></a>'
        for index, (name, items) in enumerate(ordered, 1)
    )

    sections = []
    for index, (name, items) in enumerate(ordered, 1):
        avg_score = sum(float(item.get("_score") or 0) for item in items) / len(items)
        total_sales = sum(safe_num(item.get("monthly_sales")) or 0 for item in items)
        cards = []
        for product in items:
            asin = product.get("asin", "")
            amazon_url = f"https://www.amazon.com/dp/{asin}"
            sellersprite_url = (
                "https://www.sellersprite.com/v3/competitor-lookup"
                f"?market=US&monthName=bsr_sales_nearly&asins=%5B%22{asin}%22%5D"
                "&page=1&nodeIdPaths=%5B%5D&symbolFlag=true&size=60"
                "&order%5Bfield%5D=amz_unit&order%5Bdesc%5D=true&lowPrice=N"
            )
            image_url = product.get("image_url") or ""
            reasons = "".join(
                f"<li>{esc(reason)}</li>" for reason in (product.get("_reasons") or [])[:4]
            )
            cautions = product.get("_cautions") or []
            caution_html = (
                f'<div class="cautions">{esc("；".join(cautions))}</div>'
                if cautions
                else ""
            )
            image_html = (
                f'<img src="{esc(image_url)}" alt="{esc(product.get("title", ""))}" loading="lazy">'
                if image_url
                else '<div class="no-img">No image</div>'
            )
            cards.append(
                f"""
        <article class="product-card">
          <a class="thumb" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">
            {image_html}
          </a>
          <div class="product-main">
            <div class="product-topline">
              <a class="asin" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">{esc(asin)}</a>
              <span class="score">Score {esc(product.get("_score", ""))}</span>
            </div>
            <h3>{esc(short(product.get("title", ""), 150))}</h3>
            <div class="brand">{esc(product.get("brand") or "Unknown brand")}</div>
            <div class="external-links">
              <a class="link-btn amazon" href="{esc(amazon_url)}" target="_blank" rel="noreferrer">Amazon</a>
              <a class="link-btn sprite" href="{esc(sellersprite_url)}" target="_blank" rel="noreferrer">卖家精灵</a>
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
              <span>上架 {esc(product.get("listing_date"))} {esc(product.get("listing_age"))}</span>
            </div>
            <ul class="reasons">{reasons}</ul>
            {caution_html}
          </div>
        </article>"""
            )
        sections.append(
            f"""
    <section class="category-section" id="cat-{index}">
      <div class="section-head">
        <div>
          <h2>{esc(name)}</h2>
          <p>{len(items)} products · avg score {avg_score:.1f} · combined monthly sales {total_sales:,.0f}</p>
        </div>
        <a href="#top" class="back-top">Back to top</a>
      </div>
      <div class="product-grid">{''.join(cards)}</div>
    </section>"""
        )

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Amazon 产品候选清单</title>
<style>
:root {{
  --bg: #f6f7f9;
  --panel: #ffffff;
  --text: #18202a;
  --muted: #667085;
  --line: #d9dee7;
  --accent: #0f766e;
  --accent-2: #b45309;
  --good: #166534;
  --warn: #9a3412;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: var(--bg); color: var(--text); }}
a {{ color: inherit; }}
.header {{ background: #ffffff; border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 10; }}
.header-inner {{ max-width: 1440px; margin: 0 auto; padding: 18px 28px 14px; }}
.title-row {{ display: flex; justify-content: space-between; gap: 20px; align-items: flex-start; }}
h1 {{ margin: 0; font-size: 24px; line-height: 1.2; letter-spacing: 0; }}
.subtitle {{ margin: 6px 0 0; color: var(--muted); font-size: 13px; }}
.summary {{ display: grid; grid-template-columns: repeat(4, minmax(120px, 1fr)); gap: 10px; min-width: 520px; }}
.summary div {{ border: 1px solid var(--line); background: #fbfcfe; padding: 10px 12px; border-radius: 6px; }}
.summary b {{ display: block; font-size: 20px; }}
.summary small {{ color: var(--muted); font-size: 12px; }}
.nav {{ display: flex; gap: 8px; overflow-x: auto; padding-top: 14px; }}
.nav a {{ flex: 0 0 auto; text-decoration: none; border: 1px solid var(--line); border-radius: 6px; padding: 7px 10px; font-size: 12px; color: #344054; background: #fff; }}
.nav span {{ color: var(--accent); font-weight: 700; }}
main {{ max-width: 1440px; margin: 0 auto; padding: 24px 28px 48px; }}
.category-section {{ margin-bottom: 30px; }}
.section-head {{ display: flex; justify-content: space-between; gap: 16px; align-items: flex-end; padding: 0 0 10px; border-bottom: 1px solid var(--line); }}
h2 {{ margin: 0; font-size: 20px; letter-spacing: 0; }}
.section-head p {{ margin: 4px 0 0; color: var(--muted); font-size: 13px; }}
.back-top {{ color: var(--muted); text-decoration: none; font-size: 12px; }}
.product-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(520px, 1fr)); gap: 12px; padding-top: 14px; }}
.product-card {{ display: grid; grid-template-columns: 132px 1fr; gap: 14px; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 12px; min-height: 190px; }}
.thumb {{ display: flex; align-items: center; justify-content: center; border: 1px solid var(--line); border-radius: 6px; background: #f9fafb; aspect-ratio: 1 / 1; overflow: hidden; }}
.thumb img {{ width: 100%; height: 100%; object-fit: contain; }}
.no-img {{ color: var(--muted); font-size: 12px; }}
.product-topline {{ display: flex; justify-content: space-between; gap: 12px; align-items: center; margin-bottom: 5px; }}
.asin {{ color: var(--accent); font-weight: 700; text-decoration: none; font-size: 13px; }}
.score {{ color: var(--accent-2); background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 3px 7px; font-size: 12px; font-weight: 700; }}
h3 {{ margin: 0; font-size: 15px; line-height: 1.35; letter-spacing: 0; }}
.brand {{ color: var(--muted); font-size: 12px; margin: 4px 0 8px; }}
.external-links {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 9px; }}
.link-btn {{ display: inline-flex; align-items: center; justify-content: center; min-height: 28px; padding: 5px 10px; border-radius: 6px; text-decoration: none; font-size: 12px; font-weight: 700; border: 1px solid var(--line); }}
.link-btn.amazon {{ color: #7c2d12; background: #fff7ed; border-color: #fed7aa; }}
.link-btn.sprite {{ color: #065f46; background: #ecfdf5; border-color: #a7f3d0; }}
.metrics {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; }}
.metrics span {{ background: #f8fafc; border: 1px solid #e5e7eb; border-radius: 6px; padding: 6px 7px; min-width: 0; }}
.metrics b {{ display: block; font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.metrics small {{ color: var(--muted); font-size: 11px; }}
.submetrics {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; color: #475467; font-size: 12px; }}
.submetrics span {{ border: 1px solid #e5e7eb; border-radius: 6px; padding: 3px 6px; background: #fff; }}
.reasons {{ margin: 9px 0 0; padding-left: 18px; color: var(--good); font-size: 12px; line-height: 1.45; }}
.cautions {{ margin-top: 8px; color: var(--warn); font-size: 12px; }}
@media (max-width: 900px) {{
  .title-row {{ flex-direction: column; }}
  .summary {{ min-width: 0; width: 100%; grid-template-columns: repeat(2, 1fr); }}
  .product-grid {{ grid-template-columns: 1fr; }}
}}
@media (max-width: 560px) {{
  .header-inner, main {{ padding-left: 14px; padding-right: 14px; }}
  .product-card {{ grid-template-columns: 1fr; }}
  .thumb {{ max-width: 180px; }}
  .metrics {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
}}
</style>
</head>
<body>
<header class="header" id="top">
  <div class="header-inner">
    <div class="title-row">
      <div>
        <h1>Amazon 产品候选清单</h1>
        <p class="subtitle">按 Leaf Category 分组展示；暂不包含 keyword 内容。数据来自 products/top_product_candidates.json。</p>
      </div>
      <div class="summary">
        <div><b>{len(products)}</b><small>优先候选产品</small></div>
        <div><b>{data.get('qualified_parseable_count')}</b><small>可评分商品</small></div>
        <div><b>{data.get('total_products')}</b><small>Combined 抓取商品</small></div>
        <div><b>{len(ordered)}</b><small>Leaf Categories</small></div>
      </div>
    </div>
    <nav class="nav">{category_nav}</nav>
  </div>
</header>
<main>
  {''.join(sections)}
</main>
</body>
</html>
"""


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    content = "\n".join(line.rstrip() for line in render_index(data).splitlines()) + "\n"
    OUTPUT.write_text(content, encoding="utf-8")
    products = data["top_products"]
    groups = {product.get("leaf_category") or "UNKNOWN" for product in products}
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(products)} products in {len(groups)} groups")


if __name__ == "__main__":
    main()
