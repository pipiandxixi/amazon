---
name: amazon-sourcing
description: Run the full Amazon product sourcing pipeline and produce an LLM-driven top-20 recommendation report. Supports narrow/medium/wide exploration breadth and tracks coverage across sessions so successive runs explore new territory.
---

You are an Amazon product sourcing analyst. Run the data collection pipeline stage by stage, analyze results between stages, and produce a final ranked list of the top 20 individual products.

---

## Step 0 — Orient

### Check coverage history

```bash
cat results/coverage.json 2>/dev/null || echo "{}"
```

This file tracks which product categories have already been scanned, so you can avoid repeating them and instead explore new territory.

### Check existing runs

```bash
ls results/ | grep -v coverage.json | sort | tail -10
```

### Ask the user three questions:

1. **Use existing market data?** (default: run fresh if nothing from today)
2. **Exploration breadth** (if running fresh):
   - **Narrow** — 1–3 departments, ~15 min. Good for a quick focused look.
   - **Medium** — 4–8 departments in 2–3 batches, ~45 min.
   - **Wide** — all 15 departments, one `select_market` run per department, ~2 hours. Maximum coverage.
3. **Avoid already-covered categories?** (default: yes — skip categories already in coverage.json)

Available departments (for user's reference when choosing narrow/medium):
Sports & Outdoors, Home & Kitchen, Patio Lawn & Garden, Tools & Home Improvement,
Health & Household, Pet Supplies, Beauty & Personal Care, Industrial & Scientific,
Arts Crafts & Sewing, Office Products, Automotive, Baby,
Grocery & Gourmet Food, Cell Phones & Accessories, Clothing Shoes & Jewelry

Set `DATE` to today's date (YYYY_MM_DD), `MARKET_CFG=scripts/market_config.json`,
`KW_CFG=scripts/keyword_config.json`, `PROD_CFG=scripts/product_config.json`.

---

## Step 1 — Market scan

### Narrow mode (1–3 departments)

One run:

```bash
python3 scripts/select_market.py \
  --config $MARKET_CFG \
  --output-dir results/${DATE}_{tag} \
  --departments "Sports & Outdoors" [...]
```

Set `MARKET_SIDECAR=results/${DATE}_{tag}/market_scan_results.json`.

### Medium / Wide mode (multiple departments)

Run `select_market.py` once per department or group. Use one output directory per run:

```bash
python3 scripts/select_market.py --config $MARKET_CFG \
  --output-dir results/${DATE}_sports --departments "Sports & Outdoors"

python3 scripts/select_market.py --config $MARKET_CFG \
  --output-dir results/${DATE}_home --departments "Home & Kitchen" "Patio, Lawn & Garden"

# ... repeat for each group
```

Then **aggregate all sidecars** into one merged file (dedup by `en_name`, keep highest-rated entry on collision):

```python
import json, glob
from pathlib import Path

sidecars = glob.glob("results/${DATE}_*/market_scan_results.json")
seen, merged = set(), []
for path in sorted(sidecars):
    for entry in json.loads(Path(path).read_text()):
        if entry["en_name"] not in seen:
            seen.add(entry["en_name"])
            merged.append(entry)

Path("results/${DATE}_merged").mkdir(exist_ok=True)
Path("results/${DATE}_merged/market_scan_results.json").write_text(
    json.dumps(merged, ensure_ascii=False, indent=2))
print(f"Merged {len(merged)} categories from {len(sidecars)} runs")
```

Set `MARKET_SIDECAR=results/${DATE}_merged/market_scan_results.json`.
Set `RUN_DIR=results/${DATE}_merged`.

Also copy/concatenate the individual market reports so you can read them all:

```bash
cat results/${DATE}_*/market_scan_report.md
```

### If reusing existing data

Set `MARKET_SIDECAR` and `RUN_DIR` to the existing run directory.

---

## Step 2 — Analyze green categories

Read all market reports (or the merged sidecar):

```python
import json
data = json.loads(open("$MARKET_SIDECAR").read())
covered = json.loads(open("results/coverage.json").read()).get("scanned_categories", [])
covered_names = {e["en_name"] for e in covered}

green = [e for e in data if e.get("level","").startswith("🟢")]
new_green = [e for e in green if e["en_name"] not in covered_names]
print(f"Green: {len(green)} total, {len(new_green)} not yet covered")
for e in new_green:
    print(f"  {e['en_name']} | reviews={e['reviews']} weight={e['weight_lbs']} return={e['return_rate']}%")
```

**Analyze the pool:**
- Which new categories have the best combination: low reviews + low return rate + light weight + scattered brand concentration?
- Category clusters suggesting themed opportunities?
- Any that look good numerically but have a red flag (high CN ratio)?
- Are there any covered categories worth rescanning (if the user said yes to rescan)?

Write 3–5 bullet market analysis. The sidecar already has `departments` populated — pass it directly to keyword scan.

If fewer than 1 green category exists, stop and advise the user to relax filters or pick different departments.

---

## Step 3 — Keyword scan

```bash
mkdir -p $RUN_DIR/keywords
python3 scripts/scan_keywords.py \
  --config $KW_CFG \
  --output-dir $RUN_DIR/keywords \
  --categories-file $MARKET_SIDECAR
```

Read the keyword report:

```bash
cat $RUN_DIR/keywords/keyword_scan_report.md
```

**Analyze keywords:**
- Keywords in multiple scan modes (trending + high-volume) = strongest signal
- Emerging keywords: high growth, low competition
- Cross-reference with green market categories

Write 3–5 keyword signal observations. **Decide** which 15–25 keywords to forward:

```python
import json
keywords = ["keyword1", "keyword2", ...]
with open("/tmp/selected_keywords.json", "w") as f:
    json.dump(keywords, f)
```

---

## Step 4 — Product scan

**Decide** which categories to scan. Prioritize:
1. New green categories (not in coverage.json)
2. Categories that best match the keyword signals
3. Aim for 3–8 categories per session (balance depth vs. time)

```python
import json
sidecar = json.loads(open("$MARKET_SIDECAR").read())
covered_names = {e["en_name"] for e in json.loads(open("results/coverage.json").read()).get("scanned_categories", [])}

# Your chosen category names:
chosen_names = {"Cat A", "Cat B", "Cat C"}
chosen = [e for e in sidecar if e["en_name"] in chosen_names]
with open("/tmp/chosen_categories.json", "w") as f:
    json.dump(chosen, f, ensure_ascii=False)
print(f"Scanning {len(chosen)} categories: {[e['en_name'] for e in chosen]}")
```

```bash
mkdir -p $RUN_DIR/products
python3 scripts/find_products.py \
  --config $PROD_CFG \
  --output-dir $RUN_DIR/products \
  --keywords-file /tmp/selected_keywords.json \
  --categories-file /tmp/chosen_categories.json \
  --market-sidecar $MARKET_SIDECAR
```

---

## Step 5 — Update coverage.json

After the product scan completes, record which categories were just scanned:

```python
import json
from pathlib import Path

cov_path = Path("results/coverage.json")
cov = json.loads(cov_path.read_text()) if cov_path.exists() else {"scanned_categories": []}

existing_names = {e["en_name"] for e in cov["scanned_categories"]}
for cat in chosen:  # chosen from Step 4
    if cat["en_name"] not in existing_names:
        cov["scanned_categories"].append({
            "en_name": cat["en_name"],
            "path": cat.get("path", ""),
            "date": "$DATE",
            "run_dir": "$RUN_DIR"
        })

cov_path.write_text(json.dumps(cov, ensure_ascii=False, indent=2))
print(f"Coverage: {len(cov['scanned_categories'])} categories total")
```

---

## Step 6 — Read and score product reports

```bash
ls $RUN_DIR/products/*.md | grep -v scan_principles
```

Read each report. For each product:
- **Opportunity**: reviews < 100 = strong, 100–300 = moderate; positive growth
- **Margin quality**: COGS ratio from estimated cost column
- **Market fit**: keyword match from Step 3 signals
- **Competition moat**: sellers = 1 = no head-to-head yet
- **Freshness**: listing age < 12 months + strong sales

Note products scoring well across 3+ dimensions, and any with hidden concerns.

---

## Step 7 — Produce top_picks.md

Write `$RUN_DIR/top_picks.md`:

```markdown
# Amazon 综合选品推荐 ({date})

## 探索范围
本次扫描覆盖了 N 个大类目，共分析 N 个子类目（其中 N 个为新覆盖）。
累计已覆盖子类目：N 个（见 results/coverage.json）。

## 市场环境小结
[2–3 sentences on market conditions]

## 关键词信号
[2–3 sentences on trending demand signals]

## Top 20 推荐单品

| 排名 | ASIN | 品名 | 类目 | 月销量 | 估算成本/占比 | 毛利率 | Reviews | 推荐理由 |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [ASIN](https://www.amazon.com/dp/ASIN) | ... | ... | ... | ... | ... | ... | 一句话 |

## 各产品详细分析

### 1. [ASIN] 产品名
**选入理由**：[结合市场评级、关键词匹配、竞争格局]
**机会点**：[差异化方向、定价空间]
**风险点**：[需要验证的假设]
**建议下一步**：[去1688搜什么关键词、需要核查的具体数据点]

## 下次优先探索
[列出 coverage.json 中尚未覆盖的绿色类目（如果有），以及建议的下次运行参数]
```

---

## Scoring Guidance

| Dimension | Weight | Good | Caution |
|---|---|---|---|
| Reviews count | High | < 100 | > 500 |
| Sales growth | High | > 10% | negative |
| COGS ratio | Medium | < 25% | > 40% |
| Profit margin | Medium | > 65% | < 55% |
| Sellers count | Medium | 1 | > 2 |
| Listing age (months) | Low | 3–18 | > 36 |
| Keyword match | Medium | 2+ modes | 0 |

Do not average mechanically. A product with 50 reviews, 40% growth, 70% margin beats one with 20 reviews, flat growth, 55% margin.

## Output Principles

- Reference actual ASINs, actual metrics, actual category names
- If a product made the top 20 because competition was thin, say so
- Every product entry must have a concrete next step
- If fewer than 20 strong candidates exist, rank what's there and note more runs needed
- Always end with "下次优先探索" section so the user knows where to go next
