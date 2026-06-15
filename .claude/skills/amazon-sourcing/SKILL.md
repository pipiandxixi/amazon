---
name: amazon-sourcing
description: Run the Amazon sourcing pipeline and provide LLM analysis of results. Outputs a persistent categories.json DB and report.html per run.
---

You are an Amazon product sourcing analyst. Run the unified pipeline, then reason about the results and produce a prioritized recommendation.

## Step 0 — Orient

```bash
ls -la results/html/report.html 2>/dev/null && echo "exists" || echo "no report yet"
ls -la results/json/categories.json 2>/dev/null && echo "DB exists" || echo "no DB yet"
```

If `categories.json` exists, check how stale it is and ask whether to resume batch processing or run a fresh market scan.

**新手前置检查清单**（如为首次开店，在继续前确认以下各项）：
- [ ] 预算 ≥ $3,000（首单备货 + FBA 头程 + PPC 启动费）
- [ ] 已开通或计划开通 Amazon FBA（否则 FBA 毛利率数据不适用）
- [ ] 了解 Amazon 受限类目：膳食补充剂、医疗器械、食品需要额外审批，本管道已从源头过滤这些类目
- [ ] 了解产品责任险要求（针对 $25+ 客单价类目）

---

## Step 1 — Run the pipeline

All output lands flat under `results/` — there are no date subdirectories.

### Full run (all three stages)

```bash
python3 scripts/run_pipeline.py
```

### Resume batch (skip market scan, continue products + keywords)

```bash
python3 scripts/run_pipeline.py --skip-market-scan --max-categories 5
```

Use this when `categories.json` already exists and you're iterating through categories in batches of 5.

### Market scan only (inspect before processing)

```bash
python3 scripts/run_pipeline.py --market-scan-only
```

### Common flags

| Flag | Effect |
|------|--------|
| `--skip-market-scan` | Skip market scan; use existing `categories.json` |
| `--market-scan-only` | Run market scan only, stop before product loop |
| `--max-categories N` | Process at most N categories (ordered by staleness) |
| `--skip-keywords` | Skip keyword lookup, products only |

### Output files (all flat under `results/`)

| File | Contents |
|------|----------|
| `results/json/categories.json` | **Persistent DB** — single source of truth; updated after every category |
| `results/json/market_scan_results.json` | Market scan sidecar (Stage 1 candidates with metrics) |
| `results/html/report.html` | Visual HTML report with thumbnails and clickable keyword links |
| `index.html` | Auto-updated redirect to `results/html/report.html` |

---

## Step 2 — Read and analyze results

The primary data source is `results/json/categories.json`. Each entry contains:
- `level` — 🟢/🟡/🔴 from market scan
- `products` — list of qualifying ASINs with price, sales, margin, reviews
- `keywords` — ranked keyword objects with volume, SPR, title density
- `last_updated` — ISO timestamp of last product+keyword scan

```bash
python3 -c "
import json; db = json.load(open('results/json/categories.json'))
scanned = [(k, v) for k, v in db.items() if v.get('last_updated')]
print(f'{len(scanned)}/{len(db)} categories scanned')
for k, v in sorted(scanned, key=lambda x: x[1]['last_updated'], reverse=True)[:10]:
    prods = len(v.get('products') or [])
    kws = len((v.get('keywords') or {}).get('keywords') or [])
    print(f'  {k}: {prods} products, {kws} keywords, updated {v[\"last_updated\"][:10]}')
"
```

Then open `results/html/report.html` in a browser for the visual view.

Write a 3–5 bullet market summary covering:
- Best opportunity clusters (categories with ≥2 strong ASINs, low reviews, light weight)
- Keyword signal strength (high-volume keywords with low SPR and low title density)
- Red flags (high CN ratio, categories skipped due to nav-fallback collision)

---

## Step 3 — Prioritize top candidates

Load directly from `categories.json`:

```python
import json, re

def number(v):
    m = re.search(r"[\d,.]+", str(v or ""))
    return float(m.group(0).replace(",", "")) if m else 0.0

db = json.load(open("results/json/categories.json"))
candidates = []
for cat_name, cat in db.items():
    for p in (cat.get("products") or []):
        score = number(p.get("monthly_sales")) / (number(p.get("reviews")) + 10) \
              + number(p.get("profit_margin")) / 10
        candidates.append({**p, "category": cat_name, "score": score})

top = sorted(candidates, key=lambda x: x["score"], reverse=True)[:20]
```

For each top ASIN, state:
- **机会点**: low reviews + high sales + keyword has volume/low SPR
- **风险点**: high CN ratio, certification flags
- **建议下一步**: 1688 search term, MOQ target, whether to build listing now

---

## Step 4 — Regenerate HTML standalone (if needed)

```bash
python3 scripts/generate_html_report.py
```

Reads `results/json/categories.json` and rewrites `results/html/report.html`. No flags required.
