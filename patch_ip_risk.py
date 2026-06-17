#!/usr/bin/env python3
"""Assess IP infringement risk per product and inject a badge into index.html.

Risk levels:
  high   (⛔) — Active, enforced patents/trademarks in this exact product space.
                Directly copying this product type is very likely to trigger an
                Amazon IP complaint or lawsuit.
  medium (⚠)  — Some IP-active participants exist; do patent/trademark searches
                 before entering this type of product.
  low    (✓)  — Highly commoditised, core patents mostly expired or never filed;
                generic designs are generally safe.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRODUCTS_FILE = ROOT / "products" / "manual_asins_details.json"
HTML_FILE = ROOT / "index.html"

# ── IP risk rules ──────────────────────────────────────────────────────────────
# Each rule is (match_fn, level, reason).
# Rules are evaluated in order; first match wins.
# match_fn receives (leaf_category_lower, title_lower).

RULES: list[tuple] = [
    # ── HIGH ─────────────────────────────────────────────────────────────────
    # Magnetic building toys: Magformers / Magna-Tiles have active design &
    # utility patents; one of Amazon's most litigious IP battlegrounds.
    (lambda c, t: "magnetic" in c and ("building" in c or "tile" in c or "magnet" in t),
     "high", "磁力积木专利战(Magformers/Magna-Tiles 持续诉讼)"),

    # MagSafe trademark in title — Apple actively enforces.
    (lambda c, t: "magsafe" in t,
     "high", "标题含 MagSafe 商标(Apple 积极维权)"),

    # Grill Rescue holds US design + utility patents on its bristle-free
    # replaceable-scraper head.  If the ASIN *is* Grill Rescue's own
    # product, the risk label warns against copying it.
    (lambda c, t: "grill" in c and ("grill rescue" in t or ("bristle free" in t and "replaceable" in t)),
     "high", "Grill Rescue 专利保护产品(设计+实用专利，仿制高风险)"),

    # RC / toy cars referencing licensed brands or copyrighted designs.
    (lambda c, t: c in ("cars", "toy cars", "rc cars") and
                  any(b in t for b in ("ferrari", "lamborghini", "porsche", "bmw", "mercedes",
                                       "toyota", "ford", "jeep", "bugatti", "mclaren")),
     "high", "授权品牌车模版权/商标(Mattel/原厂授权)"),

    # ── MEDIUM ───────────────────────────────────────────────────────────────
    # Wireless chargers / charging stations — Qi-open-standard but specific
    # coil layouts, housings, and multi-device arrangements have been patented
    # by Anker, Belkin, etc.
    (lambda c, t: "charging station" in c or "wireless charger" in c,
     "medium", "充电设备设计专利(Anker/Belkin 有效设计专利)"),

    # Grill brushes (general) — bristle-free / electric designs are contested.
    (lambda c, t: "grill brush" in c or "grill cleaner" in c,
     "medium", "烤架刷设计专利(电动/无刷丝设计需专利排查)"),

    # Handheld flashlights — tactical bezel / switch designs (SureFire, Streamlight).
    (lambda c, t: "flashlight" in c,
     "medium", "战术手电外观设计专利(SureFire/Streamlight)"),

    # 3D printer accessories — Bambu Lab & Creality accumulating patents rapidly.
    (lambda c, t: "3d printer" in c or "printer accessor" in c,
     "medium", "3D打印机配件专利(Bambu Lab/Creality 积极申请)"),

    # Snorkeling — Cressi, TUSA, Mares hold design patents on mask frames
    # and mouthpiece/snorkel junction designs.
    (lambda c, t: "snorkel" in c,
     "medium", "浮潜装备设计专利(Cressi/TUSA 面镜框及接口专利)"),

    # Hydration packs — CamelBak's bite-valve design has been enforced.
    (lambda c, t: "hydration" in c,
     "medium", "水合背包咬阀专利(CamelBak 维权记录)"),

    # Battery packs — Anker has some design patents; enforcement is lighter
    # than other categories but worth noting.
    (lambda c, t: "battery pack" in c,
     "medium", "移动电源设计专利(Anker，执行力度较轻)"),

    # Swing trainers — SKLZ, SuperSpeed have utility patents on training aids.
    (lambda c, t: "swing" in c and "trainer" in c,
     "medium", "挥杆训练器实用专利(SKLZ 等品牌)"),

    # Crimpers — Klein Tools / Knipex have some ergonomic-grip design patents.
    (lambda c, t: "crimper" in c,
     "medium", "压线钳设计专利(Klein/Knipex，风险较轻)"),

    # Generic "accessories" bucket is ambiguous; flag for manual review.
    (lambda c, t: c.strip() == "accessories",
     "medium", "类目名过泛，需确认具体配件类型后再做专利排查"),

    # ── LOW ──────────────────────────────────────────────────────────────────
    # Catch-all: everything else is low risk.
    (lambda c, t: True,
     "low", "高度标准化品类，核心专利基本到期，通用设计风险低"),
]


def assess_ip_risk(product: dict) -> tuple[str, str]:
    """Return (level, reason) for a product."""
    leaf = (product.get("leaf_category") or "").lower()
    title = (product.get("title") or "").lower()
    for match_fn, level, reason in RULES:
        try:
            if match_fn(leaf, title):
                return level, reason
        except Exception:
            continue
    return "low", "通用品类，风险低"


LEVEL_HTML = {
    "high":   '<span class="ip-risk ip-high" title="{reason}">⛔ 高风险</span>',
    "medium": '<span class="ip-risk ip-medium" title="{reason}">⚠ 中风险</span>',
    "low":    '<span class="ip-risk ip-low" title="{reason}">✓ 低风险</span>',
}

CSS_BLOCK = """\
.ip-risk { display: inline-flex; align-items: center; border-radius: 6px; padding: 2px 7px; font-size: 11px; font-weight: 700; margin-left: 6px; cursor: help; white-space: nowrap; }
.ip-high { color: #991b1b; background: #fef2f2; border: 1px solid #fca5a5; }
.ip-medium { color: #78350f; background: #fffbeb; border: 1px solid #fcd34d; }
.ip-low { color: #166534; background: #f0fdf4; border: 1px solid #86efac; }"""


def main() -> None:
    # 1. Load products
    data = json.loads(PRODUCTS_FILE.read_text(encoding="utf-8"))
    products = data.get("products", [])
    print(f"Loaded {len(products)} products")

    # 2. Build ASIN → badge HTML mapping
    asin_badge: dict[str, str] = {}
    counts = {"high": 0, "medium": 0, "low": 0}
    for product in products:
        asin = product.get("asin")
        if not asin:
            continue
        level, reason = assess_ip_risk(product)
        counts[level] += 1
        badge = LEVEL_HTML[level].format(reason=reason)
        asin_badge[asin] = badge

    print(f"  high={counts['high']}  medium={counts['medium']}  low={counts['low']}")

    # 3. Read index.html
    html = HTML_FILE.read_text(encoding="utf-8")

    # 4. Add CSS (once, right after .score { ... } rule)
    if "ip-risk" not in html:
        html = html.replace(
            ".score { color: var(--accent-2); background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 3px 7px; font-size: 12px; font-weight: 700; }",
            ".score { color: var(--accent-2); background: #fff7ed; border: 1px solid #fed7aa; border-radius: 6px; padding: 3px 7px; font-size: 12px; font-weight: 700; }\n" + CSS_BLOCK,
        )
        print("  CSS block injected")
    else:
        print("  CSS block already present, skipped")

    # 5. Inject badge after each ASIN anchor
    injected = 0
    skipped = []
    for asin, badge in asin_badge.items():
        # Match the exact anchor for this ASIN (already has badge → skip)
        pattern = (
            rf'(<a class="asin" href="https://www\.amazon\.com/dp/{re.escape(asin)}"'
            rf'[^>]*>{re.escape(asin)}</a>)'
            rf'(?!<span class="ip-risk)'   # don't double-inject
        )
        replacement = rf'\1{badge}'
        new_html, n = re.subn(pattern, replacement, html)
        if n:
            html = new_html
            injected += 1
        else:
            skipped.append(asin)

    print(f"  Injected badges: {injected}, skipped (not found or already present): {len(skipped)}")
    if skipped:
        print(f"  Skipped ASINs: {skipped[:10]}{'...' if len(skipped) > 10 else ''}")

    # 6. Write output
    HTML_FILE.write_text(html, encoding="utf-8")
    print(f"Wrote {HTML_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
