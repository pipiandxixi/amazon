# Amazon Scan Pipeline

The project contains two independent SellerSprite scans. Both output Markdown
reports only. No JSON result files are created.

## Market Scan

```bash
python3 scripts/select_market.py
```

The scan saves every unique category returned across the configured number of
pages, classifies all results as green/yellow/red, and writes:

```text
results/categories/market_scan_report_YYYY_MM_DD.md
```

It does not select a fixed Top-K. `scan_policy.target_candidate_min/max` audits
whether the green and yellow candidate pool is too broad or too narrow.

## Keyword Scan

```bash
python3 scripts/scan_keywords.py
```

The mode is controlled by `scripts/keyword_config.json`:

- Non-empty `target_groups`: scan each configured niche with its comma-separated
  seed keywords and `targeted_filter_params`.
- Empty `target_groups`: run the independent global scan with `filter_params`.

SellerSprite treats comma-separated include keywords as OR. Keep multiple
synonymous seeds for the same niche in one group. Do not combine unrelated
niches in one group because the returned keywords cannot be attributed cleanly.

Both modes write:

```text
results/keywords/keyword_scan_report_YYYY_MM_DD.md
```
