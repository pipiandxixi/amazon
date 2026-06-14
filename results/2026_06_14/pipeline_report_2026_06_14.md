# 亚马逊选品完整流水线报告 (2026-06-14)

> 本文件汇总市场扫描、全部候选类目商品扫描和动态商品 ASIN 关键词反查结果。

---

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

# Swing Trainers 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $37.01　均Reviews 448（中等）　重量 0.71lbs（轻）　退货率 4.37%（低）　品牌集中度 57.1%（中等）　中国卖家 68.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT) |  | Suspension Straps Trainer with Built-in Door Anchor | 855 / 7.98% | $42,741 | $49.99 | $7.69 (15%) | 101 / 21 | 4.6 | $6.31 / 72% | 1 | 4 | 1 | 2.31 pounds | 2025-06-07 1年 |
| 2 | [B0G1MSTY15](https://www.amazon.com/dp/B0G1MSTY15) |  | Calamus GearMaster Fishing Sling Tackle Bag & Tool Set | 939 / 30.02% | $42,246 | $44.99 | $6.69 (15%) | 68 / 10 | 4.7 | $7.71 / 68% | 1 | 22 | 1 | 3.09 pounds | 2026-02-27 3个月 |
| 3 | [B0FGHZXNGV](https://www.amazon.com/dp/B0FGHZXNGV) |  | BougeRV Upgraded Telescopic Camping Light | 630 / 22.25% | $37,794 | $59.99 | $8.91 (15%) | 119 / 12 | 4.3 | $6.69 / 74% | 1 | 76 | 1 | 2.49 pounds | 2025-07-14 11个月 |
| 4 | [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3) |  | Boat Stern Light Anchor Light | 856 / 29.64% | $36,799 | $42.99 | $6.66 (15%) | 30 / 13 | 4.9 | $10.11 / 61% | 3 | 14 | 1 | 1.25 pounds | 2026-03-31 2个月 |
| 5 | [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q) |  | SILCA Ultimate Sealant Bottle | 752 / 7.13% | $33,832 | $44.99 | $6.57 (15%) | 140 / - | 4.5 | $6.48 / 71% | 4 | 19 | 1 | 2.51 pounds | 2025-02-16 1年 3个月 |
| 6 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 789 / 11.11% | $31,552 | $39.99 | $5.91 (15%) | 110 / 13 | 4.7 | $4.09 / 75% | 4 | 18 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 7 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 8 | [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP) |  | Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner | 890 / 34.88% | $28,471 | $31.99 | $4.87 (15%) | 118 / 4 | 4.5 | $4.09 / 72% | 3 | 7 | 1 | 0.29 pounds | 2024-02-06 2年 4个月 |
| 9 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 740 / 54.21% | $28,113 | $37.99 | $5.64 (15%) | 127 / 7 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 10 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | 733 / 54.82% | $26,381 | $35.99 | $5.25 (15%) | 125 / 37 | 4.6 | $5.91 / 69% | 3 | 64 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 11 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 12 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 85 / 15 | 4.5 | **** /  | 1 | 22 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 13 | [B0F62YLXK6](https://www.amazon.com/dp/B0F62YLXK6) |  | Air Horn 8.3oz for Boating | **** / **** | **** | $27.99 | - | 66 / - | 4.6 | **** /  | 1 | 8 | 1 | 0.93 pounds | 2025-05-21 1年 |
| 14 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 15 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 5 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 3个月 |
| 16 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 17 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |
| 18 | [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH) |  | Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdo… | **** / **** | **** | $36.95 | - | 111 / 3 | 4.8 | **** /  | 3 | 77 | 2 | 0.2 pounds | 2025-03-14 1年 3个月 |
| 19 | [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF) |  | Grip Enhancer Tacky Towel | **** / **** | **** | $36.99 | - | 125 / - | 4.5 | **** /  | 2 | 34 | 2 | 0.29 pounds | 2024-12-17 1年 5个月 |
| 20 | [B0FVLV78Y3](https://www.amazon.com/dp/B0FVLV78Y3) |  | Strdfeve Water Ball and Gloves Set,1PC Water Bouncing Ball&2PCS C… | **** / **** | **** | $39.99 | - | 9 / 3 | 4.2 | **** /  | 1 | 5 | 1 | 0.68 pounds | 2025-10-29 7个月 |

## 二、完整商品标题

**1. [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT)** Suspension Straps Trainer with Built-in Door Anchor, All-in-One Bodyweight Training System for Home & Outdoor Use - Quick Setup in 1 Second

**2. [B0G1MSTY15](https://www.amazon.com/dp/B0G1MSTY15)** Calamus GearMaster Fishing Sling Tackle Bag & Tool Set, 3500 Tackle Box & Fishing Gear with Fishing lures, Fishing Pliers, Fishing Scissors, Lip Gripper, Wacky Tool

**3. [B0FGHZXNGV](https://www.amazon.com/dp/B0FGHZXNGV)** BougeRV Upgraded Telescopic Camping Light, 15600mAh Rotatable Electric Lantern, Collapsible Outdoor Light, Cordless Flashlight, Waterproof, Tent Lamp for Camping, Emergency, Hiking, Outdoor

**4. [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3)** Boat Stern Light Anchor Light, 28"-48" Telescoping Pole Boat Lights LED with Base & Extra Bulb, Waterproof 3NM 360° All Round Marine Navigation Lights for Boats LED for Pontoon, Fishing, Bass Boats

**5. [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q)** SILCA Ultimate Sealant Bottle | injectable Fiber Foam

**6. [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP)** Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically Designed Human Fish Hook Removal Tool.

**7. [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL)** Sea to Summit eVac Dry Bag, Roll-Top Compression Sack, 35 Liter, Turkish Tile Blue

**8. [B0CTQTYVGP](https://www.amazon.com/dp/B0CTQTYVGP)** Naturehike 4.5oz Ultralight Washable Sleeping Bag Liner, Lightweight Adult Sleep Sack & Travel Sheets for Backpacking, Hotel, Camping, Hostels, ZY20

**9. [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT)** 75FT Wakeboard Rope and Handle, Floating Water Ski Rope for Watersports, 4 Sections Ski Ropes for Water Skiing, Kneeboarding, Wakeboarding

**10. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**11. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**12. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**13. [B0F62YLXK6](https://www.amazon.com/dp/B0F62YLXK6)** Air Horn 8.3oz for Boating, 120 dB Marine Boat Horn, Loud Airhorn for Sports Events, Outdoor & Marine Use

**14. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**15. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**16. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**17. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

**18. [B0DY2SW4CH](https://www.amazon.com/dp/B0DY2SW4CH)** Nitecore NU25 MCT UL 400 Lumen Ultralight USB-C Rechargeble Outdoor Headlamp with Multiple Color Temperatures Warm Natural, Cold Lights and Red Light (Elastic Cord, Black)

**19. [B0DNZX4MZF](https://www.amazon.com/dp/B0DNZX4MZF)** Grip Enhancer Tacky Towel - USA-Made Chalkless Competition-Approved Formula for Golf, Tennis, Softball and More - Versatile Multi-Sport Moisture Control for Sweaty Hands

**20. [B0FVLV78Y3](https://www.amazon.com/dp/B0FVLV78Y3)** Strdfeve Water Ball and Gloves Set,1PC Water Bouncing Ball&2PCS Catch Mitts,Pool Baseball Catching Mitts for Beach Games,Play Catch Skip Ball&Gloves

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0F5BD54RT`: 10,137 | 2,307 | 19% | 855 | 7.98% | $42,741 | 700+ | $34K+ | 1 | $49.99 | - | 101 | 21 | 4.6 | 2.46% | $6.31 | 72% | 2025-06-07 | 1年 | FBA | -
- `B0G1MSTY15`: 9,158 | 0 | 0% | 939 | 30.02% | $42,246 | 1K+ | $49K+ | 1 | $44.99 | - | 68 | 10 | 4.7 | 1.06% | $7.71 | 68% | 2026-02-27 | 3个月 | FBA | -
- `B0FGHZXNGV`: 15,480 | 1,144 | 7% | 630 | 22.25% | $37,794 | 500+ | $29K+ | 1 | $59.99 | - | 119 | 12 | 4.3 | 1.9% | $6.69 | 74% | 2025-07-14 | 11个月 | FBA | -
- `B0GKMGJLL3`: 10,790 | 2,203 | 17% | 856 | 29.64% | $36,799 | 600+ | $25K+ | 3 | $42.99 | - | 30 | 13 | 4.9 | 1.52% | $10.11 | 61% | 2026-03-31 | 2个月 | FBA | -
- `B0DX2F3V5Q`: 11,637 | 0 | 0% | 752 | 7.13% | $33,832 | 300+ | $13K+ | 4 | $44.99 | - | 140 | - | 4.5 | - | $6.48 | 71% | 2025-02-16 | 1年 3个月 | FBA | -
- `B0DTP76XQP`: 10,123 | 353 | 3% | 789 | 11.11% | $31,552 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 13 | 4.7 | 1.65% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0CTQTYVGP`: 8,500 | 227 | 3% | 890 | 34.88% | $28,471 | 400+ | $12K+ | 3 | $31.99 | - | 118 | 4 | 4.5 | 0.45% | $4.09 | 72% | 2024-02-06 | 2年 4个月 | FBA | -
- `B0DS2CBVFT`: 8,379 | 2,034 | 20% | 740 | 54.21% | $28,113 | 300+ | $11K+ | 5 | $37.99 | - | 127 | 7 | 4.8 | 0.95% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0GL785GSP`: 13,539 | 268 | 2% | 733 | 54.82% | $26,381 | 300+ | $10K+ | 3 | $35.99 | - | 125 | 37 | 4.6 | 5.05% | $5.91 | 69% | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0F9ZZ17Z8`: 13,699 | 581 | 4% | **** | **** | **** | **** | 1 | $41.97 | - | 85 | 15 | 4.5 | 2.42% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0F62YLXK6`: 9,609 | 0 | 0% | **** | **** | **** | **** | 1 | $27.99 | - | 66 | - | 4.6 | - | **** | 2025-05-21 | 1年 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0CT5MVCFD`: 17,365 | 1,868 | 10% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 5 | 4.8 | 0.95% | **** | 2024-03-14 | 2年 3个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -
- `B0DY2SW4CH`: 12,072 | 4,962 | 29% | **** | **** | **** | **** | 3 | $36.95 | - | 111 | 3 | 4.8 | 0.46% | **** | 2025-03-14 | 1年 3个月 | FBA | -
- `B0DNZX4MZF`: 13,386 | 0 | 0% | **** | **** | **** | **** | 2 | $36.99 | - | 125 | - | 4.5 | - | **** | 2024-12-17 | 1年 5个月 | FBA | -
- `B0FVLV78Y3`: 11,661 | 1,403 | 11% | **** | **** | **** | **** | 1 | $39.99 | - | 9 | 3 | 4.2 | 0.5% | **** | 2025-10-29 | 7个月 | FBA | -

---

# Lighting Products 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products`
> 共抓取 **20** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **20** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。

> **市场评级**：🟢 Green (Recommended)　均价 $47.85　均Reviews 482（中等）　重量 1.72lbs（偏重）　退货率 6.75%（中）　品牌集中度 51.9%（中等）　中国卖家 74.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0G6L569ZB](https://www.amazon.com/dp/B0G6L569ZB) |  | Rechargeable Submersible Pool Lights with Remote | 880 / 158.46% | $51,885 | $58.96 | $8.75 (15%) | 39 / 11 | 4.4 | $6.58 / 74% | 2 | 35 | 1 | 2.37 pounds | 2026-03-09 3个月 |
| 2 | [B0GD7YRTDM](https://www.amazon.com/dp/B0GD7YRTDM) |  | APONUO Solar Pool Lights | 893 / 162.85% | $41,069 | $45.99 | $6.70 (15%) | 40 / 12 | 4.1 | $5.72 / 73% | 3 | 37 | 1 | 1.26 pounds | 2026-03-26 2个月 |
| 3 | [B0GJCRX242](https://www.amazon.com/dp/B0GJCRX242) |  | Bsgifts Solar Floating Pool Lights | 854 / 137.86% | $28,173 | $32.99 | $5.02 (15%) | 58 / 25 | 4.0 | $5.87 / 67% | 1 | 40 | 1 | 1.32 pounds | 2026-03-19 2个月 |
| 4 | [B0DZD1RC33](https://www.amazon.com/dp/B0DZD1RC33) |  | Solar Floating Pool Lights | 518 / 88.36% | $23,818 | $45.98 | $6.86 (15%) | 132 / 11 | 4.4 | $6.01 / 72% | 2 | 100 | 2 | 2.18 pounds | 2025-05-21 1年 |
| 5 | [B0DSHT56KC](https://www.amazon.com/dp/B0DSHT56KC) |  | 500W R40 120V Pool Light Bulb for Inground Pool & Spa | 287 / 22.34% | $17,217 | $59.99 | $9.03 (15%) | 21 / - | 4.7 | $7.17 / 73% | 2 | 153 | 2 | 0.71 pounds | 2025-03-02 1年 3个月 |
| 6 | [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF) |  | Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool… | 423 / 148.32% | $16,916 | $39.99 | $6.05 (15%) | 31 / 7 | 4.4 | $4.35 / 74% | 2 | 88 | 1 | 0.44 pounds | 2025-05-07 1年 1个月 |
| 7 | [B0G6Z1QM2M](https://www.amazon.com/dp/B0G6Z1QM2M) |  | Floating Pool Lights Solar Powered | 446 / 50.41% | $13,376 | $29.99 | $4.59 (15%) | 55 / 18 | 4.6 | $5.61 / 66% | 2 | 102 | 1 | 1.37 pounds | 2026-02-07 4个月 |
| 8 | [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H) |  | SIEDiNLAR Solar Floating Pool Lights with Remote | 358 / 145.11% | $12,884 | $35.99 | $5.29 (15%) | 36 / 11 | 4.0 | $5.87 / 69% | 2 | 135 | 1 | 1.57 pounds | 2026-04-05 2个月 |
| 9 | [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB) |  | 55ft Solar Pool Lights for Above Ground Pools | 538 / 183.92% | $11,293 | $20.99 | $3.10 (15%) | 117 / 9 | 4.0 | $4.46 / 64% | 4 | 77 | 1 | 0.73 pounds | 2025-02-28 1年 3个月 |
| 10 | [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC) |  | Floating Pool Lights | 359 / 146.4% | $10,759 | $29.97 | $4.43 (15%) | 30 / 12 | 4.9 | $5.76 / 66% | 2 | 94 | 1 | 1.53 pounds | 2026-04-21 1个月 |
| 11 | [B0G6SLH595](https://www.amazon.com/dp/B0G6SLH595) |  | Floating Pool Lights w/Remote | **** / **** | **** | $49.99 | - | 39 / 1 | 4.7 | **** /  | 3 | 73 | 1 | 2.12 pounds | 2026-03-14 3个月 |
| 12 | [B0DSD4NWXN](https://www.amazon.com/dp/B0DSD4NWXN) |  | Askyli Floating Pool Lights Solar with Remote | **** / **** | **** | $39.99 | - | 138 / 4 | 4.1 | **** /  | 2 | 97 | 1 | 2.62 pounds | 2025-04-27 1年 1个月 |
| 13 | [B0FWJ6C4CY](https://www.amazon.com/dp/B0FWJ6C4CY) |  | Askyli Pool Lights for Above Ground Pools | **** / **** | **** | $25.16 | - | 36 / 9 | 4.2 | **** /  | 3 | 108 | 1 | 1.43 pounds | 2026-03-07 3个月 |
| 14 | [B0CX9162PJ](https://www.amazon.com/dp/B0CX9162PJ) |  | BOXPSII Pool Lights(4 Pack) | **** / **** | **** | $52.99 | - | 148 / 2 | 4.2 | **** /  | 3 | 187 | 1 | 1.79 pounds | 2024-04-19 2年 1个月 |
| 15 | [B0G8X6721P](https://www.amazon.com/dp/B0G8X6721P) |  | Pool Lights for Inground & Above Ground Pool | **** / **** | **** | $26.84 | - | 20 / 5 | 4.4 | **** /  | 2 | 83 | 1 | 1.23 pounds | 2026-04-07 2个月 |
| 16 | [B0FWC5JQL9](https://www.amazon.com/dp/B0FWC5JQL9) |  | 500W R40 120V Pool Lights Bulb for Inground Pool & Spa | **** / **** | **** | $53.99 | - | 14 / 3 | 4.6 | **** /  | 1 | 219 | 2 | 0.71 pounds | 2025-11-18 6个月 |
| 17 | [B0D93J8T91](https://www.amazon.com/dp/B0D93J8T91) |  | LED Pool Light Bulb 12V 50W 5000LM 6500K Daylight White LED Swimm… | **** / **** | **** | $37.99 | - | 77 / 3 | 4.0 | **** /  | 1 | 288 | 1 | 0.68 pounds | 2024-08-08 1年 10个月 |
| 18 | [B0G6TLWN2W](https://www.amazon.com/dp/B0G6TLWN2W) |  | Full Moon Floating Pool Lights | **** / **** | **** | $25.99 | - | 42 / 12 | 4.2 | **** /  | 3 | 164 | 1 | 1.17 pounds | 2026-03-27 2个月 |
| 19 | [B0DN6FBDDQ](https://www.amazon.com/dp/B0DN6FBDDQ) |  | Tujoe Remote Control LED Pool Lights for Above Ground Pools Subme… | **** / **** | **** | $30.99 | - | 32 / 1 | 4.0 | **** /  | 2 | 246 | 1 | 1.59 pounds | 2024-11-16 1年 6个月 |
| 20 | [B0GCZ27BY1](https://www.amazon.com/dp/B0GCZ27BY1) |  | Qoolife Pool Chlorine Floater with Thermometer Solar Light | **** / **** | **** | $29.99 | - | 34 / 19 | 4.0 | **** /  | 1 | 336 | 1 | 1.21 pounds | 2026-03-29 2个月 |

## 二、完整商品标题

**1. [B0G6L569ZB](https://www.amazon.com/dp/B0G6L569ZB)** Rechargeable Submersible Pool Lights with Remote, 5000mAh Underwater Led Pool Light for Above Ground Pool Lights Waterproof, 9 Modes Color Changing Magnetic Swimming Inground Pool Lights-2PC

**2. [B0GD7YRTDM](https://www.amazon.com/dp/B0GD7YRTDM)** APONUO Solar Pool Lights, IP68 Waterproof Floating Pool Lights with Remote& Button Control, 9 Lighting Colors& 3 Modes Pool Solar Light, Timer&Memory, Floating Light for Pool, Party, Bathtub (2 Pack)

**3. [B0GJCRX242](https://www.amazon.com/dp/B0GJCRX242)** Bsgifts Solar Floating Pool Lights, Outdoor LED Pool Lighted that Float with Remote, IP68 Waterproof Swimming Decor Lighting for Inground Pool, Above Ground Pools, Pond, 2 Pack

**4. [B0DZD1RC33](https://www.amazon.com/dp/B0DZD1RC33)** Solar Floating Pool Lights, 14 Inch Flame Solar Pool Light Balls, Floating Glow Globe IP68 Waterproof, Inflatable Solar Lights up Balls for Swimming Pool Pond Outdoor Decor -4PCS

**5. [B0DSHT56KC](https://www.amazon.com/dp/B0DSHT56KC)** 500W R40 120V Pool Light Bulb for Inground Pool & Spa – 3000K Warm White, E26 Base, High-Power, Compatible with Pentair & Hayward Fixtures, 3,000-Hour Lifespan (2 Pack)

**6. [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF)** Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool Light Bulb Daylight White 6000K Swimming Pool Replacement for Most Pentair Hayward Light Fixtures (120V 65W)

**7. [B0G6Z1QM2M](https://www.amazon.com/dp/B0G6Z1QM2M)** Floating Pool Lights Solar Powered, 16'' Inflatable Waterproof Clownfish Solar Pool Lights that Float, Auto On/Off LED Floating Lights for Pool Garden Backyard Outdoor Decoration - (2 Piece)

**8. [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H)** SIEDiNLAR Solar Floating Pool Lights with Remote, 12 Modes RGB Color Changing Solar Powered Pool Lights, Waterproof Floating Lights for Swimming Pool, Pond, Fountain, Backyard & Party Decor (4 Pack)

**9. [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB)** 55ft Solar Pool Lights for Above Ground Pools, 150 LEDs Remote IP65 Waterproof Rope Lights, 8 Color Modes, Swimming Frame Pool Decor Accessories for Outdoor Outside Trampoline Camping

**10. [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC)** Floating Pool Lights, 15" Inflatable Solar Powered Pool Lights That Float, Color Changing LED Glow Balls, IP68 Waterproof Solar Floating Light Up Balls for Pool,Pond, Outdoor Party Decor - 2PCS

**11. [B0G6SLH595](https://www.amazon.com/dp/B0G6SLH595)** Floating Pool Lights w/Remote, 6.5" Top to Bottom Dynamic Color Changing Solar Pool Lights that Float, IP68 Waterproof Solar Floating Light for Inground Above Ground Pools Garden Decor(2)

**12. [B0DSD4NWXN](https://www.amazon.com/dp/B0DSD4NWXN)** Askyli Floating Pool Lights Solar with Remote, 7.6 Inch RGB Up and Down Color Changing Solar Pool Lights that Float with Dynamic Lighting Effects, Floating Light for Pools, Party, Decor(2)

**13. [B0FWJ6C4CY](https://www.amazon.com/dp/B0FWJ6C4CY)** Askyli Pool Lights for Above Ground Pools, Upgraded Rechargeable Dynamic Lighting Inground Pool Lights that Float w/Remote, 16H Runtimes Underwater LED Pools Light with Timer Off for Hot Tub Pond-2PC

**14. [B0CX9162PJ](https://www.amazon.com/dp/B0CX9162PJ)** BOXPSII Pool Lights(4 Pack), Upgraded Rechargeable Submersible LED Lights with Remote, IP68 Waterproof 16 Color Floating Light with Magnet, Pool Light for Above Ground Inground Pools,Hot Tub, Bath

**15. [B0G8X6721P](https://www.amazon.com/dp/B0G8X6721P)** Pool Lights for Inground & Above Ground Pool, Underwater Submersible Swimming LED Pool Light with Remote Control,Waterproof Magnetic Pools Lights for Inground Above Ground Pools,Hot tub-1 PC

**16. [B0FWC5JQL9](https://www.amazon.com/dp/B0FWC5JQL9)** 500W R40 120V Pool Lights Bulb for Inground Pool & Spa – 3000K Warm White, E26 Base, High-Power, Compatible with Pentair & Hayward Fixtures, 3,000-Hour Lifespan (2 Pack)

**17. [B0D93J8T91](https://www.amazon.com/dp/B0D93J8T91)** LED Pool Light Bulb 12V 50W 5000LM 6500K Daylight White LED Swimming Pool Light Bulb, Replaces up to 200-800W Traditionnal Bulb for Most Pentair Hayward Light Fixtures（NOT 120V）

**18. [B0G6TLWN2W](https://www.amazon.com/dp/B0G6TLWN2W)** Full Moon Floating Pool Lights - 15" Inflatable Waterproof Solar Pool Lights that Float, Cool White&Warm White Light Up Pools Balls, Float or Hang in Pond Backyard Garden Party Decorations(2)

**19. [B0DN6FBDDQ](https://www.amazon.com/dp/B0DN6FBDDQ)** Tujoe Remote Control LED Pool Lights for Above Ground Pools Submersible Waterproof Outdoor LED Rim Rope Lights with Battery Box, Waterproof Bundle Pocket for Outdoor(55.7ft Fits18ft Pool)

**20. [B0GCZ27BY1](https://www.amazon.com/dp/B0GCZ27BY1)** Qoolife Pool Chlorine Floater with Thermometer Solar Light, 3 in1Chlorine Floater for Pond Fit 1" and 3", Floating Dispenser with Remote and Adjustable for Pool Spa Hot Tub

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0G6L569ZB`: 7,303 | 2,415 | 25% | 880 | 158.46% | $51,885 | 600+ | $35K+ | 2 | $58.96 | - | 39 | 11 | 4.4 | 1.25% | $6.58 | 74% | 2026-03-09 | 3个月 | FBA | -
- `B0GD7YRTDM`: 7,610 | 1,178 | 13% | 893 | 162.85% | $41,069 | 500+ | $22K+ | 3 | $45.99 | - | 40 | 12 | 4.1 | 1.34% | $5.72 | 73% | 2026-03-26 | 2个月 | FBA | -
- `B0GJCRX242`: 7,715 | 9,574 | 55% | 854 | 137.86% | $28,173 | 700+ | $25K+ | 1 | $32.99 | - | 58 | 25 | 4.0 | 2.93% | $5.87 | 67% | 2026-03-19 | 2个月 | FBA | -
- `B0DZD1RC33`: 22,594 | 941 | 4% | 518 | 88.36% | $23,818 | 400+ | $18K+ | 2 | $45.98 | - | 132 | 11 | 4.4 | 2.12% | $6.01 | 72% | 2025-05-21 | 1年 | FBA | -
- `B0DSHT56KC`: 33,045 | 7,232 | 18% | 287 | 22.34% | $17,217 | 200+ | $11K+ | 2 | $59.99 | - | 21 | - | 4.7 | - | $7.17 | 73% | 2025-03-02 | 1年 3个月 | FBA | -
- `B0DXVSDMZF`: 21,990 | 2,628 | 11% | 423 | 148.32% | $16,916 | 200+ | $7K+ | 2 | $39.99 | - | 31 | 7 | 4.4 | 1.65% | $4.35 | 74% | 2025-05-07 | 1年 1个月 | FBA | -
- `B0G6Z1QM2M`: 22,821 | 3,198 | 12% | 446 | 50.41% | $13,376 | 300+ | $9K+ | 2 | $29.99 | - | 55 | 18 | 4.6 | 4.04% | $5.61 | 66% | 2026-02-07 | 4个月 | FBA | -
- `B0GPW9YT5H`: 28,375 | 1,218 | 4% | 358 | 145.11% | $12,884 | 200+ | $7K+ | 2 | $35.99 | - | 36 | 11 | 4.0 | 3.07% | $5.87 | 69% | 2026-04-05 | 2个月 | FBA | -
- `B0DWMMYNDB`: 18,386 | 2,081 | 10% | 538 | 183.92% | $11,293 | 200+ | $3K+ | 4 | $20.99 | - | 117 | 9 | 4.0 | 1.67% | $4.46 | 64% | 2025-02-28 | 1年 3个月 | FBA | -
- `B0GRTPX9DC`: 22,372 | 10,423 | 30% | 359 | 146.4% | $10,759 | 200+ | $6K+ | 2 | $29.97 | - | 30 | 12 | 4.9 | 3.34% | $5.76 | 66% | 2026-04-21 | 1个月 | FBA | -
- `B0G6SLH595`: 15,292 | 31,916 | 68% | **** | **** | **** | **** | 3 | $49.99 | - | 39 | 1 | 4.7 | 0.41% | **** | 2026-03-14 | 3个月 | FBA | -
- `B0DSD4NWXN`: 22,465 | 12,329 | 35% | **** | **** | **** | **** | 2 | $39.99 | - | 138 | 4 | 4.1 | 1.31% | **** | 2025-04-27 | 1年 1个月 | FBA | -
- `B0FWJ6C4CY`: 23,928 | 10,462 | 30% | **** | **** | **** | **** | 3 | $25.16 | - | 36 | 9 | 4.2 | 2.81% | **** | 2026-03-07 | 3个月 | FBA | -
- `B0CX9162PJ`: 49,291 | 7,016 | 9% | **** | **** | **** | **** | 3 | $52.99 | - | 148 | 2 | 4.2 | 1.49% | **** | 2024-04-19 | 2年 1个月 | FBA | -
- `B0G8X6721P`: 17,271 | 21,706 | 56% | **** | **** | **** | **** | 2 | $26.84 | - | 20 | 5 | 4.4 | 2.03% | **** | 2026-04-07 | 2个月 | FBA | -
- `B0FWC5JQL9`: 60,424 | 33,248 | 36% | **** | **** | **** | **** | 1 | $53.99 | - | 14 | 3 | 4.6 | 2.86% | **** | 2025-11-18 | 6个月 | FBA | -
- `B0D93J8T91`: 57,438 | 7,874 | 12% | **** | **** | **** | **** | 1 | $37.99 | - | 77 | 3 | 4.0 | 2.01% | **** | 2024-08-08 | 1年 10个月 | FBA | -
- `B0G6TLWN2W`: 36,870 | 18,936 | 34% | **** | **** | **** | **** | 3 | $25.99 | - | 42 | 12 | 4.2 | 5.61% | **** | 2026-03-27 | 2个月 | FBA | -
- `B0DN6FBDDQ`: 45,307 | 4,504 | 9% | **** | **** | **** | **** | 2 | $30.99 | - | 32 | 1 | 4.0 | 0.74% | **** | 2024-11-16 | 1年 6个月 | FBA | -
- `B0GCZ27BY1`: 44,536 | 45,214 | 50% | **** | **** | **** | **** | 1 | $29.99 | - | 34 | 19 | 4.0 | 16.67% | **** | 2026-03-29 | 2个月 | FBA | -

---

# Nozzles 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles`
> 共抓取 **0** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $26.24　均Reviews 490（中等）　重量 0.44lbs（轻）　退货率 2.63%（低）　品牌集中度 53.8%（中等）　中国卖家 74.0%

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

# Cardboard Cutouts 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Cardboard Cutouts`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $24.38　均Reviews 295（低竞争）　重量 1.31lbs（轻）　退货率 4.59%（低）　品牌集中度 61.0%（中等）　中国卖家 62.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B09PKHLH7W](https://www.amazon.com/dp/B09PKHLH7W) |  | Cardboard People Princess Collage Life Size Cardboard Cutout Stan… | 449 / 7.42% | $21,534 | $47.96 | $7.22 (15%) | 87 / - | 4.5 | $16.76 / 50% | 1 | 63 | 2 | 2.45 pounds | 2022-01-11 4年 5个月 |
| 2 | [B0GHSNNZPZ](https://www.amazon.com/dp/B0GHSNNZPZ) |  | 131PCS Classic Winnie Baby Shower Birthday Decorations Large Winn… | 428 / 37.36% | $11,552 | $26.99 | $4.13 (15%) | 13 / 2 | 4.6 | $6.13 / 62% | 1 | 19 | 1 | 1.92 pounds | 2026-03-08 3个月 |
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
- `B0GHSNNZPZ`: 59,891 | 16,592 | 22% | 428 | 37.36% | $11,552 | 400+ | $10K+ | 1 | $26.99 | - | 13 | 2 | 4.6 | 0.47% | $6.13 | 62% | 2026-03-08 | 3个月 | FBA | -
- `B0G7YT3F1H`: 537,981 | 318,998 | 28% | 290 | 40.56% | $9,567 | - | - | 1 | $32.99 | - | 2 | - | 5.0 | - | $6.13 | 66% | 2025-12-20 | 5个月 | FBA | -
- `B0GJL3W2D6`: 118,592 | 28,152 | 19% | 281 | 159.57% | $7,584 | 200+ | $5K+ | 1 | $26.99 | - | 11 | 2 | 4.4 | 0.71% | $6.90 | 59% | 2026-03-25 | 2个月 | FBA | -
- `B0FWC8ZZ48`: 128,110 | 13,251 | 9% | 226 | 103.49% | $6,778 | 100+ | $3K+ | 4 | $29.99 | - | 14 | 2 | 4.8 | 0.88% | $6.02 | 65% | 2025-10-16 | 7个月 | FBA | -

---

# Electrical System Tools 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Automotive › Tools & Equipment › Electrical System Tools`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $29.48　均Reviews 437（中等）　重量 0.99lbs（轻）　退货率 2.38%（低）　品牌集中度 43.9%（中等）　中国卖家 82.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0C4PTWP8G](https://www.amazon.com/dp/B0C4PTWP8G) |  | JRready ST5262 2Pcs Molex Micro Fit Extractors Microfit Terminal… | 184 / 9.58% | $6,622 | $35.99 | $5.43 (15%) | 80 / 2 | 4.4 | $3.57 / 75% | 3 | 117 | 1 | 0.31 pounds | 2023-05-09 3年 1个月 |
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

# Brake System Bleeding Tools 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $27.00　均Reviews 465（中等）　重量 1.55lbs（偏重）　退货率 4.69%（低）　品牌集中度 50.2%（中等）　中国卖家 83.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GGQH744M](https://www.amazon.com/dp/B0GGQH744M) |  | Brake Bleeder Kit - One-Way Check Valve | 806 / 20.66% | $18,449 | $22.89 | $3.43 (15%) | 52 / 17 | 4.7 | $4.35 / 66% | 1 | 18 | 1 | 0.29 pounds | 2026-01-14 5个月 |
| 2 | [B0F22SXPDT](https://www.amazon.com/dp/B0F22SXPDT) |  | BleedZone SRAM DB8 Brake Bleed Kit with Maxima Mineral Oil Includ… | 103 / 56.25% | $3,316 | $32.19 | $4.99 (15%) | 14 / 3 | 4.1 | $4.35 / 71% | 2 | 216 | 1 | 0.71 pounds | 2025-04-24 1年 1个月 |

## 二、完整商品标题

**1. [B0GGQH744M](https://www.amazon.com/dp/B0GGQH744M)** Brake Bleeder Kit - One-Way Check Valve, Magnet Mount, 16oz Catch Bottle, 16” Hose

**2. [B0F22SXPDT](https://www.amazon.com/dp/B0F22SXPDT)** BleedZone SRAM DB8 Brake Bleed Kit with Maxima Mineral Oil Included, 2x Pro PC Syringe & M4 Fittings, Hydraulic Bike Brake Bleeding Kit, MTB & Road Bicycle Service Tool for SRAM Mineral Oil Systems

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GGQH744M`: 8,583 | 145 | 2% | 806 | 20.66% | $18,449 | 700+ | $16K+ | 1 | $22.89 | - | 52 | 17 | 4.7 | 2.11% | $4.35 | 66% | 2026-01-14 | 5个月 | FBA | -
- `B0F22SXPDT`: 92,590 | 57,898 | 38% | 103 | 56.25% | $3,316 | 50+ | $1K+ | 2 | $32.19 | - | 14 | 3 | 4.1 | 2.91% | $4.35 | 71% | 2025-04-24 | 1年 1个月 | FBA | -

---

# Compressed Air Dusters 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters`
> 共抓取 **7** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **7** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $35.92　均Reviews 349（中等）　重量 0.86lbs（轻）　退货率 3.16%（低）　品牌集中度 60.0%（中等）　中国卖家 76.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0FPRM62Z2](https://www.amazon.com/dp/B0FPRM62Z2) |  | Compressed Air Duster-230000RPM Super Power Electric Air Duster | 692 / 74.71% | $20,753 | $29.99 | $2.33 (8%) | 49 / 27 | 4.3 | $4.87 / 76% | 1 | 62 | 1 | 0.99 pounds | 2025-10-11 8个月 |
| 2 | [B0FFGTDMMX](https://www.amazon.com/dp/B0FFGTDMMX) |  | fourq Compressed Air Duster,Mini Vacuum Cleaner 2-in-1,4000 mAh,1… | 449 / 132.63% | $12,792 | $28.49 | $2.41 (8%) | 26 / 11 | 4.2 | $6.42 / 69% | 1 | 61 | 1 | 1.57 pounds | 2025-06-26 11个月 |
| 3 | [B0FSLLJ8SZ](https://www.amazon.com/dp/B0FSLLJ8SZ) |  | Mini Ultra-Slim Electric Compressed Air Duster 150,000RPM Super P… | 346 / 67.33% | $8,993 | $25.99 | $2.04 (8%) | 55 / - | 4.3 | $4.46 / 75% | 2 | 73 | 2 | 0.64 pounds | 2025-10-31 7个月 |
| 4 | [B0GRH6MY39](https://www.amazon.com/dp/B0GRH6MY39) |  | Electric Air Duster 180000RPM | 190 / 50% | $7,598 | $39.99 | $3.08 (8%) | 48 / 3 | 4.5 | $5.72 / 78% | 1 | 188 | 1 | 1.34 pounds | 2026-03-09 3个月 |
| 5 | [B0GGR1T98P](https://www.amazon.com/dp/B0GGR1T98P) |  | Compressed Air Duster-150000RPM Super Power Cordless Air Duster | 239 / 116.81% | $5,734 | $23.99 | $1.85 (8%) | 40 / 17 | 4.3 | $4.87 / 72% | 1 | 127 | 1 | 0.93 pounds | 2026-03-14 3个月 |
| 6 | [B0FSKJNC19](https://www.amazon.com/dp/B0FSKJNC19) |  | Compressed Air Duster - Electric Air Duster Super Power 130000RPM | 161 / 16.38% | $3,701 | $22.99 | $1.80 (8%) | 127 / 70 | 4.0 | $4.87 / 71% | 2 | 80 | 1 | 0.77 pounds | 2025-11-05 7个月 |
| 7 | [B0DB8J4T52](https://www.amazon.com/dp/B0DB8J4T52) |  | Compressed Air Duster,180000RPM Electric Duster Air Blower,Cordle… | 106 / 6.19% | $2,640 | $24.91 | $1.89 (8%) | 150 / 4 | 4.3 | $5.33 / 71% | 1 | 241 | 1 | 1.1 pounds | 2024-09-27 1年 8个月 |

## 二、完整商品标题

**1. [B0FPRM62Z2](https://www.amazon.com/dp/B0FPRM62Z2)** Compressed Air Duster-230000RPM Super Power Electric Air Duster, 4-Gear Adjustable Mini Blower with Type-C Fast Charging, Dust Blower for Computer, Keyboard, House, Outdoor and Car

**2. [B0FFGTDMMX](https://www.amazon.com/dp/B0FFGTDMMX)** fourq Compressed Air Duster,Mini Vacuum Cleaner 2-in-1,4000 mAh,130,000 RPM Brushless Motor,8000Pa，120MPH/1.1LB Thrust Car Dryer Air Blower for Car Cleaning,Computer Cleaning

**3. [B0FSLLJ8SZ](https://www.amazon.com/dp/B0FSLLJ8SZ)** Mini Ultra-Slim Electric Compressed Air Duster 150,000RPM Super Power, Rechargeable Cordless Air Duster, Powerful Airflow for Computer, Keyboard, Outdoor, House and Car

**4. [B0GRH6MY39](https://www.amazon.com/dp/B0GRH6MY39)** Electric Air Duster 180000RPM, Powerful Cordless Compressed Air Duster with 3-Speed Mini Air Duster Blower, Rechargeable Dust Cleaner for Computer Keyboard, PC, Car, Outdoor & Home Cleaning

**5. [B0GGR1T98P](https://www.amazon.com/dp/B0GGR1T98P)** Compressed Air Duster-150000RPM Super Power Cordless Air Duster, Rechargeable Brushless Motor Durable Power Blower with SOS LED Light,Adjustable Dust Blower for Computer, Pet,Outdoor, House and Car

**6. [B0FSKJNC19](https://www.amazon.com/dp/B0FSKJNC19)** Compressed Air Duster - Electric Air Duster Super Power 130000RPM, 3-Gear Adjustable Mini Duster Blower with Fast Charging, Air Duster Rechargeable for Computer, Keyboard Cleaner, House, Outdoor, Car

**7. [B0DB8J4T52](https://www.amazon.com/dp/B0DB8J4T52)** Compressed Air Duster,180000RPM Electric Duster Air Blower,Cordless Rechargeable Mini Dust Blower,3 Gear Jet Fan for PC Keyboard Computer Car Outdoor House Cleaning-Black

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0FPRM62Z2`: 10,784 | 1,981 | 16% | 692 | 74.71% | $20,753 | 600+ | $18K+ | 1 | $29.99 | - | 49 | 27 | 4.3 | 3.9% | $4.87 | 76% | 2025-10-11 | 8个月 | FBA | -
- `B0FFGTDMMX`: 11,601 | 8,576 | 43% | 449 | 132.63% | $12,792 | 400+ | $12K+ | 1 | $28.49 | - | 26 | 11 | 4.2 | 2.45% | $6.42 | 69% | 2025-06-26 | 11个月 | FBA | -
- `B0FSLLJ8SZ`: 14,507 | 10,742 | 44% | 346 | 67.33% | $8,993 | 200+ | $6K+ | 2 | $25.99 | - | 55 | - | 4.3 | - | $4.46 | 75% | 2025-10-31 | 7个月 | FBA | -
- `B0GRH6MY39`: 35,296 | 8,084 | 19% | 190 | 50% | $7,598 | 100+ | $3K+ | 1 | $39.99 | - | 48 | 3 | 4.5 | 1.58% | $5.72 | 78% | 2026-03-09 | 3个月 | FBA | -
- `B0GGR1T98P`: 38,926 | 6,292 | 15% | 239 | 116.81% | $5,734 | 200+ | $5K+ | 1 | $23.99 | - | 40 | 17 | 4.3 | 7.11% | $4.87 | 72% | 2026-03-14 | 3个月 | FBA | -
- `B0FSKJNC19`: 14,439 | 21,717 | 60% | 161 | 16.38% | $3,701 | 50+ | $1K+ | 2 | $22.99 | - | 127 | 70 | 4.0 | 43.48% | $4.87 | 71% | 2025-11-05 | 7个月 | FBA | -
- `B0DB8J4T52`: 83,972 | 4,646 | 5% | 106 | 6.19% | $2,640 | - | - | 1 | $24.91 | - | 150 | 4 | 4.3 | 3.77% | $5.33 | 71% | 2024-09-27 | 1年 8个月 | FBA | -

---

# Wind Spinners 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $31.43　均Reviews 472（中等）　重量 2.36lbs（重）　退货率 3.09%（低）　品牌集中度 54.6%（中等）　中国卖家 85.0%

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

# Decorative Trays 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays`
> 共抓取 **13** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **13** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $22.23　均Reviews 466（中等）　重量 1.45lbs（轻）　退货率 9.52%（高）　品牌集中度 42.1%（中等）　中国卖家 78.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0D8TJDXRY](https://www.amazon.com/dp/B0D8TJDXRY) |  | PEMAR Mother of Pearl Decorative Tray | 253 / 15.42% | $11,625 | $45.95 | $6.86 (15%) | 102 / 3 | 4.7 | $7.38 / 69% | 3 | 79 | 1 | 2.89 pounds | 2024-07-22 1年 10个月 |
| 2 | [B0BMDLHHYT](https://www.amazon.com/dp/B0BMDLHHYT) |  | Round Clawfoot Dish | 247 / 16.81% | $10,621 | $43.00 | $6.66 (15%) | 109 / 3 | 4.3 | $4.09 / 75% | 2 | 76 | 1 | 0.46 pounds | 2022-11-16 3年 6个月 |
| 3 | [B0FL2236YS](https://www.amazon.com/dp/B0FL2236YS) |  | PU Leather Valet Tray Organizer | 443 / 6.5% | $9,742 | $21.99 | $3.41 (15%) | 54 / 8 | 4.9 | $5.61 / 59% | 4 | 16 | 1 | 1.09 pounds | 2025-09-17 8个月 |
| 4 | [B0F9JBZVJG](https://www.amazon.com/dp/B0F9JBZVJG) |  | Key Tray Key Bowl | 268 / 30.39% | $9,377 | $34.99 | $5.16 (15%) | 34 / 6 | 4.8 | $7.79 / 63% | 2 | 46 | 1 | 2.16 pounds | 2025-08-26 9个月 |
| 5 | [B0B24B6TPX](https://www.amazon.com/dp/B0B24B6TPX) |  | Handwoven Multipurpose Rectangle Rattan Tray, 20” x 12” | 170 / 137.04% | $6,798 | $39.99 | $6.15 (15%) | 138 / 2 | 4.2 | $12.25 / 54% | 1 | 100 | 1 | 2.15 pounds | 2022-09-12 3年 9个月 |
| 6 | [B0DYP3TRL2](https://www.amazon.com/dp/B0DYP3TRL2) |  | FoldTier 11 Pcs 4th of July Decoration Patriotic Tiered Tray Deco… | 267 / 7.81% | $6,672 | $24.99 | $3.65 (15%) | 64 / 3 | 4.3 | $4.35 / 68% | 3 | 160 | 1 | 0.68 pounds | 2025-03-01 1年 3个月 |
| 7 | [B0DRYD63RT](https://www.amazon.com/dp/B0DRYD63RT) |  | 12 Inch Golden Round Platter Tray | 252 / 74.64% | $5,289 | $20.99 | $3.12 (15%) | 36 / 10 | 4.5 | $5.91 / 57% | 2 | 98 | 2 | 1.81 pounds | 2025-03-12 1年 3个月 |
| 8 | [B0G3TS1YFT](https://www.amazon.com/dp/B0G3TS1YFT) |  | Vintage Brass Decorative Tray | 176 / 21.05% | $5,278 | $29.99 | $4.56 (15%) | 23 / 12 | 4.1 | $8.04 / 58% | 5 | 148 | 1 | 2.07 pounds | 2026-01-16 4个月 |
| 9 | [B0D8MW6VS1](https://www.amazon.com/dp/B0D8MW6VS1) |  | Flamingo Zen Garden Kit for Desk | 123 / 189.47% | $5,162 | $41.97 | $6.70 (16%) | 30 / 1 | 4.7 | $6.31 / 69% | 1 | 228 | 1 | 2.31 pounds | 2024-07-03 1年 11个月 |
| 10 | [B0CCVNCZWZ](https://www.amazon.com/dp/B0CCVNCZWZ) |  | INNObeta Son Gifts Valet Tray from Dad Mom | 180 / 90.38% | $3,935 | $21.86 | $3.39 (15%) | 69 / 2 | 4.7 | $3.61 / 68% | 1 | 51 | 1 | 0.49 pounds | 2023-09-25 2年 8个月 |
| 11 | [B0FK99K3D4](https://www.amazon.com/dp/B0FK99K3D4) |  | Lounsweer Acacia Wood Decorative Tray for Home Decor | **** / **** | **** | $31.99 | - | 10 / 3 | 4.9 | **** /  | 2 | 263 | 1 | 2.67 pounds | 2025-08-03 10个月 |
| 12 | [B0D5H5TRRD](https://www.amazon.com/dp/B0D5H5TRRD) |  | Round Burnt Wood Serving Tray with Beads | **** / **** | **** | $27.59 | - | 121 / 2 | 4.6 | **** /  | 4 | 293 | 2 | 1.5 pounds | 2024-08-06 1年 10个月 |
| 13 | [B0F2HXLN8V](https://www.amazon.com/dp/B0F2HXLN8V) |  | Scalloped Acrylic Tray with Magnetic Mat | **** / **** | **** | $22.09 | - | 36 / - | 4.9 | **** /  | 4 | 223 | 1 | 1.32 pounds | 2025-04-01 1年 2个月 |

## 二、完整商品标题

**1. [B0D8TJDXRY](https://www.amazon.com/dp/B0D8TJDXRY)** PEMAR Mother of Pearl Decorative Tray, 13"" Round with Gold Metal Handles, Vanity/Perfume/Trinket Tray, Catchall for Dresser, Bathroom, Vanity Table (Teal Sunlight)

**2. [B0BMDLHHYT](https://www.amazon.com/dp/B0BMDLHHYT)** Round Clawfoot Dish — by Alice Lane Home Collection — Gold — for Home Decor, Candles, Jewelry, Perfume, Cosmetics, and Coffee Table — Size Small

**3. [B0FL2236YS](https://www.amazon.com/dp/B0FL2236YS)** PU Leather Valet Tray Organizer, Modern Nightstand Organizer Bedside Desktop Storage for Womens and Men, Decorative Perfume Trinket Catchall Vanity Tray for Key Watch Wallet (Beige)

**4. [B0F9JBZVJG](https://www.amazon.com/dp/B0F9JBZVJG)** Key Tray Key Bowl, Apartment Decor, House Warming Gifts, Key Dish, Bookshelf Decoration, Entryway Decor Ideas & Bedside Table Decor (Matte Black)

**5. [B0B24B6TPX](https://www.amazon.com/dp/B0B24B6TPX)** Handwoven Multipurpose Rectangle Rattan Tray, 20” x 12” – Durable Wicker Tray with Leather Handles for Home Decor Display

**6. [B0DYP3TRL2](https://www.amazon.com/dp/B0DYP3TRL2)** FoldTier 11 Pcs 4th of July Decoration Patriotic Tiered Tray Decor Independence Day Table Sign Wooden Faux Book Stack Firework Sign 250th Anniversary Tabletop Centerpieces for Home Office Memorial Day

**7. [B0DRYD63RT](https://www.amazon.com/dp/B0DRYD63RT)** 12 Inch Golden Round Platter Tray, Trays for Domestic Purposes, Stainless Steel Serving, Circle Decorative Tray, Vanity Tray for Centerpiece Home Decor

**8. [B0G3TS1YFT](https://www.amazon.com/dp/B0G3TS1YFT)** Vintage Brass Decorative Tray, 11.8-Inch Round Serving Tray with Claw Feet, Decorative Coffee Table Tray for Dining Room, Entryway, Living Room

**9. [B0D8MW6VS1](https://www.amazon.com/dp/B0D8MW6VS1)** Flamingo Zen Garden Kit for Desk, Cute Japanese Flamingos Gifts for Women, Mini Zen Garden Sand Tray, Pink Room Decor Aesthetic, Home Office Desk Decorations, Sand Therapy Kit

**10. [B0CCVNCZWZ](https://www.amazon.com/dp/B0CCVNCZWZ)** INNObeta Son Gifts Valet Tray from Dad Mom, Desktop Storage Organizer PU Leather Bedside Tray Key Coin Holder, Perfect for Birthday, Christmas - to My Son

**11. [B0FK99K3D4](https://www.amazon.com/dp/B0FK99K3D4)** Lounsweer Acacia Wood Decorative Tray for Home Decor, 14'' x 10'' Wooden Serving Tray for Coffee Table Centerpiece Dining Kitchen Island Decoration Bathroom Counter Display

**12. [B0D5H5TRRD](https://www.amazon.com/dp/B0D5H5TRRD)** Round Burnt Wood Serving Tray with Beads, Wooden Decorative Tray for Entertaining, Decoration, and Gifting,

**13. [B0F2HXLN8V](https://www.amazon.com/dp/B0F2HXLN8V)** Scalloped Acrylic Tray with Magnetic Mat - 8x8in Customizable Display for Photos, Art & Notes | Non-Slip Base | Elegant Décor & Organizer for Jewelry/Cosmetics for Women/Mom/Weddings

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0D8TJDXRY`: 138,174 | 870 | 1% | 253 | 15.42% | $11,625 | 50+ | $2K+ | 3 | $45.95 | - | 102 | 3 | 4.7 | 1.19% | $7.38 | 69% | 2024-07-22 | 1年 10个月 | FBA | -
- `B0BMDLHHYT`: 148,672 | 1,143 | 1% | 247 | 16.81% | $10,621 | 100+ | $4K+ | 2 | $43.00 | - | 109 | 3 | 4.3 | 1.21% | $4.09 | 75% | 2022-11-16 | 3年 6个月 | FBA | -
- `B0FL2236YS`: 65,760 | 32,778 | 33% | 443 | 6.5% | $9,742 | 100+ | $2K+ | 4 | $21.99 | - | 54 | 8 | 4.9 | 1.81% | $5.61 | 59% | 2025-09-17 | 8个月 | FBA | -
- `B0F9JBZVJG`: 101,512 | 9,166 | 8% | 268 | 30.39% | $9,377 | 100+ | $3K+ | 2 | $34.99 | - | 34 | 6 | 4.8 | 2.24% | $7.79 | 63% | 2025-08-26 | 9个月 | FBA | -
- `B0B24B6TPX`: 146,077 | 9,007 | 6% | 170 | 137.04% | $6,798 | 100+ | $3K+ | 1 | $39.99 | - | 138 | 2 | 4.2 | 1.18% | $12.25 | 54% | 2022-09-12 | 3年 9个月 | FBA | -
- `B0DYP3TRL2`: 92,454 | 44,406 | 32% | 267 | 7.81% | $6,672 | 100+ | $2K+ | 3 | $24.99 | - | 64 | 3 | 4.3 | 1.12% | $4.35 | 68% | 2025-03-01 | 1年 3个月 | FBA | -
- `B0DRYD63RT`: 171,599 | 30,826 | 15% | 252 | 74.64% | $5,289 | 200+ | $4K+ | 2 | $20.99 | - | 36 | 10 | 4.5 | 3.97% | $5.91 | 57% | 2025-03-12 | 1年 3个月 | FBA | -
- `B0G3TS1YFT`: 150,603 | 65,486 | 31% | 176 | 21.05% | $5,278 | 100+ | $3K+ | 5 | $29.99 | - | 23 | 12 | 4.1 | 6.82% | $8.04 | 58% | 2026-01-16 | 4个月 | FBA | -
- `B0D8MW6VS1`: 364,473 | 1,341 | 0% | 123 | 189.47% | $5,162 | 50+ | $1K+ | 1 | $41.97 | - | 30 | 1 | 4.7 | 0.81% | $6.31 | 69% | 2024-07-03 | 1年 11个月 | FBA | -
- `B0CCVNCZWZ`: 118,854 | 43,764 | 27% | 180 | 90.38% | $3,935 | 100+ | $2K+ | 1 | $21.86 | - | 69 | 2 | 4.7 | 1.11% | $3.61 | 68% | 2023-09-25 | 2年 8个月 | FBA | -
- `B0FK99K3D4`: 313,838 | 46,599 | 15% | **** | **** | **** | **** | 2 | $31.99 | - | 10 | 3 | 4.9 | 2.91% | **** | 2025-08-03 | 10个月 | FBA | -
- `B0D5H5TRRD`: 340,664 | 14,603 | 5% | **** | **** | **** | **** | 4 | $27.59 | - | 121 | 2 | 4.6 | 1.68% | **** | 2024-08-06 | 1年 10个月 | FBA | -
- `B0F2HXLN8V`: 278,009 | 95,045 | 32% | **** | **** | **** | **** | 4 | $22.09 | - | 36 | - | 4.9 | - | **** | 2025-04-01 | 1年 2个月 | FBA | -

---

# Game Mats & Boards 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $29.62　均Reviews 308（中等）　重量 2.47lbs（重）　退货率 7.5%（中）　品牌集中度 40.3%（中等）　中国卖家 78.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0FQ5KW2WN](https://www.amazon.com/dp/B0FQ5KW2WN) |  | Crease-Free Mahjong Mat for Table | 335 / 69.3% | $10,013 | $29.89 | $4.54 (15%) | 42 / 10 | 4.9 | $10.11 / 51% | 2 | 28 | 1 | 2.7 pounds | 2025-11-09 7个月 |
| 2 | [B0FMXW89J5](https://www.amazon.com/dp/B0FMXW89J5) |  | Chinoiserie Mahjong Mat with 1 Carrying Bag Rubber Anti Slip and… | 183 / 8.56% | $5,488 | $29.99 | $3.69 (12%) | 6 / 2 | 4.1 | $10.11 / 54% | 1 | 473 | 1 | 1.95 pounds | 2025-10-11 8个月 |
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
- `B0FMXW89J5`: 191,914 | 8,494 | 17% | 183 | 8.56% | $5,488 | - | - | 1 | $29.99 | - | 6 | 2 | 4.1 | 1.09% | $10.11 | 54% | 2025-10-11 | 8个月 | FBA | -
- `B0DD6X3QTH`: 55,693 | 42,912 | 44% | 124 | 45.07% | $4,959 | 100+ | $3K+ | 1 | $39.99 | - | 71 | 5 | 4.5 | 4.03% | $10.50 | 59% | 2024-09-17 | 1年 8个月 | FBA | -
- `B0GHHG1W42`: 41,419 | 1,500 | 3% | 194 | 56.36% | $4,072 | 100+ | $2K+ | 5 | $20.99 | - | 10 | 3 | 4.9 | 1.55% | $5.61 | 58% | 2026-03-26 | 2个月 | FBA | -
- `B0GQMQCCNH`: 52,467 | 36,206 | 41% | 128 | 21.3% | $3,967 | 50+ | $1K+ | 5 | $30.99 | - | 11 | 7 | 4.3 | 5.47% | $6.02 | 66% | 2026-04-21 | 1个月 | FBA | -

---

# Boats 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats`
> 共抓取 **4** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **4** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $56.10　均Reviews 330（中等）　重量 1.46lbs（轻）　退货率 6.03%（中）　品牌集中度 62.0%（中等）　中国卖家 68.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0DM8ZC4CC](https://www.amazon.com/dp/B0DM8ZC4CC) |  | BEZGAR Pool Toys for Kids | 261 / 62.28% | $10,437 | $39.99 | $5.87 (15%) | 101 / - | 4.2 | $6.13 / 70% | 2 | 43 | 1 | 1.54 pounds | 2024-12-30 1年 5个月 |
| 2 | [B0CWXVCT2G](https://www.amazon.com/dp/B0CWXVCT2G) |  | Losbenco RC Boat | 154 / 52.43% | $6,158 | $39.99 | $6.19 (15%) | 83 / 5 | 4.2 | $7.41 / 66% | 2 | 74 | 1 | 1.48 pounds | 2024-04-18 2年 1个月 |
| 3 | [B0CQFY22N9](https://www.amazon.com/dp/B0CQFY22N9) |  | Losbenco RC Boat | 154 / 52.43% | $6,158 | $39.99 | $6.19 (15%) | 83 / 5 | 4.2 | $7.41 / 66% | 2 | 74 | 1 | 1.5 pounds | 2024-03-02 2年 3个月 |
| 4 | [B0D8TB7V29](https://www.amazon.com/dp/B0D8TB7V29) |  | GearRoot Remote Control Dolphin Toys for Kids | 116 / 29.69% | $3,131 | $26.99 | $4.12 (15%) | 12 / - | 4.1 | $5.87 / 63% | 1 | 122 | 1 | 0.86 pounds | 2024-11-03 1年 7个月 |

## 二、完整商品标题

**1. [B0DM8ZC4CC](https://www.amazon.com/dp/B0DM8ZC4CC)** BEZGAR Pool Toys for Kids, Amphibious Remote Control Car Toys for Ages 6-8, RC Stunt Car with Water Gun for Boys and Girls 8-12, Remote Control Boat with Light(Blue)

**2. [B0CWXVCT2G](https://www.amazon.com/dp/B0CWXVCT2G)** Losbenco RC Boat, 1/72 RC Tugboat for Pools and Lakes, High-Speed Remote Control Boat with 40 Mins Play Time and Low Battery Reminder for Kids and Adults - RTR Version

**3. [B0CQFY22N9](https://www.amazon.com/dp/B0CQFY22N9)** Losbenco RC Boat, 1/72 RC Tugboat for Pools and Lakes, High-Speed Remote Control Boat with 40 Mins Play Time and Low Battery Reminder for Kids and Adults - RTR Version

**4. [B0D8TB7V29](https://www.amazon.com/dp/B0D8TB7V29)** GearRoot Remote Control Dolphin Toys for Kids, 2.4G High Simulation Oceanic RC Dolphins Fish Toys for Swimming Pool Bathroom, 2x600mAh RC Boat Water Toys Great for 6+ Year olds Boys Girls Kids, Gray

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0DM8ZC4CC`: 29,850 | 731 | 2% | 261 | 62.28% | $10,437 | 200+ | $6K+ | 2 | $39.99 | - | 101 | - | 4.2 | - | $6.13 | 70% | 2024-12-30 | 1年 5个月 | FBA | -
- `B0CWXVCT2G`: 48,617 | 24,954 | 34% | 154 | 52.43% | $6,158 | 50+ | $1K+ | 2 | $39.99 | - | 83 | 5 | 4.2 | 3.25% | $7.41 | 66% | 2024-04-18 | 2年 1个月 | FBA | -
- `B0CQFY22N9`: 47,915 | 13,752 | 22% | 154 | 52.43% | $6,158 | 50+ | $1K+ | 2 | $39.99 | - | 83 | 5 | 4.2 | 3.25% | $7.41 | 66% | 2024-03-02 | 2年 3个月 | FBA | -
- `B0D8TB7V29`: 51,139 | 19,365 | 27% | 116 | 29.69% | $3,131 | 50+ | $1K+ | 1 | $26.99 | - | 12 | - | 4.1 | - | $5.87 | 63% | 2024-11-03 | 1年 7个月 | FBA | -

---

# Grinding Discs 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs`
> 共抓取 **1** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **1** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $23.53　均Reviews 360（中等）　重量 2.02lbs（重）　退货率 2.13%（低）　品牌集中度 46.8%（中等）　中国卖家 81.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0CBS4VWYB](https://www.amazon.com/dp/B0CBS4VWYB) |  | 4 in.x 5/8-11 in. Smooth Grinding Resin Filled Diamond Cup Wheel… | 101 / 134.78% | $5,655 | $55.99 | $6.83 (12%) | 28 / 2 | 4.0 | $5.49 / 78% | 3 | 135 | 1 | 1.1 pounds | 2023-08-28 2年 9个月 |

## 二、完整商品标题

**1. [B0CBS4VWYB](https://www.amazon.com/dp/B0CBS4VWYB)** 4 in.x 5/8-11 in. Smooth Grinding Resin Filled Diamond Cup Wheel for Angle Grinder, Resin Filled Diamond Grinding Wheel for Granite Marble Engineered Stone

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0CBS4VWYB`: 58,429 | 25,781 | 31% | 101 | 134.78% | $5,655 | - | - | 3 | $55.99 | 4 | 28 | 2 | 4.0 | 1.98% | $5.49 | 78% | 2023-08-28 | 2年 9个月 | FBA | -

---

# Swing Trainers 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DSRDB4YL`, `B0GKMGJLL3`, `B0G1MSTY15`, `B0F5BD54RT`, `B0CTQTYVGP`, `B0DTP76XQP`, `B0GL785GSP`, `B0FGHZXNGV`, `B0DX2F3V5Q`, `B0DS2CBVFT`, `B0F6KRVBGR`, `B0F9ZZ17Z8`, `B0F62YLXK6`, `B0GLQ8T4P3`, `B0CT5MVCFD`, `B0FNNCDS7D`, `B0G51VX3YD`, `B0DY2SW4CH`, `B0DNZX4MZF`, `B0FVLV78Y3`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **catfishing equipment **<br>鲶鱼设备 | 2.91% |  |  | 28,440 | 264 | 6 | 2 | 3,197 | $0.41 | 32.91 |
| 2 | **tackle box backpack **<br>钓具箱背囊 | 2.82% |  |  | 23,031 | 264 | 7 | 4 | 1,907 | $0.60 | 32.82 |
| 3 | **baby life jacket 12-18 months **<br>12-18个月的婴儿救生衣 | 2.61% |  |  | 19,008 | 239 | 6 | 0 | 859 | $0.32 | 32.61 |
| 4 | **fishing tackle backpack **<br>钓具背包 | 2.45% |  |  | 20,610 | 237 | 6 | 15 | 2,767 | $0.56 | 32.45 |
| 5 | **infant life vest 0-30 lbs **<br>婴儿救生衣 0-30 磅 | 2.36% |  |  | 23,098 | 607 | 14 | 0 | 648 | $0.32 | 32.36 |
| 6 | **infant life vest **<br>婴儿救生衣 | 2.31% |  |  | 19,313 | 312 | 8 | 1 | 871 | $0.63 | 32.31 |
| 7 | **kids fishing gear **<br>儿童渔具 | 2.28% |  |  | 19,153 | 329 | 8 | 4 | 8,791 | $0.72 | 32.28 |
| 8 | **backpack tackle box **<br>背负式钓箱 | 2.07% |  |  | 18,222 | 229 | 6 | 1 | 1,950 | $0.59 | 32.07 |
| 9 | **tactical sling bag **<br>战术吊袋 | 2.19% |  |  | 20,155 | 197 | 5 | 14 | 4,745 | $0.32 | 32.04 |
| 10 | **bimini top hardware **<br>比米尼顶的硬件 | 1.95% |  |  | 15,753 | 603 | 14 | 14 | 2,640 | $0.59 | 31.95 |
| 11 | **catchers mitt **<br>捕手手套 | 1.89% |  |  | 56,467 | 677 | 16 | 3 | 3,458 | $0.32 | 31.89 |
| 12 | **life jacket for 1 year old **<br>1岁的救生衣 | 2.36% |  |  | 16,523 | 190 | 5 | 0 | 664 | $0.33 | 31.86 |
| 13 | **fishing kits for adults **<br>成人钓鱼工具包 | 1.61% |  |  | 14,223 | 433 | 10 | 0 | 10,903 | $0.67 | 31.61 |
| 14 | **tacklebox **<br>钓具箱 | 1.49% |  |  | 13,899 | 283 | 7 | 1 | 1,015 | $0.41 | 31.49 |
| 15 | **fishing accessories for men **<br>男士钓鱼配件 | 2.61% |  |  | 17,466 | 151 | 4 | 2 | 809 | $0.44 | 30.16 |
| 16 | **baby life vest **<br>婴儿救生衣 | 1.47% |  |  | 11,918 | 162 | 4 | 3 | 1,099 | $0.37 | 29.57 |
| 17 | **trout fishing gear **<br>鳟鱼渔具 | 1.84% |  |  | 20,224 | 153 | 4 | 2 | 11,454 | $0.66 | 29.49 |
| 18 | **bimini tops for boats **<br>船用比米尼顶篷 | 1.43% |  |  | 52,194 | 120 | 3 | 4 | 2,305 | $0.80 | 27.43 |
| 19 | **water aerobics weights **<br>水中有氧运动重量 | 1.55% |  |  | 6,763 | 256 | 6 | 0 | 1,729 | $0.67 | 25.08 |
| 20 | **fishing bag backpack **<br>钓鱼袋背包 | 1.43% |  |  | 9,748 | 74 | 2 | 0 | 11,736 | $0.64 | 24.63 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0DSRDB4YL, B0GKMGJLL3, B0G1MSTY15, B0F5BD54RT, B0CTQTYVGP, B0DTP76XQP, B0GL785GSP, B0FGHZXNGV, B0DX2F3V5Q, B0DS2CBVFT, B0F6KRVBGR, B0F9ZZ17Z8, B0F62YLXK6, B0GLQ8T4P3, B0CT5MVCFD, B0FNNCDS7D, B0G51VX3YD, B0DY2SW4CH, B0DNZX4MZF, B0FVLV78Y3）

1. **catfishing equipment ** — 鲶鱼设备
2. **tackle box backpack ** — 钓具箱背囊
3. **baby life jacket 12-18 months ** — 12-18个月的婴儿救生衣
4. **fishing accessories for men ** — 男士钓鱼配件
5. **fishing tackle backpack ** — 钓具背包
6. **life jacket for 1 year old ** — 1岁的救生衣
7. **infant life vest 0-30 lbs ** — 婴儿救生衣 0-30 磅
8. **infant life vest ** — 婴儿救生衣
9. **kids fishing gear ** — 儿童渔具
10. **tactical sling bag ** — 战术吊袋
11. **backpack tackle box ** — 背负式钓箱
12. **bimini top hardware ** — 比米尼顶的硬件
13. **catchers mitt ** — 捕手手套
14. **trout fishing gear ** — 鳟鱼渔具
15. **fishing kits for adults ** — 成人钓鱼工具包
16. **water aerobics weights ** — 水中有氧运动重量
17. **tacklebox ** — 钓具箱
18. **baby life vest ** — 婴儿救生衣
19. **fishing bag backpack ** — 钓鱼袋背包
20. **bimini tops for boats ** — 船用比米尼顶篷

---

# Lighting Products 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0G6L569ZB`, `B0GD7YRTDM`, `B0GJCRX242`, `B0DXVSDMZF`, `B0DSHT56KC`, `B0GRTPX9DC`, `B0GPW9YT5H`, `B0G6Z1QM2M`, `B0DZD1RC33`, `B0DWMMYNDB`, `B0G6SLH595`, `B0DSD4NWXN`, `B0FWJ6C4CY`, `B0CX9162PJ`, `B0G8X6721P`, `B0FWC5JQL9`, `B0D93J8T91`, `B0G6TLWN2W`, `B0DN6FBDDQ`, `B0GCZ27BY1`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **pool lights that float **<br>漂浮的泳池灯 | 31.41% |  |  | 5,589 | 134 | 4 | 7 | 1,061 | $0.49 | 47.88 |
| 2 | **magnetic pool lights **<br>磁池灯 | 23.99% |  |  | 6,394 | 52 | 2 | 1 | 662 | $0.59 | 39.38 |
| 3 | **solar sun rings **<br>太阳太阳环 | 10.51% |  |  | 7,800 | 269 | 7 | 9 | 230 | $0.41 | 36.11 |
| 4 | **pool balls for swimming pool **<br>游泳池球 | 0.88% |  |  | 13,458 | 767 | 18 | 2 | 6,175 | $0.67 | 30.88 |
| 5 | **outdoor pool decor **<br>室外游泳池装饰 | 8.21% |  |  | 9,318 | 70 | 2 | 3 | 498 | $0.32 | 30.35 |
| 6 | **floating solar fountain **<br>漂浮的太阳能喷泉 | 1.01% |  |  | 12,757 | 96 | 3 | 3 | 1,299 | $0.64 | 25.81 |
| 7 | **solar fountain with lights **<br>带灯的太阳能喷泉 | 3.16% |  |  | 13,539 | 51 | 2 | 0 | 2,540 | $0.59 | 25.71 |
| 8 | **floating lights for pool **<br>泳池漂浮灯 | 13.10% |  |  | 4,089 | 83 | 2 | 1 | 6,389 | $0.73 | 25.43 |
| 9 | **solar fountain for pool **<br>游泳池太阳能喷泉 | 0.50% |  |  | 20,160 | 86 | 2 | 0 | 1,395 | $0.58 | 24.8 |
| 10 | **solar flame lights **<br>太阳能火焰灯 | 0.04% |  |  | 7,810 | 152 | 4 | 3 | 2,457 | $0.63 | 23.26 |
| 11 | **hot tub lights **<br>热水浴缸灯 | 0.92% |  |  | 4,277 | 143 | 4 | 4 | 5,566 | $0.81 | 16.62 |
| 12 | **floating flowers for pool **<br>游泳池的漂浮花 | 0.04% |  |  | 2,439 | 239 | 6 | 2 | 1,061 | $0.38 | 14.92 |
| 13 | **waterproof led lights **<br>防水LED灯 | 0.10% |  |  | 5,189 | 62 | 2 | 1 | 361 | $0.45 | 13.58 |
| 14 | **velas flotantes para agua **<br>贝拉斯浮台－巴拉阿瓜 | 0.12% |  |  | 3,964 | 107 | 3 | 0 | 241 | $0.44 | 13.4 |
| 15 | **pool fountains **<br>泳池喷泉 | 0.41% |  |  | 3,859 | 52 | 2 | 10 | 6,666 | $0.62 | 10.73 |
| 16 | **pool light gasket **<br>泳池灯垫圈 | 2.03% |  |  | 2,498 | 62 | 2 | 7 | 10,558 | $0.69 | 10.13 |
| 17 | **flame solar lights **<br>火焰太阳能灯 | 0.01% |  |  | 2,959 | 80 | 2 | 0 | 3,922 | $0.63 | 9.93 |
| 18 | **waterproof lights **<br>防水灯 | - |  |  | 1,926 | 100 | 3 | 0 | 287 | $0.47 | 8.85 |
| 19 | **light up beach balls for pool **<br>为泳池点亮沙滩球 | 2.33% |  |  | 1,525 | 53 | 2 | 2 | 817 | $0.57 | 8.03 |
| 20 | **hot tub light **<br>热水浴缸灯 | 1.22% |  |  | 1,458 | 59 | 2 | 4 | 5,394 | $0.77 | 7.09 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G6L569ZB, B0GD7YRTDM, B0GJCRX242, B0DXVSDMZF, B0DSHT56KC, B0GRTPX9DC, B0GPW9YT5H, B0G6Z1QM2M, B0DZD1RC33, B0DWMMYNDB, B0G6SLH595, B0DSD4NWXN, B0FWJ6C4CY, B0CX9162PJ, B0G8X6721P, B0FWC5JQL9, B0D93J8T91, B0G6TLWN2W, B0DN6FBDDQ, B0GCZ27BY1）

1. **pool lights that float ** — 漂浮的泳池灯
2. **magnetic pool lights ** — 磁池灯
3. **floating lights for pool ** — 泳池漂浮灯
4. **solar sun rings ** — 太阳太阳环
5. **outdoor pool decor ** — 室外游泳池装饰
6. **solar fountain with lights ** — 带灯的太阳能喷泉
7. **light up beach balls for pool ** — 为泳池点亮沙滩球
8. **pool light gasket ** — 泳池灯垫圈
9. **hot tub light ** — 热水浴缸灯
10. **floating solar fountain ** — 漂浮的太阳能喷泉
11. **hot tub lights ** — 热水浴缸灯
12. **pool balls for swimming pool ** — 游泳池球
13. **solar fountain for pool ** — 游泳池太阳能喷泉
14. **pool fountains ** — 泳池喷泉
15. **velas flotantes para agua ** — 贝拉斯浮台－巴拉阿瓜
16. **waterproof led lights ** — 防水LED灯
17. **floating flowers for pool ** — 游泳池的漂浮花
18. **solar flame lights ** — 太阳能火焰灯
19. **flame solar lights ** — 火焰太阳能灯
20. **waterproof lights ** — 防水灯

---

# Cardboard Cutouts 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0G7YT3F1H`, `B0GHSNNZPZ`, `B0GJL3W2D6`, `B0FWC8ZZ48`, `B09PKHLH7W`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **winnie the pooh stickers **<br>小熊维尼贴纸 | 16.92% |  |  | 16,529 | 684 | 16 | 1 | 990 | $0.32 | 46.92 |
| 2 | **winnie the pooh baby shower **<br>小熊维尼婴儿送礼会 | 15.00% |  |  | 24,582 | 226 | 6 | 3 | 6,881 | $0.32 | 45.0 |
| 3 | **winnie the pooh nursery decor **<br>小熊维尼托儿所装饰 | 13.86% |  |  | 21,167 | 137 | 4 | 1 | 996 | $0.47 | 40.71 |
| 4 | **winnie the pooh balloons **<br>小熊维尼气球 | 10.99% |  |  | 9,553 | 251 | 6 | 0 | 769 | $0.41 | 40.1 |
| 5 | **gender reveal box **<br>性别揭示盒 | 6.59% |  |  | 12,691 | 171 | 4 | 6 | 4,960 | $0.32 | 35.14 |
| 6 | **winnie the pooh decorations **<br>小熊维尼装饰品 | 11.36% |  |  | 9,307 | 91 | 3 | 0 | 896 | $0.36 | 34.52 |
| 7 | **little people princess **<br>小人儿公主 | 3.04% |  |  | 14,178 | 450 | 11 | 0 | 1,111 | $0.32 | 33.04 |
| 8 | **winnie the pooh cake topper **<br>小熊维尼蛋糕装饰 | 0.16% |  |  | 11,464 | 311 | 8 | 0 | 244 | $0.32 | 30.16 |
| 9 | **winnie the pooh backdrop **<br>小熊维尼背景 | 1.79% |  |  | 9,284 | 121 | 3 | 0 | 513 | $0.32 | 26.41 |
| 10 | **little people disney **<br>小人物迪斯尼 | 4.54% |  |  | 7,507 | 131 | 3 | 0 | 4,633 | $0.47 | 26.1 |
| 11 | **digital circus merch **<br>数字马戏团商品 | 0.32% |  |  | 9,399 | 97 | 3 | 1 | 104 | $0.32 | 23.97 |
| 12 | **winnie the pooh balloon arch **<br>小熊维尼气球拱门 | 5.00% |  |  | 3,956 | 291 | 7 | 0 | 896 | $0.42 | 22.91 |
| 13 | **pierrot the freak circus **<br>怪诞小丑马戏团 | 0.06% |  |  | 8,787 | 100 | 3 | 3 | 65 | $0.32 | 22.63 |
| 14 | **princess backdrop **<br>公主背景 | 3.38% |  |  | 5,436 | 107 | 3 | 1 | 6,207 | $0.32 | 19.6 |
| 15 | **disney decorations **<br>迪士尼装饰品 | 0.72% |  |  | 5,248 | 132 | 3 | 0 | 905 | $0.32 | 17.82 |
| 16 | **safari backdrop **<br>野生动物园背景 | 0.06% |  |  | 3,557 | 263 | 6 | 2 | 3,553 | $0.32 | 17.17 |
| 17 | **disney party decorations **<br>迪士尼派对装饰品 | 2.38% |  |  | 5,215 | 51 | 2 | 0 | 4,601 | $0.55 | 15.36 |
| 18 | **disney princess backdrop **<br>迪士尼公主背景 | 2.18% |  |  | 3,128 | 70 | 2 | 0 | 590 | $0.32 | 11.94 |
| 19 | **neutral balloon arch kit **<br>中性气球拱形套件 | 1.26% |  |  | 2,648 | 75 | 2 | 6 | 1,125 | $0.33 | 10.31 |
| 20 | **disney princess party **<br>迪士尼公主派对 | 0.15% |  |  | 2,950 | 58 | 2 | 2 | 6,137 | $0.32 | 8.95 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G7YT3F1H, B0GHSNNZPZ, B0GJL3W2D6, B0FWC8ZZ48, B09PKHLH7W）

1. **winnie the pooh stickers ** — 小熊维尼贴纸
2. **winnie the pooh baby shower ** — 小熊维尼婴儿送礼会
3. **winnie the pooh nursery decor ** — 小熊维尼托儿所装饰
4. **winnie the pooh decorations ** — 小熊维尼装饰品
5. **winnie the pooh balloons ** — 小熊维尼气球
6. **gender reveal box ** — 性别揭示盒
7. **winnie the pooh balloon arch ** — 小熊维尼气球拱门
8. **little people disney ** — 小人物迪斯尼
9. **princess backdrop ** — 公主背景
10. **little people princess ** — 小人儿公主
11. **disney party decorations ** — 迪士尼派对装饰品
12. **disney princess backdrop ** — 迪士尼公主背景
13. **winnie the pooh backdrop ** — 小熊维尼背景
14. **neutral balloon arch kit ** — 中性气球拱形套件
15. **disney decorations ** — 迪士尼装饰品
16. **digital circus merch ** — 数字马戏团商品
17. **winnie the pooh cake topper ** — 小熊维尼蛋糕装饰
18. **disney princess party ** — 迪士尼公主派对
19. **safari backdrop ** — 野生动物园背景
20. **pierrot the freak circus ** — 怪诞小丑马戏团

---

# Electrical System Tools 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GHDJM616`, `B0C4PTWP8G`, `B0FDVDL457`, `B0CR6F2HR1`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **14** 个，过滤后保留 **14** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **compression tester automotive **<br>汽车压缩测试仪 | 25.54% |  |  | 12,395 | 739 | 17 | 5 | 1,577 | $0.69 | 55.54 |
| 2 | **hose removal pliers **<br>软管拆卸钳 | 45.07% |  |  | 3,557 | 170 | 4 | 15 | 2,193 | $0.32 | 45.61 |
| 3 | **electrical pin removal tool **<br>电针拆卸工具 | 21.24% |  |  | 2,449 | 94 | 3 | 12 | 4,619 | $0.78 | 30.84 |
| 4 | **molex connector kit **<br>molex 连接器套件 | 5.01% |  |  | 7,474 | 163 | 4 | 4 | 937 | $0.44 | 28.11 |
| 5 | **rv compartment door latch **<br>房车隔间门锁 | - |  |  | 2,193 | 184 | 5 | 3 | 4,055 | $0.60 | 13.59 |
| 6 | **compression test kit **<br>压缩测试套件 | - |  |  | 3,057 | 144 | 4 | 4 | 630 | $0.60 | 13.31 |
| 7 | **new tools **<br>新工具 | - |  |  | 1,611 | 260 | 6 | 0 | 353 | $0.47 | 13.22 |
| 8 | **roll pin removal tool **<br>滚销拆卸工具 | - |  |  | 1,386 | 179 | 5 | 3 | 1,730 | $0.48 | 11.72 |
| 9 | **molex connector **<br>摩尔克斯连接器 | 1.72% |  |  | 1,832 | 58 | 2 | 1 | 1,758 | $0.33 | 8.28 |
| 10 | **trailer latch **<br>拖车闩锁 | - |  |  | 2,067 | 76 | 2 | 6 | 9,607 | $0.63 | 7.93 |
| 11 | **deutsch crimper **<br>德式卷边机 | - |  |  | 1,186 | 111 | 3 | 6 | 651 | $0.45 | 7.92 |
| 12 | **hose clamp removal tool **<br>软管夹拆卸工具 | 1.42% |  |  | 1,347 | 69 | 2 | 9 | 4,779 | $0.38 | 7.56 |
| 13 | **small screw extractor **<br>小螺丝取出器 | - |  |  | 1,385 | 83 | 2 | 1 | 4,363 | $0.62 | 6.92 |
| 14 | **micro screw extractor **<br>微型螺丝取出器 | - |  |  | 1,235 | 61 | 2 | 1 | 357 | $0.67 | 5.52 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GHDJM616, B0C4PTWP8G, B0FDVDL457, B0CR6F2HR1）

1. **hose removal pliers ** — 软管拆卸钳
2. **compression tester automotive ** — 汽车压缩测试仪
3. **electrical pin removal tool ** — 电针拆卸工具
4. **molex connector kit ** — molex 连接器套件
5. **molex connector ** — 摩尔克斯连接器
6. **hose clamp removal tool ** — 软管夹拆卸工具
7. **trailer latch ** — 拖车闩锁
8. **small screw extractor ** — 小螺丝取出器
9. **rv compartment door latch ** — 房车隔间门锁
10. **roll pin removal tool ** — 滚销拆卸工具
11. **new tools ** — 新工具
12. **micro screw extractor ** — 微型螺丝取出器
13. **deutsch crimper ** — 德式卷边机
14. **compression test kit ** — 压缩测试套件

---

# Brake System Bleeding Tools 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GGQH744M`, `B0F22SXPDT`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **5** 个，过滤后保留 **5** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **sram brake bleed kit **<br>sram 刹车放气套件 | 32.32% |  |  | 6,586 | 545 | 13 | 4 | 520 | $0.52 | 53.17 |
| 2 | **one man brake bleeder kit AC**<br>一个人的刹车放气器套件 | 25.95% |  |  | 4,075 | 181 | 5 | 4 | 896 | $0.59 | 43.15 |
| 3 | **brake bleeder valve **<br>制动放气阀 | 23.17% |  |  | 3,528 | 297 | 7 | 13 | 2,187 | $0.54 | 40.23 |
| 4 | **sram bleed kit **<br>sram 放气套件 | 18.56% |  |  | 2,359 | 394 | 9 | 0 | 242 | $0.65 | 33.28 |
| 5 | **tektro bleed kit **<br>tektro 放血套件 | - |  |  | 1,161 | 348 | 8 | 0 | 165 | $0.57 | 12.32 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GGQH744M, B0F22SXPDT）

1. **sram brake bleed kit ** — sram 刹车放气套件
2. **one man brake bleeder kit AC** — 一个人的刹车放气器套件
3. **brake bleeder valve ** — 制动放气阀
4. **sram bleed kit ** — sram 放气套件
5. **tektro bleed kit ** — tektro 放血套件

---

# Compressed Air Dusters 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0FFGTDMMX`, `B0FPRM62Z2`, `B0FSLLJ8SZ`, `B0GGR1T98P`, `B0GRH6MY39`, `B0FSKJNC19`, `B0DB8J4T52`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **computer cleaning kit **<br>电脑清洁套装 | 27.06% |  |  | 10,463 | 562 | 13 | 1 | 4,466 | $0.73 | 57.06 |
| 2 | **mini duster **<br>迷你掸子 | 31.83% |  |  | 2,709 | 487 | 12 | 10 | 14,811 | $0.34 | 45.42 |
| 3 | **ryobi blower **<br>Ryobi blower | 9.04% |  |  | 26,188 | 267 | 7 | 0 | 3,243 | $0.67 | 39.04 |
| 4 | **gaiatop fan **<br>盖亚顶风扇 | 4.91% |  |  | 21,350 | 275 | 7 | 0 | 168 | $0.32 | 34.91 |
| 5 | **air popper **<br>气爆器 | 1.94% |  |  | 20,462 | 802 | 19 | 4 | 497 | $0.49 | 31.94 |
| 6 | **tech gadgets **<br>科技小玩意 | 1.87% |  |  | 24,315 | 851 | 20 | 3 | 12,929 | $0.67 | 31.87 |
| 7 | **computer cleaner **<br>电脑清洁剂 | 1.28% |  |  | 13,947 | 750 | 18 | 0 | 7,501 | $0.76 | 31.28 |
| 8 | **macbook cleaning kit **<br>macbook 清洁套装 | 1.01% |  |  | 11,191 | 668 | 16 | 0 | 365 | $0.68 | 31.01 |
| 9 | **tornador mini **<br>迷你龙卷风 | 1.74% |  |  | 8,051 | 229 | 6 | 2 | 243 | $0.32 | 27.84 |
| 10 | **car blower for drying **<br>车用鼓风机烘干 | 2.14% |  |  | 9,161 | 120 | 3 | 0 | 1,173 | $0.59 | 26.46 |
| 11 | **computer keyboard cleaner **<br>电脑键盘清洁剂 | 7.94% |  |  | 2,450 | 186 | 5 | 0 | 2,681 | $0.86 | 22.14 |
| 12 | **crc electronic cleaner **<br>crc电子清洁剂 | 0.73% |  |  | 5,265 | 529 | 12 | 0 | 225 | $0.44 | 21.26 |
| 13 | **desktop vacuum **<br>台式真空吸尘器 | 0.51% |  |  | 6,302 | 157 | 4 | 10 | 855 | $0.42 | 20.96 |
| 14 | **macbook cleaner **<br>笔记本电脑清洁剂 | 0.89% |  |  | 4,894 | 303 | 7 | 0 | 300 | $0.47 | 20.68 |
| 15 | **powder duster for pest control **<br>虫害防治的粉末除尘器 | 1.40% |  |  | 4,158 | 313 | 8 | 4 | 264 | $0.45 | 19.72 |
| 16 | **keyboard spray dust cleaner **<br>键盘喷尘清洁剂 | 1.44% |  |  | 3,514 | 461 | 11 | 0 | 381 | $0.71 | 18.47 |
| 17 | **blower for car detailing **<br>用于汽车细节的鼓风机 | 2.04% |  |  | 4,698 | 59 | 2 | 2 | 3,377 | $0.54 | 14.39 |
| 18 | **keyboard cleaner kit **<br>键盘清洁器套件 | 0.61% |  |  | 2,250 | 157 | 4 | 2 | 1,538 | $0.75 | 12.96 |
| 19 | **desktop vacuum cleaner **<br>桌面吸尘器 | 0.60% |  |  | 2,448 | 69 | 2 | 14 | 790 | $0.41 | 8.95 |
| 20 | **keyboard spray **<br>键盘喷雾 | 0.37% |  |  | 1,257 | 61 | 2 | 0 | 389 | $0.62 | 5.93 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0FFGTDMMX, B0FPRM62Z2, B0FSLLJ8SZ, B0GGR1T98P, B0GRH6MY39, B0FSKJNC19, B0DB8J4T52）

1. **mini duster ** — 迷你掸子
2. **computer cleaning kit ** — 电脑清洁套装
3. **ryobi blower ** — Ryobi blower
4. **computer keyboard cleaner ** — 电脑键盘清洁剂
5. **gaiatop fan ** — 盖亚顶风扇
6. **car blower for drying ** — 车用鼓风机烘干
7. **blower for car detailing ** — 用于汽车细节的鼓风机
8. **air popper ** — 气爆器
9. **tech gadgets ** — 科技小玩意
10. **tornador mini ** — 迷你龙卷风
11. **keyboard spray dust cleaner ** — 键盘喷尘清洁剂
12. **powder duster for pest control ** — 虫害防治的粉末除尘器
13. **computer cleaner ** — 电脑清洁剂
14. **macbook cleaning kit ** — macbook 清洁套装
15. **macbook cleaner ** — 笔记本电脑清洁剂
16. **crc electronic cleaner ** — crc电子清洁剂
17. **keyboard cleaner kit ** — 键盘清洁器套件
18. **desktop vacuum cleaner ** — 桌面吸尘器
19. **desktop vacuum ** — 台式真空吸尘器
20. **keyboard spray ** — 键盘喷雾

---

# Wind Spinners 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GHQMHRWW`, `B0GGGPCFND`, `B0FQJVPZ4B`, `B0FJ5YYQZ4`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **14** 个，过滤后保留 **14** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **garden wind spinners **<br>花园风车 | 46.02% |  |  | 14,035 | 176 | 5 | 5 | 6,363 | $0.65 | 58.8 |
| 2 | **garden spinners **<br>花园旋转器 | 19.10% |  |  | 14,941 | 176 | 4 | 1 | 6,495 | $0.71 | 47.9 |
| 3 | **windmill for yard **<br>院子里的风车 | 8.56% |  |  | 25,212 | 274 | 7 | 6 | 2,611 | $0.32 | 38.56 |
| 4 | **spinners for yard and garden **<br>院子和花园的旋转器 | 2.68% |  |  | 12,752 | 780 | 18 | 5 | 742 | $0.76 | 32.68 |
| 5 | **garden pinwheels **<br>花园风车 | 0.42% |  |  | 7,960 | 272 | 7 | 3 | 1,426 | $0.85 | 26.34 |
| 6 | **kinetic wind spinner **<br>动感风车 | 10.78% |  |  | 2,683 | 136 | 4 | 8 | 2,615 | $0.58 | 22.95 |
| 7 | **garden spinners outdoor **<br>户外花园旋转器 | - |  |  | 6,778 | 154 | 4 | 0 | 1,466 | $0.54 | 21.26 |
| 8 | **outdoor spinners **<br>户外旋转器 | 8.83% |  |  | 1,851 | 122 | 3 | 0 | 528 | $0.57 | 18.63 |
| 9 | **wind spinners outdoor hanging **<br>风旋转器户外悬挂 | - |  |  | 6,811 | 78 | 2 | 1 | 1,457 | $0.32 | 17.52 |
| 10 | **hanging wind spinners outdoor **<br>户外悬挂风旋转器 | 0.61% |  |  | 6,073 | 79 | 2 | 2 | 2,818 | $0.71 | 16.71 |
| 11 | **outdoor wind spinner **<br>户外风力旋转器 | - |  |  | 5,414 | 74 | 2 | 1 | 6,297 | $0.73 | 14.53 |
| 12 | **metal wind spinners **<br>金属风车 | 2.63% |  |  | 2,275 | 109 | 3 | 9 | 3,961 | $0.72 | 12.63 |
| 13 | **windmills for the yard **<br>院子里的风车 | 0.37% |  |  | 2,590 | 107 | 3 | 3 | 596 | $0.32 | 10.9 |
| 14 | **yard windmill **<br>院子里的风车 | - |  |  | 2,446 | 77 | 2 | 4 | 2,338 | $0.32 | 8.74 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GHQMHRWW, B0GGGPCFND, B0FQJVPZ4B, B0FJ5YYQZ4）

1. **garden wind spinners ** — 花园风车
2. **garden spinners ** — 花园旋转器
3. **kinetic wind spinner ** — 动感风车
4. **outdoor spinners ** — 户外旋转器
5. **windmill for yard ** — 院子里的风车
6. **spinners for yard and garden ** — 院子和花园的旋转器
7. **metal wind spinners ** — 金属风车
8. **hanging wind spinners outdoor ** — 户外悬挂风旋转器
9. **garden pinwheels ** — 花园风车
10. **windmills for the yard ** — 院子里的风车
11. **yard windmill ** — 院子里的风车
12. **wind spinners outdoor hanging ** — 风旋转器户外悬挂
13. **outdoor wind spinner ** — 户外风力旋转器
14. **garden spinners outdoor ** — 户外花园旋转器

---

# Decorative Trays 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0FL2236YS`, `B0F9JBZVJG`, `B0DRYD63RT`, `B0G3TS1YFT`, `B0DYP3TRL2`, `B0D8MW6VS1`, `B0BMDLHHYT`, `B0D8TJDXRY`, `B0CCVNCZWZ`, `B0B24B6TPX`, `B0FK99K3D4`, `B0D5H5TRRD`, `B0F2HXLN8V`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **wicker tray **<br>柳条托盘 | 8.06% |  |  | 15,838 | 224 | 6 | 7 | 4,133 | $0.36 | 38.06 |
| 2 | **nancy meyers home decor **<br>南希-迈尔斯家居装饰 | 8.91% |  |  | 15,318 | 140 | 4 | 0 | 289 | $0.32 | 35.91 |
| 3 | **round wood tray **<br>圆木托盘 | 2.49% |  |  | 11,970 | 205 | 5 | 9 | 12,645 | $0.32 | 32.49 |
| 4 | **perfume tray **<br>香水托盘 | 2.40% |  |  | 48,602 | 602 | 14 | 5 | 8,646 | $0.68 | 32.4 |
| 5 | **bedside organizer **<br>床头收纳盒 | 2.39% |  |  | 11,055 | 151 | 4 | 4 | 10,600 | $0.32 | 29.94 |
| 6 | **trinket tray **<br>饰物托盘 | 2.77% |  |  | 13,921 | 105 | 3 | 13 | 10,650 | $0.32 | 28.02 |
| 7 | **key bowl for entryway table **<br>玄关桌钥匙碗 | 4.44% |  |  | 8,166 | 102 | 3 | 11 | 2,935 | $0.35 | 25.87 |
| 8 | **round trays home decor **<br>圆形托盘家居装饰 | 5.69% |  |  | 7,595 | 99 | 3 | 1 | 565 | $0.32 | 25.83 |
| 9 | **gold serving tray **<br>金色餐盘 | 3.51% |  |  | 7,203 | 157 | 4 | 5 | 6,123 | $0.32 | 25.77 |
| 10 | **gifts for son **<br>给儿子的礼物 | 4.53% |  |  | 5,297 | 461 | 11 | 9 | 1,111 | $0.62 | 25.12 |
| 11 | **night stand organizer **<br>床头柜组织者 | 5.05% |  |  | 6,553 | 93 | 3 | 0 | 7,374 | $0.39 | 22.81 |
| 12 | **woven tray **<br>编织托盘 | 4.44% |  |  | 6,808 | 78 | 2 | 5 | 4,528 | $0.75 | 21.96 |
| 13 | **key holder bowl **<br>钥匙架碗 | 4.05% |  |  | 6,395 | 76 | 2 | 8 | 4,415 | $0.32 | 20.64 |
| 14 | **leather tray **<br>皮托盘 | 4.08% |  |  | 6,424 | 72 | 2 | 9 | 8,562 | $0.73 | 20.53 |
| 15 | **candle dish **<br>蜡烛盘 | 2.32% |  |  | 4,823 | 120 | 3 | 12 | 6,578 | $0.32 | 17.97 |
| 16 | **round decorative tray **<br>圆形装饰托盘 | 2.89% |  |  | 5,165 | 61 | 2 | 8 | 1,547 | $0.32 | 16.27 |
| 17 | **scalloped tray **<br>扇形托盘 | 2.93% |  |  | 5,322 | 52 | 2 | 11 | 2,047 | $0.64 | 16.17 |
| 18 | **gold trays for decor **<br>装饰用的金盘子 | 3.21% |  |  | 4,489 | 78 | 2 | 2 | 1,799 | $0.33 | 16.09 |
| 19 | **key dish **<br>关键菜 | 3.21% |  |  | 4,719 | 67 | 2 | 3 | 10,736 | $0.32 | 16.0 |
| 20 | **bowl for keys **<br>钥匙碗 | 3.01% |  |  | 3,970 | 94 | 3 | 2 | 838 | $0.32 | 15.65 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0FL2236YS, B0F9JBZVJG, B0DRYD63RT, B0G3TS1YFT, B0DYP3TRL2, B0D8MW6VS1, B0BMDLHHYT, B0D8TJDXRY, B0CCVNCZWZ, B0B24B6TPX, B0FK99K3D4, B0D5H5TRRD, B0F2HXLN8V）

1. **nancy meyers home decor ** — 南希-迈尔斯家居装饰
2. **wicker tray ** — 柳条托盘
3. **round trays home decor ** — 圆形托盘家居装饰
4. **night stand organizer ** — 床头柜组织者
5. **gifts for son ** — 给儿子的礼物
6. **woven tray ** — 编织托盘
7. **key bowl for entryway table ** — 玄关桌钥匙碗
8. **leather tray ** — 皮托盘
9. **key holder bowl ** — 钥匙架碗
10. **gold serving tray ** — 金色餐盘
11. **key dish ** — 关键菜
12. **gold trays for decor ** — 装饰用的金盘子
13. **bowl for keys ** — 钥匙碗
14. **scalloped tray ** — 扇形托盘
15. **round decorative tray ** — 圆形装饰托盘
16. **trinket tray ** — 饰物托盘
17. **round wood tray ** — 圆木托盘
18. **perfume tray ** — 香水托盘
19. **bedside organizer ** — 床头收纳盒
20. **candle dish ** — 蜡烛盘

---

# Game Mats & Boards 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0FMXW89J5`, `B0GHHG1W42`, `B0GQMQCCNH`, `B0FQ5KW2WN`, `B0DD6X3QTH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **mahjong mat with rules AC**<br>带规则的麻将垫 | 25.59% |  |  | 19,847 | 565 | 13 | 13 | 1,635 | $0.32 | 55.59 |
| 2 | **pokemon playmat **<br>小精灵游戏垫 | 16.37% |  |  | 17,923 | 225 | 6 | 0 | 662 | $0.44 | 46.37 |
| 3 | **mah jongg mat **<br>麻将垫 | 12.53% |  |  | 12,803 | 487 | 12 | 4 | 1,765 | $0.52 | 42.53 |
| 4 | **mahjong co. **<br>麻将公司 | 1.39% |  |  | 26,144 | 284 | 7 | 0 | 1,688 | $0.32 | 31.39 |
| 5 | **tcg playmat **<br>tcg 游戏垫 | 3.11% |  |  | 9,529 | 109 | 3 | 15 | 1,988 | $0.37 | 27.62 |
| 6 | **mahjong mat bag **<br>麻将垫袋 | 3.78% |  |  | 12,204 | 73 | 2 | 15 | 1,259 | $0.32 | 27.43 |
| 7 | **dnd starter set **<br>dnd 入门套装 | 0.31% |  |  | 8,239 | 234 | 6 | 4 | 500 | $0.74 | 26.79 |
| 8 | **mahjong atelier **<br>麻将工作室 | 3.06% |  |  | 9,948 | 70 | 2 | 0 | 213 | $0.32 | 26.46 |
| 9 | **lorcana playmat **<br>罗卡娜游戏垫 | 0.58% |  |  | 8,131 | 169 | 4 | 8 | 233 | $0.65 | 25.29 |
| 10 | **pokemon board game **<br>小精灵棋盘游戏 | 0.97% |  |  | 6,777 | 208 | 5 | 1 | 801 | $0.59 | 24.52 |
| 11 | **pokemon mat **<br>小精灵垫子 | 5.16% |  |  | 5,946 | 130 | 3 | 1 | 261 | $0.62 | 23.55 |
| 12 | **yugioh playmat **<br>瑜珈垫 | 0.22% |  |  | 8,820 | 105 | 3 | 7 | 3,184 | $0.32 | 23.11 |
| 13 | **mah jong mat **<br>麻将垫 | 5.04% |  |  | 5,187 | 151 | 4 | 2 | 2,151 | $0.49 | 22.96 |
| 14 | **mahjong table mat **<br>麻将桌垫 | 5.38% |  |  | 4,674 | 120 | 3 | 12 | 1,742 | $0.52 | 20.73 |
| 15 | **battle board **<br>战斗板 | 3.84% |  |  | 5,109 | 111 | 3 | 8 | 4,931 | $0.56 | 19.61 |
| 16 | **dnd battle map **<br>dnd战斗地图 | 2.87% |  |  | 2,764 | 98 | 3 | 5 | 434 | $0.52 | 13.3 |
| 17 | **dnd maps **<br>地图 | 2.93% |  |  | 2,705 | 96 | 3 | 2 | 556 | $0.68 | 13.14 |
| 18 | **pokemon damage counters **<br>宝可梦伤害计数器 | 2.98% |  |  | 2,754 | 75 | 2 | 0 | 331 | $0.73 | 12.24 |
| 19 | **dnd mat **<br>防静电垫 | 1.87% |  |  | 1,504 | 65 | 2 | 2 | 432 | $0.54 | 8.13 |
| 20 | **mah jongg mat for table **<br>桌上麻将垫 | 1.90% |  |  | 1,714 | 50 | 2 | 1 | 1,358 | $0.52 | 7.83 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0FMXW89J5, B0GHHG1W42, B0GQMQCCNH, B0FQ5KW2WN, B0DD6X3QTH）

1. **mahjong mat with rules AC** — 带规则的麻将垫
2. **pokemon playmat ** — 小精灵游戏垫
3. **mah jongg mat ** — 麻将垫
4. **mahjong table mat ** — 麻将桌垫
5. **pokemon mat ** — 小精灵垫子
6. **mah jong mat ** — 麻将垫
7. **battle board ** — 战斗板
8. **mahjong mat bag ** — 麻将垫袋
9. **tcg playmat ** — tcg 游戏垫
10. **mahjong atelier ** — 麻将工作室
11. **pokemon damage counters ** — 宝可梦伤害计数器
12. **dnd maps ** — 地图
13. **dnd battle map ** — dnd战斗地图
14. **mah jongg mat for table ** — 桌上麻将垫
15. **dnd mat ** — 防静电垫
16. **mahjong co. ** — 麻将公司
17. **pokemon board game ** — 小精灵棋盘游戏
18. **lorcana playmat ** — 罗卡娜游戏垫
19. **dnd starter set ** — dnd 入门套装
20. **yugioh playmat ** — 瑜珈垫

---

# Boats 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0D8TB7V29`, `B0DM8ZC4CC`, `B0CWXVCT2G`, `B0CQFY22N9`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **x shot water gun **<br>x 水枪 | 29.70% |  |  | 11,992 | 61 | 2 | 0 | 269 | $0.73 | 52.75 |
| 2 | **transformer toys for boys 4-6 **<br>4-6岁男孩的变形金刚玩具 | 12.03% |  |  | 27,946 | 857 | 20 | 0 | 1,062 | $0.48 | 42.03 |
| 3 | **lego boat **<br>乐高船 | 9.47% |  |  | 19,592 | 407 | 10 | 1 | 640 | $0.58 | 39.47 |
| 4 | **nerf guns 5-7 year old **<br>nerf 枪 5-7 岁 | 5.32% |  |  | 22,513 | 799 | 19 | 0 | 425 | $0.62 | 35.32 |
| 5 | **venom toys **<br>毒液玩具 | - |  |  | 11,777 | 281 | 7 | 0 | 813 | $0.32 | 30.0 |
| 6 | **toy boat **<br>玩具船 | 2.23% |  |  | 8,610 | 296 | 7 | 11 | 14,393 | $0.32 | 29.45 |
| 7 | **orbeez gunz **<br>奥比兹枪 | 7.10% |  |  | 8,313 | 90 | 3 | 0 | 110 | $0.39 | 28.23 |
| 8 | **toys for ages 8-13 **<br>适合8-13岁的玩具 | 3.04% |  |  | 10,565 | 91 | 3 | 2 | 9,647 | $0.47 | 27.59 |
| 9 | **jet boat for adults **<br>成人喷气船 | 2.98% |  |  | 9,757 | 66 | 2 | 2 | 3,536 | $0.81 | 25.79 |
| 10 | **aviones de juguete para niños **<br>儿童玩具飞机 | 3.76% |  |  | 7,285 | 67 | 2 | 0 | 226 | $0.44 | 21.68 |
| 11 | **toy boats **<br>玩具船 | 3.19% |  |  | 4,740 | 129 | 3 | 3 | 14,456 | $0.67 | 19.12 |
| 12 | **remote control fire truck **<br>遥控消防车 | 2.94% |  |  | 2,140 | 184 | 5 | 9 | 507 | $0.37 | 16.42 |
| 13 | **rc tugboat **<br>遥控拖船 | 9.55% |  |  | 1,588 | 73 | 2 | 15 | 244 | $0.44 | 16.38 |
| 14 | **x shot nerf guns **<br>x 射击神经枪 | - |  |  | 5,973 | 51 | 2 | 0 | 359 | $0.37 | 14.5 |
| 15 | **remote control submarine **<br>遥控潜水艇 | 1.14% |  |  | 3,397 | 112 | 3 | 5 | 313 | $0.32 | 13.53 |
| 16 | **boat toy **<br>船玩具 | 1.97% |  |  | 3,829 | 75 | 2 | 8 | 14,564 | $0.32 | 13.38 |
| 17 | **shark pool toys **<br>鲨鱼池玩具 | 1.02% |  |  | 1,584 | 171 | 4 | 2 | 1,265 | $0.42 | 12.74 |
| 18 | **unicorn monster truck **<br>独角兽怪物卡车 | - |  |  | 2,476 | 124 | 3 | 6 | 561 | $0.74 | 11.15 |
| 19 | **rc ship **<br>rc船 | 3.19% |  |  | 1,775 | 77 | 2 | 1 | 4,261 | $0.32 | 10.59 |
| 20 | **remote control bulldozer **<br>遥控推土机 | 1.36% |  |  | 2,233 | 70 | 2 | 14 | 694 | $0.40 | 9.33 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0D8TB7V29, B0DM8ZC4CC, B0CWXVCT2G, B0CQFY22N9）

1. **x shot water gun ** — x 水枪
2. **transformer toys for boys 4-6 ** — 4-6岁男孩的变形金刚玩具
3. **rc tugboat ** — 遥控拖船
4. **lego boat ** — 乐高船
5. **orbeez gunz ** — 奥比兹枪
6. **nerf guns 5-7 year old ** — nerf 枪 5-7 岁
7. **aviones de juguete para niños ** — 儿童玩具飞机
8. **rc ship ** — rc船
9. **toy boats ** — 玩具船
10. **toys for ages 8-13 ** — 适合8-13岁的玩具
11. **jet boat for adults ** — 成人喷气船
12. **remote control fire truck ** — 遥控消防车
13. **toy boat ** — 玩具船
14. **boat toy ** — 船玩具
15. **remote control bulldozer ** — 遥控推土机
16. **remote control submarine ** — 遥控潜水艇
17. **shark pool toys ** — 鲨鱼池玩具
18. **x shot nerf guns ** — x 射击神经枪
19. **venom toys ** — 毒液玩具
20. **unicorn monster truck ** — 独角兽怪物卡车

---

# Grinding Discs 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0CBS4VWYB`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **2** 个，过滤后保留 **2** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **diamond grinding wheel **<br>金刚砂轮 | 100.00% |  |  | 2,333 | 154 | 4 | 8 | 5,858 | $0.41 | 42.37 |
| 2 | **grinding stone **<br>磨石 | - |  |  | 1,551 | 67 | 2 | 11 | 12,150 | $0.56 | 6.45 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0CBS4VWYB）

1. **diamond grinding wheel ** — 金刚砂轮
2. **grinding stone ** — 磨石
