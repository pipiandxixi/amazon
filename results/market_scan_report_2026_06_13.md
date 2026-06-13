# 亚马逊选市场扫描与评估报告 (2026-06-13)

> [!IMPORTANT]
> 本报告基于配置文件 `scripts/market_config.json` 中设定的过滤与风控规则进行生成。今日共分析了 **30** 个符合基本条件的子类目，其中最终筛选出 **3** 个适合新手的 🟢 绿色推荐赛道。
> **抓取完整性**：扫描 **1** 页；页面总数提示：**223**；停止原因：免费套餐仅展示 30 个，页面提示共有 223 个类目；免费套餐截断风险：**可能存在**。
> **数量审计**：当前候选类目有 11 个，位于目标区间 8-15。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **3** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **8** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **19** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Swing Trainers** | 室内练习器 | $36.27 | 447 | 0.71 lbs | 4.37% | 57.8% | 69.0% |
| 2 | **Lighting Products** | 水底灯 | $49.26 | 480 | 1.76 lbs | 6.75% | 54.0% | 76.0% |
| 3 | **Decorative Boxes** | 装饰盒 | $24.36 | 681 | 1.68 lbs | 7.91% | 50.9% | 68.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Squirt Guns** | 水枪 | $25.87 | 619 | 1.24 lbs | 3.93% | 谨慎认证类目路径 |
| 2 | **Liver Extracts** | 肝脏提取物 | $30.08 | 845 | 0.28 lbs | 0.31% | Reviews偏高 (>800) |
| 3 | **Outdoor Statues** | 户外雕像 | $23.99 | 901 | 1.09 lbs | 2.98% | Reviews偏高 (>800) |
| 4 | **Self-Watering Stakes** | 自浇水桩 | $22.63 | 844 | 1.45 lbs | 2.8% | Reviews偏高 (>800) |
| 5 | **Figurine Lights** | 雕像灯 | $25.49 | 949 | 1.37 lbs | 2.34% | Reviews偏高 (>800) |
| 6 | **Bread Proofing Baskets** | 面包发酵篮 | $28.81 | 576 | 2.01 lbs | 4.09% | 重量偏重 (>2.0 lbs) |
| 7 | **Pool & Deck Repair Products** | 油漆及密封产品 | $31.82 | 681 | 2.28 lbs | 1.93% | 重量偏重 (>2.0 lbs) |
| 8 | **Fountains** | 喷泉 | $37.12 | 848 | 2.14 lbs | 4.78% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Short Sets** | 短盘比赛 | $28.63 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 2 | **Casual** | 休闲类 | $26.04 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 3 | **Dresses** | Dresses | $31.74 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 4 | **Workout Top & Bottom Sets** | 服装套装 | $29.09 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 5 | **Sandals** | 时装凉鞋、凉拖 | $22.71 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 6 | **Tankini Sets** | 坦基尼套装 | $22.32 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 7 | **Rash Guard Sets** | Rash Guard Sets | $21.07 | 高风险类目路径过滤 |
| 8 | **Shorts** | 短裤 | $27.01 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 9 | **Sets** | 套 | $24.21 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 10 | **Skirt Sets** | 裙装套装 | $36.05 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 11 | **Clothing** | 服装 | $25.44 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 12 | **Risers** | 竖笛 | $21.13 | Review护城河太深 (>1000) |
| 13 | **Snorkeling Packages** | 套装 | $32.04 | 退货率过高 (>10.0%) |
| 14 | **Drip Irrigation Kits** | 滴灌套件 | $33.11 | 重量超标 (>2.5 lbs) |
| 15 | **Posters & Prints** | 海报和印刷品 | $23.68 | Review护城河太深 (>1000) |
| 16 | **Rash Guard Sets** | 皮疹防护套装 | $22.62 | 高风险类目路径过滤 |
| 17 | **Pants** | 长裤 | $28.09 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 18 | **Light Therapy** | 光照疗法 | $71.28 | 退货率过高 (>10.0%) |
| 19 | **Button-Down Shirts** | 扣角领衬衫 | $20.02 | 退货率过高 (>10.0%), 高风险类目路径过滤 |

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

