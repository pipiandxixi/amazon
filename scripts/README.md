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
python3 scripts/run_pipeline.py --max-categories 10                # scan more categories
```

Results go to `results/YYYY_MM_DD_{tag}/`. Key configs in `market_config.json`:
- `scan_policy.min_green_required` — minimum green markets to continue pipeline
- `category_map` — Amazon top-level category → SellerSprite department number

---

## Standalone

```bash
python3 scripts/select_market.py                                   # stage 1
python3 scripts/select_market.py --departments "Sports & Outdoors" # stage 1, filtered
python3 scripts/scan_keywords.py                                   # stage 2
python3 scripts/find_products.py                                   # stage 3, single category
python3 scripts/find_products.py --categories-file cats.json       # stage 3, batch

python3 scripts/find_asin_keywords.py B0FS72284D                   # reverse keyword lookup
```

---

## LLM-driven workflow

Use the `amazon-sourcing` skill (Claude Code) to run the pipeline with LLM analysis
between stages — choosing which categories and keywords to forward based on data:

```
/amazon-sourcing
```

---

## Manual workflow

```
1. python3 scripts/run_pipeline.py --departments "Sports & Outdoors"
2. Review results/{date}_sports/market_scan_report.md  → green categories
3. Review results/{date}_sports/keywords/keyword_scan_report.md  → top keywords
4. Review results/{date}_sports/products/{category}.md  → candidate ASINs
5. python3 scripts/find_asin_keywords.py <ASIN>  → ad keyword research
```
