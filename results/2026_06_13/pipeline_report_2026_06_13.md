# 亚马逊选品完整流水线报告 (2026-06-13)

> 本文件汇总市场扫描、全部候选类目商品扫描和动态商品 ASIN 关键词反查结果。
> 各阶段独立报告仍保留用于审计。

---

<!-- source: market_scan_report.md -->
# 亚马逊选市场扫描与评估报告 (2026-06-13)

> [!IMPORTANT]
> 本报告基于 `unified pipeline config` 中设定的过滤与风控规则进行生成。今日共分析了 **30** 个符合基本条件的子类目，其中最终筛选出 **9** 个适合新手的 🟢 绿色推荐赛道。
> **抓取完整性**：扫描 **1** 页；页面总数提示：**125**；停止原因：免费套餐仅展示 30 个，页面提示共有 125 个类目；免费套餐截断风险：**可能存在**。
> **数量审计**：当前候选类目有 16 个，超过目标上限 15。建议提高基础过滤门槛或收紧黄色/绿色风控规则，而不是截断为固定 Top-K。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **9** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **7** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **14** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Swing Trainers** | 室内练习器 | $36.27 | 447 | 0.71 lbs | 4.37% | 57.8% | 69.0% |
| 2 | **Lighting Products** | 水底灯 | $49.26 | 480 | 1.76 lbs | 6.75% | 54.0% | 76.0% |
| 3 | **Nozzles** | 喷嘴 | $26.21 | 488 | 0.42 lbs | 2.63% | 54.8% | 73.0% |
| 4 | **Cardboard Cutouts** | 硬板纸模型 | $24.51 | 295 | 1.29 lbs | 4.59% | 61.5% | 61.0% |
| 5 | **Multi-Item Party Favor Packs** | 多项目派对礼包 | $20.12 | 161 | 1.04 lbs | 4.75% | 34.5% | 91.0% |
| 6 | **Electrical System Tools** | 电气系统工具 | $31.80 | 495 | 1.01 lbs | 2.38% | 44.0% | 81.0% |
| 7 | **Brake System Bleeding Tools** | 刹车排气 | $28.04 | 469 | 1.58 lbs | 4.69% | 50.1% | 83.0% |
| 8 | **Trophies** | 奖杯 | $25.32 | 297 | 1.01 lbs | 2.59% | 48.8% | 48.0% |
| 9 | **Grinding Discs** | 磨片 | $24.71 | 365 | 1.92 lbs | 2.13% | 47.2% | 80.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Compressed Air Dusters** | 压缩除尘罐 | $35.18 | 351 | 0.86 lbs | 3.16% | 谨慎认证类目路径 |
| 2 | **Wind Spinners** | Wind Spinners | $31.29 | 468 | 2.35 lbs | 3.09% | 重量偏重 (>2.0 lbs) |
| 3 | **Paddleboard Accessories** | 冲浪板配件 | $52.63 | 326 | 2.37 lbs | 4.17% | 重量偏重 (>2.0 lbs) |
| 4 | **Batteries & Battery Chargers** | 电池和电池 | $25.35 | 469 | 0.96 lbs | 9.83% | 退货率偏高 (>8.0%), 带电/合规资质敏感关键字 |
| 5 | **Decorative Trays** | 装饰性托盘 | $22.59 | 466 | 1.44 lbs | 9.52% | 退货率偏高 (>8.0%) |
| 6 | **Game Mats & Boards** | 游戏垫和游戏板 | $29.68 | 308 | 2.47 lbs | 7.5% | 重量偏重 (>2.0 lbs), 谨慎认证类目路径 |
| 7 | **Boats** | 船 | $56.64 | 338 | 1.45 lbs | 6.03% | 谨慎认证类目路径 |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Rash Guard Sets** | Rash Guard Sets | $21.07 | 高风险类目路径过滤 |
| 2 | **Sets** | 套 | $24.21 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 3 | **Skirt Sets** | 裙装套装 | $36.05 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 4 | **Rash Guard Sets** | 皮疹防护套装 | $22.62 | 高风险类目路径过滤 |
| 5 | **Button-Down Shirts** | 扣角领衬衫 | $20.02 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 6 | **Active Pants** | 运动裤 | $32.34 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 7 | **Glasses** | 眼镜 | $54.83 | 退货率过高 (>10.0%) |
| 8 | **Pant Sets** | 长裤套装 | $22.81 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 9 | **Wall Molding & Trim** | 墙压条和镶边 | $21.73 | 退货率过高 (>10.0%) |
| 10 | **Candlestick Holders** | 烛台座 | $23.68 | 退货率过高 (>10.0%) |
| 11 | **Spotlights** | 聚光灯 | $27.69 | 退货率过高 (>10.0%) |
| 12 | **Livestock Health Supplies** | 牲畜健康用品 | $31.72 | 排除类关键字过滤 |
| 13 | **Cup Carriers** | 外卖杯托盘 | $22.45 | 重量超标 (>2.5 lbs) |
| 14 | **Clutches** | 手拿包 | $32.66 | 退货率过高 (>10.0%), 高风险类目路径过滤 |

## 三、 候选类目详细数据指标画像 (供大模型分析使用)

以下为入选的绿色与黄色子类目的完整数据指标。您可以将这些数据输入大模型（如 Gemini、Claude），让其结合具体品类特性进行深入的入选原因、产品特征及商业机会评估。

### 🟢 绿色类目详情列表

#### 🏆 🟢-1. Swing Trainers (室内练习器)

- **完整市场路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.27`
  *   **平均 Reviews (Avg Reviews)**：`447 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`4.37%`
  *   **平均毛利率 (Profit Margin)**：`58.18%`
  *   **品牌集中度 (Brand Concentration)**：`57.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 高尔夫球场 › 用品 训练 › 室内练习器`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`25`
  *   **新品平均价格**：`$ 17.99`
  *   **新品平均星级**：`3.6`
  *   **新品月均销量**：`1,039`
  *   **新品月均销售额**：`$14,808`
  *   **平均重量**：`0.71 pounds (320 g)`
  *   **平均体积**：`145.42 in³ (2,383 cm³)`
  *   **平均毛利率**：`58.18%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-2. Lighting Products (水底灯)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$49.26`
  *   **平均 Reviews (Avg Reviews)**：`480 个`
  *   **物理重量 (Weight)**：`1.76 lbs`
  *   **平均退货率 (Return Rate)**：`6.75%`
  *   **平均毛利率 (Profit Margin)**：`66.87%`
  *   **品牌集中度 (Brand Concentration)**：`54.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 水底灯`
  *   **A+数量占比**：`93%`
  *   **新品平均评分数**：`85`
  *   **新品平均价格**：`$ 51.09`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`1,296`
  *   **新品月均销售额**：`$76,140`
  *   **平均重量**：`1.76 pounds (798 g)`
  *   **平均体积**：`640.46 in³ (10,495 cm³)`
  *   **平均毛利率**：`66.87%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-3. Nozzles (喷嘴)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.21`
  *   **平均 Reviews (Avg Reviews)**：`488 个`
  *   **物理重量 (Weight)**：`0.42 lbs`
  *   **平均退货率 (Return Rate)**：`2.63%`
  *   **平均毛利率 (Profit Margin)**：`63.39%`
  *   **品牌集中度 (Brand Concentration)**：`54.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 电动工具 › 替换件和配件 › 高压清洗机配件 › 喷嘴`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`53`
  *   **新品平均价格**：`$ 33.15`
  *   **新品平均星级**：`2.6`
  *   **新品月均销量**：`815`
  *   **新品月均销售额**：`$22,501`
  *   **平均重量**：`0.42 pounds (191 g)`
  *   **平均体积**：`66.31 in³ (1,087 cm³)`
  *   **平均毛利率**：`63.39%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`13.5‰`

---

#### 🏆 🟢-4. Cardboard Cutouts (硬板纸模型)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.51`
  *   **平均 Reviews (Avg Reviews)**：`295 个`
  *   **物理重量 (Weight)**：`1.29 lbs`
  *   **平均退货率 (Return Rate)**：`4.59%`
  *   **平均毛利率 (Profit Margin)**：`60.41%`
  *   **品牌集中度 (Brand Concentration)**：`61.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`61.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 硬板纸模型`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`27`
  *   **新品平均价格**：`$ 23.7`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`483`
  *   **新品月均销售额**：`$11,697`
  *   **平均重量**：`1.29 pounds (587 g)`
  *   **平均体积**：`334.67 in³ (5,484 cm³)`
  *   **平均毛利率**：`60.41%`
  *   **卖家所属地**：`中国|61.0%`
  *   **搜索购买比**：`6.4‰`

---

#### 🏆 🟢-5. Multi-Item Party Favor Packs (多项目派对礼包)

- **完整市场路径**：`Home & Kitchen › Event & Party Supplies › Favors › Multi-Item Party Favor Packs  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.12`
  *   **平均 Reviews (Avg Reviews)**：`161 个`
  *   **物理重量 (Weight)**：`1.04 lbs`
  *   **平均退货率 (Return Rate)**：`4.75%`
  *   **平均毛利率 (Profit Margin)**：`57.15%`
  *   **品牌集中度 (Brand Concentration)**：`34.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`91.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Event & Party Supplies › Favors › Multi-Item Party Favor Packs  市场分析`
  *   **市场路径(中文)**：`家居用品 › 活动 › 赠品 › 多项目派对礼包`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`58`
  *   **新品平均价格**：`$ 20.69`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`625`
  *   **新品月均销售额**：`$12,320`
  *   **平均重量**：`1.04 pounds (474 g)`
  *   **平均体积**：`95.00 in³ (1,557 cm³)`
  *   **平均毛利率**：`57.15%`
  *   **卖家所属地**：`中国|91.0%`
  *   **搜索购买比**：`7.2‰`

---

#### 🏆 🟢-6. Electrical System Tools (电气系统工具)

- **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.80`
  *   **平均 Reviews (Avg Reviews)**：`495 个`
  *   **物理重量 (Weight)**：`1.01 lbs`
  *   **平均退货率 (Return Rate)**：`2.38%`
  *   **平均毛利率 (Profit Margin)**：`55.71%`
  *   **品牌集中度 (Brand Concentration)**：`44.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 电气系统工具`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`49`
  *   **新品平均价格**：`$ 18.38`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`416`
  *   **新品月均销售额**：`$8,219`
  *   **平均重量**：`1.01 pounds (458 g)`
  *   **平均体积**：`317.86 in³ (5,209 cm³)`
  *   **平均毛利率**：`55.71%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟢-7. Brake System Bleeding Tools (刹车排气)

- **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.04`
  *   **平均 Reviews (Avg Reviews)**：`469 个`
  *   **物理重量 (Weight)**：`1.58 lbs`
  *   **平均退货率 (Return Rate)**：`4.69%`
  *   **平均毛利率 (Profit Margin)**：`55.51%`
  *   **品牌集中度 (Brand Concentration)**：`50.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 制动工具 › 刹车排气`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`32`
  *   **新品平均价格**：`$ 17.61`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`406`
  *   **新品月均销售额**：`$7,863`
  *   **平均重量**：`1.58 pounds (715 g)`
  *   **平均体积**：`309.45 in³ (5,071 cm³)`
  *   **平均毛利率**：`55.51%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`8.9‰`

---

#### 🏆 🟢-8. Trophies (奖杯)

- **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.32`
  *   **平均 Reviews (Avg Reviews)**：`297 个`
  *   **物理重量 (Weight)**：`1.01 lbs`
  *   **平均退货率 (Return Rate)**：`2.59%`
  *   **平均毛利率 (Profit Margin)**：`62.93%`
  *   **品牌集中度 (Brand Concentration)**：`48.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 辅料 › 、奖牌 › 奖杯`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`35`
  *   **新品平均价格**：`$ 30.63`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`503`
  *   **新品月均销售额**：`$19,484`
  *   **平均重量**：`1.01 pounds (458 g)`
  *   **平均体积**：`179.90 in³ (2,948 cm³)`
  *   **平均毛利率**：`62.93%`
  *   **卖家所属地**：`中国|48.0%`
  *   **搜索购买比**：`6.5‰`

---

#### 🏆 🟢-9. Grinding Discs (磨片)

- **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.71`
  *   **平均 Reviews (Avg Reviews)**：`365 个`
  *   **物理重量 (Weight)**：`1.92 lbs`
  *   **平均退货率 (Return Rate)**：`2.13%`
  *   **平均毛利率 (Profit Margin)**：`61.53%`
  *   **品牌集中度 (Brand Concentration)**：`47.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs  市场分析`
  *   **市场路径(中文)**：`工业类 › 磨削加工 › 研磨砂轮 › 磨片`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`21`
  *   **新品平均价格**：`$ 21.56`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`391`
  *   **新品月均销售额**：`$7,714`
  *   **平均重量**：`1.92 pounds (870 g)`
  *   **平均体积**：`13.21 in³ (216 cm³)`
  *   **平均毛利率**：`61.53%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`15.0‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Compressed Air Dusters (压缩除尘罐)

- **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.18`
  *   **平均 Reviews (Avg Reviews)**：`351 个`
  *   **物理重量 (Weight)**：`0.86 lbs`
  *   **平均退货率 (Return Rate)**：`3.16%`
  *   **平均毛利率 (Profit Margin)**：`73.82%`
  *   **品牌集中度 (Brand Concentration)**：`59.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
  *   **市场路径(中文)**：`电子产品 › 计算机 › 电脑配件 › 清洁 › 压缩除尘罐`
  *   **A+数量占比**：`92%`
  *   **新品平均评分数**：`120`
  *   **新品平均价格**：`$ 34.14`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`536`
  *   **新品月均销售额**：`$17,904`
  *   **平均重量**：`0.86 pounds (391 g)`
  *   **平均体积**：`43.61 in³ (715 cm³)`
  *   **平均毛利率**：`73.82%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`13.0‰`

---

#### 🏆 🟡-2. Wind Spinners (Wind Spinners)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.29`
  *   **平均 Reviews (Avg Reviews)**：`468 个`
  *   **物理重量 (Weight)**：`2.35 lbs`
  *   **平均退货率 (Return Rate)**：`3.09%`
  *   **平均毛利率 (Profit Margin)**：`59.69%`
  *   **品牌集中度 (Brand Concentration)**：`54.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`86.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`53`
  *   **新品平均价格**：`$ 22.04`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`776`
  *   **新品月均销售额**：`$14,498`
  *   **平均重量**：`2.35 pounds (1,068 g)`
  *   **平均体积**：`269.80 in³ (4,421 cm³)`
  *   **平均毛利率**：`59.69%`
  *   **卖家所属地**：`中国|86.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟡-3. Paddleboard Accessories (冲浪板配件)

- **完整市场路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$52.63`
  *   **平均 Reviews (Avg Reviews)**：`326 个`
  *   **物理重量 (Weight)**：`2.37 lbs`
  *   **平均退货率 (Return Rate)**：`4.17%`
  *   **平均毛利率 (Profit Margin)**：`64.35%`
  *   **品牌集中度 (Brand Concentration)**：`42.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 划船和你 › 立式单肩肩背 › 冲浪板配件`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`34`
  *   **新品平均价格**：`$ 74.69`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`642`
  *   **新品月均销售额**：`$50,084`
  *   **平均重量**：`2.37 pounds (1,077 g)`
  *   **平均体积**：`425.27 in³ (6,969 cm³)`
  *   **平均毛利率**：`64.35%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟡-4. Batteries & Battery Chargers (电池和电池)

- **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.35`
  *   **平均 Reviews (Avg Reviews)**：`469 个`
  *   **物理重量 (Weight)**：`0.96 lbs`
  *   **平均退货率 (Return Rate)**：`9.83%`
  *   **平均毛利率 (Profit Margin)**：`62.74%`
  *   **品牌集中度 (Brand Concentration)**：`61.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`84.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 溜冰鞋、滑板和滑板车 › 自行车车 › 自行车车配件 › 电池和电池`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`74`
  *   **新品平均价格**：`$ 34.93`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`587`
  *   **新品月均销售额**：`$17,697`
  *   **平均重量**：`0.96 pounds (435 g)`
  *   **平均体积**：`56.28 in³ (922 cm³)`
  *   **平均毛利率**：`62.74%`
  *   **卖家所属地**：`中国|84.0%`
  *   **搜索购买比**：`9.9‰`

---

#### 🏆 🟡-5. Decorative Trays (装饰性托盘)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.59`
  *   **平均 Reviews (Avg Reviews)**：`466 个`
  *   **物理重量 (Weight)**：`1.44 lbs`
  *   **平均退货率 (Return Rate)**：`9.52%`
  *   **平均毛利率 (Profit Margin)**：`56.91%`
  *   **品牌集中度 (Brand Concentration)**：`42.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰性托盘`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`125`
  *   **新品平均价格**：`$ 21.22`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`675`
  *   **新品月均销售额**：`$12,628`
  *   **平均重量**：`1.44 pounds (655 g)`
  *   **平均体积**：`233.47 in³ (3,826 cm³)`
  *   **平均毛利率**：`56.91%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟡-6. Game Mats & Boards (游戏垫和游戏板)

- **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.68`
  *   **平均 Reviews (Avg Reviews)**：`308 个`
  *   **物理重量 (Weight)**：`2.47 lbs`
  *   **平均退货率 (Return Rate)**：`7.5%`
  *   **平均毛利率 (Profit Margin)**：`58.53%`
  *   **品牌集中度 (Brand Concentration)**：`40.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 游戏配件 › 游戏垫和游戏板`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 33.43`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`331`
  *   **新品月均销售额**：`$10,904`
  *   **平均重量**：`2.47 pounds (1,121 g)`
  *   **平均体积**：`301.69 in³ (4,944 cm³)`
  *   **平均毛利率**：`58.53%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`3.8‰`

---

