---
name: amazon-sourcing
description: Run the Amazon sourcing pipeline and provide LLM analysis of results. Outputs a single pipeline_report_*.md and report.html per run.
---

You are an Amazon product sourcing analyst. Run the unified pipeline, then reason about the results and produce a prioritized recommendation.

## Step 0 — Orient

```bash
ls results/ | sort | tail -10
```

Check if today's results already exist (`results/YYYY_MM_DD/pipeline_report_*.md`). If they do, ask whether to reuse them or run fresh.

**新手前置检查清单**（如为首次开店，在继续前确认以下各项）：
- [ ] 预算 ≥ $3,000（首单备货 + FBA 头程 + PPC 启动费）
- [ ] 已开通或计划开通 Amazon FBA（否则 FBA 毛利率数据不适用）
- [ ] 了解 Amazon 受限类目：膳食补充剂、医疗器械、食品需要额外审批，本管道已从源头过滤这些类目
- [ ] 了解产品责任险要求（针对 $25+ 客单价类目）

---

## Step 1 — Run the unified pipeline

The single entry point runs all three stages (market scan → product scan → keyword lookup) and writes one report:

```bash
cd /path/to/amazon
python3 scripts/run_pipeline.py
```

Output per run (all under `results/YYYY_MM_DD/`):
- `pipeline_report_YYYY_MM_DD.md` — merged human-readable report
- `html/report.html` — visual HTML report with product thumbnails and keyword tables
- `json/market_scan_results.json` — market scan sidecar
- `json/stage1_handoff_YYYY_MM_DD.json` — candidate categories (Stage 1 → 2 handoff)
- `json/stage2_handoff_YYYY_MM_DD.json` — products with image URLs (Stage 2 → 3 handoff)
- `json/stage3_keywords_YYYY_MM_DD.json` — structured keyword data per category

Optional flags:
- `--skip-asin-keywords` — skip Stage 3 (faster, products only)
- `--dry-run` — validate config without opening SellerSprite
- `--date YYYY_MM_DD` — write results under a specific date directory
- `--start-from 2` — skip Stage 1, resume from saved stage1 handoff JSON
- `--start-from 3` — skip Stages 1 & 2, re-run keyword lookup only (useful when tuning keyword filters)

The pipeline config (`scripts/pipeline_config.json`) controls all three stages in one file.

---

## Step 2 — Read and analyze the pipeline report

```bash
cat results/YYYY_MM_DD/pipeline_report_YYYY_MM_DD.md
```

The report contains three sections in order:
1. **市场扫描** — categories scored Green/Yellow/Red with metrics
2. **产品扫描** — per-category qualified products with price, sales, margin, reviews
3. **关键词反查** — per-category keyword tables (batch traffic-extend lookup)

Read the full report, then write a 3–5 bullet market summary covering:
- Best opportunity clusters (categories with ≥2 strong ASINs, low reviews, light weight)
- Keyword signal strength (high-volume keywords with low SPR and low title density)
- Red flags (high CN ratio, categories skipped due to nav-fallback collision)

---

## Step 3 — Prioritize top candidates

From the product sections, extract and rank the top 15–20 ASINs across all categories. Scoring logic:

```python
import json, re

def number(v):
    m = re.search(r"[\d,.]+", str(v or ""))
    return float(m.group(0).replace(",", "")) if m else 0.0

s2 = json.loads(open("results/YYYY_MM_DD/json/stage2_handoff_YYYY_MM_DD.json").read())
products = s2["products"]
# Sort by: monthly_sales / (reviews + 10) + profit_margin / 10
```

For each candidate ASIN, state:
- **机会点**: low reviews + high sales + keyword has volume/low SPR
- **风险点**: high CN ratio, certification flags
- **建议下一步**: 1688 search term, MOQ target, whether to build listing now

---

## Step 4 — Re-run keyword lookup only (if needed)

If you only want to tune keyword filters without re-scraping market/products:

```bash
python3 scripts/run_pipeline.py --start-from 3
```

This reads `json/stage2_handoff_YYYY_MM_DD.json`, re-runs Stage 3 with current config, and regenerates the pipeline report and HTML.

---

## Step 5 — Generate HTML report standalone (if needed)

```bash
python3 scripts/generate_html_report.py --date YYYY_MM_DD
```

Reads the three stage JSON files and writes `results/YYYY_MM_DD/html/report.html`.
Requires stage1, stage2, and optionally stage3 JSON files to exist.
