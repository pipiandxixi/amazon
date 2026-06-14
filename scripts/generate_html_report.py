#!/usr/bin/env python3
"""Generate a self-contained HTML report from pipeline handoff JSONs.

Usage:
  python3 scripts/generate_html_report.py                    # today
  python3 scripts/generate_html_report.py --date 2026_06_14
"""

from __future__ import annotations

import argparse
import datetime
import html as _html
import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from scan_common import dated_results_dir


def _e(s) -> str:
    return _html.escape(str(s) if s is not None else "")


CSS = """
:root{--border:#e5e7eb;--text:#111827;--muted:#6b7280;--bg:#f3f4f6;--card:#fff}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);line-height:1.5}
a{color:inherit;text-decoration:none}
header{background:#1e293b;color:#f1f5f9;padding:1.5rem 2rem}
header h1{font-size:1.5rem;font-weight:700;letter-spacing:-.02em}
header p{color:#94a3b8;font-size:.85rem;margin-top:.3rem}
nav{background:var(--card);padding:.65rem 2rem;border-bottom:1px solid var(--border);display:flex;flex-wrap:wrap;gap:.35rem;position:sticky;top:0;z-index:100;box-shadow:0 1px 4px rgba(0,0,0,.07)}
nav a{padding:.2rem .65rem;border-radius:9999px;font-size:.77rem;font-weight:500}
nav a.green{background:#dcfce7;color:#166534}
nav a.yellow{background:#fef9c3;color:#854d0e}
nav a:hover{opacity:.75}
main{max-width:1400px;margin:0 auto;padding:1.25rem 1.25rem 4rem}
.last-updated{font-size:.72rem;color:var(--muted);margin-top:.4rem}
.cat{background:var(--card);border:1px solid var(--border);border-radius:.75rem;margin-bottom:1.25rem;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.04)}
.cat-header{padding:1.1rem 1.5rem;border-bottom:1px solid var(--border)}
.cat-title{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;margin-bottom:.5rem}
.badge{display:inline-block;padding:.18rem .55rem;border-radius:.375rem;font-size:.73rem;font-weight:700}
.badge.green{background:#dcfce7;color:#166534}
.badge.yellow{background:#fef9c3;color:#854d0e}
h2{font-size:1.05rem;font-weight:700}
h2 small{color:var(--muted);font-weight:400;font-size:.85rem;margin-left:.35rem}
.metrics{display:flex;flex-wrap:wrap;gap:.35rem 1.25rem}
.metric{font-size:.8rem;color:var(--muted)}
.metric strong{color:var(--text);font-weight:600}
details{border-top:1px solid var(--border)}
details>summary{padding:.7rem 1.5rem;cursor:pointer;font-size:.85rem;font-weight:600;color:#374151;list-style:none;display:flex;align-items:center;gap:.5rem;user-select:none}
details>summary::-webkit-details-marker{display:none}
details>summary::before{content:'▶';font-size:.55rem;color:var(--muted);transition:transform .15s;flex-shrink:0}
details[open]>summary::before{transform:rotate(90deg)}
.product-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:.65rem;padding:.85rem 1.5rem 1.25rem}
.pcard{border:1px solid var(--border);border-radius:.5rem;overflow:hidden;font-size:.77rem;transition:box-shadow .15s,transform .15s}
.pcard:hover{box-shadow:0 4px 14px rgba(0,0,0,.09);transform:translateY(-1px)}
.pcard img{width:100%;aspect-ratio:1;object-fit:contain;background:#f8fafc;padding:.2rem;display:block}
.pcard .no-img{width:100%;aspect-ratio:1;background:#f1f5f9;display:flex;align-items:center;justify-content:center;color:var(--muted);font-size:.7rem}
.pcard .pinfo{padding:.45rem .55rem .55rem}
.pasin{font-family:monospace;font-size:.67rem;color:var(--muted);margin-bottom:.15rem}
.ptitle{font-size:.73rem;line-height:1.3;margin:.15rem 0 .4rem;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.pstats{display:grid;grid-template-columns:1fr 1fr;gap:.2rem .4rem}
.pstat{display:flex;flex-direction:column}
.plabel{font-size:.62rem;color:var(--muted)}
.pval{font-weight:600;font-size:.77rem}
.kw-wrap{padding:0 1.5rem 1.1rem;overflow-x:auto}
table.kwtable{width:100%;border-collapse:collapse;font-size:.8rem}
.kwtable th{padding:.4rem .7rem;text-align:left;font-size:.68rem;color:var(--muted);text-transform:uppercase;background:#f9fafb;border-bottom:1px solid var(--border);white-space:nowrap}
.kwtable td{padding:.45rem .7rem;border-bottom:1px solid var(--border);vertical-align:top}
.kwtable tr:last-child td{border-bottom:none}
.kwtable tr:hover td{background:#f9fafb}
.kwtable td:first-child{color:var(--muted);font-size:.75rem;width:2rem}
.kw-zh{color:var(--muted);font-size:.72rem;display:block;margin-top:.1rem}
.no-data{padding:.9rem 1.5rem;color:var(--muted);font-size:.85rem;font-style:italic}
.kw-link{color:#2563eb;text-decoration:underline;text-decoration-color:#93c5fd;text-underline-offset:2px;transition:color .12s}
.kw-link:hover{color:#1d4ed8}
.plinks{display:inline-flex;gap:.2rem;margin-left:.35rem}
.plinks a{font-size:.58rem;padding:.05rem .28rem;border-radius:.25rem;font-weight:700;text-decoration:none;border:1px solid currentColor;line-height:1.4;opacity:.7;transition:opacity .12s}
.plinks a:hover{opacity:1}
.plinks a:first-child{color:#c45500}
.plinks a:last-child{color:#1a6d38}
"""


