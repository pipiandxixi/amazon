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
