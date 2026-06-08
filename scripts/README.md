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

## Global Keyword Scan

```bash
python3 scripts/scan_keywords.py
```

The keyword scan is global and independent. It does not read market results,
candidate categories, or seed keywords. It writes:

```text
results/keywords/keyword_scan_report_YYYY_MM_DD.md
```
