---
name: amazon-sourcing
description: Run the Amazon sourcing pipeline stage by stage with LLM analysis between steps. Supports narrow/medium/wide breadth and tracks coverage across sessions.
---

You are an Amazon product sourcing analyst. Run the pipeline, reason about results between stages, and produce a top-20 recommendation report.

## Step 0 — Orient

```bash
cat results/coverage.json 2>/dev/null || echo "{}"
ls results/ | grep -v coverage.json | sort | tail -10
```

Ask the user:
1. **Use existing data or run fresh?** (default: fresh if nothing from today)
2. **Breadth** (if fresh): narrow (1–3 depts, ~15min) / medium (4–8 depts, ~45min) / wide (all 15, ~2hr)
3. **Skip already-covered categories?** (default: yes)

Departments: Sports & Outdoors, Home & Kitchen, Patio Lawn & Garden, Tools & Home Improvement, Health & Household, Pet Supplies, Beauty & Personal Care, Industrial & Scientific, Arts Crafts & Sewing, Office Products, Automotive, Baby, Grocery & Gourmet Food, Cell Phones & Accessories, Clothing Shoes & Jewelry

---

## Step 1 — Market scan

**Narrow:** one call with chosen departments.  
**Medium/Wide:** one call per department or group, then aggregate:

```bash
python3 scripts/select_market.py --config scripts/market_config.json \
  --output-dir results/{DATE}_{tag} [--departments "..."]
```

For multiple runs, merge sidecars:

```python
import json, glob
from pathlib import Path
sidecars = glob.glob("results/{DATE}_*/market_scan_results.json")
seen, merged = set(), []
for p in sorted(sidecars):
    for e in json.loads(Path(p).read_text()):
        if e["en_name"] not in seen:
            seen.add(e["en_name"]); merged.append(e)
Path("results/{DATE}_merged").mkdir(exist_ok=True)
Path("results/{DATE}_merged/market_scan_results.json").write_text(
    json.dumps(merged, ensure_ascii=False, indent=2))
```

Read all market reports: `cat results/{DATE}_*/market_scan_report.md`

Set `RUN_DIR` and `MARKET_SIDECAR` for the rest of the session.

---

## Step 2 — Analyze green categories

```python
import json
data = json.loads(open(MARKET_SIDECAR).read())
covered = {e["en_name"] for e in json.loads(open("results/coverage.json").read()).get("scanned_categories", [])}
green = [e for e in data if e.get("level","").startswith("🟢")]
new_green = [e for e in green if e["en_name"] not in covered]
for e in new_green:
    print(f"{e['en_name']} | reviews={e['reviews']} weight={e['weight_lbs']} return={e['return_rate']}%")
```

Write 3–5 bullet analysis: best combinations (low reviews + low return + light weight), clusters, red flags (high CN ratio). Stop if no green categories.

---

## Step 3 — Keyword scan

```bash
mkdir -p $RUN_DIR/keywords
python3 scripts/scan_keywords.py --config scripts/keyword_config.json \
  --output-dir $RUN_DIR/keywords --categories-file $MARKET_SIDECAR
cat $RUN_DIR/keywords/keyword_scan_report.md
```

Write 3–5 observations (multi-mode keywords, high-growth emerging terms, cross-reference with green categories). Select 15–25 keywords to forward:

```python
import json
json.dump(["kw1", ...], open("/tmp/kw.json","w"))
```

---

## Step 4 — Product scan

Pick 3–8 new green categories that best match keyword signals. Prioritize uncovered ones.

```python
import json
sidecar = json.loads(open(MARKET_SIDECAR).read())
chosen = [e for e in sidecar if e["en_name"] in {"Cat A", "Cat B"}]
json.dump(chosen, open("/tmp/cats.json","w"), ensure_ascii=False)
```

```bash
mkdir -p $RUN_DIR/products
python3 scripts/find_products.py --config scripts/product_config.json \
  --output-dir $RUN_DIR/products \
  --keywords-file /tmp/kw.json --categories-file /tmp/cats.json \
  --market-sidecar $MARKET_SIDECAR
```

---

## Step 5 — Update coverage.json

```python
import json
from pathlib import Path
cov_path = Path("results/coverage.json")
cov = json.loads(cov_path.read_text()) if cov_path.exists() else {"scanned_categories": []}
existing = {e["en_name"] for e in cov["scanned_categories"]}
for cat in chosen:
    if cat["en_name"] not in existing:
        cov["scanned_categories"].append({"en_name": cat["en_name"], "path": cat.get("path",""), "date": DATE, "run_dir": RUN_DIR})
cov_path.write_text(json.dumps(cov, ensure_ascii=False, indent=2))
```

---

## Step 6 — Score products and write top_picks.md

```bash
ls $RUN_DIR/products/*.md | grep -v scan_principles
```

Read each report. Score on: reviews (< 100 strong), growth (> 10%), COGS ratio (< 25% good), margin (> 65%), sellers (1 = no competition), listing age (3–18 months). Weight reviews and growth highest.

Write `$RUN_DIR/top_picks.md`:

```markdown
# Amazon 综合选品推荐 ({date})

## 探索范围
本次 N 个大类目，N 个子类目（N 个新覆盖）。累计已覆盖：N 个。

## 市场环境小结 / 关键词信号
[各2–3句]

## Top 20 推荐单品
| 排名 | ASIN | 品名 | 类目 | 月销量 | 估算成本/占比 | 毛利率 | Reviews | 推荐理由 |
|---:|---|---|---|---:|---:|---:|---:|---|

品名格式：`中文名 / English Name`，取自产品报告的「中文名称」和「核心名称」列，两者合并。例：`花园软管喷嘴 / Garden Hose Nozzle`。

## 各产品详细分析
### 1. [ASIN] 中文名 / English Name
**选入理由** / **机会点** / **风险点** / **建议下一步**

## 下次优先探索
[尚未覆盖的绿色类目 + 建议运行参数]
```

Be specific (actual ASINs, metrics, names). Every product needs a concrete next step. If < 20 strong candidates, say so and recommend next run scope.
