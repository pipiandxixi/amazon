# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Amazon FBA product sourcing pipeline. It runs three research stages against a live SellerSprite browser session via `opencli`, with results persisted to a category database after each category.

```
Stage 1: Market Scan (select_market.py)
  → scores sub-categories 🟢/🟡/🔴 by risk rules
  → upserts candidates into results/json/categories.json

Stage 2+3: Per-Category Loop (run_pipeline.py)
  → for each Green category (ordered by staleness):
      find_products.py  — scrapes product listings
      find_asin_keywords.py — batch traffic-extend keyword lookup
  → updates categories.json and regenerates report.html after each category
```

`results/json/categories.json` is the single persistent store — all progress survives interruptions. `pipeline_config.json` contains only static filters and thresholds.

## Running the pipeline

```bash
# Activate venv first
source .venv/bin/activate

# Full pipeline (market scan + all categories)
python3 scripts/run_pipeline.py

# Common flags
python3 scripts/run_pipeline.py --dry-run               # validate config, no browser
python3 scripts/run_pipeline.py --skip-keywords         # skip keyword lookup (products only)
python3 scripts/run_pipeline.py --date 2026_06_01       # override date label in reports

# Resume / partial runs
python3 scripts/run_pipeline.py --skip-market-scan                   # skip market scan, use existing categories.json
python3 scripts/run_pipeline.py --market-scan-only                   # run market scan only, stop before product loop
python3 scripts/run_pipeline.py --skip-market-scan --max-categories 5  # batch: process 5 categories

# Standalone ASIN keyword lookup (debugging only)
python3 scripts/find_asin_keywords.py B0FS72284D B0EXAMPLE2 --category "Trophies"

# Regenerate HTML report from existing categories.json
python3 scripts/generate_html_report.py
```

## Required Product And Keyword Scan Batch Workflow

When resuming product scans and keyword selection from the existing persistent
category database, run at most five categories per batch:

```bash
python3 scripts/run_pipeline.py --skip-market-scan --max-categories 5
```

After every batch:

1. Read `results/json/categories.json` and identify the five categories updated
   in the batch from their `last_updated` values.
2. Verify `results/json/categories.json` and `results/html/report.html`.
3. Commit the batch outputs and push `main` so the public report is updated.
4. Commit only files related to the current batch. Do not include unrelated or
   legacy result changes.
5. In the final response, list every updated category with its product count
   and keyword count, plus the commit hash and push result.

Do not start the next batch until the current five-category batch has been
committed, pushed, and reported.

## Pre-run requirement

The pipeline requires a live SellerSprite browser session:
1. Open Chrome and navigate to sellersprite.com (must be logged in)
2. Run `opencli browser ss bind` to attach to that tab

## Config

All pipeline parameters live in `scripts/pipeline_config.json`. Config fields follow the pattern `{"value": ..., "label": "..."}` — **edit `value` only**, never `label`.

The config is divided into three top-level sections matching the three stages:
- `market` — filter params, scan policy, department IDs, risk rules (red/yellow thresholds, excluded path keywords)
- `products` — filter params (price, sales, reviews, weight, margin, etc.) and scan policy
- `asin_keywords` — filters, score weights, scan policy

`pipeline.candidate_levels` controls which market ratings flow into the product loop (default: Green only). Yellow categories are only created by `downgrade_empty_categories()` after failed product scans and are not re-processed by the loop.

**Do not add a `category` key under `products`** — the pipeline validates that this field is absent and will raise `ValueError` if present.

## Architecture details

- `scan_common.py` — shared browser automation primitives. All browser interaction goes through `opencli browser ss eval/open`. `dated_results_dir()` ignores the `date_str` argument and always returns `results/` flat.
- `run_pipeline.py` — main entry point. Imports stage modules directly and calls their functions with in-memory data.
- `generate_html_report.py` — generates `results/html/report.html` from `categories.json`. Called after each category by `run_pipeline.py`; also runnable standalone.
- `values()` helper (duplicated in each script) unwraps `{"value": x}` dicts from config.
- ASIN priority scoring formula: `monthly_sales / (reviews + 10) + profit_margin / 10`
- Keyword scoring uses configurable weights from `asin_keywords.score_weights` in the config.
- `allowed_traffic_types` and `max_organic_rank` filters in `asin_keywords` have no effect — the `/v3/traffic/extend/asin` page does not expose those columns; `traffic_type` and `organic_rank` are always empty in scraped output.

For end-to-end runs with LLM analysis of results, use `/amazon-sourcing`.