def _slug(name: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in name.lower()).strip("-")


def _ss_url(asin: str) -> str:
    return (
        f"https://www.sellersprite.com/v3/competitor-lookup?market=US"
        f"&monthName=bsr_sales_nearly&asins=%5B%22{asin}%22%5D"
        f"&page=1&nodeIdPaths=%5B%5D&symbolFlag=false&size=60"
        f"&order%5Bfield%5D=amz_unit&order%5Bdesc%5D=true&lowPrice=N"
    )


def _product_card(p: dict) -> str:
    img_url = p.get("image_url", "")
    img = (f'<img src="{_e(img_url)}" loading="lazy" alt="">'
           if img_url else '<div class="no-img">No image</div>')
    asin = p.get("asin", "")
    return f"""<div class="pcard">
      <a href="https://www.amazon.com/dp/{_e(asin)}" target="_blank" rel="noopener">{img}</a>
      <div class="pinfo">
        <div class="pasin">{_e(asin)}
          <span class="plinks"><a href="https://www.amazon.com/dp/{_e(asin)}" target="_blank" rel="noopener" title="Amazon 商品页">AMZ</a><a href="{_e(_ss_url(asin))}" target="_blank" rel="noopener" title="卖家精灵竞品分析">SS</a></span>
        </div>
        <div class="ptitle">{_e(p.get('title',''))}</div>
        <div class="pstats">
          <div class="pstat"><span class="plabel">价格</span><span class="pval">{_e(p.get('price','-'))}</span></div>
          <div class="pstat"><span class="plabel">月销量</span><span class="pval">{_e(p.get('monthly_sales','-'))}</span></div>
          <div class="pstat"><span class="plabel">评论</span><span class="pval">{_e(p.get('reviews','-'))}</span></div>
          <div class="pstat"><span class="plabel">毛利率</span><span class="pval">{_e(p.get('profit_margin','-'))}</span></div>
          <div class="pstat"><span class="plabel">评分</span><span class="pval">{_e(p.get('rating','-'))} ⭐</span></div>
          <div class="pstat"><span class="plabel">卖家数</span><span class="pval">{_e(p.get('sellers','-'))}</span></div>
        </div>
      </div>
    </div>"""


def _keyword_table(keywords: list[dict], asins: list[str]) -> str:
    if not keywords:
        return '<p class="no-data">该类目无关键词数据。</p>'
    asin_preview = ", ".join(asins[:4]) + ("…" if len(asins) > 4 else "")
    rows = []
    for i, kw in enumerate(keywords, 1):
        rows.append(f"""<tr>
          <td>{i}</td>
          <td><a href="https://www.sellersprite.com/v3/keyword-conversion-rate?marketId=1&reverseType=W&bidMatchType=1&keywordMatchType=all&keywordList={urllib.parse.quote(kw.get('keyword',''))}" target="_blank" rel="noopener" class="kw-link"><strong>{_e(kw.get('keyword',''))}</strong></a><span class="kw-zh">{_e(kw.get('translation',''))}</span></td>
          <td>{_e(kw.get('searches','-'))}</td>
          <td>{_e(kw.get('purchases','-'))}</td>
          <td>{_e(kw.get('traffic_share','-'))}</td>
          <td>{_e(kw.get('spr','-'))}</td>
          <td>{_e(kw.get('title_density','-'))}</td>
          <td>{_e(kw.get('ppc_bid','-'))}</td>
          <td>{_e(kw.get('ad_score','-'))}</td>
        </tr>""")
    return f"""<div class="kw-wrap">
      <p style="font-size:.77rem;color:var(--muted);margin-bottom:.5rem">查询 ASIN: {_e(asin_preview)}</p>
      <table class="kwtable">
        <thead><tr>
          <th>#</th><th>关键词</th><th>月搜索量</th><th>月购买量</th>
          <th>流量占比</th><th>SPR</th><th>标题密度</th><th>PPC竞价</th><th>分数</th>
        </tr></thead>
        <tbody>{"".join(rows)}</tbody>
      </table>
    </div>"""


