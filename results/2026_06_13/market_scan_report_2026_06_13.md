# 亚马逊选市场扫描与评估报告 (2026-06-13)

> [!IMPORTANT]
> 本报告基于配置文件 `scripts/market_config.json` 中设定的过滤与风控规则进行生成。今日共分析了 **30** 个符合基本条件的子类目，其中最终筛选出 **9** 个适合新手的 🟢 绿色推荐赛道。
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
