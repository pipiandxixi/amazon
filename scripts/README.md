# Amazon Scan Pipeline

```
Market Scan → Keyword Scan → Product Scan
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
market candidates → product categories
product ASINs → reverse keyword lookup
```

Result JSON files remain available for auditing, but are never used to drive the
next stage. `pipeline_config.json` contains static filters and policies only; it
does not contain a preselected category, keyword, product, or ASIN.

Market, product, and ASIN-keyword reports record whether the free plan may have
truncated visible results.

The final human-readable output is combined into
`results/YYYY_MM_DD/pipeline_report_YYYY_MM_DD.md`. Individual stage reports are
kept beside it for auditing.

## Individual Stage Debugging

The original scripts and configs remain available for isolated debugging. They
are not the recommended end-to-end workflow.
