# Amazon Scan Pipeline

```
Market Scan → Product Scan → Category Keyword Batch Lookup
```

Scripts run against a live SellerSprite session via `opencli`.  
Config fields: `{"value": ..., "label": "..."}` — edit `value` only.
Default outputs are grouped by run date under `results/YYYY_MM_DD/`.

---

## Recommended: Unified Pipeline

```bash
python3 scripts/run_pipeline.py
```

The unified entrypoint reads only `scripts/pipeline_config.json`. Dynamic values
are passed in memory:

```
market candidates → product categories → per-category ASIN lists
```

Result JSON files remain available for auditing, but are never used to drive the
next stage. `pipeline_config.json` contains static filters and policies only; it
does not contain a preselected category, keyword, product, or ASIN.

### Stage 1 — Market Scan (`select_market.py`)

Scans SellerSprite's market research page across configured departments. Each
sub-category is rated 🟢 Green / 🟡 Yellow / 🔴 Red based on risk rules (return
rate, weight, regulatory keywords, brand concentration, etc.). Green and Yellow
candidates are passed in memory to Stage 2.

Output: `results/YYYY_MM_DD/market_scan_report.md`

### Stage 2 — Product Scan (`find_products.py`)

For every candidate category, opens the SellerSprite product research page,
applies all filters (monthly sales, price, reviews, profit margin, FBA fee,
weight, sellers, etc.), and scrapes up to `max_products` qualifying listings.
Resolved SellerSprite category Node IDs are saved in `categories.json`; later
runs reuse them and open a fully filtered product-research URL directly, without
reopening the category picker.

Output: `results/YYYY_MM_DD/products/{category_slug}.md` (one file per category)

Market, product, and keyword reports record whether the free plan may have
truncated visible results.

Categories that have been scanned but return no qualifying products are
automatically marked Yellow with low attention priority. Normal incremental
batches scan Green categories first and skip these low-attention categories.

### Stage 3 — Category Keyword Batch Lookup (`find_asin_keywords.py`)

For each category that yielded products, selects the top `max_asins` (default 5)
ASINs ranked by `monthly_sales / (reviews + 10) + profit_margin / 10`, then
opens the SellerSprite **traffic-extend** page with all ASINs in a single URL:

```
/v3/traffic/extend/asin?q=ASIN1,ASIN2,...&marketId=1&date=
```

This batch query returns keywords shared across multiple products in the same
category — more representative than single-ASIN reverse lookup. Keywords are
filtered and scored (traffic share, search volume, purchase count, organic rank),
then the top `max_keywords` are written to a per-category report.

Output: `results/YYYY_MM_DD/category_keywords_{category_slug}_{date}.md`

### Combined Report

All stage reports are merged into a single human-readable file:

```
results/YYYY_MM_DD/pipeline_report_YYYY_MM_DD.md
```

Individual stage reports are kept beside it for auditing.

---

## CLI Options

```bash
python3 scripts/run_pipeline.py --dry-run          # validate config, no browser
python3 scripts/run_pipeline.py --skip-asin-keywords  # skip Stage 3
python3 scripts/run_pipeline.py --date 2026_06_01  # override run date
```

## Individual Stage Debugging

The original scripts and configs remain available for isolated debugging:

```bash
# Single-ASIN or multi-ASIN keyword lookup (standalone)
python3 scripts/find_asin_keywords.py B0FS72284D B0EXAMPLE2 --category "Trophies"
```

These are not the recommended end-to-end workflow.

## Browser Interaction Strategy

- Product research: direct GET URL for category Node ID and all filters. The
  category picker is used only once when a category has no cached Node ID.
- Keyword research: direct GET URL for departments and all filter fields.
- Market research: SellerSprite exposes this page as a POST form, so it cannot
  be represented by URL alone; the script fills named fields and submits the
  form directly without clicking the page button.
- ASIN traffic extension: ASINs are loaded by URL, but SellerSprite still
  requires server-side query/variant actions before the keyword table exists.
  Keyword filters are applied locally after scraping, avoiding the page's
  position-dependent filter inputs and its additional submit click.
