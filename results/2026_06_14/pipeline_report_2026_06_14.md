# 亚马逊选品完整流水线报告 (2026-06-14)

> 本文件汇总市场扫描、全部候选类目商品扫描和动态商品 ASIN 关键词反查结果。

---

# 亚马逊选市场扫描与评估报告 (2026-06-14)

> [!IMPORTANT]
> 本报告基于 `unified pipeline config` 中设定的过滤与风控规则进行生成。今日共分析了 **30** 个符合基本条件的子类目，其中最终筛选出 **3** 个适合新手的 🟢 绿色推荐赛道。
> **抓取完整性**：扫描 **1** 页；页面总数提示：**365**；停止原因：免费套餐仅展示 30 个，页面提示共有 365 个类目；免费套餐截断风险：**可能存在**。
> **数量审计**：当前候选类目有 10 个，位于目标区间 8-25。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **3** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **7** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **20** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Swing Trainers** | 室内练习器 | $37.01 | 448 | 0.71 lbs | 4.37% | 57.1% | 68.0% |
| 2 | **Lighting Products** | 水底灯 | $47.85 | 482 | 1.72 lbs | 6.75% | 51.9% | 74.0% |
| 3 | **Nicotine Patches** | 尼古丁药膏 | $22.22 | 468 | 0.13 lbs | 1.27% | 73.4% | 49.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Water Balloons** | 水气球 | $21.35 | 694 | 0.82 lbs | 1.83% | Reviews偏高 (>550), 谨慎认证类目路径 |
| 2 | **Squirt Guns** | 水枪 | $25.91 | 619 | 1.24 lbs | 3.93% | Reviews偏高 (>550), 谨慎认证类目路径 |
| 3 | **Drip Irrigation Kits** | 滴灌套件 | $33.30 | 618 | 2.58 lbs | 3.37% | 重量偏重 (>2.5 lbs), Reviews偏高 (>550) |
| 4 | **Bread Proofing Baskets** | 面包发酵篮 | $29.00 | 570 | 2.03 lbs | 4.09% | Reviews偏高 (>550) |
| 5 | **Ultrasonic Repellers** | Ultrasonic Repellers | $28.76 | 625 | 0.61 lbs | 3.27% | Reviews偏高 (>550) |
| 6 | **Decorative Boxes** | 装饰盒 | $23.78 | 694 | 1.57 lbs | 7.91% | Reviews偏高 (>550) |
| 7 | **Pool & Deck Repair Products** | 油漆及密封产品 | $31.79 | 682 | 2.28 lbs | 1.93% | Reviews偏高 (>550) |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Short Sets** | 短盘比赛 | $28.49 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 2 | **Pullovers** | 套头衫 | $22.12 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 3 | **Dresses** | Dresses | $32.04 | 退货率过高 (>10.0%), Review护城河太深 (>700), 高风险类目路径过滤 |
| 4 | **Workout Top & Bottom Sets** | 服装套装 | $28.82 | 退货率过高 (>10.0%), Review护城河太深 (>700), 高风险类目路径过滤 |
| 5 | **Vests** | 针织背心 | $21.37 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 6 | **Polos** | Polos | $20.98 | 退货率过高 (>10.0%), Review护城河太深 (>700), 高风险类目路径过滤 |
| 7 | **Tankini Sets** | 坦基尼套装 | $22.41 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 8 | **Rash Guard Sets** | Rash Guard Sets | $20.98 | 高风险类目路径过滤 |
| 9 | **Sets** | 套 | $24.13 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 10 | **Skirt Sets** | 裙装套装 | $35.46 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 11 | **Trellises** | 格架 | $26.71 | 重量超标 (>4.0 lbs) |
| 12 | **Pool Hoses** | 泳池软管 | $31.60 | Review护城河太深 (>700) |
| 13 | **Clothing** | 服装 | $24.85 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 14 | **Track & Active Jackets** | 风衣、夹克 | $29.81 | 退货率过高 (>10.0%), Review护城河太深 (>700), 高风险类目路径过滤 |
| 15 | **Handheld Steamers** | 手持式蒸汽机 | $67.20 | 重量超标 (>4.0 lbs) |
| 16 | **Rash Guard Sets** | 皮疹防护套装 | $22.34 | 高风险类目路径过滤 |
| 17 | **Skirts** | 裙子 | $24.15 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 18 | **Light Therapy** | 光照疗法 | $70.55 | 退货率过高 (>10.0%), Review护城河太深 (>700), 高风险类目路径过滤 |
| 19 | **Fountains** | 喷泉 | $36.81 | Review护城河太深 (>700) |
| 20 | **Pants & Capris** | 长裤和紧身裤 | $22.90 | 退货率过高 (>10.0%), Review护城河太深 (>700), 高风险类目路径过滤 |

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

#### 🏆 🟢-3. Nicotine Patches (尼古丁药膏)

- **完整市场路径**：`Health & Household › Health Care › Smoking Cessation › Nicotine Patches  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.22`
  *   **平均 Reviews (Avg Reviews)**：`468 个`
  *   **物理重量 (Weight)**：`0.13 lbs`
  *   **平均退货率 (Return Rate)**：`1.27%`
  *   **平均毛利率 (Profit Margin)**：`65.13%`
  *   **品牌集中度 (Brand Concentration)**：`73.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`49.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Smoking Cessation › Nicotine Patches  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 戒烟 › 尼古丁药膏`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`38`
  *   **新品平均价格**：`$ 21.54`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`457`
  *   **新品月均销售额**：`$8,331`
  *   **平均重量**：`0.13 pounds (59 g)`
  *   **平均体积**：`18.07 in³ (296 cm³)`
  *   **平均毛利率**：`65.13%`
  *   **卖家所属地**：`中国|49.0%`
  *   **搜索购买比**：`24.3‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Water Balloons (水气球)

- **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Water Balloons  市场分析`
- **触发警示项**：`Reviews偏高 (>550), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.35`
  *   **平均 Reviews (Avg Reviews)**：`694 个`
  *   **物理重量 (Weight)**：`0.82 lbs`
  *   **平均退货率 (Return Rate)**：`1.83%`
  *   **平均毛利率 (Profit Margin)**：`56.27%`
  *   **品牌集中度 (Brand Concentration)**：`74.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Water Balloons  市场分析`
  *   **市场路径(中文)**：`玩具 › 体育 › 游泳池 › 水气球`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`39`
  *   **新品平均价格**：`$ 21`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`694`
  *   **新品月均销售额**：`$15,449`
  *   **平均重量**：`0.82 pounds (372 g)`
  *   **平均体积**：`482.64 in³ (7,909 cm³)`
  *   **平均毛利率**：`56.27%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`10.2‰`

---

#### 🏆 🟡-2. Squirt Guns (水枪)

- **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
- **触发警示项**：`Reviews偏高 (>550), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.91`
  *   **平均 Reviews (Avg Reviews)**：`619 个`
  *   **物理重量 (Weight)**：`1.24 lbs`
  *   **平均退货率 (Return Rate)**：`3.93%`
  *   **平均毛利率 (Profit Margin)**：`53.97%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
  *   **市场路径(中文)**：`玩具 › 体育 › 游泳池 › 水枪`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`151`
  *   **新品平均价格**：`$ 31.35`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`1,695`
  *   **新品月均销售额**：`$51,047`
  *   **平均重量**：`1.24 pounds (561 g)`
  *   **平均体积**：`259.12 in³ (4,246 cm³)`
  *   **平均毛利率**：`53.97%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`5.7‰`

---

#### 🏆 🟡-3. Drip Irrigation Kits (滴灌套件)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Watering Equipment › Automatic Irrigation Equipment › Drip Irrigation Kits  市场分析`
- **触发警示项**：`重量偏重 (>2.5 lbs), Reviews偏高 (>550)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.30`
  *   **平均 Reviews (Avg Reviews)**：`618 个`
  *   **物理重量 (Weight)**：`2.58 lbs`
  *   **平均退货率 (Return Rate)**：`3.37%`
  *   **平均毛利率 (Profit Margin)**：`61.61%`
  *   **品牌集中度 (Brand Concentration)**：`50.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Watering Equipment › Automatic Irrigation Equipment › Drip Irrigation Kits  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 浇灌工具 › 打药机 › 滴灌套件`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`125`
  *   **新品平均价格**：`$ 34.63`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`1,127`
  *   **新品月均销售额**：`$36,155`
  *   **平均重量**：`2.58 pounds (1,170 g)`
  *   **平均体积**：`341.29 in³ (5,593 cm³)`
  *   **平均毛利率**：`61.61%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`8.6‰`

---

#### 🏆 🟡-4. Bread Proofing Baskets (面包发酵篮)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets  市场分析`
- **触发警示项**：`Reviews偏高 (>550)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.00`
  *   **平均 Reviews (Avg Reviews)**：`570 个`
  *   **物理重量 (Weight)**：`2.03 lbs`
  *   **平均退货率 (Return Rate)**：`4.09%`
  *   **平均毛利率 (Profit Margin)**：`56.61%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 烘焙用具 › 烘焙工具 › 烘焙 › 面包发酵篮`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`92`
  *   **新品平均价格**：`$ 28.1`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`588`
  *   **新品月均销售额**：`$16,379`
  *   **平均重量**：`2.03 pounds (919 g)`
  *   **平均体积**：`393.57 in³ (6,449 cm³)`
  *   **平均毛利率**：`56.61%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟡-5. Ultrasonic Repellers (Ultrasonic Repellers)

- **完整市场路径**：`Health & Household › Household Supplies › Indoor Insect & Pest Control › Ultrasonic Repellers  市场分析`
- **触发警示项**：`Reviews偏高 (>550)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.76`
  *   **平均 Reviews (Avg Reviews)**：`625 个`
  *   **物理重量 (Weight)**：`0.61 lbs`
  *   **平均退货率 (Return Rate)**：`3.27%`
  *   **平均毛利率 (Profit Margin)**：`66.96%`
  *   **品牌集中度 (Brand Concentration)**：`70.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`7.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Household Supplies › Indoor Insect & Pest Control › Ultrasonic Repellers  市场分析`
  *   **市场路径(中文)**：`Health & Household › Household Supplies › Indoor Insect & Pest Control › Ultrasonic Repellers`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`103`
  *   **新品平均价格**：`$ 26.2`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`934`
  *   **新品月均销售额**：`$28,464`
  *   **平均重量**：`0.61 pounds (276 g)`
  *   **平均体积**：`56.83 in³ (931 cm³)`
  *   **平均毛利率**：`66.96%`
  *   **卖家所属地**：`美国|93.0%`
  *   **搜索购买比**：`7.8‰`

---

