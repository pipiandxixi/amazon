#!/usr/bin/env python3
"""Generate a 4-column product grid image from top_picks.md.

Usage:
    python3 scripts/generate_grid_image.py --picks results/2026_06_10_full_sweep/top_picks.md
    python3 scripts/generate_grid_image.py --picks ... --top-n 60 --width 1440 --out grid.jpg
"""

from __future__ import annotations

import argparse
import io
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image, ImageDraw, ImageFont

# ── Layout constants ─────────────────────────────────────────────────────────
COLS = 4
OUTER_PAD = 28        # left/right margin
CARD_GAP = 16         # gap between cards (horizontal and vertical)
CARD_PAD = 14         # inner padding inside each card
IMG_SIZE = 280        # product image (square px)
NAME_FONT_SIZE = 15
PRICE_FONT_SIZE = 16
REASON_FONT_SIZE = 13
RANK_FONT_SIZE = 14

BG_COLOR = "#E8EAF0"
CARD_COLOR = "#FFFFFF"
TEXT_COLOR = "#111827"
PRICE_COLOR = "#16A34A"   # green for price
DIM_COLOR = "#6B7280"
RANK_BG_COLOR = "#1D4ED8"
RANK_FG_COLOR = "#FFFFFF"
CARD_RADIUS = 10

# ── Font loading ─────────────────────────────────────────────────────────────
_FONT_CANDIDATES = [
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/STHeiti Light.ttc",
]

def _load_font(size: int) -> ImageFont.FreeTypeFont:
    for path in _FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()

F_NAME   = _load_font(NAME_FONT_SIZE)
F_PRICE  = _load_font(PRICE_FONT_SIZE)
F_REASON = _load_font(REASON_FONT_SIZE)
F_RANK   = _load_font(RANK_FONT_SIZE)

# ── Parse top_picks.md ────────────────────────────────────────────────────────
def parse_top_picks(path: Path, top_n: int) -> list[dict]:
    """Extract rank, ASIN, name, price, reason from the scored table.

    Table columns (12-col format with price):
      0:排名  1:ASIN  2:品名  3:类目  4:价格  5:月销量  6:增长率
      7:毛利率  8:Reviews  9:卖家数  10:上架时长  11:推荐理由
    Falls back gracefully to the old 11-col format (no price column).
    """
    products: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "排名" in line:
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 11:
            continue
        rank_s, asin_s, name = cols[0], cols[1], cols[2]
        has_price_col = len(cols) >= 12 and cols[4].startswith("$")
        price = cols[4] if has_price_col else ""
        reason = cols[11] if has_price_col else cols[10]
        try:
            rank = int(rank_s)
        except ValueError:
            continue
        m = re.search(r"\[([A-Z0-9]+)\]", asin_s)
        if not m:
            continue
        products.append({
            "rank": rank, "asin": m.group(1),
            "name": name, "price": price, "reason": reason,
        })
        if len(products) >= top_n:
            break
    return products


