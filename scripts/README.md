# Amazon Scan Pipeline

```
Market Scan → Keyword Scan → Product Scan
```

Scripts run against a live SellerSprite session via `opencli`.  
Config fields: `{"value": ..., "label": "..."}` — edit `value` only.
Default outputs are grouped by run date under `results/YYYY_MM_DD/`.

---

## Scripts

```bash
python3 scripts/select_market.py                                   # stage 1
python3 scripts/select_market.py --departments "Sports & Outdoors" # stage 1, filtered
python3 scripts/scan_keywords.py                                   # stage 2
python3 scripts/find_products.py                                   # stage 3, single category
python3 scripts/find_products.py --categories-file cats.json       # stage 3, batch

python3 scripts/find_asin_keywords.py B0FS72284D                   # reverse keyword lookup
```

The default single-category product config currently scans `Swing Trainers`.
Market, product, and ASIN-keyword reports record whether the free plan may have
truncated the visible results.

---

## Workflow

Use the `amazon-sourcing` skill in Claude Code — it runs each stage and analyzes
results between steps to decide what to forward downstream:

```
/amazon-sourcing
```

Manual order:
```
1. select_market.py  → market_scan_results.json  (read, decide which categories)
2. scan_keywords.py  → keyword_scan_results.json  (read, decide which keywords)
3. find_products.py  → products/{category}.md
4. find_asin_keywords.py <ASIN>  → ad keyword research
```
