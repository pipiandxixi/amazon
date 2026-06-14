# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project does

Amazon FBA product sourcing pipeline. It automates three sequential research stages against a live SellerSprite browser session via `opencli`, then merges all output into a single Markdown report.

```
Stage 1: Market Scan (select_market.py)
  → scores sub-categories 🟢/🟡/🔴 by risk rules

Stage 2: Product Scan (find_products.py)
  → applies product filters per candidate category, scrapes listings

Stage 3: ASIN Keyword Lookup (find_asin_keywords.py)
  → batch traffic-extend query for top ASINs per category
```

All stage results pass **in memory** between stages — no JSON file is read back to drive the next stage. `pipeline_config.json` contains only static filters and thresholds.

## Running the pipeline

```bash
# Activate venv first
source .venv/bin/activate

# Full pipeline (all three stages)
python3 scripts/run_pipeline.py

# Common flags
python3 scripts/run_pipeline.py --dry-run               # validate config, no browser
python3 scripts/run_pipeline.py --skip-asin-keywords    # skip Stage 3
python3 scripts/run_pipeline.py --date 2026_06_01       # override output date

# Resume from a specific stage (reads the previous stage's handoff JSON)
python3 scripts/run_pipeline.py --start-from 2          # skip Stage 1, re-run Stage 2+3
python3 scripts/run_pipeline.py --start-from 3          # skip Stages 1&2, re-run Stage 3 only

# Standalone ASIN keyword lookup (debugging only)
python3 scripts/find_asin_keywords.py B0FS72284D B0EXAMPLE2 --category "Trophies"
```

Output lands in `results/YYYY_MM_DD/pipeline_report_YYYY_MM_DD.md`.

Each full run also writes two handoff files in the same directory:
- `stage1_handoff_YYYY_MM_DD.json` — candidate categories + market markdown (Stage 1 → 2)
- `stage2_handoff_YYYY_MM_DD.json` — products list + product markdowns (Stage 2 → 3)

These enable `--start-from` to resume without re-running earlier stages. On a full run they are refreshed before each downstream stage reads them, so results are always consistent.

## Pre-run requirement

The pipeline requires a live SellerSprite browser session:
1. Open Chrome and navigate to sellersprite.com (must be logged in)
2. Run `opencli browser ss bind` to attach to that tab

`scan_common.check_browser_ready()` is called at startup and will exit with a Chinese-language error message if the session is not bound or not logged in.

## Config

All pipeline parameters live in `scripts/pipeline_config.json`. Config fields follow the pattern `{"value": ..., "label": "..."}` — **edit `value` only**, never `label`.

The config is divided into three top-level sections matching the three stages:
- `market` — filter params, scan policy, department IDs, risk rules (red/yellow thresholds, excluded path keywords)
- `products` — filter params (price, sales, reviews, weight, margin, etc.) and scan policy
- `asin_keywords` — filters, score weights, scan policy

`pipeline.candidate_levels` controls which market ratings flow into Stage 2 (default: Green + Yellow).

**Do not add a `category` key under `products`** — the pipeline validates that this field is absent and will raise `ValueError` if present.

## Architecture details

- `scan_common.py` — shared browser automation primitives (`eval_browser`, `open_browser`, `extract_json_array`, `check_browser_ready`). All browser interaction goes through `opencli browser ss eval/open`.
- `run_pipeline.py` imports the three stage modules directly (`import find_asin_keywords as asin_scan`, etc.) and calls their functions with in-memory data. Each stage module is also runnable standalone.
- Stage scripts run from `scripts/` but `scan_common.py` computes `PROJECT_ROOT` as the parent of `scripts/`, so results always land at repo root `/results/`.
- `values()` helper (duplicated in each script) unwraps `{"value": x}` dicts from config.
- ASIN priority scoring formula: `monthly_sales / (reviews + 10) + profit_margin / 10`
- Keyword scoring uses configurable weights from `asin_keywords.score_weights` in the config.

## Use the `/amazon-sourcing` skill

For end-to-end runs with LLM analysis of results, use:

```
/amazon-sourcing
```

This skill handles the full workflow: checks for existing results, runs the pipeline if needed, reads the report, and produces a prioritized sourcing recommendation.
