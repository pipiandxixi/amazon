---
name: amazon-sourcing
description: Run the Amazon sourcing pipeline and provide LLM analysis of results. Outputs a single pipeline_report_*.md per run.
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
python3 scripts/run_pipeline.py --config scripts/pipeline_config.json
```

Output per run:
- `results/YYYY_MM_DD/pipeline_report_YYYY_MM_DD.md` — complete human-readable report (market + products + keywords)
- `results/YYYY_MM_DD/market_scan_results.json` — machine-readable sidecar for re-analysis

Optional flags:
- `--skip-asin-keywords` — skip the keyword stage (faster, products only)
- `--dry-run` — validate config without opening SellerSprite
- `--date YYYY_MM_DD` — write results under a specific date directory

The pipeline config (`scripts/pipeline_config.json`) controls all three stages in one file. Edit it to adjust filters, scoring weights, candidate levels (Green/Yellow), and keyword filter thresholds.

---

## Step 2 — Read and analyze the pipeline report

```bash
cat results/YYYY_MM_DD/pipeline_report_YYYY_MM_DD.md
```

The report contains three sections in order:
1. **市场扫描** — 30 categories scored Green/Yellow/Red with metrics
2. **产品扫描** — per-category qualified products with price, sales, margin, reviews
3. **关键词反查** — per-category keyword tables (batch traffic-extend lookup, up to 20 ASINs/category)

Read the full report, then write a 3–5 bullet market summary covering:
- Best opportunity clusters (categories with ≥2 strong ASINs, low reviews, light weight)
- Keyword signal strength (high-volume keywords with low SPR and low title density)
- Red flags (high CN ratio, nav-fallback categories sharing the same product pool)

---

## Step 3 — Prioritize top candidates

From the product sections, extract and rank the top 15–20 ASINs across all categories. Scoring logic:

```python
import json, re

def number(v):
    m = re.search(r"[\d,.]+", str(v or ""))
    return float(m.group(0).replace(",", "")) if m else 0.0

sidecar = json.loads(open("results/YYYY_MM_DD/market_scan_results.json").read())
green_yellow = {e["en_name"] for e in sidecar if not e.get("level","").startswith("🔴")}
```

For each candidate ASIN, state:
- **机会点**: low reviews + high sales + keyword has volume/low SPR
- **风险点**: nav-fallback contamination, high CN ratio, certification flags
- **建议下一步**: 1688 search term, MOQ target, whether to build listing now

---

## Step 4 — Identify nav-fallback contamination

Check the pipeline log or report for `[nav-fallback]` warnings. Categories affected share the same "Sports & Outdoors" product pool and produce duplicate ASIN sets across different category keyword files. Flag these to the user — their keyword data is valid but product scan data is not category-specific.

---

## Step 5 — Generate grid image (optional)

The grid image requires ASIN images fetched separately. This only works if you have a `products/` directory from a standalone `find_products.py` run:

```bash
python3 scripts/fetch_asin_images.py --run-dir results/YYYY_MM_DD
python3 scripts/generate_grid_image.py --picks results/YYYY_MM_DD/top_picks.md --top-n 60 --width 1440
```

> Note: The unified pipeline does not write `products/*.md` or `asin_images.json`. To use the grid image, run `find_products.py` standalone with `--output-dir results/YYYY_MM_DD/products`.

---

## Advanced: run individual stages manually

If you need to run only one stage (e.g., re-run keywords without redoing the market scan):

**Market scan only:**
```bash
python3 scripts/select_market.py --config scripts/market_config.json
# writes results/YYYY_MM_DD/market_scan_report.md and market_scan_results.json
```

**Product scan only (batch mode):**
```bash
python3 scripts/find_products.py --config scripts/product_config.json \
  --categories-file /tmp/cats.json --output-dir results/YYYY_MM_DD/products \
  --batch-size 15 --top-n 60
# writes per-category .md files and top_picks.md
```

**Keyword lookup only (single category):**
```bash
python3 scripts/find_asin_keywords.py ASIN1 ASIN2 ... \
  --category "Category Name" --config scripts/asin_keyword_config.json
# writes results/YYYY_MM_DD/category_keywords_{slug}_YYYY_MM_DD.md
```
