# Amazon Scan Pipeline

```
Market Scan → Keyword Scan → Product Scan
```

Scripts run against a live SellerSprite session via `opencli`.  
Config fields: `{"value": ..., "label": "..."}` — edit `value` only.

---

## Pipeline

```bash
python3 scripts/run_pipeline.py                                    # all categories
python3 scripts/run_pipeline.py --departments "Sports & Outdoors"  # one category
python3 scripts/run_pipeline.py --skip-market                      # reuse market scan
python3 scripts/run_pipeline.py --skip-market --skip-keywords      # product scan only
```

Results go to `results/YYYY_MM_DD_{tag}/`. Key configs in `pipeline_config.json`:
- `max_categories_to_products` (default 5) — green categories forwarded to product scan
- `max_keywords_to_products` (default 20) — green keywords forwarded as product filter
- `category_map` — Amazon top-level category → SellerSprite department number

---

## Standalone

```bash
python3 scripts/select_market.py                   # stage 1
python3 scripts/scan_keywords.py                   # stage 2
python3 scripts/find_products.py                   # stage 3, single category
python3 scripts/find_products.py --categories-file cats.json  # stage 3, batch

python3 scripts/find_asin_keywords.py B0FS72284D   # reverse keyword lookup on ASIN
python3 scripts/import_market_excel.py market.xlsx --report results/market_scan_report.md
```

---

## Workflow

```
1. python3 scripts/run_pipeline.py --departments "Sports & Outdoors"
2. Review results/{date}_sports/market_scan_report.md  → green categories
3. Review results/{date}_sports/keywords/keyword_scan_report.md  → top keywords
4. Review results/{date}_sports/products/{category}.md  → candidate ASINs
5. python3 scripts/find_asin_keywords.py <ASIN>  → ad keyword research
```
