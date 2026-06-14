# 亚马逊选品完整流水线报告 (2026-06-14)

> 本文件汇总市场扫描、全部候选类目商品扫描和动态商品 ASIN 关键词反查结果。
> 各阶段独立报告仍保留用于审计。

---

<!-- source: market_scan_report.md -->
# 亚马逊选市场扫描与评估报告 (2026-06-14)

> [!IMPORTANT]
> 本报告基于 `unified pipeline config` 中设定的过滤与风控规则进行生成。今日共分析了 **30** 个符合基本条件的子类目，其中最终筛选出 **7** 个适合新手的 🟢 绿色推荐赛道。
> **抓取完整性**：扫描 **1** 页；页面总数提示：**117**；停止原因：免费套餐仅展示 30 个，页面提示共有 117 个类目；免费套餐截断风险：**可能存在**。
> **数量审计**：当前候选类目有 15 个，位于目标区间 8-15。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **7** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **8** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **15** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Swing Trainers** | 室内练习器 | $37.01 | 448 | 0.71 lbs | 4.37% | 57.1% | 68.0% |
| 2 | **Lighting Products** | 水底灯 | $47.85 | 482 | 1.72 lbs | 6.75% | 51.9% | 74.0% |
| 3 | **Nozzles** | 喷嘴 | $26.24 | 490 | 0.44 lbs | 2.63% | 53.8% | 74.0% |
| 4 | **Cardboard Cutouts** | 硬板纸模型 | $24.38 | 295 | 1.31 lbs | 4.59% | 61.0% | 62.0% |
| 5 | **Electrical System Tools** | 电气系统工具 | $29.48 | 437 | 0.99 lbs | 2.38% | 43.9% | 82.0% |
| 6 | **Brake System Bleeding Tools** | 刹车排气 | $27.00 | 465 | 1.55 lbs | 4.69% | 50.2% | 83.0% |
| 7 | **Trophies** | 奖杯 | $25.63 | 297 | 1.01 lbs | 2.59% | 49.0% | 49.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Compressed Air Dusters** | 压缩除尘罐 | $35.92 | 349 | 0.86 lbs | 3.16% | 谨慎认证类目路径 |
| 2 | **Wind Spinners** | Wind Spinners | $31.43 | 472 | 2.36 lbs | 3.09% | 重量偏重 (>2.0 lbs) |
| 3 | **Paddleboard Accessories** | 冲浪板配件 | $53.08 | 322 | 2.37 lbs | 4.17% | 重量偏重 (>2.0 lbs) |
| 4 | **Batteries & Battery Chargers** | 电池和电池 | $25.18 | 470 | 0.95 lbs | 9.83% | 退货率偏高 (>8.0%), 带电/合规资质敏感关键字 |
| 5 | **Decorative Trays** | 装饰性托盘 | $22.23 | 466 | 1.45 lbs | 9.52% | 退货率偏高 (>8.0%) |
| 6 | **Game Mats & Boards** | 游戏垫和游戏板 | $29.62 | 308 | 2.47 lbs | 7.5% | 重量偏重 (>2.0 lbs), 谨慎认证类目路径 |
| 7 | **Boats** | 船 | $56.10 | 330 | 1.46 lbs | 6.03% | 谨慎认证类目路径 |
| 8 | **Grinding Discs** | 磨片 | $23.53 | 360 | 2.02 lbs | 2.13% | 重量偏重 (>2.0 lbs) |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Rash Guard Sets** | Rash Guard Sets | $20.98 | 高风险类目路径过滤 |
| 2 | **Sets** | 套 | $24.13 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 3 | **Skirt Sets** | 裙装套装 | $35.46 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 4 | **Rash Guard Sets** | 皮疹防护套装 | $22.34 | 高风险类目路径过滤 |
| 5 | **Button-Down Shirts** | 扣角领衬衫 | $21.08 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 6 | **Active Pants** | 运动裤 | $32.73 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 7 | **Glasses** | 眼镜 | $54.83 | 退货率过高 (>10.0%) |
| 8 | **Pant Sets** | 长裤套装 | $22.70 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 9 | **Wall Molding & Trim** | 墙压条和镶边 | $21.67 | 退货率过高 (>10.0%) |
| 10 | **Candlestick Holders** | 烛台座 | $24.18 | 退货率过高 (>10.0%) |
| 11 | **Spotlights** | 聚光灯 | $28.32 | 退货率过高 (>10.0%) |
| 12 | **Livestock Health Supplies** | 牲畜健康用品 | $31.76 | 排除类关键字过滤 |
| 13 | **Cup Carriers** | 外卖杯托盘 | $22.27 | 重量超标 (>2.5 lbs) |
| 14 | **Clutches** | 手拿包 | $32.88 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 15 | **Oolong** | 乌龙 | $20.15 | 高风险类目路径过滤 |

## 三、 候选类目详细数据指标画像 (供大模型分析使用)

以下为入选的绿色与黄色子类目的完整数据指标。您可以将这些数据输入大模型（如 Gemini、Claude），让其结合具体品类特性进行深入的入选原因、产品特征及商业机会评估。

### 🟢 绿色类目详情列表

#### 🏆 🟢-1. Swing Trainers (室内练习器)

- **完整市场路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$37.01`
  *   **平均 Reviews (Avg Reviews)**：`448 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`4.37%`
  *   **平均毛利率 (Profit Margin)**：`58.39%`
  *   **品牌集中度 (Brand Concentration)**：`57.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 高尔夫球场 › 用品 训练 › 室内练习器`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 18.27`
  *   **新品平均星级**：`3.6`
  *   **新品月均销量**：`1,043`
  *   **新品月均销售额**：`$15,154`
  *   **平均重量**：`0.71 pounds (321 g)`
  *   **平均体积**：`150.45 in³ (2,465 cm³)`
  *   **平均毛利率**：`58.39%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-2. Lighting Products (水底灯)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$47.85`
  *   **平均 Reviews (Avg Reviews)**：`482 个`
  *   **物理重量 (Weight)**：`1.72 lbs`
  *   **平均退货率 (Return Rate)**：`6.75%`
  *   **平均毛利率 (Profit Margin)**：`66.79%`
  *   **品牌集中度 (Brand Concentration)**：`51.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 水底灯`
  *   **A+数量占比**：`95%`
  *   **新品平均评分数**：`82`
  *   **新品平均价格**：`$ 47.76`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`1,236`
  *   **新品月均销售额**：`$66,017`
  *   **平均重量**：`1.72 pounds (781 g)`
  *   **平均体积**：`633.46 in³ (10,381 cm³)`
  *   **平均毛利率**：`66.79%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-3. Nozzles (喷嘴)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.24`
  *   **平均 Reviews (Avg Reviews)**：`490 个`
  *   **物理重量 (Weight)**：`0.44 lbs`
  *   **平均退货率 (Return Rate)**：`2.63%`
  *   **平均毛利率 (Profit Margin)**：`63.66%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 电动工具 › 替换件和配件 › 高压清洗机配件 › 喷嘴`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`55`
  *   **新品平均价格**：`$ 32.04`
  *   **新品平均星级**：`2.6`
  *   **新品月均销量**：`839`
  *   **新品月均销售额**：`$23,205`
  *   **平均重量**：`0.44 pounds (200 g)`
  *   **平均体积**：`70.03 in³ (1,148 cm³)`
  *   **平均毛利率**：`63.66%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`13.5‰`

---

#### 🏆 🟢-4. Cardboard Cutouts (硬板纸模型)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.38`
  *   **平均 Reviews (Avg Reviews)**：`295 个`
  *   **物理重量 (Weight)**：`1.31 lbs`
  *   **平均退货率 (Return Rate)**：`4.59%`
  *   **平均毛利率 (Profit Margin)**：`60.41%`
  *   **品牌集中度 (Brand Concentration)**：`61.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 硬板纸模型`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`27`
  *   **新品平均价格**：`$ 22.88`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`482`
  *   **新品月均销售额**：`$11,431`
  *   **平均重量**：`1.31 pounds (594 g)`
  *   **平均体积**：`337.59 in³ (5,532 cm³)`
  *   **平均毛利率**：`60.41%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`6.4‰`

---

#### 🏆 🟢-5. Electrical System Tools (电气系统工具)

- **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.48`
  *   **平均 Reviews (Avg Reviews)**：`437 个`
  *   **物理重量 (Weight)**：`0.99 lbs`
  *   **平均退货率 (Return Rate)**：`2.38%`
  *   **平均毛利率 (Profit Margin)**：`55.8%`
  *   **品牌集中度 (Brand Concentration)**：`43.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 电气系统工具`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`47`
  *   **新品平均价格**：`$ 18.35`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`418`
  *   **新品月均销售额**：`$8,313`
  *   **平均重量**：`0.99 pounds (449 g)`
  *   **平均体积**：`316.05 in³ (5,179 cm³)`
  *   **平均毛利率**：`55.8%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟢-6. Brake System Bleeding Tools (刹车排气)

- **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.00`
  *   **平均 Reviews (Avg Reviews)**：`465 个`
  *   **物理重量 (Weight)**：`1.55 lbs`
  *   **平均退货率 (Return Rate)**：`4.69%`
  *   **平均毛利率 (Profit Margin)**：`55.45%`
  *   **品牌集中度 (Brand Concentration)**：`50.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 制动工具 › 刹车排气`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`32`
  *   **新品平均价格**：`$ 17.61`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`411`
  *   **新品月均销售额**：`$8,002`
  *   **平均重量**：`1.55 pounds (704 g)`
  *   **平均体积**：`303.90 in³ (4,980 cm³)`
  *   **平均毛利率**：`55.45%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`8.9‰`

---

#### 🏆 🟢-7. Trophies (奖杯)

- **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.63`
  *   **平均 Reviews (Avg Reviews)**：`297 个`
  *   **物理重量 (Weight)**：`1.01 lbs`
  *   **平均退货率 (Return Rate)**：`2.59%`
  *   **平均毛利率 (Profit Margin)**：`62.86%`
  *   **品牌集中度 (Brand Concentration)**：`49.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`49.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 辅料 › 、奖牌 › 奖杯`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`34`
  *   **新品平均价格**：`$ 30.54`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`544`
  *   **新品月均销售额**：`$21,199`
  *   **平均重量**：`1.01 pounds (458 g)`
  *   **平均体积**：`179.64 in³ (2,944 cm³)`
  *   **平均毛利率**：`62.86%`
  *   **卖家所属地**：`中国|49.0%`
  *   **搜索购买比**：`6.5‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Compressed Air Dusters (压缩除尘罐)

- **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.92`
  *   **平均 Reviews (Avg Reviews)**：`349 个`
  *   **物理重量 (Weight)**：`0.86 lbs`
  *   **平均退货率 (Return Rate)**：`3.16%`
  *   **平均毛利率 (Profit Margin)**：`74.31%`
  *   **品牌集中度 (Brand Concentration)**：`60.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
  *   **市场路径(中文)**：`电子产品 › 计算机 › 电脑配件 › 清洁 › 压缩除尘罐`
  *   **A+数量占比**：`92%`
  *   **新品平均评分数**：`118`
  *   **新品平均价格**：`$ 34.21`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`542`
  *   **新品月均销售额**：`$16,850`
  *   **平均重量**：`0.86 pounds (392 g)`
  *   **平均体积**：`42.95 in³ (704 cm³)`
  *   **平均毛利率**：`74.31%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`13.0‰`

---

#### 🏆 🟡-2. Wind Spinners (Wind Spinners)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.43`
  *   **平均 Reviews (Avg Reviews)**：`472 个`
  *   **物理重量 (Weight)**：`2.36 lbs`
  *   **平均退货率 (Return Rate)**：`3.09%`
  *   **平均毛利率 (Profit Margin)**：`59.7%`
  *   **品牌集中度 (Brand Concentration)**：`54.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`85.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`51`
  *   **新品平均价格**：`$ 21.94`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`749`
  *   **新品月均销售额**：`$13,820`
  *   **平均重量**：`2.36 pounds (1,070 g)`
  *   **平均体积**：`269.46 in³ (4,416 cm³)`
  *   **平均毛利率**：`59.7%`
  *   **卖家所属地**：`中国|85.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟡-3. Paddleboard Accessories (冲浪板配件)

- **完整市场路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$53.08`
  *   **平均 Reviews (Avg Reviews)**：`322 个`
  *   **物理重量 (Weight)**：`2.37 lbs`
  *   **平均退货率 (Return Rate)**：`4.17%`
  *   **平均毛利率 (Profit Margin)**：`64.36%`
  *   **品牌集中度 (Brand Concentration)**：`42.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 划船和你 › 立式单肩肩背 › 冲浪板配件`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`35`
  *   **新品平均价格**：`$ 76.83`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`651`
  *   **新品月均销售额**：`$50,572`
  *   **平均重量**：`2.37 pounds (1,077 g)`
  *   **平均体积**：`425.27 in³ (6,969 cm³)`
  *   **平均毛利率**：`64.36%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟡-4. Batteries & Battery Chargers (电池和电池)

- **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.18`
  *   **平均 Reviews (Avg Reviews)**：`470 个`
  *   **物理重量 (Weight)**：`0.95 lbs`
  *   **平均退货率 (Return Rate)**：`9.83%`
  *   **平均毛利率 (Profit Margin)**：`62.58%`
  *   **品牌集中度 (Brand Concentration)**：`61.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`84.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 溜冰鞋、滑板和滑板车 › 自行车车 › 自行车车配件 › 电池和电池`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`74`
  *   **新品平均价格**：`$ 34.11`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`590`
  *   **新品月均销售额**：`$17,597`
  *   **平均重量**：`0.95 pounds (429 g)`
  *   **平均体积**：`56.33 in³ (923 cm³)`
  *   **平均毛利率**：`62.58%`
  *   **卖家所属地**：`中国|84.0%`
  *   **搜索购买比**：`9.9‰`

---

#### 🏆 🟡-5. Decorative Trays (装饰性托盘)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.23`
  *   **平均 Reviews (Avg Reviews)**：`466 个`
  *   **物理重量 (Weight)**：`1.45 lbs`
  *   **平均退货率 (Return Rate)**：`9.52%`
  *   **平均毛利率 (Profit Margin)**：`56.79%`
  *   **品牌集中度 (Brand Concentration)**：`42.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰性托盘`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`125`
  *   **新品平均价格**：`$ 22.18`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`669`
  *   **新品月均销售额**：`$12,639`
  *   **平均重量**：`1.45 pounds (658 g)`
  *   **平均体积**：`226.34 in³ (3,709 cm³)`
  *   **平均毛利率**：`56.79%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟡-6. Game Mats & Boards (游戏垫和游戏板)

- **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.62`
  *   **平均 Reviews (Avg Reviews)**：`308 个`
  *   **物理重量 (Weight)**：`2.47 lbs`
  *   **平均退货率 (Return Rate)**：`7.5%`
  *   **平均毛利率 (Profit Margin)**：`58.18%`
  *   **品牌集中度 (Brand Concentration)**：`40.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 游戏配件 › 游戏垫和游戏板`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 33.34`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`333`
  *   **新品月均销售额**：`$10,879`
  *   **平均重量**：`2.47 pounds (1,120 g)`
  *   **平均体积**：`304.41 in³ (4,988 cm³)`
  *   **平均毛利率**：`58.18%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`3.8‰`

---

