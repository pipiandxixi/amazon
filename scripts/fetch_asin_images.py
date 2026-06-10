#!/usr/bin/env python3
"""Retroactive utility: collect Amazon product image URLs for an existing run.

find_products.py now saves image URLs automatically during scan (to products/asin_images.json).
Use this script only for runs that predate that feature.

Usage:
    python3 scripts/fetch_asin_images.py --picks results/2026_06_10_full_sweep/top_picks.md
    # writes to results/2026_06_10_full_sweep/products/asin_images.json (auto-detected by generate_grid_image.py)
"""

from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

from scan_common import eval_browser, open_browser


def parse_asins(picks_path: Path, top_n: int) -> list[str]:
    asins = []
    for line in picks_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "排名" in line:
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 2:
            continue
        m = re.search(r"\[([A-Z0-9]+)\]", cols[1])
        if m:
            asins.append(m.group(1))
        if len(asins) >= top_n:
            break
    return asins


_EXTRACT_IMG_JS = """
(() => {
  // 1. data-old-hires on main image (highest res)
  const landing = document.querySelector('#landingImage, #imgBlkFront');
  if (landing) {
    const hi = landing.dataset['oldHires'] || landing.getAttribute('data-old-hires');
    if (hi && hi.startsWith('http')) return hi;
    const src = landing.src;
    if (src && src.startsWith('http') && !src.includes('transparent-pixel')) return src;
  }
  // 2. og:image meta tag
  const og = document.querySelector('meta[property="og:image"]');
  if (og && og.content && og.content.startsWith('http')) return og.content;
  // 3. Any images/I/ CDN image on page
  const imgs = Array.from(document.querySelectorAll('img[src*="images/I/"]'));
  for (const img of imgs) {
    if (img.naturalWidth > 100) return img.src;
  }
  return '';
})()
"""


def fetch_image_url(asin: str) -> str:
    open_browser(f"https://www.amazon.com/dp/{asin}")
    time.sleep(2.5)
    result = eval_browser(_EXTRACT_IMG_JS)
    result = result.strip().strip('"').strip("'")
    return result if result.startswith("http") else ""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--picks", required=True)
    parser.add_argument("--top-n", type=int, default=60, dest="top_n")
    parser.add_argument("--out", default="",
                        help="Output path; defaults to {picks_dir}/products/asin_images.json")
    parser.add_argument("--resume", action="store_true", help="Skip already-fetched ASINs")
    args = parser.parse_args()

    asins = parse_asins(Path(args.picks), args.top_n)
    print(f"ASINs to fetch: {len(asins)}")

    picks_path = Path(args.picks)
    out_path = Path(args.out) if args.out else picks_path.parent / "products" / "asin_images.json"
    mapping: dict[str, str] = {}
    if args.resume and out_path.exists():
        mapping = json.loads(out_path.read_text())
        print(f"Resuming: {len(mapping)} already fetched")

    for i, asin in enumerate(asins, 1):
        if asin in mapping:
            print(f"  [{i}/{len(asins)}] {asin} (cached)")
            continue
        url = fetch_image_url(asin)
        mapping[asin] = url
        status = "✓" if url else "✗ placeholder"
        print(f"  [{i}/{len(asins)}] {asin} {status}")
        # Save incrementally
        out_path.write_text(json.dumps(mapping, indent=2))

    # Return browser to SellerSprite
    open_browser("https://www.sellersprite.com/v3/product-research")
    print(f"\nDone. {sum(1 for v in mapping.values() if v)} / {len(mapping)} images found.")
    print(f"Saved → {out_path}")


if __name__ == "__main__":
    main()