#### 🏆 🟡-6. Decorative Boxes (装饰盒)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
- **触发警示项**：`Reviews偏高 (>550)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.78`
  *   **平均 Reviews (Avg Reviews)**：`694 个`
  *   **物理重量 (Weight)**：`1.57 lbs`
  *   **平均退货率 (Return Rate)**：`7.91%`
  *   **平均毛利率 (Profit Margin)**：`57.46%`
  *   **品牌集中度 (Brand Concentration)**：`54.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰盒`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`66`
  *   **新品平均价格**：`$ 21.72`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`890`
  *   **新品月均销售额**：`$20,682`
  *   **平均重量**：`1.57 pounds (710 g)`
  *   **平均体积**：`325.95 in³ (5,341 cm³)`
  *   **平均毛利率**：`57.46%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`4.5‰`

---

#### 🏆 🟡-7. Pool & Deck Repair Products (油漆及密封产品)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products  市场分析`
- **触发警示项**：`Reviews偏高 (>550)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.79`
  *   **平均 Reviews (Avg Reviews)**：`682 个`
  *   **物理重量 (Weight)**：`2.28 lbs`
  *   **平均退货率 (Return Rate)**：`1.93%`
  *   **平均毛利率 (Profit Margin)**：`58.44%`
  *   **品牌集中度 (Brand Concentration)**：`57.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 油漆及密封产品`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`62`
  *   **新品平均价格**：`$ 19.47`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`688`
  *   **新品月均销售额**：`$13,545`
  *   **平均重量**：`2.28 pounds (1,032 g)`
  *   **平均体积**：`643.59 in³ (10,547 cm³)`
  *   **平均毛利率**：`58.44%`
  *   **卖家所属地**：`美国|52.0%`
  *   **搜索购买比**：`23.2‰`

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
| 6 | [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP) |  | Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically… | 805 / 11.11% | $32,192 | $39.99 | $5.91 (15%) | 110 / 12 | 4.7 | $4.09 / 75% | 4 | 18 | 1 | 0.26 pounds | 2025-01-25 1年 4个月 |
| 7 | [B0D37GG2SJ](https://www.amazon.com/dp/B0D37GG2SJ) |  | Golf Netting | 678 / 6.91% | $30,476 | $44.95 | $6.83 (15%) | 137 / 10 | 4.4 | $7.55 / 68% | 3 | 6 | 1 | 2.25 pounds | 2024-06-08 2年 |
| 8 | [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT) |  | 75FT Wakeboard Rope and Handle | 784 / 54.21% | $29,784 | $37.99 | $5.64 (15%) | 129 / 9 | 4.8 | $8.04 / 64% | 5 | 4 | 1 | 2.58 pounds | 2025-03-22 1年 2个月 |
| 9 | [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL) |  | Sea to Summit eVac Dry Bag | 574 / 93.82% | $28,671 | $49.95 | $7.40 (15%) | 8 / 4 | 4.8 | $4.09 / 77% | 1 | 390 | 1 | 0.4 pounds | 2025-01-13 1年 5个月 |
| 10 | [B0GKG8PKTX](https://www.amazon.com/dp/B0GKG8PKTX) |  | Ultralight Camping Chair Backpacking Chair | 813 / 22.35% | $27,634 | $33.99 | $4.95 (15%) | 90 / 8 | 4.6 | $7.63 / 63% | 5 | 134 | 2 | 4.17 pounds | 2026-02-12 4个月 |
| 11 | [B0FZJSDVF8](https://www.amazon.com/dp/B0FZJSDVF8) |  | 4 Pack Granny Pants Yard Game,Family Party Outdoor Granny Pants G… | **** / **** | **** | $39.99 | - | 47 / 6 | 4.0 | **** /  | 3 | 22 | 1 | 3.35 pounds | 2025-12-02 6个月 |
| 12 | [B0F98Y7S35](https://www.amazon.com/dp/B0F98Y7S35) |  | DURATECH 12V Cordless Electric Fillet Knife with 8" & 10" Razor-S… | **** / **** | **** | $59.99 | - | 115 / 12 | 4.5 | **** /  | 1 | 19 | 1 | 3.53 pounds | 2025-09-13 9个月 |
| 13 | [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8) |  | Pool Paddle Water Aerobics Equipment | **** / **** | **** | $41.97 | - | 86 / 16 | 4.5 | **** /  | 1 | 23 | 1 | 1.3 pounds | 2025-09-30 8个月 |
| 14 | [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP) |  | WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag… | **** / **** | **** | $35.99 | - | 127 / 35 | 4.6 | **** /  | 3 | 61 | 1 | 0.82 pounds | 2026-02-20 3个月 |
| 15 | [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR) |  | Detachable Clip in Bimini Top Mesh Sidewalls | **** / **** | **** | $59.99 | - | 57 / 6 | 4.6 | **** /  | 2 | 9 | 1 | 2.73 pounds | 2025-06-24 11个月 |
| 16 | [B0F62YLXK6](https://www.amazon.com/dp/B0F62YLXK6) |  | Air Horn 8.3oz for Boating | **** / **** | **** | $27.99 | - | 66 / - | 4.6 | **** /  | 1 | 8 | 1 | 0.93 pounds | 2025-05-21 1年 |
| 17 | [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3) |  | Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Visio… | **** / **** | **** | $59.99 | - | 41 / 12 | 4.5 | **** /  | 1 | 15 | 2 | 1.54 pounds | 2026-02-08 4个月 |
| 18 | [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD) |  | Wakesurf Rope and Handle | **** / **** | **** | $47.99 | - | 88 / 5 | 4.8 | **** /  | 4 | 1 | 1 | 2.16 pounds | 2024-03-14 2年 3个月 |
| 19 | [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D) |  | Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit | **** / **** | **** | $34.95 | - | 67 / 20 | 4.8 | **** /  | 2 | 15 | 1 | 0.82 pounds | 2025-11-25 6个月 |
| 20 | [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD) |  | SUNNYLiFE Swim Vest | **** / **** | **** | $49.00 | - | 5 / 2 | 4.5 | **** /  | 1 | 75 | 2 | 0.53 pounds | 2026-01-29 4个月 |

## 二、完整商品标题

**1. [B0F5BD54RT](https://www.amazon.com/dp/B0F5BD54RT)** Suspension Straps Trainer with Built-in Door Anchor, All-in-One Bodyweight Training System for Home & Outdoor Use - Quick Setup in 1 Second

**2. [B0G1MSTY15](https://www.amazon.com/dp/B0G1MSTY15)** Calamus GearMaster Fishing Sling Tackle Bag & Tool Set, 3500 Tackle Box & Fishing Gear with Fishing lures, Fishing Pliers, Fishing Scissors, Lip Gripper, Wacky Tool

**3. [B0FGHZXNGV](https://www.amazon.com/dp/B0FGHZXNGV)** BougeRV Upgraded Telescopic Camping Light, 15600mAh Rotatable Electric Lantern, Collapsible Outdoor Light, Cordless Flashlight, Waterproof, Tent Lamp for Camping, Emergency, Hiking, Outdoor

**4. [B0GKMGJLL3](https://www.amazon.com/dp/B0GKMGJLL3)** Boat Stern Light Anchor Light, 28"-48" Telescoping Pole Boat Lights LED with Base & Extra Bulb, Waterproof 3NM 360° All Round Marine Navigation Lights for Boats LED for Pontoon, Fishing, Bass Boats

**5. [B0DX2F3V5Q](https://www.amazon.com/dp/B0DX2F3V5Q)** SILCA Ultimate Sealant Bottle | injectable Fiber Foam

**6. [B0DTP76XQP](https://www.amazon.com/dp/B0DTP76XQP)** Human Fish Hook Removal Tool. The Only Ambidextrous Ergonomically Designed Human Fish Hook Removal Tool.

**7. [B0D37GG2SJ](https://www.amazon.com/dp/B0D37GG2SJ)** Golf Netting, 10ft, 15ft, 20ft Sports Netting - Heavy Duty High Impact Multi-Sport Practice Net for Golf, Baseball, Soccer, Hockey, Lacrosse, Backyard Driving & Training Barrier

**8. [B0DS2CBVFT](https://www.amazon.com/dp/B0DS2CBVFT)** 75FT Wakeboard Rope and Handle, Floating Water Ski Rope for Watersports, 4 Sections Ski Ropes for Water Skiing, Kneeboarding, Wakeboarding

**9. [B0DSRDB4YL](https://www.amazon.com/dp/B0DSRDB4YL)** Sea to Summit eVac Dry Bag, Roll-Top Compression Sack, 35 Liter, Turkish Tile Blue

**10. [B0GKG8PKTX](https://www.amazon.com/dp/B0GKG8PKTX)** Ultralight Camping Chair Backpacking Chair, Portable Camp Chair with Cup Holder & Storage Bag, Lightweight Compact Folding Chair for Hiking, Travel, Picnic Mountaineering（Deep Black）

**11. [B0FZJSDVF8](https://www.amazon.com/dp/B0FZJSDVF8)** 4 Pack Granny Pants Yard Game,Family Party Outdoor Granny Pants Game with 20pcs Bouncy Balls for The Family Gathering,The Family Reunion Ultimate Backyard Party Games

**12. [B0F98Y7S35](https://www.amazon.com/dp/B0F98Y7S35)** DURATECH 12V Cordless Electric Fillet Knife with 8" & 10" Razor-Sharp Blades, Electric Fish Fillet Knife with 2.0Ah Built-in Battery, Type-C Charge, Non-Slip Handle, Storage Case for Fishing Filleting

**13. [B0F9ZZ17Z8](https://www.amazon.com/dp/B0F9ZZ17Z8)** Pool Paddle Water Aerobics Equipment | Adjustable Resistance Pool Exercise Equipment for Adults, Swim Paddles Water Weights Dumbbells for Aquatic Exercise, Aqua Weights for Men & Women Workout Gear

**14. [B0GL785GSP](https://www.amazon.com/dp/B0GL785GSP)** WATERFLY Small Crossbody Sling Bag: RFID Sling Backpack Chest Bag Travel Shoulder Multiple Pockets Hiking Daypack for Man Woman

**15. [B0F6KRVBGR](https://www.amazon.com/dp/B0F6KRVBGR)** Detachable Clip in Bimini Top Mesh Sidewalls, Boat Sun Shade Universal Fit for 4 Bow Bimini Tops, with Straps Clips (Bimini Tops Not Included)

**16. [B0F62YLXK6](https://www.amazon.com/dp/B0F62YLXK6)** Air Horn 8.3oz for Boating, 120 dB Marine Boat Horn, Loud Airhorn for Sports Events, Outdoor & Marine Use

**17. [B0GLQ8T4P3](https://www.amazon.com/dp/B0GLQ8T4P3)** Punvoe Trail Camera 64MP 4K HD Game Camera with 100ft Night Vision 0.1s Trigger Time Motion Activated 130° Wide Angle Ip67 Waterproof WiFi Hunting Camera with 64GB SD Card for Wildlife Monitoring

**18. [B0CT5MVCFD](https://www.amazon.com/dp/B0CT5MVCFD)** Wakesurf Rope and Handle, 25ft Floating Wake Surf Ropes, Surf Tow Rope for Wakesurfing and Watersports

**19. [B0FNNCDS7D](https://www.amazon.com/dp/B0FNNCDS7D)** Upgraded Rechargeable Bore Sight Laser with 32 Adapter Kit, Professional Green/Red Laser Bore Sight Fits .17 to 12GA Calibers

**20. [B0G51VX3YD](https://www.amazon.com/dp/B0G51VX3YD)** SUNNYLiFE Swim Vest, 1-2 Years, Into The Garden Ditsy Floral, EPE/Natural Rubber/Polyester, 13.39x12.6x1.77 Inches, 1.27 lbs

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
- `B0DTP76XQP`: 10,123 | 218 | 2% | 805 | 11.11% | $32,192 | 200+ | $7K+ | 4 | $39.99 | - | 110 | 12 | 4.7 | 1.49% | $4.09 | 75% | 2025-01-25 | 1年 4个月 | FBA | -
- `B0D37GG2SJ`: 11,819 | 2,260 | 16% | 678 | 6.91% | $30,476 | 200+ | $8K+ | 3 | $44.95 | - | 137 | 10 | 4.4 | 1.47% | $7.55 | 68% | 2024-06-08 | 2年 | FBA | -
- `B0DS2CBVFT`: 7,728 | 1,832 | 19% | 784 | 54.21% | $29,784 | 300+ | $11K+ | 5 | $37.99 | - | 129 | 9 | 4.8 | 1.15% | $8.04 | 64% | 2025-03-22 | 1年 2个月 | FBA | -
- `B0DSRDB4YL`: 210,040 | 7,666 | 35% | 574 | 93.82% | $28,671 | - | - | 1 | $49.95 | - | 8 | 4 | 4.8 | 0.7% | $4.09 | 77% | 2025-01-13 | 1年 5个月 | FBA | -
- `B0GKG8PKTX`: 9,431 | 511 | 5% | 813 | 22.35% | $27,634 | 300+ | $10K+ | 5 | $33.99 | - | 90 | 8 | 4.6 | 0.98% | $7.63 | 63% | 2026-02-12 | 4个月 | FBA | -
- `B0FZJSDVF8`: 9,043 | 7,937 | 47% | **** | **** | **** | **** | 3 | $39.99 | - | 47 | 6 | 4.0 | 0.88% | **** | 2025-12-02 | 6个月 | FBA | -
- `B0F98Y7S35`: 20,723 | 3,756 | 15% | **** | **** | **** | **** | 1 | $59.99 | - | 115 | 12 | 4.5 | 2.66% | **** | 2025-09-13 | 9个月 | FBA | -
- `B0F9ZZ17Z8`: 13,826 | 38 | 0% | **** | **** | **** | **** | 1 | $41.97 | - | 86 | 16 | 4.5 | 2.52% | **** | 2025-09-30 | 8个月 | FBA | -
- `B0GL785GSP`: 12,238 | 20 | 0% | **** | **** | **** | **** | 3 | $35.99 | - | 127 | 35 | 4.6 | 4.78% | **** | 2026-02-20 | 3个月 | FBA | -
- `B0F6KRVBGR`: 17,233 | 2,507 | 13% | **** | **** | **** | **** | 2 | $59.99 | - | 57 | 6 | 4.6 | 1.37% | **** | 2025-06-24 | 11个月 | FBA | -
- `B0F62YLXK6`: 9,609 | 0 | 0% | **** | **** | **** | **** | 1 | $27.99 | - | 66 | - | 4.6 | - | **** | 2025-05-21 | 1年 | FBA | -
- `B0GLQ8T4P3`: 12,940 | 10,879 | 46% | **** | **** | **** | **** | 1 | $59.99 | - | 41 | 12 | 4.5 | 2.84% | **** | 2026-02-08 | 4个月 | FBA | -
- `B0CT5MVCFD`: 17,365 | 1,868 | 10% | **** | **** | **** | **** | 4 | $47.99 | - | 88 | 5 | 4.8 | 0.95% | **** | 2024-03-14 | 2年 3个月 | FBA | -
- `B0FNNCDS7D`: 10,619 | 2,566 | 19% | **** | **** | **** | **** | 2 | $34.95 | - | 67 | 20 | 4.8 | 2.79% | **** | 2025-11-25 | 6个月 | FBA | -
- `B0G51VX3YD`: 9,887 | 6,681 | 40% | **** | **** | **** | **** | 1 | $49.00 | - | 5 | 2 | 4.5 | 0.4% | **** | 2026-01-29 | 4个月 | FBA | -

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
| 5 | [B0G6Z1QM2M](https://www.amazon.com/dp/B0G6Z1QM2M) |  | Floating Pool Lights Solar Powered | 448 / 50.41% | $17,405 | $38.85 | $5.66 (15%) | 56 / 19 | 4.6 | $5.61 / 71% | 2 | 98 | 1 | 1.37 pounds | 2026-02-07 4个月 |
| 6 | [B0DSHT56KC](https://www.amazon.com/dp/B0DSHT56KC) |  | 500W R40 120V Pool Light Bulb for Inground Pool & Spa | 287 / 22.34% | $17,217 | $59.99 | $9.03 (15%) | 21 / - | 4.7 | $7.17 / 73% | 2 | 153 | 2 | 0.71 pounds | 2025-03-02 1年 3个月 |
| 7 | [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF) |  | Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool… | 423 / 148.32% | $16,916 | $39.99 | $6.05 (15%) | 31 / 7 | 4.4 | $4.35 / 74% | 2 | 88 | 1 | 0.44 pounds | 2025-05-07 1年 1个月 |
| 8 | [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H) |  | SIEDiNLAR Solar Floating Pool Lights with Remote | 358 / 145.11% | $12,884 | $35.99 | $5.29 (15%) | 36 / 11 | 4.0 | $5.87 / 69% | 2 | 135 | 1 | 1.57 pounds | 2026-04-05 2个月 |
| 9 | [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC) |  | Floating Pool Lights | 379 / 146.4% | $11,359 | $29.97 | $4.43 (15%) | 30 / - | 4.9 | $5.76 / 66% | 2 | 99 | 1 | 1.53 pounds | 2026-04-21 1个月 |
| 10 | [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB) |  | 55ft Solar Pool Lights for Above Ground Pools | 538 / 183.92% | $11,293 | $20.99 | $3.10 (15%) | 117 / 9 | 4.0 | $4.46 / 64% | 4 | 77 | 1 | 0.73 pounds | 2025-02-28 1年 3个月 |
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

**5. [B0G6Z1QM2M](https://www.amazon.com/dp/B0G6Z1QM2M)** Floating Pool Lights Solar Powered, 16'' Inflatable Waterproof Clownfish Solar Pool Lights that Float, Auto On/Off LED Floating Lights for Pool Garden Backyard Outdoor Decoration - (2 Piece)

**6. [B0DSHT56KC](https://www.amazon.com/dp/B0DSHT56KC)** 500W R40 120V Pool Light Bulb for Inground Pool & Spa – 3000K Warm White, E26 Base, High-Power, Compatible with Pentair & Hayward Fixtures, 3,000-Hour Lifespan (2 Pack)

**7. [B0DXVSDMZF](https://www.amazon.com/dp/B0DXVSDMZF)** Bright Led Pool Light Bulb,120V 65W with 6000LM E27/E26 Base Pool Light Bulb Daylight White 6000K Swimming Pool Replacement for Most Pentair Hayward Light Fixtures (120V 65W)

**8. [B0GPW9YT5H](https://www.amazon.com/dp/B0GPW9YT5H)** SIEDiNLAR Solar Floating Pool Lights with Remote, 12 Modes RGB Color Changing Solar Powered Pool Lights, Waterproof Floating Lights for Swimming Pool, Pond, Fountain, Backyard & Party Decor (4 Pack)

**9. [B0GRTPX9DC](https://www.amazon.com/dp/B0GRTPX9DC)** Floating Pool Lights, 15" Inflatable Solar Powered Pool Lights That Float, Color Changing LED Glow Balls, IP68 Waterproof Solar Floating Light Up Balls for Pool,Pond, Outdoor Party Decor - 2PCS

**10. [B0DWMMYNDB](https://www.amazon.com/dp/B0DWMMYNDB)** 55ft Solar Pool Lights for Above Ground Pools, 150 LEDs Remote IP65 Waterproof Rope Lights, 8 Color Modes, Swimming Frame Pool Decor Accessories for Outdoor Outside Trampoline Camping

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
- `B0G6Z1QM2M`: 20,833 | 845 | 4% | 448 | 50.41% | $17,405 | 300+ | $9K+ | 2 | $38.85 | - | 56 | 19 | 4.6 | 4.24% | $5.61 | 71% | 2026-02-07 | 4个月 | FBA | -
- `B0DSHT56KC`: 33,045 | 7,232 | 18% | 287 | 22.34% | $17,217 | 200+ | $11K+ | 2 | $59.99 | - | 21 | - | 4.7 | - | $7.17 | 73% | 2025-03-02 | 1年 3个月 | FBA | -
- `B0DXVSDMZF`: 21,990 | 2,628 | 11% | 423 | 148.32% | $16,916 | 200+ | $7K+ | 2 | $39.99 | - | 31 | 7 | 4.4 | 1.65% | $4.35 | 74% | 2025-05-07 | 1年 1个月 | FBA | -
- `B0GPW9YT5H`: 28,375 | 1,218 | 4% | 358 | 145.11% | $12,884 | 200+ | $7K+ | 2 | $35.99 | - | 36 | 11 | 4.0 | 3.07% | $5.87 | 69% | 2026-04-05 | 2个月 | FBA | -
- `B0GRTPX9DC`: 20,656 | 14,256 | 41% | 379 | 146.4% | $11,359 | 200+ | $5K+ | 2 | $29.97 | - | 30 | - | 4.9 | - | $5.76 | 66% | 2026-04-21 | 1个月 | FBA | -
- `B0DWMMYNDB`: 18,386 | 2,081 | 10% | 538 | 183.92% | $11,293 | 200+ | $3K+ | 4 | $20.99 | - | 117 | 9 | 4.0 | 1.67% | $4.46 | 64% | 2025-02-28 | 1年 3个月 | FBA | -
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

# Nicotine Patches 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Health & Household › Health Care › Smoking Cessation › Nicotine Patches`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟢 Green (Recommended)　均价 $22.22　均Reviews 468（中等）　重量 0.13lbs（轻）　退货率 1.27%（低）　品牌集中度 73.4%（垄断）　中国卖家 49.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0G839C2C2](https://www.amazon.com/dp/B0G839C2C2) |  | 120 Count | 476 / 8.75% | $10,943 | $22.99 | $3.46 (15%) | 30 / 11 | 4.7 | $3.44 / 70% | 1 | 32 | 1 | 0.09 pounds | 2026-01-07 5个月 |
| 2 | [B0DKP86SX6](https://www.amazon.com/dp/B0DKP86SX6) |  | Recovery Patches 60 Pack | 278 / 14.29% | $6,113 | $21.99 | $3.28 (15%) | 35 / - | 4.2 | $3.54 / 69% | 1 | 72 | 1 | 0.19 pounds | 2024-11-17 1年 6个月 |

## 二、完整商品标题

**1. [B0G839C2C2](https://www.amazon.com/dp/B0G839C2C2)** 120 Count - Nicotine Patches 3mg (Applicable to Step 1/Step 2/Step 3), Transdermal Stop Smoking Aid for Craving Relief, Flexible Dosing with Fast-Acting Nicotine Replacement Therapy

**2. [B0DKP86SX6](https://www.amazon.com/dp/B0DKP86SX6)** Recovery Patches 60 Pack - Wake Up Refreshed & Energized with Our 100% Natural Ingredients Recovery Stickers - Skin-Friendly & Waterproof - Apply Before Drinking - Enhanced Morning Formula

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0G839C2C2`: 42,499 | 5,570 | 12% | 476 | 8.75% | $10,943 | 400+ | $9K+ | 1 | $22.99 | - | 30 | 11 | 4.7 | 2.31% | $3.44 | 70% | 2026-01-07 | 5个月 | FBA | -
- `B0DKP86SX6`: 71,157 | 0 | 0% | 278 | 14.29% | $6,113 | 100+ | $2K+ | 1 | $21.99 | - | 35 | - | 4.2 | - | $3.54 | 69% | 2024-11-17 | 1年 6个月 | FBA | -

---

# Water Balloons 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Water Balloons`
> 共抓取 **5** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **5** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $21.35　均Reviews 694（中等）　重量 0.82lbs（轻）　退货率 1.83%（低）　品牌集中度 74.4%（垄断）　中国卖家 78.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GKFSMPTP](https://www.amazon.com/dp/B0GKFSMPTP) |  | 25Pcs Reusable Water Balloons with 2pcs Bow and Arrow for Kids | 713 / 106.72% | $20,527 | $28.79 | $4.29 (15%) | 43 / 18 | 4.0 | $7.23 / 60% | 3 | 32 | 1 | 1.41 pounds | 2026-03-10 3个月 |
| 2 | [B0DZML5ZPH](https://www.amazon.com/dp/B0DZML5ZPH) |  | 24PCS Reusable Water Balloons | 722 / 142.97% | $20,209 | $27.99 | $4.28 (15%) | 133 / 6 | 4.3 | $5.52 / 65% | 2 | 29 | 1 | 1.46 pounds | 2025-05-12 1年 1个月 |
| 3 | [B0GD11KHJB](https://www.amazon.com/dp/B0GD11KHJB) |  | 133 PCS Granny Pants Yard Game 2 Pack with 16 Balls Field Day Out… | 465 / 34.16% | $13,480 | $28.99 | $4.25 (15%) | 37 / 6 | 4.4 | $6.48 / 63% | 2 | 76 | 1 | 2.71 pounds | 2026-03-02 3个月 |
| 4 | [B0GC43CR19](https://www.amazon.com/dp/B0GC43CR19) |  | 15Pcs Reusable Water Balloons for Kids & Family Outdoor Play | 191 / 35.29% | $6,683 | $34.99 | $5.24 (15%) | 3 / - | 5.0 | $5.61 / 69% | 2 | 44 | 1 | 1.39 pounds | 2026-02-02 4个月 |
| 5 | [B0DZFGJQ5N](https://www.amazon.com/dp/B0DZFGJQ5N) |  | Zuru 16 ft Water Slide Wipeout and 100 Balloons Set | 108 / 118.18% | $3,563 | $32.99 | $4.99 (15%) | 3 / - | 5.0 | $7.55 / 62% | 1 | 179 | 1 | 3.97 pounds | 2025-03-07 1年 3个月 |

## 二、完整商品标题

**1. [B0GKFSMPTP](https://www.amazon.com/dp/B0GKFSMPTP)** 25Pcs Reusable Water Balloons with 2pcs Bow and Arrow for Kids, Pool Beach Water Fight Equipment for Boys and Girls, Outdoor Summer Toys for Kids Ages 3-12

**2. [B0DZML5ZPH](https://www.amazon.com/dp/B0DZML5ZPH)** 24PCS Reusable Water Balloons, Self-Sealing Silicone Water Bomb, Refillable Water Balls for Boys and Girls, Outdoor Summer Water Toys Pool Beach Park Yard

**3. [B0GD11KHJB](https://www.amazon.com/dp/B0GD11KHJB)** 133 PCS Granny Pants Yard Game 2 Pack with 16 Balls Field Day Outdoor Giant Pants Games for Adults Kids Family Large Outside Lawn Backyard Carnival Picnic Camping Birthday Party Big Pants Tossing Game

**4. [B0GC43CR19](https://www.amazon.com/dp/B0GC43CR19)** 15Pcs Reusable Water Balloons for Kids & Family Outdoor Play – Quick Fill, Soft Silicone, Easy to Collect, No Magnets, Perfect for Yard, Pool Beach Games, Summer Water Toys

**5. [B0DZFGJQ5N](https://www.amazon.com/dp/B0DZFGJQ5N)** Zuru 16 ft Water Slide Wipeout and 100 Balloons Set - Bundle with 2 Lane Water Slide Wipeout Plus 5 Bunches of Rapid-Filling Self-Sealing Water Balloons for Kids, Boys, Girls | Summer Outdoor Playset

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GKFSMPTP`: 6,375 | 3,584 | 39% | 713 | 106.72% | $20,527 | 300+ | $9K+ | 3 | $28.79 | - | 43 | 18 | 4.0 | 2.52% | $7.23 | 60% | 2026-03-10 | 3个月 | FBA | -
- `B0DZML5ZPH`: 5,326 | 635 | 11% | 722 | 142.97% | $20,209 | 700+ | $18K+ | 2 | $27.99 | - | 133 | 6 | 4.3 | 0.83% | $5.52 | 65% | 2025-05-12 | 1年 1个月 | FBA | -
- `B0GD11KHJB`: 22,675 | 1,209 | 7% | 465 | 34.16% | $13,480 | 200+ | $5K+ | 2 | $28.99 | - | 37 | 6 | 4.4 | 1.29% | $6.48 | 63% | 2026-03-02 | 3个月 | FBA | -
- `B0GC43CR19`: 9,479 | 72,160 | 88% | 191 | 35.29% | $6,683 | 100+ | $3K+ | 2 | $34.99 | - | 3 | - | 5.0 | - | $5.61 | 69% | 2026-02-02 | 4个月 | FBA | -
- `B0DZFGJQ5N`: 106,855 | 0 | 0% | 108 | 118.18% | $3,563 | 100+ | $2K+ | 1 | $32.99 | - | 3 | - | 5.0 | - | $7.55 | 62% | 2025-03-07 | 1年 3个月 | FBA | -

---

# Squirt Guns 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns`
> 共抓取 **11** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **11** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $25.91　均Reviews 619（中等）　重量 1.24lbs（轻）　退货率 3.93%（低）　品牌集中度 53.8%（中等）　中国卖家 68.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GQ2BQQDS](https://www.amazon.com/dp/B0GQ2BQQDS) |  | 2 Pack Electric Water Gun for Adults Kids USB-C Charging Port | 952 / 182.54% | $47,590 | $49.99 | $7.43 (15%) | 33 / 1 | 4.2 | $7.57 / 70% | 1 | 260 | 1 | 3.17 pounds | 2026-04-21 1个月 |
| 2 | [B0GH71NJPF](https://www.amazon.com/dp/B0GH71NJPF) |  | 2 Pack Large Electric Water Guns for Adults & Kids | 741 / 9.64% | $40,007 | $53.99 | $8.15 (15%) | 31 / 17 | 4.4 | $8.59 / 69% | 1 | 85 | 1 | 3.26 pounds | 2026-02-28 3个月 |
| 3 | [B0BKVHW3CZ](https://www.amazon.com/dp/B0BKVHW3CZ) |  | Quanquer 8 Pack 600cc Water Guns for Kids & Adults | 998 / 45.99% | $39,910 | $39.99 | $5.93 (15%) | 107 / 16 | 4.6 | $8.87 / 63% | 2 | 91 | 1 | 3.79 pounds | 2025-12-04 6个月 |
| 4 | [B0H13XKQ27](https://www.amazon.com/dp/B0H13XKQ27) |  | Electric Water Gun for Adults & Kids | 643 / 100% | $32,144 | $49.99 | $7.49 (15%) | 20 / 14 | 4.6 | $7.01 / 71% | 2 | 52 | 1 | 1.41 pounds | 2026-05-12 1个月 |
| 5 | [B0BPH8P5D9](https://www.amazon.com/dp/B0BPH8P5D9) |  | Threan 100 Pack Water Gun for Kids Mini Water Gun Toy Colors Plas… | 572 / 131.58% | $21,158 | $36.99 | $5.48 (15%) | 53 / 2 | 4.1 | $8.21 / 63% | 2 | 121 | 1 | 2.95 pounds | 2023-01-28 3年 4个月 |
| 6 | [B0GJSTS72K](https://www.amazon.com/dp/B0GJSTS72K) |  | Electric Water Gun for Adults Kids | 723 / 44.73% | $16,911 | $23.39 | $3.46 (15%) | 44 / 12 | 4.1 | $6.13 / 59% | 2 | 55 | 1 | 1.21 pounds | 2026-03-14 3个月 |
| 7 | [B0DRVGDYGK](https://www.amazon.com/dp/B0DRVGDYGK) |  | Water Gun for Kids | 429 / 7.38% | $12,008 | $27.99 | $4.16 (15%) | 43 / 7 | 4.7 | $7.32 / 59% | 2 | 136 | 1 | 2.45 pounds | 2025-09-24 8个月 |
| 8 | [B0GDG4T6L8](https://www.amazon.com/dp/B0GDG4T6L8) |  | Electric Water Gun | 414 / 102.2% | $10,222 | $24.69 | $3.75 (15%) | 45 / 17 | 4.4 | $6.13 / 60% | 3 | 204 | 1 | 0.9 pounds | 2026-01-29 4个月 |
| 9 | [B0DRY4N6MG](https://www.amazon.com/dp/B0DRY4N6MG) |  | Electric Gel Ball Blaster | 181 / 77.05% | $7,238 | $39.99 | $6.19 (15%) | 117 / 2 | 4.1 | $7.41 / 66% | 1 | 369 | 1 | 3.2 pounds | 2025-01-07 1年 5个月 |
| 10 | [B0F3NVTP3J](https://www.amazon.com/dp/B0F3NVTP3J) |  | 9 Pack Water Guns Pool Toys Summer Lake Pool Deals Game Blaster O… | 159 / 140% | $4,132 | $25.99 | $3.81 (15%) | 17 / 1 | 5.0 | $7.63 / 56% | 1 | 292 | 1 | 1.61 pounds | 2025-05-21 1年 |
| 11 | [B09TZVCD7R](https://www.amazon.com/dp/B09TZVCD7R) |  | 24 Packs 4 Inch Fire Extinguisher Toys Fire Extinguisher Mini Wat… | **** / **** | **** | $26.99 | - | 139 / - | 4.3 | **** /  | 1 | 376 | 1 | 1.27 pounds | 2022-03-20 4年 2个月 |

## 二、完整商品标题

**1. [B0GQ2BQQDS](https://www.amazon.com/dp/B0GQ2BQQDS)** 2 Pack Electric Water Gun for Adults Kids USB-C Charging Port, Automatic High Powered Squirt Gun,Powerful Shooting Long Range Auto Water Blaster, Outdoor Water Toy Pool Game (Blue+Red)

**2. [B0GH71NJPF](https://www.amazon.com/dp/B0GH71NJPF)** 2 Pack Large Electric Water Guns for Adults & Kids, Automatic Squirt Guns with LED Light, 730CC High Capacity Water Gun with 26-33FT Long Range & Battery Powered for Summer Outdoor Beach Pool Toy Gift

**3. [B0BKVHW3CZ](https://www.amazon.com/dp/B0BKVHW3CZ)** Quanquer 8 Pack 600cc Water Guns for Kids & Adults, Large Capacity Pump Action Super Squirt Blasters Soaker with Long Range up to 32 FT, Summer Outdoor Pool Beach Water Toys for Boys Girls

**4. [B0H13XKQ27](https://www.amazon.com/dp/B0H13XKQ27)** Electric Water Gun for Adults & Kids, Voice Control Automatic Water Guns, 26-30 FT Long Range Gatling Watergun with LED Lights, Squirt Water Guns Summer Outdoor Pool Toys for Boys Girls Ages 8-12+

**5. [B0BPH8P5D9](https://www.amazon.com/dp/B0BPH8P5D9)** Threan 100 Pack Water Gun for Kids Mini Water Gun Toy Colors Plastic Squirt Pistol Small Fun for Adults Teens Summer Pool Beach Party Favor Outdoor Game Bath Birthday(Cool)

**6. [B0GJSTS72K](https://www.amazon.com/dp/B0GJSTS72K)** Electric Water Gun for Adults Kids, High-Capacity Automatic Squirt Gun with LED Lights, 32FT Long Range Transparent Water Blaster, Summer Outdoor Pool & Beach Party Toys for Boys Girls(Blue)

**7. [B0DRVGDYGK](https://www.amazon.com/dp/B0DRVGDYGK)** Water Gun for Kids, 18Pcs Super Water Blaster, Long Range Squirt Guns for Pool Beach Summer Outdoor Party, Easy Pump Action Water Toys for Boys Girls Adults

**8. [B0GDG4T6L8](https://www.amazon.com/dp/B0GDG4T6L8)** Electric Water Gun, Squirt Blaster Automatic Toy for Kids & Adults, 350cc Large Capacity, 25-32ft Long Range, Rechargeable Battery, Auto-Sync LED Lights, Summer Outdoor Toy for Pool, Beach & Backyard

**9. [B0DRY4N6MG](https://www.amazon.com/dp/B0DRY4N6MG)** Electric Gel Ball Blaster, High Speed Automatic Splatter Ball Blaster with 80000+ and Goggles, Rechargeable Splatter Ball Toys for Outdoor Activities Shooting Game Party Favors-2 Pcs

**10. [B0F3NVTP3J](https://www.amazon.com/dp/B0F3NVTP3J)** 9 Pack Water Guns Pool Toys Summer Lake Pool Deals Game Blaster Outdoor Water Shooters Swimming Play Activities for Kids Teens Adults (9 Dinosaurs)

**11. [B09TZVCD7R](https://www.amazon.com/dp/B09TZVCD7R)** 24 Packs 4 Inch Fire Extinguisher Toys Fire Extinguisher Mini Water Firemen Squirter for Party Favors

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GQ2BQQDS`: 29,511 | 2,551 | 8% | 952 | 182.54% | $47,590 | 300+ | $15K+ | 1 | $49.99 | - | 33 | 1 | 4.2 | 0.11% | $7.57 | 70% | 2026-04-21 | 1个月 | FBA | -
- `B0GH71NJPF`: 6,760 | 3,870 | 36% | 741 | 9.64% | $40,007 | 700+ | $45K+ | 1 | $53.99 | - | 31 | 17 | 4.4 | 2.29% | $8.59 | 69% | 2026-02-28 | 3个月 | FBA | -
- `B0BKVHW3CZ`: 7,783 | 581 | 7% | 998 | 45.99% | $39,910 | 900+ | $37K+ | 2 | $39.99 | - | 107 | 16 | 4.6 | 1.6% | $8.87 | 63% | 2025-12-04 | 6个月 | FBA | -
- `B0H13XKQ27`: 5,249 | 4,182 | 44% | 643 | 100% | $32,144 | 400+ | $16K+ | 2 | $49.99 | - | 20 | 14 | 4.6 | 2.18% | $7.01 | 71% | 2026-05-12 | 1个月 | FBA | -
- `B0BPH8P5D9`: 10,559 | 1,296 | 11% | 572 | 131.58% | $21,158 | 400+ | $14K+ | 2 | $36.99 | - | 53 | 2 | 4.1 | 0.35% | $8.21 | 63% | 2023-01-28 | 3年 4个月 | FBA | -
- `B0GJSTS72K`: 4,446 | 108 | 2% | 723 | 44.73% | $16,911 | 500+ | $12K+ | 2 | $23.39 | - | 44 | 12 | 4.1 | 1.66% | $6.13 | 59% | 2026-03-14 | 3个月 | FBA | -
- `B0DRVGDYGK`: 12,442 | 6,137 | 33% | 429 | 7.38% | $12,008 | 400+ | $10K+ | 2 | $27.99 | - | 43 | 7 | 4.7 | 1.63% | $7.32 | 59% | 2025-09-24 | 8个月 | FBA | -
- `B0GDG4T6L8`: 22,452 | 1,245 | 5% | 414 | 102.2% | $10,222 | 200+ | $5K+ | 3 | $24.69 | - | 45 | 17 | 4.4 | 4.11% | $6.13 | 60% | 2026-01-29 | 4个月 | FBA | -
- `B0DRY4N6MG`: 55,921 | 24,444 | 30% | 181 | 77.05% | $7,238 | 100+ | $3K+ | 1 | $39.99 | - | 117 | 2 | 4.1 | 1.1% | $7.41 | 66% | 2025-01-07 | 1年 5个月 | FBA | -
- `B0F3NVTP3J`: 39,782 | 11,911 | 23% | 159 | 140% | $4,132 | 100+ | $2K+ | 1 | $25.99 | - | 17 | 1 | 5.0 | 0.63% | $7.63 | 56% | 2025-05-21 | 1年 | FBA | -
- `B09TZVCD7R`: 69,105 | 2,500 | 3% | **** | **** | **** | **** | 1 | $26.99 | - | 139 | - | 4.3 | - | **** | 2022-03-20 | 4年 2个月 | FBA | -

---

# Drip Irrigation Kits 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Watering Equipment › Automatic Irrigation Equipment › Drip Irrigation Kits`
> 共抓取 **13** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **13** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $33.30　均Reviews 618（中等）　重量 2.58lbs（重）　退货率 3.37%（低）　品牌集中度 50.8%（中等）　中国卖家 70.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GJZXWSK6](https://www.amazon.com/dp/B0GJZXWSK6) |  | Drip Irrigation System,106FT Automatic Garden Watering System wit… | 559 / 43.01% | $13,969 | $24.99 | $3.77 (15%) | 24 / - | 4.6 | $7.23 / 56% | 2 | 83 | 1 | 3.22 pounds | 2026-03-26 2个月 |
| 2 | [B0G1473Y3J](https://www.amazon.com/dp/B0G1473Y3J) |  | HIRALIY 50FT Quick-Connect Drip Irrigation Kit | 598 / 21.02% | $12,672 | $21.19 | $3.19 (15%) | 44 / 8 | 4.0 | $6.13 / 56% | 2 | 61 | 1 | 1.42 pounds | 2026-02-10 4个月 |
| 3 | [B0DY7X7M4V](https://www.amazon.com/dp/B0DY7X7M4V) |  | Drip Irrigation Kit Automatic Watering System with Water Timer 64… | 267 / 97.52% | $7,473 | $27.99 | $4.18 (15%) | 117 / 8 | 4.0 | $7.30 / 59% | 5 | 196 | 1 | 3.06 pounds | 2025-04-12 1年 2个月 |
| 4 | [B0G64FH1N1](https://www.amazon.com/dp/B0G64FH1N1) |  | [All-New 2027] Automatic Plant Waterer for Indoor | 209 / 146.38% | $7,313 | $34.99 | $5.24 (15%) | 21 / 7 | 4.5 | $5.61 / 69% | 1 | 131 | 1 | 1.36 pounds | 2026-02-12 4个月 |
| 5 | [B0FMXHDBHK](https://www.amazon.com/dp/B0FMXHDBHK) |  | RAINPOINT WiFi Smart Programmable Solar Drip Irrigation System fo… | 121 / 48.98% | $6,838 | $56.51 | $8.29 (15%) | 23 / 4 | 4.5 | $6.40 / 74% | 3 | 198 | 1 | 1.9 pounds | 2025-09-30 8个月 |
| 6 | [B0F1T5QBP8](https://www.amazon.com/dp/B0F1T5QBP8) |  | 118FT Drip Irrigation System | 228 / 62.38% | $5,698 | $24.99 | $3.85 (15%) | 64 / 7 | 4.2 | $6.90 / 57% | 1 | 132 | 1 | 2.2 pounds | 2025-03-18 1年 2个月 |
| 7 | [B0C7MGZCJK](https://www.amazon.com/dp/B0C7MGZCJK) |  | RISINGUP 49FT Solar Drip Irrigation System | 155 / 36.55% | $5,423 | $34.99 | $5.42 (15%) | 87 / 5 | 4.2 | $6.13 / 67% | 2 | 192 | 1 | 1.79 pounds | 2023-08-29 2年 9个月 |
| 8 | [B0CYG23NZR](https://www.amazon.com/dp/B0CYG23NZR) |  | SteadySpring® Smart Watering Garden Mat for Raised Garden Beds 30… | 114 / 20.45% | $4,217 | $36.99 | $5.49 (15%) | 19 / - | 4.0 | $5.61 / 70% | 1 | 270 | 2 | 0.64 pounds | 2024-03-26 2年 2个月 |
| 9 | [B0GF7SNVMD](https://www.amazon.com/dp/B0GF7SNVMD) |  | 100FT Drip Irrigation Kit System for Garden 360° Adjustable Garde… | 143 / 172.92% | $4,003 | $27.99 | $4.34 (15%) | 25 / 1 | 4.7 | $6.02 / 63% | 3 | 249 | 1 | 1.96 pounds | 2026-03-02 3个月 |
| 10 | [B0GHQXCCZ2](https://www.amazon.com/dp/B0GHQXCCZ2) |  | Solar Drip Irrigation System Timed Watering | 153 / 57.95% | $3,976 | $25.99 | $4.01 (15%) | 14 / 5 | 4.4 | $5.87 / 62% | 2 | 147 | 1 | 1.68 pounds | 2026-02-08 4个月 |
| 11 | [B0D2J1KMC9](https://www.amazon.com/dp/B0D2J1KMC9) |  | LCD Display Solar Drip Irrigation System Kit | **** / **** | **** | $29.99 | - | 91 / 1 | 4.0 | **** /  | 1 | 195 | 1 | 1.58 pounds | 2024-06-03 2年 |
| 12 | [B0GH6XXK1F](https://www.amazon.com/dp/B0GH6XXK1F) |  | 6.5L Plant Self Watering Bag | **** / **** | **** | $25.00 | - | 11 / 4 | 4.5 | **** /  | 1 | 211 | 1 | 1.3 pounds | 2026-03-06 3个月 |
| 13 | [B0BNS5VR78](https://www.amazon.com/dp/B0BNS5VR78) |  | Al-Magor-Professional Drip Irrigation Hole Punch Tool for 1/4 Inc… | **** / **** | **** | $21.99 | - | 127 / 1 | 4.4 | **** /  | 1 | 271 | 1 | 0.24 pounds | 2022-12-02 3年 6个月 |

## 二、完整商品标题

**1. [B0GJZXWSK6](https://www.amazon.com/dp/B0GJZXWSK6)** Drip Irrigation System,106FT Automatic Garden Watering System with 1/2" & 1/4" Fast-Lock Tubing Adjustable Nozzles & Sprinklers,Quick-Connect Drip Irrigation System Kit for Garden,Lawn,Potted Plants

**2. [B0G1473Y3J](https://www.amazon.com/dp/B0G1473Y3J)** HIRALIY 50FT Quick-Connect Drip Irrigation Kit, Garden Watering System with 40FT 1/4" Tubing, 10FT Main Hose & 12 Adjustable Drippers for Patio Pots, Raised Beds & Small Vegetable Gardens

**3. [B0DY7X7M4V](https://www.amazon.com/dp/B0DY7X7M4V)** Drip Irrigation Kit Automatic Watering System with Water Timer 64FT 1/4 Tubing and 12 Rain Spray Watering Nozzles in 4 Directions for Potted Plants Yard Lawn Juvenile Plants Greenhouse Mist

**4. [B0G64FH1N1](https://www.amazon.com/dp/B0G64FH1N1)** [All-New 2027] Automatic Plant Waterer for Indoor, Unistyle Plant Watering Devices for Potted Plants, Drip Irrigation System with Programmable

**5. [B0FMXHDBHK](https://www.amazon.com/dp/B0FMXHDBHK)** RAINPOINT WiFi Smart Programmable Solar Drip Irrigation System for Indoor Houseplant Water Up to 15 Pots, Compact Vacation Auto Plant Waterer Self Watering Device While Away Low Water Auto Shut-Off

**6. [B0F1T5QBP8](https://www.amazon.com/dp/B0F1T5QBP8)** 118FT Drip Irrigation System, Garden Watering System, Quick-Connect Drip Irrigation Kit for Lawn Raised Bed Greenhouse, Plant Watering System with 1/4'' Drip IrrigationTubing, Drip Emitters,Connectors

**7. [B0C7MGZCJK](https://www.amazon.com/dp/B0C7MGZCJK)** RISINGUP 49FT Solar Drip Irrigation System, Auto Plant Watering Kit with Anti-Siphoning Device 750ml/min Flow with 2200mAh Battery, for 15 Potted Plants Outdoor Garden, Patio, Balcony, Greenhouse

**8. [B0CYG23NZR](https://www.amazon.com/dp/B0CYG23NZR)** SteadySpring® Smart Watering Garden Mat for Raised Garden Beds 30-Day Irrigation Auto Refills with Rain for Gardens, Tomato Plants, Flowers (2-Pack)

**9. [B0GF7SNVMD](https://www.amazon.com/dp/B0GF7SNVMD)** 100FT Drip Irrigation Kit System for Garden 360° Adjustable Garden Sprinklers for Yard Watering System with 18 Nozzles Raised Bed Greenhouse Plant Watering Devices Misting System

**10. [B0GHQXCCZ2](https://www.amazon.com/dp/B0GHQXCCZ2)** Solar Drip Irrigation System Timed Watering, Programmable Solar Water Drip for 15 Plants, Drip Irrigation Kit with 33FT 1/4'' Tube, 15x Tee Fitting, 15x Flow Valve, 15x Drip Stake(Solar Powered)

**11. [B0D2J1KMC9](https://www.amazon.com/dp/B0D2J1KMC9)** LCD Display Solar Drip Irrigation System Kit, 30 Working Modes & 10 Watering Interval Solar Powered Drip Irrigation Kit Supports 15 Potted Plants, 2200mAh Automatic Watering System for Garden

**12. [B0GH6XXK1F](https://www.amazon.com/dp/B0GH6XXK1F)** 6.5L Plant Self Watering Bag, Automatic Drip Irrigation System with 4 Adjustable Outlets & Precision Flow Control Valves, Waterer for Indoor Outdoor Potted Plants & Flowers, Vacation Care（3PCS）

**13. [B0BNS5VR78](https://www.amazon.com/dp/B0BNS5VR78)** Al-Magor-Professional Drip Irrigation Hole Punch Tool for 1/4 Inch Fitting & Emitter Insertion Tubes Pipes 16/20mm The Original Drip Irrigation Punch Tool with Adapter for Inserting Drippers

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GJZXWSK6`: 20,133 | 0 | 0% | 559 | 43.01% | $13,969 | 100+ | $2K+ | 2 | $24.99 | - | 24 | - | 4.6 | - | $7.23 | 56% | 2026-03-26 | 2个月 | FBA | -
- `B0G1473Y3J`: 17,035 | 3,241 | 16% | 598 | 21.02% | $12,672 | 300+ | $6K+ | 2 | $21.19 | - | 44 | 8 | 4.0 | 1.34% | $6.13 | 56% | 2026-02-10 | 4个月 | FBA | -
- `B0DY7X7M4V`: 38,579 | 1,406 | 4% | 267 | 97.52% | $7,473 | - | - | 5 | $27.99 | - | 117 | 8 | 4.0 | 3% | $7.30 | 59% | 2025-04-12 | 1年 2个月 | FBA | -
- `B0G64FH1N1`: 34,380 | 10,354 | 23% | 209 | 146.38% | $7,313 | 100+ | $3K+ | 1 | $34.99 | - | 21 | 7 | 4.5 | 3.35% | $5.61 | 69% | 2026-02-12 | 4个月 | FBA | -
- `B0FMXHDBHK`: 41,281 | 37,409 | 49% | 121 | 48.98% | $6,838 | 50+ | $2K+ | 3 | $56.51 | - | 23 | 4 | 4.5 | 3.31% | $6.40 | 74% | 2025-09-30 | 8个月 | FBA | -
- `B0F1T5QBP8`: 35,692 | 7,485 | 17% | 228 | 62.38% | $5,698 | 200+ | $3K+ | 1 | $24.99 | - | 64 | 7 | 4.2 | 3.07% | $6.90 | 57% | 2025-03-18 | 1年 2个月 | FBA | -
- `B0C7MGZCJK`: 104,047 | 10,659 | 9% | 155 | 36.55% | $5,423 | 100+ | $3K+ | 2 | $34.99 | 3 | 87 | 5 | 4.2 | 3.23% | $6.13 | 67% | 2023-08-29 | 2年 9个月 | FBA | -
- `B0CYG23NZR`: 72,011 | 23,826 | 25% | 114 | 20.45% | $4,217 | 50+ | $1K+ | 1 | $36.99 | - | 19 | - | 4.0 | - | $5.61 | 70% | 2024-03-26 | 2年 2个月 | FBA | -
- `B0GF7SNVMD`: 18,090 | 85,782 | 83% | 143 | 172.92% | $4,003 | 50+ | $1K+ | 3 | $27.99 | - | 25 | 1 | 4.7 | 0.7% | $6.02 | 63% | 2026-03-02 | 3个月 | FBA | -
- `B0GHQXCCZ2`: 39,563 | 56,796 | 59% | 153 | 57.95% | $3,976 | 100+ | $2K+ | 2 | $25.99 | - | 14 | 5 | 4.4 | 3.27% | $5.87 | 62% | 2026-02-08 | 4个月 | FBA | -
- `B0D2J1KMC9`: 49,593 | 36,846 | 43% | **** | **** | **** | **** | 1 | $29.99 | - | 91 | 1 | 4.0 | 0.93% | **** | 2024-06-03 | 2年 | FBA | -
- `B0GH6XXK1F`: 59,849 | 7,282 | 11% | **** | **** | **** | **** | 1 | $25.00 | - | 11 | 4 | 4.5 | 3.25% | **** | 2026-03-06 | 3个月 | FBA | -
- `B0BNS5VR78`: 76,884 | 44,054 | 37% | **** | **** | **** | **** | 1 | $21.99 | 8 | 127 | 1 | 4.4 | 0.85% | **** | 2022-12-02 | 3年 6个月 | FBA | -

---

# Bread Proofing Baskets 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $29.00　均Reviews 570（中等）　重量 2.03lbs（重）　退货率 4.09%（低）　品牌集中度 53.8%（中等）　中国卖家 67.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0G94RRF26](https://www.amazon.com/dp/B0G94RRF26) |  | 5 Inch Mini Banneton Bread Proofing Basket Set of 4 | 230 / 11.79% | $5,170 | $22.48 | $3.46 (15%) | 33 / 3 | 4.7 | $5.76 / 59% | 2 | 78 | 1 | 1.15 pounds | 2026-02-04 4个月 |
| 2 | [B0F6CJX4BW](https://www.amazon.com/dp/B0F6CJX4BW) |  | 12-Pack Mini Banneton Baskets (5 Inch) | 120 / 27.66% | $3,479 | $28.99 | $4.24 (15%) | 96 / 2 | 4.7 | $7.07 / 61% | 1 | 148 | 1 | 1.79 pounds | 2025-06-22 11个月 |

## 二、完整商品标题

**1. [B0G94RRF26](https://www.amazon.com/dp/B0G94RRF26)** 5 Inch Mini Banneton Bread Proofing Basket Set of 4, Easy-Clean Round Sourdough Proofing Basket, Small Banneton for Sourdough Bread Baking Supplies with Liners

**2. [B0F6CJX4BW](https://www.amazon.com/dp/B0F6CJX4BW)** 12-Pack Mini Banneton Baskets (5 Inch), Round Sourdough Proofing Basket Set with Linen Liners for Small Loaves & Home Bakery Supplies

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0G94RRF26`: 29,531 | 7,491 | 19% | 230 | 11.79% | $5,170 | 200+ | $4K+ | 2 | $22.48 | - | 33 | 3 | 4.7 | 1.3% | $5.76 | 59% | 2026-02-04 | 4个月 | FBA | -
- `B0F6CJX4BW`: 60,584 | 10,844 | 15% | 120 | 27.66% | $3,479 | 100+ | $2K+ | 1 | $28.99 | - | 96 | 2 | 4.7 | 1.67% | $7.07 | 61% | 2025-06-22 | 11个月 | FBA | -

---

# Ultrasonic Repellers 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Health & Household › Household Supplies › Indoor Insect & Pest Control › Ultrasonic Repellers`
> 共抓取 **2** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **2** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $28.76　均Reviews 625（中等）　重量 0.61lbs（轻）　退货率 3.27%（低）　品牌集中度 70.0%（垄断）　中国卖家 7.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GXK8D82J](https://www.amazon.com/dp/B0GXK8D82J) |  | Ultrasonic Mouse Repellent Plug-in | 236 / 103.38% | $7,078 | $29.99 | $4.35 (14%) | 18 / 3 | 4.8 | $4.35 / 71% | 2 | 101 | 1 | 0.6 pounds | 2026-04-27 1个月 |
| 2 | [B0FV3R9L2R](https://www.amazon.com/dp/B0FV3R9L2R) |  | 2-Pack Ultrasonic Rodent Repellent for Car Engine | 170 / 17.82% | $5,098 | $29.99 | $4.54 (15%) | 39 / 10 | 4.4 | $4.76 / 69% | 1 | 67 | 1 | 0.9 pounds | 2025-12-02 6个月 |

## 二、完整商品标题

**1. [B0GXK8D82J](https://www.amazon.com/dp/B0GXK8D82J)** Ultrasonic Mouse Repellent Plug-in – Indoor Rodent Deterrent with 3 Modes & LED Strobe Lights, Mice Rat Squirrel Control for Attic, Garage, Basement (Green)

**2. [B0FV3R9L2R](https://www.amazon.com/dp/B0FV3R9L2R)** 2-Pack Ultrasonic Rodent Repellent for Car Engine, Battery Powered Under Hood Mouse Repellent with LED Strobe Lights, Keeps Rats and Mice Away from RVs, Garage, Shed, Attic, Indoors

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GXK8D82J`: 89,283 | 44,315 | 33% | 236 | 103.38% | $7,078 | 100+ | $2K+ | 2 | $29.99 | - | 18 | 3 | 4.8 | 1.27% | $4.35 | 71% | 2026-04-27 | 1个月 | FBA | -
- `B0FV3R9L2R`: 66,479 | 34,408 | 34% | 170 | 17.82% | $5,098 | 100+ | $3K+ | 1 | $29.99 | - | 39 | 10 | 4.4 | 5.88% | $4.76 | 69% | 2025-12-02 | 6个月 | FBA | -

---

# Decorative Boxes 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes`
> 共抓取 **18** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **18** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $23.78　均Reviews 694（中等）　重量 1.57lbs（偏重）　退货率 7.91%（中）　品牌集中度 54.4%（中等）　中国卖家 67.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B0GKXY24FG](https://www.amazon.com/dp/B0GKXY24FG) |  | Vintage Faux Book Box Set of 3 Brown Linen Decorative Books for S… | 867 / 13.24% | $19,499 | $22.49 | $3.43 (15%) | 58 / 23 | 4.8 | $6.02 / 58% | 4 | 9 | 1 | 1.94 pounds | 2026-04-06 2个月 |
| 2 | [B0GRC76TKN](https://www.amazon.com/dp/B0GRC76TKN) |  | One Hitter Box & 2pcs Metal Tubes | 578 / 146.7% | $12,132 | $20.99 | $3.18 (15%) | 16 / 9 | 4.3 | $3.54 / 68% | 1 | 50 | 2 | 0.13 pounds | 2026-03-22 2个月 |
| 3 | [B0CJ1XRT2Z](https://www.amazon.com/dp/B0CJ1XRT2Z) |  | Navigators Compass Design Wooden Keepsake Box | 195 / 51.47% | $9,748 | $49.99 | $7.61 (15%) | 118 / 6 | 4.4 | $8.89 / 67% | 4 | 272 | 1 | 4.3 pounds | 2023-09-16 2年 8个月 |
| 4 | [B0G6391R1J](https://www.amazon.com/dp/B0G6391R1J) |  | Set of 3 Decorative Books for Home Decor | 328 / 101.31% | $7,869 | $23.99 | $3.69 (15%) | 47 / 5 | 4.8 | $5.91 / 60% | 3 | 98 | 1 | 1.92 pounds | 2025-12-15 5个月 |
| 5 | [B0CGHZ1DDM](https://www.amazon.com/dp/B0CGHZ1DDM) |  | S'Mores Station | 211 / 10.92% | $6,328 | $29.99 | $4.40 (15%) | 106 / 3 | 4.5 | $7.30 / 61% | 2 | 232 | 1 | 1.63 pounds | 2023-11-18 2年 6个月 |
| 6 | [B0FH4CGRG6](https://www.amazon.com/dp/B0FH4CGRG6) |  | Reallnaive 35 Pcs S'mores Station Box Farmhouse Smores Bar Holder… | 179 / 79.44% | $6,084 | $33.99 | $5.25 (15%) | 21 / 4 | 4.2 | $6.31 / 66% | 3 | 231 | 1 | 1.85 pounds | 2025-07-13 11个月 |
| 7 | [B0FLW9HLWH](https://www.amazon.com/dp/B0FLW9HLWH) |  | cherish & dwell Beautiful Cozy Corduroy Decorative Storage Boxes… | 162 / 95.74% | $4,858 | $29.99 | $4.45 (15%) | 35 / - | 4.9 | $7.55 / 60% | 1 | 401 | 1 | 3.33 pounds | 2025-12-15 5个月 |
| 8 | [B0DG2J8D21](https://www.amazon.com/dp/B0DG2J8D21) |  | Vintage Treasure Chest | 176 / 10.11% | $4,574 | $25.99 | $3.86 (15%) | 82 / 4 | 4.7 | $7.32 / 57% | 3 | 421 | 1 | 1.79 pounds | 2024-10-29 1年 7个月 |
| 9 | [B0DX841J37](https://www.amazon.com/dp/B0DX841J37) |  | Large Wooden Memory Box for Keepsakes | 130 / 11.32% | $4,549 | $34.99 | $5.16 (15%) | 56 / 3 | 4.8 | $7.79 / 63% | 1 | 266 | 1 | 3 pounds | 2025-04-10 1年 2个月 |
| 10 | [B0FN46S75Q](https://www.amazon.com/dp/B0FN46S75Q) |  | SwallowLiving Vintage Wooden Treasure Chest Box with Lock | 125 / 32.26% | $4,374 | $34.99 | $5.41 (15%) | 12 / 4 | 4.9 | $7.89 / 62% | 2 | 722 | 2 | 2.31 pounds | 2025-10-28 7个月 |
| 11 | [B0FQJ8JPFM](https://www.amazon.com/dp/B0FQJ8JPFM) |  | Bamboo Phone Box | **** / **** | **** | $34.99 | - | 10 / 3 | 4.6 | **** /  | 2 | 564 | 1 | 2.43 pounds | 2025-11-12 7个月 |
| 12 | [B0F4D1JVBP](https://www.amazon.com/dp/B0F4D1JVBP) |  | Decorative Book Storage Box Set of 2 | **** / **** | **** | $24.99 | - | 96 / 8 | 4.6 | **** /  | 5 | 302 | 1 | 1.34 pounds | 2025-05-26 1年 |
| 13 | [B0G31WNCCS](https://www.amazon.com/dp/B0G31WNCCS) |  | Decorative Books for Home Decor | **** / **** | **** | $20.99 | - | 17 / 3 | 4.7 | **** /  | 2 | 408 | 1 | 1.59 pounds | 2026-01-09 5个月 |
| 14 | [B0DMN38XJM](https://www.amazon.com/dp/B0DMN38XJM) |  | TwoDays Motivational Office Decor | **** / **** | **** | $25.99 | - | 67 / 6 | 4.7 | **** /  | 1 | 396 | 1 | 1.76 pounds | 2025-01-28 1年 4个月 |
| 15 | [B0FQ84PMTP](https://www.amazon.com/dp/B0FQ84PMTP) |  | Decorative Fake Books for Home Decor | **** / **** | **** | $24.99 | - | 12 / 1 | 4.3 | **** /  | 1 | 304 | 1 | 1.3 pounds | 2025-12-19 5个月 |
| 16 | [B0DX23QLV3](https://www.amazon.com/dp/B0DX23QLV3) |  | Unfinished Wood Box with Hinged Lid 1 Pack | **** / **** | **** | $22.99 | - | 50 / 3 | 4.3 | **** /  | 1 | 506 | 1 | 1.39 pounds | 2025-08-15 9个月 |
| 17 | [B0GT8CF7MB](https://www.amazon.com/dp/B0GT8CF7MB) |  | CNARIO Decorative Books for Home Decor | **** / **** | **** | $24.99 | - | 28 / 4 | 4.9 | **** /  | 1 | 449 | 1 | 1.83 pounds | 2026-04-10 2个月 |
| 18 | [B0C8HDZCTS](https://www.amazon.com/dp/B0C8HDZCTS) |  | Hipiwe Glass Display Case for Collectibles Vintage Gold Display B… | **** / **** | **** | $20.99 | - | 66 / 1 | 4.5 | **** /  | 3 | 440 | 1 | 1.12 pounds | 2023-07-03 2年 11个月 |

## 二、完整商品标题

**1. [B0GKXY24FG](https://www.amazon.com/dp/B0GKXY24FG)** Vintage Faux Book Box Set of 3 Brown Linen Decorative Books for Shelves, Fake Books for Decoration with Secret Compartment, Rustic Farmhouse Coffee Table Decor (Brown-Beige-White)

**2. [B0GRC76TKN](https://www.amazon.com/dp/B0GRC76TKN)** One Hitter Box & 2pcs Metal Tubes, Handmade Walnut Storage Box, Portable Storage Box, Lid 360°Rotation DIY Handmade Art Decorations Gifts for Men, Gifts for Father's Day

**3. [B0CJ1XRT2Z](https://www.amazon.com/dp/B0CJ1XRT2Z)** Navigators Compass Design Wooden Keepsake Box, Large Memory Box for Keepsakes, Decorative Storage Box for Memories, Jewelry, & Photos, Memorial Boxes for Men & Women

**4. [B0G6391R1J](https://www.amazon.com/dp/B0G6391R1J)** Set of 3 Decorative Books for Home Decor, Linen Faux Books for Coffee Table, Bookshelf or Mantel, Aesthetic Fake Book Storage Boxes with Magnetic Snap for Photo Organization & Keepsakes Box

**5. [B0CGHZ1DDM](https://www.amazon.com/dp/B0CGHZ1DDM)** S'Mores Station, Farmhouse Smores Caddy with Handles, Smores Kit for Fire Pit Smores Maker Box, Smores Bar Station with 5Pcs Extendable Marshmallow Roasting Sticks, Camping Essentials Gear Accessories

**6. [B0FH4CGRG6](https://www.amazon.com/dp/B0FH4CGRG6)** Reallnaive 35 Pcs S'mores Station Box Farmhouse Smores Bar Holder with Handles 8 Extendable Marshmallow Roasting Sticks 1 Storage Bucket 24 Label Cards Storage Smores Accessories Organizer(Brown)

**7. [B0FLW9HLWH](https://www.amazon.com/dp/B0FLW9HLWH)** cherish & dwell Beautiful Cozy Corduroy Decorative Storage Boxes with Lids – Set of 2 Keepsake Boxes for Photos, Documents and Home Decor Accents - Giftable Memory Boxes for Mom

**8. [B0DG2J8D21](https://www.amazon.com/dp/B0DG2J8D21)** Vintage Treasure Chest, Pirate Keepsakes Box for Gifts, Wooden Storage, Green Decorative Container for Jewelry, Pearl Trinkets, Tarot Cards - Large

**9. [B0DX841J37](https://www.amazon.com/dp/B0DX841J37)** Large Wooden Memory Box for Keepsakes, Wooden Keepsake Box for Memories, Weddings, Engraved Memory Keepsake Box, Decorative Storage Box

**10. [B0FN46S75Q](https://www.amazon.com/dp/B0FN46S75Q)** SwallowLiving Vintage Wooden Treasure Chest Box with Lock – 12.2"x7.1"x7.1" Decorative Storage Box for Keepsakes, Jewelry, Gifts, Pirate Chest Style with Combination Padlock,Brown

**11. [B0FQJ8JPFM](https://www.amazon.com/dp/B0FQJ8JPFM)** Bamboo Phone Box, Premium Cell Phone Box for Family Time, Cell Phone Jail with Charging Holes,Phone Lock Box Holds 6 Phones (Walnut)

**12. [B0F4D1JVBP](https://www.amazon.com/dp/B0F4D1JVBP)** Decorative Book Storage Box Set of 2, Stylish Decorative Books, Linen Faux Book Storage Box for Bookshelf, Coffee Tables, Home Decor, GrassGreen

**13. [B0G31WNCCS](https://www.amazon.com/dp/B0G31WNCCS)** Decorative Books for Home Decor, Coffee Table Books Decor, 2 Linen Faux/Fake Books with Beads for Farmhouse Decor, Bookself, Mordern Room Decor Aesthetic

**14. [B0DMN38XJM](https://www.amazon.com/dp/B0DMN38XJM)** TwoDays Motivational Office Decor - Modern Decorative Books (Set of 3), 6.7 x 9.8 x 1.4 inches

**15. [B0FQ84PMTP](https://www.amazon.com/dp/B0FQ84PMTP)** Decorative Fake Books for Home Decor – Set of 2 Linen Faux Book Storage Boxes with Hidden Storage to Reduce Visible Clutter, Coffee Table & Bookshelf Decor for Living Room Styling

**16. [B0DX23QLV3](https://www.amazon.com/dp/B0DX23QLV3)** Unfinished Wood Box with Hinged Lid 1 Pack - 10.6" x 7.6" x 4.3" Smooth Unpainted Wooden Storage Box for Crafts, Jewelry, DIY Painting, Gift Packaging - Lightweight & Warp-Resistant

**17. [B0GT8CF7MB](https://www.amazon.com/dp/B0GT8CF7MB)** CNARIO Decorative Books for Home Decor, Set of 3 Linen Faux Books, Coffee Table Decor, Hidden Storage Book Box for Bookshelf, Mantel & Entryway, Photo & Keepsake Organization

**18. [B0C8HDZCTS](https://www.amazon.com/dp/B0C8HDZCTS)** Hipiwe Glass Display Case for Collectibles Vintage Gold Display Box with Black Wood Base for Plants Action Figurine Models Clear Keepsake Box, Square, 3.3x3.3x3.6 Inch

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B0GKXY24FG`: 19,925 | 20,720 | 51% | 867 | 13.24% | $19,499 | 500+ | $12K+ | 4 | $22.49 | - | 58 | 23 | 4.8 | 2.65% | $6.02 | 58% | 2026-04-06 | 2个月 | FBA | -
- `B0GRC76TKN`: 53,955 | 14,468 | 21% | 578 | 146.7% | $12,132 | 500+ | $11K+ | 1 | $20.99 | - | 16 | 9 | 4.3 | 1.56% | $3.54 | 68% | 2026-03-22 | 2个月 | FBA | -
- `B0CJ1XRT2Z`: 151,038 | 15,076 | 9% | 195 | 51.47% | $9,748 | 100+ | $5K+ | 4 | $49.99 | - | 118 | 6 | 4.4 | 3.08% | $8.89 | 67% | 2023-09-16 | 2年 8个月 | FBA | -
- `B0G6391R1J`: 95,305 | 10,426 | 10% | 328 | 101.31% | $7,869 | 200+ | $4K+ | 3 | $23.99 | - | 47 | 5 | 4.8 | 1.52% | $5.91 | 60% | 2025-12-15 | 5个月 | FBA | -
- `B0CGHZ1DDM`: 163,909 | 29,375 | 15% | 211 | 10.92% | $6,328 | 100+ | $2K+ | 2 | $29.99 | - | 106 | 3 | 4.5 | 1.42% | $7.30 | 61% | 2023-11-18 | 2年 6个月 | FBA | -
- `B0FH4CGRG6`: 159,924 | 38,971 | 20% | 179 | 79.44% | $6,084 | 50+ | $1K+ | 3 | $33.99 | - | 21 | 4 | 4.2 | 2.23% | $6.31 | 66% | 2025-07-13 | 11个月 | FBA | -
- `B0FLW9HLWH`: 200,907 | 0 | 0% | 162 | 95.74% | $4,858 | 100+ | $2K+ | 1 | $29.99 | - | 35 | - | 4.9 | - | $7.55 | 60% | 2025-12-15 | 5个月 | FBA | -
- `B0DG2J8D21`: 218,934 | 5,428 | 2% | 176 | 10.11% | $4,574 | 50+ | $1K+ | 3 | $25.99 | - | 82 | 4 | 4.7 | 2.27% | $7.32 | 57% | 2024-10-29 | 1年 7个月 | FBA | -
- `B0DX841J37`: 183,605 | 59,487 | 24% | 130 | 11.32% | $4,549 | 100+ | $3K+ | 1 | $34.99 | - | 56 | 3 | 4.8 | 2.31% | $7.79 | 63% | 2025-04-10 | 1年 2个月 | FBA | -
- `B0FN46S75Q`: 209,815 | 14,882 | 7% | 125 | 32.26% | $4,374 | 50+ | $1K+ | 2 | $34.99 | - | 12 | 4 | 4.9 | 3.2% | $7.89 | 62% | 2025-10-28 | 7个月 | FBA | -
- `B0FQJ8JPFM`: 314,638 | 58,692 | 20% | **** | **** | **** | **** | 2 | $34.99 | - | 10 | 3 | 4.6 | 2.44% | **** | 2025-11-12 | 7个月 | FBA | -
- `B0F4D1JVBP`: 196,228 | 84,330 | 35% | **** | **** | **** | **** | 5 | $24.99 | - | 96 | 8 | 4.6 | 5.23% | **** | 2025-05-26 | 1年 | FBA | -
- `B0G31WNCCS`: 198,505 | 18,165 | 8% | **** | **** | **** | **** | 2 | $20.99 | - | 17 | 3 | 4.7 | 1.71% | **** | 2026-01-09 | 5个月 | FBA | -
- `B0DMN38XJM`: 208,177 | 3,577 | 2% | **** | **** | **** | **** | 1 | $25.99 | - | 67 | 6 | 4.7 | 4.26% | **** | 2025-01-28 | 1年 4个月 | FBA | -
- `B0FQ84PMTP`: 257,831 | 43,344 | 14% | **** | **** | **** | **** | 1 | $24.99 | - | 12 | 1 | 4.3 | 0.8% | **** | 2025-12-19 | 5个月 | FBA | -
- `B0DX23QLV3`: 223,864 | 18,495 | 8% | **** | **** | **** | **** | 1 | $22.99 | - | 50 | 3 | 4.3 | 2.34% | **** | 2025-08-15 | 9个月 | FBA | -
- `B0GT8CF7MB`: 222,875 | 113,370 | 34% | **** | **** | **** | **** | 1 | $24.99 | - | 28 | 4 | 4.9 | 3.6% | **** | 2026-04-10 | 2个月 | FBA | -
- `B0C8HDZCTS`: 233,779 | 11,423 | 5% | **** | **** | **** | **** | 3 | $20.99 | - | 66 | 1 | 4.5 | 0.8% | **** | 2023-07-03 | 2年 11个月 | FBA | -

---

# Pool & Deck Repair Products 合格产品扫描 (2026-06-14)

> **所在品类路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products`
> 共抓取 **3** 个通过全部筛选条件的候选商品。

> **抓取完整性**：页面可见 **3** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。

> **市场评级**：🟡 Yellow (Cautious)　均价 $31.79　均Reviews 682（中等）　重量 2.28lbs（重）　退货率 1.93%（低）　品牌集中度 57.6%（中等）　中国卖家 48.0%

## 一、候选商品列表

| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |
|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|
| 1 | [B00Q2L3S1O](https://www.amazon.com/dp/B00Q2L3S1O) |  | Pool Patch Pool Deck Repair Kit | 200 / 120.22% | $9,398 | $46.99 | $7.11 (15%) | 107 / 3 | 4.1 | $7.46 / 69% | 1 | 98 | 2 | 3.53 pounds | 2015-03-26 11年 2个月 |
| 2 | [B00Q2L3QCU](https://www.amazon.com/dp/B00Q2L3QCU) |  | Pool Patch Gray Pool Tile Adhesive Thinset Repair Kit 3 lb | 171 / 40.21% | $6,838 | $39.99 | $5.90 (15%) | 57 / - | 4.2 | $7.30 / 67% | 1 | 92 | 2 | 3.17 pounds | 2015-02-25 11年 3个月 |
| 3 | [B0D5DMD84K](https://www.amazon.com/dp/B0D5DMD84K) |  | Pool Anchor Socket Cover Shields for Ladder and Handrails，Pool La… | 150 / 46.46% | $4,499 | $29.99 | $4.49 (15%) | 52 / 2 | 4.2 | $6.31 / 64% | 1 | 115 | 1 | 0.86 pounds | 2024-07-02 1年 11个月 |

## 二、完整商品标题

**1. [B00Q2L3S1O](https://www.amazon.com/dp/B00Q2L3S1O)** Pool Patch Pool Deck Repair Kit - Sand Buff 3lb Cool Deck Patch DIY Patio Repair

**2. [B00Q2L3QCU](https://www.amazon.com/dp/B00Q2L3QCU)** Pool Patch Gray Pool Tile Adhesive Thinset Repair Kit 3 lb - Easy to Mix and Apply Setting Formula - Perfect to Glue Pool Tile - Quick-Drying, Extra Strong Bond - (coverage: approx. 6 sq. ft)

**3. [B0D5DMD84K](https://www.amazon.com/dp/B0D5DMD84K)** Pool Anchor Socket Cover Shields for Ladder and Handrails，Pool Ladder Hole Covers and Railing Bases Accessories -White Set of 2

## 三、下一步建议

1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。

2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。

3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。

## 四、原始数值

- `B00Q2L3S1O`: 57,371 | 7,125 | 11% | 200 | 120.22% | $9,398 | 100+ | $4K+ | 1 | $46.99 | - | 107 | 3 | 4.1 | 1.5% | $7.46 | 69% | 2015-03-26 | 11年 2个月 | FBA | -
- `B00Q2L3QCU`: 34,290 | 8,753 | 21% | 171 | 40.21% | $6,838 | 100+ | $3K+ | 1 | $39.99 | - | 57 | - | 4.2 | - | $7.30 | 67% | 2015-02-25 | 11年 3个月 | FBA | -
- `B0D5DMD84K`: 64,808 | 25,254 | 28% | 150 | 46.46% | $4,499 | 100+ | $2K+ | 1 | $29.99 | - | 52 | 2 | 4.2 | 1.33% | $6.31 | 64% | 2024-07-02 | 1年 11个月 | FBA | -

---

# Swing Trainers 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0DSRDB4YL`, `B0GKMGJLL3`, `B0G1MSTY15`, `B0F5BD54RT`, `B0GKG8PKTX`, `B0DTP76XQP`, `B0FGHZXNGV`, `B0DX2F3V5Q`, `B0DS2CBVFT`, `B0D37GG2SJ`, `B0FZJSDVF8`, `B0F98Y7S35`, `B0F9ZZ17Z8`, `B0GL785GSP`, `B0F6KRVBGR`, `B0F62YLXK6`, `B0GLQ8T4P3`, `B0CT5MVCFD`, `B0FNNCDS7D`, `B0G51VX3YD`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **catfishing equipment **<br>鲶鱼设备 | 3.09% |  |  | 28,440 | 264 | 6 | 2 | 3,197 | $0.41 | 33.09 |
| 2 | **tackle box backpack **<br>钓具箱背囊 | 2.96% |  |  | 23,031 | 264 | 7 | 4 | 1,907 | $0.60 | 32.96 |
| 3 | **baby life jacket 12-18 months **<br>12-18个月的婴儿救生衣 | 2.73% |  |  | 19,008 | 239 | 6 | 0 | 859 | $0.32 | 32.73 |
| 4 | **fishing tackle backpack **<br>钓具背包 | 2.57% |  |  | 20,610 | 237 | 6 | 15 | 2,767 | $0.56 | 32.57 |
| 5 | **infant life vest **<br>婴儿救生衣 | 2.39% |  |  | 19,313 | 312 | 8 | 1 | 871 | $0.63 | 32.39 |
| 6 | **kids fishing gear **<br>儿童渔具 | 2.39% |  |  | 19,153 | 329 | 8 | 4 | 8,791 | $0.72 | 32.39 |
| 7 | **backpack tackle box **<br>背负式钓箱 | 2.17% |  |  | 18,222 | 229 | 6 | 1 | 1,950 | $0.59 | 32.17 |
| 8 | **tactical sling bag **<br>战术吊袋 | 2.30% |  |  | 20,155 | 197 | 5 | 14 | 4,745 | $0.32 | 32.15 |
| 9 | **life jacket for 1 year old **<br>1岁的救生衣 | 2.51% |  |  | 16,523 | 190 | 5 | 0 | 664 | $0.33 | 32.01 |
| 10 | **fishing kits for adults **<br>成人钓鱼工具包 | 1.69% |  |  | 14,223 | 433 | 10 | 0 | 10,903 | $0.67 | 31.69 |
| 11 | **tacklebox **<br>钓具箱 | 1.57% |  |  | 13,899 | 283 | 7 | 1 | 1,015 | $0.41 | 31.57 |
| 12 | **fishing accessories for men **<br>男士钓鱼配件 | 2.73% |  |  | 17,466 | 151 | 4 | 2 | 809 | $0.44 | 30.28 |
| 13 | **boat shade **<br>船影 | 1.34% |  |  | 9,882 | 178 | 5 | 11 | 5,678 | $0.49 | 30.0 |
| 14 | **baby life vest **<br>婴儿救生衣 | 1.54% |  |  | 11,918 | 162 | 4 | 3 | 1,099 | $0.37 | 29.64 |
| 15 | **trout fishing gear **<br>鳟鱼渔具 | 1.93% |  |  | 20,224 | 153 | 4 | 2 | 11,454 | $0.66 | 29.58 |
| 16 | **saltwater fishing gear **<br>咸水渔具 | 1.39% |  |  | 24,475 | 144 | 4 | 2 | 14,318 | $0.60 | 28.59 |
| 17 | **bimini tops for boats **<br>船用比米尼顶篷 | 1.75% |  |  | 52,194 | 120 | 3 | 4 | 2,305 | $0.80 | 27.75 |
| 18 | **kayak lights **<br>皮划艇灯 | 1.36% |  |  | 9,782 | 123 | 3 | 9 | 8,160 | $0.41 | 27.07 |
| 19 | **water aerobics weights **<br>水中有氧运动重量 | 1.62% |  |  | 6,763 | 256 | 6 | 0 | 1,729 | $0.67 | 25.15 |
| 20 | **fishing bag backpack **<br>钓鱼袋背包 | 1.50% |  |  | 9,748 | 74 | 2 | 0 | 11,736 | $0.64 | 24.7 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0DSRDB4YL, B0GKMGJLL3, B0G1MSTY15, B0F5BD54RT, B0GKG8PKTX, B0DTP76XQP, B0FGHZXNGV, B0DX2F3V5Q, B0DS2CBVFT, B0D37GG2SJ, B0FZJSDVF8, B0F98Y7S35, B0F9ZZ17Z8, B0GL785GSP, B0F6KRVBGR, B0F62YLXK6, B0GLQ8T4P3, B0CT5MVCFD, B0FNNCDS7D, B0G51VX3YD）

1. **catfishing equipment ** — 鲶鱼设备
2. **tackle box backpack ** — 钓具箱背囊
3. **baby life jacket 12-18 months ** — 12-18个月的婴儿救生衣
4. **fishing accessories for men ** — 男士钓鱼配件
5. **fishing tackle backpack ** — 钓具背包
6. **life jacket for 1 year old ** — 1岁的救生衣
7. **infant life vest ** — 婴儿救生衣
8. **kids fishing gear ** — 儿童渔具
9. **tactical sling bag ** — 战术吊袋
10. **backpack tackle box ** — 背负式钓箱
11. **trout fishing gear ** — 鳟鱼渔具
12. **bimini tops for boats ** — 船用比米尼顶篷
13. **fishing kits for adults ** — 成人钓鱼工具包
14. **water aerobics weights ** — 水中有氧运动重量
15. **tacklebox ** — 钓具箱
16. **baby life vest ** — 婴儿救生衣
17. **fishing bag backpack ** — 钓鱼袋背包
18. **saltwater fishing gear ** — 咸水渔具
19. **kayak lights ** — 皮划艇灯
20. **boat shade ** — 船影

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
| 1 | **pool lights that float **<br>漂浮的泳池灯 | 30.97% |  |  | 5,589 | 134 | 4 | 7 | 1,061 | $0.49 | 47.88 |
| 2 | **magnetic pool lights **<br>磁池灯 | 23.65% |  |  | 6,394 | 52 | 2 | 1 | 662 | $0.59 | 39.04 |
| 3 | **solar sun rings **<br>太阳太阳环 | 10.29% |  |  | 7,800 | 269 | 7 | 9 | 230 | $0.41 | 35.89 |
| 4 | **pool balls for swimming pool **<br>游泳池球 | 0.87% |  |  | 13,458 | 767 | 18 | 2 | 6,175 | $0.67 | 30.87 |
| 5 | **outdoor pool decor **<br>室外游泳池装饰 | 8.09% |  |  | 9,318 | 70 | 2 | 3 | 498 | $0.32 | 30.23 |
| 6 | **solar fountain for pool **<br>游泳池太阳能喷泉 | 1.97% |  |  | 20,160 | 86 | 2 | 0 | 1,395 | $0.58 | 26.27 |
| 7 | **floating solar fountain **<br>漂浮的太阳能喷泉 | 1.00% |  |  | 12,757 | 96 | 3 | 3 | 1,299 | $0.64 | 25.8 |
| 8 | **solar fountain with lights **<br>带灯的太阳能喷泉 | 3.11% |  |  | 13,539 | 51 | 2 | 0 | 2,540 | $0.59 | 25.66 |
| 9 | **floating lights for pool **<br>泳池漂浮灯 | 12.92% |  |  | 4,089 | 83 | 2 | 1 | 6,389 | $0.73 | 25.25 |
| 10 | **solar flame lights **<br>太阳能火焰灯 | 0.04% |  |  | 7,810 | 152 | 4 | 3 | 2,457 | $0.63 | 23.26 |
| 11 | **hot tub lights **<br>热水浴缸灯 | 0.91% |  |  | 4,277 | 143 | 4 | 4 | 5,566 | $0.81 | 16.61 |
| 12 | **floating flowers for pool **<br>游泳池的漂浮花 | 0.04% |  |  | 2,439 | 239 | 6 | 2 | 1,061 | $0.38 | 14.92 |
| 13 | **waterproof led lights **<br>防水LED灯 | 0.10% |  |  | 5,189 | 62 | 2 | 1 | 361 | $0.45 | 13.58 |
| 14 | **velas flotantes para agua **<br>贝拉斯浮台－巴拉阿瓜 | 0.12% |  |  | 3,964 | 107 | 3 | 0 | 241 | $0.44 | 13.4 |
| 15 | **pool fountains **<br>泳池喷泉 | 0.40% |  |  | 3,859 | 52 | 2 | 10 | 6,666 | $0.62 | 10.72 |
| 16 | **pool light gasket **<br>泳池灯垫圈 | 2.00% |  |  | 2,498 | 62 | 2 | 7 | 10,558 | $0.69 | 10.1 |
| 17 | **flame solar lights **<br>火焰太阳能灯 | 0.01% |  |  | 2,959 | 80 | 2 | 0 | 3,922 | $0.63 | 9.93 |
| 18 | **waterproof lights **<br>防水灯 | - |  |  | 1,926 | 100 | 3 | 0 | 287 | $0.47 | 8.85 |
| 19 | **light up beach balls for pool **<br>为泳池点亮沙滩球 | 2.30% |  |  | 1,525 | 53 | 2 | 2 | 817 | $0.57 | 8.0 |
| 20 | **hot tub light **<br>热水浴缸灯 | 1.20% |  |  | 1,458 | 59 | 2 | 4 | 5,394 | $0.77 | 7.07 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G6L569ZB, B0GD7YRTDM, B0GJCRX242, B0DXVSDMZF, B0DSHT56KC, B0GRTPX9DC, B0GPW9YT5H, B0G6Z1QM2M, B0DZD1RC33, B0DWMMYNDB, B0G6SLH595, B0DSD4NWXN, B0FWJ6C4CY, B0CX9162PJ, B0G8X6721P, B0FWC5JQL9, B0D93J8T91, B0G6TLWN2W, B0DN6FBDDQ, B0GCZ27BY1）

1. **pool lights that float ** — 漂浮的泳池灯
2. **magnetic pool lights ** — 磁池灯
3. **floating lights for pool ** — 泳池漂浮灯
4. **solar sun rings ** — 太阳太阳环
5. **outdoor pool decor ** — 室外游泳池装饰
6. **solar fountain with lights ** — 带灯的太阳能喷泉
7. **light up beach balls for pool ** — 为泳池点亮沙滩球
8. **pool light gasket ** — 泳池灯垫圈
9. **solar fountain for pool ** — 游泳池太阳能喷泉
10. **hot tub light ** — 热水浴缸灯
11. **floating solar fountain ** — 漂浮的太阳能喷泉
12. **hot tub lights ** — 热水浴缸灯
13. **pool balls for swimming pool ** — 游泳池球
14. **pool fountains ** — 泳池喷泉
15. **velas flotantes para agua ** — 贝拉斯浮台－巴拉阿瓜
16. **waterproof led lights ** — 防水LED灯
17. **floating flowers for pool ** — 游泳池的漂浮花
18. **solar flame lights ** — 太阳能火焰灯
19. **flame solar lights ** — 火焰太阳能灯
20. **waterproof lights ** — 防水灯

---

# Nicotine Patches 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0G839C2C2`, `B0DKP86SX6`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **9** 个，过滤后保留 **9** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **x39 patches lifewave stem cell **<br>x39 贴片 Lifewave 干细胞 | 40.45% |  |  | 6,620 | 300 | 7 | 0 | 74 | $0.73 | 53.24 |
| 2 | **hangover kits **<br>宿醉套装 | 33.59% |  |  | 4,702 | 127 | 3 | 6 | 400 | $0.32 | 45.75 |
| 3 | **nad patches **<br>nad 补丁 | - |  |  | 19,812 | 215 | 5 | 14 | 221 | $0.58 | 30.0 |
| 4 | **girls trip gifts favors **<br>女孩旅行礼物恩惠 | - |  |  | 18,789 | 659 | 15 | 9 | 5,649 | $0.32 | 30.0 |
| 5 | **nicoderm cq **<br>尼古德姆cq | 13.20% |  |  | 1,480 | 253 | 6 | 4 | 47 | $0.32 | 26.16 |
| 6 | **nicoderm patches **<br>尼古丁贴剂 | 12.48% |  |  | 1,448 | 200 | 5 | 0 | 150 | $0.32 | 25.38 |
| 7 | **lifewave patches **<br>生命波补丁 | - |  |  | 4,123 | 140 | 4 | 2 | 242 | $0.52 | 15.25 |
| 8 | **hangover recovery kit **<br>宿醉恢复套件 | 0.27% |  |  | 3,404 | 74 | 2 | 4 | 338 | $0.32 | 10.78 |
| 9 | **no nicotine cigarettes **<br>没有尼古丁香烟 | - |  |  | 1,794 | 54 | 2 | 0 | 671 | $0.32 | 6.29 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G839C2C2, B0DKP86SX6）

1. **x39 patches lifewave stem cell ** — x39 贴片 Lifewave 干细胞
2. **hangover kits ** — 宿醉套装
3. **nicoderm cq ** — 尼古德姆cq
4. **nicoderm patches ** — 尼古丁贴剂
5. **hangover recovery kit ** — 宿醉恢复套件
6. **no nicotine cigarettes ** — 没有尼古丁香烟
7. **nad patches ** — nad 补丁
8. **lifewave patches ** — 生命波补丁
9. **girls trip gifts favors ** — 女孩旅行礼物恩惠

---

# Water Balloons 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GC43CR19`, `B0GKFSMPTP`, `B0GD11KHJB`, `B0DZFGJQ5N`, `B0DZML5ZPH`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **zuru bunch o balloons **<br>zuru 束 o 气球 | 26.91% |  |  | 4,549 | 129 | 3 | 12 | 231 | $0.46 | 42.46 |
| 2 | **32 panel hacky sack **<br>32面袋球 | 9.62% |  |  | 47,661 | 490 | 12 | 0 | 98 | $0.37 | 39.62 |
| 3 | **backyard water fun **<br>后院玩水 | 13.63% |  |  | 16,585 | 63 | 2 | 0 | 12,259 | $0.47 | 36.78 |
| 4 | **little tikes outdoor toys **<br>little tikes 户外玩具 | 3.14% |  |  | 69,974 | 209 | 5 | 0 | 728 | $0.41 | 33.14 |
| 5 | **basketball hoop for kids 1-3 **<br>1-3岁儿童篮球架 | 2.66% |  |  | 11,218 | 355 | 9 | 5 | 1,564 | $0.68 | 32.66 |
| 6 | **little tikes water table **<br>little tikes 地下水位 | 1.24% |  |  | 27,980 | 304 | 8 | 0 | 682 | $0.32 | 31.24 |
| 7 | **2 year old boy toys **<br>2岁男孩的玩具 | 0.67% |  |  | 32,911 | 865 | 20 | 0 | 8,306 | $0.62 | 30.67 |
| 8 | **baby water table **<br>婴儿饮水台 | 0.81% |  |  | 17,694 | 129 | 3 | 0 | 13,784 | $0.46 | 27.26 |
| 9 | **juguetes para niños 1 a 2 años **<br>juguetes para niños 1 a 2 años | 0.57% |  |  | 25,104 | 85 | 2 | 0 | 830 | $0.52 | 24.82 |
| 10 | **water slide for kids **<br>儿童水滑梯 | 0.73% |  |  | 18,711 | 80 | 2 | 7 | 12,137 | $0.32 | 24.73 |
| 11 | **toddler outdoor playset **<br>幼儿户外玩具套装 | 0.53% |  |  | 30,314 | 81 | 2 | 3 | 3,851 | $0.39 | 24.58 |
| 12 | **water fun for kids outdoor **<br>孩子们在户外玩水 | 6.25% |  |  | 7,754 | 52 | 2 | 0 | 1,832 | $0.32 | 24.36 |
| 13 | **toddler basketball hoop set **<br>幼儿篮球架套装 | 0.55% |  |  | 12,749 | 76 | 2 | 2 | 1,610 | $0.67 | 24.35 |
| 14 | **yard games for family **<br>适合家庭的院子游戏 | 0.58% |  |  | 5,384 | 476 | 11 | 1 | 519 | $0.54 | 21.35 |
| 15 | **giant tower stack game **<br>巨型塔堆叠游戏 | 6.58% |  |  | 5,557 | 60 | 2 | 0 | 978 | $0.69 | 20.69 |
| 16 | **slingshot for kids **<br>儿童弹弓 | 1.09% |  |  | 4,486 | 802 | 19 | 7 | 1,140 | $0.55 | 20.06 |
| 17 | **burger mania game **<br>汉堡狂热游戏 | 6.80% |  |  | 1,509 | 335 | 8 | 0 | 137 | $0.32 | 19.82 |
| 18 | **adult yard games **<br>成人院子游戏 | 1.22% |  |  | 3,974 | 257 | 6 | 0 | 9,914 | $0.48 | 19.17 |
| 19 | **giant water balloon **<br>巨大的水气球 | 5.14% |  |  | 2,210 | 147 | 4 | 0 | 7,323 | $0.43 | 16.91 |
| 20 | **ants in the pants game **<br>裤子里的蚂蚁游戏 | 2.09% |  |  | 3,140 | 159 | 4 | 0 | 250 | $0.35 | 16.32 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GC43CR19, B0GKFSMPTP, B0GD11KHJB, B0DZFGJQ5N, B0DZML5ZPH）

1. **zuru bunch o balloons ** — zuru 束 o 气球
2. **backyard water fun ** — 后院玩水
3. **32 panel hacky sack ** — 32面袋球
4. **burger mania game ** — 汉堡狂热游戏
5. **giant tower stack game ** — 巨型塔堆叠游戏
6. **water fun for kids outdoor ** — 孩子们在户外玩水
7. **giant water balloon ** — 巨大的水气球
8. **little tikes outdoor toys ** — little tikes 户外玩具
9. **basketball hoop for kids 1-3 ** — 1-3岁儿童篮球架
10. **ants in the pants game ** — 裤子里的蚂蚁游戏
11. **little tikes water table ** — little tikes 地下水位
12. **adult yard games ** — 成人院子游戏
13. **slingshot for kids ** — 儿童弹弓
14. **baby water table ** — 婴儿饮水台
15. **water slide for kids ** — 儿童水滑梯
16. **2 year old boy toys ** — 2岁男孩的玩具
17. **yard games for family ** — 适合家庭的院子游戏
18. **juguetes para niños 1 a 2 años ** — juguetes para niños 1 a 2 años
19. **toddler basketball hoop set ** — 幼儿篮球架套装
20. **toddler outdoor playset ** — 幼儿户外玩具套装

---

# Squirt Guns 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GQ2BQQDS`, `B0H13XKQ27`, `B0GH71NJPF`, `B0GJSTS72K`, `B0BPH8P5D9`, `B0BKVHW3CZ`, `B0DRVGDYGK`, `B0GDG4T6L8`, `B0F3NVTP3J`, `B0DRY4N6MG`, `B09TZVCD7R`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **orbeez gel gun **<br>orbeez 凝胶枪 | 10.79% |  |  | 59,008 | 861 | 20 | 0 | 109 | $0.48 | 40.79 |
| 2 | **orby gun **<br>奥比枪 | 6.69% |  |  | 35,039 | 413 | 10 | 8 | 93 | $0.42 | 36.69 |
| 3 | **splat gun **<br>喷枪 | 5.83% |  |  | 43,110 | 844 | 20 | 0 | 156 | $0.33 | 35.83 |
| 4 | **spyra 4 **<br>Spyra 4 | 10.59% |  |  | 10,692 | 104 | 3 | 3 | 51 | $0.55 | 35.79 |
| 5 | **gel blaster gun **<br>凝胶爆破枪 | 3.09% |  |  | 42,896 | 626 | 15 | 0 | 461 | $0.44 | 33.09 |
| 6 | **water squirter for kids **<br>儿童喷水器 | 2.59% |  |  | 16,251 | 659 | 15 | 3 | 605 | $0.71 | 32.59 |
| 7 | **nerf water gun **<br>nerf水枪 | 3.15% |  |  | 9,375 | 246 | 6 | 0 | 331 | $0.70 | 31.9 |
| 8 | **toy guns **<br>玩具枪 | 1.79% |  |  | 27,764 | 211 | 5 | 3 | 11,772 | $0.46 | 31.79 |
| 9 | **orbeez gun **<br>orbeez枪 | 1.69% |  |  | 20,859 | 273 | 7 | 0 | 160 | $0.58 | 31.69 |
| 10 | **gel blaster pistol **<br>凝胶爆破手枪 | 1.50% |  |  | 20,656 | 212 | 5 | 0 | 3,358 | $0.32 | 31.5 |
| 11 | **splat ball gun **<br>泼球枪 | 1.44% |  |  | 11,595 | 485 | 12 | 1 | 112 | $0.35 | 31.44 |
| 12 | **water pistol **<br>水枪 | 1.80% |  |  | 8,976 | 376 | 9 | 14 | 5,548 | $0.45 | 29.75 |
| 13 | **water shooters **<br>水射手 | 4.05% |  |  | 7,454 | 298 | 7 | 2 | 545 | $0.54 | 28.96 |
| 14 | **orbeez gel gun ammo **<br>Orbeez胶枪弹药 | 1.84% |  |  | 8,067 | 339 | 8 | 0 | 46 | $0.37 | 27.97 |
| 15 | **semi automatic slingshot **<br>半自动弹弓 | 1.84% |  |  | 11,518 | 87 | 3 | 0 | 177 | $0.37 | 26.19 |
| 16 | **x shot water gun **<br>x 水枪 | 2.99% |  |  | 11,992 | 61 | 2 | 0 | 269 | $0.73 | 26.04 |
| 17 | **water blasters **<br>喷水器 | 1.90% |  |  | 8,700 | 94 | 3 | 5 | 5,059 | $0.72 | 24.0 |
| 18 | **orbeez gunz **<br>奥比兹枪 | 1.55% |  |  | 8,313 | 90 | 3 | 0 | 110 | $0.39 | 22.68 |
| 19 | **orbeez for gel blasters **<br>用于凝胶喷射器的 ORBEEZ | 1.39% |  |  | 5,463 | 211 | 5 | 0 | 88 | $0.47 | 22.32 |
| 20 | **￼orby gun **<br>奥比枪 | 2.05% |  |  | 5,529 | 54 | 2 | 0 | 143 | $0.42 | 15.81 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GQ2BQQDS, B0H13XKQ27, B0GH71NJPF, B0GJSTS72K, B0BPH8P5D9, B0BKVHW3CZ, B0DRVGDYGK, B0GDG4T6L8, B0F3NVTP3J, B0DRY4N6MG, B09TZVCD7R）

1. **orbeez gel gun ** — orbeez 凝胶枪
2. **spyra 4 ** — Spyra 4
3. **orby gun ** — 奥比枪
4. **splat gun ** — 喷枪
5. **water shooters ** — 水射手
6. **nerf water gun ** — nerf水枪
7. **gel blaster gun ** — 凝胶爆破枪
8. **x shot water gun ** — x 水枪
9. **water squirter for kids ** — 儿童喷水器
10. **￼orby gun ** — 奥比枪
11. **water blasters ** — 喷水器
12. **semi automatic slingshot ** — 半自动弹弓
13. **orbeez gel gun ammo ** — Orbeez胶枪弹药
14. **water pistol ** — 水枪
15. **toy guns ** — 玩具枪
16. **orbeez gun ** — orbeez枪
17. **orbeez gunz ** — 奥比兹枪
18. **gel blaster pistol ** — 凝胶爆破手枪
19. **splat ball gun ** — 泼球枪
20. **orbeez for gel blasters ** — 用于凝胶喷射器的 ORBEEZ

---

# Drip Irrigation Kits 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GJZXWSK6`, `B0G1473Y3J`, `B0G64FH1N1`, `B0GHQXCCZ2`, `B0FMXHDBHK`, `B0CYG23NZR`, `B0GF7SNVMD`, `B0F1T5QBP8`, `B0C7MGZCJK`, `B0DY7X7M4V`, `B0D2J1KMC9`, `B0GH6XXK1F`, `B0BNS5VR78`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **13** 个，过滤后保留 **13** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **solar irrigation system **<br>太阳能灌溉系统 | 78.59% |  |  | 4,876 | 137 | 4 | 6 | 461 | $0.63 | 46.6 |
| 2 | **plant waterer **<br>植物浇灌器 | 4.10% |  |  | 11,938 | 337 | 8 | 7 | 2,290 | $0.42 | 34.1 |
| 3 | **irrigation drippers **<br>灌溉滴头 | - |  |  | 13,018 | 553 | 13 | 9 | 2,954 | $0.72 | 30.0 |
| 4 | **blumat watering system **<br>布鲁马特浇水系统 | 4.66% |  |  | 6,234 | 256 | 6 | 2 | 209 | $0.55 | 27.13 |
| 5 | **sprinkler for garden **<br>花园洒水器 | - |  |  | 13,026 | 141 | 4 | 0 | 14,896 | $0.74 | 27.05 |
| 6 | **flower sprinkler **<br>花洒 | - |  |  | 13,196 | 106 | 3 | 8 | 3,442 | $0.46 | 25.3 |
| 7 | **pollinator watering station **<br>授粉者饮水站 | 0.14% |  |  | 6,314 | 179 | 5 | 10 | 208 | $0.65 | 21.72 |
| 8 | **drip acclimation kit **<br>滴灌适应套件 | - |  |  | 4,535 | 255 | 6 | 10 | 100 | $0.32 | 19.07 |
| 9 | **vegetable garden supplies **<br>菜园用品 | 0.23% |  |  | 6,867 | 94 | 3 | 0 | 553 | $0.53 | 18.66 |
| 10 | **hanging plant waterer **<br>悬挂式植物浇水器 | 4.18% |  |  | 1,958 | 161 | 4 | 5 | 1,029 | $0.62 | 16.15 |
| 11 | **waterer for potted plants **<br>盆栽浇水器 | 3.73% |  |  | 1,683 | 138 | 4 | 0 | 1,521 | $0.47 | 14.0 |
| 12 | **drippers for drip irrigation **<br>滴灌用滴头 | - |  |  | 3,759 | 110 | 3 | 2 | 2,126 | $0.72 | 13.02 |
| 13 | **tree diaper **<br>树尿布 | 4.36% |  |  | 1,743 | 81 | 2 | 0 | 199 | $0.37 | 11.9 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GJZXWSK6, B0G1473Y3J, B0G64FH1N1, B0GHQXCCZ2, B0FMXHDBHK, B0CYG23NZR, B0GF7SNVMD, B0F1T5QBP8, B0C7MGZCJK, B0DY7X7M4V, B0D2J1KMC9, B0GH6XXK1F, B0BNS5VR78）

1. **solar irrigation system ** — 太阳能灌溉系统
2. **blumat watering system ** — 布鲁马特浇水系统
3. **tree diaper ** — 树尿布
4. **hanging plant waterer ** — 悬挂式植物浇水器
5. **plant waterer ** — 植物浇灌器
6. **waterer for potted plants ** — 盆栽浇水器
7. **vegetable garden supplies ** — 菜园用品
8. **pollinator watering station ** — 授粉者饮水站
9. **sprinkler for garden ** — 花园洒水器
10. **irrigation drippers ** — 灌溉滴头
11. **flower sprinkler ** — 花洒
12. **drippers for drip irrigation ** — 滴灌用滴头
13. **drip acclimation kit ** — 滴灌适应套件

---

# Bread Proofing Baskets 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0G94RRF26`, `B0F6CJX4BW`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **3** 个，过滤后保留 **3** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **banetons **<br>宴席 | 95.60% |  |  | 2,733 | 158 | 4 | 0 | 865 | $0.79 | 43.37 |
| 2 | **proofing bowl **<br>打样碗 | 4.40% |  |  | 2,275 | 217 | 5 | 14 | 2,300 | $0.69 | 18.95 |
| 3 | **mini sourdough banneton basket **<br>迷你酸面包篮 | - |  |  | 1,331 | 76 | 2 | 0 | 420 | $0.74 | 6.46 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0G94RRF26, B0F6CJX4BW）

1. **banetons ** — 宴席
2. **proofing bowl ** — 打样碗
3. **mini sourdough banneton basket ** — 迷你酸面包篮

---

# Ultrasonic Repellers 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GXK8D82J`, `B0FV3R9L2R`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **rodent repellent **<br>驱鼠剂 | 71.97% |  |  | 130,126 | 6,857 | 156 | 35 | 7,696 | $1.56 | 60.0 |
| 2 | **rodent repellent for car engines **<br>汽车发动机驱鼠剂 | 7.79% |  |  | 38,783 | 3,319 | 76 | 11 | 1,048 | -- | 37.79 |
| 3 | **sofyre mouse repellent pouches **<br>sofyre 鼠类驱赶袋 | 1.38% |  |  | 43,651 | 331 | 8 | 0 | 196 | $1.37 | 31.38 |
| 4 | **squirrel repellent **<br>驱赶松鼠 | 0.65% |  |  | 139,618 | 7,818 | 178 | 23 | 2,433 | $2.22 | 30.65 |
| 5 | **mouse repellent ultrasonic plug in **<br>驱鼠超声波插件 | 0.93% |  |  | 9,284 | 863 | 20 | 1 | 548 | -- | 29.5 |
| 6 | **ultrasonic rodent repeller **<br>超声波驱鼠器 | 1.68% |  |  | 6,001 | 436 | 10 | 2 | 1,713 | $1.78 | 23.68 |
| 7 | **rodent repellent plug in **<br>灭鼠插件 | 1.56% |  |  | 4,910 | 1,199 | 28 | 0 | 623 | $2.07 | 21.38 |
| 8 | **rodent repellent for cars **<br>汽车驱鼠剂 | 1.40% |  |  | 4,182 | 620 | 15 | 2 | 607 | $0.84 | 19.76 |
| 9 | **electronic rodent repellent devices **<br>电子驱鼠器 | 0.84% |  |  | 3,070 | 292 | 7 | 0 | 959 | -- | 16.98 |
| 10 | **rat repellent for car **<br>车用驱鼠剂 | 0.94% |  |  | 2,931 | 237 | 6 | 3 | 527 | $0.79 | 16.8 |
| 11 | **mouse repellent for cars **<br>汽车驱鼠剂 | 0.67% |  |  | 2,879 | 438 | 10 | 1 | 678 | $1.55 | 16.43 |
| 12 | **mice repellent for cars **<br>汽车驱鼠剂 | 0.64% |  |  | 2,396 | 492 | 12 | 0 | 895 | $1.44 | 15.43 |
| 13 | **ultrasonic rodent repellent **<br>超声波驱鼠剂 | 0.66% |  |  | 2,302 | 204 | 5 | 5 | 1,674 | $1.99 | 15.26 |
| 14 | **rodent deterrent for cars **<br>汽车灭鼠剂 | 0.86% |  |  | 2,482 | 179 | 5 | 0 | 612 | $0.87 | 14.77 |
| 15 | **mice repellent ultrasonic **<br>超声波驱鼠器 | 0.56% |  |  | 2,063 | 354 | 9 | 0 | 929 | $2.25 | 14.69 |
| 16 | **mouse deterrent ultrasonic **<br>老鼠威慑超声波 | 0.51% |  |  | 1,373 | 202 | 5 | 1 | 879 | $2.28 | 13.26 |
| 17 | **osmo repelmax mouse repel **<br>Osmo 鼠类驱避剂 | 0.65% |  |  | 2,918 | 33 | 1 | 0 | 192 | -- | 8.14 |
| 18 | **osmo repelmax mouse repellent **<br>Osmo RepelMax 鼠类驱避剂 | 3.13% |  |  | 1,773 | 15 | 1 | 0 | 316 | -- | 7.43 |
| 19 | **plug in rodent repeller ultrasonic indoor **<br>插入式室内超声波驱鼠器 | 0.51% |  |  | 1,847 | 11 | 1 | 0 | 594 | -- | 4.75 |
| 20 | **ardito **<br>ardito | 0.61% |  |  | 140 | 1 | 1 | 10 | 37 | $2.80 | 0.94 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GXK8D82J, B0FV3R9L2R）

1. **rodent repellent ** — 驱鼠剂
2. **rodent repellent for car engines ** — 汽车发动机驱鼠剂
3. **osmo repelmax mouse repellent ** — Osmo RepelMax 鼠类驱避剂
4. **ultrasonic rodent repeller ** — 超声波驱鼠器
5. **rodent repellent plug in ** — 灭鼠插件
6. **rodent repellent for cars ** — 汽车驱鼠剂
7. **sofyre mouse repellent pouches ** — sofyre 鼠类驱赶袋
8. **rat repellent for car ** — 车用驱鼠剂
9. **mouse repellent ultrasonic plug in ** — 驱鼠超声波插件
10. **rodent deterrent for cars ** — 汽车灭鼠剂
11. **electronic rodent repellent devices ** — 电子驱鼠器
12. **mouse repellent for cars ** — 汽车驱鼠剂
13. **ultrasonic rodent repellent ** — 超声波驱鼠剂
14. **osmo repelmax mouse repel ** — Osmo 鼠类驱避剂
15. **squirrel repellent ** — 驱赶松鼠
16. **mice repellent for cars ** — 汽车驱鼠剂
17. **ardito ** — ardito
18. **mice repellent ultrasonic ** — 超声波驱鼠器
19. **plug in rodent repeller ultrasonic indoor ** — 插入式室内超声波驱鼠器
20. **mouse deterrent ultrasonic ** — 老鼠威慑超声波

---

# Decorative Boxes 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B0GRC76TKN`, `B0GKXY24FG`, `B0FH4CGRG6`, `B0FN46S75Q`, `B0G6391R1J`, `B0FLW9HLWH`, `B0DX841J37`, `B0CJ1XRT2Z`, `B0CGHZ1DDM`, `B0DG2J8D21`, `B0FQJ8JPFM`, `B0F4D1JVBP`, `B0G31WNCCS`, `B0DMN38XJM`, `B0FQ84PMTP`, `B0DX23QLV3`, `B0GT8CF7MB`, `B0C8HDZCTS`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **20** 个，过滤后保留 **20** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**可能存在**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **fake books **<br>假书 | 17.70% |  |  | 30,026 | 438 | 10 | 15 | 5,119 | $0.32 | 47.7 |
| 2 | **libros decorativos para sala **<br>客厅的装饰性书籍 | 14.91% |  |  | 24,379 | 234 | 6 | 0 | 387 | $0.44 | 44.91 |
| 3 | **faux books for decoration **<br>装饰用假书 | 8.38% |  |  | 13,842 | 181 | 5 | 6 | 3,036 | $0.48 | 37.43 |
| 4 | **smores station AC**<br>斯莫尔斯站 | 9.05% |  |  | 8,988 | 299 | 7 | 9 | 238 | $0.44 | 37.03 |
| 5 | **treasure chest box **<br>宝箱 | 3.24% |  |  | 7,901 | 379 | 9 | 12 | 4,513 | $0.32 | 29.04 |
| 6 | **smore kit **<br>烟熏套件 | 5.60% |  |  | 6,119 | 229 | 6 | 1 | 300 | $0.64 | 27.84 |
| 7 | **decorative boxes with lids **<br>带盖子的装饰盒 | 1.42% |  |  | 12,545 | 71 | 2 | 2 | 800 | $0.32 | 24.97 |
| 8 | **small treasure chest **<br>小宝箱 | 2.11% |  |  | 5,182 | 370 | 9 | 2 | 8,631 | $0.35 | 22.47 |
| 9 | **smores box **<br>烟盒 | 5.54% |  |  | 4,402 | 125 | 3 | 4 | 451 | $0.48 | 20.59 |
| 10 | **wooden box with hinged lid **<br>带铰链盖的木箱 | 2.51% |  |  | 6,029 | 102 | 3 | 12 | 4,528 | $0.37 | 19.67 |
| 11 | **s'mores kit **<br>s&#39;mores 套装 | 3.57% |  |  | 2,401 | 336 | 8 | 8 | 238 | $0.47 | 18.37 |
| 12 | **faux book storage box **<br>仿书收纳盒 | 1.66% |  |  | 2,985 | 185 | 5 | 7 | 2,879 | $0.47 | 16.88 |
| 13 | **large treasure chest **<br>大宝箱 | 2.02% |  |  | 3,580 | 135 | 4 | 2 | 8,188 | $0.32 | 15.93 |
| 14 | **smore maker **<br>烟雾机 | 2.07% |  |  | 4,049 | 110 | 3 | 2 | 226 | $0.72 | 15.67 |
| 15 | **brown decor **<br>棕色装饰 | 1.67% |  |  | 3,969 | 104 | 3 | 0 | 348 | $0.32 | 14.81 |
| 16 | **smores kits **<br>烟熏套装 | 2.93% |  |  | 2,817 | 92 | 3 | 2 | 351 | $0.60 | 13.16 |
| 17 | **smores kit for fire pit AC**<br>火坑烟熏套件 | 3.55% |  |  | 2,849 | 78 | 2 | 6 | 346 | $0.36 | 13.15 |
| 18 | **designer books decor set **<br>设计师书籍装饰套装 | 1.82% |  |  | 4,139 | 56 | 2 | 5 | 1,005 | $0.32 | 12.9 |
| 19 | **book boxes decorative **<br>书盒装饰 | 2.35% |  |  | 2,728 | 74 | 2 | 0 | 281 | $0.48 | 11.51 |
| 20 | **wooden box with lid **<br>带盖木盒 | 1.27% |  |  | 2,736 | 70 | 2 | 1 | 12,467 | $0.33 | 10.24 |

## 免费套餐当前可见原始关键词（查询 ASIN: B0GRC76TKN, B0GKXY24FG, B0FH4CGRG6, B0FN46S75Q, B0G6391R1J, B0FLW9HLWH, B0DX841J37, B0CJ1XRT2Z, B0CGHZ1DDM, B0DG2J8D21, B0FQJ8JPFM, B0F4D1JVBP, B0G31WNCCS, B0DMN38XJM, B0FQ84PMTP, B0DX23QLV3, B0GT8CF7MB, B0C8HDZCTS）

1. **fake books ** — 假书
2. **libros decorativos para sala ** — 客厅的装饰性书籍
3. **smores station AC** — 斯莫尔斯站
4. **faux books for decoration ** — 装饰用假书
5. **smore kit ** — 烟熏套件
6. **smores box ** — 烟盒
7. **s'mores kit ** — s&#39;mores 套装
8. **smores kit for fire pit AC** — 火坑烟熏套件
9. **treasure chest box ** — 宝箱
10. **smores kits ** — 烟熏套装
11. **wooden box with hinged lid ** — 带铰链盖的木箱
12. **book boxes decorative ** — 书盒装饰
13. **small treasure chest ** — 小宝箱
14. **smore maker ** — 烟雾机
15. **large treasure chest ** — 大宝箱
16. **designer books decor set ** — 设计师书籍装饰套装
17. **brown decor ** — 棕色装饰
18. **faux book storage box ** — 仿书收纳盒
19. **decorative boxes with lids ** — 带盖子的装饰盒
20. **wooden box with lid ** — 带盖木盒

---

# Pool & Deck Repair Products 拓展流量词候选 (2026-06-14)

> 查询 ASIN：`B00Q2L3QCU`, `B0D5DMD84K`, `B00Q2L3S1O`
> 来源：卖家精灵拓展流量词（批量多 ASIN 查询）。排序分数综合流量占比、搜索量、购买量和自然排名，
> 用于生成广告测试候选，不代表应直接使用高竞价投放。
> 筛选参数：`{"min_searches": 1000, "min_purchases": 50, "max_organic_rank": 100, "max_spr": 20, "max_title_density": 15, "max_products": 15000, "max_ppc_bid": 1.0, "allowed_traffic_types": ["自然搜索词", "广告流量词"], "excluded_keywords": ["hudson", "jobe", "industries", "nr3xldu"], "require_numeric_searches": true}`
> 原始关键词 **9** 个，过滤后保留 **9** 个。
> 抓取完整性：页面可见 **0** 个；页面总数提示 **未识别**；下一页 **不可用或未识别**；免费套餐截断风险：**未检测到**。
> 指标可用性：**不可用**。若指标不可用，过滤后 0 条不能解释为没有关键词机会。

| # | 关键词 | 流量占比 | 类型 | 自然排名 | 月搜索量 | 月购买量 | SPR | 标题密度 | 需供比 / 商品数 | PPC 竞价 | 分数 |
|---:|---|---:|---|---|---:|---:|---:|---:|---|---|---:|
| 1 | **pool patches **<br>池补丁 | 29.15% |  |  | 7,117 | 286 | 7 | 3 | 4,531 | $0.35 | 53.38 |
| 2 | **pool tile adhesive **<br>泳池瓷砖粘合剂 | 31.47% |  |  | 4,568 | 584 | 14 | 4 | 697 | $0.32 | 49.14 |
| 3 | **pool patch kit **<br>泳池补丁套件 | 19.52% |  |  | 4,881 | 318 | 8 | 0 | 1,201 | $0.44 | 39.28 |
| 4 | **pool liner patch kit **<br>泳池衬垫贴片套件 | - |  |  | 14,198 | 844 | 20 | 2 | 1,373 | $0.42 | 30.0 |
| 5 | **pool repair kit **<br>泳池修理包 | 6.59% |  |  | 6,181 | 296 | 7 | 0 | 8,359 | $0.35 | 28.95 |
| 6 | **thinset mortar for tile **<br>薄型瓷砖砂浆 | 13.28% |  |  | 2,050 | 60 | 2 | 0 | 480 | $0.54 | 20.38 |
| 7 | **pool cover patch **<br>游泳池盖补丁 | - |  |  | 1,341 | 291 | 7 | 11 | 793 | $0.62 | 12.68 |
| 8 | **muscle bound tile adhesive **<br>肌肉结合瓷砖粘合剂 | - |  |  | 1,426 | 172 | 4 | 0 | 138 | $0.56 | 11.45 |
| 9 | **tile adhesive glue **<br>瓷砖胶 | - |  |  | 1,137 | 77 | 2 | 0 | 10,677 | $0.61 | 6.12 |

## 免费套餐当前可见原始关键词（查询 ASIN: B00Q2L3QCU, B0D5DMD84K, B00Q2L3S1O）

1. **pool tile adhesive ** — 泳池瓷砖粘合剂
2. **pool patches ** — 池补丁
3. **pool patch kit ** — 泳池补丁套件
4. **thinset mortar for tile ** — 薄型瓷砖砂浆
5. **pool repair kit ** — 泳池修理包
6. **tile adhesive glue ** — 瓷砖胶
7. **pool liner patch kit ** — 泳池衬垫贴片套件
8. **pool cover patch ** — 游泳池盖补丁
9. **muscle bound tile adhesive ** — 肌肉结合瓷砖粘合剂