#### 🏆 🟡-7. Boats (船)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$56.10`
  *   **平均 Reviews (Avg Reviews)**：`330 个`
  *   **物理重量 (Weight)**：`1.46 lbs`
  *   **平均退货率 (Return Rate)**：`6.03%`
  *   **平均毛利率 (Profit Margin)**：`69.1%`
  *   **品牌集中度 (Brand Concentration)**：`62.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 船`
  *   **A+数量占比**：`98%`
  *   **新品平均评分数**：`39`
  *   **新品平均价格**：`$ 54.62`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`319`
  *   **新品月均销售额**：`$16,000`
  *   **平均重量**：`1.46 pounds (661 g)`
  *   **平均体积**：`317.55 in³ (5,204 cm³)`
  *   **平均毛利率**：`69.1%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`2.9‰`

---

#### 🏆 🟡-8. Grinding Discs (磨片)

- **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.53`
  *   **平均 Reviews (Avg Reviews)**：`360 个`
  *   **物理重量 (Weight)**：`2.02 lbs`
  *   **平均退货率 (Return Rate)**：`2.13%`
  *   **平均毛利率 (Profit Margin)**：`60.83%`
  *   **品牌集中度 (Brand Concentration)**：`46.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs  市场分析`
  *   **市场路径(中文)**：`工业类 › 磨削加工 › 研磨砂轮 › 磨片`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`15`
  *   **新品平均价格**：`$ 22.82`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`397`
  *   **新品月均销售额**：`$7,480`
  *   **平均重量**：`2.02 pounds (918 g)`
  *   **平均体积**：`13.04 in³ (214 cm³)`
  *   **平均毛利率**：`60.83%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`15.0‰`

---

---

<!-- source: products/batteries_battery_chargers.md -->
# Batteries & Battery Chargers 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $25.18　均Reviews 470（中等）　重量 0.95lbs（轻）　退货率 9.83%（高）　品牌集中度 61.4%（中等）　中国卖家 84.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DJT1YH6F](https://www.amazon.com/dp/B0DJT1YH6F) |  | Vitality Sports Golf Chipping Net | 999 / 27.16% | $45,924 | $45.97 | $7.02 (15%) | 106 / 7 | 4.6 | $7.23 / 69% | 2 | 3 | 2 | 3.24 pounds | 2024-11-07 1年 7个月 |
| 2 | [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT) |  | Suspension Straps Trainer with Built-in Door Anchor | 855 / 7.98% | $42,741 | $49.99 | $7.69 (15%) | 101 / 21 | 4.6 | $6.31 / 72% | 1 | 4 | 1 | 2.31 pounds | 2025-06-07 1年 |
| 3 | [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3) |  | Boat Stern Light Anchor Light | 856 / 29.64% | $36,799 | $42.99 | $6.66 (15%) | 30 / 13 | 4.9 | $10.11 / 61% | 3 | 14 | 1 | 1.25 pounds | 2026-03-31 2个月 |
| 4 | [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q) |  | SILCA Ultimate Sealant Bottle | 749 / 7.13% | $33,698 | $44.99 | $6.57 (15%) | 140 / - | 4.5 | $6.48 / 71% | 4 | 19 | 1 | 2.51 pounds | 2025-02-16 1年 3个月 |
| 5 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 789 / 11.11% | $31,552 | $39.99 | $5.91 (15%) | 110 / 13 | 4.7 | $4.09 / 75% | 4 | 19 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 6 | [B0G93DF8CJ](https://www.amazon.com/dp/B0G93DF8CJ) |  | Exun Soccer Fan Gift Basket Set 2026 | 1,000 / 102.84% | $29,990 | $29.99 | $4.37 (15%) | 58 / 16 | 4.8 | $6.13 / 65% | 1 | 163 | 1 | 1.87 pounds | 2026-02-20 3个月 |
| 7 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 8 | [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP) |  | Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner | 890 / 34.88% | $28,471 | $31.99 | $4.87 (15%) | 118 / 4 | 4.5 | $4.09 / 72% | 3 | 7 | 1 | 0.29 pounds | 2024-02-06 2年 4个月 |
| 9 | [B0DRFSFCYQ](https://www.amazon.com/dp/B0DRFSFCYQ) |  | Telescoping Boat Hook for Docking | 678 / 103.33% | $28,469 | $41.99 | $6.11 (15%) | 138 / 13 | 4.6 | $12.37 / 56% | 2 | 5 | 1 | 2.65 pounds | 2025-01-26 1年 4个月 |
| 10 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 740 / 54.21% | $28,113 | $37.99 | $5.64 (15%) | 127 / 7 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 11 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | **** / **** | **** | $35.99 | - | 125 / 37 | 4.6 | **** /  | 3 | 64 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 12 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 13 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 85 / 15 | 4.5 | **** /  | 1 | 22 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 14 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 15 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 5 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 2个月 |
| 16 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 17 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |
| 18 | [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64) |  | GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men | **** / **** | **** | $49.99 | - | 97 / - | 4.5 | **** /  | 5 | 19 | 1 | 1.3 pounds | 2025-03-28 1年 2个月 |
| 19 | [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF) |  | Grip Enhancer Tacky Towel | **** / **** | **** | $36.99 | - | 125 / - | 4.5 | **** /  | 2 | 34 | 2 | 0.29 pounds | 2024-12-17 1年 5个月 |
| 20 | [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH) |  | Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdo… | **** / **** | **** | $36.95 | - | 111 / 3 | 4.8 | **** /  | 3 | 77 | 2 | 0.2 pounds | 2025-03-14 1年 2个月 |

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

**11. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**12. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**13. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**14. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**15. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**16. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**17. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

**18. [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64)** GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men, Natural Rattan Wicker Bike Baskets for Adult Bikes, Basket for Bikes with Liner, Bicycle Baskets for Beach Cruiser

**19. [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF)** Grip Enhancer Tacky Towel - USA-Made Chalkless Competition-Approved Formula for Golf, Tennis, Softball and More - Versatile Multi-Sport Moisture Control for Sweaty Hands

**20. [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH)** Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdoor Headlamp with Multiple Color Temperatures Warm Natural, Cold Lights and Red Light (Elastic Cord, Black)

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0DJT1YH6F`: 6,744 | 1,208 | 15% | 999 | 27.16% | $45,924 | 700+ | $27K+ | 2 | $45.97 | - | 106 | 7 | 4.6 | 0.7% | $7.23 | 69% | 2024-11-07 | 1年 7个月 | FBA | -
- `B0F5BD54RT`: 10,137 | 2,307 | 19% | 855 | 7.98% | $42,741 | 700+ | $34K+ | 1 | $49.99 | - | 101 | 21 | 4.6 | 2.46% | $6.31 | 72% | 2025-06-07 | 1年 | FBA | -
- `B0GKMGJLL3`: 10,790 | 2,203 | 17% | 856 | 29.64% | $36,799 | 600+ | $25K+ | 3 | $42.99 | - | 30 | 13 | 4.9 | 1.52% | $10.11 | 61% | 2026-03-31 | 2个月 | FBA | -
- `B0DX2F3V5Q`: 11,637 | 0 | 0% | 749 | 7.13% | $33,698 | 300+ | $13K+ | 4 | $44.99 | - | 140 | - | 4.5 | - | $6.48 | 71% | 2025-02-16 | 1年 3个月 | FBA | -
- `B0DTP76XQP`: 10,207 | 353 | 3% | 789 | 11.11% | $31,552 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 13 | 4.7 | 1.65% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0G93DF8CJ`: 4,786 | 3,333 | 41% | 1,000 | 102.84% | $29,990 | 900+ | $27K+ | 1 | $29.99 | - | 58 | 16 | 4.8 | 1.6% | $6.13 | 65% | 2026-02-20 | 3个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0CTQTYVGP`: 8,500 | 227 | 3% | 890 | 34.88% | $28,471 | 400+ | $12K+ | 3 | $31.99 | - | 118 | 4 | 4.5 | 0.45% | $4.09 | 72% | 2024-02-06 | 2年 4个月 | FBA | -
- `B0DRFSFCYQ`: 13,590 | 25 | 0% | 678 | 103.33% | $28,469 | 500+ | $20K+ | 2 | $41.99 | - | 138 | 13 | 4.6 | 1.92% | $12.37 | 56% | 2025-01-26 | 1年 4个月 | FBA | -
- `B0DS2CBVFT`: 8,379 | 2,034 | 20% | 740 | 54.21% | $28,113 | 300+ | $11K+ | 5 | $37.99 | - | 127 | 7 | 4.8 | 0.95% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0GL785GSP`: 13,539 | 268 | 2% | **** | **** | **** | **** | 3 | $35.99 | - | 125 | 37 | 4.6 | 5.05% | **** | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0F9ZZ17Z8`: 13,699 | 581 | 4% | **** | **** | **** | **** | 1 | $41.97 | - | 85 | 15 | 4.5 | 2.42% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0CT5MVCFD`: 17,365 | 1,868 | 10% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 5 | 4.8 | 0.95% | **** | 2024-03-14 | 2年 2个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -
- `B0DS23SX64`: 15,152 | 0 | 0% | **** | **** | **** | **** | 5 | $49.99 | - | 97 | - | 4.5 | - | **** | 2025-03-28 | 1年 2个月 | FBA | -
- `B0DNZX4MZF`: 13,386 | 0 | 0% | **** | **** | **** | **** | 2 | $36.99 | - | 125 | - | 4.5 | - | **** | 2024-12-17 | 1年 5个月 | FBA | -
- `B0DY2SW4CH`: 12,094 | 943 | 7% | **** | **** | **** | **** | 3 | $36.95 | - | 111 | 3 | 4.8 | 0.47% | **** | 2025-03-14 | 1年 2个月 | FBA | -

---

<!-- source: products/boats.md -->
# Boats 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $56.10　均Reviews 330（中等）　重量 1.46lbs（轻）　退货率 6.03%（中）　品牌集中度 62.0%（中等）　中国卖家 68.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0CWXVCT2G](https://www.amazon.com/dp/B0CWXVCT2G) |  | Losbenco RC Boat | 154 / 52.43% | $6,158 | $39.99 | $6.19 (15%) | 83 / 5 | 4.2 | $7.41 / 66% | 1 | 77 | 1 | 1.48 pounds | 2024-04-18 2年 1个月 |
| 2 | [B0D8TB7V29](https://www.amazon.com/dp/B0D8TB7V29) |  | GearRoot Remote Control Dolphin Toys for Kids | 116 / 29.69% | $3,131 | $26.99 | $4.12 (15%) | 12 / - | 4.1 | $5.87 / 63% | 1 | 122 | 1 | 0.86 pounds | 2024-11-03 1年 7个月 |

## 二、完整商品标题

**1. [B0CWXVCT2G](https://www.amazon.com/dp/B0CWXVCT2G)** Losbenco RC Boat, 1/72 RC Tugboat for Pools and Lakes, High-Speed Remote Control Boat with 40 Mins Play Time and Low Battery Reminder for Kids and Adults - RTR Version

**2. [B0D8TB7V29](https://www.amazon.com/dp/B0D8TB7V29)** GearRoot Remote Control Dolphin Toys for Kids, 2.4G High Simulation Oceanic RC Dolphins Fish Toys for Swimming Pool Bathroom, 2x600mAh RC Boat Water Toys Great for 6+ Year olds Boys Girls Kids, Gray

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0CWXVCT2G`: 48,617 | 24,954 | 34% | 154 | 52.43% | $6,158 | 50+ | $1K+ | 1 | $39.99 | - | 83 | 5 | 4.2 | 3.25% | $7.41 | 66% | 2024-04-18 | 2年 1个月 | FBA | -
- `B0D8TB7V29`: 51,139 | 19,365 | 27% | 116 | 29.69% | $3,131 | 50+ | $1K+ | 1 | $26.99 | - | 12 | - | 4.1 | - | $5.87 | 63% | 2024-11-03 | 1年 7个月 | FBA | -

---