#### 🏆 🟡-7. Boats (船)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$56.64`
  *   **平均 Reviews (Avg Reviews)**：`338 个`
  *   **物理重量 (Weight)**：`1.45 lbs`
  *   **平均退货率 (Return Rate)**：`6.03%`
  *   **平均毛利率 (Profit Margin)**：`69.15%`
  *   **品牌集中度 (Brand Concentration)**：`61.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 船`
  *   **A+数量占比**：`98%`
  *   **新品平均评分数**：`40`
  *   **新品平均价格**：`$ 54.62`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`316`
  *   **新品月均销售额**：`$15,845`
  *   **平均重量**：`1.45 pounds (657 g)`
  *   **平均体积**：`317.47 in³ (5,202 cm³)`
  *   **平均毛利率**：`69.15%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`2.9‰`

---

---

<!-- source: products/batteries_battery_chargers.md -->
# Batteries & Battery Chargers 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers`
> 共抓取 **14** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **14** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $25.35　均Reviews 469（中等）　重量 0.96lbs（轻）　退货率 9.83%（高）　品牌集中度 61.8%（中等）　中国卖家 84.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DMN32R1B](https://www.amazon.com/dp/B0DMN32R1B) |  | 42V Compact Electric Scooter Hoverboard Charger for Hover-1 Gotra… | 983 / 18.62% | $23,582 | $23.99 | $3.59 (15%) | 142 / 19 | 4.2 | $4.09 / 68% | 1 | 14 | 1 | 0.46 pounds | 2025-02-15 1年 3个月 |
| 2 | [B0FXM8XJ7F](https://www.amazon.com/dp/B0FXM8XJ7F) |  | 54.6V 2A Ebike Electric Scooter Charger for 48V Lithium Battery | 591 / 150% | $13,073 | $22.12 | $3.41 (15%) | 58 / 14 | 4.4 | $5.22 / 61% | 1 | 24 | 1 | 1.12 pounds | 2026-01-24 4个月 |
| 3 | [B0G3PRSR6K](https://www.amazon.com/dp/B0G3PRSR6K) |  | ETL Certified 54.6V 1.5A Electric Bike & Scooter Charger | 443 / 100.64% | $12,400 | $27.99 | $4.30 (15%) | 23 / 15 | 4.5 | $5.22 / 66% | 1 | 28 | 1 | 1.06 pounds | 2026-03-23 2个月 |
| 4 | [B0G3PR5VQ2](https://www.amazon.com/dp/B0G3PR5VQ2) |  | ETL Certified 42V 2A Electric Scooter Charger | 452 / 55.87% | $12,199 | $26.99 | $3.96 (15%) | 13 / 5 | 4.9 | $5.22 / 66% | 1 | 18 | 1 | 1.08 pounds | 2026-01-21 4个月 |
| 5 | [B0CBFRFV5W](https://www.amazon.com/dp/B0CBFRFV5W) |  | 24V(Max 29.4V) 2A 3-Pin XLR Charger for Electric Scooter Go-Go El… | 283 / 78.99% | $8,456 | $29.88 | $4.58 (15%) | 111 / 6 | 4.4 | $4.68 / 69% | 1 | 75 | 1 | 0.9 pounds | 2023-08-15 2年 9个月 |
| 6 | [B0FQMYN3TJ](https://www.amazon.com/dp/B0FQMYN3TJ) |  | WUKUR 54.6V 2A Electric Scooter Charger 5 Connectors for 48V Lith… | 335 / 9.72% | $7,032 | $20.99 | $3.22 (15%) | 43 / 12 | 4.2 | $4.76 / 62% | 1 | 61 | 1 | 0.93 pounds | 2025-10-28 7个月 |
| 7 | [B0G58V9RGN](https://www.amazon.com/dp/B0G58V9RGN) |  | 54.6V 3A Fast Battery Charger for Electric Scooter | 152 / 65.91% | $6,686 | $43.99 | $6.56 (15%) | 15 / 2 | 4.9 | $5.76 / 72% | 1 | 99 | 1 | 1.74 pounds | 2025-12-06 6个月 |
| 8 | [B0GMTLLL5B](https://www.amazon.com/dp/B0GMTLLL5B) |  | Electric Scooter Charger 42V 2A | 217 / 44.74% | $6,506 | $29.98 | $4.58 (15%) | 6 / 5 | 4.7 | $5.61 / 66% | 2 | 98 | 1 | 1.32 pounds | 2026-03-11 3个月 |
| 9 | [B0F1SW6TQT](https://www.amazon.com/dp/B0F1SW6TQT) |  | VHBW 42V 2A Electric Scooter Charger Compatible with iScooter i9… | 205 / 73.64% | $5,123 | $24.99 | $3.65 (15%) | 40 / 10 | 4.4 | $4.35 / 68% | 1 | 94 | 1 | 0.68 pounds | 2025-04-21 1年 1个月 |
| 10 | [B0F4MCNJ99](https://www.amazon.com/dp/B0F4MCNJ99) |  | 24V(Max 29.4V) 5A Lithium Battery Charger for 24V Lithium Packs 3… | 122 / 101.61% | $4,635 | $37.99 | $5.79 (15%) | 30 / - | 4.4 | $5.61 / 70% | 3 | 255 | 2 | 1.43 pounds | 2025-06-06 1年 |
| 11 | [B0F5Q3GHWG](https://www.amazon.com/dp/B0F5Q3GHWG) |  | 42V for Hiboy Electric Scooter Charger Compatible with Hiboy S2 P… | **** / **** | **** | $20.99 | - | 53 / 3 | 4.6 | **** /  | 1 | 82 | 1 | 0.71 pounds | 2025-06-21 11个月 |
| 12 | [B0DQTXGVRN](https://www.amazon.com/dp/B0DQTXGVRN) |  | 54.6V 2A Lithium Battery Charger for 48V 13s Li-ion Batterie,Powe… | **** / **** | **** | $28.99 | - | 57 / 1 | 4.2 | **** /  | 5 | 124 | 1 | 0.93 pounds | 2025-03-11 1年 3个月 |
| 13 | [B0DM23P9QV](https://www.amazon.com/dp/B0DM23P9QV) |  | Fancy Buying 4 Prong Scooter Charger 63V 1.1A for Segway Ninebot… | **** / **** | **** | $26.99 | - | 8 / 4 | 4.2 | **** /  | 1 | 249 | 1 | 0.73 pounds | 2025-02-10 1年 4个月 |
| 14 | [B0CZQ1X9L3](https://www.amazon.com/dp/B0CZQ1X9L3) |  | 24V2A MX350 MX400 Charger for Razor E100 E125 E150 E175 E200 E200… | **** / **** | **** | $23.99 | - | 33 / 5 | 4.3 | **** /  | 1 | 135 | 1 | 0.49 pounds | 2024-04-25 2年 1个月 |

## 二、完整商品标题

**1. [B0DMN32R1B](https://www.amazon.com/dp/B0DMN32R1B)** 42V Compact Electric Scooter Hoverboard Charger for Hover-1 Gotrax Jetson & More 36V Lithium Battery, UL Certified Safe & Powerful & Small with 2 Common Connectors

**2. [B0FXM8XJ7F](https://www.amazon.com/dp/B0FXM8XJ7F)** 54.6V 2A Ebike Electric Scooter Charger for 48V Lithium Battery, 5 Adapter Plugs Fast Replacement Charger Compatible with Rad Power Bikes, Velotric, Heybike, Juiced, Ecotric - UL Listed

**3. [B0G3PRSR6K](https://www.amazon.com/dp/B0G3PRSR6K)** ETL Certified 54.6V 1.5A Electric Bike & Scooter Charger, 7-in-1 Universal Fast Charger Replacement for 48V 13S Lithium Battery, Compatible with Razor Gotrax Xiaomi Jetson Ninebot Hoverboard & E-Bike

**4. [B0G3PR5VQ2](https://www.amazon.com/dp/B0G3PR5VQ2)** ETL Certified 42V 2A Electric Scooter Charger, 7-in-1 Universal Charger Replacement for 36V 10S Lithium Battery, Compatible with Razor Gotrax Xiaomi Jetson Ninebot Hoverboard & E-Bike

**5. [B0CBFRFV5W](https://www.amazon.com/dp/B0CBFRFV5W)** 24V(Max 29.4V) 2A 3-Pin XLR Charger for Electric Scooter Go-Go Elite Traveller, Plus HD US, Ezip Mountain Trailz, Jazzy Power Chair,Shoprider,Schwinn S300 S350 S400 S500 S650,Pride Mobility

**6. [B0FQMYN3TJ](https://www.amazon.com/dp/B0FQMYN3TJ)** WUKUR 54.6V 2A Electric Scooter Charger 5 Connectors for 48V Lithium Batteries Compatible with Lectric XP 2.0/3.0, for Ecotric City/Beach, for Evercross H5/H7 Ebike

**7. [B0G58V9RGN](https://www.amazon.com/dp/B0G58V9RGN)** 54.6V 3A Fast Battery Charger for Electric Scooter, Hoverboard, E Scooter, Electric Ebike, Universal 7-in-1 Replacement for 48V Lithium Battery 100-240V Input,Compatible with Segway, Volpam, Jetson

**8. [B0GMTLLL5B](https://www.amazon.com/dp/B0GMTLLL5B)** Electric Scooter Charger 42V 2A, UL Listed Fast Charger for 36V Lithium Battery, with 7 Plugs – Home/Travel/Outdoor Use – Compatible with Razor, Jetson, Gotrax, Ninebot & Most 36V Scooters

**9. [B0F1SW6TQT](https://www.amazon.com/dp/B0F1SW6TQT)** VHBW 42V 2A Electric Scooter Charger Compatible with iScooter i9 Charger for i9 i8 i8L E9D E9 Pro E9T i9 i9Pro i9Plus 1S, Also Compatible with isinwheel S9 S9 Pro S9 Max Scooter

**10. [B0F4MCNJ99](https://www.amazon.com/dp/B0F4MCNJ99)** 24V(Max 29.4V) 5A Lithium Battery Charger for 24V Lithium Packs 3-Pin Male XLR Connector, HD Screen Display Real-time Charging Voltage, Built-in Cooling Fan

**11. [B0F5Q3GHWG](https://www.amazon.com/dp/B0F5Q3GHWG)** 42V for Hiboy Electric Scooter Charger Compatible with Hiboy S2 Pro, S2 Lite, S2, KS4, KS4 Pro, NEX, NEX3, NEX5, Max, Max3, Max V2 Electric Scooter Foldable e-Scooter Power Supply

**12. [B0DQTXGVRN](https://www.amazon.com/dp/B0DQTXGVRN)** 54.6V 2A Lithium Battery Charger for 48V 13s Li-ion Batterie,Power Adapter with HD Display for Real-Time Charging Voltage Built-in Fan for Rapid Cooling and Smart Power-Off Function

**13. [B0DM23P9QV](https://www.amazon.com/dp/B0DM23P9QV)** Fancy Buying 4 Prong Scooter Charger 63V 1.1A for Segway Ninebot S/S-MAX/Mini lite/Mini PRO, Compatible with Ninebot by Segway Go Kart Kit,Gokart PRO 54V(15S) Lithium Battery

**14. [B0CZQ1X9L3](https://www.amazon.com/dp/B0CZQ1X9L3)** 24V2A MX350 MX400 Charger for Razor E100 E125 E150 E175 E200 E200S E300 E300S E500 PR200 E225S E325S, Pocket Mod, Sports Mod, and Dirt Quad, Ground Force, Mini Chopper for W13112099014

## 三、尚未分析的候选类目（共 3 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 2 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 3 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 3 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0DMN32R1B`: 8,622 | 546 | 6% | 983 | 18.62% | $23,582 | 800+ | $19K+ | 1 | $23.99 | - | 142 | 19 | 4.2 | 1.93% | $4.09 | 68% | 2025-02-15 | 1年 3个月 | FBA | -
- `B0FXM8XJ7F`: 11,427 | 3,125 | 21% | 591 | 150% | $13,073 | 500+ | $10K+ | 1 | $22.12 | - | 58 | 14 | 4.4 | 2.37% | $5.22 | 61% | 2026-01-24 | 4个月 | FBA | -
- `B0G3PRSR6K`: 13,601 | 1,514 | 10% | 443 | 100.64% | $12,400 | 400+ | $11K+ | 1 | $27.99 | - | 23 | 15 | 4.5 | 3.39% | $5.22 | 66% | 2026-03-23 | 2个月 | FBA | -
- `B0G3PR5VQ2`: 11,505 | 3,000 | 21% | 452 | 55.87% | $12,199 | 300+ | $8K+ | 1 | $26.99 | - | 13 | 5 | 4.9 | 1.11% | $5.22 | 66% | 2026-01-21 | 4个月 | FBA | -
- `B0CBFRFV5W`: 33,817 | 1,099 | 3% | 283 | 78.99% | $8,456 | 200+ | $5K+ | 1 | $29.88 | - | 111 | 6 | 4.4 | 2.12% | $4.68 | 69% | 2023-08-15 | 2年 9个月 | FBA | -
- `B0FQMYN3TJ`: 27,130 | 1,946 | 7% | 335 | 9.72% | $7,032 | 200+ | $4K+ | 1 | $20.99 | - | 43 | 12 | 4.2 | 3.58% | $4.76 | 62% | 2025-10-28 | 7个月 | FBA | -
- `B0G58V9RGN`: 44,358 | 3,970 | 8% | 152 | 65.91% | $6,686 | 100+ | $4K+ | 1 | $43.99 | - | 15 | 2 | 4.9 | 1.32% | $5.76 | 72% | 2025-12-06 | 6个月 | FBA | -
- `B0GMTLLL5B`: 43,961 | 3,547 | 8% | 217 | 44.74% | $6,506 | 50+ | $1K+ | 2 | $29.98 | - | 6 | 5 | 4.7 | 2.3% | $5.61 | 66% | 2026-03-11 | 3个月 | FBA | -
- `B0F1SW6TQT`: 41,096 | 5,051 | 11% | 205 | 73.64% | $5,123 | 100+ | $2K+ | 1 | $24.99 | - | 40 | 10 | 4.4 | 4.88% | $4.35 | 68% | 2025-04-21 | 1年 1个月 | FBA | -
- `B0F4MCNJ99`: 108,225 | 0 | 0% | 122 | 101.61% | $4,635 | - | - | 3 | $37.99 | - | 30 | - | 4.4 | - | $5.61 | 70% | 2025-06-06 | 1年 | FBA | -
- `B0F5Q3GHWG`: 35,885 | 8,488 | 19% | **** | **** | **** | **** | 1 | $20.99 | - | 53 | 3 | 4.6 | 1.49% | **** | 2025-06-21 | 11个月 | FBA | -
- `B0DQTXGVRN`: 53,286 | 32,933 | 36% | **** | **** | **** | **** | 5 | $28.99 | - | 57 | 1 | 4.2 | 0.85% | **** | 2025-03-11 | 1年 3个月 | FBA | -
- `B0DM23P9QV`: 95,023 | 2,491 | 3% | **** | **** | **** | **** | 1 | $26.99 | - | 8 | 4 | 4.2 | 3.28% | **** | 2025-02-10 | 1年 4个月 | FBA | -
- `B0CZQ1X9L3`: 56,737 | 13,759 | 20% | **** | **** | **** | **** | 1 | $23.99 | - | 33 | 5 | 4.3 | 3.97% | **** | 2024-04-25 | 2年 1个月 | FBA | -

---

<!-- source: products/boats.md -->
# Boats 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats`
> 共抓取 **3** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **3** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $56.64　均Reviews 338（中等）　重量 1.45lbs（轻）　退货率 6.03%（中）　品牌集中度 61.7%（中等）　中国卖家 67.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0FC2VL633](https://www.amazon.com/dp/B0FC2VL633) |  | Remote Control Boat Crocodile Water Toy for Kids 3-5 | 421 / 23.15% | $12,626 | $29.99 | $4.63 (15%) | 90 / 14 | 4.1 | $5.87 / 65% | 4 | 26 | 1 | 0.84 pounds | 2025-07-09 11个月 |
| 2 | [B0CWXVCT2G](https://www.amazon.com/dp/B0CWXVCT2G) |  | Losbenco RC Boat | 154 / 52.43% | $6,158 | $39.99 | $6.19 (15%) | 83 / 5 | 4.2 | $7.41 / 66% | 1 | 77 | 1 | 1.48 pounds | 2024-04-18 2年 1个月 |
| 3 | [B0D8TB7V29](https://www.amazon.com/dp/B0D8TB7V29) |  | GearRoot Remote Control Dolphin Toys for Kids | 116 / 29.69% | $3,131 | $26.99 | $4.12 (15%) | 12 / - | 4.1 | $5.87 / 63% | 1 | 122 | 1 | 0.86 pounds | 2024-11-03 1年 7个月 |

## 二、完整商品标题

**1. [B0FC2VL633](https://www.amazon.com/dp/B0FC2VL633)** Remote Control Boat Crocodile Water Toy for Kids 3-5, 5-7, 10-12, RC Alligator for Boys 4-6, 6-8, Top Summer Swimming Pool/Lake Toys for Kids Ages 8-12 (Water Operation ONLY - Green)

**2. [B0CWXVCT2G](https://www.amazon.com/dp/B0CWXVCT2G)** Losbenco RC Boat, 1/72 RC Tugboat for Pools and Lakes, High-Speed Remote Control Boat with 40 Mins Play Time and Low Battery Reminder for Kids and Adults - RTR Version

**3. [B0D8TB7V29](https://www.amazon.com/dp/B0D8TB7V29)** GearRoot Remote Control Dolphin Toys for Kids, 2.4G High Simulation Oceanic RC Dolphins Fish Toys for Swimming Pool Bathroom, 2x600mAh RC Boat Water Toys Great for 6+ Year olds Boys Girls Kids, Gray

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0FC2VL633`: 17,382 | 1,659 | 9% | 421 | 23.15% | $12,626 | 300+ | $8K+ | 4 | $29.99 | - | 90 | 14 | 4.1 | 3.33% | $5.87 | 65% | 2025-07-09 | 11个月 | FBA | -
- `B0CWXVCT2G`: 48,617 | 24,954 | 34% | 154 | 52.43% | $6,158 | 50+ | $1K+ | 1 | $39.99 | - | 83 | 5 | 4.2 | 3.25% | $7.41 | 66% | 2024-04-18 | 2年 1个月 | FBA | -
- `B0D8TB7V29`: 51,139 | 19,365 | 27% | 116 | 29.69% | $3,131 | 50+ | $1K+ | 1 | $26.99 | - | 12 | - | 4.1 | - | $5.87 | 63% | 2024-11-03 | 1年 7个月 | FBA | -

---

<!-- source: products/brake_system_bleeding_tools.md -->
# Brake System Bleeding Tools 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $28.04　均Reviews 469（中等）　重量 1.58lbs（偏重）　退货率 4.69%（低）　品牌集中度 50.1%（中等）　中国卖家 83.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GGQH744M](https://www.amazon.com/dp/B0GGQH744M) |  | Brake Bleeder Kit - One-Way Check Valve | 806 / 20.66% | $18,449 | $22.89 | $3.43 (15%) | 52 / 17 | 4.7 | $4.35 / 66% | 1 | 18 | 1 | 0.29 pounds | 2026-01-14 4个月 |
| 2 | [B0F22SXPDT](https://www.amazon.com/dp/B0F22SXPDT) |  | BleedZone SRAM DB8 Brake Bleed Kit with Maxima Mineral Oil Includ… | 103 / 56.25% | $3,316 | $32.19 | $4.99 (15%) | 14 / 3 | 4.1 | $4.35 / 71% | 2 | 216 | 1 | 0.71 pounds | 2025-04-24 1年 1个月 |

## 二、完整商品标题

**1. [B0GGQH744M](https://www.amazon.com/dp/B0GGQH744M)** Brake Bleeder Kit - One-Way Check Valve, Magnet Mount, 16oz Catch Bottle, 16” Hose

**2. [B0F22SXPDT](https://www.amazon.com/dp/B0F22SXPDT)** BleedZone SRAM DB8 Brake Bleed Kit with Maxima Mineral Oil Included, 2x Pro PC Syringe & M4 Fittings, Hydraulic Bike Brake Bleeding Kit, MTB & Road Bicycle Service Tool for SRAM Mineral Oil Systems

## 三、尚未分析的候选类目（共 9 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 2 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 3 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 4 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 5 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 6 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 7 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 8 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 9 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 9 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0GGQH744M`: 8,583 | 145 | 2% | 806 | 20.66% | $18,449 | 700+ | $16K+ | 1 | $22.89 | - | 52 | 17 | 4.7 | 2.11% | $4.35 | 66% | 2026-01-14 | 4个月 | FBA | -
- `B0F22SXPDT`: 92,590 | 57,898 | 38% | 103 | 56.25% | $3,316 | 50+ | $1K+ | 2 | $32.19 | - | 14 | 3 | 4.1 | 2.91% | $4.35 | 71% | 2025-04-24 | 1年 1个月 | FBA | -

---

<!-- source: products/cardboard_cutouts.md -->
# Cardboard Cutouts 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts`
> 共抓取 **6** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **6** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $24.51　均Reviews 295（低竞争）　重量 1.29lbs（轻）　退货率 4.59%（低）　品牌集中度 61.5%（中等）　中国卖家 61.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B09PKHLH7W](https://www.amazon.com/dp/B09PKHLH7W) |  | Cardboard People Princess Collage Life Size Cardboard Cutout Stan… | 449 / 7.42% | $21,534 | $47.96 | $7.22 (15%) | 87 / - | 4.5 | $16.76 / 50% | 1 | 63 | 2 | 2.45 pounds | 2022-01-11 4年 5个月 |
| 2 | [B0GHSNNZPZ](https://www.amazon.com/dp/B0GHSNNZPZ) |  | 131PCS Classic Winnie Baby Shower Birthday Decorations Large Winn… | 402 / 37.36% | $10,850 | $26.99 | $4.13 (15%) | 13 / 4 | 4.6 | $6.13 / 62% | 1 | 21 | 1 | 1.92 pounds | 2026-03-08 3个月 |
| 3 | [B0G7YT3F1H](https://www.amazon.com/dp/B0G7YT3F1H) |  | Giraffe Cardboard Cutout Life-Size Animal Cutout Realistic Safari… | 290 / 40.56% | $9,567 | $32.99 | $5.09 (15%) | 2 / - | 5.0 | $6.13 / 66% | 1 | 528 | 1 | 1.37 pounds | 2025-12-20 5个月 |
| 4 | [B0GJL3W2D6](https://www.amazon.com/dp/B0GJL3W2D6) |  | 131PCS Pink Winnie Baby Shower Birthday Decorations for Girl Larg… | 281 / 159.57% | $7,584 | $26.99 | $4.17 (15%) | 11 / 2 | 4.4 | $6.90 / 59% | 1 | 72 | 1 | 1.74 pounds | 2026-03-25 2个月 |
| 5 | [B0FWC8ZZ48](https://www.amazon.com/dp/B0FWC8ZZ48) |  | 4 Ft Happy Birthday Jesus Cardboard Cutout Stand Up Life Size Lar… | 220 / 103.49% | $6,598 | $29.99 | $4.48 (15%) | 14 / 2 | 4.8 | $6.02 / 65% | 4 | 63 | 1 | 1.41 pounds | 2025-10-16 7个月 |
| 6 | [B0FG2C7QD8](https://www.amazon.com/dp/B0FG2C7QD8) |  | Yookeer 4ft Lion Cardboard Cutout Stand up Life Size Safari-Theme… | 148 / 5.97% | $4,587 | $30.99 | $4.88 (16%) | 21 / 2 | 4.2 | $6.90 / 62% | 4 | 141 | 2 | 1.81 pounds | 2025-07-20 10个月 |

## 二、完整商品标题

**1. [B09PKHLH7W](https://www.amazon.com/dp/B09PKHLH7W)** Cardboard People Princess Collage Life Size Cardboard Cutout Standup - Disney

**2. [B0GHSNNZPZ](https://www.amazon.com/dp/B0GHSNNZPZ)** 131PCS Classic Winnie Baby Shower Birthday Decorations Large Winnie Coroplast Cutout with Stand, Neutral Balloons Arch& Bee Stickers for Gender Reveal, First Birthday, Photo Props & Pooh Party

**3. [B0G7YT3F1H](https://www.amazon.com/dp/B0G7YT3F1H)** Giraffe Cardboard Cutout Life-Size Animal Cutout Realistic Safari Jungle Photo Booth Prop Decor for Parties, Zoo-Themed Events, Classrooms, Birthday Decoration Supplies 28.39 x 59.06 Inches

**4. [B0GJL3W2D6](https://www.amazon.com/dp/B0GJL3W2D6)** 131PCS Pink Winnie Baby Shower Birthday Decorations for Girl Large Winnie Cutouts Stand Up, Pooh Balloons Arch & Bee Stickers for Gender Reveal, First Birthday, Photo Props & Newborn Party

**5. [B0FWC8ZZ48](https://www.amazon.com/dp/B0FWC8ZZ48)** 4 Ft Happy Birthday Jesus Cardboard Cutout Stand Up Life Size Large Religious Christ Party Decoration Christian Photo Props Backdrop for Jesus Party Easter VBS Church Baptism Sunday School

**6. [B0FG2C7QD8](https://www.amazon.com/dp/B0FG2C7QD8)** Yookeer 4ft Lion Cardboard Cutout Stand up Life Size Safari-Themed Birthday Party Decoration Jungle Lion Cardboard Stand-up Photo Prop for Zoo Theme Vbs Event Backdrop Stand up Decorations

## 三、尚未分析的候选类目（共 12 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Multi-Item Party Favor Packs | 多项目派对礼包 | `Home & Kitchen > Event & Party Supplies > Favors > Multi-Item Party Favor Packs` |
| 2 | Electrical System Tools | 电气系统工具 | `Automotive > Tools & Equipment > Electrical System Tools` |
| 3 | Brake System Bleeding Tools | 刹车排气 | `Automotive > Tools & Equipment > Brake Tools > Brake System Bleeding Tools` |
| 4 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 5 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 6 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 7 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 8 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 9 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 10 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 11 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 12 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 12 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B09PKHLH7W`: 105,040 | 8,436 | 7% | 449 | 7.42% | $21,534 | 200+ | $9K+ | 1 | $47.96 | - | 87 | - | 4.5 | - | $16.76 | 50% | 2022-01-11 | 4年 5个月 | FBA | -
- `B0GHSNNZPZ`: 57,231 | 12,495 | 18% | 402 | 37.36% | $10,850 | 300+ | $8K+ | 1 | $26.99 | - | 13 | 4 | 4.6 | 1% | $6.13 | 62% | 2026-03-08 | 3个月 | FBA | -
- `B0G7YT3F1H`: 537,981 | 318,998 | 28% | 290 | 40.56% | $9,567 | - | - | 1 | $32.99 | - | 2 | - | 5.0 | - | $6.13 | 66% | 2025-12-20 | 5个月 | FBA | -
- `B0GJL3W2D6`: 118,592 | 28,152 | 19% | 281 | 159.57% | $7,584 | 200+ | $5K+ | 1 | $26.99 | - | 11 | 2 | 4.4 | 0.71% | $6.90 | 59% | 2026-03-25 | 2个月 | FBA | -
- `B0FWC8ZZ48`: 102,764 | 30,609 | 23% | 220 | 103.49% | $6,598 | 100+ | $3K+ | 4 | $29.99 | - | 14 | 2 | 4.8 | 0.91% | $6.02 | 65% | 2025-10-16 | 7个月 | FBA | -
- `B0FG2C7QD8`: 144,300 | 68,602 | 33% | 148 | 5.97% | $4,587 | 50+ | $1K+ | 4 | $30.99 | - | 21 | 2 | 4.2 | 1.35% | $6.90 | 62% | 2025-07-20 | 10个月 | FBA | -

---

<!-- source: products/compressed_air_dusters.md -->
# Compressed Air Dusters 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters`
> 共抓取 **6** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **6** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $35.18　均Reviews 351（中等）　重量 0.86lbs（轻）　退货率 3.16%（低）　品牌集中度 59.8%（中等）　中国卖家 77.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0FPRM62Z2](https://www.amazon.com/dp/B0FPRM62Z2) |  | Compressed Air Duster-230000RPM Super Power Electric Air Duster | 679 / 74.71% | $20,363 | $29.99 | $2.33 (8%) | 48 / 26 | 4.3 | $4.87 / 76% | 1 | 61 | 1 | 0.99 pounds | 2025-10-11 8个月 |
| 2 | [B0FFGTDMMX](https://www.amazon.com/dp/B0FFGTDMMX) |  | fourq Compressed Air Duster,Mini Vacuum Cleaner 2-in-1,4000 mAh,1… | 449 / 132.63% | $12,792 | $28.49 | $2.41 (8%) | 26 / 11 | 4.2 | $6.42 / 69% | 1 | 61 | 1 | 1.57 pounds | 2025-06-26 11个月 |
| 3 | [B0FSLLJ8SZ](https://www.amazon.com/dp/B0FSLLJ8SZ) |  | Mini Ultra-Slim Electric Compressed Air Duster 150,000RPM Super P… | 346 / 67.33% | $8,993 | $25.99 | $2.04 (8%) | 55 / - | 4.3 | $4.46 / 75% | 2 | 67 | 2 | 0.64 pounds | 2025-10-31 7个月 |
| 4 | [B0GRH6MY39](https://www.amazon.com/dp/B0GRH6MY39) |  | Electric Air Duster 180000RPM | 190 / 50% | $7,598 | $39.99 | $3.08 (8%) | 48 / 3 | 4.5 | $5.72 / 78% | 1 | 188 | 1 | 1.34 pounds | 2026-03-09 3个月 |
| 5 | [B0GGR1T98P](https://www.amazon.com/dp/B0GGR1T98P) |  | Compressed Air Duster-150000RPM Super Power Cordless Air Duster | 239 / 116.81% | $5,734 | $23.99 | $1.85 (8%) | 40 / 17 | 4.3 | $4.87 / 72% | 1 | 126 | 1 | 0.93 pounds | 2026-03-14 2个月 |
| 6 | [B0DB8J4T52](https://www.amazon.com/dp/B0DB8J4T52) |  | Compressed Air Duster,180000RPM Electric Duster Air Blower,Cordle… | 103 / 8.25% | $2,566 | $24.91 | $1.89 (8%) | 150 / 2 | 4.3 | $5.33 / 71% | 1 | 241 | 1 | 1.1 pounds | 2024-09-27 1年 8个月 |

## 二、完整商品标题

**1. [B0FPRM62Z2](https://www.amazon.com/dp/B0FPRM62Z2)** Compressed Air Duster-230000RPM Super Power Electric Air Duster, 4-Gear Adjustable Mini Blower with Type-C Fast Charging, Dust Blower for Computer, Keyboard, House, Outdoor and Car

**2. [B0FFGTDMMX](https://www.amazon.com/dp/B0FFGTDMMX)** fourq Compressed Air Duster,Mini Vacuum Cleaner 2-in-1,4000 mAh,130,000 RPM Brushless Motor,8000Pa，120MPH/1.1LB Thrust Car Dryer Air Blower for Car Cleaning,Computer Cleaning

**3. [B0FSLLJ8SZ](https://www.amazon.com/dp/B0FSLLJ8SZ)** Mini Ultra-Slim Electric Compressed Air Duster 150,000RPM Super Power, Rechargeable Cordless Air Duster, Powerful Airflow for Computer, Keyboard, Outdoor, House and Car

**4. [B0GRH6MY39](https://www.amazon.com/dp/B0GRH6MY39)** Electric Air Duster 180000RPM, Powerful Cordless Compressed Air Duster with 3-Speed Mini Air Duster Blower, Rechargeable Dust Cleaner for Computer Keyboard, PC, Car, Outdoor & Home Cleaning

**5. [B0GGR1T98P](https://www.amazon.com/dp/B0GGR1T98P)** Compressed Air Duster-150000RPM Super Power Cordless Air Duster, Rechargeable Brushless Motor Durable Power Blower with SOS LED Light,Adjustable Dust Blower for Computer, Pet,Outdoor, House and Car

**6. [B0DB8J4T52](https://www.amazon.com/dp/B0DB8J4T52)** Compressed Air Duster,180000RPM Electric Duster Air Blower,Cordless Rechargeable Mini Dust Blower,3 Gear Jet Fan for PC Keyboard Computer Car Outdoor House Cleaning-Black

## 三、尚未分析的候选类目（共 6 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 2 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 3 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 4 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 5 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 6 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 6 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0FPRM62Z2`: 10,984 | 1,637 | 13% | 679 | 74.71% | $20,363 | 600+ | $18K+ | 1 | $29.99 | - | 48 | 26 | 4.3 | 3.83% | $4.87 | 76% | 2025-10-11 | 8个月 | FBA | -
- `B0FFGTDMMX`: 11,601 | 8,576 | 43% | 449 | 132.63% | $12,792 | 400+ | $12K+ | 1 | $28.49 | - | 26 | 11 | 4.2 | 2.45% | $6.42 | 69% | 2025-06-26 | 11个月 | FBA | -
- `B0FSLLJ8SZ`: 13,811 | 10,742 | 44% | 346 | 67.33% | $8,993 | 200+ | $6K+ | 2 | $25.99 | - | 55 | - | 4.3 | - | $4.46 | 75% | 2025-10-31 | 7个月 | FBA | -
- `B0GRH6MY39`: 35,296 | 8,084 | 19% | 190 | 50% | $7,598 | 100+ | $3K+ | 1 | $39.99 | - | 48 | 3 | 4.5 | 1.58% | $5.72 | 78% | 2026-03-09 | 3个月 | FBA | -
- `B0GGR1T98P`: 38,926 | 6,292 | 15% | 239 | 116.81% | $5,734 | 200+ | $5K+ | 1 | $23.99 | - | 40 | 17 | 4.3 | 7.11% | $4.87 | 72% | 2026-03-14 | 2个月 | FBA | -
- `B0DB8J4T52`: 83,650 | 6,250 | 9% | 103 | 8.25% | $2,566 | - | - | 1 | $24.91 | - | 150 | 2 | 4.3 | 1.94% | $5.33 | 71% | 2024-09-27 | 1年 8个月 | FBA | -

---

<!-- source: products/decorative_trays.md -->
# Decorative Trays 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays`
> 共抓取 **14** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **14** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $22.59　均Reviews 466（中等）　重量 1.44lbs（轻）　退货率 9.52%（高）　品牌集中度 42.5%（中等）　中国卖家 78.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0D8TJDXRY](https://www.amazon.com/dp/B0D8TJDXRY) |  | PEMAR Mother of Pearl Decorative Tray | 253 / 15.42% | $11,625 | $45.95 | $6.86 (15%) | 102 / 3 | 4.7 | $7.38 / 69% | 3 | 79 | 1 | 2.89 pounds | 2024-07-22 1年 10个月 |
| 2 | [B0BMDLHHYT](https://www.amazon.com/dp/B0BMDLHHYT) |  | Round Clawfoot Dish | 247 / 16.81% | $10,621 | $43.00 | $6.66 (15%) | 109 / 3 | 4.3 | $4.09 / 75% | 2 | 76 | 1 | 0.46 pounds | 2022-11-16 3年 6个月 |
| 3 | [B0FL2236YS](https://www.amazon.com/dp/B0FL2236YS) |  | PU Leather Valet Tray Organizer | 440 / 6.5% | $9,676 | $21.99 | $3.41 (15%) | 54 / 8 | 4.9 | $5.61 / 59% | 4 | 27 | 1 | 1.09 pounds | 2025-09-17 8个月 |
| 4 | [B0DT1X5W9W](https://www.amazon.com/dp/B0DT1X5W9W) |  | Serving Acacia Wood Valet Tray for Men Women | 371 / 28.4% | $8,529 | $22.99 | $3.54 (15%) | 56 / 7 | 4.6 | $4.28 / 66% | 2 | 31 | 1 | 0.04 pounds | 2025-02-22 1年 3个月 |
| 5 | [B0B24B6TPX](https://www.amazon.com/dp/B0B24B6TPX) |  | Summit Living Handwoven Multipurpose Rectangle Rattan Tray | 170 / 137.04% | $6,798 | $39.99 | $6.15 (15%) | 138 / 2 | 4.2 | $12.25 / 54% | 1 | 100 | 1 | 2.15 pounds | 2022-09-12 3年 9个月 |
| 6 | [B0DYP3TRL2](https://www.amazon.com/dp/B0DYP3TRL2) |  | FoldTier 11 Pcs 4th of July Decoration Patriotic Tiered Tray Deco… | 260 / 7.81% | $6,497 | $24.99 | $3.65 (15%) | 64 / 3 | 4.3 | $4.35 / 68% | 3 | 160 | 1 | 0.68 pounds | 2025-03-01 1年 3个月 |
| 7 | [B0DRYD63RT](https://www.amazon.com/dp/B0DRYD63RT) |  | 12 Inch Golden Round Platter Tray | 252 / 74.64% | $5,289 | $20.99 | $3.12 (15%) | 36 / 10 | 4.5 | $5.91 / 57% | 2 | 98 | 2 | 1.81 pounds | 2025-03-12 1年 3个月 |
| 8 | [B0G3TS1YFT](https://www.amazon.com/dp/B0G3TS1YFT) |  | Vintage Brass Decorative Tray | 176 / 21.05% | $5,278 | $29.99 | $4.56 (15%) | 23 / 12 | 4.1 | $8.04 / 58% | 5 | 148 | 1 | 2.07 pounds | 2026-01-16 4个月 |
| 9 | [B0D8MW6VS1](https://www.amazon.com/dp/B0D8MW6VS1) |  | Flamingo Zen Garden Kit for Desk | 123 / 189.47% | $5,162 | $41.97 | $6.70 (16%) | 30 / 1 | 4.7 | $6.31 / 69% | 1 | 228 | 1 | 2.31 pounds | 2024-07-03 1年 11个月 |
| 10 | [B0CRVTY72B](https://www.amazon.com/dp/B0CRVTY72B) |  | INNObeta Son in Law Gifts Valet Tray from Dad | 190 / 47.41% | $4,153 | $21.86 | $3.34 (15%) | 102 / 5 | 4.8 | $3.66 / 68% | 1 | 75 | 1 | 0.49 pounds | 2024-03-20 2年 2个月 |
| 11 | [B0CCVNCZWZ](https://www.amazon.com/dp/B0CCVNCZWZ) |  | INNObeta Son Gifts Valet Tray from Dad Mom | **** / **** | **** | $21.86 | - | 69 / 2 | 4.7 | **** /  | 1 | 51 | 1 | 0.49 pounds | 2023-09-25 2年 8个月 |
| 12 | [B0FK99K3D4](https://www.amazon.com/dp/B0FK99K3D4) |  | Acacia Wood Decorative Tray for Home Decor | **** / **** | **** | $31.99 | - | 10 / 3 | 4.9 | **** /  | 2 | 221 | 1 | 2.67 pounds | 2025-08-03 10个月 |
| 13 | [B0D5H5TRRD](https://www.amazon.com/dp/B0D5H5TRRD) |  | Round Burnt Wood Serving Tray with Beads | **** / **** | **** | $27.59 | - | 121 / 2 | 4.6 | **** /  | 4 | 346 | 2 | 1.5 pounds | 2024-08-06 1年 10个月 |
| 14 | [B0F2HXLN8V](https://www.amazon.com/dp/B0F2HXLN8V) |  | Scalloped Acrylic Tray with Magnetic Mat | **** / **** | **** | $22.09 | - | 36 / - | 4.9 | **** /  | 4 | 138 | 1 | 1.32 pounds | 2025-04-01 1年 2个月 |

## 二、完整商品标题

**1. [B0D8TJDXRY](https://www.amazon.com/dp/B0D8TJDXRY)** PEMAR Mother of Pearl Decorative Tray, 13"" Round with Gold Metal Handles, Vanity/Perfume/Trinket Tray, Catchall for Dresser, Bathroom, Vanity Table (Teal Sunlight)

**2. [B0BMDLHHYT](https://www.amazon.com/dp/B0BMDLHHYT)** Round Clawfoot Dish — by Alice Lane Home Collection — Gold — for Home Decor, Candles, Jewelry, Perfume, Cosmetics, and Coffee Table — Size Small

**3. [B0FL2236YS](https://www.amazon.com/dp/B0FL2236YS)** PU Leather Valet Tray Organizer, Modern Nightstand Organizer Bedside Desktop Storage for Womens and Men, Decorative Perfume Trinket Catchall Vanity Tray for Key Watch Wallet (Beige)

**4. [B0DT1X5W9W](https://www.amazon.com/dp/B0DT1X5W9W)** Serving Acacia Wood Valet Tray for Men Women, Catch All Acacia Mens Key Dump Bedside Nightstand Organizer EDC Decorative Wooden Tray for Phone Watch Wallet Keys Jewelry

**5. [B0B24B6TPX](https://www.amazon.com/dp/B0B24B6TPX)** Summit Living Handwoven Multipurpose Rectangle Rattan Tray, 20” x 12” – Durable Wicker Tray with Leather Handles for Home Decor Display

**6. [B0DYP3TRL2](https://www.amazon.com/dp/B0DYP3TRL2)** FoldTier 11 Pcs 4th of July Decoration Patriotic Tiered Tray Decor Independence Day Table Sign Wooden Faux Book Stack Firework Sign 250th Anniversary Tabletop Centerpieces for Home Office Memorial Day

**7. [B0DRYD63RT](https://www.amazon.com/dp/B0DRYD63RT)** 12 Inch Golden Round Platter Tray, Trays for Domestic Purposes, Stainless Steel Serving, Circle Decorative Tray, Vanity Tray for Centerpiece Home Decor

**8. [B0G3TS1YFT](https://www.amazon.com/dp/B0G3TS1YFT)** Vintage Brass Decorative Tray, 11.8-Inch Round Serving Tray with Claw Feet, Decorative Coffee Table Tray for Dining Room, Entryway, Living Room

**9. [B0D8MW6VS1](https://www.amazon.com/dp/B0D8MW6VS1)** Flamingo Zen Garden Kit for Desk, Cute Japanese Flamingos Gifts for Women, Mini Zen Garden Sand Tray, Pink Room Decor Aesthetic, Home Office Desk Decorations, Sand Therapy Kit

**10. [B0CRVTY72B](https://www.amazon.com/dp/B0CRVTY72B)** INNObeta Son in Law Gifts Valet Tray from Dad, Mom, Desktop Storage Organizer PU Leather Bedside Tray Key Coin Holder for Birthday, Christmas

**11. [B0CCVNCZWZ](https://www.amazon.com/dp/B0CCVNCZWZ)** INNObeta Son Gifts Valet Tray from Dad Mom, Desktop Storage Organizer PU Leather Bedside Tray Key Coin Holder, Perfect for Birthday, Christmas - to My Son

**12. [B0FK99K3D4](https://www.amazon.com/dp/B0FK99K3D4)** Acacia Wood Decorative Tray for Home Decor, 14'' x 10'' Wooden Serving Tray for Coffee Table Centerpiece Dining Kitchen Island Decoration Bathroom Counter Display

**13. [B0D5H5TRRD](https://www.amazon.com/dp/B0D5H5TRRD)** Round Burnt Wood Serving Tray with Beads, Wooden Decorative Tray for Entertaining, Decoration, and Gifting,

**14. [B0F2HXLN8V](https://www.amazon.com/dp/B0F2HXLN8V)** Scalloped Acrylic Tray with Magnetic Mat - 8x8in Customizable Display for Photos, Art & Notes | Non-Slip Base | Elegant Décor & Organizer for Jewelry/Cosmetics for Women/Mom/Weddings

## 三、尚未分析的候选类目（共 2 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 2 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 2 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0D8TJDXRY`: 138,174 | 870 | 1% | 253 | 15.42% | $11,625 | 50+ | $2K+ | 3 | $45.95 | - | 102 | 3 | 4.7 | 1.19% | $7.38 | 69% | 2024-07-22 | 1年 10个月 | FBA | -
- `B0BMDLHHYT`: 148,672 | 1,143 | 1% | 247 | 16.81% | $10,621 | 100+ | $4K+ | 2 | $43.00 | - | 109 | 3 | 4.3 | 1.21% | $4.09 | 75% | 2022-11-16 | 3年 6个月 | FBA | -
- `B0FL2236YS`: 85,688 | 12,685 | 13% | 440 | 6.5% | $9,676 | 100+ | $2K+ | 4 | $21.99 | - | 54 | 8 | 4.9 | 1.82% | $5.61 | 59% | 2025-09-17 | 8个月 | FBA | -
- `B0DT1X5W9W`: 91,981 | 4,386 | 5% | 371 | 28.4% | $8,529 | 300+ | $6K+ | 2 | $22.99 | - | 56 | 7 | 4.6 | 1.89% | $4.28 | 66% | 2025-02-22 | 1年 3个月 | FBA | -
- `B0B24B6TPX`: 146,077 | 9,007 | 6% | 170 | 137.04% | $6,798 | 100+ | $3K+ | 1 | $39.99 | - | 138 | 2 | 4.2 | 1.18% | $12.25 | 54% | 2022-09-12 | 3年 9个月 | FBA | -
- `B0DYP3TRL2`: 92,454 | 44,406 | 32% | 260 | 7.81% | $6,497 | 100+ | $2K+ | 3 | $24.99 | - | 64 | 3 | 4.3 | 1.15% | $4.35 | 68% | 2025-03-01 | 1年 3个月 | FBA | -
- `B0DRYD63RT`: 171,599 | 30,826 | 15% | 252 | 74.64% | $5,289 | 200+ | $4K+ | 2 | $20.99 | - | 36 | 10 | 4.5 | 3.97% | $5.91 | 57% | 2025-03-12 | 1年 3个月 | FBA | -
- `B0G3TS1YFT`: 150,603 | 65,486 | 31% | 176 | 21.05% | $5,278 | 100+ | $3K+ | 5 | $29.99 | - | 23 | 12 | 4.1 | 6.82% | $8.04 | 58% | 2026-01-16 | 4个月 | FBA | -
- `B0D8MW6VS1`: 364,473 | 1,341 | 0% | 123 | 189.47% | $5,162 | 50+ | $1K+ | 1 | $41.97 | - | 30 | 1 | 4.7 | 0.81% | $6.31 | 69% | 2024-07-03 | 1年 11个月 | FBA | -
- `B0CRVTY72B`: 147,174 | 51,385 | 27% | 190 | 47.41% | $4,153 | 100+ | $2K+ | 1 | $21.86 | - | 102 | 5 | 4.8 | 2.63% | $3.66 | 68% | 2024-03-20 | 2年 2个月 | FBA | -
- `B0CCVNCZWZ`: 118,854 | 43,764 | 27% | **** | **** | **** | **** | 1 | $21.86 | - | 69 | 2 | 4.7 | 1.11% | **** | 2023-09-25 | 2年 8个月 | FBA | -
- `B0FK99K3D4`: 278,035 | 46,599 | 15% | **** | **** | **** | **** | 2 | $31.99 | - | 10 | 3 | 4.9 | 2.91% | **** | 2025-08-03 | 10个月 | FBA | -
- `B0D5H5TRRD`: 384,945 | 14,603 | 5% | **** | **** | **** | **** | 4 | $27.59 | - | 121 | 2 | 4.6 | 1.68% | **** | 2024-08-06 | 1年 10个月 | FBA | -
- `B0F2HXLN8V`: 206,686 | 95,045 | 32% | **** | **** | **** | **** | 4 | $22.09 | - | 36 | - | 4.9 | - | **** | 2025-04-01 | 1年 2个月 | FBA | -

---

<!-- source: products/electrical_system_tools.md -->
# Electrical System Tools 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Automotive › Tools & Equipment › Electrical System Tools`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $31.80　均Reviews 495（中等）　重量 1.01lbs（轻）　退货率 2.38%（低）　品牌集中度 44.0%（中等）　中国卖家 81.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0C4PTWP8G](https://www.amazon.com/dp/B0C4PTWP8G) |  | JRready ST5262 2Pcs Molex Micro Fit Extractors Microfit Terminal… | 184 / 9.58% | $6,622 | $35.99 | $5.43 (15%) | 80 / 2 | 4.4 | $3.57 / 75% | 3 | 89 | 1 | 0.31 pounds | 2023-05-09 3年 1个月 |
| 2 | [B0CR6F2HR1](https://www.amazon.com/dp/B0CR6F2HR1) |  | JRready ST5291 Deutsch Pin Removal Tool for Deutsch Size 12 16 20… | 204 / 11.6% | $6,118 | $29.99 | $4.42 (15%) | 91 / 1 | 4.2 | $4.28 / 71% | 1 | 69 | 1 | 0.57 pounds | 2024-01-08 2年 5个月 |
| 3 | [B0GHDJM616](https://www.amazon.com/dp/B0GHDJM616) |  | 9 PCS Electrical Disconnect Pliers for Cars | 221 / 29.94% | $5,965 | $26.99 | $4.05 (15%) | 36 / 6 | 4.8 | $6.48 / 61% | 2 | 72 | 1 | 2.65 pounds | 2026-02-19 3个月 |
| 4 | [B0FDVDL457](https://www.amazon.com/dp/B0FDVDL457) |  | Noid Light Test Kit | 232 / 42% | $5,102 | $21.99 | $3.36 (15%) | 64 / 2 | 4.4 | $5.22 / 61% | 1 | 63 | 1 | 1.12 pounds | 2025-10-17 7个月 |

## 二、完整商品标题

**1. [B0C4PTWP8G](https://www.amazon.com/dp/B0C4PTWP8G)** JRready ST5262 2Pcs Molex Micro Fit Extractors Microfit Terminal Release Tool Kit for Molex MX3.0 Male/Female Terminals Microfit 3.0 Extraction Tool for Micro-Fit Terminals Pin Removal Tool Kit

**2. [B0CR6F2HR1](https://www.amazon.com/dp/B0CR6F2HR1)** JRready ST5291 Deutsch Pin Removal Tool for Deutsch Size 12 16 20 Solid Contacts Wire Gauge 12-22 AWG,Terminal Release Tool Kit for Deutsch DT, DTM, DTP, DTHD, and HD Series Connectors

**3. [B0GHDJM616](https://www.amazon.com/dp/B0GHDJM616)** 9 PCS Electrical Disconnect Pliers for Cars, Electrical Connector Removal Tool and Connector Removal Tools, Relay Puller & Hose Removal Pliers,Panel Clip Remover & Filter Caliper

**4. [B0FDVDL457](https://www.amazon.com/dp/B0FDVDL457)** Noid Light Test Kit, 11-Piece Fuel Injector Noid Light Test Kit with 8 Noids & IAC Tester, Fits Multiple Car Injection System Types

## 三、尚未分析的候选类目（共 10 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Brake System Bleeding Tools | 刹车排气 | `Automotive > Tools & Equipment > Brake Tools > Brake System Bleeding Tools` |
| 2 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 3 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 4 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 5 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 6 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 7 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 8 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 9 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 10 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 10 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0C4PTWP8G`: 38,438 | 13,642 | 26% | 184 | 9.58% | $6,622 | 100+ | $3K+ | 3 | $35.99 | - | 80 | 2 | 4.4 | 1.09% | $3.57 | 75% | 2023-05-09 | 3年 1个月 | FBA | -
- `B0CR6F2HR1`: 28,712 | 21,985 | 43% | 204 | 11.6% | $6,118 | 100+ | $2K+ | 1 | $29.99 | - | 91 | 1 | 4.2 | 0.49% | $4.28 | 71% | 2024-01-08 | 2年 5个月 | FBA | -
- `B0GHDJM616`: 26,530 | 28,394 | 52% | 221 | 29.94% | $5,965 | 100+ | $2K+ | 2 | $26.99 | - | 36 | 6 | 4.8 | 2.71% | $6.48 | 61% | 2026-02-19 | 3个月 | FBA | -
- `B0FDVDL457`: 23,854 | 7,645 | 24% | 232 | 42% | $5,102 | 100+ | $2K+ | 1 | $21.99 | - | 64 | 2 | 4.4 | 0.86% | $5.22 | 61% | 2025-10-17 | 7个月 | FBA | -

---

<!-- source: products/game_mats_boards.md -->
# Game Mats & Boards 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $29.68　均Reviews 308（中等）　重量 2.47lbs（重）　退货率 7.5%（中）　品牌集中度 40.7%（中等）　中国卖家 78.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0FQ5KW2WN](https://www.amazon.com/dp/B0FQ5KW2WN) |  | Crease-Free Mahjong Mat for Table | 335 / 69.3% | $10,013 | $29.89 | $4.54 (15%) | 42 / 10 | 4.9 | $10.11 / 51% | 2 | 28 | 1 | 2.7 pounds | 2025-11-09 7个月 |
| 2 | [B0FMXW89J5](https://www.amazon.com/dp/B0FMXW89J5) |  | Chinoiserie Mahjong Mat with 1 Carrying Bag Rubber Anti Slip and… | 183 / 8.56% | $5,488 | $29.99 | $3.69 (12%) | 6 / 2 | 4.1 | $10.11 / 54% | 1 | 346 | 1 | 1.95 pounds | 2025-10-11 8个月 |
| 3 | [B0DD6X3QTH](https://www.amazon.com/dp/B0DD6X3QTH) |  | DND Map 32 Terrain 24” x 36",17” x 17",13” x 17" Double Sidedv Gr… | 124 / 45.07% | $4,959 | $39.99 | $5.90 (15%) | 71 / 5 | 4.5 | $10.50 / 59% | 1 | 115 | 1 | 3.1 pounds | 2024-09-17 1年 8个月 |
| 4 | [B0GHHG1W42](https://www.amazon.com/dp/B0GHHG1W42) |  | 24" Playmat for Trading Card Games with Damage Counters | 194 / 56.36% | $4,072 | $20.99 | $3.21 (15%) | 10 / 3 | 4.9 | $5.61 / 58% | 5 | 85 | 1 | 1.39 pounds | 2026-03-26 2个月 |
| 5 | [B0GQMQCCNH](https://www.amazon.com/dp/B0GQMQCCNH) |  | Mahjong Mat with Black Carrying Bag | 128 / 21.3% | $3,967 | $30.99 | $4.52 (15%) | 11 / 7 | 4.3 | $6.02 / 66% | 5 | 105 | 1 | 2.82 pounds | 2026-04-21 1个月 |

## 二、完整商品标题

**1. [B0FQ5KW2WN](https://www.amazon.com/dp/B0FQ5KW2WN)** Crease-Free Mahjong Mat for Table, American Mahjong Mat with Charleston Rules, 31.5 x 31.5 inch Non-Slip Rubber Backing Noise-Reducing Mah Jongg Learning Mat with Carrying Bag (Blue)

**2. [B0FMXW89J5](https://www.amazon.com/dp/B0FMXW89J5)** Chinoiserie Mahjong Mat with 1 Carrying Bag Rubber Anti Slip and Noise Reduction Multi Purpose Game Table Cover for Mahjong, Card, Board Tile Games-874

**3. [B0DD6X3QTH](https://www.amazon.com/dp/B0DD6X3QTH)** DND Map 32 Terrain 24” x 36",17” x 17",13” x 17" Double Sidedv Grids Dry Erase Battle Mats for Dungeons & Dragons Game with Dice Set,Clips,Eraser,Markers

**4. [B0GHHG1W42](https://www.amazon.com/dp/B0GHHG1W42)** 24" Playmat for Trading Card Games with Damage Counters, 2 Player Gaming Mat Board Stadium with Playmat Bag, Red-White, 2mm Thick

**5. [B0GQMQCCNH](https://www.amazon.com/dp/B0GQMQCCNH)** Mahjong Mat with Black Carrying Bag, 31.5"x31.5" Waterproof Mahjong Table Mat, with Natural Rubber Non-Slip Backing, Includes 3 Dice & Travel Bag (Purple Lotus)

## 三、尚未分析的候选类目（共 1 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 1 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0FQ5KW2WN`: 20,800 | 14,276 | 41% | 335 | 69.3% | $10,013 | 200+ | $5K+ | 2 | $29.89 | - | 42 | 10 | 4.9 | 2.99% | $10.11 | 51% | 2025-11-09 | 7个月 | FBA | -
- `B0FMXW89J5`: 148,268 | 8,494 | 17% | 183 | 8.56% | $5,488 | - | - | 1 | $29.99 | - | 6 | 2 | 4.1 | 1.09% | $10.11 | 54% | 2025-10-11 | 8个月 | FBA | -
- `B0DD6X3QTH`: 55,693 | 42,912 | 44% | 124 | 45.07% | $4,959 | 100+ | $3K+ | 1 | $39.99 | - | 71 | 5 | 4.5 | 4.03% | $10.50 | 59% | 2024-09-17 | 1年 8个月 | FBA | -
- `B0GHHG1W42`: 41,419 | 1,500 | 3% | 194 | 56.36% | $4,072 | 100+ | $2K+ | 5 | $20.99 | - | 10 | 3 | 4.9 | 1.55% | $5.61 | 58% | 2026-03-26 | 2个月 | FBA | -
- `B0GQMQCCNH`: 52,467 | 36,206 | 41% | 128 | 21.3% | $3,967 | 50+ | $1K+ | 5 | $30.99 | - | 11 | 7 | 4.3 | 5.47% | $6.02 | 66% | 2026-04-21 | 1个月 | FBA | -

---

<!-- source: products/grinding_discs.md -->
# Grinding Discs 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $24.71　均Reviews 365（中等）　重量 1.92lbs（偏重）　退货率 2.13%（低）　品牌集中度 47.2%（中等）　中国卖家 80.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DB1B6DKZ](https://www.amazon.com/dp/B0DB1B6DKZ) |  | 11PCS Wood Carving Disc Set for 4" or 4 1/2" Angle Grinder | 671 / 85.42% | $26,833 | $39.99 | $4.70 (12%) | 132 / 9 | 4.6 | $7.30 / 70% | 1 | 7 | 1 | 3.12 pounds | 2024-09-06 1年 9个月 |
| 2 | [B0CBS4VWYB](https://www.amazon.com/dp/B0CBS4VWYB) |  | 4 in.x 5/8-11 in. Smooth Grinding Resin Filled Diamond Cup Wheel… | 101 / 134.78% | $5,655 | $55.99 | $6.83 (12%) | 28 / 2 | 4.0 | $5.49 / 78% | 3 | 135 | 1 | 1.1 pounds | 2023-08-28 2年 9个月 |

## 二、完整商品标题

**1. [B0DB1B6DKZ](https://www.amazon.com/dp/B0DB1B6DKZ)** 11PCS Wood Carving Disc Set for 4" or 4 1/2" Angle Grinder, Stump Tool Grinding Wheel Disc with 5/8" Adapter Ring, Woodworking Grinder Attachment for Cutting Shaping Carving Sanding Polishing

**2. [B0CBS4VWYB](https://www.amazon.com/dp/B0CBS4VWYB)** 4 in.x 5/8-11 in. Smooth Grinding Resin Filled Diamond Cup Wheel for Angle Grinder, Resin Filled Diamond Grinding Wheel for Granite Marble Engineered Stone

## 三、尚未分析的候选类目（共 7 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 2 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 3 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 4 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 5 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 6 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 7 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 7 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0DB1B6DKZ`: 5,410 | 1,544 | 22% | 671 | 85.42% | $26,833 | 600+ | $23K+ | 1 | $39.99 | - | 132 | 9 | 4.6 | 1.34% | $7.30 | 70% | 2024-09-06 | 1年 9个月 | FBA | -
- `B0CBS4VWYB`: 58,429 | 25,781 | 31% | 101 | 134.78% | $5,655 | - | - | 3 | $55.99 | 4 | 28 | 2 | 4.0 | 1.98% | $5.49 | 78% | 2023-08-28 | 2年 9个月 | FBA | -

---

<!-- source: products/lighting_products.md -->
# Lighting Products 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products`
> 共抓取 **18** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **18** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $49.26　均Reviews 480（中等）　重量 1.76lbs（偏重）　退货率 6.75%（中）　品牌集中度 54.0%（中等）　中国卖家 76.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0G6L569ZB](https://www.amazon.com/dp/B0G6L569ZB) |  | Rechargeable Submersible Pool Lights with Remote | 815 / 158.46% | $48,052 | $58.96 | $8.75 (15%) | 39 / 11 | 4.4 | $6.58 / 74% | 2 | 37 | 1 | 2.37 pounds | 2026-03-09 3个月 |
| 2 | [B0GD7YRTDM](https://www.amazon.com/dp/B0GD7YRTDM) |  | APONUO Solar Pool Lights | 814 / 162.85% | $34,994 | $42.99 | $6.32 (15%) | 40 / 10 | 4.1 | $5.72 / 72% | 3 | 34 | 1 | 1.26 pounds | 2026-03-26 2个月 |
| 3 | [B0GJCRX242](https://www.amazon.com/dp/B0GJCRX242) |  | Solar Floating Pool Lights | 822 / 137.86% | $27,118 | $32.99 | $5.02 (15%) | 58 / 25 | 4.0 | $5.87 / 67% | 1 | 42 | 1 | 1.32 pounds | 2026-03-19 2个月 |
| 4 | [B0DZD1RC33](https://www.amazon.com/dp/B0DZD1RC33) |  | Solar Floating Pool Lights | 518 / 88.36% | $23,818 | $45.98 | $6.86 (15%) | 132 / 11 | 4.4 | $6.01 / 72% | 2 | 100 | 2 | 2.18 pounds | 2025-05-21 1年 |
| 5 | [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF) |  | Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool… | 423 / 148.32% | $16,916 | $39.99 | $6.05 (15%) | 31 / 7 | 4.4 | $4.35 / 74% | 2 | 88 | 1 | 0.44 pounds | 2025-05-07 1年 1个月 |
| 6 | [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H) |  | SIEDiNLAR Solar Floating Pool Lights with Remote | 358 / 145.11% | $12,884 | $35.99 | $5.29 (15%) | 36 / 11 | 4.0 | $5.87 / 69% | 2 | 135 | 1 | 1.57 pounds | 2026-04-05 2个月 |
| 7 | [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB) |  | 55ft Solar Pool Lights for Above Ground Pools | 538 / 183.92% | $11,293 | $20.99 | $3.10 (15%) | 117 / 9 | 4.0 | $4.46 / 64% | 4 | 77 | 1 | 0.73 pounds | 2025-02-28 1年 3个月 |
| 8 | [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC) |  | Floating Pool Lights | 359 / 146.4% | $10,759 | $29.97 | $4.43 (15%) | 30 / 12 | 4.9 | $5.76 / 66% | 2 | 94 | 1 | 1.53 pounds | 2026-04-21 1个月 |
| 9 | [B0DSD4NWXN](https://www.amazon.com/dp/B0DSD4NWXN) |  | Askyli Floating Pool Lights Solar with Remote | 306 / 21.14% | $8,718 | $39.99 | $8.99 (22%) | 138 / 4 | 4.1 | $7.41 / 59% | 2 | 97 | 1 | 2.62 pounds | 2025-04-27 1年 1个月 |
| 10 | [B0FWJ6C4CY](https://www.amazon.com/dp/B0FWJ6C4CY) |  | Askyli Pool Lights for Above Ground Pools | 320 / 151.46% | $8,051 | $25.16 | $3.84 (15%) | 36 / 9 | 4.2 | $5.72 / 62% | 3 | 108 | 1 | 1.43 pounds | 2026-03-07 3个月 |
| 11 | [B0G6SLH595](https://www.amazon.com/dp/B0G6SLH595) |  | Floating Pool Lights w/Remote | **** / **** | **** | $36.99 | - | 39 / 1 | 4.7 | **** /  | 3 | 120 | 1 | 2.12 pounds | 2026-03-14 2个月 |
| 12 | [B0CX9162PJ](https://www.amazon.com/dp/B0CX9162PJ) |  | BOXPSII Pool Lights(4 Pack) | **** / **** | **** | $52.99 | - | 148 / 2 | 4.2 | **** /  | 3 | 187 | 1 | 1.79 pounds | 2024-04-19 2年 1个月 |
| 13 | [B0G8X6721P](https://www.amazon.com/dp/B0G8X6721P) |  | Pool Lights for Inground & Above Ground Pool | **** / **** | **** | $26.84 | - | 20 / 6 | 4.4 | **** /  | 2 | 98 | 1 | 1.23 pounds | 2026-04-07 2个月 |
| 14 | [B0FWC5JQL9](https://www.amazon.com/dp/B0FWC5JQL9) |  | 500W R40 120V Pool Lights Bulb for Inground Pool & Spa | **** / **** | **** | $53.99 | - | 14 / 3 | 4.6 | **** /  | 1 | 219 | 2 | 0.71 pounds | 2025-11-18 6个月 |
| 15 | [B0D93J8T91](https://www.amazon.com/dp/B0D93J8T91) |  | LED Pool Light Bulb 12V 50W 5000LM 6500K Daylight White LED Swimm… | **** / **** | **** | $37.99 | - | 75 / - | 4.0 | **** /  | 1 | 288 | 1 | 0.68 pounds | 2024-08-08 1年 10个月 |
| 16 | [B0DN6FBDDQ](https://www.amazon.com/dp/B0DN6FBDDQ) |  | Tujoe Remote Control LED Pool Lights for Above Ground Pools Subme… | **** / **** | **** | $30.99 | - | 32 / 1 | 4.0 | **** /  | 2 | 246 | 1 | 1.59 pounds | 2024-11-16 1年 6个月 |
| 17 | [B0GCZ27BY1](https://www.amazon.com/dp/B0GCZ27BY1) |  | Qoolife Pool Chlorine Floater with Thermometer Solar Light | **** / **** | **** | $29.99 | - | 34 / 19 | 4.0 | **** /  | 1 | 336 | 1 | 1.21 pounds | 2026-03-29 2个月 |
| 18 | [B0GL8DTBM6](https://www.amazon.com/dp/B0GL8DTBM6) |  | Solar Floating Pool Lights: Solar Pool Lights That Float with Rem… | **** / **** | **** | $23.99 | - | 31 / 9 | 4.2 | **** /  | 3 | 285 | 2 | 0.93 pounds | 2026-03-25 2个月 |

## 二、完整商品标题

**1. [B0G6L569ZB](https://www.amazon.com/dp/B0G6L569ZB)** Rechargeable Submersible Pool Lights with Remote, 5000mAh Underwater Led Pool Light for Above Ground Pool Lights Waterproof, 9 Modes Color Changing Magnetic Swimming Inground Pool Lights-2PC

**2. [B0GD7YRTDM](https://www.amazon.com/dp/B0GD7YRTDM)** APONUO Solar Pool Lights, IP68 Waterproof Floating Pool Lights with Remote& Button Control, 9 Lighting Colors& 3 Modes Pool Solar Light, Timer&Memory, Floating Light for Pool, Party, Bathtub (2 Pack)

**3. [B0GJCRX242](https://www.amazon.com/dp/B0GJCRX242)** Solar Floating Pool Lights, Outdoor LED Pool Lighted that Float with Remote, IP68 Waterproof Swimming Decor Lighting for Inground Pool, Above Ground Pools, Pond, 2 Pack

**4. [B0DZD1RC33](https://www.amazon.com/dp/B0DZD1RC33)** Solar Floating Pool Lights, 14 Inch Flame Solar Pool Light Balls, Floating Glow Globe IP68 Waterproof, Inflatable Solar Lights up Balls for Swimming Pool Pond Outdoor Decor -4PCS

**5. [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF)** Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool Light Bulb Daylight White 6000K Swimming Pool Replacement for Most Pentair Hayward Light Fixtures (120V 65W)

**6. [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H)** SIEDiNLAR Solar Floating Pool Lights with Remote, 12 Modes RGB Color Changing Solar Powered Pool Lights, Waterproof Floating Lights for Swimming Pool, Pond, Fountain, Backyard & Party Decor (4 Pack)

**7. [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB)** 55ft Solar Pool Lights for Above Ground Pools, 150 LEDs Remote IP65 Waterproof Rope Lights, 8 Color Modes, Swimming Frame Pool Decor Accessories for Outdoor Outside Trampoline Camping

**8. [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC)** Floating Pool Lights, 15" Inflatable Solar Powered Pool Lights That Float, Color Changing LED Glow Balls, IP68 Waterproof Solar Floating Light Up Balls for Pool,Pond, Outdoor Party Decor - 2PCS

**9. [B0DSD4NWXN](https://www.amazon.com/dp/B0DSD4NWXN)** Askyli Floating Pool Lights Solar with Remote, 7.6 Inch RGB Up and Down Color Changing Solar Pool Lights that Float with Dynamic Lighting Effects, Floating Light for Pools, Party, Decor(2)

**10. [B0FWJ6C4CY](https://www.amazon.com/dp/B0FWJ6C4CY)** Askyli Pool Lights for Above Ground Pools, Upgraded Rechargeable Dynamic Lighting Inground Pool Lights that Float w/Remote, 16H Runtimes Underwater LED Pools Light with Timer Off for Hot Tub Pond-2PC

**11. [B0G6SLH595](https://www.amazon.com/dp/B0G6SLH595)** Floating Pool Lights w/Remote, 6.5" Top to Bottom Dynamic Color Changing Solar Pool Lights that Float, IP68 Waterproof Solar Floating Light for Inground Above Ground Pools Garden Decor(2)

**12. [B0CX9162PJ](https://www.amazon.com/dp/B0CX9162PJ)** BOXPSII Pool Lights(4 Pack), Upgraded Rechargeable Submersible LED Lights with Remote, IP68 Waterproof 16 Color Floating Light with Magnet, Pool Light for Above Ground Inground Pools,Hot Tub, Bath

**13. [B0G8X6721P](https://www.amazon.com/dp/B0G8X6721P)** Pool Lights for Inground & Above Ground Pool, Underwater Submersible Swimming LED Pool Light with Remote Control,Waterproof Magnetic Pools Lights for Inground Above Ground Pools,Hot tub-1 PC

**14. [B0FWC5JQL9](https://www.amazon.com/dp/B0FWC5JQL9)** 500W R40 120V Pool Lights Bulb for Inground Pool & Spa – 3000K Warm White, E26 Base, High-Power, Compatible with Pentair & Hayward Fixtures, 3,000-Hour Lifespan (2 Pack)

**15. [B0D93J8T91](https://www.amazon.com/dp/B0D93J8T91)** LED Pool Light Bulb 12V 50W 5000LM 6500K Daylight White LED Swimming Pool Light Bulb, Replaces up to 200-800W Traditionnal Bulb for Most Pentair Hayward Light Fixtures（NOT 120V）

**16. [B0DN6FBDDQ](https://www.amazon.com/dp/B0DN6FBDDQ)** Tujoe Remote Control LED Pool Lights for Above Ground Pools Submersible Waterproof Outdoor LED Rim Rope Lights with Battery Box, Waterproof Bundle Pocket for Outdoor(55.7ft Fits18ft Pool)

**17. [B0GCZ27BY1](https://www.amazon.com/dp/B0GCZ27BY1)** Qoolife Pool Chlorine Floater with Thermometer Solar Light, 3 in1Chlorine Floater for Pond Fit 1" and 3", Floating Dispenser with Remote and Adjustable for Pool Spa Hot Tub

**18. [B0GL8DTBM6](https://www.amazon.com/dp/B0GL8DTBM6)** Solar Floating Pool Lights: Solar Pool Lights That Float with Remote, 7 Lighting, RGB 6 Dynamic Modes, IP68 Waterproof Swimming Pool Lights for Inground Pool Bathtub Party Garden Weeding (2 Pack)

## 三、尚未分析的候选类目（共 14 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Nozzles | 喷嘴 | `Patio, Lawn & Garden > Outdoor Power Tools > Replacement Parts & Accessories > Pressure Washer Parts & Accessories > Nozzles` |
| 2 | Cardboard Cutouts | 硬板纸模型 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Cardboard Cutouts` |
| 3 | Multi-Item Party Favor Packs | 多项目派对礼包 | `Home & Kitchen > Event & Party Supplies > Favors > Multi-Item Party Favor Packs` |
| 4 | Electrical System Tools | 电气系统工具 | `Automotive > Tools & Equipment > Electrical System Tools` |
| 5 | Brake System Bleeding Tools | 刹车排气 | `Automotive > Tools & Equipment > Brake Tools > Brake System Bleeding Tools` |
| 6 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 7 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 8 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 9 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 10 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 11 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 12 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 13 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 14 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 14 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0G6L569ZB`: 9,861 | 555 | 5% | 815 | 158.46% | $48,052 | 600+ | $35K+ | 2 | $58.96 | - | 39 | 11 | 4.4 | 1.35% | $6.58 | 74% | 2026-03-09 | 3个月 | FBA | -
- `B0GD7YRTDM`: 9,432 | 2,514 | 21% | 814 | 162.85% | $34,994 | 500+ | $22K+ | 3 | $42.99 | - | 40 | 10 | 4.1 | 1.23% | $5.72 | 72% | 2026-03-26 | 2个月 | FBA | -
- `B0GJCRX242`: 9,176 | 11,610 | 56% | 822 | 137.86% | $27,118 | 700+ | $26K+ | 1 | $32.99 | - | 58 | 25 | 4.0 | 3.04% | $5.87 | 67% | 2026-03-19 | 2个月 | FBA | -
- `B0DZD1RC33`: 22,594 | 941 | 4% | 518 | 88.36% | $23,818 | 400+ | $18K+ | 2 | $45.98 | - | 132 | 11 | 4.4 | 2.12% | $6.01 | 72% | 2025-05-21 | 1年 | FBA | -
- `B0DXVSDMZF`: 21,990 | 2,628 | 11% | 423 | 148.32% | $16,916 | 200+ | $7K+ | 2 | $39.99 | - | 31 | 7 | 4.4 | 1.65% | $4.35 | 74% | 2025-05-07 | 1年 1个月 | FBA | -
- `B0GPW9YT5H`: 28,375 | 1,218 | 4% | 358 | 145.11% | $12,884 | 200+ | $7K+ | 2 | $35.99 | - | 36 | 11 | 4.0 | 3.07% | $5.87 | 69% | 2026-04-05 | 2个月 | FBA | -
- `B0DWMMYNDB`: 18,386 | 2,081 | 10% | 538 | 183.92% | $11,293 | 200+ | $3K+ | 4 | $20.99 | - | 117 | 9 | 4.0 | 1.67% | $4.46 | 64% | 2025-02-28 | 1年 3个月 | FBA | -
- `B0GRTPX9DC`: 22,372 | 10,423 | 30% | 359 | 146.4% | $10,759 | 200+ | $6K+ | 2 | $29.97 | - | 30 | 12 | 4.9 | 3.34% | $5.76 | 66% | 2026-04-21 | 1个月 | FBA | -
- `B0DSD4NWXN`: 22,465 | 12,329 | 35% | 306 | 21.14% | $8,718 | - | - | 2 | $39.99 | - | 138 | 4 | 4.1 | 1.31% | $7.41 | 59% | 2025-04-27 | 1年 1个月 | FBA | -
- `B0FWJ6C4CY`: 23,928 | 10,462 | 30% | 320 | 151.46% | $8,051 | 200+ | $9K+ | 3 | $25.16 | - | 36 | 9 | 4.2 | 2.81% | $5.72 | 62% | 2026-03-07 | 3个月 | FBA | -
- `B0G6SLH595`: 27,486 | 13,081 | 32% | **** | **** | **** | **** | 3 | $36.99 | - | 39 | 1 | 4.7 | 0.49% | **** | 2026-03-14 | 2个月 | FBA | -
- `B0CX9162PJ`: 49,291 | 7,016 | 9% | **** | **** | **** | **** | 3 | $52.99 | - | 148 | 2 | 4.2 | 1.49% | **** | 2024-04-19 | 2年 1个月 | FBA | -
- `B0G8X6721P`: 23,221 | 13,401 | 37% | **** | **** | **** | **** | 2 | $26.84 | - | 20 | 6 | 4.4 | 2.78% | **** | 2026-04-07 | 2个月 | FBA | -
- `B0FWC5JQL9`: 60,424 | 33,248 | 36% | **** | **** | **** | **** | 1 | $53.99 | - | 14 | 3 | 4.6 | 2.86% | **** | 2025-11-18 | 6个月 | FBA | -
- `B0D93J8T91`: 69,495 | 10,494 | 13% | **** | **** | **** | **** | 1 | $37.99 | - | 75 | - | 4.0 | - | **** | 2024-08-08 | 1年 10个月 | FBA | -
- `B0DN6FBDDQ`: 45,307 | 4,504 | 9% | **** | **** | **** | **** | 2 | $30.99 | - | 32 | 1 | 4.0 | 0.74% | **** | 2024-11-16 | 1年 6个月 | FBA | -
- `B0GCZ27BY1`: 44,536 | 45,214 | 50% | **** | **** | **** | **** | 1 | $29.99 | - | 34 | 19 | 4.0 | 16.67% | **** | 2026-03-29 | 2个月 | FBA | -
- `B0GL8DTBM6`: 71,193 | 54,323 | 44% | **** | **** | **** | **** | 3 | $23.99 | - | 31 | 9 | 4.2 | 8.11% | **** | 2026-03-25 | 2个月 | FBA | -

---

<!-- source: products/multi_item_party_favor_packs.md -->
# Multi-Item Party Favor Packs 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Home & Kitchen › Event & Party Supplies › Favors › Multi-Item Party Favor Packs`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $20.12　均Reviews 161（低竞争）　重量 1.04lbs（轻）　退货率 4.75%（低）　品牌集中度 34.5%（分散）　中国卖家 91.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GQTBS8WH](https://www.amazon.com/dp/B0GQTBS8WH) |  | 24 PCs Kids Keychains | 780 / 172.02% | $17,152 | $21.99 | $3.26 (15%) | 38 / 9 | 4.7 | $5.76 / 59% | 1 | 9 | 1 | 0.77 pounds | 2026-03-30 2个月 |
| 2 | [B0GGBHWRQF](https://www.amazon.com/dp/B0GGBHWRQF) |  | 24Pcs Toy Inspired Story Birthday Party Supplies Reusable Drinkin… | 479 / 108.8% | $14,365 | $29.99 | $4.59 (15%) | 34 / 7 | 5.0 | $5.61 / 66% | 1 | 19 | 1 | 0.49 pounds | 2026-02-12 4个月 |
| 3 | [B0G2RR1NTG](https://www.amazon.com/dp/B0G2RR1NTG) |  | J6&H6 2026 Soccer Party Favors Soccer Goodie Bags Including 12 So… | 568 / 30.2% | $14,194 | $24.99 | $3.66 (15%) | 37 / 11 | 4.9 | $6.34 / 60% | 4 | 27 | 1 | 1.83 pounds | 2025-12-24 5个月 |
| 4 | [B0C3HSQ4HK](https://www.amazon.com/dp/B0C3HSQ4HK) |  | 24 Pcs Inflatable Guitars for Parties Bulk Blow Rock Star Guitar… | 428 / 30.11% | $12,836 | $29.99 | $4.64 (15%) | 141 / 3 | 4.2 | $6.76 / 62% | 5 | 59 | 1 | 2.91 pounds | 2023-04-27 3年 1个月 |
| 5 | [B0FPQRQJN7](https://www.amazon.com/dp/B0FPQRQJN7) |  | 12 Set K-pop Party Favors Includes Inflatable Microphones and Hea… | 408 / 45.85% | $11,828 | $28.99 | $4.23 (15%) | 19 / 7 | 4.8 | $4.76 / 69% | 4 | 42 | 1 | 0.88 pounds | 2025-09-05 9个月 |
| 6 | [B0FM88PPZW](https://www.amazon.com/dp/B0FM88PPZW) |  | Axolotl Gifts for Girls | 418 / 17.38% | $11,282 | $26.99 | $4.05 (15%) | 50 / 7 | 4.8 | $6.48 / 61% | 1 | 37 | 1 | 2.14 pounds | 2025-09-30 8个月 |
| 7 | [B0FY36HRX3](https://www.amazon.com/dp/B0FY36HRX3) |  | SHQDD 46 PCS 4th of July Foam Glow Stick Pack | 258 / 144.64% | $9,801 | $33.26 | $3.75 (11%) | 21 / 1 | 4.8 | $9.22 / 61% | 1 | 53 | 1 | 1.76 pounds | 2026-02-01 4个月 |
| 8 | [B0GGGMZMS9](https://www.amazon.com/dp/B0GGGMZMS9) |  | WenmthG 40Pcs Teacher Appreciation Gifts Bulk for Women Men Cowor… | 376 / 192.25% | $8,644 | $22.99 | $3.53 (15%) | 16 / 10 | 4.6 | $6.13 / 58% | 3 | 79 | 1 | 2.23 pounds | 2026-01-15 4个月 |
| 9 | [B0F1FZLMV1](https://www.amazon.com/dp/B0F1FZLMV1) |  | Lunmon 50 Sets Patriotic Rubber Ducks Bulk 4th of July Rubber Duc… | 198 / 96.1% | $7,720 | $38.99 | $5.71 (15%) | 19 / 2 | 4.6 | $7.55 / 66% | 3 | 169 | 1 | 2.93 pounds | 2025-03-31 1年 2个月 |
| 10 | [B0FGJQBGRR](https://www.amazon.com/dp/B0FGJQBGRR) |  | Hiboom 48 Gone Fishing Party Favors Set 12 Candy Mini Tackle Boxe… | 237 / 108.26% | $6,160 | $25.99 | $3.86 (15%) | 22 / 3 | 4.1 | $5.76 / 63% | 2 | 138 | 1 | 1.1 pounds | 2025-07-06 11个月 |
| 11 | [B0G7HHBH8D](https://www.amazon.com/dp/B0G7HHBH8D) |  | HigzYovn 12-Pack Dr Seu Party Favors Pre-Packaged: Oh The Places… | **** / **** | **** | $20.99 | - | 5 / - | 5.0 | **** /  | 1 | 225 | 1 | 0.73 pounds | 2026-02-08 4个月 |
| 12 | [B0DSPXBGYD](https://www.amazon.com/dp/B0DSPXBGYD) |  | Hollowfly 24 Sets 2026 Graduation Gifts Graduation Rubber Ducks w… | **** / **** | **** | $30.99 | - | 26 / - | 4.8 | **** /  | 3 | 276 | 1 | 1.39 pounds | 2025-01-12 1年 5个月 |
| 13 | [B0FLCGYFGS](https://www.amazon.com/dp/B0FLCGYFGS) |  | 256pcs Blue Dog Party Favors | **** / **** | **** | $26.99 | - | 16 / 2 | 4.3 | **** /  | 1 | 137 | 1 | 2.78 pounds | 2025-09-15 8个月 |
| 14 | [B0FC6BTZDC](https://www.amazon.com/dp/B0FC6BTZDC) |  | Quelay 50 Sets Funeral Favors for Guests | **** / **** | **** | $28.99 | - | 17 / 4 | 4.8 | **** /  | 3 | 390 | 1 | 0.93 pounds | 2025-08-02 10个月 |
| 15 | [B0GN2NCTH9](https://www.amazon.com/dp/B0GN2NCTH9) |  | Huwena 24 Sets Quinceanera Party Favor for Guest Recuerdos Para 1… | **** / **** | **** | $33.99 | - | 4 / - | 4.7 | **** /  | 5 | 270 | 1 | 0.79 pounds | 2026-02-14 3个月 |
| 16 | [B0F2MX2NZZ](https://www.amazon.com/dp/B0F2MX2NZZ) |  | 24 Sets Color Your Own Hero Masks DIY Blank Masks Wooden Painting… | **** / **** | **** | $23.99 | - | 13 / - | 5.0 | **** /  | 2 | 310 | 1 | 2.18 pounds | 2025-03-31 1年 2个月 |
| 17 | [B0GQ6YNKTV](https://www.amazon.com/dp/B0GQ6YNKTV) |  | 231PCS Cars Birthday Decorations Set Race Car Birthday Party Deco… | **** / **** | **** | $24.99 | - | 9 / 5 | 4.5 | **** /  | 2 | 370 | 1 | 2.62 pounds | 2026-03-31 2个月 |
| 18 | [B0FHH8884M](https://www.amazon.com/dp/B0FHH8884M) |  | Nosiny 106 Pcs Capybara Party Favors Birthday Decorations Include… | **** / **** | **** | $29.99 | - | 5 / - | 4.4 | **** /  | 5 | 863 | 1 | 1.28 pounds | 2025-07-28 10个月 |
| 19 | [B0FXGPB4CS](https://www.amazon.com/dp/B0FXGPB4CS) |  | 32 Sets Bear Baby Shower Thank You Gifts | **** / **** | **** | $23.99 | - | 4 / 3 | 4.4 | **** /  | 2 | 442 | 1 | 0.9 pounds | 2025-11-20 6个月 |
| 20 | [B0BQV62J5P](https://www.amazon.com/dp/B0BQV62J5P) |  | 122 Pcs Softball Party Favors Softball Gifts for Girls and Boys | **** / **** | **** | $27.99 | - | 97 / 1 | 4.7 | **** /  | 1 | 626 | 1 | 1.74 pounds | 2023-01-08 3年 5个月 |

## 二、完整商品标题

**1. [B0GQTBS8WH](https://www.amazon.com/dp/B0GQTBS8WH)** 24 PCs Kids Keychains, Cute Plush Keychains, Funny Plush Backpack Charms, Perfect for Birthday Gifts, Back-to-School Goodie Bags, Classroom Prizes, Party Favors

**2. [B0GGBHWRQF](https://www.amazon.com/dp/B0GGBHWRQF)** 24Pcs Toy Inspired Story Birthday Party Supplies Reusable Drinking Straws,8 Designs Toy Themed Story Party Favors with 2 Cleaning Brushes

**3. [B0G2RR1NTG](https://www.amazon.com/dp/B0G2RR1NTG)** J6&H6 2026 Soccer Party Favors Soccer Goodie Bags Including 12 Soccer Drawstring Bags Stress-relieving Soccer Straws Keychains silicone Wristband and stickers for Soccer Party Gift. (soccer)

**4. [B0C3HSQ4HK](https://www.amazon.com/dp/B0C3HSQ4HK)** 24 Pcs Inflatable Guitars for Parties Bulk Blow Rock Star Guitar Set Rock and Roll Party Decorations Photo Booth Props for Birthday 80s 90s Themed Party Carnival, 12 Colors

**5. [B0FPQRQJN7](https://www.amazon.com/dp/B0FPQRQJN7)** 12 Set K-pop Party Favors Includes Inflatable Microphones and Heart Sunglasses K-pop Music Theme Party Favors 80s 90s Cosplay Stage Decoration Supplies(Pink, Purple, Blue, Yellow)

**6. [B0FM88PPZW](https://www.amazon.com/dp/B0FM88PPZW)** Axolotl Gifts for Girls, Axolotl Toys with Fluffy Diary, Sticker, and More Stuff - Gifts for Kids 6-8 Year Old, Christmas Birthday for Girls Age 3 4 5 6 7 8 9 10 Years Old

**7. [B0FY36HRX3](https://www.amazon.com/dp/B0FY36HRX3)** SHQDD 46 PCS 4th of July Foam Glow Stick Pack, Red White Blue Glow Sticks, July 4 Party Favors, Light up Party Supplies for Independence Day Celebrations,Glow in the Dark Accessories for Kids & Adults

**8. [B0GGGMZMS9](https://www.amazon.com/dp/B0GGGMZMS9)** WenmthG 40Pcs Teacher Appreciation Gifts Bulk for Women Men Coworker - Thank You Teachers Gifts with Notebooks Pens Keychains Organza Bags - Best Teacher’s Day Graduation End of Year Birthday Gift

**9. [B0F1FZLMV1](https://www.amazon.com/dp/B0F1FZLMV1)** Lunmon 50 Sets Patriotic Rubber Ducks Bulk 4th of July Rubber Ducks Gifts with Red White Blue Cards Organza Bags for Independence Day 250th Anniversary Party Decor

**10. [B0FGJQBGRR](https://www.amazon.com/dp/B0FGJQBGRR)** Hiboom 48 Gone Fishing Party Favors Set 12 Candy Mini Tackle Boxes 12 Fish Cupcake Pole Picks 12 Red White Floater 12 Thank You Cards with Rope Fishing Birthday Cake Decor (5.12 x 2.76 x 0.91 Inch)

**11. [B0G7HHBH8D](https://www.amazon.com/dp/B0G7HHBH8D)** HigzYovn 12-Pack Dr Seu Party Favors Pre-Packaged: Oh The Places You Go Decorations Individually Wrapped Paint Your Own Wooden Magnet Craft Kits with Thank You Card, Kindergarten Graduation

**12. [B0DSPXBGYD](https://www.amazon.com/dp/B0DSPXBGYD)** Hollowfly 24 Sets 2026 Graduation Gifts Graduation Rubber Ducks with Grad Cap Sunglasses Chain, Grad Party Favors Bulk for College Party Decor

**13. [B0FLCGYFGS](https://www.amazon.com/dp/B0FLCGYFGS)** 256pcs Blue Dog Party Favors, Birthday Party Supplies Including Sticky Geckos, Coins, Sunflower Glasses with Cards, Birthday Decorations Gifts Bag Goodies, Classroom Rewards for Kids

**14. [B0FC6BTZDC](https://www.amazon.com/dp/B0FC6BTZDC)** Quelay 50 Sets Funeral Favors for Guests, Mini Rosary Organza Bags Sympathy Thank You Cards Celebration of Life Favors for Memorial Party Supplies Funeral Guest Return Gifts

**15. [B0GN2NCTH9](https://www.amazon.com/dp/B0GN2NCTH9)** Huwena 24 Sets Quinceanera Party Favor for Guest Recuerdos Para 15 Años Quinceañeras Catholic Rosary Necklace Bulk Crucifix Prayer with Faux Pearl Sweet 15th Birthday Religious Gift with Box(Pink)

**16. [B0F2MX2NZZ](https://www.amazon.com/dp/B0F2MX2NZZ)** 24 Sets Color Your Own Hero Masks DIY Blank Masks Wooden Painting Craft Kits Include Beautiful Cards and Art Supplies for Boys Girls Birthday Party Graffiti Crafts Party Favors

**17. [B0GQ6YNKTV](https://www.amazon.com/dp/B0GQ6YNKTV)** 231PCS Cars Birthday Decorations Set Race Car Birthday Party Decorations Kit with Tablecloth, Banner, Plates, Cups, Napkins, Stickers & Slap Bracelets, Car Themed Party Decorations Serves 24

**18. [B0FHH8884M](https://www.amazon.com/dp/B0FHH8884M)** Nosiny 106 Pcs Capybara Party Favors Birthday Decorations Include Capybara 4 in 1 Ballpoint Pens Keychain Sticky Note Resin Figurines Stickers Organza Bags for Goodies Bags Stuff Party Rewards

**19. [B0FXGPB4CS](https://www.amazon.com/dp/B0FXGPB4CS)** 32 Sets Bear Baby Shower Thank You Gifts, Vintage Pooh Baby Shower Party Favors, Winnie Acrylic Keychains for Guests, Winnie Favors with Thank You Card, Winnie Party Decoration, 8 Styles

**20. [B0BQV62J5P](https://www.amazon.com/dp/B0BQV62J5P)** 122 Pcs Softball Party Favors Softball Gifts for Girls and Boys, Include Softball Bracelet Drawstring Softball Bag Foam Mini Softball Ball Hair Ties Button Badges and Softball Stickers for Team

## 三、尚未分析的候选类目（共 11 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Electrical System Tools | 电气系统工具 | `Automotive > Tools & Equipment > Electrical System Tools` |
| 2 | Brake System Bleeding Tools | 刹车排气 | `Automotive > Tools & Equipment > Brake Tools > Brake System Bleeding Tools` |
| 3 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 4 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 5 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 6 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 7 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 8 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 9 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 10 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 11 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 11 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0GQTBS8WH`: 31,680 | 6,491 | 17% | 780 | 172.02% | $17,152 | 800+ | $17K+ | 1 | $21.99 | - | 38 | 9 | 4.7 | 1.15% | $5.76 | 59% | 2026-03-30 | 2个月 | FBA | -
- `B0GGBHWRQF`: 55,491 | 23,911 | 30% | 479 | 108.8% | $14,365 | 400+ | $10K+ | 1 | $29.99 | - | 34 | 7 | 5.0 | 1.46% | $5.61 | 66% | 2026-02-12 | 4个月 | FBA | -
- `B0G2RR1NTG`: 60,458 | 5,390 | 8% | 568 | 30.2% | $14,194 | 200+ | $4K+ | 4 | $24.99 | - | 37 | 11 | 4.9 | 1.94% | $6.34 | 60% | 2025-12-24 | 5个月 | FBA | -
- `B0C3HSQ4HK`: 84,656 | 29,818 | 27% | 428 | 30.11% | $12,836 | 200+ | $5K+ | 5 | $29.99 | - | 141 | 3 | 4.2 | 0.7% | $6.76 | 62% | 2023-04-27 | 3年 1个月 | FBA | -
- `B0FPQRQJN7`: 73,390 | 24,342 | 25% | 408 | 45.85% | $11,828 | 100+ | $2K+ | 4 | $28.99 | - | 19 | 7 | 4.8 | 1.72% | $4.76 | 69% | 2025-09-05 | 9个月 | FBA | -
- `B0FM88PPZW`: 71,290 | 9,466 | 12% | 418 | 17.38% | $11,282 | 300+ | $8K+ | 1 | $26.99 | - | 50 | 7 | 4.8 | 1.67% | $6.48 | 61% | 2025-09-30 | 8个月 | FBA | -
- `B0FY36HRX3`: 84,617 | 3,147 | 4% | 258 | 144.64% | $9,801 | 200+ | $6K+ | 1 | $33.26 | - | 21 | 1 | 4.8 | 0.39% | $9.22 | 61% | 2026-02-01 | 4个月 | FBA | -
- `B0GGGMZMS9`: 99,828 | 11,100 | 10% | 376 | 192.25% | $8,644 | 100+ | $2K+ | 3 | $22.99 | - | 16 | 10 | 4.6 | 2.66% | $6.13 | 58% | 2026-01-15 | 4个月 | FBA | -
- `B0F1FZLMV1`: 134,835 | 48,521 | 26% | 198 | 96.1% | $7,720 | 100+ | $3K+ | 3 | $38.99 | - | 19 | 2 | 4.6 | 1.01% | $7.55 | 66% | 2025-03-31 | 1年 2个月 | FBA | -
- `B0FGJQBGRR`: 130,923 | 32,003 | 20% | 237 | 108.26% | $6,160 | 100+ | $2K+ | 2 | $25.99 | - | 22 | 3 | 4.1 | 1.27% | $5.76 | 63% | 2025-07-06 | 11个月 | FBA | -
- `B0G7HHBH8D`: 157,143 | 65,444 | 29% | **** | **** | **** | **** | 1 | $20.99 | - | 5 | - | 5.0 | - | **** | 2026-02-08 | 4个月 | FBA | -
- `B0DSPXBGYD`: 223,907 | 0 | 0% | **** | **** | **** | **** | 3 | $30.99 | - | 26 | - | 4.8 | - | **** | 2025-01-12 | 1年 5个月 | FBA | -
- `B0FLCGYFGS`: 130,616 | 63,545 | 33% | **** | **** | **** | **** | 1 | $26.99 | - | 16 | 2 | 4.3 | 1.2% | **** | 2025-09-15 | 8个月 | FBA | -
- `B0FC6BTZDC`: 224,566 | 24,722 | 10% | **** | **** | **** | **** | 3 | $28.99 | - | 17 | 4 | 4.8 | 2.67% | **** | 2025-08-02 | 10个月 | FBA | -
- `B0GN2NCTH9`: 215,896 | 82,280 | 23% | **** | **** | **** | **** | 5 | $33.99 | - | 4 | - | 4.7 | - | **** | 2026-02-14 | 3个月 | FBA | -
- `B0F2MX2NZZ`: 191,752 | 4,195 | 2% | **** | **** | **** | **** | 2 | $23.99 | - | 13 | - | 5.0 | - | **** | 2025-03-31 | 1年 2个月 | FBA | -
- `B0GQ6YNKTV`: 171,185 | 160,284 | 48% | **** | **** | **** | **** | 2 | $24.99 | - | 9 | 5 | 4.5 | 3.47% | **** | 2026-03-31 | 2个月 | FBA | -
- `B0FHH8884M`: 478,829 | 5,406 | 1% | **** | **** | **** | **** | 5 | $29.99 | - | 5 | - | 4.4 | - | **** | 2025-07-28 | 10个月 | FBA | -
- `B0FXGPB4CS`: 210,962 | 84,014 | 28% | **** | **** | **** | **** | 2 | $23.99 | - | 4 | 3 | 4.4 | 2.24% | **** | 2025-11-20 | 6个月 | FBA | -
- `B0BQV62J5P`: 401,855 | 18,733 | 5% | **** | **** | **** | **** | 1 | $27.99 | 2 | 97 | 1 | 4.7 | 0.9% | **** | 2023-01-08 | 3年 5个月 | FBA | -

---

<!-- source: products/nozzles.md -->
# Nozzles 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles`
> 共抓取 **0** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $26.21　均Reviews 488（中等）　重量 0.42lbs（轻）　退货率 2.63%（低）　品牌集中度 54.8%（中等）　中国卖家 73.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|

## 二、完整商品标题

## 三、尚未分析的候选类目（共 13 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Cardboard Cutouts | 硬板纸模型 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Cardboard Cutouts` |
| 2 | Multi-Item Party Favor Packs | 多项目派对礼包 | `Home & Kitchen > Event & Party Supplies > Favors > Multi-Item Party Favor Packs` |
| 3 | Electrical System Tools | 电气系统工具 | `Automotive > Tools & Equipment > Electrical System Tools` |
| 4 | Brake System Bleeding Tools | 刹车排气 | `Automotive > Tools & Equipment > Brake Tools > Brake System Bleeding Tools` |
| 5 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 6 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 7 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 8 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 9 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 10 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 11 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 12 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 13 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 13 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

---

<!-- source: products/paddleboard_accessories.md -->
# Paddleboard Accessories 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories`
> 共抓取 **7** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **7** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $52.63　均Reviews 326（中等）　重量 2.37lbs（重）　退货率 4.17%（低）　品牌集中度 42.9%（中等）　中国卖家 73.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0D2HDB38D](https://www.amazon.com/dp/B0D2HDB38D) |  | Paddle Board Cooler | 304 / 107.45% | $12,154 | $39.98 | $6.10 (15%) | 116 / 6 | 4.6 | $7.89 / 65% | 2 | 62 | 1 | 2.84 pounds | 2024-05-29 2年 |
| 2 | [B07GCQZZP1](https://www.amazon.com/dp/B07GCQZZP1) |  | Repair Kit with HH-66 Vinyl Cement Glue (or Without Glue) for Inf… | 179 / 35.56% | $7,151 | $39.95 | $5.86 (15%) | 20 / 1 | 4.6 | $4.93 / 73% | 1 | 108 | 1 | 0.4 pounds | 2023-12-27 2年 5个月 |
| 3 | [B0GL11PYLB](https://www.amazon.com/dp/B0GL11PYLB) |  | YEEGO DIRECT Paddle Board Cooler Waterproof,50L Double Deck Insul… | 135 / 181.4% | $6,749 | $49.99 | $7.36 (15%) | 5 / - | 5.0 | $12.64 / 60% | 1 | 131 | 1 | 2.58 pounds | 2026-03-25 2个月 |
| 4 | [B0CXSFHCP8](https://www.amazon.com/dp/B0CXSFHCP8) |  | Paddle Board Cooler | 151 / 24.36% | $6,038 | $39.99 | $6.09 (15%) | 139 / 1 | 4.6 | $8.31 / 64% | 4 | 180 | 1 | 3.24 pounds | 2024-05-29 2年 |
| 5 | [B0DSZKQTNC](https://www.amazon.com/dp/B0DSZKQTNC) |  | Waterproof Paddle Board Cooler | 146 / 48.15% | $5,839 | $39.99 | $6.01 (15%) | 86 / 1 | 4.6 | $8.39 / 64% | 1 | 123 | 1 | 2.67 pounds | 2025-02-07 1年 4个月 |
| 6 | [B0FB423WBC](https://www.amazon.com/dp/B0FB423WBC) |  | Paddle Board Cooler Waterproof,26L SUP Paddleboard Cooler Deck Ba… | 161 / 45.65% | $4,828 | $29.99 | $4.42 (15%) | 51 / - | 4.2 | $7.88 / 59% | 2 | 122 | 1 | 2.58 pounds | 2025-07-16 10个月 |
| 7 | [B0F43J7ZKL](https://www.amazon.com/dp/B0F43J7ZKL) |  | niphean SUP Carrying Strap | 147 / 97.4% | $4,115 | $27.99 | $4.33 (15%) | 71 / - | 4.4 | $4.35 / 69% | 5 | 149 | 1 | 0.68 pounds | 2025-05-14 1年 |

## 二、完整商品标题

**1. [B0D2HDB38D](https://www.amazon.com/dp/B0D2HDB38D)** Paddle Board Cooler - Waterproof SUP Cooler Bag for Stand Up Paddle Board and Kayak - Leakproof Inflatable Cooler for SUP Accessories - Essential Paddleboard Accessory for Water Storage

**2. [B07GCQZZP1](https://www.amazon.com/dp/B07GCQZZP1)** Repair Kit with HH-66 Vinyl Cement Glue (or Without Glue) for Inflatable Stand Up Paddle Boards (SUP) Includes 3" x 6" Red, White, Blue, Clear, Grey PVC, 5 Patches and 6 Prong Valve Wrench

**3. [B0GL11PYLB](https://www.amazon.com/dp/B0GL11PYLB)** YEEGO DIRECT Paddle Board Cooler Waterproof,50L Double Deck Insulated SUP Cooler Fits 50 Cans,Detachable Bottle Opener,Ice Chest & Cooler Seat, Water Sports Accessories for Kayaking Beach Camping

**4. [B0CXSFHCP8](https://www.amazon.com/dp/B0CXSFHCP8)** Paddle Board Cooler, Paddleboard Cooler Deck Bag with Detachable Bottle Opener, Paddle Board Accessories, Sup Cooler Bag for Beach, Camping, Kayaking, Travel

**5. [B0DSZKQTNC](https://www.amazon.com/dp/B0DSZKQTNC)** Waterproof Paddle Board Cooler, Upgraded Hard Bottom Paddleboard Cooler Deck Bag with Adjustable Strap, Bottle Opener, SUP Kayak Cooler Fits 30 Cans for Paddleboarding, Kayaking, Camping

**6. [B0FB423WBC](https://www.amazon.com/dp/B0FB423WBC)** Paddle Board Cooler Waterproof,26L SUP Paddleboard Cooler Deck Bag fits 42 Cans,2 Compartments Paddle Board Accessories for Kayaking,Beach, Camping(Blue)

**7. [B0F43J7ZKL](https://www.amazon.com/dp/B0F43J7ZKL)** niphean SUP Carrying Strap, Paddle Board Accessories for Inflatable Paddle Board, Adjustable Shoulder Strap for Paddleboard

## 三、尚未分析的候选类目（共 4 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 2 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 3 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 4 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 4 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0D2HDB38D`: 21,296 | 4,595 | 17% | 304 | 107.45% | $12,154 | 100+ | $3K+ | 2 | $39.98 | - | 116 | 6 | 4.6 | 1.97% | $7.89 | 65% | 2024-05-29 | 2年 | FBA | -
- `B07GCQZZP1`: 44,369 | 11,992 | 21% | 179 | 35.56% | $7,151 | 100+ | $3K+ | 1 | $39.95 | - | 20 | 1 | 4.6 | 0.56% | $4.93 | 73% | 2023-12-27 | 2年 5个月 | FBA | -
- `B0GL11PYLB`: 54,849 | 0 | 0% | 135 | 181.4% | $6,749 | 100+ | $4K+ | 1 | $49.99 | - | 5 | - | 5.0 | - | $12.64 | 60% | 2026-03-25 | 2个月 | FBA | -
- `B0CXSFHCP8`: 13,602 | 45,026 | 77% | 151 | 24.36% | $6,038 | - | - | 4 | $39.99 | - | 139 | 1 | 4.6 | 0.66% | $8.31 | 64% | 2024-05-29 | 2年 | FBA | -
- `B0DSZKQTNC`: 51,630 | 726 | 1% | 146 | 48.15% | $5,839 | 100+ | $3K+ | 1 | $39.99 | - | 86 | 1 | 4.6 | 0.68% | $8.39 | 64% | 2025-02-07 | 1年 4个月 | FBA | -
- `B0FB423WBC`: 52,130 | 0 | 0% | 161 | 45.65% | $4,828 | 50+ | $1K+ | 2 | $29.99 | - | 51 | - | 4.2 | - | $7.88 | 59% | 2025-07-16 | 10个月 | FBA | -
- `B0F43J7ZKL`: 55,019 | 0 | 0% | 147 | 97.4% | $4,115 | - | - | 5 | $27.99 | - | 71 | - | 4.4 | - | $4.35 | 69% | 2025-05-14 | 1年 | FBA | -

---

<!-- source: products/scan_principles.md -->
# 选品原则 (2026-06-13)

本文件由批量产品扫描自动生成，同批次所有品类报告共享同一套筛选条件。

本次产品扫描依据以下量化条件筛选候选商品，每项条件均有明确的选品逻辑：

- **月销量最小值** ≥/≤/= `100`　*确保产品有稳定市场需求，低于此销量视为市场过小*
- **月销量最大值** ≥/≤/= `1000`　*避开竞争过于激烈的大爆款，聚焦中等规模机会*
- **月销量增长率最小值（百分比）** ≥/≤/= `5`
- **月销量增长率最大值（百分比；排除低基数异常暴增）** ≥/≤/= `200`
- **近 7 天大类 BSR 排名改善率最小值（百分比；正数表示改善）** ≥/≤/= `0`
- **变体数最小值** ≥/≤/= `1`　*排除变体结构过于单一的产品*
- **变体数最大值** ≥/≤/= `5`　*变体过多会拉高库存管理复杂度和资金占用*
- **价格最小值（美元）** ≥/≤/= `20`　*低价品利润薄、运营容错率低，过滤不符合要求的产品*
- **价格最大值（美元）** ≥/≤/= `60`　*客单价过高会拉长消费者决策周期并增加资金压力*
- **评分数最大值** ≥/≤/= `150`　*评价数低说明竞争护城河浅，新卖家仍有进入机会*
- **评分最小值** ≥/≤/= `4`　*过滤质量差评产品，只关注消费者认可的品类*
- **评分最大值** ≥/≤/= `5`　*评分上限（通常无需限制，保留作兜底）*
- **毛利率最小值（百分比）** ≥/≤/= `50`　*确保覆盖 FBA 费用、广告成本后仍有合理利润空间*
- **包装重量最大值（克）** ≥/≤/= `1500`　*重量直接决定 FBA 头程和月租费，轻量化是新卖家核心竞争力*
- **卖家数量最小值** ≥/≤/= `1`　*至少有一家卖家说明品类已有验证，排除无人做的死角*
- **卖家数量最大值** ≥/≤/= `2`　*卖家少说明市场未饱和，存在空白或新兴机会*
- **配送方式** ≥/≤/= `FBA`　*FBA 配送是新卖家标准模式，确保物流体验和搜索权重*

---

<!-- source: products/swing_trainers.md -->
# Swing Trainers 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $36.27　均Reviews 447（中等）　重量 0.71lbs（轻）　退货率 4.37%（低）　品牌集中度 57.8%（中等）　中国卖家 69.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GHNCYS4W](https://www.amazon.com/dp/B0GHNCYS4W) |  | Golf Alignment Sticks Holder | 435 / 17.73% | $13,046 | $29.99 | $4.62 (15%) | 27 / 5 | 4.6 | $6.18 / 64% | 1 | 42 | 1 | 2.45 pounds | 2026-02-12 4个月 |
| 2 | [B0GJGFVXVH](https://www.amazon.com/dp/B0GJGFVXVH) |  | Connector Golf Swing Trainer for Posture Correction and Arm Align… | 195 / 28.57% | $7,213 | $36.99 | $5.43 (15%) | 11 / 1 | 4.9 | $7.15 / 66% | 1 | 92 | 1 | 1.28 pounds | 2026-03-21 2个月 |
| 3 | [B0FXWTDY16](https://www.amazon.com/dp/B0FXWTDY16) |  | The Connector Golf Training Aid | 132 / 18.89% | $5,147 | $38.99 | $5.69 (15%) | 13 / 2 | 4.4 | $7.96 / 65% | 1 | 125 | 1 | 1.28 pounds | 2025-12-17 5个月 |
| 4 | [B0DCX6FR3P](https://www.amazon.com/dp/B0DCX6FR3P) |  | Tour Aim + Alignment Stick Adapter | 120 / 39.6% | $4,794 | $39.95 | $5.90 (15%) | 39 / 1 | 4.1 | $4.09 / 75% | 1 | 292 | 2 | 0.22 pounds | 2024-08-13 1年 10个月 |

## 二、完整商品标题

**1. [B0GHNCYS4W](https://www.amazon.com/dp/B0GHNCYS4W)** Golf Alignment Sticks Holder, Golf Training Aid with Alignment Sticks & Protective Padding, Swing Trainer Practice Teaching Aid Driving Range for Aiming, Putting, Swing, Golf Gifts for Men Women

**2. [B0GJGFVXVH](https://www.amazon.com/dp/B0GJGFVXVH)** Connector Golf Swing Trainer for Posture Correction and Arm Alignment, Golf Training Aid for Proper Swing Mechanics, Golf Swing Ball Training, Golf Connector Ball Practice, All Skill Levels

**3. [B0FXWTDY16](https://www.amazon.com/dp/B0FXWTDY16)** The Connector Golf Training Aid - Golf Swing Trainer Aid for Posture Correction Practice, Suitable for Golfers of All Levels Looking to Improve Overall Game

**4. [B0DCX6FR3P](https://www.amazon.com/dp/B0DCX6FR3P)** Tour Aim + Alignment Stick Adapter — Perfect Your Aim, Alignment, Face Angle, and Ball Position. Use Real Golf Tees of Mats.

## 三、尚未分析的候选类目（共 15 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Lighting Products | 水底灯 | `Patio, Lawn & Garden > Pools, Hot Tubs & Supplies > Parts & Accessories > Lighting Products` |
| 2 | Nozzles | 喷嘴 | `Patio, Lawn & Garden > Outdoor Power Tools > Replacement Parts & Accessories > Pressure Washer Parts & Accessories > Nozzles` |
| 3 | Cardboard Cutouts | 硬板纸模型 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Cardboard Cutouts` |
| 4 | Multi-Item Party Favor Packs | 多项目派对礼包 | `Home & Kitchen > Event & Party Supplies > Favors > Multi-Item Party Favor Packs` |
| 5 | Electrical System Tools | 电气系统工具 | `Automotive > Tools & Equipment > Electrical System Tools` |
| 6 | Brake System Bleeding Tools | 刹车排气 | `Automotive > Tools & Equipment > Brake Tools > Brake System Bleeding Tools` |
| 7 | Trophies | 奖杯 | `Sports & Outdoors > Sports & Outdoor Recreation Accessories > Trophies, Medals & Awards > Trophies` |
| 8 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 9 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 10 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 11 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 12 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 13 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 14 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 15 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 15 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0GHNCYS4W`: 16,191 | 14,093 | 47% | 435 | 17.73% | $13,046 | 400+ | $11K+ | 1 | $29.99 | - | 27 | 5 | 4.6 | 1.15% | $6.18 | 64% | 2026-02-12 | 4个月 | FBA | -
- `B0GJGFVXVH`: 31,592 | 3,174 | 9% | 195 | 28.57% | $7,213 | 100+ | $3K+ | 1 | $36.99 | - | 11 | 1 | 4.9 | 0.51% | $7.15 | 66% | 2026-03-21 | 2个月 | FBA | -
- `B0FXWTDY16`: 38,140 | 19,139 | 33% | 132 | 18.89% | $5,147 | 100+ | $3K+ | 1 | $38.99 | - | 13 | 2 | 4.4 | 1.52% | $7.96 | 65% | 2025-12-17 | 5个月 | FBA | -
- `B0DCX6FR3P`: 66,033 | 11,438 | 14% | 120 | 39.6% | $4,794 | 50+ | $1K+ | 1 | $39.95 | - | 39 | 1 | 4.1 | 0.83% | $4.09 | 75% | 2024-08-13 | 1年 10个月 | FBA | -

---

<!-- source: products/trophies.md -->
# Trophies 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $25.32　均Reviews 297（低竞争）　重量 1.01lbs（轻）　退货率 2.59%（低）　品牌集中度 48.8%（中等）　中国卖家 48.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DJT1YH6F](https://www.amazon.com/dp/B0DJT1YH6F) |  | Vitality Sports Golf Chipping Net | 999 / 27.16% | $45,924 | $45.97 | $7.02 (15%) | 106 / 7 | 4.6 | $7.23 / 69% | 2 | 3 | 2 | 3.24 pounds | 2024-11-07 1年 7个月 |
| 2 | [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT) |  | Suspension Straps Trainer with Built-in Door Anchor | 855 / 7.98% | $42,741 | $49.99 | $7.69 (15%) | 101 / 21 | 4.6 | $6.31 / 72% | 1 | 4 | 1 | 2.31 pounds | 2025-06-07 1年 |
| 3 | [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3) |  | Boat Stern Light Anchor Light | 857 / 29.64% | $36,842 | $42.99 | $6.66 (15%) | 30 / 13 | 4.9 | $10.11 / 61% | 3 | 14 | 1 | 1.25 pounds | 2026-03-31 2个月 |
| 4 | [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q) |  | SILCA Ultimate Sealant Bottle | 749 / 7.13% | $33,698 | $44.99 | $6.57 (15%) | 140 / - | 4.5 | $6.48 / 71% | 4 | 19 | 1 | 2.51 pounds | 2025-02-16 1年 3个月 |
| 5 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 789 / 11.11% | $31,552 | $39.99 | $5.91 (15%) | 110 / 13 | 4.7 | $4.09 / 75% | 4 | 19 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 6 | [B0G93DF8CJ](https://www.amazon.com/dp/B0G93DF8CJ) |  | Exun Soccer Fan Gift Basket Set 2026 | 1,000 / 102.84% | $29,990 | $29.99 | $4.37 (15%) | 58 / 16 | 4.8 | $6.13 / 65% | 1 | 163 | 1 | 1.87 pounds | 2026-02-20 3个月 |
| 7 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 8 | [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP) |  | Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner | 890 / 34.88% | $28,471 | $31.99 | $4.87 (15%) | 118 / 4 | 4.5 | $4.09 / 72% | 3 | 7 | 1 | 0.29 pounds | 2024-02-06 2年 4个月 |
| 9 | [B0DRFSFCYQ](https://www.amazon.com/dp/B0DRFSFCYQ) |  | Telescoping Boat Hook for Docking | 678 / 103.33% | $28,469 | $41.99 | $6.11 (15%) | 138 / 13 | 4.6 | $12.37 / 56% | 2 | 5 | 1 | 2.65 pounds | 2025-01-26 1年 4个月 |
| 10 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 740 / 54.21% | $28,113 | $37.99 | $5.64 (15%) | 127 / 7 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 11 | [B0FV8M2Y78](https://www.amazon.com/dp/B0FV8M2Y78) |  | A2C Original Fold-Magnet Golf Cart Phone Holder with Rangefinder… | **** / **** | **** | $39.99 | - | 51 / 11 | 4.3 | **** /  | 1 | 60 | 1 | 0.55 pounds | 2026-01-19 4个月 |
| 12 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | **** / **** | **** | $35.99 | - | 125 / 37 | 4.6 | **** /  | 3 | 64 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 13 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 14 | [B0G48PCVTH](https://www.amazon.com/dp/B0G48PCVTH) |  | CVLIFE WolfCloak Motion Awake Red Dot Sight for RMR Footprint | **** / **** | **** | $59.99 | - | 30 / 8 | 4.1 | **** /  | 1 | 12 | 1 | 0.44 pounds | 2026-03-11 3个月 |
| 15 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 85 / 15 | 4.5 | **** /  | 1 | 22 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 16 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 6 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 2个月 |
| 17 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 18 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 19 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |
| 20 | [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64) |  | GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men | **** / **** | **** | $49.99 | - | 97 / - | 4.5 | **** /  | 5 | 19 | 1 | 1.3 pounds | 2025-03-28 1年 2个月 |

## 二、完整商品标题

**1. [B0DJT1YH6F](https://www.amazon.com/dp/B0DJT1YH6F)** Vitality Sports Golf Chipping Net, 3PCS Pop-Up Golf Practice Net for Backyard, Indoor Outdoor Chipping Game with 3 Targets, 1 Hitting Mat, 20 Balls, Tee Box

**2. [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT)** Suspension Straps Trainer with Built-in Door Anchor, All-in-One Bodyweight Training System for Home & Outdoor Use - Quick Setup in 1 Second

**3. [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3)** Boat Stern Light Anchor Light, 28"-48" Telescoping Pole Boat Lights LED with Base & Extra Bulb, Waterproof 3NM 360° All Round Marine Navigation Lights for Boats LED for Pontoon, Fishing, Bass Boats

**4. [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q)** SILCA Ultimate Sealant Bottle | injectable Fiber Foam

**5. [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP)** Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically Designed Human Fish Hook Removal Tool.

**6. [B0G93DF8CJ](https://www.amazon.com/dp/B0G93DF8CJ)** Exun Soccer Fan Gift Basket Set 2026 – 9 Piece Sports Accessories Bundle with Stainless Steel Tumbler, Towel, Keychain, Hat, Wristband & Metal Pin – Triple Nation Flag Design, World Soccer Lover Gift

**7. [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL)** Sea to Summit eVac Dry Bag, Roll-Top Compression Sack, 35 Liter, Turkish Tile Blue

**8. [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP)** Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner, Lightweight Adult Sleep Sack & Travel Sheets for Backpacking, Hotel, Camping, Hostels, ZY20

**9. [B0DRFSFCYQ](https://www.amazon.com/dp/B0DRFSFCYQ)** Telescoping Boat Hook for Docking, Non-Slip Rubber Tip, 3-Stage Anodized Aluminum Pole, Floating, Lightweight & Durable, Scratch-Resistant & Rustproof, 3/4" Threaded End for Push Pull Boating

**10. [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT)** 75FT Wakeboard Rope and Handle, Floating Water Ski Rope for Watersports, 4 Sections Ski Ropes for Water Skiing, Kneeboarding, Wakeboarding

**11. [B0FV8M2Y78](https://www.amazon.com/dp/B0FV8M2Y78)** A2C Original Fold-Magnet Golf Cart Phone Holder with Rangefinder Mount, CNC Aircraft-Grade Aluminum Alloy, Premium Fathers Day Golf Gifts for Men Dad Him Women, Golf Accessories Essentials Gadgets

**12. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**13. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**14. [B0G48PCVTH](https://www.amazon.com/dp/B0G48PCVTH)** CVLIFE WolfCloak Motion Awake Red Dot Sight for RMR Footprint, 2 MOA Reflex Sight with 0.33" Ultra-Low Profile for Full-Sized Pistols, 1500G Shockproof Optic, Adapter for Glock MOS and 21mm Picatinny

**15. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**16. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**17. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**18. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**19. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

**20. [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64)** GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men, Natural Rattan Wicker Bike Baskets for Adult Bikes, Basket for Bikes with Liner, Bicycle Baskets for Beach Cruiser

## 三、尚未分析的候选类目（共 8 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Grinding Discs | 磨片 | `Industrial & Scientific > Abrasive & Finishing Products > Abrasive Wheels & Discs > Grinding Discs` |
| 2 | Compressed Air Dusters | 压缩除尘罐 | `Electronics > Computers & Accessories > Computer Accessories & Peripherals > Cleaning & Repair > Compressed Air Dusters` |
| 3 | Wind Spinners | Wind Spinners | `Patio, Lawn & Garden > Outdoor Décor > Garden Sculptures & Statues > Wind Sculptures & Spinners > Wind Spinners` |
| 4 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 5 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 6 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 7 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 8 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 8 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0DJT1YH6F`: 6,744 | 1,208 | 15% | 999 | 27.16% | $45,924 | 700+ | $27K+ | 2 | $45.97 | - | 106 | 7 | 4.6 | 0.7% | $7.23 | 69% | 2024-11-07 | 1年 7个月 | FBA | -
- `B0F5BD54RT`: 10,137 | 2,307 | 19% | 855 | 7.98% | $42,741 | 700+ | $34K+ | 1 | $49.99 | - | 101 | 21 | 4.6 | 2.46% | $6.31 | 72% | 2025-06-07 | 1年 | FBA | -
- `B0GKMGJLL3`: 10,780 | 2,090 | 16% | 857 | 29.64% | $36,842 | 600+ | $25K+ | 3 | $42.99 | - | 30 | 13 | 4.9 | 1.52% | $10.11 | 61% | 2026-03-31 | 2个月 | FBA | -
- `B0DX2F3V5Q`: 11,637 | 0 | 0% | 749 | 7.13% | $33,698 | 300+ | $13K+ | 4 | $44.99 | - | 140 | - | 4.5 | - | $6.48 | 71% | 2025-02-16 | 1年 3个月 | FBA | -
- `B0DTP76XQP`: 10,207 | 353 | 3% | 789 | 11.11% | $31,552 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 13 | 4.7 | 1.65% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0G93DF8CJ`: 4,786 | 3,333 | 41% | 1,000 | 102.84% | $29,990 | 900+ | $27K+ | 1 | $29.99 | - | 58 | 16 | 4.8 | 1.6% | $6.13 | 65% | 2026-02-20 | 3个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0CTQTYVGP`: 8,500 | 227 | 3% | 890 | 34.88% | $28,471 | 400+ | $12K+ | 3 | $31.99 | - | 118 | 4 | 4.5 | 0.45% | $4.09 | 72% | 2024-02-06 | 2年 4个月 | FBA | -
- `B0DRFSFCYQ`: 13,590 | 25 | 0% | 678 | 103.33% | $28,469 | 500+ | $20K+ | 2 | $41.99 | - | 138 | 13 | 4.6 | 1.92% | $12.37 | 56% | 2025-01-26 | 1年 4个月 | FBA | -
- `B0DS2CBVFT`: 8,379 | 2,034 | 20% | 740 | 54.21% | $28,113 | 300+ | $11K+ | 5 | $37.99 | - | 127 | 7 | 4.8 | 0.95% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0FV8M2Y78`: 10,613 | 960 | 8% | **** | **** | **** | **** | 1 | $39.99 | - | 51 | 11 | 4.3 | 1.54% | **** | 2026-01-19 | 4个月 | FBA | -
- `B0GL785GSP`: 13,539 | 268 | 2% | **** | **** | **** | **** | 3 | $35.99 | - | 125 | 37 | 4.6 | 5.05% | **** | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0G48PCVTH`: 26,514 | 566 | 2% | **** | **** | **** | **** | 1 | $59.99 | - | 30 | 8 | 4.1 | 1.83% | **** | 2026-03-11 | 3个月 | FBA | -
- `B0F9ZZ17Z8`: 13,699 | 581 | 4% | **** | **** | **** | **** | 1 | $41.97 | - | 85 | 15 | 4.5 | 2.42% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0CT5MVCFD`: 14,494 | 8,366 | 37% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 6 | 4.8 | 1.14% | **** | 2024-03-14 | 2年 2个月 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -
- `B0DS23SX64`: 15,152 | 0 | 0% | **** | **** | **** | **** | 5 | $49.99 | - | 97 | - | 4.5 | - | **** | 2025-03-28 | 1年 2个月 | FBA | -

---

<!-- source: products/wind_spinners.md -->
# Wind Spinners 合格产品扫描 (2026-06-13)

> **所在品类路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $31.29　均Reviews 468（中等）　重量 2.35lbs（重）　退货率 3.09%（低）　品牌集中度 54.8%（中等）　中国卖家 86.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GHQMHRWW](https://www.amazon.com/dp/B0GHQMHRWW) |  | Stainless Steel Bird Deterrents for Outside Patio | 382 / 13.6% | $9,546 | $24.99 | $3.71 (15%) | 24 / - | 4.6 | $3.54 / 71% | 1 | 78 | 1 | 0.2 pounds | 2026-03-25 2个月 |
| 2 | [B0FQJVPZ4B](https://www.amazon.com/dp/B0FQJVPZ4B) |  | 10 Pack 8 Inch Sublimation Wind Spinner Blanks Aluminum Metal Win… | 253 / 22.68% | $6,575 | $25.99 | $3.86 (15%) | 67 / 10 | 4.6 | $6.02 / 62% | 2 | 104 | 1 | 1.79 pounds | 2025-10-22 7个月 |
| 3 | [B0FJ5YYQZ4](https://www.amazon.com/dp/B0FJ5YYQZ4) |  | 360 Degree Double Blade Metal Wind Spinner for Patio | 154 / 11.64% | $5,542 | $35.99 | $5.34 (15%) | 77 / 8 | 4.0 | $6.18 / 68% | 5 | 92 | 1 | 2.29 pounds | 2025-09-03 9个月 |
| 4 | [B0CXCCWQKX](https://www.amazon.com/dp/B0CXCCWQKX) |  | 10 PCS Sublimation Wind Spinner Blanks 3D Aluminum Wind Spinners… | 104 / 12.05% | $3,847 | $36.99 | $5.68 (15%) | 65 / 1 | 4.8 | $6.90 / 66% | 2 | 257 | 1 | 2.93 pounds | 2024-04-10 2年 2个月 |
| 5 | [B0GGGPCFND](https://www.amazon.com/dp/B0GGGPCFND) |  | Hummingbird Mandala Wind Spinner for Mother's Day | 137 / 10.1% | $3,150 | $22.99 | $3.46 (15%) | 40 / 5 | 4.7 | $3.44 / 70% | 3 | 86 | 1 | 0.04 pounds | 2026-03-01 3个月 |

## 二、完整商品标题

**1. [B0GHQMHRWW](https://www.amazon.com/dp/B0GHQMHRWW)** Stainless Steel Bird Deterrents for Outside Patio, Reflective 3D Bird Scare Devices Wind Spinners Outdoor Decor, Woodpecker Deterrent Bird Reflectors to Keep Pigeon Crow Away House Yard Window, Round

**2. [B0FQJVPZ4B](https://www.amazon.com/dp/B0FQJVPZ4B)** 10 Pack 8 Inch Sublimation Wind Spinner Blanks Aluminum Metal Wind Spinners Sublimation Blanks 8 Inch for Indoor and Outdoor Ornaments

**3. [B0FJ5YYQZ4](https://www.amazon.com/dp/B0FJ5YYQZ4)** 360 Degree Double Blade Metal Wind Spinner for Patio, Lawn & Garden (Copper 53 * 12 inch)

**4. [B0CXCCWQKX](https://www.amazon.com/dp/B0CXCCWQKX)** 10 PCS Sublimation Wind Spinner Blanks 3D Aluminum Wind Spinners 10 Inch Hanging Wind Spinners Indoor Outdoor Spinner Suspension Decoration Yard Garden,Halloween Sublimation Blanks

**5. [B0GGGPCFND](https://www.amazon.com/dp/B0GGGPCFND)** Hummingbird Mandala Wind Spinner for Mother's Day, IDEA SHOW 12In 3D Kinetic Metal Wind Spinners, Hummingbird Gift for Women, Mom, Garden Decor Outdoor/Indoor Decoration, Dynamic Art Hanging Sculpture

## 三、尚未分析的候选类目（共 5 个）

以下类目在市场扫描中被标记为绿色或黄色推荐，但本次产品扫描**未覆盖**。统一流水线会继续扫描剩余动态候选类目；如单独调试阶段脚本，可使用 `find_products.py --categories-file` 批量扫描。

| 序号 | 英文名称 | 中文名称 | 完整路径 |
| ---: | --- | --- | --- |
| 1 | Paddleboard Accessories | 冲浪板配件 | `Sports & Outdoors > Sports > Water Sports > Stand-Up Paddleboarding > Paddleboard Accessories` |
| 2 | Batteries & Battery Chargers | 电池和电池 | `Sports & Outdoors > Sports > Skates, Skateboards & Scooters > Scooters & Equipment > Components & Parts > Batteries & Battery Chargers` |
| 3 | Decorative Trays | 装饰性托盘 | `Home & Kitchen > Home Décor Products > Home Décor Accents > Decorative Accessories > Decorative Trays` |
| 4 | Game Mats & Boards | 游戏垫和游戏板 | `Toys & Games > Games & Accessories > Game Accessories > Game Mats & Boards` |
| 5 | Boats | 船 | `Toys & Games > Remote & App Controlled Vehicles & Parts > Remote & App Controlled Vehicles > Boats` |

## 四、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **扩大类目覆盖**：本次批量扫描共处理 16 个品类。市场扫描还有 5 个候选类目未覆盖，统一流水线会继续处理所有动态候选类目。

3. **关键词验证**：将本报告候选商品的核心关键词输入卖家精灵「关键词研究」，确认搜索量、购买率与 pipeline 关键词扫描结果吻合，再决定是否建 Listing。

4. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 五、原始数值

- `B0GHQMHRWW`: 28,621 | 13,924 | 33% | 382 | 13.6% | $9,546 | 300+ | - | 1 | $24.99 | - | 24 | - | 4.6 | - | $3.54 | 71% | 2026-03-25 | 2个月 | FBA | -
- `B0FQJVPZ4B`: 44,679 | 465 | 1% | 253 | 22.68% | $6,575 | 100+ | $2K+ | 2 | $25.99 | - | 67 | 10 | 4.6 | 3.95% | $6.02 | 62% | 2025-10-22 | 7个月 | FBA | -
- `B0FJ5YYQZ4`: 42,525 | 11,084 | 21% | 154 | 11.64% | $5,542 | 50+ | $1K+ | 5 | $35.99 | - | 77 | 8 | 4.0 | 5.19% | $6.18 | 68% | 2025-09-03 | 9个月 | FBA | -
- `B0CXCCWQKX`: 97,018 | 29,849 | 39% | 104 | 12.05% | $3,847 | - | - | 2 | $36.99 | - | 65 | 1 | 4.8 | 0.96% | $6.90 | 66% | 2024-04-10 | 2年 2个月 | FBA | -
- `B0GGGPCFND`: 40,308 | 29,898 | 43% | 137 | 10.1% | $3,150 | 50+ | $1K+ | 3 | $22.99 | - | 40 | 5 | 4.7 | 3.65% | $3.44 | 70% | 2026-03-01 | 3个月 | FBA | -

---

<!-- source: asin_keywords_B0DSRDB4YL_2026_06_13.md -->
# ASIN `B0DSRDB4YL` 推广关键词候选 (2026-06-13)

> 来源：卖家精灵关键词反查。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **15** 个，过滤后保留 **0** 个。
> 抓取完整性：页面可见 **15** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|

## 免费套餐当前可见原始关键词

1. **dry bag** — 干燥袋
2. **sea to summit dry bag** — 海底至山顶干货袋
3. **sea to summit toiletry bag** — 海到山顶洗漱包
4. **yeti sidekick dry bag** — Yeti 搭档干包
5. **roll top dry bag** — 卷顶干燥袋
6. **sea to summit big river dry bag** — 海登大河干袋
7. **seatosummit dry bag** — seatosummit 干燥袋
8. **sea to summit ultra-sil dry bag** — 海到顶峰超轻防水袋
9. **compression dry bag** — 压缩干燥袋
10. **waterproof compression dry bags** — 防水压缩干袋
11. **35l dry bag** — 35升干袋
12. **sea to summit dry bags** — 海登顶干袋
13. **xl dry bag**
14. **dry bag sea to summit** — 干袋海登顶
15. **sea to summit lightweight dry bag** — sea to summit 轻量干袋

---

<!-- source: asin_keywords_B0G7YT3F1H_2026_06_13.md -->
# ASIN `B0G7YT3F1H` 推广关键词候选 (2026-06-13)

> 来源：卖家精灵关键词反查。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **7** 个。
> 抓取完整性：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **lifesize cardboard cutout**<br>实物大小的纸板切口 | 33.32% / 144 /  / 主要流量词 /  / - | 自然搜索词 | 17 / 第1页, 17 / 56 / 06月07日排名 | 4,012 / 134 | 104 / 2.60% | 3 | 0 | 2.0 / 2,040 | $1.08 / $1.58 / $1.90 | 53.22 |
| 2 | **inflatable giraffe**<br>充气长颈鹿 | 66.68% / 288 /  / 主要流量词 /  / - | 自然搜索词 | 22 / 第1页, 22 / 53 / 今日07:55排名 | 1,680 / 56 | 126 / 7.54% | 3 | 9 | 7.5 / 223 | $0.32 / $0.40 / $0.50 | 49.66 |
| 3 | **jirafa de peluche gigante**<br>巨型毛绒长颈鹿 | - / - | 自然搜索词 | 41 / 第1页, 41 / 53 / 05月15日排名 | 2,943 / 98 | 20 / 0.70% | 1 | 0 | 15.6 / 189 | $0.34 / $0.39 / $0.45 | 16.89 |
| 4 | **large giraffe stuffed animal**<br>大长颈鹿填充动物 | - / - | 自然搜索词 | 40 / 第1页, 40 / 56 / 05月16日排名 | 1,870 / 62 | 40 / 2.17% | 1 | 1 | 1.2 / 1,603 | $0.43 / $0.62 / $0.82 | 15.74 |
| 5 | **giant giraffe**<br>巨型长颈鹿 | - / - | 自然搜索词 | 41 / 第1页, 41 / 65 / 2天前10:22排名 | 400 / 13 | 11 / 2.81% | 1 | 6 | 0.0 / 13,139 | $0.38 / $0.49 / $0.58 | 11.35 |
| 6 | **giant giraffe stuffed animal**<br>巨型长颈鹿毛绒玩具 | - / - | 自然搜索词 | 51 / 第1页, 51 / 55 / 06月03日排名 | 1,856 / 62 | 39 / 2.15% | 1 | 3 | 1.1 / 1,739 | $0.43 / $0.61 / $0.83 | 5.66 |
| 7 | **large stuffed giraffe**<br>大毛绒长颈鹿 | - / - | 自然搜索词 | 55 / 第1页, 55 / 56 / 05月24日排名 | 929 / 31 | 25 / 2.75% | 1 | 0 | 0.5 / 1,743 | $0.42 / $0.58 / $0.71 | 3.11 |

## 免费套餐当前可见原始关键词

1. **inflatable giraffe** — 充气长颈鹿
2. **lifesize cardboard cutout** — 实物大小的纸板切口
3. **jirafa de peluche gigante** — 巨型毛绒长颈鹿
4. **giant giraffe stuffed animal** — 巨型长颈鹿毛绒玩具
5. **large giraffe stuffed animal** — 大长颈鹿填充动物
6. **animal cutouts** — 动物剪纸
7. **large stuffed giraffe** — 大毛绒长颈鹿
8. **giraffe party decorations** — 长颈鹿派对装饰品
9. **giant giraffe** — 巨型长颈鹿
10. **giant stuffed giraffe** — 巨型毛绒长颈鹿
11. **large giraffe** — 大长颈鹿
12. **giraffe inflatable** — 长颈鹿充气
13. **jungle safari jeep photo booth prop**
14. **zoo animals cutouts**
15. **large safari cutouts with stand jungle forest animals**
16. **jungle safari cardboard**
17. **safari cardboard cutout**
18. **jungle cardboard**
19. **safari animal cardboard cutout**
20. **jungle party cardboard cutouts**

---

<!-- source: asin_keywords_B0GKMGJLL3_2026_06_13.md -->
# ASIN `B0GKMGJLL3` 推广关键词候选 (2026-06-13)

> 来源：卖家精灵关键词反查。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **3** 个。
> 抓取完整性：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **kayak lights**<br>皮划艇灯 | 8.69% / 1,616 / - | 自然搜索词 | 38 / 第1页, 38 / 53 / 今日07:57排名 | 9,485 / 316 | 194 / 2.05% | 5 | 9 | 1.2 / 7,947 | $0.41 / $0.62 / $0.72 | 47.36 |
| 2 | **boat spotlight**<br>船聚光灯 | 3.07% / 572 / - | 自然搜索词 | 39 / 第1页, 39 / 56 / 昨日07:00排名 | 3,598 / 120 | 47 / 1.31% | 2 | 5 | 1.6 / 2,232 | $0.44 / $0.59 / $0.74 | 22.62 |
| 3 | **boat anchor pole**<br>船锚杆 | 2.14% / 398 / - | 自然搜索词 | 93 / 第2页, 30 / 55 / 今日05:33排名 | 5,974 / 199 | 58 / 0.98% | 2 | 6 | 2.8 / 2,122 | $0.32 / $0.35 / $0.38 | 16.99 |

## 免费套餐当前可见原始关键词

1. **boat lights** — 船灯
2. **kayak lights** — 皮划艇灯
3. **boat navigation lights** — 船用导航灯
4. **boat anchor** — 船锚
5. **navigation lights for boats led** — 船用导航灯 led
6. **stern lights for boats** — 船尾灯
7. **stern light** — 船尾灯
8. **boat light** — 船灯
9. **anchor light** — 锚灯
10. **boat anchor light** — 船锚灯
11. **bass boat accessories** — 鲈鱼船配件
12. **boat stern light** — 船尾灯
13. **boat spotlight** — 船聚光灯
14. **boat navigation lights led** — 船用导航灯 LED
15. **boat anchors** — 船锚
16. **boat anchor pole** — 船锚杆
17. **boat lights bow and stern** — 船灯船头和船尾
18. **jon boat accessories** — 乔恩船配件
19. **boat stern light pole** — 船尾灯杆
20. **boat running lights** — 船行灯
