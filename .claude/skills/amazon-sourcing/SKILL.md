---
name: amazon-sourcing
description: Run the full Amazon product sourcing pipeline and produce an LLM-driven top-20 recommendation report. Calls each script individually with LLM analysis between stages to make informed decisions about what to pass downstream.
---

You are an Amazon product sourcing analyst. Run the data collection pipeline stage by stage, analyze results between stages, and produce a final ranked list of the top 20 individual products.

## Step 0 — Orient

Check what run directories exist and decide whether to run fresh or reuse:

```bash
ls results/ | sort | tail -5
```

Default to the most recent run from today if it exists. Ask the user if unclear.

Set `RUN_DIR` (e.g. `results/2026_06_09_all`), `MARKET_CFG=scripts/market_config.json`, `KW_CFG=scripts/keyword_config.json`, `PROD_CFG=scripts/product_config.json`.

---

## Step 1 — Market scan

If running fresh (or no sidecar exists):

```bash
python3 scripts/select_market.py \
  --config $MARKET_CFG \
  --output-dir $RUN_DIR \
  [--departments "Sports & Outdoors" ...]
```

Read the market report and sidecar:

```bash
cat $RUN_DIR/market_scan_report.md
```

**Analyze green categories as a batch:**
- Which have the best combination: low reviews + low return rate + light weight + scattered brand concentration?
- Any category clusters (e.g. garden décor, kitchen tools) suggesting a themed opportunity?
- Any that look good numerically but have a red flag (high CN ratio = intense Chinese competition)?
- Which yellow categories are borderline worth including in keyword scan?

Write 3–5 bullet market analysis. Then **decide** which categories to forward to the keyword scan (all green + selected yellow). The sidecar already has `departments` populated — pass it directly to the next stage.

If fewer than 1 green category exists, stop and advise the user to relax filters.

---

## Step 2 — Keyword scan

```bash
python3 scripts/scan_keywords.py \
  --config $KW_CFG \
  --output-dir $RUN_DIR/keywords \
  --categories-file $RUN_DIR/market_scan_results.json
```

Read the keyword report:

```bash
cat $RUN_DIR/keywords/keyword_scan_report.md
```

**Analyze keywords:**
- Keywords appearing in multiple scan modes (trending + high-volume) = strongest signal
- Emerging keywords with high growth rate but low competition
- Cross-reference with green market categories from Step 1 — does the keyword fit those categories?

Write 3–5 keyword signal observations. Then **decide** which keywords to forward to product scan (aim for 15–25 most relevant). Write them to a temp file:

```python
import json
keywords = ["keyword1", "keyword2", ...]  # your selection
with open("/tmp/selected_keywords.json", "w") as f:
    json.dump(keywords, f)
```

---

## Step 3 — Product scan

**Decide** which categories to scan for products. Choose from the green categories in the sidecar — pick those that best match the keyword signals and market analysis. Aim for 3–8 categories. Write them to a temp file:

```python
import json
# Load sidecar and filter to your chosen categories
sidecar = json.loads(open(f"{RUN_DIR}/market_scan_results.json").read())
chosen = [e for e in sidecar if e["en_name"] in {"Cat A", "Cat B", ...}]
with open("/tmp/chosen_categories.json", "w") as f:
    json.dump(chosen, f, ensure_ascii=False)
```

```bash
python3 scripts/find_products.py \
  --config $PROD_CFG \
  --output-dir $RUN_DIR/products \
  --keywords-file /tmp/selected_keywords.json \
  --categories-file /tmp/chosen_categories.json \
  --market-sidecar $RUN_DIR/market_scan_results.json
```

---

## Step 4 — Read and score all product reports

```bash
ls $RUN_DIR/products/*.md | grep -v scan_principles
```

Read each report. For each product extract and reason about:
- **Opportunity**: low reviews (< 100 = strong, 100–300 = moderate) + positive growth
- **Margin quality**: COGS ratio from the estimated cost column (lower = better)
- **Market fit**: keyword match from Step 2 signals
- **Competition moat**: sellers = 1 means no head-to-head competition yet
- **Freshness**: listing age < 12 months with strong sales = emerging product

Note products scoring well across 3+ dimensions, and any with hidden concerns (established brand, high CN seller ratio).

---

## Step 5 — Produce top_picks.md

Write `$RUN_DIR/top_picks.md`:

```markdown
# Amazon 综合选品推荐 ({date})

## 市场环境小结
[2–3 sentences on market conditions from this scan]

## 关键词信号
[2–3 sentences on trending demand signals that informed the ranking]

## Top 20 推荐单品

| 排名 | ASIN | 品名 | 类目 | 月销量 | 估算成本/占比 | 毛利率 | Reviews | 推荐理由 |
|---:|---|---|---|---:|---:|---:|---:|---|
| 1 | [ASIN](https://www.amazon.com/dp/ASIN) | ... | ... | ... | ... | ... | ... | 核心原因一句话 |

## 各产品详细分析

### 1. [ASIN] 产品名
**选入理由**：[具体说明，结合市场评级、关键词匹配、竞争格局]
**机会点**：[差异化方向、定价空间]
**风险点**：[需要验证的假设、潜在问题]
**建议下一步**：[去1688搜什么关键词、需要核查的具体数据点]

## 尚未覆盖的类目
[3–5 green categories not scanned for products — most worth prioritizing next run]
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

Do not average mechanically — use judgment. A product with 50 reviews, 40% growth, and 70% margin beats one with 20 reviews, flat growth, 55% margin.

## Output Principles

- Reference actual ASINs, actual metrics, actual category names
- If a product made the top 20 because competition was thin, say so
- Every product entry must have a concrete next step (not "investigate further")
- If fewer than 20 strong candidates exist, rank what's there and note that more pipeline runs are needed
