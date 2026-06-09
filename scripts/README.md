# Amazon Scan Pipeline

Three-stage automated research pipeline for finding Amazon product opportunities:

```
Market Scan → Keyword Scan → Product Scan
```

All scripts run against a live SellerSprite browser session via `opencli`.  
All JSON config fields use `{"value": ..., "label": "中文说明"}` — edit `value`, ignore `label`.

---

## Quick Start — Full Pipeline

```bash
# Scan all categories (results in results/YYYY_MM_DD_all/)
python3 scripts/run_pipeline.py

# Restrict to one top-level Amazon category (results in results/YYYY_MM_DD_sports/)
python3 scripts/run_pipeline.py --departments "Sports & Outdoors"

# Multiple categories (results in results/YYYY_MM_DD_sports_home/)
python3 scripts/run_pipeline.py --departments "Sports & Outdoors" "Home & Kitchen"

# Custom run label, reuse yesterday's market scan
python3 scripts/run_pipeline.py --tag retest --skip-market

# Skip both stage 1 and 2, rerun product scan only
python3 scripts/run_pipeline.py --skip-market --skip-keywords
```

`--departments` values must match keys in `pipeline_config.json` → `category_map`.

### Result Directory Structure

Each pipeline run writes to its own directory — runs never overwrite each other:

```
results/
  YYYY_MM_DD_{tag}/
    market_scan_report.md       ← market candidates with risk classification
    market_scan_results.json    ← sidecar for downstream stages
    keywords/
      keyword_scan_report.md    ← keyword candidates across 6 scan modes
      keyword_scan_results.json ← sidecar for product scan
    products/
      scan_principles.md        ← shared selection criteria (batch mode only)
      {category_slug}.md        ← one report per scanned product category
```

### Pipeline Config (`scripts/pipeline_config.json`)

| Key | Default | Purpose |
|---|---|---|
| `pipeline.max_categories_to_products` | 5 | Max green categories forwarded to product scan |
| `pipeline.max_keywords_to_products` | 20 | Max green keywords forwarded to product scan |
| `pipeline.min_green_markets_required` | 1 | Abort if fewer green markets found |
| `category_map` | 15 entries | Amazon top-level category → SellerSprite department number |

---

## Stage 1 — Market Scan

**Config:** `scripts/market_config.json`

```bash
# Standalone (results in results/market_scan_report_YYYY_MM_DD.md)
python3 scripts/select_market.py
python3 scripts/select_market.py --departments "Sports & Outdoors"  # filter by category
```

Scrapes the SellerSprite market research page, applies numeric filters, and classifies
each category as 🟢 Green / 🟡 Yellow / 🔴 Red using `risk_rules`.
`scan_policy.target_candidate_min/max` audits whether the candidate pool is appropriately sized.

Append an XLSX export from SellerSprite to an existing report:

```bash
python3 scripts/import_market_excel.py /path/to/market-research.xlsx \
  --report results/market_scan_report_YYYY_MM_DD.md
```

---

## Stage 2 — Keyword Scan

**Config:** `scripts/keyword_config.json`

```bash
# Standalone (results in results/keywords/keyword_scan_report_YYYY_MM_DD.md)
python3 scripts/scan_keywords.py
```

Runs 6 configurable scan modes against the SellerSprite keyword research page
(趋势市场 / 市场需求 / 搜索飙升 / 高容量低竞争 / 低成本入局 / 长尾细分).
Results are deduplicated across modes and classified as 🟢 / 🟡 / 🔴.

In pipeline mode, `departments` is derived from the market scan results.
In standalone mode, `departments` in `keyword_config.json` controls which top-level
categories are searched (see the `_comment_departments` field for the number→name mapping).

---

## Stage 3 — Product Scan

**Config:** `scripts/product_config.json`

```bash
# Standalone — scans the single category in product_config.json → category
python3 scripts/find_products.py

# Batch mode — scans each category in a JSON file
python3 scripts/find_products.py --categories-file my_categories.json

# With keyword filter (adds includeKeywords to the product filter form)
python3 scripts/find_products.py --keywords-file my_keywords.json
```

Navigates the SellerSprite product research category tree, applies all configured
filters, and writes one Markdown report per scanned category. Each report includes:
- **候选商品列表** — table with Chinese name translation, metrics, and clickable Amazon ASIN links
- **尚未分析的候选类目** — categories from market scan not yet scanned
- **下一步建议** — next actions

In batch/pipeline mode, selection criteria are extracted to a shared `scan_principles.md` in the
same `products/` directory instead of being repeated in every per-category report.

Key filter fields in `product_config.json`:

| Filter | Default | Purpose |
|---|---|---|
| `min/max_monthly_sales` | 100–1000 | Target mid-tier sellers |
| `max_reviews` | 150 | Low competition moat |
| `min_profit_margin` | 50% | Cover FBA + ads |
| `max_package_weight_g` | 1500g | Lightweight advantage |
| `max_sellers` | 2 | Uncrowded market |

The `category` field in `product_config.json` is the standalone default only.
In pipeline mode it is bypassed entirely; categories come from the market scan.

---

## Post-Pipeline — ASIN Keyword Reverse Lookup

After identifying a product from the product scan report, find its advertising keywords:

```bash
python3 scripts/find_asin_keywords.py B0FS72284D
```

**Config:** `scripts/asin_keyword_config.json`

Default filters: monthly searches ≥ 300, organic rank ≤ 100, SPR ≤ 20,
title density ≤ 15, PPC bid ≤ $2.00. Writes:

```
results/asin_keywords_{ASIN}_YYYY_MM_DD.md
```

Optional overrides:

```bash
python3 scripts/find_asin_keywords.py B0FS72284D --limit 20 --wait-seconds 10
```

---

## Typical Workflow

```
1. Run pipeline for one department per day (systematic coverage)
   python3 scripts/run_pipeline.py --departments "Sports & Outdoors"
   python3 scripts/run_pipeline.py --departments "Home & Kitchen"
   ...

2. Review results/{date}_{tag}/market_scan_report.md
   → Confirm green categories make sense

3. Review results/{date}_{tag}/keywords/keyword_scan_report.md
   → Note high-opportunity keywords

4. Review results/{date}_{tag}/products/{category}.md
   → Pick candidate ASINs

5. Run ASIN keyword lookup for each candidate
   python3 scripts/find_asin_keywords.py <ASIN>
```
