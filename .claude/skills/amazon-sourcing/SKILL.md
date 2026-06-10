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

**新手前置检查清单**（如为首次开店，在继续前确认以下各项）：
- [ ] 预算 ≥ $3,000（首单备货 + FBA 头程 + PPC 启动费）
- [ ] 已开通或计划开通 Amazon FBA（否则 FBA 毛利率数据不适用）
- [ ] 了解 Amazon 受限类目：膳食补充剂、医疗器械、食品需要额外审批，本管道已从源头过滤这些类目
- [ ] 了解产品责任险要求（针对 $25+ 客单价类目）

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

Pick green categories that best match keyword signals. Prioritize uncovered ones.  
For **narrow** runs pick 3–8; for **full sweeps** pass all uncovered categories at once.

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
  --market-sidecar $MARKET_SIDECAR \
  --batch-size 15 --top-n 60
```

`--batch-size 15` causes `top_picks.md` to be written automatically after every 15 categories and once more at the end. Omit for small runs (< 15 categories); top_picks is still written at the end.

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

## Step 6 — Review top_picks.md and add analysis

`top_picks.md` is written automatically by `find_products.py` (via `aggregate_top_picks.py`).  
If the scan was run **without** `--batch-size`, generate it manually:

```bash
python3 scripts/aggregate_top_picks.py --run-dir $RUN_DIR --top-n 50
```

The auto-generated report contains:
- Scored table with 推荐理由
- **`## 新手优先聚类`** — 自动识别的 2-5 个产品集群，每个集群有 ≥2 个 ASIN 入榜。这是新手最应关注的机会，同一类目多个 ASIN 同时排名代表信号强度高，不是偶然。优先在 1688 验证这些类目的 COGS。
- **`⚠️混入` 标记** — 推荐理由列中含此标记的产品来自已知的"垃圾桶类目"（如 Deck Hardware），该类目被卖家滥用归类，产品与类目名称无真实对应关系。**不要按类目名称去找供货**，需直接用产品名在 1688 搜索。

Your job in this step is to **add the narrative sections** that require LLM judgment:

Open `$RUN_DIR/top_picks.md` and append or fill in:

```markdown
## 市场环境小结 / 关键词信号
[各2–3句：本次扫描发现的类目机会、关键词信号、竞争格局变化]

## 各产品详细分析（重点前10名）
### 1. [ASIN] 中文名 / English Name
**机会点** / **风险点** / **建议下一步**

## 下次优先探索
[尚未覆盖的绿色类目 + 建议运行参数]
```

Be specific (actual ASINs, metrics). Every product needs a concrete next step. If fewer than 20 strong candidates, say so and recommend next run scope.

---

## Step 7 — Generate grid image

```bash
python3 scripts/generate_grid_image.py \
  --picks $RUN_DIR/top_picks.md \
  --top-n 60 --width 1440
```

Output: `$RUN_DIR/top_picks_grid.jpg` — 4 columns, each card shows product image, rank badge, name, price, and 推荐理由.

Image URLs are auto-loaded from `$RUN_DIR/products/asin_images.json` (written by `find_products.py` during scan). No extra steps needed if the product scan used `--output-dir`.