# ── Image download ────────────────────────────────────────────────────────────
def fetch_product_image(asin: str) -> Image.Image:
    """Download main product image from Amazon; return gray placeholder on failure."""
    for url in [
        f"https://images-na.ssl-images-amazon.com/images/P/{asin}.01.LZZZZZZZ.jpg",
        f"https://m.media-amazon.com/images/P/{asin}.01._SX500_.jpg",
    ]:
        try:
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(req, timeout=14) as r:
                data = r.read()
            img = Image.open(io.BytesIO(data)).convert("RGB")
            if img.width > 30 and img.height > 30:
                img.thumbnail((IMG_SIZE, IMG_SIZE), Image.LANCZOS)
                # Pad to exact square with white background
                square = Image.new("RGB", (IMG_SIZE, IMG_SIZE), "#FFFFFF")
                x = (IMG_SIZE - img.width) // 2
                y = (IMG_SIZE - img.height) // 2
                square.paste(img, (x, y))
                return square
        except Exception:
            continue

    # Gray placeholder with ASIN label
    ph = Image.new("RGB", (IMG_SIZE, IMG_SIZE), "#E5E7EB")
    d = ImageDraw.Draw(ph)
    d.text((IMG_SIZE // 2, IMG_SIZE // 2), asin, fill="#9CA3AF",
           font=_load_font(11), anchor="mm")
    return ph


def fetch_all_images(products: list[dict],
                     url_map: dict[str, str] | None = None) -> dict[str, Image.Image]:
    """Download all product images in parallel.

    If url_map is provided (ASIN → image URL), use those real CDN URLs directly.
    url_map is auto-detected from products/asin_images.json (written by find_products.py),
    or can be supplied explicitly via --image-urls (fetch_asin_images.py for retroactive runs).
    Falls back to ASIN-based URL guessing when no map entry exists for an ASIN.
    """
    def _fetch(asin: str) -> Image.Image:
        if url_map and url_map.get(asin):
            # Use the pre-fetched real URL directly
            try:
                req = Request(url_map[asin], headers={"User-Agent": "Mozilla/5.0"})
                with urlopen(req, timeout=14) as r:
                    data = r.read()
                img = Image.open(io.BytesIO(data)).convert("RGB")
                if img.width > 30 and img.height > 30:
                    img.thumbnail((IMG_SIZE, IMG_SIZE), Image.LANCZOS)
                    square = Image.new("RGB", (IMG_SIZE, IMG_SIZE), "#FFFFFF")
                    square.paste(img, ((IMG_SIZE - img.width) // 2, (IMG_SIZE - img.height) // 2))
                    return square
            except Exception:
                pass
        return fetch_product_image(asin)  # fallback to ASIN-based guess

    results: dict[str, Image.Image] = {}
    print(f"Downloading {len(products)} product images (parallel)...")
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(_fetch, p["asin"]): p["asin"] for p in products}
        done = 0
        for fut in as_completed(futures):
            asin = futures[fut]
            results[asin] = fut.result()
            done += 1
            if done % 10 == 0 or done == len(products):
                print(f"  {done}/{len(products)} downloaded")
    return results


# ── Text wrapping ─────────────────────────────────────────────────────────────
def wrap_text(draw: ImageDraw.ImageDraw, text: str,
              font: ImageFont.FreeTypeFont, max_w: int, max_lines: int = 2) -> list[str]:
    """Wrap text to fit max_w pixels wide; truncate with '…' if needed."""
    lines: list[str] = []
    remaining = text
    while remaining and len(lines) < max_lines:
        lo, hi = 1, len(remaining)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            bbox = draw.textbbox((0, 0), remaining[:mid], font=font)
            if bbox[2] - bbox[0] <= max_w:
                lo = mid
            else:
                hi = mid - 1
        lines.append(remaining[:lo])
        remaining = remaining[lo:]
    if remaining:
        last = lines[-1]
        while last:
            bbox = draw.textbbox((0, 0), last + "…", font=font)
            if bbox[2] - bbox[0] <= max_w:
                lines[-1] = last + "…"
                break
            last = last[:-1]
    return lines


# ── Card drawing ──────────────────────────────────────────────────────────────
def card_height(draw: ImageDraw.ImageDraw, inner_w: int, product: dict) -> int:
    """Calculate the height of one card given its inner content width."""
    name_lines = wrap_text(draw, product["name"], F_NAME, inner_w, 2)
    reason_lines = wrap_text(draw, product["reason"], F_REASON, inner_w, 2)
    name_h = sum(draw.textbbox((0, 0), l, font=F_NAME)[3] + 4 for l in name_lines)
    price_h = (draw.textbbox((0, 0), product["price"], font=F_PRICE)[3] + 4
               if product.get("price") else 0)
    reason_h = sum(draw.textbbox((0, 0), l, font=F_REASON)[3] + 4 for l in reason_lines)
    return CARD_PAD + IMG_SIZE + 10 + name_h + 6 + price_h + 6 + reason_h + CARD_PAD


def draw_card(canvas: Image.Image, draw: ImageDraw.ImageDraw,
              x: int, y: int, w: int, h: int,
              product: dict, img: Image.Image) -> None:
    inner_w = w - 2 * CARD_PAD

    # Card background
    try:
        draw.rounded_rectangle([x, y, x + w, y + h], radius=CARD_RADIUS, fill=CARD_COLOR)
    except AttributeError:
        draw.rectangle([x, y, x + w, y + h], fill=CARD_COLOR)

    # Product image (centered horizontally)
    img_x = x + CARD_PAD + (inner_w - IMG_SIZE) // 2
    img_y = y + CARD_PAD
    canvas.paste(img, (img_x, img_y))

    # Rank badge (top-left corner of image)
    rank_text = str(product["rank"])
    rbbox = draw.textbbox((0, 0), rank_text, font=F_RANK)
    rw = rbbox[2] - rbbox[0] + 10
    rh = rbbox[3] - rbbox[1] + 6
    try:
        draw.rounded_rectangle([img_x, img_y, img_x + rw, img_y + rh],
                                radius=4, fill=RANK_BG_COLOR)
    except AttributeError:
        draw.rectangle([img_x, img_y, img_x + rw, img_y + rh], fill=RANK_BG_COLOR)
    draw.text((img_x + 5, img_y + 3), rank_text, fill=RANK_FG_COLOR, font=F_RANK)

    # Product name
    ty = img_y + IMG_SIZE + 10
    for line in wrap_text(draw, product["name"], F_NAME, inner_w, 2):
        lh = draw.textbbox((0, 0), line, font=F_NAME)[3]
        draw.text((x + CARD_PAD, ty), line, fill=TEXT_COLOR, font=F_NAME)
        ty += lh + 4

    # Price (shown before reason)
    ty += 6
    if product.get("price"):
        lh = draw.textbbox((0, 0), product["price"], font=F_PRICE)[3]
        draw.text((x + CARD_PAD, ty), product["price"], fill=PRICE_COLOR, font=F_PRICE)
        ty += lh + 4

    # Reason
    ty += 6
    for line in wrap_text(draw, product["reason"], F_REASON, inner_w, 2):
        lh = draw.textbbox((0, 0), line, font=F_REASON)[3]
        draw.text((x + CARD_PAD, ty), line, fill=DIM_COLOR, font=F_REASON)
        ty += lh + 4


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--picks", required=True, help="Path to top_picks.md")
    parser.add_argument("--top-n", type=int, default=60, dest="top_n")
    parser.add_argument("--width", type=int, default=1440, help="Canvas width in px")
    parser.add_argument("--out", default="", help="Output image path (default: top_picks_grid.jpg next to picks file)")
    parser.add_argument("--image-urls", default="", dest="image_urls",
                        help="JSON file mapping ASIN→image URL (from fetch_asin_images.py)")
    args = parser.parse_args()

    picks_path = Path(args.picks)
    out_path = Path(args.out) if args.out else picks_path.parent / "top_picks_grid.jpg"

    products = parse_top_picks(picks_path, args.top_n)
    if not products:
        raise SystemExit("No products parsed from top_picks.md")
    print(f"Parsed {len(products)} products")

    url_map: dict[str, str] = {}
    # Prefer explicit --image-urls flag; fall back to auto-detected sidecar from find_products.py
    image_urls_path = (Path(args.image_urls) if args.image_urls
                       else picks_path.parent / "products" / "asin_images.json")
    if image_urls_path.exists():
        url_map = json.loads(image_urls_path.read_text())
        print(f"Loaded {len(url_map)} image URLs from {image_urls_path}")

    images = fetch_all_images(products, url_map or None)

    # ── Layout calculation ──────────────────────────────────────────────────
    col_w = (args.width - 2 * OUTER_PAD - (COLS - 1) * CARD_GAP) // COLS
    inner_w = col_w - 2 * CARD_PAD

    # Pre-calculate all card heights (needs a temp draw surface)
    probe = Image.new("RGB", (1, 1))
    probe_draw = ImageDraw.Draw(probe)
    heights = [card_height(probe_draw, inner_w, p) for p in products]

    # Row heights = max card height in that row
    rows = [products[i:i + COLS] for i in range(0, len(products), COLS)]
    row_heights = [max(heights[i * COLS: i * COLS + COLS]) for i in range(len(rows))]

    total_h = (2 * OUTER_PAD
               + sum(row_heights)
               + (len(rows) - 1) * CARD_GAP)

    print(f"Canvas: {args.width} × {total_h} px  ({len(rows)} rows × {COLS} cols)")

    # ── Render ───────────────────────────────────────────────────────────────
    canvas = Image.new("RGB", (args.width, total_h), BG_COLOR)
    draw = ImageDraw.Draw(canvas)

    py = OUTER_PAD
    for row_i, row in enumerate(rows):
        row_h = row_heights[row_i]
        for col_i, product in enumerate(row):
            px = OUTER_PAD + col_i * (col_w + CARD_GAP)
            idx = row_i * COLS + col_i
            img = images.get(product["asin"], Image.new("RGB", (IMG_SIZE, IMG_SIZE), "#E5E7EB"))
            draw_card(canvas, draw, px, py, col_w, row_h, product, img)
        py += row_h + CARD_GAP

    canvas.save(out_path, quality=92)
    print(f"Saved → {out_path}")


if __name__ == "__main__":
    main()