#### 🏆 🟢-3. Decorative Boxes (装饰盒)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.36`
  *   **平均 Reviews (Avg Reviews)**：`681 个`
  *   **物理重量 (Weight)**：`1.68 lbs`
  *   **平均退货率 (Return Rate)**：`7.91%`
  *   **平均毛利率 (Profit Margin)**：`57.59%`
  *   **品牌集中度 (Brand Concentration)**：`50.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰盒`
  *   **A+数量占比**：`78%`
  *   **新品平均评分数**：`65`
  *   **新品平均价格**：`$ 21.72`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`886`
  *   **新品月均销售额**：`$20,623`
  *   **平均重量**：`1.68 pounds (762 g)`
  *   **平均体积**：`347.00 in³ (5,686 cm³)`
  *   **平均毛利率**：`57.59%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`4.5‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Squirt Guns (水枪)

- **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.87`
  *   **平均 Reviews (Avg Reviews)**：`619 个`
  *   **物理重量 (Weight)**：`1.24 lbs`
  *   **平均退货率 (Return Rate)**：`3.93%`
  *   **平均毛利率 (Profit Margin)**：`54.03%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
  *   **市场路径(中文)**：`玩具 › 体育 › 游泳池 › 水枪`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`150`
  *   **新品平均价格**：`$ 31.59`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`1,693`
  *   **新品月均销售额**：`$50,445`
  *   **平均重量**：`1.24 pounds (560 g)`
  *   **平均体积**：`262.32 in³ (4,299 cm³)`
  *   **平均毛利率**：`54.03%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`5.7‰`

---

#### 🏆 🟡-2. Liver Extracts (肝脏提取物)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Glandular Extracts › Liver Extracts  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.08`
  *   **平均 Reviews (Avg Reviews)**：`845 个`
  *   **物理重量 (Weight)**：`0.28 lbs`
  *   **平均退货率 (Return Rate)**：`0.31%`
  *   **平均毛利率 (Profit Margin)**：`68.57%`
  *   **品牌集中度 (Brand Concentration)**：`62.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`17.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Glandular Extracts › Liver Extracts  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 身、泳和附剂 › 圣诞体提取物 › 肝脏提取物`
  *   **A+数量占比**：`94%`
  *   **新品平均评分数**：`75`
  *   **新品平均价格**：`$ 31.38`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`1,133`
  *   **新品月均销售额**：`$36,344`
  *   **平均重量**：`0.28 pounds (128 g)`
  *   **平均体积**：`43.40 in³ (711 cm³)`
  *   **平均毛利率**：`68.57%`
  *   **卖家所属地**：`美国|83.0%`
  *   **搜索购买比**：`22.9‰`

---

#### 🏆 🟡-3. Outdoor Statues (户外雕像)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Outdoor Statues  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.99`
  *   **平均 Reviews (Avg Reviews)**：`901 个`
  *   **物理重量 (Weight)**：`1.09 lbs`
  *   **平均退货率 (Return Rate)**：`2.98%`
  *   **平均毛利率 (Profit Margin)**：`57.01%`
  *   **品牌集中度 (Brand Concentration)**：`43.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Outdoor Statues  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 雕塑、雕像 › 户外雕像`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`61`
  *   **新品平均价格**：`$ 21.63`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`1,257`
  *   **新品月均销售额**：`$26,095`
  *   **平均重量**：`1.09 pounds (493 g)`
  *   **平均体积**：`471.44 in³ (7,725 cm³)`
  *   **平均毛利率**：`57.01%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`5.1‰`

---

#### 🏆 🟡-4. Self-Watering Stakes (自浇水桩)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Pots, Planters & Container Accessories › Plant Container Accessories › Self-Watering Stakes  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.63`
  *   **平均 Reviews (Avg Reviews)**：`844 个`
  *   **物理重量 (Weight)**：`1.45 lbs`
  *   **平均退货率 (Return Rate)**：`2.8%`
  *   **平均毛利率 (Profit Margin)**：`52.55%`
  *   **品牌集中度 (Brand Concentration)**：`52.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Pots, Planters & Container Accessories › Plant Container Accessories › Self-Watering Stakes  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 花盆、花架、育苗盘 › 花盆配件 › 自浇水桩`
  *   **A+数量占比**：`92%`
  *   **新品平均评分数**：`444`
  *   **新品平均价格**：`$ 19.33`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`698`
  *   **新品月均销售额**：`$13,770`
  *   **平均重量**：`1.45 pounds (657 g)`
  *   **平均体积**：`136.87 in³ (2,243 cm³)`
  *   **平均毛利率**：`52.55%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`12.2‰`

---

#### 🏆 🟡-5. Figurine Lights (雕像灯)

- **完整市场路径**：`Tools & Home Improvement › Lighting & Ceiling Fans › Outdoor Lighting › Landscape Lighting › Figurine Lights  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.49`
  *   **平均 Reviews (Avg Reviews)**：`949 个`
  *   **物理重量 (Weight)**：`1.37 lbs`
  *   **平均退货率 (Return Rate)**：`2.34%`
  *   **平均毛利率 (Profit Margin)**：`57.1%`
  *   **品牌集中度 (Brand Concentration)**：`54.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`84.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Lighting & Ceiling Fans › Outdoor Lighting › Landscape Lighting › Figurine Lights  市场分析`
  *   **市场路径(中文)**：`工具 › 照明 › 户外照明 › 景观照明 › 雕像灯`
  *   **A+数量占比**：`97%`
  *   **新品平均评分数**：`75`
  *   **新品平均价格**：`$ 23.2`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`959`
  *   **新品月均销售额**：`$21,144`
  *   **平均重量**：`1.37 pounds (623 g)`
  *   **平均体积**：`287.77 in³ (4,716 cm³)`
  *   **平均毛利率**：`57.1%`
  *   **卖家所属地**：`中国|84.0%`
  *   **搜索购买比**：`4.9‰`