def _category_section(cat: dict, products: list[dict] | None, kw_entry: dict | None) -> str:
    name = cat["en_name"]
    zh = cat.get("zh_name", "")
    level = cat.get("level", "")
    badge_cls = "green" if "Green" in level else "yellow"
    badge_text = "🟢 推荐" if "Green" in level else "🟡 谨慎"

    last_updated = cat.get("last_updated")
    if last_updated:
        # Format ISO timestamp to readable: "2026-06-14T20:05:00" → "2026-06-14 20:05"
        updated_display = last_updated.replace("T", " ")[:16]
        updated_html = f'<div class="last-updated">最后更新: {_e(updated_display)}</div>'
    else:
        updated_html = '<div class="last-updated">尚未扫描产品数据</div>'

    metrics = f"""<div class="metrics">
      <span class="metric">均价 <strong>${_e(cat.get('price','-'))}</strong></span>
      <span class="metric">评论数 <strong>{_e(cat.get('reviews','-'))}</strong></span>
      <span class="metric">重量 <strong>{_e(cat.get('weight_lbs','-'))} lbs</strong></span>
      <span class="metric">退货率 <strong>{_e(cat.get('return_rate','-'))}%</strong></span>
      <span class="metric">品牌集中度 <strong>{_e(cat.get('brand_conc','-'))}%</strong></span>
      <span class="metric">中国卖家 <strong>{_e(cat.get('cn_ratio','-'))}%</strong></span>
    </div>"""

    if products is None:
        prods = '<p class="no-data">产品数据待扫描。</p>'
        kws = ""
    else:
        if products:
            cards = "".join(_product_card(p) for p in products)
            prods = f"""<details open>
    <summary>产品 ({len(products)})</summary>
    <div class="product-grid">{cards}</div>
  </details>"""
        else:
            prods = """<details>
    <summary>产品 (0)</summary>
    <p class="no-data">该类目在 SellerSprite 产品树导航失败（nav-fallback 碰撞已跳过）。</p>
  </details>"""

        keywords = kw_entry.get("keywords", []) if kw_entry else []
        asins = kw_entry.get("asins", []) if kw_entry else []
        kw_content = _keyword_table(keywords, asins)
        kws = f"""<details open>
    <summary>关键词 ({len(keywords)})</summary>
    {kw_content}
  </details>"""

    return f"""<section class="cat" id="{_slug(name)}">
  <div class="cat-header">
    <div class="cat-title">
      <span class="badge {badge_cls}">{badge_text}</span>
      <h2>{_e(name)}<small>{_e(zh)}</small></h2>
    </div>
    {updated_html}
    {metrics}
  </div>
  {prods}
  {kws}
</section>"""


def update_index(repo_root: Path) -> None:
    """Regenerate the root index.html pointing to the single results/html/report.html."""
    report_path = repo_root / "results" / "html" / "report.html"
    if not report_path.exists():
        return

    html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=results/html/report.html">
<title>Amazon 选品报告</title>
</head>
<body>
<p><a href="results/html/report.html">跳转到选品报告 →</a></p>
</body>
</html>"""

    index_path = repo_root / "index.html"
    index_path.write_text(html, encoding="utf-8")
    print(f"[INDEX] {index_path}")


def generate_from_db(root: Path, db: dict, date_str: str) -> Path:
    """Render the full HTML report from the categories DB dict (in-memory)."""
    cats = list(db.values())
    n_green   = sum(1 for c in cats if "Green"  in c.get("level", ""))
    n_yellow  = sum(1 for c in cats if "Yellow" in c.get("level", ""))
    n_scanned = sum(1 for c in cats if c.get("last_updated"))
    date_display = date_str.replace("_", "-")

    nav_links = "".join(
        f'<a href="#{_slug(c["en_name"])}" class="{"green" if "Green" in c.get("level","") else "yellow"}">'
        f'{_e(c["en_name"])}</a>'
        for c in cats
    )

    sections = "\n".join(
        _category_section(c, c.get("products"), c.get("keywords"))
        for c in cats
    )

    page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Amazon 选品报告 — {date_display}</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Amazon 选品报告</h1>
  <p>{date_display} &nbsp;·&nbsp; {n_green} 绿色推荐 &nbsp;·&nbsp; {n_yellow} 黄色候选 &nbsp;·&nbsp; {n_scanned}/{len(cats)} 类目已扫描产品</p>
</header>
<nav>{nav_links}</nav>
<main>
{sections}
</main>
</body>
</html>"""

    out_dir = root / "html"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "report.html"
    out.write_text(page, encoding="utf-8")
    print(f"[HTML REPORT] {out}")
    update_index(root.parent)
    return out


def generate(root: Path, date_str: str) -> Path:
    """Load categories.json from root and render HTML. Entry point for standalone use."""
    db_path = root / "json" / "categories.json"
    if not db_path.exists():
        raise FileNotFoundError(f"categories.json not found: {db_path}")
    db = json.loads(db_path.read_text(encoding="utf-8"))
    return generate_from_db(root, db, date_str)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default="")
    args = parser.parse_args()
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    root = dated_results_dir(date_str)
    generate(root, date_str)


if __name__ == "__main__":
    main()
