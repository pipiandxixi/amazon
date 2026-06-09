#!/usr/bin/env python3
"""Three-stage Amazon product research pipeline: market → keywords → products.

Results are written to a per-run directory so that multiple runs on the same
day (or with different department filters) never overwrite each other:

  results/{date}_{tag}/
    market_scan_report.md
    market_scan_results.json
    keywords/
      keyword_scan_report.md
      keyword_scan_results.json
    products/
      {category_slug}.md   (one file per scanned product category)

Run tag is derived from --departments (first ASCII word of each name, joined
by "_"), or defaults to "all" when no departments are specified. Override with
--tag for custom labels (e.g. A/B testing different configs).

Examples
--------
  # Scan all categories (default tag: all)
  python scripts/run_pipeline.py

  # Restrict market scan to one top-level category (tag: sports)
  python scripts/run_pipeline.py --departments "Sports & Outdoors"

  # Multiple categories (tag: sports_home)
  python scripts/run_pipeline.py --departments "Sports & Outdoors" "Home & Kitchen"

  # Custom tag, re-use existing market scan
  python scripts/run_pipeline.py --tag v2 --skip-market

Department names must match keys in pipeline_config.json category_map.
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
    """Derive a short, filesystem-safe run tag.

    explicit_tag takes priority. Otherwise, take the first ASCII word of each
    department name (lower-cased) and join with "_" (e.g. ["Sports & Outdoors",
    "Home & Kitchen"] → "sports_home"). Fall back to "all" when no departments
    are given. Tag is capped at 40 characters.
    """
    if explicit_tag:
        clean = re.sub(r"[^a-z0-9_-]", "", explicit_tag.lower())
        return clean[:40] or "run"
    if not departments:
        return "all"
    parts = [re.sub(r"[^a-z0-9]", "", d.split()[0].lower()) for d in departments]
    return "_".join(p for p in parts if p)[:40]


def _run_stage(stage_name: str, cmd: list[str]) -> None:
    """Run a subprocess stage; raise SystemExit on non-zero exit."""
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
        "--config", default="scripts/pipeline_config.json",
        help="Pipeline config file (default: scripts/pipeline_config.json)",
    )
    parser.add_argument(
        "--date", default="",
        help="Report date YYYY_MM_DD (default: today)",
    )
    parser.add_argument(
        "--departments", nargs="*", default=[], metavar="DEPT",
        help=(
            "Top-level Amazon category names to restrict the market scan "
            "(e.g. 'Sports & Outdoors' 'Home & Kitchen'). "
            "Must match keys in category_map inside pipeline_config.json. "
            "Omit to scan all departments."
        ),
    )
    parser.add_argument(
        "--tag", default="",
        help=(
            "Override the run tag used in the result directory name. "
            "Defaults to a slug derived from --departments, or 'all'."
        ),
    )
    parser.add_argument(
        "--skip-market", action="store_true", dest="skip_market",
        help="Skip stage 1; reuse market_scan_results.json already in the run directory",
    )
    parser.add_argument(
        "--skip-keywords", action="store_true", dest="skip_keywords",
        help="Skip stage 2; reuse keyword_scan_results.json already in the run directory",
    )
    parser.add_argument(
        "--max-keywords", type=int, default=0, dest="max_keywords",
        help="Max keywords forwarded to find_products (0 = use pipeline config default)",
    )
    args = parser.parse_args()

    # --- Load pipeline config ---
    cfg_path = Path(args.config)
    if not cfg_path.exists():
        raise SystemExit(f"Pipeline config not found: {cfg_path}")
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    pipeline_cfg = cfg.get("pipeline", {})
    category_map: dict[str, dict] = cfg.get("category_map", {})

    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    max_keywords = args.max_keywords or int(pipeline_cfg.get("max_keywords_to_products", 20))
    min_green = int(pipeline_cfg.get("min_green_markets_required", 1))
    max_categories = int(pipeline_cfg.get("max_categories_to_products", 5))

    market_config = cfg.get("market_config", "scripts/market_config.json")
    keyword_config = cfg.get("keyword_config", "scripts/keyword_config.json")
    product_config = cfg.get("product_config", "scripts/product_config.json")

    # --- Set up run directory ---
    run_tag = _derive_tag(args.departments, args.tag)
    run_dir = RESULTS_DIR / f"{date_str}_{run_tag}"
    keywords_dir = run_dir / "keywords"
    products_dir = run_dir / "products"
    for d in (run_dir, keywords_dir, products_dir):
        d.mkdir(parents=True, exist_ok=True)
    print(f"Run directory: {run_dir}")

    # Resolve --departments names → SellerSprite department numbers via category_map.
    # These are forwarded to select_market.py for pre-filtering the market scan page.
    dept_numbers: list[int] = []
    if args.departments:
        unknown: list[str] = []
        for name in args.departments:
            mapping = category_map.get(name)
            if mapping and mapping.get("department") is not None:
                dept_numbers.append(int(mapping["department"]))
            else:
                unknown.append(name)
        if unknown:
            print(f"  WARNING: no department mapping for: {unknown} — those will be ignored in market filter")
        print(f"  Departments: {args.departments} → numbers {dept_numbers}")

    # --- Stage 1: Market scan ---
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
            "--config", market_config,
            "--date", date_str,
            "--output-dir", str(run_dir),
        ]
        if dept_numbers:
            # Pass resolved numbers so select_market can filter the market page
            market_cmd += ["--department-numbers"] + [str(n) for n in dept_numbers]
        _run_stage("select_market", market_cmd)
        if not market_sidecar.exists():
            raise SystemExit(f"Stage 1 done but {market_sidecar} not found — check select_market output")

    # --- Validate green market count ---
    market_data: list[dict] = json.loads(market_sidecar.read_text(encoding="utf-8"))
    green_market_count = sum(1 for e in market_data if e.get("level", "").startswith("🟢"))
    if green_market_count < min_green:
        raise SystemExit(
            f"Pipeline stopped: only {green_market_count} green market(s) found "
            f"(min_green_markets_required={min_green}). "
            "Relax market_config.json filters or lower min_green_markets_required."
        )
    print(f"  Market sidecar: {len(market_data)} candidates ({green_market_count} green).")

    # --- Enrich market entries with department numbers + product_path ---
    # category_map translates Amazon top-level category names to SellerSprite
    # department checkbox numbers (for keyword scan) and derives product_path
    # arrays (for category tree navigation in product scan).
    enriched: list[dict] = []
    skipped_no_dept: list[str] = []
    for entry in market_data:
        path_str: str = entry.get("path", "")
        path_parts = [s.strip() for s in re.split(r'[>›]', path_str) if s.strip()]
        top_level = path_parts[0] if path_parts else ""
        mapping = category_map.get(top_level)
        dept = mapping.get("department") if mapping else None
        product_path = path_parts
        enriched_entry = {**entry, "product_path": product_path}
        if dept is not None:
            enriched_entry["departments"] = [int(dept)]
        else:
            enriched_entry["departments"] = []
            skipped_no_dept.append(entry.get("en_name", top_level))
        enriched.append(enriched_entry)

    dept_covered = [e for e in enriched if e["departments"]]
    print(
        f"  Enriched: {len(dept_covered)} with department mapping, "
        f"{len(skipped_no_dept)} without: {skipped_no_dept[:5]}"
    )

    # --- Stage 2: Keyword scan ---
    keyword_sidecar = keywords_dir / "keyword_scan_results.json"
    if args.skip_keywords:
        if not keyword_sidecar.exists():
            raise SystemExit(
                f"--skip-keywords: no sidecar at {keyword_sidecar}. "
                "Run without --skip-keywords first."
            )
        print(f"[SKIP] Stage 2: using {keyword_sidecar}")
    else:
        # Pass all enriched entries so keyword scan covers the union of departments
        # from all candidate categories (not just the green ones selected for product scan).
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as tmp_cats:
            json.dump(enriched, tmp_cats, ensure_ascii=False)
            tmp_cats_path = tmp_cats.name
        _run_stage(
            "scan_keywords",
            [sys.executable, "scripts/scan_keywords.py",
             "--config", keyword_config,
             "--date", date_str,
             "--output-dir", str(keywords_dir),
             "--categories-file", tmp_cats_path],
        )
        if not keyword_sidecar.exists():
            raise SystemExit(f"Stage 2 done but {keyword_sidecar} not found")

    keyword_data: list[dict] = json.loads(keyword_sidecar.read_text(encoding="utf-8"))
    # Prefer green keywords; fall back to all candidates (sidecar excludes red)
    green_keywords = [k for k in keyword_data if k.get("level") == "🟢 Green (Recommended)"]
    top_keywords = (green_keywords or keyword_data)[:max_keywords]
    print(f"  Keywords: {len(keyword_data)} candidates, forwarding top {len(top_keywords)}")

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tmp_kw:
        json.dump([k["keyword"] for k in top_keywords], tmp_kw, ensure_ascii=False)
        tmp_kw_path = tmp_kw.name

    # --- Stage 3: Product scan ---
    # Only pass green categories (up to max_categories_to_products) to keep
    # the product scan focused on confirmed opportunities. Fall back to all
    # enriched entries if none are green.
    green_categories = [e for e in enriched if e.get("level", "").startswith("🟢")]
    product_categories = (green_categories or enriched)[:max_categories]
    print(
        f"  Product scan: {len(product_categories)} categories "
        f"(green={len(green_categories)}, cap={max_categories})"
    )

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", delete=False, encoding="utf-8"
    ) as tmp_prod_cats:
        json.dump(product_categories, tmp_prod_cats, ensure_ascii=False)
        tmp_prod_cats_path = tmp_prod_cats.name

    _run_stage(
        "find_products",
        [sys.executable, "scripts/find_products.py",
         "--config", product_config,
         "--date", date_str,
         "--output-dir", str(products_dir),
         "--keywords-file", tmp_kw_path,
         "--categories-file", tmp_prod_cats_path,
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