---

#### 🏆 🟡-6. Bread Proofing Baskets (面包发酵篮)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.81`
  *   **平均 Reviews (Avg Reviews)**：`576 个`
  *   **物理重量 (Weight)**：`2.01 lbs`
  *   **平均退货率 (Return Rate)**：`4.09%`
  *   **平均毛利率 (Profit Margin)**：`56.92%`
  *   **品牌集中度 (Brand Concentration)**：`53.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 烘焙用具 › 烘焙工具 › 烘焙 › 面包发酵篮`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`91`
  *   **新品平均价格**：`$ 28.1`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`586`
  *   **新品月均销售额**：`$16,648`
  *   **平均重量**：`2.01 pounds (910 g)`
  *   **平均体积**：`394.94 in³ (6,472 cm³)`
  *   **平均毛利率**：`56.92%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟡-7. Pool & Deck Repair Products (油漆及密封产品)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.82`
  *   **平均 Reviews (Avg Reviews)**：`681 个`
  *   **物理重量 (Weight)**：`2.28 lbs`
  *   **平均退货率 (Return Rate)**：`1.93%`
  *   **平均毛利率 (Profit Margin)**：`58.49%`
  *   **品牌集中度 (Brand Concentration)**：`57.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 油漆及密封产品`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`62`
  *   **新品平均价格**：`$ 19.47`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`677`
  *   **新品月均销售额**：`$13,309`
  *   **平均重量**：`2.28 pounds (1,032 g)`
  *   **平均体积**：`643.59 in³ (10,547 cm³)`
  *   **平均毛利率**：`58.49%`
  *   **卖家所属地**：`美国|52.0%`
  *   **搜索购买比**：`23.2‰`

---

#### 🏆 🟡-8. Fountains (喷泉)

- **完整市场路径**：`Pet Supplies › Dogs › Feeding & Watering Supplies › Fountains  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$37.12`
  *   **平均 Reviews (Avg Reviews)**：`848 个`
  *   **物理重量 (Weight)**：`2.14 lbs`
  *   **平均退货率 (Return Rate)**：`4.78%`
  *   **平均毛利率 (Profit Margin)**：`63.26%`
  *   **品牌集中度 (Brand Concentration)**：`54.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Dogs › Feeding & Watering Supplies › Fountains  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 犬类 › 喂食 › 喷泉`
  *   **A+数量占比**：`94%`
  *   **新品平均评分数**：`83`
  *   **新品平均价格**：`$ 42.65`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`599`
  *   **新品月均销售额**：`$25,591`
  *   **平均重量**：`2.14 pounds (972 g)`
  *   **平均体积**：`542.30 in³ (8,887 cm³)`
  *   **平均毛利率**：`63.26%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`10.2‰`

---
