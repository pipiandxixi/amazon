#!/usr/bin/env python3
"""Three-stage Amazon product research pipeline: market → keywords → products.

Results are written to a per-run directory so that multiple runs on the same
day (or with different department filters) never overwrite each other:

  results/{date}_{tag}/
    market_scan_report.md
    market_scan_results.json       ← enriched with product_path + departments
    keywords/
      keyword_scan_report.md
      keyword_scan_results.json
    products/
      {category_slug}.md           ← one file per scanned product category

Run tag is derived from --departments (first ASCII word of each name, joined
by "_"), or defaults to "all". Override with --tag.

Examples
--------
  python scripts/run_pipeline.py
  python scripts/run_pipeline.py --departments "Sports & Outdoors"
  python scripts/run_pipeline.py --departments "Sports & Outdoors" "Home & Kitchen"
  python scripts/run_pipeline.py --tag v2 --skip-market
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = PROJECT_ROOT / "results"


def _derive_tag(departments: list[str], explicit_tag: str) -> str:
    if explicit_tag:
        clean = re.sub(r"[^a-z0-9_-]", "", explicit_tag.lower())
        return clean[:40] or "run"
    if not departments:
        return "all"
    parts = [re.sub(r"[^a-z0-9]", "", d.split()[0].lower()) for d in departments]
    return "_".join(p for p in parts if p)[:40]


def _run_stage(stage_name: str, cmd: list[str]) -> None:
    print(f"\n{'='*60}")
    print(f"[STAGE] {stage_name}")
    print(f"  cmd: {' '.join(cmd)}")
    print('='*60)
    result = subprocess.run(cmd, cwd=str(PROJECT_ROOT))
    if result.returncode != 0:
        raise SystemExit(
            f"Pipeline stopped: stage '{stage_name}' exited with code {result.returncode}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--market-config", default="scripts/market_config.json",
        dest="market_config",
        help="Market config file (default: scripts/market_config.json)",
    )
    parser.add_argument(
        "--keyword-config", default="scripts/keyword_config.json",
        dest="keyword_config",
    )
    parser.add_argument(
        "--product-config", default="scripts/product_config.json",
        dest="product_config",
    )
    parser.add_argument("--date", default="", help="Report date YYYY_MM_DD (default: today)")
    parser.add_argument(
        "--departments", nargs="*", default=[], metavar="DEPT",
        help="Top-level Amazon category names to restrict the market scan.",
    )
    parser.add_argument("--tag", default="", help="Override run directory tag")
    parser.add_argument("--skip-market", action="store_true", dest="skip_market",
                        help="Reuse market_scan_results.json already in the run directory")
    parser.add_argument("--skip-keywords", action="store_true", dest="skip_keywords",
                        help="Reuse keyword_scan_results.json already in the run directory")
    parser.add_argument(
        "--max-keywords", type=int, default=20, dest="max_keywords",
        help="Max keywords forwarded to find_products (default 20)",
    )
    parser.add_argument(
        "--max-categories", type=int, default=5, dest="max_categories",
        help="Max green categories forwarded to find_products (default 5)",
    )
    args = parser.parse_args()

    # Read min_green_required from market config
    market_cfg_path = Path(args.market_config)
    if not market_cfg_path.exists():
        raise SystemExit(f"Market config not found: {market_cfg_path}")
    market_cfg = json.loads(market_cfg_path.read_text(encoding="utf-8"))
    min_green = int(market_cfg.get("scan_policy", {}).get("min_green_required", {}).get("value", 1))

    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    run_tag = _derive_tag(args.departments, args.tag)
    run_dir = RESULTS_DIR / f"{date_str}_{run_tag}"
    keywords_dir = run_dir / "keywords"
    products_dir = run_dir / "products"
    for d in (run_dir, keywords_dir, products_dir):
        d.mkdir(parents=True, exist_ok=True)
    print(f"Run directory: {run_dir}")

    # --- Stage 1: Market scan ---
    # select_market.py resolves --departments names → numbers internally and
    # writes the sidecar with product_path + departments already populated.
    market_sidecar = run_dir / "market_scan_results.json"
    if args.skip_market:
        if not market_sidecar.exists():
            raise SystemExit(
                f"--skip-market: no sidecar at {market_sidecar}. "
                "Run without --skip-market first."
            )
        print(f"[SKIP] Stage 1: using {market_sidecar}")
    else:
        market_cmd = [
            sys.executable, "scripts/select_market.py",
            "--config", args.market_config,
            "--date", date_str,
            "--output-dir", str(run_dir),
        ]
        if args.departments:
            market_cmd += ["--departments"] + args.departments
        _run_stage("select_market", market_cmd)
        if not market_sidecar.exists():
            raise SystemExit(f"Stage 1 done but {market_sidecar} not found")

    market_data: list[dict] = json.loads(market_sidecar.read_text(encoding="utf-8"))
    green_count = sum(1 for e in market_data if e.get("level", "").startswith("🟢"))
    print(f"  Market sidecar: {len(market_data)} candidates ({green_count} green).")
    if green_count < min_green:
        raise SystemExit(
            f"Pipeline stopped: only {green_count} green market(s) found "
            f"(min_green_required={min_green}). "
            "Relax market_config.json filters or lower scan_policy.min_green_required."
        )

    # --- Stage 2: Keyword scan ---
    # Pass the market sidecar directly — it already has `departments` per entry.
    keyword_sidecar = keywords_dir / "keyword_scan_results.json"
    if args.skip_keywords:
        if not keyword_sidecar.exists():
            raise SystemExit(
                f"--skip-keywords: no sidecar at {keyword_sidecar}. "
                "Run without --skip-keywords first."
            )
        print(f"[SKIP] Stage 2: using {keyword_sidecar}")
    else:
        _run_stage(
            "scan_keywords",
            [sys.executable, "scripts/scan_keywords.py",
             "--config", args.keyword_config,
             "--date", date_str,
             "--output-dir", str(keywords_dir),
             "--categories-file", str(market_sidecar)],
        )
        if not keyword_sidecar.exists():
            raise SystemExit(f"Stage 2 done but {keyword_sidecar} not found")

    keyword_data: list[dict] = json.loads(keyword_sidecar.read_text(encoding="utf-8"))
    green_keywords = [k for k in keyword_data if k.get("level") == "🟢 Green (Recommended)"]
    top_keywords = (green_keywords or keyword_data)[:args.max_keywords]
    print(f"  Keywords: {len(keyword_data)} candidates, forwarding top {len(top_keywords)}")

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tmp_kw:
        json.dump([k["keyword"] for k in top_keywords], tmp_kw, ensure_ascii=False)
        tmp_kw_path = tmp_kw.name

    # --- Stage 3: Product scan ---
    # Pass green categories (up to --max-categories); fall back to all if none green.
    # The sidecar already carries product_path + departments from stage 1.
    green_cats = [e for e in market_data if e.get("level", "").startswith("🟢")]
    product_cats = (green_cats or market_data)[:args.max_categories]
    print(
        f"  Product scan: {len(product_cats)} categories "
        f"(green={len(green_cats)}, cap={args.max_categories})"
    )

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tmp_cats:
        json.dump(product_cats, tmp_cats, ensure_ascii=False)
        tmp_cats_path = tmp_cats.name

    _run_stage(
        "find_products",
        [sys.executable, "scripts/find_products.py",
         "--config", args.product_config,
         "--date", date_str,
         "--output-dir", str(products_dir),
         "--keywords-file", tmp_kw_path,
         "--categories-file", tmp_cats_path,
         "--market-sidecar", str(market_sidecar)],
    )

    print(f"\n{'='*60}")
    print("Pipeline complete!")
    print(f"  Run directory  : {run_dir}")
    print(f"  Market report  : {run_dir / 'market_scan_report.md'}")
    print(f"  Keyword report : {keywords_dir / 'keyword_scan_report.md'}")
    print(f"  Product reports: {products_dir}/")
    print('='*60)


if __name__ == "__main__":
    main()