<!-- source: products/brake_system_bleeding_tools.md -->
# Brake System Bleeding Tools 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $27.00　均Reviews 465（中等）　重量 1.55lbs（偏重）　退货率 4.69%（低）　品牌集中度 50.2%（中等）　中国卖家 83.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GGQH744M](https://www.amazon.com/dp/B0GGQH744M) |  | Brake Bleeder Kit - One-Way Check Valve | 806 / 20.66% | $18,449 | $22.89 | $3.43 (15%) | 52 / 17 | 4.7 | $4.35 / 66% | 1 | 18 | 1 | 0.29 pounds | 2026-01-14 4个月 |
| 2 | [B0F22SXPDT](https://www.amazon.com/dp/B0F22SXPDT) |  | BleedZone SRAM DB8 Brake Bleed Kit with Maxima Mineral Oil Includ… | 103 / 56.25% | $3,316 | $32.19 | $4.99 (15%) | 14 / 3 | 4.1 | $4.35 / 71% | 2 | 216 | 1 | 0.71 pounds | 2025-04-24 1年 1个月 |

## 二、完整商品标题

**1. [B0GGQH744M](https://www.amazon.com/dp/B0GGQH744M)** Brake Bleeder Kit - One-Way Check Valve, Magnet Mount, 16oz Catch Bottle, 16” Hose

**2. [B0F22SXPDT](https://www.amazon.com/dp/B0F22SXPDT)** BleedZone SRAM DB8 Brake Bleed Kit with Maxima Mineral Oil Included, 2x Pro PC Syringe & M4 Fittings, Hydraulic Bike Brake Bleeding Kit, MTB & Road Bicycle Service Tool for SRAM Mineral Oil Systems

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GGQH744M`: 8,583 | 145 | 2% | 806 | 20.66% | $18,449 | 700+ | $16K+ | 1 | $22.89 | - | 52 | 17 | 4.7 | 2.11% | $4.35 | 66% | 2026-01-14 | 4个月 | FBA | -
- `B0F22SXPDT`: 92,590 | 57,898 | 38% | 103 | 56.25% | $3,316 | 50+ | $1K+ | 2 | $32.19 | - | 14 | 3 | 4.1 | 2.91% | $4.35 | 71% | 2025-04-24 | 1年 1个月 | FBA | -

---

<!-- source: products/cardboard_cutouts.md -->
# Cardboard Cutouts 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $24.38　均Reviews 295（低竞争）　重量 1.31lbs（轻）　退货率 4.59%（低）　品牌集中度 61.0%（中等）　中国卖家 62.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B09PKHLH7W](https://www.amazon.com/dp/B09PKHLH7W) |  | Cardboard People Princess Collage Life Size Cardboard Cutout Stan… | 449 / 7.42% | $21,534 | $47.96 | $7.22 (15%) | 87 / - | 4.5 | $16.76 / 50% | 1 | 63 | 2 | 2.45 pounds | 2022-01-11 4年 5个月 |
| 2 | [B0GHSNNZPZ](https://www.amazon.com/dp/B0GHSNNZPZ) |  | 131PCS Classic Winnie Baby Shower Birthday Decorations Large Winn… | 402 / 37.36% | $10,850 | $26.99 | $4.13 (15%) | 13 / 4 | 4.6 | $6.13 / 62% | 1 | 21 | 1 | 1.92 pounds | 2026-03-08 3个月 |
| 3 | [B0G7YT3F1H](https://www.amazon.com/dp/B0G7YT3F1H) |  | Giraffe Cardboard Cutout Life-Size Animal Cutout Realistic Safari… | 290 / 40.56% | $9,567 | $32.99 | $5.09 (15%) | 2 / - | 5.0 | $6.13 / 66% | 1 | 528 | 1 | 1.37 pounds | 2025-12-20 5个月 |
| 4 | [B0GJL3W2D6](https://www.amazon.com/dp/B0GJL3W2D6) |  | 131PCS Pink Winnie Baby Shower Birthday Decorations for Girl Larg… | 281 / 159.57% | $7,584 | $26.99 | $4.17 (15%) | 11 / 2 | 4.4 | $6.90 / 59% | 1 | 72 | 1 | 1.74 pounds | 2026-03-25 2个月 |
| 5 | [B0FWC8ZZ48](https://www.amazon.com/dp/B0FWC8ZZ48) |  | 4 Ft Happy Birthday Jesus Cardboard Cutout Stand Up Life Size Lar… | 226 / 103.49% | $6,778 | $29.99 | $4.48 (15%) | 14 / 2 | 4.8 | $6.02 / 65% | 4 | 80 | 1 | 1.41 pounds | 2025-10-16 7个月 |

## 二、完整商品标题

**1. [B09PKHLH7W](https://www.amazon.com/dp/B09PKHLH7W)** Cardboard People Princess Collage Life Size Cardboard Cutout Standup - Disney

**2. [B0GHSNNZPZ](https://www.amazon.com/dp/B0GHSNNZPZ)** 131PCS Classic Winnie Baby Shower Birthday Decorations Large Winnie Coroplast Cutout with Stand, Neutral Balloons Arch& Bee Stickers for Gender Reveal, First Birthday, Photo Props & Pooh Party

**3. [B0G7YT3F1H](https://www.amazon.com/dp/B0G7YT3F1H)** Giraffe Cardboard Cutout Life-Size Animal Cutout Realistic Safari Jungle Photo Booth Prop Decor for Parties, Zoo-Themed Events, Classrooms, Birthday Decoration Supplies 28.39 x 59.06 Inches

**4. [B0GJL3W2D6](https://www.amazon.com/dp/B0GJL3W2D6)** 131PCS Pink Winnie Baby Shower Birthday Decorations for Girl Large Winnie Cutouts Stand Up, Pooh Balloons Arch & Bee Stickers for Gender Reveal, First Birthday, Photo Props & Newborn Party

**5. [B0FWC8ZZ48](https://www.amazon.com/dp/B0FWC8ZZ48)** 4 Ft Happy Birthday Jesus Cardboard Cutout Stand Up Life Size Large Religious Christ Party Decoration Christian Photo Props Backdrop for Jesus Party Easter VBS Church Baptism Sunday School

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B09PKHLH7W`: 105,040 | 8,436 | 7% | 449 | 7.42% | $21,534 | 200+ | $9K+ | 1 | $47.96 | - | 87 | - | 4.5 | - | $16.76 | 50% | 2022-01-11 | 4年 5个月 | FBA | -
- `B0GHSNNZPZ`: 57,231 | 12,495 | 18% | 402 | 37.36% | $10,850 | 300+ | $8K+ | 1 | $26.99 | - | 13 | 4 | 4.6 | 1% | $6.13 | 62% | 2026-03-08 | 3个月 | FBA | -
- `B0G7YT3F1H`: 537,981 | 318,998 | 28% | 290 | 40.56% | $9,567 | - | - | 1 | $32.99 | - | 2 | - | 5.0 | - | $6.13 | 66% | 2025-12-20 | 5个月 | FBA | -
- `B0GJL3W2D6`: 118,592 | 28,152 | 19% | 281 | 159.57% | $7,584 | 200+ | $5K+ | 1 | $26.99 | - | 11 | 2 | 4.4 | 0.71% | $6.90 | 59% | 2026-03-25 | 2个月 | FBA | -
- `B0FWC8ZZ48`: 128,110 | 13,251 | 9% | 226 | 103.49% | $6,778 | 100+ | $3K+ | 4 | $29.99 | - | 14 | 2 | 4.8 | 0.88% | $6.02 | 65% | 2025-10-16 | 7个月 | FBA | -

---

<!-- source: products/compressed_air_dusters.md -->
# Compressed Air Dusters 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters`
> 共抓取 **6** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **6** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $35.92　均Reviews 349（中等）　重量 0.86lbs（轻）　退货率 3.16%（低）　品牌集中度 60.0%（中等）　中国卖家 76.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0FPRM62Z2](https://www.amazon.com/dp/B0FPRM62Z2) |  | Compressed Air Duster-230000RPM Super Power Electric Air Duster | 679 / 74.71% | $20,363 | $29.99 | $2.33 (8%) | 48 / 26 | 4.3 | $4.87 / 76% | 1 | 61 | 1 | 0.99 pounds | 2025-10-11 8个月 |
| 2 | [B0FFGTDMMX](https://www.amazon.com/dp/B0FFGTDMMX) |  | fourq Compressed Air Duster,Mini Vacuum Cleaner 2-in-1,4000 mAh,1… | 449 / 132.63% | $12,792 | $28.49 | $2.41 (8%) | 26 / 11 | 4.2 | $6.42 / 69% | 1 | 61 | 1 | 1.57 pounds | 2025-06-26 11个月 |
| 3 | [B0FSLLJ8SZ](https://www.amazon.com/dp/B0FSLLJ8SZ) |  | Mini Ultra-Slim Electric Compressed Air Duster 150,000RPM Super P… | 346 / 67.33% | $8,993 | $25.99 | $2.04 (8%) | 55 / - | 4.3 | $4.46 / 75% | 2 | 73 | 2 | 0.64 pounds | 2025-10-31 7个月 |
| 4 | [B0GRH6MY39](https://www.amazon.com/dp/B0GRH6MY39) |  | Electric Air Duster 180000RPM | 190 / 50% | $7,598 | $39.99 | $3.08 (8%) | 48 / 3 | 4.5 | $5.72 / 78% | 1 | 188 | 1 | 1.34 pounds | 2026-03-09 3个月 |
| 5 | [B0GGR1T98P](https://www.amazon.com/dp/B0GGR1T98P) |  | Compressed Air Duster-150000RPM Super Power Cordless Air Duster | 239 / 116.81% | $5,734 | $23.99 | $1.85 (8%) | 40 / 17 | 4.3 | $4.87 / 72% | 1 | 127 | 1 | 0.93 pounds | 2026-03-14 2个月 |
| 6 | [B0DB8J4T52](https://www.amazon.com/dp/B0DB8J4T52) |  | Compressed Air Duster,180000RPM Electric Duster Air Blower,Cordle… | 106 / 6.19% | $2,640 | $24.91 | $1.89 (8%) | 150 / 4 | 4.3 | $5.33 / 71% | 1 | 241 | 1 | 1.1 pounds | 2024-09-27 1年 8个月 |

## 二、完整商品标题

**1. [B0FPRM62Z2](https://www.amazon.com/dp/B0FPRM62Z2)** Compressed Air Duster-230000RPM Super Power Electric Air Duster, 4-Gear Adjustable Mini Blower with Type-C Fast Charging, Dust Blower for Computer, Keyboard, House, Outdoor and Car

**2. [B0FFGTDMMX](https://www.amazon.com/dp/B0FFGTDMMX)** fourq Compressed Air Duster,Mini Vacuum Cleaner 2-in-1,4000 mAh,130,000 RPM Brushless Motor,8000Pa，120MPH/1.1LB Thrust Car Dryer Air Blower for Car Cleaning,Computer Cleaning

**3. [B0FSLLJ8SZ](https://www.amazon.com/dp/B0FSLLJ8SZ)** Mini Ultra-Slim Electric Compressed Air Duster 150,000RPM Super Power, Rechargeable Cordless Air Duster, Powerful Airflow for Computer, Keyboard, Outdoor, House and Car

**4. [B0GRH6MY39](https://www.amazon.com/dp/B0GRH6MY39)** Electric Air Duster 180000RPM, Powerful Cordless Compressed Air Duster with 3-Speed Mini Air Duster Blower, Rechargeable Dust Cleaner for Computer Keyboard, PC, Car, Outdoor & Home Cleaning

**5. [B0GGR1T98P](https://www.amazon.com/dp/B0GGR1T98P)** Compressed Air Duster-150000RPM Super Power Cordless Air Duster, Rechargeable Brushless Motor Durable Power Blower with SOS LED Light,Adjustable Dust Blower for Computer, Pet,Outdoor, House and Car

**6. [B0DB8J4T52](https://www.amazon.com/dp/B0DB8J4T52)** Compressed Air Duster,180000RPM Electric Duster Air Blower,Cordless Rechargeable Mini Dust Blower,3 Gear Jet Fan for PC Keyboard Computer Car Outdoor House Cleaning-Black

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0FPRM62Z2`: 10,984 | 1,637 | 13% | 679 | 74.71% | $20,363 | 600+ | $18K+ | 1 | $29.99 | - | 48 | 26 | 4.3 | 3.83% | $4.87 | 76% | 2025-10-11 | 8个月 | FBA | -
- `B0FFGTDMMX`: 11,601 | 8,576 | 43% | 449 | 132.63% | $12,792 | 400+ | $12K+ | 1 | $28.49 | - | 26 | 11 | 4.2 | 2.45% | $6.42 | 69% | 2025-06-26 | 11个月 | FBA | -
- `B0FSLLJ8SZ`: 14,507 | 10,742 | 44% | 346 | 67.33% | $8,993 | 200+ | $6K+ | 2 | $25.99 | - | 55 | - | 4.3 | - | $4.46 | 75% | 2025-10-31 | 7个月 | FBA | -
- `B0GRH6MY39`: 35,296 | 8,084 | 19% | 190 | 50% | $7,598 | 100+ | $3K+ | 1 | $39.99 | - | 48 | 3 | 4.5 | 1.58% | $5.72 | 78% | 2026-03-09 | 3个月 | FBA | -
- `B0GGR1T98P`: 38,926 | 6,292 | 15% | 239 | 116.81% | $5,734 | 200+ | $5K+ | 1 | $23.99 | - | 40 | 17 | 4.3 | 7.11% | $4.87 | 72% | 2026-03-14 | 2个月 | FBA | -
- `B0DB8J4T52`: 83,972 | 4,646 | 5% | 106 | 6.19% | $2,640 | - | - | 1 | $24.91 | - | 150 | 4 | 4.3 | 3.77% | $5.33 | 71% | 2024-09-27 | 1年 8个月 | FBA | -

---

<!-- source: products/decorative_trays.md -->
# Decorative Trays 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays`
> 共抓取 **14** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **14** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $22.23　均Reviews 466（中等）　重量 1.45lbs（轻）　退货率 9.52%（高）　品牌集中度 42.1%（中等）　中国卖家 78.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0D8TJDXRY](https://www.amazon.com/dp/B0D8TJDXRY) |  | PEMAR Mother of Pearl Decorative Tray | 253 / 15.42% | $11,625 | $45.95 | $6.86 (15%) | 102 / 3 | 4.7 | $7.38 / 69% | 3 | 79 | 1 | 2.89 pounds | 2024-07-22 1年 10个月 |
| 2 | [B0BMDLHHYT](https://www.amazon.com/dp/B0BMDLHHYT) |  | Round Clawfoot Dish | 247 / 16.81% | $10,621 | $43.00 | $6.66 (15%) | 109 / 3 | 4.3 | $4.09 / 75% | 2 | 76 | 1 | 0.46 pounds | 2022-11-16 3年 6个月 |
| 3 | [B0FL2236YS](https://www.amazon.com/dp/B0FL2236YS) |  | PU Leather Valet Tray Organizer | 440 / 6.5% | $9,676 | $21.99 | $3.41 (15%) | 54 / 8 | 4.9 | $5.61 / 59% | 4 | 27 | 1 | 1.09 pounds | 2025-09-17 8个月 |
| 4 | [B0DT1X5W9W](https://www.amazon.com/dp/B0DT1X5W9W) |  | Serving Acacia Wood Valet Tray for Men Women | 371 / 28.4% | $8,529 | $22.99 | $3.54 (15%) | 56 / 7 | 4.6 | $4.28 / 66% | 2 | 31 | 1 | 0.04 pounds | 2025-02-22 1年 3个月 |
| 5 | [B0B24B6TPX](https://www.amazon.com/dp/B0B24B6TPX) |  | Handwoven Multipurpose Rectangle Rattan Tray, 20” x 12” | 170 / 137.04% | $6,798 | $39.99 | $6.15 (15%) | 138 / 2 | 4.2 | $12.25 / 54% | 1 | 100 | 1 | 2.15 pounds | 2022-09-12 3年 9个月 |
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

**5. [B0B24B6TPX](https://www.amazon.com/dp/B0B24B6TPX)** Handwoven Multipurpose Rectangle Rattan Tray, 20” x 12” – Durable Wicker Tray with Leather Handles for Home Decor Display

**6. [B0DYP3TRL2](https://www.amazon.com/dp/B0DYP3TRL2)** FoldTier 11 Pcs 4th of July Decoration Patriotic Tiered Tray Decor Independence Day Table Sign Wooden Faux Book Stack Firework Sign 250th Anniversary Tabletop Centerpieces for Home Office Memorial Day

**7. [B0DRYD63RT](https://www.amazon.com/dp/B0DRYD63RT)** 12 Inch Golden Round Platter Tray, Trays for Domestic Purposes, Stainless Steel Serving, Circle Decorative Tray, Vanity Tray for Centerpiece Home Decor

**8. [B0G3TS1YFT](https://www.amazon.com/dp/B0G3TS1YFT)** Vintage Brass Decorative Tray, 11.8-Inch Round Serving Tray with Claw Feet, Decorative Coffee Table Tray for Dining Room, Entryway, Living Room

**9. [B0D8MW6VS1](https://www.amazon.com/dp/B0D8MW6VS1)** Flamingo Zen Garden Kit for Desk, Cute Japanese Flamingos Gifts for Women, Mini Zen Garden Sand Tray, Pink Room Decor Aesthetic, Home Office Desk Decorations, Sand Therapy Kit

**10. [B0CRVTY72B](https://www.amazon.com/dp/B0CRVTY72B)** INNObeta Son in Law Gifts Valet Tray from Dad, Mom, Desktop Storage Organizer PU Leather Bedside Tray Key Coin Holder for Birthday, Christmas

**11. [B0CCVNCZWZ](https://www.amazon.com/dp/B0CCVNCZWZ)** INNObeta Son Gifts Valet Tray from Dad Mom, Desktop Storage Organizer PU Leather Bedside Tray Key Coin Holder, Perfect for Birthday, Christmas - to My Son

**12. [B0FK99K3D4](https://www.amazon.com/dp/B0FK99K3D4)** Acacia Wood Decorative Tray for Home Decor, 14'' x 10'' Wooden Serving Tray for Coffee Table Centerpiece Dining Kitchen Island Decoration Bathroom Counter Display

**13. [B0D5H5TRRD](https://www.amazon.com/dp/B0D5H5TRRD)** Round Burnt Wood Serving Tray with Beads, Wooden Decorative Tray for Entertaining, Decoration, and Gifting,

**14. [B0F2HXLN8V](https://www.amazon.com/dp/B0F2HXLN8V)** Scalloped Acrylic Tray with Magnetic Mat - 8x8in Customizable Display for Photos, Art & Notes | Non-Slip Base | Elegant Décor & Organizer for Jewelry/Cosmetics for Women/Mom/Weddings

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

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
- `B0FK99K3D4`: 278,209 | 46,599 | 15% | **** | **** | **** | **** | 2 | $31.99 | - | 10 | 3 | 4.9 | 2.91% | **** | 2025-08-03 | 10个月 | FBA | -
- `B0D5H5TRRD`: 384,945 | 14,603 | 5% | **** | **** | **** | **** | 4 | $27.59 | - | 121 | 2 | 4.6 | 1.68% | **** | 2024-08-06 | 1年 10个月 | FBA | -
- `B0F2HXLN8V`: 206,686 | 95,045 | 32% | **** | **** | **** | **** | 4 | $22.09 | - | 36 | - | 4.9 | - | **** | 2025-04-01 | 1年 2个月 | FBA | -

---

<!-- source: products/electrical_system_tools.md -->
# Electrical System Tools 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Automotive › Tools & Equipment › Electrical System Tools`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $29.48　均Reviews 437（中等）　重量 0.99lbs（轻）　退货率 2.38%（低）　品牌集中度 43.9%（中等）　中国卖家 82.0%

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

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0C4PTWP8G`: 38,438 | 13,642 | 26% | 184 | 9.58% | $6,622 | 100+ | $3K+ | 3 | $35.99 | - | 80 | 2 | 4.4 | 1.09% | $3.57 | 75% | 2023-05-09 | 3年 1个月 | FBA | -
- `B0CR6F2HR1`: 28,712 | 21,985 | 43% | 204 | 11.6% | $6,118 | 100+ | $2K+ | 1 | $29.99 | - | 91 | 1 | 4.2 | 0.49% | $4.28 | 71% | 2024-01-08 | 2年 5个月 | FBA | -
- `B0GHDJM616`: 26,530 | 28,394 | 52% | 221 | 29.94% | $5,965 | 100+ | $2K+ | 2 | $26.99 | - | 36 | 6 | 4.8 | 2.71% | $6.48 | 61% | 2026-02-19 | 3个月 | FBA | -
- `B0FDVDL457`: 23,854 | 7,645 | 24% | 232 | 42% | $5,102 | 100+ | $2K+ | 1 | $21.99 | - | 64 | 2 | 4.4 | 0.86% | $5.22 | 61% | 2025-10-17 | 7个月 | FBA | -

---

<!-- source: products/game_mats_boards.md -->
# Game Mats & Boards 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $29.62　均Reviews 308（中等）　重量 2.47lbs（重）　退货率 7.5%（中）　品牌集中度 40.3%（中等）　中国卖家 78.0%

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

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0FQ5KW2WN`: 20,800 | 14,276 | 41% | 335 | 69.3% | $10,013 | 200+ | $5K+ | 2 | $29.89 | - | 42 | 10 | 4.9 | 2.99% | $10.11 | 51% | 2025-11-09 | 7个月 | FBA | -
- `B0FMXW89J5`: 148,268 | 8,494 | 17% | 183 | 8.56% | $5,488 | - | - | 1 | $29.99 | - | 6 | 2 | 4.1 | 1.09% | $10.11 | 54% | 2025-10-11 | 8个月 | FBA | -
- `B0DD6X3QTH`: 55,693 | 42,912 | 44% | 124 | 45.07% | $4,959 | 100+ | $3K+ | 1 | $39.99 | - | 71 | 5 | 4.5 | 4.03% | $10.50 | 59% | 2024-09-17 | 1年 8个月 | FBA | -
- `B0GHHG1W42`: 41,419 | 1,500 | 3% | 194 | 56.36% | $4,072 | 100+ | $2K+ | 5 | $20.99 | - | 10 | 3 | 4.9 | 1.55% | $5.61 | 58% | 2026-03-26 | 2个月 | FBA | -
- `B0GQMQCCNH`: 52,467 | 36,206 | 41% | 128 | 21.3% | $3,967 | 50+ | $1K+ | 5 | $30.99 | - | 11 | 7 | 4.3 | 5.47% | $6.02 | 66% | 2026-04-21 | 1个月 | FBA | -

---

<!-- source: products/grinding_discs.md -->
# Grinding Discs 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $23.53　均Reviews 360（中等）　重量 2.02lbs（重）　退货率 2.13%（低）　品牌集中度 46.8%（中等）　中国卖家 81.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DB1B6DKZ](https://www.amazon.com/dp/B0DB1B6DKZ) |  | 11PCS Wood Carving Disc Set for 4" or 4 1/2" Angle Grinder | 671 / 85.42% | $26,833 | $39.99 | $4.70 (12%) | 132 / 9 | 4.6 | $7.30 / 70% | 1 | 7 | 1 | 3.12 pounds | 2024-09-06 1年 9个月 |
| 2 | [B0CBS4VWYB](https://www.amazon.com/dp/B0CBS4VWYB) |  | 4 in.x 5/8-11 in. Smooth Grinding Resin Filled Diamond Cup Wheel… | 101 / 134.78% | $5,655 | $55.99 | $6.83 (12%) | 28 / 2 | 4.0 | $5.49 / 78% | 3 | 135 | 1 | 1.1 pounds | 2023-08-28 2年 9个月 |

## 二、完整商品标题

**1. [B0DB1B6DKZ](https://www.amazon.com/dp/B0DB1B6DKZ)** 11PCS Wood Carving Disc Set for 4" or 4 1/2" Angle Grinder, Stump Tool Grinding Wheel Disc with 5/8" Adapter Ring, Woodworking Grinder Attachment for Cutting Shaping Carving Sanding Polishing

**2. [B0CBS4VWYB](https://www.amazon.com/dp/B0CBS4VWYB)** 4 in.x 5/8-11 in. Smooth Grinding Resin Filled Diamond Cup Wheel for Angle Grinder, Resin Filled Diamond Grinding Wheel for Granite Marble Engineered Stone

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0DB1B6DKZ`: 5,410 | 1,544 | 22% | 671 | 85.42% | $26,833 | 600+ | $23K+ | 1 | $39.99 | - | 132 | 9 | 4.6 | 1.34% | $7.30 | 70% | 2024-09-06 | 1年 9个月 | FBA | -
- `B0CBS4VWYB`: 58,429 | 25,781 | 31% | 101 | 134.78% | $5,655 | - | - | 3 | $55.99 | 4 | 28 | 2 | 4.0 | 1.98% | $5.49 | 78% | 2023-08-28 | 2年 9个月 | FBA | -

---

<!-- source: products/lighting_products.md -->
# Lighting Products 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $47.85　均Reviews 482（中等）　重量 1.72lbs（偏重）　退货率 6.75%（中）　品牌集中度 51.9%（中等）　中国卖家 74.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0G6L569ZB](https://www.amazon.com/dp/B0G6L569ZB) |  | Rechargeable Submersible Pool Lights with Remote | 815 / 158.46% | $48,052 | $58.96 | $8.75 (15%) | 39 / 11 | 4.4 | $6.58 / 74% | 2 | 37 | 1 | 2.37 pounds | 2026-03-09 3个月 |
| 2 | [B0GD7YRTDM](https://www.amazon.com/dp/B0GD7YRTDM) |  | APONUO Solar Pool Lights | 814 / 162.85% | $34,994 | $42.99 | $6.32 (15%) | 40 / 10 | 4.1 | $5.72 / 72% | 3 | 34 | 1 | 1.26 pounds | 2026-03-26 2个月 |
| 3 | [B0GJCRX242](https://www.amazon.com/dp/B0GJCRX242) |  | Solar Floating Pool Lights | 822 / 137.86% | $27,118 | $32.99 | $5.02 (15%) | 58 / 25 | 4.0 | $5.87 / 67% | 1 | 42 | 1 | 1.32 pounds | 2026-03-19 2个月 |
| 4 | [B0DZD1RC33](https://www.amazon.com/dp/B0DZD1RC33) |  | Solar Floating Pool Lights | 518 / 88.36% | $23,818 | $45.98 | $6.86 (15%) | 132 / 11 | 4.4 | $6.01 / 72% | 2 | 100 | 2 | 2.18 pounds | 2025-05-21 1年 |
| 5 | [B0DSHT56KC](https://www.amazon.com/dp/B0DSHT56KC) |  | 500W R40 120V Pool Light Bulb for Inground Pool & Spa | 287 / 22.34% | $17,217 | $59.99 | $9.03 (15%) | 21 / - | 4.7 | $7.17 / 73% | 2 | 153 | 2 | 0.71 pounds | 2025-03-02 1年 3个月 |
| 6 | [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF) |  | Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool… | 423 / 148.32% | $16,916 | $39.99 | $6.05 (15%) | 31 / 7 | 4.4 | $4.35 / 74% | 2 | 88 | 1 | 0.44 pounds | 2025-05-07 1年 1个月 |
| 7 | [B0G6Z1QM2M](https://www.amazon.com/dp/B0G6Z1QM2M) |  | Floating Pool Lights Solar Powered | 446 / 50.41% | $13,376 | $29.99 | $4.59 (15%) | 55 / 18 | 4.6 | $5.61 / 66% | 2 | 102 | 1 | 1.37 pounds | 2026-02-07 4个月 |
| 8 | [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H) |  | SIEDiNLAR Solar Floating Pool Lights with Remote | 358 / 145.11% | $12,884 | $35.99 | $5.29 (15%) | 36 / 11 | 4.0 | $5.87 / 69% | 2 | 135 | 1 | 1.57 pounds | 2026-04-05 2个月 |
| 9 | [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB) |  | 55ft Solar Pool Lights for Above Ground Pools | 538 / 183.92% | $11,293 | $20.99 | $3.10 (15%) | 117 / 9 | 4.0 | $4.46 / 64% | 4 | 77 | 1 | 0.73 pounds | 2025-02-28 1年 3个月 |
| 10 | [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC) |  | Floating Pool Lights | 359 / 146.4% | $10,759 | $29.97 | $4.43 (15%) | 30 / 12 | 4.9 | $5.76 / 66% | 2 | 94 | 1 | 1.53 pounds | 2026-04-21 1个月 |
| 11 | [B0DSD4NWXN](https://www.amazon.com/dp/B0DSD4NWXN) |  | Askyli Floating Pool Lights Solar with Remote | **** / **** | **** | $39.99 | - | 138 / 4 | 4.1 | **** /  | 2 | 97 | 1 | 2.62 pounds | 2025-04-27 1年 1个月 |
| 12 | [B0FWJ6C4CY](https://www.amazon.com/dp/B0FWJ6C4CY) |  | Askyli Pool Lights for Above Ground Pools | **** / **** | **** | $25.16 | - | 36 / 9 | 4.2 | **** /  | 3 | 108 | 1 | 1.43 pounds | 2026-03-07 3个月 |
| 13 | [B0G6SLH595](https://www.amazon.com/dp/B0G6SLH595) |  | Floating Pool Lights w/Remote | **** / **** | **** | $36.99 | - | 39 / 1 | 4.7 | **** /  | 3 | 120 | 1 | 2.12 pounds | 2026-03-14 2个月 |
| 14 | [B0CX9162PJ](https://www.amazon.com/dp/B0CX9162PJ) |  | BOXPSII Pool Lights(4 Pack) | **** / **** | **** | $52.99 | - | 148 / 2 | 4.2 | **** /  | 3 | 187 | 1 | 1.79 pounds | 2024-04-19 2年 1个月 |
| 15 | [B0G8X6721P](https://www.amazon.com/dp/B0G8X6721P) |  | Pool Lights for Inground & Above Ground Pool | **** / **** | **** | $26.84 | - | 20 / 6 | 4.4 | **** /  | 2 | 98 | 1 | 1.23 pounds | 2026-04-07 2个月 |
| 16 | [B0FWC5JQL9](https://www.amazon.com/dp/B0FWC5JQL9) |  | 500W R40 120V Pool Lights Bulb for Inground Pool & Spa | **** / **** | **** | $53.99 | - | 14 / 3 | 4.6 | **** /  | 1 | 219 | 2 | 0.71 pounds | 2025-11-18 6个月 |
| 17 | [B0D93J8T91](https://www.amazon.com/dp/B0D93J8T91) |  | LED Pool Light Bulb 12V 50W 5000LM 6500K Daylight White LED Swimm… | **** / **** | **** | $37.99 | - | 77 / 3 | 4.0 | **** /  | 1 | 288 | 1 | 0.68 pounds | 2024-08-08 1年 10个月 |
| 18 | [B0DN6FBDDQ](https://www.amazon.com/dp/B0DN6FBDDQ) |  | Tujoe Remote Control LED Pool Lights for Above Ground Pools Subme… | **** / **** | **** | $30.99 | - | 32 / 1 | 4.0 | **** /  | 2 | 246 | 1 | 1.59 pounds | 2024-11-16 1年 6个月 |
| 19 | [B0GCZ27BY1](https://www.amazon.com/dp/B0GCZ27BY1) |  | Qoolife Pool Chlorine Floater with Thermometer Solar Light | **** / **** | **** | $29.99 | - | 34 / 19 | 4.0 | **** /  | 1 | 336 | 1 | 1.21 pounds | 2026-03-29 2个月 |
| 20 | [B0GL8DTBM6](https://www.amazon.com/dp/B0GL8DTBM6) |  | Solar Floating Pool Lights: Solar Pool Lights That Float with Rem… | **** / **** | **** | $23.99 | - | 31 / 9 | 4.2 | **** /  | 3 | 288 | 2 | 0.93 pounds | 2026-03-25 2个月 |

## 二、完整商品标题

**1. [B0G6L569ZB](https://www.amazon.com/dp/B0G6L569ZB)** Rechargeable Submersible Pool Lights with Remote, 5000mAh Underwater Led Pool Light for Above Ground Pool Lights Waterproof, 9 Modes Color Changing Magnetic Swimming Inground Pool Lights-2PC

**2. [B0GD7YRTDM](https://www.amazon.com/dp/B0GD7YRTDM)** APONUO Solar Pool Lights, IP68 Waterproof Floating Pool Lights with Remote& Button Control, 9 Lighting Colors& 3 Modes Pool Solar Light, Timer&Memory, Floating Light for Pool, Party, Bathtub (2 Pack)

**3. [B0GJCRX242](https://www.amazon.com/dp/B0GJCRX242)** Solar Floating Pool Lights, Outdoor LED Pool Lighted that Float with Remote, IP68 Waterproof Swimming Decor Lighting for Inground Pool, Above Ground Pools, Pond, 2 Pack

**4. [B0DZD1RC33](https://www.amazon.com/dp/B0DZD1RC33)** Solar Floating Pool Lights, 14 Inch Flame Solar Pool Light Balls, Floating Glow Globe IP68 Waterproof, Inflatable Solar Lights up Balls for Swimming Pool Pond Outdoor Decor -4PCS

**5. [B0DSHT56KC](https://www.amazon.com/dp/B0DSHT56KC)** 500W R40 120V Pool Light Bulb for Inground Pool & Spa – 3000K Warm White, E26 Base, High-Power, Compatible with Pentair & Hayward Fixtures, 3,000-Hour Lifespan (2 Pack)

**6. [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF)** Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool Light Bulb Daylight White 6000K Swimming Pool Replacement for Most Pentair Hayward Light Fixtures (120V 65W)

**7. [B0G6Z1QM2M](https://www.amazon.com/dp/B0G6Z1QM2M)** Floating Pool Lights Solar Powered, 16'' Inflatable Waterproof Clownfish Solar Pool Lights that Float, Auto On/Off LED Floating Lights for Pool Garden Backyard Outdoor Decoration - (2 Piece)

**8. [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H)** SIEDiNLAR Solar Floating Pool Lights with Remote, 12 Modes RGB Color Changing Solar Powered Pool Lights, Waterproof Floating Lights for Swimming Pool, Pond, Fountain, Backyard & Party Decor (4 Pack)

**9. [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB)** 55ft Solar Pool Lights for Above Ground Pools, 150 LEDs Remote IP65 Waterproof Rope Lights, 8 Color Modes, Swimming Frame Pool Decor Accessories for Outdoor Outside Trampoline Camping

**10. [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC)** Floating Pool Lights, 15" Inflatable Solar Powered Pool Lights That Float, Color Changing LED Glow Balls, IP68 Waterproof Solar Floating Light Up Balls for Pool,Pond, Outdoor Party Decor - 2PCS

**11. [B0DSD4NWXN](https://www.amazon.com/dp/B0DSD4NWXN)** Askyli Floating Pool Lights Solar with Remote, 7.6 Inch RGB Up and Down Color Changing Solar Pool Lights that Float with Dynamic Lighting Effects, Floating Light for Pools, Party, Decor(2)

**12. [B0FWJ6C4CY](https://www.amazon.com/dp/B0FWJ6C4CY)** Askyli Pool Lights for Above Ground Pools, Upgraded Rechargeable Dynamic Lighting Inground Pool Lights that Float w/Remote, 16H Runtimes Underwater LED Pools Light with Timer Off for Hot Tub Pond-2PC

**13. [B0G6SLH595](https://www.amazon.com/dp/B0G6SLH595)** Floating Pool Lights w/Remote, 6.5" Top to Bottom Dynamic Color Changing Solar Pool Lights that Float, IP68 Waterproof Solar Floating Light for Inground Above Ground Pools Garden Decor(2)

**14. [B0CX9162PJ](https://www.amazon.com/dp/B0CX9162PJ)** BOXPSII Pool Lights(4 Pack), Upgraded Rechargeable Submersible LED Lights with Remote, IP68 Waterproof 16 Color Floating Light with Magnet, Pool Light for Above Ground Inground Pools,Hot Tub, Bath

**15. [B0G8X6721P](https://www.amazon.com/dp/B0G8X6721P)** Pool Lights for Inground & Above Ground Pool, Underwater Submersible Swimming LED Pool Light with Remote Control,Waterproof Magnetic Pools Lights for Inground Above Ground Pools,Hot tub-1 PC

**16. [B0FWC5JQL9](https://www.amazon.com/dp/B0FWC5JQL9)** 500W R40 120V Pool Lights Bulb for Inground Pool & Spa – 3000K Warm White, E26 Base, High-Power, Compatible with Pentair & Hayward Fixtures, 3,000-Hour Lifespan (2 Pack)

**17. [B0D93J8T91](https://www.amazon.com/dp/B0D93J8T91)** LED Pool Light Bulb 12V 50W 5000LM 6500K Daylight White LED Swimming Pool Light Bulb, Replaces up to 200-800W Traditionnal Bulb for Most Pentair Hayward Light Fixtures（NOT 120V）

**18. [B0DN6FBDDQ](https://www.amazon.com/dp/B0DN6FBDDQ)** Tujoe Remote Control LED Pool Lights for Above Ground Pools Submersible Waterproof Outdoor LED Rim Rope Lights with Battery Box, Waterproof Bundle Pocket for Outdoor(55.7ft Fits18ft Pool)

**19. [B0GCZ27BY1](https://www.amazon.com/dp/B0GCZ27BY1)** Qoolife Pool Chlorine Floater with Thermometer Solar Light, 3 in1Chlorine Floater for Pond Fit 1" and 3", Floating Dispenser with Remote and Adjustable for Pool Spa Hot Tub

**20. [B0GL8DTBM6](https://www.amazon.com/dp/B0GL8DTBM6)** Solar Floating Pool Lights: Solar Pool Lights That Float with Remote, 7 Lighting, RGB 6 Dynamic Modes, IP68 Waterproof Swimming Pool Lights for Inground Pool Bathtub Party Garden Weeding (2 Pack)

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0G6L569ZB`: 9,861 | 555 | 5% | 815 | 158.46% | $48,052 | 600+ | $35K+ | 2 | $58.96 | - | 39 | 11 | 4.4 | 1.35% | $6.58 | 74% | 2026-03-09 | 3个月 | FBA | -
- `B0GD7YRTDM`: 9,432 | 2,514 | 21% | 814 | 162.85% | $34,994 | 500+ | $22K+ | 3 | $42.99 | - | 40 | 10 | 4.1 | 1.23% | $5.72 | 72% | 2026-03-26 | 2个月 | FBA | -
- `B0GJCRX242`: 9,176 | 11,610 | 56% | 822 | 137.86% | $27,118 | 700+ | $26K+ | 1 | $32.99 | - | 58 | 25 | 4.0 | 3.04% | $5.87 | 67% | 2026-03-19 | 2个月 | FBA | -
- `B0DZD1RC33`: 22,594 | 941 | 4% | 518 | 88.36% | $23,818 | 400+ | $18K+ | 2 | $45.98 | - | 132 | 11 | 4.4 | 2.12% | $6.01 | 72% | 2025-05-21 | 1年 | FBA | -
- `B0DSHT56KC`: 33,045 | 7,232 | 18% | 287 | 22.34% | $17,217 | 200+ | $11K+ | 2 | $59.99 | - | 21 | - | 4.7 | - | $7.17 | 73% | 2025-03-02 | 1年 3个月 | FBA | -
- `B0DXVSDMZF`: 21,990 | 2,628 | 11% | 423 | 148.32% | $16,916 | 200+ | $7K+ | 2 | $39.99 | - | 31 | 7 | 4.4 | 1.65% | $4.35 | 74% | 2025-05-07 | 1年 1个月 | FBA | -
- `B0G6Z1QM2M`: 22,821 | 3,198 | 12% | 446 | 50.41% | $13,376 | 300+ | $9K+ | 2 | $29.99 | - | 55 | 18 | 4.6 | 4.04% | $5.61 | 66% | 2026-02-07 | 4个月 | FBA | -
- `B0GPW9YT5H`: 28,375 | 1,218 | 4% | 358 | 145.11% | $12,884 | 200+ | $7K+ | 2 | $35.99 | - | 36 | 11 | 4.0 | 3.07% | $5.87 | 69% | 2026-04-05 | 2个月 | FBA | -
- `B0DWMMYNDB`: 18,386 | 2,081 | 10% | 538 | 183.92% | $11,293 | 200+ | $3K+ | 4 | $20.99 | - | 117 | 9 | 4.0 | 1.67% | $4.46 | 64% | 2025-02-28 | 1年 3个月 | FBA | -
- `B0GRTPX9DC`: 22,372 | 10,423 | 30% | 359 | 146.4% | $10,759 | 200+ | $6K+ | 2 | $29.97 | - | 30 | 12 | 4.9 | 3.34% | $5.76 | 66% | 2026-04-21 | 1个月 | FBA | -
- `B0DSD4NWXN`: 22,465 | 12,329 | 35% | **** | **** | **** | **** | 2 | $39.99 | - | 138 | 4 | 4.1 | 1.31% | **** | 2025-04-27 | 1年 1个月 | FBA | -
- `B0FWJ6C4CY`: 23,928 | 10,462 | 30% | **** | **** | **** | **** | 3 | $25.16 | - | 36 | 9 | 4.2 | 2.81% | **** | 2026-03-07 | 3个月 | FBA | -
- `B0G6SLH595`: 27,486 | 13,081 | 32% | **** | **** | **** | **** | 3 | $36.99 | - | 39 | 1 | 4.7 | 0.49% | **** | 2026-03-14 | 2个月 | FBA | -
- `B0CX9162PJ`: 49,291 | 7,016 | 9% | **** | **** | **** | **** | 3 | $52.99 | - | 148 | 2 | 4.2 | 1.49% | **** | 2024-04-19 | 2年 1个月 | FBA | -
- `B0G8X6721P`: 23,221 | 13,401 | 37% | **** | **** | **** | **** | 2 | $26.84 | - | 20 | 6 | 4.4 | 2.78% | **** | 2026-04-07 | 2个月 | FBA | -
- `B0FWC5JQL9`: 60,424 | 33,248 | 36% | **** | **** | **** | **** | 1 | $53.99 | - | 14 | 3 | 4.6 | 2.86% | **** | 2025-11-18 | 6个月 | FBA | -
- `B0D93J8T91`: 57,438 | 7,874 | 12% | **** | **** | **** | **** | 1 | $37.99 | - | 77 | 3 | 4.0 | 2.01% | **** | 2024-08-08 | 1年 10个月 | FBA | -
- `B0DN6FBDDQ`: 45,307 | 4,504 | 9% | **** | **** | **** | **** | 2 | $30.99 | - | 32 | 1 | 4.0 | 0.74% | **** | 2024-11-16 | 1年 6个月 | FBA | -
- `B0GCZ27BY1`: 44,536 | 45,214 | 50% | **** | **** | **** | **** | 1 | $29.99 | - | 34 | 19 | 4.0 | 16.67% | **** | 2026-03-29 | 2个月 | FBA | -
- `B0GL8DTBM6`: 71,193 | 54,323 | 44% | **** | **** | **** | **** | 3 | $23.99 | - | 31 | 9 | 4.2 | 8.11% | **** | 2026-03-25 | 2个月 | FBA | -

---

<!-- source: products/nozzles.md -->
# Nozzles 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles`
> 共抓取 **0** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $26.24　均Reviews 490（中等）　重量 0.44lbs（轻）　退货率 2.63%（低）　品牌集中度 53.8%（中等）　中国卖家 74.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|

## 二、完整商品标题

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

---

<!-- source: products/paddleboard_accessories.md -->
# Paddleboard Accessories 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $53.08　均Reviews 322（中等）　重量 2.37lbs（重）　退货率 4.17%（低）　品牌集中度 42.7%（中等）　中国卖家 72.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DJT1YH6F](https://www.amazon.com/dp/B0DJT1YH6F) |  | Vitality Sports Golf Chipping Net | 999 / 27.16% | $45,924 | $45.97 | $7.02 (15%) | 106 / 7 | 4.6 | $7.23 / 69% | 2 | 3 | 2 | 3.24 pounds | 2024-11-07 1年 7个月 |
| 2 | [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT) |  | Suspension Straps Trainer with Built-in Door Anchor | 855 / 7.98% | $42,741 | $49.99 | $7.69 (15%) | 101 / 21 | 4.6 | $6.31 / 72% | 1 | 4 | 1 | 2.31 pounds | 2025-06-07 1年 |
| 3 | [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3) |  | Boat Stern Light Anchor Light | 856 / 29.64% | $36,799 | $42.99 | $6.66 (15%) | 30 / 13 | 4.9 | $10.11 / 61% | 3 | 14 | 1 | 1.25 pounds | 2026-03-31 2个月 |
| 4 | [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q) |  | SILCA Ultimate Sealant Bottle | 749 / 7.13% | $33,698 | $44.99 | $6.57 (15%) | 140 / - | 4.5 | $6.48 / 71% | 4 | 19 | 1 | 2.51 pounds | 2025-02-16 1年 3个月 |
| 5 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 789 / 11.11% | $31,552 | $39.99 | $5.91 (15%) | 110 / 13 | 4.7 | $4.09 / 75% | 4 | 19 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 6 | [B0G93DF8CJ](https://www.amazon.com/dp/B0G93DF8CJ) |  | Exun Soccer Fan Gift Basket Set 2026 | 1,000 / 102.84% | $29,990 | $29.99 | $4.37 (15%) | 58 / 16 | 4.8 | $6.13 / 65% | 1 | 163 | 1 | 1.87 pounds | 2026-02-20 3个月 |
| 7 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 8 | [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP) |  | Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner | 890 / 34.88% | $28,471 | $31.99 | $4.87 (15%) | 118 / 4 | 4.5 | $4.09 / 72% | 3 | 7 | 1 | 0.29 pounds | 2024-02-06 2年 4个月 |
| 9 | [B0DRFSFCYQ](https://www.amazon.com/dp/B0DRFSFCYQ) |  | Telescoping Boat Hook for Docking | 678 / 103.33% | $28,469 | $41.99 | $6.11 (15%) | 138 / 13 | 4.6 | $12.37 / 56% | 2 | 5 | 1 | 2.65 pounds | 2025-01-26 1年 4个月 |
| 10 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 740 / 54.21% | $28,113 | $37.99 | $5.64 (15%) | 127 / 7 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 11 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | **** / **** | **** | $35.99 | - | 125 / 37 | 4.6 | **** /  | 3 | 64 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 12 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 13 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 85 / 15 | 4.5 | **** /  | 1 | 22 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 14 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 15 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 5 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 2个月 |
| 16 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 17 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |
| 18 | [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64) |  | GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men | **** / **** | **** | $49.99 | - | 97 / - | 4.5 | **** /  | 5 | 19 | 1 | 1.3 pounds | 2025-03-28 1年 2个月 |
| 19 | [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF) |  | Grip Enhancer Tacky Towel | **** / **** | **** | $36.99 | - | 125 / - | 4.5 | **** /  | 2 | 34 | 2 | 0.29 pounds | 2024-12-17 1年 5个月 |
| 20 | [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH) |  | Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdo… | **** / **** | **** | $36.95 | - | 111 / 3 | 4.8 | **** /  | 3 | 77 | 2 | 0.2 pounds | 2025-03-14 1年 2个月 |

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

**11. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**12. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**13. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**14. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**15. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**16. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**17. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

**18. [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64)** GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men, Natural Rattan Wicker Bike Baskets for Adult Bikes, Basket for Bikes with Liner, Bicycle Baskets for Beach Cruiser

**19. [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF)** Grip Enhancer Tacky Towel - USA-Made Chalkless Competition-Approved Formula for Golf, Tennis, Softball and More - Versatile Multi-Sport Moisture Control for Sweaty Hands

**20. [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH)** Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdoor Headlamp with Multiple Color Temperatures Warm Natural, Cold Lights and Red Light (Elastic Cord, Black)

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0DJT1YH6F`: 6,744 | 1,208 | 15% | 999 | 27.16% | $45,924 | 700+ | $27K+ | 2 | $45.97 | - | 106 | 7 | 4.6 | 0.7% | $7.23 | 69% | 2024-11-07 | 1年 7个月 | FBA | -
- `B0F5BD54RT`: 10,137 | 2,307 | 19% | 855 | 7.98% | $42,741 | 700+ | $34K+ | 1 | $49.99 | - | 101 | 21 | 4.6 | 2.46% | $6.31 | 72% | 2025-06-07 | 1年 | FBA | -
- `B0GKMGJLL3`: 10,790 | 2,203 | 17% | 856 | 29.64% | $36,799 | 600+ | $25K+ | 3 | $42.99 | - | 30 | 13 | 4.9 | 1.52% | $10.11 | 61% | 2026-03-31 | 2个月 | FBA | -
- `B0DX2F3V5Q`: 11,637 | 0 | 0% | 749 | 7.13% | $33,698 | 300+ | $13K+ | 4 | $44.99 | - | 140 | - | 4.5 | - | $6.48 | 71% | 2025-02-16 | 1年 3个月 | FBA | -
- `B0DTP76XQP`: 10,207 | 353 | 3% | 789 | 11.11% | $31,552 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 13 | 4.7 | 1.65% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0G93DF8CJ`: 4,786 | 3,333 | 41% | 1,000 | 102.84% | $29,990 | 900+ | $27K+ | 1 | $29.99 | - | 58 | 16 | 4.8 | 1.6% | $6.13 | 65% | 2026-02-20 | 3个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0CTQTYVGP`: 8,500 | 227 | 3% | 890 | 34.88% | $28,471 | 400+ | $12K+ | 3 | $31.99 | - | 118 | 4 | 4.5 | 0.45% | $4.09 | 72% | 2024-02-06 | 2年 4个月 | FBA | -
- `B0DRFSFCYQ`: 13,590 | 25 | 0% | 678 | 103.33% | $28,469 | 500+ | $20K+ | 2 | $41.99 | - | 138 | 13 | 4.6 | 1.92% | $12.37 | 56% | 2025-01-26 | 1年 4个月 | FBA | -
- `B0DS2CBVFT`: 8,379 | 2,034 | 20% | 740 | 54.21% | $28,113 | 300+ | $11K+ | 5 | $37.99 | - | 127 | 7 | 4.8 | 0.95% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0GL785GSP`: 13,539 | 268 | 2% | **** | **** | **** | **** | 3 | $35.99 | - | 125 | 37 | 4.6 | 5.05% | **** | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0F9ZZ17Z8`: 13,699 | 581 | 4% | **** | **** | **** | **** | 1 | $41.97 | - | 85 | 15 | 4.5 | 2.42% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0CT5MVCFD`: 17,365 | 1,868 | 10% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 5 | 4.8 | 0.95% | **** | 2024-03-14 | 2年 2个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -
- `B0DS23SX64`: 15,152 | 0 | 0% | **** | **** | **** | **** | 5 | $49.99 | - | 97 | - | 4.5 | - | **** | 2025-03-28 | 1年 2个月 | FBA | -
- `B0DNZX4MZF`: 13,386 | 0 | 0% | **** | **** | **** | **** | 2 | $36.99 | - | 125 | - | 4.5 | - | **** | 2024-12-17 | 1年 5个月 | FBA | -
- `B0DY2SW4CH`: 12,094 | 943 | 7% | **** | **** | **** | **** | 3 | $36.95 | - | 111 | 3 | 4.8 | 0.47% | **** | 2025-03-14 | 1年 2个月 | FBA | -

---

<!-- source: products/scan_principles.md -->
# 选品原则 (2026-06-14)

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
# Swing Trainers 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $37.01　均Reviews 448（中等）　重量 0.71lbs（轻）　退货率 4.37%（低）　品牌集中度 57.1%（中等）　中国卖家 68.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DJT1YH6F](https://www.amazon.com/dp/B0DJT1YH6F) |  | Vitality Sports Golf Chipping Net | 999 / 27.16% | $45,924 | $45.97 | $7.02 (15%) | 106 / 7 | 4.6 | $7.23 / 69% | 2 | 3 | 2 | 3.24 pounds | 2024-11-07 1年 7个月 |
| 2 | [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT) |  | Suspension Straps Trainer with Built-in Door Anchor | 855 / 7.98% | $42,741 | $49.99 | $7.69 (15%) | 101 / 21 | 4.6 | $6.31 / 72% | 1 | 4 | 1 | 2.31 pounds | 2025-06-07 1年 |
| 3 | [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3) |  | Boat Stern Light Anchor Light | 856 / 29.64% | $36,799 | $42.99 | $6.66 (15%) | 30 / 13 | 4.9 | $10.11 / 61% | 3 | 14 | 1 | 1.25 pounds | 2026-03-31 2个月 |
| 4 | [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q) |  | SILCA Ultimate Sealant Bottle | 749 / 7.13% | $33,698 | $44.99 | $6.57 (15%) | 140 / - | 4.5 | $6.48 / 71% | 4 | 19 | 1 | 2.51 pounds | 2025-02-16 1年 3个月 |
| 5 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 789 / 11.11% | $31,552 | $39.99 | $5.91 (15%) | 110 / 13 | 4.7 | $4.09 / 75% | 4 | 19 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 6 | [B0G93DF8CJ](https://www.amazon.com/dp/B0G93DF8CJ) |  | Exun Soccer Fan Gift Basket Set 2026 | 1,000 / 102.84% | $29,990 | $29.99 | $4.37 (15%) | 58 / 16 | 4.8 | $6.13 / 65% | 1 | 163 | 1 | 1.87 pounds | 2026-02-20 3个月 |
| 7 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 8 | [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP) |  | Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner | 890 / 34.88% | $28,471 | $31.99 | $4.87 (15%) | 118 / 4 | 4.5 | $4.09 / 72% | 3 | 7 | 1 | 0.29 pounds | 2024-02-06 2年 4个月 |
| 9 | [B0DRFSFCYQ](https://www.amazon.com/dp/B0DRFSFCYQ) |  | Telescoping Boat Hook for Docking | 678 / 103.33% | $28,469 | $41.99 | $6.11 (15%) | 138 / 13 | 4.6 | $12.37 / 56% | 2 | 5 | 1 | 2.65 pounds | 2025-01-26 1年 4个月 |
| 10 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 740 / 54.21% | $28,113 | $37.99 | $5.64 (15%) | 127 / 7 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 11 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | **** / **** | **** | $35.99 | - | 125 / 37 | 4.6 | **** /  | 3 | 64 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 12 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 13 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 85 / 15 | 4.5 | **** /  | 1 | 22 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 14 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 15 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 5 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 2个月 |
| 16 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 17 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |
| 18 | [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64) |  | GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men | **** / **** | **** | $49.99 | - | 97 / - | 4.5 | **** /  | 5 | 19 | 1 | 1.3 pounds | 2025-03-28 1年 2个月 |
| 19 | [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF) |  | Grip Enhancer Tacky Towel | **** / **** | **** | $36.99 | - | 125 / - | 4.5 | **** /  | 2 | 34 | 2 | 0.29 pounds | 2024-12-17 1年 5个月 |
| 20 | [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH) |  | Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdo… | **** / **** | **** | $36.95 | - | 111 / 3 | 4.8 | **** /  | 3 | 77 | 2 | 0.2 pounds | 2025-03-14 1年 2个月 |

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

**11. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**12. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**13. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**14. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**15. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**16. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**17. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

**18. [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64)** GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men, Natural Rattan Wicker Bike Baskets for Adult Bikes, Basket for Bikes with Liner, Bicycle Baskets for Beach Cruiser

**19. [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF)** Grip Enhancer Tacky Towel - USA-Made Chalkless Competition-Approved Formula for Golf, Tennis, Softball and More - Versatile Multi-Sport Moisture Control for Sweaty Hands

**20. [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH)** Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdoor Headlamp with Multiple Color Temperatures Warm Natural, Cold Lights and Red Light (Elastic Cord, Black)

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0DJT1YH6F`: 6,744 | 1,208 | 15% | 999 | 27.16% | $45,924 | 700+ | $27K+ | 2 | $45.97 | - | 106 | 7 | 4.6 | 0.7% | $7.23 | 69% | 2024-11-07 | 1年 7个月 | FBA | -
- `B0F5BD54RT`: 10,137 | 2,307 | 19% | 855 | 7.98% | $42,741 | 700+ | $34K+ | 1 | $49.99 | - | 101 | 21 | 4.6 | 2.46% | $6.31 | 72% | 2025-06-07 | 1年 | FBA | -
- `B0GKMGJLL3`: 10,790 | 2,203 | 17% | 856 | 29.64% | $36,799 | 600+ | $25K+ | 3 | $42.99 | - | 30 | 13 | 4.9 | 1.52% | $10.11 | 61% | 2026-03-31 | 2个月 | FBA | -
- `B0DX2F3V5Q`: 11,637 | 0 | 0% | 749 | 7.13% | $33,698 | 300+ | $13K+ | 4 | $44.99 | - | 140 | - | 4.5 | - | $6.48 | 71% | 2025-02-16 | 1年 3个月 | FBA | -
- `B0DTP76XQP`: 10,207 | 353 | 3% | 789 | 11.11% | $31,552 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 13 | 4.7 | 1.65% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0G93DF8CJ`: 4,786 | 3,333 | 41% | 1,000 | 102.84% | $29,990 | 900+ | $27K+ | 1 | $29.99 | - | 58 | 16 | 4.8 | 1.6% | $6.13 | 65% | 2026-02-20 | 3个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0CTQTYVGP`: 8,500 | 227 | 3% | 890 | 34.88% | $28,471 | 400+ | $12K+ | 3 | $31.99 | - | 118 | 4 | 4.5 | 0.45% | $4.09 | 72% | 2024-02-06 | 2年 4个月 | FBA | -
- `B0DRFSFCYQ`: 13,590 | 25 | 0% | 678 | 103.33% | $28,469 | 500+ | $20K+ | 2 | $41.99 | - | 138 | 13 | 4.6 | 1.92% | $12.37 | 56% | 2025-01-26 | 1年 4个月 | FBA | -
- `B0DS2CBVFT`: 8,379 | 2,034 | 20% | 740 | 54.21% | $28,113 | 300+ | $11K+ | 5 | $37.99 | - | 127 | 7 | 4.8 | 0.95% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0GL785GSP`: 13,539 | 268 | 2% | **** | **** | **** | **** | 3 | $35.99 | - | 125 | 37 | 4.6 | 5.05% | **** | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0F9ZZ17Z8`: 13,699 | 581 | 4% | **** | **** | **** | **** | 1 | $41.97 | - | 85 | 15 | 4.5 | 2.42% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0CT5MVCFD`: 17,365 | 1,868 | 10% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 5 | 4.8 | 0.95% | **** | 2024-03-14 | 2年 2个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -
- `B0DS23SX64`: 15,152 | 0 | 0% | **** | **** | **** | **** | 5 | $49.99 | - | 97 | - | 4.5 | - | **** | 2025-03-28 | 1年 2个月 | FBA | -
- `B0DNZX4MZF`: 13,386 | 0 | 0% | **** | **** | **** | **** | 2 | $36.99 | - | 125 | - | 4.5 | - | **** | 2024-12-17 | 1年 5个月 | FBA | -
- `B0DY2SW4CH`: 12,094 | 943 | 7% | **** | **** | **** | **** | 3 | $36.95 | - | 111 | 3 | 4.8 | 0.47% | **** | 2025-03-14 | 1年 2个月 | FBA | -

---

<!-- source: products/trophies.md -->
# Trophies 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $25.63　均Reviews 297（低竞争）　重量 1.01lbs（轻）　退货率 2.59%（低）　品牌集中度 49.0%（中等）　中国卖家 49.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DJT1YH6F](https://www.amazon.com/dp/B0DJT1YH6F) |  | Vitality Sports Golf Chipping Net | 999 / 27.16% | $45,924 | $45.97 | $7.02 (15%) | 106 / 7 | 4.6 | $7.23 / 69% | 2 | 3 | 2 | 3.24 pounds | 2024-11-07 1年 7个月 |
| 2 | [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT) |  | Suspension Straps Trainer with Built-in Door Anchor | 855 / 7.98% | $42,741 | $49.99 | $7.69 (15%) | 101 / 21 | 4.6 | $6.31 / 72% | 1 | 4 | 1 | 2.31 pounds | 2025-06-07 1年 |
| 3 | [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3) |  | Boat Stern Light Anchor Light | 856 / 29.64% | $36,799 | $42.99 | $6.66 (15%) | 30 / 13 | 4.9 | $10.11 / 61% | 3 | 14 | 1 | 1.25 pounds | 2026-03-31 2个月 |
| 4 | [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q) |  | SILCA Ultimate Sealant Bottle | 749 / 7.13% | $33,698 | $44.99 | $6.57 (15%) | 140 / - | 4.5 | $6.48 / 71% | 4 | 19 | 1 | 2.51 pounds | 2025-02-16 1年 3个月 |
| 5 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 789 / 11.11% | $31,552 | $39.99 | $5.91 (15%) | 110 / 13 | 4.7 | $4.09 / 75% | 4 | 19 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 6 | [B0G93DF8CJ](https://www.amazon.com/dp/B0G93DF8CJ) |  | Exun Soccer Fan Gift Basket Set 2026 | 1,000 / 102.84% | $29,990 | $29.99 | $4.37 (15%) | 58 / 16 | 4.8 | $6.13 / 65% | 1 | 163 | 1 | 1.87 pounds | 2026-02-20 3个月 |
| 7 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 8 | [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP) |  | Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner | 890 / 34.88% | $28,471 | $31.99 | $4.87 (15%) | 118 / 4 | 4.5 | $4.09 / 72% | 3 | 7 | 1 | 0.29 pounds | 2024-02-06 2年 4个月 |
| 9 | [B0DRFSFCYQ](https://www.amazon.com/dp/B0DRFSFCYQ) |  | Telescoping Boat Hook for Docking | 678 / 103.33% | $28,469 | $41.99 | $6.11 (15%) | 138 / 13 | 4.6 | $12.37 / 56% | 2 | 5 | 1 | 2.65 pounds | 2025-01-26 1年 4个月 |
| 10 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 740 / 54.21% | $28,113 | $37.99 | $5.64 (15%) | 127 / 7 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 11 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | **** / **** | **** | $35.99 | - | 125 / 37 | 4.6 | **** /  | 3 | 64 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 12 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 13 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 85 / 15 | 4.5 | **** /  | 1 | 22 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 14 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 15 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 5 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 2个月 |
| 16 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 17 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |
| 18 | [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64) |  | GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men | **** / **** | **** | $49.99 | - | 97 / - | 4.5 | **** /  | 5 | 19 | 1 | 1.3 pounds | 2025-03-28 1年 2个月 |
| 19 | [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF) |  | Grip Enhancer Tacky Towel | **** / **** | **** | $36.99 | - | 125 / - | 4.5 | **** /  | 2 | 34 | 2 | 0.29 pounds | 2024-12-17 1年 5个月 |
| 20 | [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH) |  | Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdo… | **** / **** | **** | $36.95 | - | 111 / 3 | 4.8 | **** /  | 3 | 77 | 2 | 0.2 pounds | 2025-03-14 1年 2个月 |

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

**11. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**12. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**13. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**14. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**15. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**16. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**17. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

**18. [B0DS23SX64](https://www.amazon.com/dp/B0DS23SX64)** GRANNY SAYS Bike Basket Front with Cup Holder for Women and Men, Natural Rattan Wicker Bike Baskets for Adult Bikes, Basket for Bikes with Liner, Bicycle Baskets for Beach Cruiser

**19. [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF)** Grip Enhancer Tacky Towel - USA-Made Chalkless Competition-Approved Formula for Golf, Tennis, Softball and More - Versatile Multi-Sport Moisture Control for Sweaty Hands

**20. [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH)** Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdoor Headlamp with Multiple Color Temperatures Warm Natural, Cold Lights and Red Light (Elastic Cord, Black)

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0DJT1YH6F`: 6,744 | 1,208 | 15% | 999 | 27.16% | $45,924 | 700+ | $27K+ | 2 | $45.97 | - | 106 | 7 | 4.6 | 0.7% | $7.23 | 69% | 2024-11-07 | 1年 7个月 | FBA | -
- `B0F5BD54RT`: 10,137 | 2,307 | 19% | 855 | 7.98% | $42,741 | 700+ | $34K+ | 1 | $49.99 | - | 101 | 21 | 4.6 | 2.46% | $6.31 | 72% | 2025-06-07 | 1年 | FBA | -
- `B0GKMGJLL3`: 10,790 | 2,203 | 17% | 856 | 29.64% | $36,799 | 600+ | $25K+ | 3 | $42.99 | - | 30 | 13 | 4.9 | 1.52% | $10.11 | 61% | 2026-03-31 | 2个月 | FBA | -
- `B0DX2F3V5Q`: 11,637 | 0 | 0% | 749 | 7.13% | $33,698 | 300+ | $13K+ | 4 | $44.99 | - | 140 | - | 4.5 | - | $6.48 | 71% | 2025-02-16 | 1年 3个月 | FBA | -
- `B0DTP76XQP`: 10,207 | 353 | 3% | 789 | 11.11% | $31,552 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 13 | 4.7 | 1.65% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0G93DF8CJ`: 4,786 | 3,333 | 41% | 1,000 | 102.84% | $29,990 | 900+ | $27K+ | 1 | $29.99 | - | 58 | 16 | 4.8 | 1.6% | $6.13 | 65% | 2026-02-20 | 3个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0CTQTYVGP`: 8,500 | 227 | 3% | 890 | 34.88% | $28,471 | 400+ | $12K+ | 3 | $31.99 | - | 118 | 4 | 4.5 | 0.45% | $4.09 | 72% | 2024-02-06 | 2年 4个月 | FBA | -
- `B0DRFSFCYQ`: 13,590 | 25 | 0% | 678 | 103.33% | $28,469 | 500+ | $20K+ | 2 | $41.99 | - | 138 | 13 | 4.6 | 1.92% | $12.37 | 56% | 2025-01-26 | 1年 4个月 | FBA | -
- `B0DS2CBVFT`: 8,379 | 2,034 | 20% | 740 | 54.21% | $28,113 | 300+ | $11K+ | 5 | $37.99 | - | 127 | 7 | 4.8 | 0.95% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0GL785GSP`: 13,539 | 268 | 2% | **** | **** | **** | **** | 3 | $35.99 | - | 125 | 37 | 4.6 | 5.05% | **** | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0F9ZZ17Z8`: 13,699 | 581 | 4% | **** | **** | **** | **** | 1 | $41.97 | - | 85 | 15 | 4.5 | 2.42% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0CT5MVCFD`: 17,365 | 1,868 | 10% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 5 | 4.8 | 0.95% | **** | 2024-03-14 | 2年 2个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -
- `B0DS23SX64`: 15,152 | 0 | 0% | **** | **** | **** | **** | 5 | $49.99 | - | 97 | - | 4.5 | - | **** | 2025-03-28 | 1年 2个月 | FBA | -
- `B0DNZX4MZF`: 13,386 | 0 | 0% | **** | **** | **** | **** | 2 | $36.99 | - | 125 | - | 4.5 | - | **** | 2024-12-17 | 1年 5个月 | FBA | -
- `B0DY2SW4CH`: 12,094 | 943 | 7% | **** | **** | **** | **** | 3 | $36.95 | - | 111 | 3 | 4.8 | 0.47% | **** | 2025-03-14 | 1年 2个月 | FBA | -

---

<!-- source: products/wind_spinners.md -->
# Wind Spinners 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $31.43　均Reviews 472（中等）　重量 2.36lbs（重）　退货率 3.09%（低）　品牌集中度 54.6%（中等）　中国卖家 85.0%

> 选品原则详见 [scan_principles.md](scan_principles.md)

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GHQMHRWW](https://www.amazon.com/dp/B0GHQMHRWW) |  | Stainless Steel Bird Deterrents for Outside Patio | 382 / 13.6% | $9,546 | $24.99 | $3.71 (15%) | 24 / - | 4.6 | $3.54 / 71% | 1 | 78 | 1 | 0.2 pounds | 2026-03-25 2个月 |
| 2 | [B0FQJVPZ4B](https://www.amazon.com/dp/B0FQJVPZ4B) |  | 10 Pack 8 Inch Sublimation Wind Spinner Blanks Aluminum Metal Win… | 253 / 22.68% | $6,575 | $25.99 | $3.86 (15%) | 67 / 10 | 4.6 | $6.02 / 62% | 2 | 104 | 1 | 1.79 pounds | 2025-10-22 7个月 |
| 3 | [B0FJ5YYQZ4](https://www.amazon.com/dp/B0FJ5YYQZ4) |  | 360 Degree Double Blade Metal Wind Spinner for Patio | 154 / 11.64% | $5,542 | $35.99 | $5.34 (15%) | 77 / 8 | 4.0 | $6.18 / 68% | 5 | 92 | 1 | 2.29 pounds | 2025-09-03 9个月 |
| 4 | [B0GGGPCFND](https://www.amazon.com/dp/B0GGGPCFND) |  | Hummingbird Mandala Wind Spinner for Mother's Day | 137 / 10.1% | $3,150 | $22.99 | $3.46 (15%) | 40 / 5 | 4.7 | $3.44 / 70% | 3 | 86 | 1 | 0.04 pounds | 2026-03-01 3个月 |

## 二、完整商品标题

**1. [B0GHQMHRWW](https://www.amazon.com/dp/B0GHQMHRWW)** Stainless Steel Bird Deterrents for Outside Patio, Reflective 3D Bird Scare Devices Wind Spinners Outdoor Decor, Woodpecker Deterrent Bird Reflectors to Keep Pigeon Crow Away House Yard Window, Round

**2. [B0FQJVPZ4B](https://www.amazon.com/dp/B0FQJVPZ4B)** 10 Pack 8 Inch Sublimation Wind Spinner Blanks Aluminum Metal Wind Spinners Sublimation Blanks 8 Inch for Indoor and Outdoor Ornaments

**3. [B0FJ5YYQZ4](https://www.amazon.com/dp/B0FJ5YYQZ4)** 360 Degree Double Blade Metal Wind Spinner for Patio, Lawn & Garden (Copper 53 * 12 inch)

**4. [B0GGGPCFND](https://www.amazon.com/dp/B0GGGPCFND)** Hummingbird Mandala Wind Spinner for Mother's Day, IDEA SHOW 12In 3D Kinetic Metal Wind Spinners, Hummingbird Gift for Women, Mom, Garden Decor Outdoor/Indoor Decoration, Dynamic Art Hanging Sculpture

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GHQMHRWW`: 28,621 | 13,924 | 33% | 382 | 13.6% | $9,546 | 300+ | - | 1 | $24.99 | - | 24 | - | 4.6 | - | $3.54 | 71% | 2026-03-25 | 2个月 | FBA | -
- `B0FQJVPZ4B`: 44,679 | 465 | 1% | 253 | 22.68% | $6,575 | 100+ | $2K+ | 2 | $25.99 | - | 67 | 10 | 4.6 | 3.95% | $6.02 | 62% | 2025-10-22 | 7个月 | FBA | -
- `B0FJ5YYQZ4`: 42,525 | 11,084 | 21% | 154 | 11.64% | $5,542 | 50+ | $1K+ | 5 | $35.99 | - | 77 | 8 | 4.0 | 5.19% | $6.18 | 68% | 2025-09-03 | 9个月 | FBA | -
- `B0GGGPCFND`: 40,308 | 29,898 | 43% | 137 | 10.1% | $3,150 | 50+ | $1K+ | 3 | $22.99 | - | 40 | 5 | 4.7 | 3.65% | $3.44 | 70% | 2026-03-01 | 3个月 | FBA | -

---

<!-- source: category_keywords_batteries_battery_chargers_2026_06_14.md -->
# Batteries & Battery Chargers 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DSRDB4YL`, `B0GKMGJLL3`, `B0G93DF8CJ`, `B0DJT1YH6F`, `B0F5BD54RT`, `B0CTQTYVGP`, `B0DTP76XQP`, `B0DX2F3V5Q`, `B0DS2CBVFT`, `B0DRFSFCYQ`, `B0GL785GSP`, `B0F6KRVBGR`, `B0F9ZZ17Z8`, `B0GLQ8T4P3`, `B0CT5MVCFD`, `B0FNNCDS7D`, `B0G51VX3YD`, `B0DS23SX64`, `B0DNZX4MZF`, `B0DY2SW4CH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **mundial 2026 **<br>2026年世界杯 | 3.79% |  |  | 67,617 | 797 | 19 | 1 | 327 | $1.36 | 33.79 |
| 2 | **cristiano ronaldo **<br>克里斯蒂亚诺·罗纳尔多 | 1.68% |  |  | 33,783 | 388 | 9 | 15 | 503 | $0.32 | 31.68 |
| 3 | **infant pool float **<br>婴儿泳池漂浮物 | 1.59% |  |  | 58,343 | 700 | 16 | 8 | 1,368 | $1.11 | 31.59 |
| 4 | **kids swim vest **<br>儿童游泳背心 | 1.57% |  |  | 22,819 | 273 | 7 | 14 | 7,373 | $1.15 | 31.57 |
| 5 | **life vest for toddlers 1-2 **<br>1-2 岁幼儿救生衣 | 1.10% |  |  | 16,719 | 402 | 10 | 0 | 825 | $1.31 | 31.1 |
| 6 | **swim vest for toddlers 1-2 **<br>1-2 岁幼儿游泳背心 | 1.07% |  |  | 17,648 | 241 | 6 | 1 | 512 | $1.38 | 31.07 |
| 7 | **baby life jacket 12-18 months **<br>12-18个月的婴儿救生衣 | 1.03% |  |  | 19,008 | 239 | 6 | 0 | 859 | $0.32 | 31.03 |
| 8 | **infant life vest 0-30 lbs **<br>婴儿救生衣 0-30 磅 | 0.93% |  |  | 23,098 | 607 | 14 | 0 | 648 | $0.32 | 30.93 |
| 9 | **infant life vest **<br>婴儿救生衣 | 0.91% |  |  | 19,313 | 312 | 8 | 1 | 871 | $0.63 | 30.91 |
| 10 | **soccer gifts for boys 8-12 **<br>8-12岁男孩足球礼物 | 0.89% |  |  | 23,051 | 631 | 15 | 1 | 5,067 | $0.43 | 30.89 |
| 11 | **baby swim float **<br>婴儿游泳浮台 | 0.80% |  |  | 37,952 | 664 | 16 | 9 | 1,654 | $1.06 | 30.8 |
| 12 | **golf party decorations **<br>高尔夫球派对装饰品 | 0.78% |  |  | 19,740 | 671 | 16 | 9 | 6,640 | $0.64 | 30.78 |
| 13 | **life jacket for 1 year old **<br>1岁的救生衣 | 0.93% |  |  | 16,523 | 190 | 5 | 0 | 664 | $0.33 | 30.43 |
| 14 | **fifa album 2026 **<br>FIFA 2026相册 | 1.07% |  |  | 33,902 | 138 | 4 | 0 | 84 | $0.55 | 27.97 |
| 15 | **soccer stuff **<br>足球用品 | 0.77% |  |  | 20,132 | 136 | 4 | 1 | 13,293 | $1.48 | 27.57 |
| 16 | **2026 world cup merchandise **<br>2026年世界杯商品 | 1.20% |  |  | 13,251 | 86 | 2 | 2 | 2,541 | $0.56 | 25.5 |
| 17 | **good good golf **<br>好高尔夫 | 0.81% |  |  | 19,772 | 81 | 2 | 1 | 238 | $0.90 | 24.86 |
| 18 | **golf at home **<br>在家打高尔夫球 | 1.16% |  |  | 18,827 | 58 | 2 | 1 | 392 | $1.31 | 24.06 |
| 19 | **stanley messi **<br>斯坦利·梅西 | 0.93% |  |  | 9,752 | 30 | 1 | 0 | 8,239 | $0.32 | 21.93 |
| 20 | **copa del mundo 2026 **<br>2026年世界杯 | 0.96% |  |  | 6,412 | 73 | 2 | 0 | 231 | $0.32 | 17.43 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0DSRDB4YL, B0GKMGJLL3, B0G93DF8CJ, B0DJT1YH6F, B0F5BD54RT, B0CTQTYVGP, B0DTP76XQP, B0DX2F3V5Q, B0DS2CBVFT, B0DRFSFCYQ, B0GL785GSP, B0F6KRVBGR, B0F9ZZ17Z8, B0GLQ8T4P3, B0CT5MVCFD, B0FNNCDS7D, B0G51VX3YD, B0DS23SX64, B0DNZX4MZF, B0DY2SW4CH）

1. **mundial 2026 ** — 2026年世界杯
2. **cristiano ronaldo ** — 克里斯蒂亚诺·罗纳尔多
3. **infant pool float ** — 婴儿泳池漂浮物
4. **kids swim vest ** — 儿童游泳背心
5. **2026 world cup merchandise ** — 2026年世界杯商品
6. **golf at home ** — 在家打高尔夫球
7. **life vest for toddlers 1-2 ** — 1-2 岁幼儿救生衣
8. **fifa album 2026 ** — FIFA 2026相册
9. **swim vest for toddlers 1-2 ** — 1-2 岁幼儿游泳背心
10. **baby life jacket 12-18 months ** — 12-18个月的婴儿救生衣
11. **copa del mundo 2026 ** — 2026年世界杯
12. **life jacket for 1 year old ** — 1岁的救生衣
13. **stanley messi ** — 斯坦利·梅西
14. **infant life vest 0-30 lbs ** — 婴儿救生衣 0-30 磅
15. **infant life vest ** — 婴儿救生衣
16. **soccer gifts for boys 8-12 ** — 8-12岁男孩足球礼物
17. **good good golf ** — 好高尔夫
18. **baby swim float ** — 婴儿游泳浮台
19. **golf party decorations ** — 高尔夫球派对装饰品
20. **soccer stuff ** — 足球用品

---

<!-- source: category_keywords_boats_2026_06_14.md -->
# Boats 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0D8TB7V29`, `B0CWXVCT2G`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **0** 个，过滤后保留 **0** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|

## 免费套餐当前可见原始关键词（查询 ASIN: B0D8TB7V29, B0CWXVCT2G）

---

<!-- source: category_keywords_brake_system_bleeding_tools_2026_06_14.md -->
# Brake System Bleeding Tools 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GGQH744M`, `B0F22SXPDT`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **brake fluid bleeder kit **<br>制动液泄放套件 | 13.68% |  |  | 9,382 | 273 | 7 | 14 | 1,389 | $1.00 | 42.44 |
| 2 | **break bleeder kit **<br>断流器套件 | 12.98% |  |  | 7,009 | 255 | 6 | 1 | 1,194 | $1.10 | 37.0 |
| 3 | **brake bleeding kit **<br>制动器放气套件 | 12.69% |  |  | 7,040 | 235 | 6 | 4 | 1,593 | $1.12 | 36.77 |
| 4 | **sram brake bleed kit **<br>sram 刹车放气套件 | 8.27% |  |  | 6,586 | 545 | 13 | 4 | 520 | $0.52 | 31.44 |
| 5 | **motorcycle brake bleeder kit **<br>摩托车刹车放气器套件 | 7.61% |  |  | 5,089 | 165 | 4 | 6 | 1,572 | $1.05 | 26.04 |
| 6 | **one man brake bleeder kit AC**<br>一个人的刹车放气器套件 | 6.59% |  |  | 4,075 | 181 | 5 | 4 | 896 | $0.59 | 23.79 |
| 7 | **brake bleeder valve **<br>制动放气阀 | 5.93% |  |  | 3,528 | 297 | 7 | 13 | 2,187 | $0.54 | 22.99 |
| 8 | **sram bleed kit **<br>sram 放气套件 | 4.75% |  |  | 2,359 | 394 | 9 | 0 | 242 | $0.65 | 19.47 |
| 9 | **brake bleeder tool **<br>刹车放气工具 | 4.00% |  |  | 2,481 | 200 | 5 | 5 | 3,868 | $1.08 | 18.96 |
| 10 | **pneumatic brake bleeder kit **<br>气动制动泄放器套件 | 1.21% |  |  | 1,878 | 176 | 4 | 2 | 775 | $0.94 | 13.77 |
| 11 | **brake pressure bleeder **<br>制动压力放气器 | 0.37% |  |  | 3,560 | 123 | 3 | 10 | 5,263 | $1.40 | 13.64 |
| 12 | **one way brake bleeder valve **<br>单向刹车放气阀 | 5.56% |  |  | 2,880 | 25 | 1 | 1 | 650 | $0.51 | 12.57 |
| 13 | **vacuum bleeder **<br>真空放气机 | 1.33% |  |  | 2,868 | 97 | 3 | 0 | 754 | $1.10 | 11.92 |
| 14 | **pressure brake bleeder **<br>压力制动放气器 | 1.47% |  |  | 2,989 | 78 | 2 | 4 | 5,033 | $1.03 | 11.35 |
| 15 | **brake system bleeding tools **<br>制动系统放气工具 | 3.77% |  |  | 1,904 | 44 | 1 | 3 | 2,215 | $1.09 | 9.78 |
| 16 | **brake pressure bleeder kit **<br>制动压力泄放器套件 | 0.50% |  |  | 2,655 | 66 | 2 | 4 | 1,573 | $1.16 | 9.11 |
| 17 | **vacuum brake bleeder kit **<br>真空制动泄放器套件 | 1.00% |  |  | 1,911 | 77 | 2 | 13 | 851 | $1.19 | 8.67 |
| 18 | **brake bleeder check valve **<br>制动放气单向阀 | 3.82% |  |  | 2,039 | 12 | 1 | 3 | 947 | $0.53 | 8.5 |
| 19 | **brake flush kit **<br>刹车冲洗套件 | 1.32% |  |  | 2,243 | 46 | 2 | 1 | 831 | $0.91 | 8.11 |
| 20 | **clutch bleeder kit **<br>离合器放气套件 | 2.63% |  |  | 1,508 | 41 | 1 | 2 | 685 | $1.10 | 7.7 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GGQH744M, B0F22SXPDT）

1. **brake fluid bleeder kit ** — 制动液泄放套件
2. **break bleeder kit ** — 断流器套件
3. **brake bleeding kit ** — 制动器放气套件
4. **sram brake bleed kit ** — sram 刹车放气套件
5. **motorcycle brake bleeder kit ** — 摩托车刹车放气器套件
6. **one man brake bleeder kit AC** — 一个人的刹车放气器套件
7. **brake bleeder valve ** — 制动放气阀
8. **one way brake bleeder valve ** — 单向刹车放气阀
9. **sram bleed kit ** — sram 放气套件
10. **brake bleeder tool ** — 刹车放气工具
11. **brake bleeder check valve ** — 制动放气单向阀
12. **brake system bleeding tools ** — 制动系统放气工具
13. **clutch bleeder kit ** — 离合器放气套件
14. **pressure brake bleeder ** — 压力制动放气器
15. **vacuum bleeder ** — 真空放气机
16. **brake flush kit ** — 刹车冲洗套件
17. **pneumatic brake bleeder kit ** — 气动制动泄放器套件
18. **vacuum brake bleeder kit ** — 真空制动泄放器套件
19. **brake pressure bleeder kit ** — 制动压力泄放器套件
20. **brake pressure bleeder ** — 制动压力放气器

---

<!-- source: category_keywords_cardboard_cutouts_2026_06_14.md -->
# Cardboard Cutouts 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0G7YT3F1H`, `B0GHSNNZPZ`, `B0GJL3W2D6`, `B0FWC8ZZ48`, `B09PKHLH7W`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **winnie the pooh stickers **<br>小熊维尼贴纸 | 11.03% |  |  | 16,529 | 684 | 16 | 1 | 990 | $0.32 | 41.03 |
| 2 | **winnie the pooh baby shower **<br>小熊维尼婴儿送礼会 | 9.78% |  |  | 24,582 | 226 | 6 | 3 | 6,881 | $0.32 | 39.78 |
| 3 | **winnie the pooh balloons **<br>小熊维尼气球 | 7.16% |  |  | 9,553 | 251 | 6 | 0 | 769 | $0.41 | 36.27 |
| 4 | **winnie the pooh nursery decor **<br>小熊维尼托儿所装饰 | 9.04% |  |  | 21,167 | 137 | 4 | 1 | 996 | $0.47 | 35.89 |
| 5 | **gender reveal box **<br>性别揭示盒 | 4.30% |  |  | 12,691 | 171 | 4 | 6 | 4,960 | $0.32 | 32.85 |
| 6 | **little people princess **<br>小人儿公主 | 1.98% |  |  | 14,178 | 450 | 11 | 0 | 1,111 | $0.32 | 31.98 |
| 7 | **winnie the pooh decorations **<br>小熊维尼装饰品 | 7.41% |  |  | 9,307 | 91 | 3 | 0 | 896 | $0.36 | 30.57 |
| 8 | **little people disney **<br>小人物迪斯尼 | 2.96% |  |  | 7,507 | 131 | 3 | 0 | 4,633 | $0.47 | 24.52 |
| 9 | **winnie the pooh balloon arch **<br>小熊维尼气球拱门 | 3.26% |  |  | 3,956 | 291 | 7 | 0 | 896 | $0.42 | 21.17 |
| 10 | **princess backdrop **<br>公主背景 | 2.20% |  |  | 5,436 | 107 | 3 | 1 | 6,207 | $0.32 | 18.42 |
| 11 | **winnie the pooh centerpieces **<br>小熊维尼的中央装饰品 | 4.95% |  |  | 5,820 | 36 | 1 | 0 | 445 | $0.32 | 18.39 |
| 12 | **winnie the pooh cutouts **<br>小熊维尼剪纸 | 3.62% |  |  | 3,802 | 34 | 1 | 0 | 771 | $0.44 | 12.92 |
| 13 | **baby winnie the pooh **<br>小熊维尼宝宝 | 1.85% |  |  | 4,102 | 44 | 2 | 9 | 2,893 | $0.32 | 12.25 |
| 14 | **winnie the pooh first birthday **<br>小熊维尼第一个生日 | 3.13% |  |  | 3,322 | 41 | 1 | 0 | 957 | $0.32 | 11.82 |
| 15 | **winnie the pooh gender reveal **<br>小熊维尼性别揭秘 | 2.99% |  |  | 3,667 | 27 | 1 | 0 | 685 | $0.32 | 11.67 |
| 16 | **cardboard cut out **<br>纸板剪下来 | 1.83% |  |  | 3,750 | 19 | 1 | 0 | 10,628 | $0.82 | 10.28 |
| 17 | **winnie the pooh arch cover **<br>小熊维尼拱形盖 | 1.66% |  |  | 2,849 | 11 | 1 | 0 | 378 | $0.35 | 7.91 |
| 18 | **winnie the pooh 1st birthday **<br>小熊维尼一岁生日 | 2.22% |  |  | 2,193 | 16 | 1 | 1 | 1,355 | $0.32 | 7.41 |
| 19 | **baby shower winnie the pooh **<br>婴儿送礼会小熊维尼 | 1.98% |  |  | 2,207 | 11 | 1 | 0 | 1,772 | $0.67 | 6.94 |
| 20 | **pooh baby shower decorations **<br>小熊维尼婴儿淋浴装饰品 | 2.11% |  |  | 1,725 | 18 | 1 | 5 | 1,269 | $0.32 | 6.46 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G7YT3F1H, B0GHSNNZPZ, B0GJL3W2D6, B0FWC8ZZ48, B09PKHLH7W）

1. **winnie the pooh stickers ** — 小熊维尼贴纸
2. **winnie the pooh baby shower ** — 小熊维尼婴儿送礼会
3. **winnie the pooh nursery decor ** — 小熊维尼托儿所装饰
4. **winnie the pooh decorations ** — 小熊维尼装饰品
5. **winnie the pooh balloons ** — 小熊维尼气球
6. **winnie the pooh centerpieces ** — 小熊维尼的中央装饰品
7. **gender reveal box ** — 性别揭示盒
8. **winnie the pooh cutouts ** — 小熊维尼剪纸
9. **winnie the pooh balloon arch ** — 小熊维尼气球拱门
10. **winnie the pooh first birthday ** — 小熊维尼第一个生日
11. **winnie the pooh gender reveal ** — 小熊维尼性别揭秘
12. **little people disney ** — 小人物迪斯尼
13. **winnie the pooh 1st birthday ** — 小熊维尼一岁生日
14. **princess backdrop ** — 公主背景
15. **pooh baby shower decorations ** — 小熊维尼婴儿淋浴装饰品
16. **baby shower winnie the pooh ** — 婴儿送礼会小熊维尼
17. **little people princess ** — 小人儿公主
18. **baby winnie the pooh ** — 小熊维尼宝宝
19. **cardboard cut out ** — 纸板剪下来
20. **winnie the pooh arch cover ** — 小熊维尼拱形盖

---

<!-- source: category_keywords_compressed_air_dusters_2026_06_14.md -->
# Compressed Air Dusters 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0FFGTDMMX`, `B0FPRM62Z2`, `B0FSLLJ8SZ`, `B0GGR1T98P`, `B0GRH6MY39`, `B0DB8J4T52`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **bullseye blower as seen on tv **<br>电视上看到的靶心吹风机 | 19.28% |  |  | 113,506 | 488 | 12 | 0 | 164 | $1.05 | 49.28 |
| 2 | **bullseye blower **<br>靶心吹风机 | 8.22% |  |  | 63,843 | 383 | 9 | 1 | 187 | $1.15 | 38.22 |
| 3 | **computer cleaning kit **<br>电脑清洁套装 | 7.07% |  |  | 10,463 | 562 | 13 | 1 | 4,466 | $0.73 | 37.07 |
| 4 | **aspiradora para carro **<br>车载吸尘器 | 4.48% |  |  | 73,207 | 702 | 16 | 0 | 704 | $1.00 | 34.48 |
| 5 | **ryobi blower **<br>Ryobi blower | 2.31% |  |  | 26,188 | 267 | 7 | 0 | 3,243 | $0.67 | 32.31 |
| 6 | **mini leaf blower **<br>迷你吹叶机 | 1.41% |  |  | 19,868 | 494 | 12 | 1 | 1,039 | $0.92 | 31.41 |
| 7 | **gaiatop fan **<br>盖亚顶风扇 | 1.26% |  |  | 21,350 | 275 | 7 | 0 | 168 | $0.32 | 31.26 |
| 8 | **portable vacuum for car **<br>车载便携式吸尘器 | 1.24% |  |  | 23,390 | 654 | 15 | 1 | 10,980 | $1.11 | 31.24 |
| 9 | **car vacuum cleaner **<br>汽车吸尘器 | 1.17% |  |  | 22,464 | 566 | 13 | 6 | 11,921 | $1.27 | 31.17 |
| 10 | **turbo jet blower **<br>涡轮喷射鼓风机 | 1.16% |  |  | 13,962 | 237 | 6 | 5 | 805 | $1.41 | 31.16 |
| 11 | **shark handheld vacuum **<br>鲨鱼手持式真空吸尘器 | 0.97% |  |  | 20,636 | 315 | 8 | 0 | 1,400 | $0.95 | 30.97 |
| 12 | **mini vacuum cleaner **<br>迷你吸尘器 | 0.77% |  |  | 17,162 | 470 | 11 | 3 | 3,986 | $0.82 | 30.77 |
| 13 | **mini duster **<br>迷你掸子 | 8.22% |  |  | 2,709 | 487 | 12 | 10 | 14,811 | $0.34 | 23.64 |
| 14 | **electronic duster spray **<br>电子除尘喷雾 | 4.62% |  |  | 4,042 | 213 | 5 | 0 | 435 | $1.16 | 22.7 |
| 15 | **condensed air **<br>冷凝空气 | 6.11% |  |  | 2,642 | 831 | 19 | 0 | 163 | $1.47 | 21.39 |
| 16 | **computer duster spray **<br>电脑除尘喷雾 | 0.85% |  |  | 4,186 | 660 | 15 | 0 | 335 | $1.42 | 19.22 |
| 17 | **air blower duster **<br>吹风除尘器 | 7.98% |  |  | 3,491 | 26 | 1 | 0 | 2,226 | $0.53 | 16.26 |
| 18 | **computer keyboard cleaner **<br>电脑键盘清洁剂 | 1.98% |  |  | 2,450 | 186 | 5 | 0 | 2,681 | $0.86 | 16.18 |
| 19 | **end dust spray **<br>末端粉尘喷雾 | 1.91% |  |  | 1,406 | 365 | 9 | 0 | 119 | $0.84 | 14.72 |
| 20 | **air compressor blower gun **<br>空压机鼓风机枪 | 2.73% |  |  | 1,936 | 121 | 3 | 0 | 1,660 | $1.02 | 12.65 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0FFGTDMMX, B0FPRM62Z2, B0FSLLJ8SZ, B0GGR1T98P, B0GRH6MY39, B0DB8J4T52）

1. **bullseye blower as seen on tv ** — 电视上看到的靶心吹风机
2. **bullseye blower ** — 靶心吹风机
3. **mini duster ** — 迷你掸子
4. **air blower duster ** — 吹风除尘器
5. **computer cleaning kit ** — 电脑清洁套装
6. **condensed air ** — 冷凝空气
7. **electronic duster spray ** — 电子除尘喷雾
8. **aspiradora para carro ** — 车载吸尘器
9. **air compressor blower gun ** — 空压机鼓风机枪
10. **ryobi blower ** — Ryobi blower
11. **computer keyboard cleaner ** — 电脑键盘清洁剂
12. **end dust spray ** — 末端粉尘喷雾
13. **mini leaf blower ** — 迷你吹叶机
14. **gaiatop fan ** — 盖亚顶风扇
15. **portable vacuum for car ** — 车载便携式吸尘器
16. **car vacuum cleaner ** — 汽车吸尘器
17. **turbo jet blower ** — 涡轮喷射鼓风机
18. **shark handheld vacuum ** — 鲨鱼手持式真空吸尘器
19. **computer duster spray ** — 电脑除尘喷雾
20. **mini vacuum cleaner ** — 迷你吸尘器

---

<!-- source: category_keywords_decorative_trays_2026_06_14.md -->
# Decorative Trays 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0FL2236YS`, `B0DT1X5W9W`, `B0DRYD63RT`, `B0G3TS1YFT`, `B0DYP3TRL2`, `B0D8MW6VS1`, `B0BMDLHHYT`, `B0D8TJDXRY`, `B0CRVTY72B`, `B0B24B6TPX`, `B0CCVNCZWZ`, `B0FK99K3D4`, `B0D5H5TRRD`, `B0F2HXLN8V`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **0** 个，过滤后保留 **0** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|

## 免费套餐当前可见原始关键词（查询 ASIN: B0FL2236YS, B0DT1X5W9W, B0DRYD63RT, B0G3TS1YFT, B0DYP3TRL2, B0D8MW6VS1, B0BMDLHHYT, B0D8TJDXRY, B0CRVTY72B, B0B24B6TPX, B0CCVNCZWZ, B0FK99K3D4, B0D5H5TRRD, B0F2HXLN8V）

---

<!-- source: category_keywords_electrical_system_tools_2026_06_14.md -->
# Electrical System Tools 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GHDJM616`, `B0C4PTWP8G`, `B0FDVDL457`, `B0CR6F2HR1`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **compression tester automotive **<br>汽车压缩测试仪 | 11.76% |  |  | 12,395 | 739 | 17 | 5 | 1,577 | $0.69 | 41.76 |
| 2 | **hose removal pliers **<br>软管拆卸钳 | 20.77% |  |  | 3,557 | 170 | 4 | 15 | 2,193 | $0.32 | 36.38 |
| 3 | **noid light test kit **<br>noid 光测试套件 | 11.16% |  |  | 2,799 | 407 | 10 | 13 | 136 | $0.85 | 26.76 |
| 4 | **molex pin extractor **<br>molex 针提取器 | 10.65% |  |  | 3,193 | 191 | 5 | 11 | 7,010 | $1.19 | 26.59 |
| 5 | **molex connector kit **<br>molex 连接器套件 | 2.31% |  |  | 7,474 | 163 | 4 | 4 | 937 | $0.44 | 25.41 |
| 6 | **deutsch pin removal tool **<br>德国销拆卸工具 | 10.08% |  |  | 2,503 | 310 | 8 | 14 | 440 | $1.31 | 25.09 |
| 7 | **car clip remover tool **<br>汽车夹拆除工具 | 4.46% |  |  | 4,651 | 452 | 11 | 3 | 2,178 | $0.83 | 23.76 |
| 8 | **electrical pin removal tool **<br>电针拆卸工具 | 9.78% |  |  | 2,449 | 94 | 3 | 12 | 4,619 | $0.78 | 19.38 |
| 9 | **depinning tool kit **<br>脱钉工具包 | 5.77% |  |  | 2,905 | 140 | 4 | 14 | 288 | $0.89 | 18.58 |
| 10 | **panel clip pliers **<br>面板夹钳 | 0.30% |  |  | 3,551 | 231 | 6 | 6 | 1,169 | $0.92 | 17.4 |
| 11 | **automotive clip removal tool **<br>汽车夹拆卸工具 | 0.95% |  |  | 3,074 | 615 | 14 | 1 | 14,408 | $0.83 | 17.1 |
| 12 | **deutsch connector tool **<br>德国连接器工具 | 9.87% |  |  | 2,560 | 22 | 1 | 3 | 869 | $1.27 | 16.09 |
| 13 | **push pin removal tool **<br>推针拆卸工具 | 0.22% |  |  | 2,563 | 311 | 8 | 1 | 5,202 | $1.00 | 15.35 |
| 14 | **clip removal pliers **<br>夹子拆卸钳 | 0.17% |  |  | 3,427 | 126 | 3 | 13 | 5,529 | $0.90 | 13.32 |
| 15 | **molex connector **<br>摩尔克斯连接器 | 0.79% |  |  | 1,832 | 58 | 2 | 1 | 1,758 | $0.33 | 7.35 |
| 16 | **hose clamp removal tool **<br>软管夹拆卸工具 | 0.65% |  |  | 1,347 | 69 | 2 | 9 | 4,779 | $0.38 | 6.79 |
| 17 | **awg wire gauge tool **<br>awg线规工具 | 0.20% |  |  | 1,968 | 20 | 1 | 0 | 6,487 | $0.43 | 5.14 |
| 18 | **zml pliers **<br>ZML 钳子 | - |  |  | 2,049 | 15 | 1 | 0 | 150 | $0.77 | 4.85 |
| 19 | **specialty tools for mechanics **<br>机械专业工具 | 0.09% |  |  | 1,581 | 11 | 1 | 0 | 508 | $0.55 | 3.8 |
| 20 | **wire terminal removal tool **<br>接线端子拆卸工具 | - |  |  | 635 | 27 | 1 | 0 | 4,162 | $0.79 | 2.62 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GHDJM616, B0C4PTWP8G, B0FDVDL457, B0CR6F2HR1）

1. **hose removal pliers ** — 软管拆卸钳
2. **compression tester automotive ** — 汽车压缩测试仪
3. **noid light test kit ** — noid 光测试套件
4. **molex pin extractor ** — molex 针提取器
5. **deutsch pin removal tool ** — 德国销拆卸工具
6. **deutsch connector tool ** — 德国连接器工具
7. **electrical pin removal tool ** — 电针拆卸工具
8. **depinning tool kit ** — 脱钉工具包
9. **car clip remover tool ** — 汽车夹拆除工具
10. **molex connector kit ** — molex 连接器套件
11. **automotive clip removal tool ** — 汽车夹拆卸工具
12. **molex connector ** — 摩尔克斯连接器
13. **hose clamp removal tool ** — 软管夹拆卸工具
14. **panel clip pliers ** — 面板夹钳
15. **push pin removal tool ** — 推针拆卸工具
16. **awg wire gauge tool ** — awg线规工具
17. **clip removal pliers ** — 夹子拆卸钳
18. **specialty tools for mechanics ** — 机械专业工具
19. **zml pliers ** — ZML 钳子
20. **wire terminal removal tool ** — 接线端子拆卸工具

---

<!-- source: category_keywords_game_mats_boards_2026_06_14.md -->
# Game Mats & Boards 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0FMXW89J5`, `B0GHHG1W42`, `B0GQMQCCNH`, `B0FQ5KW2WN`, `B0DD6X3QTH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **0** 个，过滤后保留 **0** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|

## 免费套餐当前可见原始关键词（查询 ASIN: B0FMXW89J5, B0GHHG1W42, B0GQMQCCNH, B0FQ5KW2WN, B0DD6X3QTH）

---

<!-- source: category_keywords_grinding_discs_2026_06_14.md -->
# Grinding Discs 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DB1B6DKZ`, `B0CBS4VWYB`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **0** 个，过滤后保留 **0** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|

## 免费套餐当前可见原始关键词（查询 ASIN: B0DB1B6DKZ, B0CBS4VWYB）

---

<!-- source: category_keywords_lighting_products_2026_06_14.md -->
# Lighting Products 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0G6L569ZB`, `B0GD7YRTDM`, `B0GJCRX242`, `B0DXVSDMZF`, `B0DSHT56KC`, `B0GRTPX9DC`, `B0GPW9YT5H`, `B0G6Z1QM2M`, `B0DZD1RC33`, `B0DWMMYNDB`, `B0DSD4NWXN`, `B0FWJ6C4CY`, `B0G6SLH595`, `B0CX9162PJ`, `B0G8X6721P`, `B0FWC5JQL9`, `B0D93J8T91`, `B0DN6FBDDQ`, `B0GCZ27BY1`, `B0GL8DTBM6`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **pool lights solar powered **<br>池灯太阳能供电 | 7.53% |  |  | 12,480 | 160 | 4 | 2 | 3,698 | $1.18 | 35.53 |
| 2 | **pool solar lights **<br>泳池太阳能灯 | 4.24% |  |  | 20,996 | 434 | 10 | 1 | 5,319 | $1.29 | 34.24 |
| 3 | **above ground pool lights **<br>地上泳池灯 | 2.71% |  |  | 49,502 | 430 | 10 | 4 | 3,719 | $1.61 | 32.71 |
| 4 | **above ground pool fountain **<br>地上游泳池喷泉 | 1.94% |  |  | 19,402 | 223 | 6 | 2 | 1,308 | $1.08 | 31.94 |
| 5 | **pool floating lights **<br>泳池漂浮灯 | 5.04% |  |  | 7,603 | 191 | 5 | 0 | 6,361 | $0.78 | 29.8 |
| 6 | **solar sun rings **<br>太阳太阳环 | 2.17% |  |  | 7,800 | 269 | 7 | 9 | 230 | $0.41 | 27.77 |
| 7 | **solar lights for pool **<br>泳池太阳能灯 | 3.93% |  |  | 8,769 | 81 | 2 | 0 | 5,306 | $0.81 | 25.52 |
| 8 | **pool lights that float **<br>漂浮的泳池灯 | 6.97% |  |  | 5,589 | 134 | 4 | 7 | 1,061 | $0.49 | 24.85 |
| 9 | **outdoor pool decor **<br>室外游泳池装饰 | 2.08% |  |  | 9,318 | 70 | 2 | 3 | 498 | $0.32 | 24.22 |
| 10 | **submersible pool lights **<br>潜水池灯 | 7.96% |  |  | 5,581 | 58 | 2 | 6 | 1,892 | $1.42 | 22.02 |
| 11 | **solar powered pool lights **<br>太阳能泳池灯 | 5.14% |  |  | 6,699 | 48 | 2 | 0 | 3,684 | $1.18 | 20.94 |
| 12 | **magnetic pool lights **<br>磁池灯 | 4.89% |  |  | 6,394 | 52 | 2 | 1 | 662 | $0.59 | 20.28 |
| 13 | **light up pool balls **<br>点亮台球 | 2.52% |  |  | 3,867 | 361 | 9 | 3 | 546 | $1.10 | 20.25 |
| 14 | **pool lights underwater **<br>水下泳池灯 | 3.23% |  |  | 3,019 | 195 | 5 | 0 | 3,445 | $1.04 | 19.02 |
| 15 | **floating pool light **<br>漂浮池灯 | 1.92% |  |  | 3,060 | 302 | 7 | 14 | 6,452 | $0.96 | 18.04 |
| 16 | **floating lights for pool **<br>泳池漂浮灯 | 2.12% |  |  | 4,089 | 83 | 2 | 1 | 6,389 | $0.73 | 14.45 |
| 17 | **luces para piscina **<br>luces para piscina | 2.02% |  |  | 4,270 | 23 | 1 | 0 | 1,757 | $1.51 | 11.71 |
| 18 | **light up pool floats **<br>点亮泳池漂浮物 | 2.18% |  |  | 3,045 | 33 | 1 | 1 | 871 | $1.25 | 9.92 |
| 19 | **pool solar lights floating **<br>水池太阳能灯漂浮 | 2.94% |  |  | 2,025 | 44 | 1 | 0 | 1,043 | $1.27 | 9.19 |
| 20 | **solar pool lights floating **<br>太阳能泳池灯漂浮 | 3.31% |  |  | 2,231 | 24 | 1 | 0 | 980 | $1.39 | 8.97 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G6L569ZB, B0GD7YRTDM, B0GJCRX242, B0DXVSDMZF, B0DSHT56KC, B0GRTPX9DC, B0GPW9YT5H, B0G6Z1QM2M, B0DZD1RC33, B0DWMMYNDB, B0DSD4NWXN, B0FWJ6C4CY, B0G6SLH595, B0CX9162PJ, B0G8X6721P, B0FWC5JQL9, B0D93J8T91, B0DN6FBDDQ, B0GCZ27BY1, B0GL8DTBM6）

1. **submersible pool lights ** — 潜水池灯
2. **pool lights solar powered ** — 池灯太阳能供电
3. **pool lights that float ** — 漂浮的泳池灯
4. **solar powered pool lights ** — 太阳能泳池灯
5. **pool floating lights ** — 泳池漂浮灯
6. **magnetic pool lights ** — 磁池灯
7. **pool solar lights ** — 泳池太阳能灯
8. **solar lights for pool ** — 泳池太阳能灯
9. **solar pool lights floating ** — 太阳能泳池灯漂浮
10. **pool lights underwater ** — 水下泳池灯
11. **pool solar lights floating ** — 水池太阳能灯漂浮
12. **above ground pool lights ** — 地上泳池灯
13. **light up pool balls ** — 点亮台球
14. **light up pool floats ** — 点亮泳池漂浮物
15. **solar sun rings ** — 太阳太阳环
16. **floating lights for pool ** — 泳池漂浮灯
17. **outdoor pool decor ** — 室外游泳池装饰
18. **luces para piscina ** — luces para piscina
19. **above ground pool fountain ** — 地上游泳池喷泉
20. **floating pool light ** — 漂浮池灯

---

<!-- source: category_keywords_paddleboard_accessories_2026_06_14.md -->
# Paddleboard Accessories 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DSRDB4YL`, `B0GKMGJLL3`, `B0G93DF8CJ`, `B0DJT1YH6F`, `B0F5BD54RT`, `B0CTQTYVGP`, `B0DTP76XQP`, `B0DX2F3V5Q`, `B0DS2CBVFT`, `B0DRFSFCYQ`, `B0GL785GSP`, `B0F6KRVBGR`, `B0F9ZZ17Z8`, `B0GLQ8T4P3`, `B0CT5MVCFD`, `B0FNNCDS7D`, `B0G51VX3YD`, `B0DS23SX64`, `B0DNZX4MZF`, `B0DY2SW4CH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **mundial 2026 **<br>2026年世界杯 | 3.79% |  |  | 67,617 | 797 | 19 | 1 | 327 | $1.36 | 33.79 |
| 2 | **cristiano ronaldo **<br>克里斯蒂亚诺·罗纳尔多 | 1.68% |  |  | 33,783 | 388 | 9 | 15 | 503 | $0.32 | 31.68 |
| 3 | **infant pool float **<br>婴儿泳池漂浮物 | 1.59% |  |  | 58,343 | 700 | 16 | 8 | 1,368 | $1.11 | 31.59 |
| 4 | **kids swim vest **<br>儿童游泳背心 | 1.57% |  |  | 22,819 | 273 | 7 | 14 | 7,373 | $1.15 | 31.57 |
| 5 | **life vest for toddlers 1-2 **<br>1-2 岁幼儿救生衣 | 1.10% |  |  | 16,719 | 402 | 10 | 0 | 825 | $1.31 | 31.1 |
| 6 | **swim vest for toddlers 1-2 **<br>1-2 岁幼儿游泳背心 | 1.07% |  |  | 17,648 | 241 | 6 | 1 | 512 | $1.38 | 31.07 |
| 7 | **baby life jacket 12-18 months **<br>12-18个月的婴儿救生衣 | 1.03% |  |  | 19,008 | 239 | 6 | 0 | 859 | $0.32 | 31.03 |
| 8 | **infant life vest 0-30 lbs **<br>婴儿救生衣 0-30 磅 | 0.93% |  |  | 23,098 | 607 | 14 | 0 | 648 | $0.32 | 30.93 |
| 9 | **infant life vest **<br>婴儿救生衣 | 0.91% |  |  | 19,313 | 312 | 8 | 1 | 871 | $0.63 | 30.91 |
| 10 | **soccer gifts for boys 8-12 **<br>8-12岁男孩足球礼物 | 0.89% |  |  | 23,051 | 631 | 15 | 1 | 5,067 | $0.43 | 30.89 |
| 11 | **baby swim float **<br>婴儿游泳浮台 | 0.80% |  |  | 37,952 | 664 | 16 | 9 | 1,654 | $1.06 | 30.8 |
| 12 | **golf party decorations **<br>高尔夫球派对装饰品 | 0.78% |  |  | 19,740 | 671 | 16 | 9 | 6,640 | $0.64 | 30.78 |
| 13 | **life jacket for 1 year old **<br>1岁的救生衣 | 0.93% |  |  | 16,523 | 190 | 5 | 0 | 664 | $0.33 | 30.43 |
| 14 | **fifa album 2026 **<br>FIFA 2026相册 | 1.07% |  |  | 33,902 | 138 | 4 | 0 | 84 | $0.55 | 27.97 |
| 15 | **soccer stuff **<br>足球用品 | 0.77% |  |  | 20,132 | 136 | 4 | 1 | 13,293 | $1.48 | 27.57 |
| 16 | **2026 world cup merchandise **<br>2026年世界杯商品 | 1.20% |  |  | 13,251 | 86 | 2 | 2 | 2,541 | $0.56 | 25.5 |
| 17 | **good good golf **<br>好高尔夫 | 0.81% |  |  | 19,772 | 81 | 2 | 1 | 238 | $0.90 | 24.86 |
| 18 | **golf at home **<br>在家打高尔夫球 | 1.16% |  |  | 18,827 | 58 | 2 | 1 | 392 | $1.31 | 24.06 |
| 19 | **stanley messi **<br>斯坦利·梅西 | 0.93% |  |  | 9,752 | 30 | 1 | 0 | 8,239 | $0.32 | 21.93 |
| 20 | **copa del mundo 2026 **<br>2026年世界杯 | 0.96% |  |  | 6,412 | 73 | 2 | 0 | 231 | $0.32 | 17.43 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0DSRDB4YL, B0GKMGJLL3, B0G93DF8CJ, B0DJT1YH6F, B0F5BD54RT, B0CTQTYVGP, B0DTP76XQP, B0DX2F3V5Q, B0DS2CBVFT, B0DRFSFCYQ, B0GL785GSP, B0F6KRVBGR, B0F9ZZ17Z8, B0GLQ8T4P3, B0CT5MVCFD, B0FNNCDS7D, B0G51VX3YD, B0DS23SX64, B0DNZX4MZF, B0DY2SW4CH）

1. **mundial 2026 ** — 2026年世界杯
2. **cristiano ronaldo ** — 克里斯蒂亚诺·罗纳尔多
3. **infant pool float ** — 婴儿泳池漂浮物
4. **kids swim vest ** — 儿童游泳背心
5. **2026 world cup merchandise ** — 2026年世界杯商品
6. **golf at home ** — 在家打高尔夫球
7. **life vest for toddlers 1-2 ** — 1-2 岁幼儿救生衣
8. **fifa album 2026 ** — FIFA 2026相册
9. **swim vest for toddlers 1-2 ** — 1-2 岁幼儿游泳背心
10. **baby life jacket 12-18 months ** — 12-18个月的婴儿救生衣
11. **copa del mundo 2026 ** — 2026年世界杯
12. **life jacket for 1 year old ** — 1岁的救生衣
13. **stanley messi ** — 斯坦利·梅西
14. **infant life vest 0-30 lbs ** — 婴儿救生衣 0-30 磅
15. **infant life vest ** — 婴儿救生衣
16. **soccer gifts for boys 8-12 ** — 8-12岁男孩足球礼物
17. **good good golf ** — 好高尔夫
18. **baby swim float ** — 婴儿游泳浮台
19. **golf party decorations ** — 高尔夫球派对装饰品
20. **soccer stuff ** — 足球用品

---

<!-- source: category_keywords_swing_trainers_2026_06_14.md -->
# Swing Trainers 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DSRDB4YL`, `B0GKMGJLL3`, `B0G93DF8CJ`, `B0DJT1YH6F`, `B0F5BD54RT`, `B0CTQTYVGP`, `B0DTP76XQP`, `B0DX2F3V5Q`, `B0DS2CBVFT`, `B0DRFSFCYQ`, `B0GL785GSP`, `B0F6KRVBGR`, `B0F9ZZ17Z8`, `B0GLQ8T4P3`, `B0CT5MVCFD`, `B0FNNCDS7D`, `B0G51VX3YD`, `B0DS23SX64`, `B0DNZX4MZF`, `B0DY2SW4CH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **mundial 2026 **<br>2026年世界杯 | 3.79% |  |  | 67,617 | 797 | 19 | 1 | 327 | $1.36 | 33.79 |
| 2 | **cristiano ronaldo **<br>克里斯蒂亚诺·罗纳尔多 | 1.68% |  |  | 33,783 | 388 | 9 | 15 | 503 | $0.32 | 31.68 |
| 3 | **infant pool float **<br>婴儿泳池漂浮物 | 1.59% |  |  | 58,343 | 700 | 16 | 8 | 1,368 | $1.11 | 31.59 |
| 4 | **kids swim vest **<br>儿童游泳背心 | 1.57% |  |  | 22,819 | 273 | 7 | 14 | 7,373 | $1.15 | 31.57 |
| 5 | **life vest for toddlers 1-2 **<br>1-2 岁幼儿救生衣 | 1.10% |  |  | 16,719 | 402 | 10 | 0 | 825 | $1.31 | 31.1 |
| 6 | **swim vest for toddlers 1-2 **<br>1-2 岁幼儿游泳背心 | 1.07% |  |  | 17,648 | 241 | 6 | 1 | 512 | $1.38 | 31.07 |
| 7 | **baby life jacket 12-18 months **<br>12-18个月的婴儿救生衣 | 1.03% |  |  | 19,008 | 239 | 6 | 0 | 859 | $0.32 | 31.03 |
| 8 | **infant life vest 0-30 lbs **<br>婴儿救生衣 0-30 磅 | 0.93% |  |  | 23,098 | 607 | 14 | 0 | 648 | $0.32 | 30.93 |
| 9 | **infant life vest **<br>婴儿救生衣 | 0.91% |  |  | 19,313 | 312 | 8 | 1 | 871 | $0.63 | 30.91 |
| 10 | **soccer gifts for boys 8-12 **<br>8-12岁男孩足球礼物 | 0.89% |  |  | 23,051 | 631 | 15 | 1 | 5,067 | $0.43 | 30.89 |
| 11 | **baby swim float **<br>婴儿游泳浮台 | 0.80% |  |  | 37,952 | 664 | 16 | 9 | 1,654 | $1.06 | 30.8 |
| 12 | **golf party decorations **<br>高尔夫球派对装饰品 | 0.78% |  |  | 19,740 | 671 | 16 | 9 | 6,640 | $0.64 | 30.78 |
| 13 | **life jacket for 1 year old **<br>1岁的救生衣 | 0.93% |  |  | 16,523 | 190 | 5 | 0 | 664 | $0.33 | 30.43 |
| 14 | **fifa album 2026 **<br>FIFA 2026相册 | 1.07% |  |  | 33,902 | 138 | 4 | 0 | 84 | $0.55 | 27.97 |
| 15 | **soccer stuff **<br>足球用品 | 0.77% |  |  | 20,132 | 136 | 4 | 1 | 13,293 | $1.48 | 27.57 |
| 16 | **2026 world cup merchandise **<br>2026年世界杯商品 | 1.20% |  |  | 13,251 | 86 | 2 | 2 | 2,541 | $0.56 | 25.5 |
| 17 | **good good golf **<br>好高尔夫 | 0.81% |  |  | 19,772 | 81 | 2 | 1 | 238 | $0.90 | 24.86 |
| 18 | **golf at home **<br>在家打高尔夫球 | 1.16% |  |  | 18,827 | 58 | 2 | 1 | 392 | $1.31 | 24.06 |
| 19 | **stanley messi **<br>斯坦利·梅西 | 0.93% |  |  | 9,752 | 30 | 1 | 0 | 8,239 | $0.32 | 21.93 |
| 20 | **copa del mundo 2026 **<br>2026年世界杯 | 0.96% |  |  | 6,412 | 73 | 2 | 0 | 231 | $0.32 | 17.43 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0DSRDB4YL, B0GKMGJLL3, B0G93DF8CJ, B0DJT1YH6F, B0F5BD54RT, B0CTQTYVGP, B0DTP76XQP, B0DX2F3V5Q, B0DS2CBVFT, B0DRFSFCYQ, B0GL785GSP, B0F6KRVBGR, B0F9ZZ17Z8, B0GLQ8T4P3, B0CT5MVCFD, B0FNNCDS7D, B0G51VX3YD, B0DS23SX64, B0DNZX4MZF, B0DY2SW4CH）

1. **mundial 2026 ** — 2026年世界杯
2. **cristiano ronaldo ** — 克里斯蒂亚诺·罗纳尔多
3. **infant pool float ** — 婴儿泳池漂浮物
4. **kids swim vest ** — 儿童游泳背心
5. **2026 world cup merchandise ** — 2026年世界杯商品
6. **golf at home ** — 在家打高尔夫球
7. **life vest for toddlers 1-2 ** — 1-2 岁幼儿救生衣
8. **fifa album 2026 ** — FIFA 2026相册
9. **swim vest for toddlers 1-2 ** — 1-2 岁幼儿游泳背心
10. **baby life jacket 12-18 months ** — 12-18个月的婴儿救生衣
11. **copa del mundo 2026 ** — 2026年世界杯
12. **life jacket for 1 year old ** — 1岁的救生衣
13. **stanley messi ** — 斯坦利·梅西
14. **infant life vest 0-30 lbs ** — 婴儿救生衣 0-30 磅
15. **infant life vest ** — 婴儿救生衣
16. **soccer gifts for boys 8-12 ** — 8-12岁男孩足球礼物
17. **good good golf ** — 好高尔夫
18. **baby swim float ** — 婴儿游泳浮台
19. **golf party decorations ** — 高尔夫球派对装饰品
20. **soccer stuff ** — 足球用品

---

<!-- source: category_keywords_trophies_2026_06_14.md -->
# Trophies 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DSRDB4YL`, `B0GKMGJLL3`, `B0G93DF8CJ`, `B0DJT1YH6F`, `B0F5BD54RT`, `B0CTQTYVGP`, `B0DTP76XQP`, `B0DX2F3V5Q`, `B0DS2CBVFT`, `B0DRFSFCYQ`, `B0GL785GSP`, `B0F6KRVBGR`, `B0F9ZZ17Z8`, `B0GLQ8T4P3`, `B0CT5MVCFD`, `B0FNNCDS7D`, `B0G51VX3YD`, `B0DS23SX64`, `B0DNZX4MZF`, `B0DY2SW4CH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **mundial 2026 **<br>2026年世界杯 | 3.79% |  |  | 67,617 | 797 | 19 | 1 | 327 | $1.36 | 33.79 |
| 2 | **cristiano ronaldo **<br>克里斯蒂亚诺·罗纳尔多 | 1.68% |  |  | 33,783 | 388 | 9 | 15 | 503 | $0.32 | 31.68 |
| 3 | **infant pool float **<br>婴儿泳池漂浮物 | 1.59% |  |  | 58,343 | 700 | 16 | 8 | 1,368 | $1.11 | 31.59 |
| 4 | **kids swim vest **<br>儿童游泳背心 | 1.57% |  |  | 22,819 | 273 | 7 | 14 | 7,373 | $1.15 | 31.57 |
| 5 | **life vest for toddlers 1-2 **<br>1-2 岁幼儿救生衣 | 1.10% |  |  | 16,719 | 402 | 10 | 0 | 825 | $1.31 | 31.1 |
| 6 | **swim vest for toddlers 1-2 **<br>1-2 岁幼儿游泳背心 | 1.07% |  |  | 17,648 | 241 | 6 | 1 | 512 | $1.38 | 31.07 |
| 7 | **baby life jacket 12-18 months **<br>12-18个月的婴儿救生衣 | 1.03% |  |  | 19,008 | 239 | 6 | 0 | 859 | $0.32 | 31.03 |
| 8 | **infant life vest 0-30 lbs **<br>婴儿救生衣 0-30 磅 | 0.93% |  |  | 23,098 | 607 | 14 | 0 | 648 | $0.32 | 30.93 |
| 9 | **infant life vest **<br>婴儿救生衣 | 0.91% |  |  | 19,313 | 312 | 8 | 1 | 871 | $0.63 | 30.91 |
| 10 | **soccer gifts for boys 8-12 **<br>8-12岁男孩足球礼物 | 0.89% |  |  | 23,051 | 631 | 15 | 1 | 5,067 | $0.43 | 30.89 |
| 11 | **baby swim float **<br>婴儿游泳浮台 | 0.80% |  |  | 37,952 | 664 | 16 | 9 | 1,654 | $1.06 | 30.8 |
| 12 | **golf party decorations **<br>高尔夫球派对装饰品 | 0.78% |  |  | 19,740 | 671 | 16 | 9 | 6,640 | $0.64 | 30.78 |
| 13 | **life jacket for 1 year old **<br>1岁的救生衣 | 0.93% |  |  | 16,523 | 190 | 5 | 0 | 664 | $0.33 | 30.43 |
| 14 | **fifa album 2026 **<br>FIFA 2026相册 | 1.07% |  |  | 33,902 | 138 | 4 | 0 | 84 | $0.55 | 27.97 |
| 15 | **soccer stuff **<br>足球用品 | 0.77% |  |  | 20,132 | 136 | 4 | 1 | 13,293 | $1.48 | 27.57 |
| 16 | **2026 world cup merchandise **<br>2026年世界杯商品 | 1.20% |  |  | 13,251 | 86 | 2 | 2 | 2,541 | $0.56 | 25.5 |
| 17 | **good good golf **<br>好高尔夫 | 0.81% |  |  | 19,772 | 81 | 2 | 1 | 238 | $0.90 | 24.86 |
| 18 | **golf at home **<br>在家打高尔夫球 | 1.16% |  |  | 18,827 | 58 | 2 | 1 | 392 | $1.31 | 24.06 |
| 19 | **stanley messi **<br>斯坦利·梅西 | 0.93% |  |  | 9,752 | 30 | 1 | 0 | 8,239 | $0.32 | 21.93 |
| 20 | **copa del mundo 2026 **<br>2026年世界杯 | 0.96% |  |  | 6,412 | 73 | 2 | 0 | 231 | $0.32 | 17.43 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0DSRDB4YL, B0GKMGJLL3, B0G93DF8CJ, B0DJT1YH6F, B0F5BD54RT, B0CTQTYVGP, B0DTP76XQP, B0DX2F3V5Q, B0DS2CBVFT, B0DRFSFCYQ, B0GL785GSP, B0F6KRVBGR, B0F9ZZ17Z8, B0GLQ8T4P3, B0CT5MVCFD, B0FNNCDS7D, B0G51VX3YD, B0DS23SX64, B0DNZX4MZF, B0DY2SW4CH）

1. **mundial 2026 ** — 2026年世界杯
2. **cristiano ronaldo ** — 克里斯蒂亚诺·罗纳尔多
3. **infant pool float ** — 婴儿泳池漂浮物
4. **kids swim vest ** — 儿童游泳背心
5. **2026 world cup merchandise ** — 2026年世界杯商品
6. **golf at home ** — 在家打高尔夫球
7. **life vest for toddlers 1-2 ** — 1-2 岁幼儿救生衣
8. **fifa album 2026 ** — FIFA 2026相册
9. **swim vest for toddlers 1-2 ** — 1-2 岁幼儿游泳背心
10. **baby life jacket 12-18 months ** — 12-18个月的婴儿救生衣
11. **copa del mundo 2026 ** — 2026年世界杯
12. **life jacket for 1 year old ** — 1岁的救生衣
13. **stanley messi ** — 斯坦利·梅西
14. **infant life vest 0-30 lbs ** — 婴儿救生衣 0-30 磅
15. **infant life vest ** — 婴儿救生衣
16. **soccer gifts for boys 8-12 ** — 8-12岁男孩足球礼物
17. **good good golf ** — 好高尔夫
18. **baby swim float ** — 婴儿游泳浮台
19. **golf party decorations ** — 高尔夫球派对装饰品
20. **soccer stuff ** — 足球用品

---

<!-- source: category_keywords_wind_spinners_2026_06_14.md -->
# Wind Spinners 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GHQMHRWW`, `B0GGGPCFND`, `B0FQJVPZ4B`, `B0FJ5YYQZ4`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 300, "min_purchases": 10, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 2.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **garden spinners **<br>花园旋转器 | 13.69% |  |  | 14,941 | 176 | 4 | 1 | 6,495 | $0.71 | 42.49 |
| 2 | **garden wind spinners **<br>花园风车 | 13.08% |  |  | 14,035 | 176 | 5 | 5 | 6,363 | $0.65 | 41.88 |
| 3 | **yard spinners **<br>院子里的纺纱机 | 21.34% |  |  | 7,264 | 109 | 3 | 0 | 4,691 | $0.84 | 41.32 |
| 4 | **garden spinner **<br>花园旋转器 | 17.54% |  |  | 6,326 | 321 | 8 | 3 | 6,529 | $1.23 | 40.19 |
| 5 | **windmill for yard **<br>院子里的风车 | 6.24% |  |  | 25,212 | 274 | 7 | 6 | 2,611 | $0.32 | 36.24 |
| 6 | **spinners for yard and garden **<br>院子和花园的旋转器 | 1.27% |  |  | 12,752 | 780 | 18 | 5 | 742 | $0.76 | 31.27 |
| 7 | **garden pinwheels **<br>花园风车 | 0.31% |  |  | 7,960 | 272 | 7 | 3 | 1,426 | $0.85 | 26.23 |
| 8 | **yard spinner **<br>院子里的旋转器 | 8.97% |  |  | 3,297 | 159 | 4 | 2 | 4,572 | $0.81 | 23.51 |
| 9 | **hanging wind spinners outdoor **<br>户外悬挂风旋转器 | 0.30% |  |  | 6,073 | 79 | 2 | 2 | 2,818 | $0.71 | 16.4 |
| 10 | **wind spinner for garden **<br>花园风力旋转器 | 8.19% |  |  | 1,975 | 16 | 1 | 1 | 6,290 | $0.92 | 12.94 |
| 11 | **metal wind spinners outdoor **<br>户外金属风旋转器 | 0.14% |  |  | 5,210 | 26 | 1 | 3 | 656 | $0.75 | 11.86 |
| 12 | **metal wind spinners **<br>金属风车 | 1.76% |  |  | 2,275 | 109 | 3 | 9 | 3,961 | $0.72 | 11.76 |
| 13 | **yard spinners outdoor **<br>户外旋转花园装饰 | 0.15% |  |  | 5,381 | 16 | 1 | 0 | 591 | $0.58 | 11.71 |
| 14 | **windmills for the yard **<br>院子里的风车 | 0.26% |  |  | 2,590 | 107 | 3 | 3 | 596 | $0.32 | 10.79 |
| 15 | **outdoor spinners **<br>户外旋转器 | 0.08% |  |  | 1,851 | 122 | 3 | 0 | 528 | $0.57 | 9.88 |
| 16 | **yard windmill **<br>院子里的风车 | - |  |  | 2,446 | 77 | 2 | 4 | 2,338 | $0.32 | 8.74 |
| 17 | **whirly wind spinners **<br>旋风风车 | 1.89% |  |  | 2,924 | 14 | 1 | 0 | 1,047 | $0.52 | 8.44 |
| 18 | **wind mill **<br>风车 | 0.41% |  |  | 3,439 | 22 | 1 | 8 | 4,260 | $0.32 | 8.39 |
| 19 | **spinfinity wind spinner **<br>Spinfinity 风车 | 2.36% |  |  | 2,309 | 11 | 1 | 3 | 699 | $0.38 | 7.53 |
| 20 | **metal sublimation blanks **<br>金属升华毛坯 | 1.98% |  |  | 1,612 | 42 | 1 | 2 | 2,404 | $0.52 | 7.3 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GHQMHRWW, B0GGGPCFND, B0FQJVPZ4B, B0FJ5YYQZ4）

1. **yard spinners ** — 院子里的纺纱机
2. **garden spinner ** — 花园旋转器
3. **garden spinners ** — 花园旋转器
4. **garden wind spinners ** — 花园风车
5. **yard spinner ** — 院子里的旋转器
6. **wind spinner for garden ** — 花园风力旋转器
7. **windmill for yard ** — 院子里的风车
8. **spinfinity wind spinner ** — Spinfinity 风车
9. **metal sublimation blanks ** — 金属升华毛坯
10. **whirly wind spinners ** — 旋风风车
11. **metal wind spinners ** — 金属风车
12. **spinners for yard and garden ** — 院子和花园的旋转器
13. **wind mill ** — 风车
14. **garden pinwheels ** — 花园风车
15. **hanging wind spinners outdoor ** — 户外悬挂风旋转器
16. **windmills for the yard ** — 院子里的风车
17. **yard spinners outdoor ** — 户外旋转花园装饰
18. **metal wind spinners outdoor ** — 户外金属风旋转器
19. **outdoor spinners ** — 户外旋转器
20. **yard windmill ** — 院子里的风车
