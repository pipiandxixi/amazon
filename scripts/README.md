# Amazon Scan Pipeline

The pipeline follows this order:

1. Find promising green leaf categories.
2. Find qualified products inside one exact leaf category.
3. Reverse-search selected product ASINs for advertising keyword candidates.

All scripts output Markdown reports under `results/`.

All JSON configuration fields use:

```json
"parameter_name": {"value": 100, "label": "参数的中文含义"}
```

Edit `value`; scripts ignore `label`.

## Market Scan

```bash
python3 scripts/select_market.py
```

The scan saves every unique category returned across the configured number of
pages, classifies all results as green/yellow/red, and writes:

```text
results/market_scan_report_YYYY_MM_DD.md
```

It does not select a fixed Top-K. `scan_policy.target_candidate_min/max` audits
whether the green and yellow candidate pool is too broad or too narrow.

Append all fields from a SellerSprite market-research XLSX export:

```bash
python3 scripts/import_market_excel.py /path/to/market-research.xlsx \
  --report results/market_scan_report_YYYY_MM_DD.md
```

The importer uses only the Python standard library and replaces the previous
Excel appendix when rerun.

## Product Scan

```bash
python3 scripts/find_products.py
```

The product scan is controlled by `scripts/product_config.json`. Set:

- `category.path` to the exact SellerSprite leaf category path.
- `filters` to the qualified-product thresholds.
- `scan_policy.max_products` to the maximum number of independent products.

Each configurable field keeps its Chinese meaning beside the value:

```json
"min_monthly_sales": {"value": "100", "label": "月销量最小值"}
```

Edit `value`; `label` is documentation and is ignored by the scripts.

The script selects the exact leaf category, applies product filters, disables
`展示所有变体`, and writes a report containing product metrics and ASINs:

```text
results/product_scan_<category>_YYYY_MM_DD.md
```

The default config currently scans `Float Valves` using the validated
new-seller thresholds:

- Monthly sales: `100-1000`
- Variants: `1-5`
- Price: `$15-$60`
- Reviews: `<=150`
- Rating: `4.0-5.0`
- Profit margin: `>=50%`
- Package weight: `<=1500g`
- Sellers: `1-2`
- Fulfillment: `FBA`
- Exact leaf-category ranking only; hide duplicate variants

## ASIN Keyword Scan

After choosing a qualified product from the product report, reverse-search its
ASIN:

```bash
python3 scripts/find_asin_keywords.py B0FS72284D
```

The keyword scan is controlled by `scripts/asin_keyword_config.json`. Its
default promotion-candidate filters are:

- Monthly searches: `>=300`
- Monthly purchases: `>=10`
- Organic rank: `<=100`
- SPR: `<=20`
- Title density: `<=15`
- Related products: `<=15000`
- PPC exact-match suggested bid: `<=$2.00`
- Traffic type: organic or advertising keywords
- Exclude configured competitor brands, model numbers, and irrelevant terms
- Exclude keywords without numeric search-volume data

The same config also controls ranking weights, result count, and wait times.
Its fields use the same adjacent `{ "value": ..., "label": ... }` format.
Optional command-line overrides:

```bash
python3 scripts/find_asin_keywords.py B0FS72284D \
  --config scripts/asin_keyword_config.json \
  --limit 20 \
  --wait-seconds 10
```

The script uses SellerSprite keyword reverse lookup and ranks candidates using
traffic share, search volume, purchases, and organic rank. It writes:

```text
results/asin_keywords_<ASIN>_YYYY_MM_DD.md
```

These are product-level advertising candidates. They are intentionally not
merged back into the market/category report.
