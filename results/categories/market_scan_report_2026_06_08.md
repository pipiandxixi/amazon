# 亚马逊选市场扫描与评估报告 (2026-06-08)

> [!IMPORTANT]
> 本报告基于配置文件 `scripts/market_config.json` 中设定的过滤与风控规则进行生成。今日共分析了 **218** 个符合基本条件的子类目，其中最终筛选出 **78** 个适合新手的 🟢 绿色推荐赛道。
> **数量审计**：当前候选类目有 134 个，超过目标上限 15。建议提高基础过滤门槛或收紧黄色/绿色风控规则，而不是截断为固定 Top-K。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **78** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **56** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **84** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Swing Trainers** | 室内练习器 | $38.65 | 444 | 0.70 lbs | 4.37% | 59.9% | 67.0% |
| 2 | **Bread Proofing Baskets** | 面包发酵篮 | $27.88 | 570 | 1.88 lbs | 4.09% | 53.9% | 66.0% |
| 3 | **Lighting Products** | 水底灯 | $49.41 | 475 | 1.70 lbs | 6.75% | 51.5% | 76.0% |
| 4 | **Shilajit** | Shilajit | $32.19 | 714 | 0.40 lbs | 0.34% | 63.2% | 41.0% |
| 5 | **Decorative Boxes** | 装饰盒 | $24.84 | 680 | 1.66 lbs | 7.91% | 49.1% | 67.0% |
| 6 | **Nozzles** | 喷嘴 | $26.98 | 497 | 0.44 lbs | 2.63% | 54.9% | 72.0% |
| 7 | **Cups** | 杯子 | $21.43 | 487 | 1.31 lbs | 3.95% | 56.2% | 65.0% |
| 8 | **Tap Extractors** | 分接抽水机 | $27.16 | 796 | 1.42 lbs | 4.89% | 60.5% | 77.0% |
| 9 | **Herb & Spice Mills** | 草本植物 | $22.71 | 759 | 0.57 lbs | 3.55% | 59.6% | 54.0% |
| 10 | **Dash Covers** | 仪表盘罩 | $30.26 | 787 | 1.20 lbs | 6.55% | 62.9% | 89.0% |
| 11 | **Bladder Control Devices** | 膀胱控制设备 | $31.65 | 499 | 0.56 lbs | 3.9% | 46.8% | 60.0% |
| 12 | **Feeders** | 喂食器 | $23.98 | 572 | 1.08 lbs | 5.44% | 48.0% | 83.0% |
| 13 | **Emblems** | 车标 | $20.84 | 582 | 0.12 lbs | 4.71% | 46.5% | 55.0% |
| 14 | **Plaques & Wall Art** | 装饰墙 | $20.35 | 619 | 1.04 lbs | 2.89% | 46.1% | 88.0% |
| 15 | **Electrical System Tools** | 电气系统工具 | $31.23 | 489 | 1.00 lbs | 2.38% | 44.9% | 81.0% |
| 16 | **Brake System Bleeding Tools** | 刹车排气 | $27.56 | 474 | 1.58 lbs | 4.69% | 50.4% | 82.0% |
| 17 | **Kava Kava** | 卡瓦胡椒 | $35.87 | 295 | 0.65 lbs | 0.39% | 63.4% | 14.0% |
| 18 | **Hands Free Leashes** | 免手持牵绳 | $23.90 | 769 | 0.74 lbs | 6.44% | 64.8% | 50.0% |
| 19 | **Honey Jars** | 蜂蜜罐子 | $21.74 | 662 | 1.83 lbs | 5.4% | 52.4% | 75.0% |
| 20 | **Trophies** | 奖杯 | $24.41 | 291 | 0.97 lbs | 2.59% | 46.0% | 54.0% |
| 21 | **Insulin Injectors** | 胰岛素注射器 | $24.29 | 479 | 0.47 lbs | 1.5% | 64.0% | 38.0% |
| 22 | **Oolong** | 乌龙 | $20.14 | 464 | 0.46 lbs | 0.26% | 59.7% | 49.0% |
| 23 | **Headlights** | 车头灯 | $33.78 | 557 | 0.47 lbs | 5.21% | 57.8% | 71.0% |
| 24 | **Tattoo Kits** | 纹身套装 | $32.80 | 530 | 1.52 lbs | 2.09% | 63.3% | 71.0% |
| 25 | **Network & Cable Testers** | 网络 | $119.03 | 426 | 0.61 lbs | 5.23% | 64.5% | 70.0% |
| 26 | **Drill Bits** | 钻头 | $26.43 | 264 | 0.98 lbs | 2.68% | 52.9% | 74.0% |
| 27 | **Cookbook Stands** | 菜谱架 | $24.65 | 712 | 1.87 lbs | 6.17% | 54.7% | 66.0% |
| 28 | **Countersink Drill Bits** | 沉孔钻头 | $21.48 | 588 | 0.49 lbs | 1.85% | 53.8% | 64.0% |
| 29 | **Tie-Downs** | 栓系器具 | $26.48 | 548 | 1.60 lbs | 3.74% | 59.2% | 51.0% |
| 30 | **Exterior Lighting** | 外部照明 | $23.81 | 523 | 0.77 lbs | 4.66% | 52.5% | 67.0% |
| 31 | **Deburring Cutters** | 去毛刺刀具 | $22.36 | 370 | 0.47 lbs | 1.93% | 63.4% | 59.0% |
| 32 | **Bar Tools & Drinkware** | 酒吧工具 | $25.94 | 365 | 1.27 lbs | 5.44% | 53.4% | 61.0% |
| 33 | **Wood Burning Tools** | 木材燃烧工具 | $31.55 | 567 | 1.07 lbs | 4.0% | 54.0% | 80.0% |
| 34 | **Sound Therapy** | 声音疗法 | $54.87 | 254 | 0.96 lbs | 6.32% | 45.5% | 75.0% |
| 35 | **Pond Lights** | 池塘灯 | $46.35 | 235 | 1.53 lbs | 6.15% | 64.6% | 68.0% |
| 36 | **Paint Roller Extension Poles** | 油漆滚筒加长杆 | $36.17 | 354 | 2.00 lbs | 4.55% | 56.1% | 65.0% |
| 37 | **Angle Grinder Wheels** | 角磨机砂轮 | $23.63 | 165 | 1.54 lbs | 2.41% | 58.2% | 75.0% |
| 38 | **Scoreboards & Timers** | 记分牌和计时器 | $52.27 | 352 | 1.54 lbs | 5.13% | 54.1% | 72.0% |
| 39 | **Brake Controls** | 制动控制装置 | $87.23 | 308 | 1.22 lbs | 6.05% | 59.1% | 56.0% |
| 40 | **Seat Covers** | 摩托车座套 | $31.10 | 316 | 1.15 lbs | 5.29% | 50.3% | 88.0% |
| 41 | **Float Valves** | 浮阀 | $20.85 | 183 | 0.67 lbs | 4.44% | 43.0% | 63.0% |
| 42 | **Weaving Looms** | 织机 | $21.49 | 311 | 1.01 lbs | 3.33% | 57.5% | 66.0% |
| 43 | **Leak Detection Tools** | 泄漏检测工具 | $100.92 | 154 | 1.45 lbs | 4.3% | 53.9% | 47.0% |
| 44 | **Optics Accessories** | 光学配件 | $32.88 | 354 | 0.20 lbs | 5.63% | 52.5% | 44.0% |
| 45 | **Bait Traps** | 诱饵陷阱 | $26.88 | 284 | 1.68 lbs | 3.31% | 60.9% | 55.0% |
| 46 | **Fly Tying Equipment** | 绑蝇设备 | $22.02 | 478 | 0.30 lbs | 2.84% | 62.7% | 53.0% |
| 47 | **Flags** | 标志 | $23.28 | 223 | 0.60 lbs | 2.61% | 62.7% | 54.0% |
| 48 | **Growth Charts** | 身高墙贴 | $20.12 | 416 | 0.80 lbs | 3.72% | 47.4% | 66.0% |
| 49 | **Tortilla Servers** | 玉米饼服务员 | $21.25 | 454 | 1.57 lbs | 6.26% | 58.1% | 38.0% |
| 50 | **Devotional Candles** | 祈祷蜡烛 | $25.95 | 191 | 1.74 lbs | 4.08% | 61.1% | 56.0% |
| 51 | **Trim** | 装饰 | $27.56 | 248 | 0.27 lbs | 2.44% | 61.9% | 64.0% |
| 52 | **Tools** | 工具 | $33.49 | 187 | 1.44 lbs | 3.64% | 46.3% | 64.0% |
| 53 | **License Plate Frames** | 摩托车牌照架 | $20.31 | 146 | 0.57 lbs | 4.18% | 54.8% | 78.0% |
| 54 | **Gutters** | 排水沟 | $24.76 | 136 | 1.75 lbs | 5.02% | 53.2% | 67.0% |
| 55 | **Fuel System** | 燃油系统 | $24.65 | 98 | 0.65 lbs | 4.31% | 49.5% | 76.0% |
| 56 | **Car Rack Parts & Accessories** | 汽车货架零件和配件 | $45.21 | 240 | 1.33 lbs | 6.72% | 46.9% | 51.0% |
| 57 | **Serveware** | 碗碟 | $22.08 | 429 | 1.49 lbs | 5.33% | 57.7% | 58.0% |
| 58 | **Collectible Vehicles** | 交通工具摆件 | $23.98 | 213 | 0.89 lbs | 5.81% | 63.7% | 83.0% |
| 59 | **3D Printer Extruders** | 3D打印机挤出机 | $27.77 | 157 | 0.18 lbs | 4.99% | 58.8% | 80.0% |
| 60 | **Mailbox Hardware** | 信箱硬件 | $21.44 | 201 | 1.11 lbs | 7.65% | 55.5% | 65.0% |
| 61 | **Grill Lighting** | 点火器 | $37.59 | 607 | 1.29 lbs | 5.43% | 53.9% | 58.0% |
| 62 | **Fuel** | 燃油表 | $31.69 | 107 | 0.38 lbs | 4.87% | 51.3% | 68.0% |
| 63 | **Deviled Egg Plates** | 咸蛋盘 | $22.00 | 349 | 1.87 lbs | 5.01% | 59.1% | 61.0% |
| 64 | **Aprons** | 围裙 | $22.00 | 72 | 0.75 lbs | 3.04% | 58.8% | 77.0% |
| 65 | **Nail Pullers** | 羊角起钉钳 | $24.20 | 371 | 1.20 lbs | 2.27% | 61.9% | 55.0% |
| 66 | **Cheese Knives** | 奶酪刀 | $21.33 | 542 | 0.65 lbs | 4.02% | 47.6% | 48.0% |
| 67 | **Angle** | 角规 | $25.14 | 386 | 0.56 lbs | 2.9% | 60.6% | 64.0% |
| 68 | **Card Playing** | 纸牌游戏 | $20.06 | 198 | 0.78 lbs | 4.78% | 58.9% | 73.0% |
| 69 | **Brazing Rods** | 钎杆 | $37.36 | 158 | 0.66 lbs | 2.03% | 62.7% | 53.0% |
| 70 | **Fixed-Blade Knives** | 固定刀刃的刀具 | $46.05 | 714 | 0.61 lbs | 3.09% | 58.3% | 34.0% |
| 71 | **Knitting Looms & Boards** | 编织机、织布机 | $30.48 | 453 | 1.77 lbs | 5.9% | 49.9% | 63.0% |
| 72 | **Sheets** | 桌子 | $26.11 | 89 | 1.94 lbs | 7.07% | 53.8% | 76.0% |
| 73 | **Oil Pressure Tools** | 油压工具 | $28.75 | 123 | 1.03 lbs | 5.44% | 53.4% | 75.0% |
| 74 | **Carriers** | 外带用品 | $22.52 | 231 | 1.31 lbs | 6.02% | 53.4% | 71.0% |
| 75 | **Embroidery Storage** | 绣花收纳 | $23.36 | 194 | 1.37 lbs | 4.95% | 53.4% | 87.0% |
| 76 | **Hunting Dog Equipment** | 猎犬装备 | $32.83 | 278 | 0.95 lbs | 5.22% | 60.1% | 42.0% |
| 77 | **UV Phone Sterilizer Boxes** | 紫外线手机消毒盒 | $62.46 | 341 | 1.97 lbs | 7.51% | 63.7% | 27.0% |
| 78 | **Paper Craft Tools** | 纸工艺工具 | $35.65 | 306 | 1.78 lbs | 4.13% | 58.6% | 49.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Outdoor Statues** | 户外雕像 | $24.31 | 918 | 1.11 lbs | 2.98% | Reviews偏高 (>800) |
| 2 | **Liver Extracts** | 肝脏提取物 | $30.26 | 843 | 0.28 lbs | 0.31% | Reviews偏高 (>800) |
| 3 | **Squirt Guns** | 水枪 | $27.30 | 616 | 1.54 lbs | 3.93% | 谨慎认证类目路径 |
| 4 | **Grill Pads & Floor Mats** | 烤炉垫和地垫 | $22.02 | 976 | 1.73 lbs | 3.25% | Reviews偏高 (>800) |
| 5 | **Self-Watering Stakes** | 自浇水桩 | $22.73 | 840 | 1.49 lbs | 2.8% | Reviews偏高 (>800) |
| 6 | **Bread Knives** | 面包刀 | $20.57 | 998 | 0.81 lbs | 2.92% | Reviews偏高 (>800) |
| 7 | **Pool & Deck Repair Products** | 油漆及密封产品 | $32.75 | 679 | 2.41 lbs | 1.93% | 重量偏重 (>2.0 lbs) |
| 8 | **Fountains** | 喷泉 | $38.99 | 961 | 2.18 lbs | 4.78% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |
| 9 | **Trays & Bags** | 托盘、口袋 | $23.80 | 874 | 1.19 lbs | 9.42% | 退货率偏高 (>8.0%), Reviews偏高 (>800) |
| 10 | **Glasses & Goggles** | 眼镜和护目镜 | $22.58 | 887 | 0.23 lbs | 6.05% | Reviews偏高 (>800) |
| 11 | **Compressed Air Dusters** | 压缩除尘罐 | $34.09 | 349 | 0.87 lbs | 3.16% | 谨慎认证类目路径 |
| 12 | **Wind Spinners** | Wind Spinners | $31.21 | 472 | 2.48 lbs | 3.09% | 重量偏重 (>2.0 lbs) |
| 13 | **Birdhouses** | 鸟屋 | $30.93 | 620 | 2.16 lbs | 2.92% | 重量偏重 (>2.0 lbs) |
| 14 | **Batteries & Battery Chargers** | 电池和电池 | $23.82 | 482 | 0.96 lbs | 9.83% | 退货率偏高 (>8.0%), 带电/合规资质敏感关键字 |
| 15 | **Battery Switches** | 接线柱 | $21.79 | 602 | 0.66 lbs | 5.58% | 带电/合规资质敏感关键字 |
| 16 | **Paddleboard Accessories** | 冲浪板配件 | $53.14 | 345 | 2.42 lbs | 4.17% | 重量偏重 (>2.0 lbs) |
| 17 | **Poultry Fountains & Waterers** | 家禽自动喂水器和饮水器 | $26.74 | 615 | 2.19 lbs | 2.74% | 重量偏重 (>2.0 lbs) |
| 18 | **Replacement Sensors** | 更换传感器 | $46.99 | 999 | 0.47 lbs | 9.2% | 退货率偏高 (>8.0%), Reviews偏高 (>800) |
| 19 | **Neon Accent Lights** | 霓虹灯 | $27.14 | 944 | 0.83 lbs | 6.23% | Reviews偏高 (>800) |
| 20 | **Hand Tools** | 手动工具 | $22.88 | 945 | 1.46 lbs | 3.71% | Reviews偏高 (>800) |
| 21 | **Decorative Trays** | 装饰性托盘 | $23.03 | 492 | 1.52 lbs | 9.52% | 退货率偏高 (>8.0%) |
| 22 | **Trucks** | 卡车 | $67.37 | 868 | 2.48 lbs | 7.79% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800), 谨慎认证类目路径 |
| 23 | **Game Mats & Boards** | 游戏垫和游戏板 | $30.04 | 326 | 2.47 lbs | 7.5% | 重量偏重 (>2.0 lbs), 谨慎认证类目路径 |
| 24 | **Hand Exercisers** | 手部锻炼器具 | $30.96 | 806 | 1.35 lbs | 5.3% | Reviews偏高 (>800) |
| 25 | **Motion Detectors** | 生命探测器 | $38.80 | 899 | 0.71 lbs | 6.68% | Reviews偏高 (>800), 谨慎认证类目路径 |
| 26 | **Airbrush Sets** | 喷漆套装 | $51.53 | 901 | 2.50 lbs | 4.67% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |
| 27 | **Welding Helmets** | 焊接头盔 | $61.89 | 874 | 1.16 lbs | 3.46% | Reviews偏高 (>800) |
| 28 | **Alternative Medicine** | 替代药物 | $39.92 | 940 | 0.54 lbs | 2.58% | Reviews偏高 (>800) |
| 29 | **Handlebar Mounts** | Handlebar Mounts | $24.03 | 851 | 0.86 lbs | 5.37% | Reviews偏高 (>800) |
| 30 | **Boats** | 船 | $56.23 | 338 | 1.49 lbs | 6.03% | 谨慎认证类目路径 |
| 31 | **Remote & App Controlled Vehicle Batteries** | 遥控 | $35.60 | 455 | 0.38 lbs | 6.27% | 谨慎认证类目路径 |
| 32 | **Sewing Storage** | 缝纫用品收纳用品 | $23.93 | 929 | 2.12 lbs | 5.03% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |
| 33 | **Battery Chargers** | 电池充电器 | $30.92 | 379 | 0.50 lbs | 6.99% | 谨慎认证类目路径, 带电/合规资质敏感关键字 |
| 34 | **Flower Pressing** | 压花 | $22.48 | 175 | 1.69 lbs | 2.87% | 谨慎认证类目路径 |
| 35 | **Tea Storage Chests** | 茶叶罐 | $24.40 | 657 | 2.44 lbs | 6.54% | 重量偏重 (>2.0 lbs) |
| 36 | **Guitars & Strings** | 吉他 | $29.38 | 625 | 1.30 lbs | 5.12% | 谨慎认证类目路径 |
| 37 | **Rods** | 杆 | $20.66 | 278 | 2.23 lbs | 1.94% | 重量偏重 (>2.0 lbs) |
| 38 | **Airplanes & Jets** | 飞机 | $57.95 | 256 | 0.94 lbs | 8.46% | 退货率偏高 (>8.0%), 谨慎认证类目路径 |
| 39 | **Gaiters** | 护腿、护脚 | $33.12 | 386 | 0.68 lbs | 8.64% | 退货率偏高 (>8.0%) |
| 40 | **Cream Chargers & Whippers** | 奶油充电器 | $38.45 | 438 | 1.50 lbs | 2.63% | 带电/合规资质敏感关键字 |
| 41 | **Metric Inserts & Kits** | 米制刀片和套件 | $43.87 | 196 | 2.49 lbs | 5.6% | 重量偏重 (>2.0 lbs) |
| 42 | **Monoculars** | 单筒望远镜 | $72.01 | 620 | 0.74 lbs | 7.05% | 谨慎认证类目路径 |
| 43 | **Alarms & Anti-Theft** | 摩托车防盗器 | $32.91 | 705 | 0.89 lbs | 4.72% | 谨慎认证类目路径 |
| 44 | **Replacement Wheels** | 备用轮 | $24.50 | 298 | 2.05 lbs | 8.59% | 退货率偏高 (>8.0%), 重量偏重 (>2.0 lbs) |
| 45 | **Hair Dryer Stands** | 吹风机支架 | $20.87 | 219 | 1.34 lbs | 8.66% | 退货率偏高 (>8.0%) |
| 46 | **Bats** | 蝙蝠 | $34.37 | 344 | 2.19 lbs | 2.61% | 重量偏重 (>2.0 lbs) |
| 47 | **Bulb Planters** | 球茎栽植器 | $23.92 | 295 | 2.32 lbs | 2.9% | 重量偏重 (>2.0 lbs) |
| 48 | **Speedometers** | 车速里程表 | $46.69 | 173 | 0.39 lbs | 9.17% | 退货率偏高 (>8.0%) |
| 49 | **Food Processor Parts & Accessories** | 食物处理器零件 | $31.23 | 313 | 1.08 lbs | 8.72% | 退货率偏高 (>8.0%) |
| 50 | **Amplifiers** | 放大器 | $90.53 | 647 | 0.71 lbs | 9.82% | 退货率偏高 (>8.0%), 谨慎认证类目路径 |
| 51 | **Kick Plates** | 踢脚板 | $27.06 | 111 | 1.56 lbs | 8.07% | 退货率偏高 (>8.0%) |
| 52 | **Breast Pump Carrying Bags** | 奶泵携带包 | $36.50 | 154 | 1.23 lbs | 9.17% | 退货率偏高 (>8.0%) |
| 53 | **Fenders** | 挡泥板 | $41.60 | 127 | 2.25 lbs | 5.43% | 重量偏重 (>2.0 lbs) |
| 54 | **Helicopters** | 直升机 | $22.11 | 296 | 0.77 lbs | 3.29% | 谨慎认证类目路径 |
| 55 | **Dice Bags & Boxes** | 骰袋和骰盒 | $22.43 | 430 | 0.73 lbs | 3.93% | 谨慎认证类目路径 |
| 56 | **Heating & Temperature Control** | 暖气 | $24.94 | 140 | 1.09 lbs | 9.98% | 退货率偏高 (>8.0%) |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Workout Top & Bottom Sets** | 服装套装 | $28.92 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 2 | **Sandals** | 时装凉鞋、凉拖 | $22.89 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 3 | **Shrugs** | 女装短针织衫 | $20.28 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 4 | **One-Pieces** | 连体泳衣 | $21.25 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 5 | **Tankini Sets** | 坦基尼套装 | $22.45 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 6 | **Shorts** | 短裤 | $26.75 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 7 | **Rash Guard Sets** | Rash Guard Sets | $21.18 | 高风险类目路径过滤 |
| 8 | **Sets** | 套 | $24.64 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 9 | **Figurine Lights** | 雕像灯 | $25.18 | Review护城河太深 (>1000) |
| 10 | **Skirt Sets** | 裙装套装 | $34.96 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 11 | **Clothing** | 服装 | $25.12 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 12 | **Drip Irrigation Kits** | 滴灌套件 | $32.72 | 重量超标 (>2.5 lbs) |
| 13 | **Light Therapy** | 光照疗法 | $72.14 | 退货率过高 (>10.0%) |
| 14 | **Pants** | 长裤 | $27.63 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 15 | **Snorkeling Packages** | 套装 | $32.66 | 退货率过高 (>10.0%), Review护城河太深 (>1000) |
| 16 | **Casual Jackets** | 休闲夹克 | $37.65 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 17 | **Button-Down Shirts** | 扣角领衬衫 | $20.38 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 18 | **Hand Fuel Pumps** | 手动燃油泵 | $32.24 | Review护城河太深 (>1000) |
| 19 | **Casual** | 休闲类 | $37.65 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 20 | **Beneficial Insects** | 益虫 | $31.29 | 排除类关键字过滤 |
| 21 | **Pantsuits** | 裤装 | $57.91 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 22 | **Wrinkle & Anti-Aging Devices** | 皱纹和抗衰老设备 | $112.68 | 退货率过高 (>10.0%) |
| 23 | **Herbal Supplements** | 草药补充剂 | $23.63 | Review护城河太深 (>1000) |
| 24 | **Old Fashioned Glasses** | 古典杯 | $25.55 | Review护城河太深 (>1000) |
| 25 | **Active Pants** | 运动裤 | $33.26 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 26 | **Dresses** | 连衣裙 | $36.48 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 27 | **Closet Rods** | 壁橱杆 | $22.98 | 高风险类目路径过滤 |
| 28 | **Fluid Evacuators** | 流体抽出器 | $38.01 | 重量超标 (>2.5 lbs) |
| 29 | **GPS Trackers** | GPS 追踪器 | $39.52 | Review护城河太深 (>1000) |
| 30 | **Car Stereo Receivers** | 汽车音响 | $105.06 | 退货率过高 (>10.0%) |
| 31 | **Pant Sets** | 长裤套装 | $22.95 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 32 | **Night Out** | 晚宴裙装 | $27.93 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 33 | **Battery Jumper Cables** | 电池跳线 | $23.58 | Review护城河太深 (>1000) |
| 34 | **Costumes** | 装扮服饰 | $37.40 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 35 | **Assortments & Variety Gifts** | 种类 | $32.24 | Review护城河太深 (>1000) |
| 36 | **Candlestick Holders** | 烛台座 | $24.25 | 退货率过高 (>10.0%) |
| 37 | **Accessories** | 配件 | $20.81 | Review护城河太深 (>1000) |
| 38 | **Bustiers & Corsets** | 紧身衣 | $26.64 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 39 | **Cup Carriers** | 外卖杯托盘 | $22.15 | 重量超标 (>2.5 lbs) |
| 40 | **Robots** | 机器人 | $51.95 | Review护城河太深 (>1000) |
| 41 | **Nut & Bolt Assortment Sets** | 螺母和螺栓套装 | $20.09 | 重量超标 (>2.5 lbs) |
| 42 | **Livestock Health Supplies** | 牲畜健康用品 | $31.45 | 排除类关键字过滤 |
| 43 | **Decorative Candle Lanterns** | 装饰性点烛灯笼 | $38.49 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 44 | **Hair Accessories** | 头饰 | $22.96 | 重量超标 (>2.5 lbs) |
| 45 | **Horns & Sirens** | 喇叭 | $28.33 | Review护城河太深 (>1000) |
| 46 | **Book Stands** | 书架 | $27.06 | 重量超标 (>2.5 lbs) |
| 47 | **Candle Sets** | 蜡烛套装 | $23.04 | Review护城河太深 (>1000) |
| 48 | **Shoes** | 鞋 | $49.29 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 49 | **Clutches** | 手拿包 | $32.44 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 50 | **Raincoats** | 雨衣 | $23.83 | 退货率过高 (>10.0%) |
| 51 | **Jerseys** | 球衣 | $38.10 | 高风险类目路径过滤 |
| 52 | **Trench Coats** | 风雨衣 | $54.77 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 53 | **Home Décor Products** | 家居装饰 | $20.56 | 退货率过高 (>10.0%) |
| 54 | **Sweatpants** | Sweatpants | $27.22 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 55 | **Protective Gear** | 防护装备 | $41.94 | 重量超标 (>2.5 lbs) |
| 56 | **Bag Sealers** | 封袋机 | $41.20 | 重量超标 (>2.5 lbs) |
| 57 | **Hearing Amplifiers** | 助听扩音器 | $121.96 | 退货率过高 (>10.0%) |
| 58 | **Tops** | Tops | $22.08 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 59 | **Floor Molding & Trim** | 地板压条和镶边 | $24.66 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 60 | **Workout Top & Bottom Sets** | 服装套装 | $32.51 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 61 | **Pant Sets** | 长裤套装 | $23.24 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 62 | **In-Dash Navigation** | 内置车载导航 | $111.94 | 退货率过高 (>10.0%) |
| 63 | **AV Receivers & Amplifiers** | AV接收机 | $112.01 | 退货率过高 (>10.0%) |
| 64 | **Training Heads** | 培训负责人 | $28.46 | 退货率过高 (>10.0%) |
| 65 | **Wormers** | 虫子 | $39.21 | 排除类关键字过滤 |
| 66 | **Manual Pasta Makers** | 手动面条机 | $29.23 | Review护城河太深 (>1000) |
| 67 | **Hoodies** | 帽衫 | $37.42 | 高风险类目路径过滤 |
| 68 | **Shoulder Bags** | 单肩包 | $43.52 | 高风险类目路径过滤 |
| 69 | **Wedding Dresses** | 婚纱 | $82.75 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 70 | **Clothing** | 服装 | $20.36 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 71 | **Foot Warmers** | 暖脚 | $30.00 | 退货率过高 (>10.0%) |
| 72 | **Candle Sconces** | 壁突式烛台 | $28.03 | 退货率过高 (>10.0%) |
| 73 | **Urinal Accessories** | 小便池配件 | $33.42 | 重量超标 (>2.5 lbs) |
| 74 | **Candleholder Sets** | 烛台套装 | $30.23 | 退货率过高 (>10.0%) |
| 75 | **Digital Media Receivers** | 数字媒体接收器 | $157.23 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 76 | **Night Vision Binoculars & Goggles** | 夜视双筒望远镜和护目镜 | $99.79 | 退货率过高 (>10.0%) |
| 77 | **Masonry Chisels** | 砌筑用凿子 | $26.80 | 重量超标 (>2.5 lbs) |
| 78 | **In-Dash DVD & Video Receivers** | 仪表盘视频 | $150.46 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 79 | **Clothing** | 衣服 | $20.70 | 高风险类目路径过滤 |
| 80 | **Advent Calendars** | 圣诞日历 | $28.24 | 退货率过高 (>10.0%) |
| 81 | **One-Piece Pajamas** | 连体睡衣 | $31.96 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 82 | **Swimwear** | 泳衣 | $29.18 | 高风险类目路径过滤 |
| 83 | **Tools** | 工具 | $42.93 | 重量超标 (>2.5 lbs) |
| 84 | **Ostomy Belts** | 造口术束带 | $26.22 | 退货率过高 (>10.0%) |

## 三、 候选类目详细数据指标画像 (供大模型分析使用)

以下为入选的绿色与黄色子类目的完整数据指标。您可以将这些数据输入大模型（如 Gemini、Claude），让其结合具体品类特性进行深入的入选原因、产品特征及商业机会评估。

### 🟢 绿色类目详情列表

#### 🏆 🟢-1. Swing Trainers (室内练习器)

- **完整市场路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.65`
  *   **平均 Reviews (Avg Reviews)**：`444 个`
  *   **物理重量 (Weight)**：`0.70 lbs`
  *   **平均退货率 (Return Rate)**：`4.37%`
  *   **平均毛利率 (Profit Margin)**：`58.68%`
  *   **品牌集中度 (Brand Concentration)**：`59.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Golf › Training Equipment › Swing Trainers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 高尔夫球场 › 用品 训练 › 室内练习器`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 19.19`
  *   **新品平均星级**：`3.4`
  *   **新品月均销量**：`1,141`
  *   **新品月均销售额**：`$16,418`
  *   **平均重量**：`0.70 pounds (320 g)`
  *   **平均体积**：`148.44 in³ (2,433 cm³)`
  *   **平均毛利率**：`58.68%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-2. Bread Proofing Baskets (面包发酵篮)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.88`
  *   **平均 Reviews (Avg Reviews)**：`570 个`
  *   **物理重量 (Weight)**：`1.88 lbs`
  *   **平均退货率 (Return Rate)**：`4.09%`
  *   **平均毛利率 (Profit Margin)**：`56.98%`
  *   **品牌集中度 (Brand Concentration)**：`53.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Baking Tools & Accessories › Baking & Pastry Utensils › Bread Proofing Baskets  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 烘焙用具 › 烘焙工具 › 烘焙 › 面包发酵篮`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`78`
  *   **新品平均价格**：`$ 27.2`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`604`
  *   **新品月均销售额**：`$16,777`
  *   **平均重量**：`1.88 pounds (852 g)`
  *   **平均体积**：`409.06 in³ (6,703 cm³)`
  *   **平均毛利率**：`56.98%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟢-3. Lighting Products (水底灯)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$49.41`
  *   **平均 Reviews (Avg Reviews)**：`475 个`
  *   **物理重量 (Weight)**：`1.70 lbs`
  *   **平均退货率 (Return Rate)**：`6.75%`
  *   **平均毛利率 (Profit Margin)**：`67.33%`
  *   **品牌集中度 (Brand Concentration)**：`51.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 水底灯`
  *   **A+数量占比**：`97%`
  *   **新品平均评分数**：`60`
  *   **新品平均价格**：`$ 51.02`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`1,109`
  *   **新品月均销售额**：`$61,518`
  *   **平均重量**：`1.70 pounds (772 g)`
  *   **平均体积**：`635.48 in³ (10,414 cm³)`
  *   **平均毛利率**：`67.33%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-4. Shilajit (Shilajit)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Shilajit  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.19`
  *   **平均 Reviews (Avg Reviews)**：`714 个`
  *   **物理重量 (Weight)**：`0.40 lbs`
  *   **平均退货率 (Return Rate)**：`0.34%`
  *   **平均毛利率 (Profit Margin)**：`67.84%`
  *   **品牌集中度 (Brand Concentration)**：`63.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`41.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Shilajit  市场分析`
  *   **市场路径(中文)**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Shilajit`
  *   **A+数量占比**：`94%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 30.85`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`326`
  *   **新品月均销售额**：`$10,296`
  *   **平均重量**：`0.40 pounds (182 g)`
  *   **平均体积**：`56.85 in³ (932 cm³)`
  *   **平均毛利率**：`67.84%`
  *   **卖家所属地**：`美国|59.0%`
  *   **搜索购买比**：`15.3‰`

---

#### 🏆 🟢-5. Decorative Boxes (装饰盒)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.84`
  *   **平均 Reviews (Avg Reviews)**：`680 个`
  *   **物理重量 (Weight)**：`1.66 lbs`
  *   **平均退货率 (Return Rate)**：`7.91%`
  *   **平均毛利率 (Profit Margin)**：`58.2%`
  *   **品牌集中度 (Brand Concentration)**：`49.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰盒`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`67`
  *   **新品平均价格**：`$ 23.16`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`788`
  *   **新品月均销售额**：`$17,579`
  *   **平均重量**：`1.66 pounds (751 g)`
  *   **平均体积**：`381.88 in³ (6,258 cm³)`
  *   **平均毛利率**：`58.2%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`4.5‰`

---

#### 🏆 🟢-6. Nozzles (喷嘴)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.98`
  *   **平均 Reviews (Avg Reviews)**：`497 个`
  *   **物理重量 (Weight)**：`0.44 lbs`
  *   **平均退货率 (Return Rate)**：`2.63%`
  *   **平均毛利率 (Profit Margin)**：`64.78%`
  *   **品牌集中度 (Brand Concentration)**：`54.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 电动工具 › 替换件和配件 › 高压清洗机配件 › 喷嘴`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`54`
  *   **新品平均价格**：`$ 33.14`
  *   **新品平均星级**：`2.6`
  *   **新品月均销量**：`818`
  *   **新品月均销售额**：`$23,991`
  *   **平均重量**：`0.44 pounds (201 g)`
  *   **平均体积**：`66.32 in³ (1,087 cm³)`
  *   **平均毛利率**：`64.78%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`13.5‰`

---

#### 🏆 🟢-7. Cups (杯子)

- **完整市场路径**：`Home & Kitchen › Event & Party Supplies › Tableware › Cups  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.43`
  *   **平均 Reviews (Avg Reviews)**：`487 个`
  *   **物理重量 (Weight)**：`1.31 lbs`
  *   **平均退货率 (Return Rate)**：`3.95%`
  *   **平均毛利率 (Profit Margin)**：`51.41%`
  *   **品牌集中度 (Brand Concentration)**：`56.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Event & Party Supplies › Tableware › Cups  市场分析`
  *   **市场路径(中文)**：`家居用品 › 活动 › 餐具 › 杯子`
  *   **A+数量占比**：`65%`
  *   **新品平均评分数**：`523`
  *   **新品平均价格**：`$ 26.68`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`1,221`
  *   **新品月均销售额**：`$29,126`
  *   **平均重量**：`1.31 pounds (594 g)`
  *   **平均体积**：`39.92 in³ (654 cm³)`
  *   **平均毛利率**：`51.41%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`8.6‰`

---

#### 🏆 🟢-8. Tap Extractors (分接抽水机)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Taps & Dies › Tap Extractors  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.16`
  *   **平均 Reviews (Avg Reviews)**：`796 个`
  *   **物理重量 (Weight)**：`1.42 lbs`
  *   **平均退货率 (Return Rate)**：`4.89%`
  *   **平均毛利率 (Profit Margin)**：`59.89%`
  *   **品牌集中度 (Brand Concentration)**：`60.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Taps & Dies › Tap Extractors  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具 › 水龙头 › 分接抽水机`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`395`
  *   **新品平均价格**：`$ 16.04`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`379`
  *   **新品月均销售额**：`$6,451`
  *   **平均重量**：`1.42 pounds (643 g)`
  *   **平均体积**：`59.45 in³ (974 cm³)`
  *   **平均毛利率**：`59.89%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟢-9. Herb & Spice Mills (草本植物)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Seasoning & Spice Tools › Herb & Spice Mills  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.71`
  *   **平均 Reviews (Avg Reviews)**：`759 个`
  *   **物理重量 (Weight)**：`0.57 lbs`
  *   **平均退货率 (Return Rate)**：`3.55%`
  *   **平均毛利率 (Profit Margin)**：`60.83%`
  *   **品牌集中度 (Brand Concentration)**：`59.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Seasoning & Spice Tools › Herb & Spice Mills  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 调味品 › 草本植物`
  *   **A+数量占比**：`58%`
  *   **新品平均评分数**：`49`
  *   **新品平均价格**：`$ 15.92`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`871`
  *   **新品月均销售额**：`$13,068`
  *   **平均重量**：`0.57 pounds (258 g)`
  *   **平均体积**：`28.60 in³ (469 cm³)`
  *   **平均毛利率**：`60.83%`
  *   **卖家所属地**：`中国|54.0%`
  *   **搜索购买比**：`4.9‰`

---

#### 🏆 🟢-10. Dash Covers (仪表盘罩)

- **完整市场路径**：`Automotive › Interior Accessories › Covers › Dash Covers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.26`
  *   **平均 Reviews (Avg Reviews)**：`787 个`
  *   **物理重量 (Weight)**：`1.20 lbs`
  *   **平均退货率 (Return Rate)**：`6.55%`
  *   **平均毛利率 (Profit Margin)**：`59.0%`
  *   **品牌集中度 (Brand Concentration)**：`62.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`89.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Interior Accessories › Covers › Dash Covers  市场分析`
  *   **市场路径(中文)**：`汽车 › 内部配件 › 覆盖物 › 仪表盘罩`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`249`
  *   **新品平均价格**：`$ 24.66`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`630`
  *   **新品月均销售额**：`$16,632`
  *   **平均重量**：`1.20 pounds (543 g)`
  *   **平均体积**：`585.41 in³ (9,593 cm³)`
  *   **平均毛利率**：`59%`
  *   **卖家所属地**：`中国|89.0%`
  *   **搜索购买比**：`4.3‰`

---

#### 🏆 🟢-11. Bladder Control Devices (膀胱控制设备)

- **完整市场路径**：`Health & Household › Health Care › Incontinence & Ostomy › Bladder Control Devices  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.65`
  *   **平均 Reviews (Avg Reviews)**：`499 个`
  *   **物理重量 (Weight)**：`0.56 lbs`
  *   **平均退货率 (Return Rate)**：`3.9%`
  *   **平均毛利率 (Profit Margin)**：`62.53%`
  *   **品牌集中度 (Brand Concentration)**：`46.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Incontinence & Ostomy › Bladder Control Devices  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 成人失禁用品 › 膀胱控制设备`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`218`
  *   **新品平均价格**：`$ 38.93`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`346`
  *   **新品月均销售额**：`$12,286`
  *   **平均重量**：`0.56 pounds (255 g)`
  *   **平均体积**：`135.69 in³ (2,224 cm³)`
  *   **平均毛利率**：`62.53%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`10.6‰`

---

#### 🏆 🟢-12. Feeders (喂食器)

- **完整市场路径**：`Pet Supplies › Birds › Feeding & Watering Supplies › Feeders  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.98`
  *   **平均 Reviews (Avg Reviews)**：`572 个`
  *   **物理重量 (Weight)**：`1.08 lbs`
  *   **平均退货率 (Return Rate)**：`5.44%`
  *   **平均毛利率 (Profit Margin)**：`52.64%`
  *   **品牌集中度 (Brand Concentration)**：`48.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Birds › Feeding & Watering Supplies › Feeders  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 鸟类 › 喂食 › 喂食器`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`207`
  *   **新品平均价格**：`$ 44.42`
  *   **新品平均星级**：`3.4`
  *   **新品月均销量**：`552`
  *   **新品月均销售额**：`$17,891`
  *   **平均重量**：`1.08 pounds (490 g)`
  *   **平均体积**：`196.00 in³ (3,212 cm³)`
  *   **平均毛利率**：`52.64%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟢-13. Emblems (车标)

- **完整市场路径**：`Automotive › Exterior Accessories › Emblems  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.84`
  *   **平均 Reviews (Avg Reviews)**：`582 个`
  *   **物理重量 (Weight)**：`0.12 lbs`
  *   **平均退货率 (Return Rate)**：`4.71%`
  *   **平均毛利率 (Profit Margin)**：`61.61%`
  *   **品牌集中度 (Brand Concentration)**：`46.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Exterior Accessories › Emblems  市场分析`
  *   **市场路径(中文)**：`汽车 › 外部配件 › 车标`
  *   **A+数量占比**：`38%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 14.74`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`384`
  *   **新品月均销售额**：`$5,510`
  *   **平均重量**：`0.12 pounds (55 g)`
  *   **平均体积**：`32.46 in³ (532 cm³)`
  *   **平均毛利率**：`61.61%`
  *   **卖家所属地**：`美国|45.0%`
  *   **搜索购买比**：`3.8‰`

---

#### 🏆 🟢-14. Plaques & Wall Art (装饰墙)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Plaques & Wall Art  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.35`
  *   **平均 Reviews (Avg Reviews)**：`619 个`
  *   **物理重量 (Weight)**：`1.04 lbs`
  *   **平均退货率 (Return Rate)**：`2.89%`
  *   **平均毛利率 (Profit Margin)**：`58.79%`
  *   **品牌集中度 (Brand Concentration)**：`46.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`88.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Plaques & Wall Art  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 装饰墙`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`148`
  *   **新品平均价格**：`$ 18.84`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`374`
  *   **新品月均销售额**：`$7,183`
  *   **平均重量**：`1.04 pounds (471 g)`
  *   **平均体积**：`69.79 in³ (1,144 cm³)`
  *   **平均毛利率**：`58.79%`
  *   **卖家所属地**：`中国|88.0%`
  *   **搜索购买比**：`4.9‰`

---

#### 🏆 🟢-15. Electrical System Tools (电气系统工具)

- **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.23`
  *   **平均 Reviews (Avg Reviews)**：`489 个`
  *   **物理重量 (Weight)**：`1.00 lbs`
  *   **平均退货率 (Return Rate)**：`2.38%`
  *   **平均毛利率 (Profit Margin)**：`55.1%`
  *   **品牌集中度 (Brand Concentration)**：`44.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 电气系统工具`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`46`
  *   **新品平均价格**：`$ 18.34`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`367`
  *   **新品月均销售额**：`$7,072`
  *   **平均重量**：`1.00 pounds (455 g)`
  *   **平均体积**：`319.28 in³ (5,232 cm³)`
  *   **平均毛利率**：`55.1%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟢-16. Brake System Bleeding Tools (刹车排气)

- **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.56`
  *   **平均 Reviews (Avg Reviews)**：`474 个`
  *   **物理重量 (Weight)**：`1.58 lbs`
  *   **平均退货率 (Return Rate)**：`4.69%`
  *   **平均毛利率 (Profit Margin)**：`55.53%`
  *   **品牌集中度 (Brand Concentration)**：`50.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 制动工具 › 刹车排气`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`34`
  *   **新品平均价格**：`$ 18.55`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`378`
  *   **新品月均销售额**：`$7,390`
  *   **平均重量**：`1.58 pounds (717 g)`
  *   **平均体积**：`308.88 in³ (5,062 cm³)`
  *   **平均毛利率**：`55.53%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`8.9‰`

---

#### 🏆 🟢-17. Kava Kava (卡瓦胡椒)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Kava Kava  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.87`
  *   **平均 Reviews (Avg Reviews)**：`295 个`
  *   **物理重量 (Weight)**：`0.65 lbs`
  *   **平均退货率 (Return Rate)**：`0.39%`
  *   **平均毛利率 (Profit Margin)**：`68.59%`
  *   **品牌集中度 (Brand Concentration)**：`63.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`14.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Kava Kava  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 身、泳和附剂 › 草本补充 › 卡瓦胡椒`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`28`
  *   **新品平均价格**：`$ 26.98`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`261`
  *   **新品月均销售额**：`$7,018`
  *   **平均重量**：`0.65 pounds (293 g)`
  *   **平均体积**：`73.64 in³ (1,207 cm³)`
  *   **平均毛利率**：`68.59%`
  *   **卖家所属地**：`美国|86.0%`
  *   **搜索购买比**：`12.2‰`

---

#### 🏆 🟢-18. Hands Free Leashes (免手持牵绳)

- **完整市场路径**：`Pet Supplies › Dogs › Collars, Harnesses & Leashes › Leashes › Hands Free Leashes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.90`
  *   **平均 Reviews (Avg Reviews)**：`769 个`
  *   **物理重量 (Weight)**：`0.74 lbs`
  *   **平均退货率 (Return Rate)**：`6.44%`
  *   **平均毛利率 (Profit Margin)**：`61.31%`
  *   **品牌集中度 (Brand Concentration)**：`64.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`50.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Dogs › Collars, Harnesses & Leashes › Leashes › Hands Free Leashes  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 犬类 › 项圈、背带 › 绳索 › 免手持牵绳`
  *   **A+数量占比**：`97%`
  *   **新品平均评分数**：`66`
  *   **新品平均价格**：`$ 21.15`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`194`
  *   **新品月均销售额**：`$4,100`
  *   **平均重量**：`0.74 pounds (334 g)`
  *   **平均体积**：`106.96 in³ (1,753 cm³)`
  *   **平均毛利率**：`61.31%`
  *   **卖家所属地**：`中国|50.0%`
  *   **搜索购买比**：`8.7‰`

---

#### 🏆 🟢-19. Honey Jars (蜂蜜罐子)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Honey Jars  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.74`
  *   **平均 Reviews (Avg Reviews)**：`662 个`
  *   **物理重量 (Weight)**：`1.83 lbs`
  *   **平均退货率 (Return Rate)**：`5.4%`
  *   **平均毛利率 (Profit Margin)**：`52.97%`
  *   **品牌集中度 (Brand Concentration)**：`52.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Honey Jars  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 小甜甜 › 碗碟 › 蜂蜜罐子`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 18.29`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`210`
  *   **新品月均销售额**：`$3,924`
  *   **平均重量**：`1.83 pounds (831 g)`
  *   **平均体积**：`185.78 in³ (3,044 cm³)`
  *   **平均毛利率**：`52.97%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`7.8‰`

---

#### 🏆 🟢-20. Trophies (奖杯)

- **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.41`
  *   **平均 Reviews (Avg Reviews)**：`291 个`
  *   **物理重量 (Weight)**：`0.97 lbs`
  *   **平均退货率 (Return Rate)**：`2.59%`
  *   **平均毛利率 (Profit Margin)**：`62.16%`
  *   **品牌集中度 (Brand Concentration)**：`46.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 辅料 › 、奖牌 › 奖杯`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 29.89`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`337`
  *   **新品月均销售额**：`$11,024`
  *   **平均重量**：`0.97 pounds (440 g)`
  *   **平均体积**：`172.11 in³ (2,820 cm³)`
  *   **平均毛利率**：`62.16%`
  *   **卖家所属地**：`中国|54.0%`
  *   **搜索购买比**：`6.5‰`

---

#### 🏆 🟢-21. Insulin Injectors (胰岛素注射器)

- **完整市场路径**：`Health & Household › Health Care › Diabetes Care › Insulin Injectors  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.29`
  *   **平均 Reviews (Avg Reviews)**：`479 个`
  *   **物理重量 (Weight)**：`0.47 lbs`
  *   **平均退货率 (Return Rate)**：`1.5%`
  *   **平均毛利率 (Profit Margin)**：`61.28%`
  *   **品牌集中度 (Brand Concentration)**：`64.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`38.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Diabetes Care › Insulin Injectors  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 糖尿病护理 › 胰岛素注射器`
  *   **A+数量占比**：`51%`
  *   **新品平均评分数**：`92`
  *   **新品平均价格**：`$ 29.79`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`299`
  *   **新品月均销售额**：`$9,075`
  *   **平均重量**：`0.47 pounds (212 g)`
  *   **平均体积**：`125.09 in³ (2,050 cm³)`
  *   **平均毛利率**：`61.28%`
  *   **卖家所属地**：`美国|62.0%`
  *   **搜索购买比**：`24.9‰`

---

#### 🏆 🟢-22. Oolong (乌龙)

- **完整市场路径**：`Grocery & Gourmet Food › Beverages › Tea › Oolong  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.14`
  *   **平均 Reviews (Avg Reviews)**：`464 个`
  *   **物理重量 (Weight)**：`0.46 lbs`
  *   **平均退货率 (Return Rate)**：`0.26%`
  *   **平均毛利率 (Profit Margin)**：`59.14%`
  *   **品牌集中度 (Brand Concentration)**：`59.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`49.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Grocery & Gourmet Food › Beverages › Tea › Oolong  市场分析`
  *   **市场路径(中文)**：`杂货店 › 饮料 › 茶叶 › 乌龙`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`35`
  *   **新品平均价格**：`$ 25.23`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`278`
  *   **新品月均销售额**：`$7,272`
  *   **平均重量**：`0.46 pounds (209 g)`
  *   **平均体积**：`111.87 in³ (1,833 cm³)`
  *   **平均毛利率**：`59.14%`
  *   **卖家所属地**：`美国|51.0%`
  *   **搜索购买比**：`18.2‰`

---

#### 🏆 🟢-23. Headlights (车头灯)

- **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Accessories › Lights & Reflectors › Headlights  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.78`
  *   **平均 Reviews (Avg Reviews)**：`557 个`
  *   **物理重量 (Weight)**：`0.47 lbs`
  *   **平均退货率 (Return Rate)**：`5.21%`
  *   **平均毛利率 (Profit Margin)**：`67.3%`
  *   **品牌集中度 (Brand Concentration)**：`57.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Accessories › Lights & Reflectors › Headlights  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 骑自行车 › 配件 › 车灯、镜面反射 › 车头灯`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 24.41`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`268`
  *   **新品月均销售额**：`$5,944`
  *   **平均重量**：`0.47 pounds (212 g)`
  *   **平均体积**：`32.30 in³ (529 cm³)`
  *   **平均毛利率**：`67.3%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`4.7‰`

---

#### 🏆 🟢-24. Tattoo Kits (纹身套装)

- **完整市场路径**：`Beauty & Personal Care › Personal Care › Piercing & Tattoo Supplies › Tattoo Supplies › Tattoo Kits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.80`
  *   **平均 Reviews (Avg Reviews)**：`530 个`
  *   **物理重量 (Weight)**：`1.52 lbs`
  *   **平均退货率 (Return Rate)**：`2.09%`
  *   **平均毛利率 (Profit Margin)**：`59.37%`
  *   **品牌集中度 (Brand Concentration)**：`63.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Beauty & Personal Care › Personal Care › Piercing & Tattoo Supplies › Tattoo Supplies › Tattoo Kits  市场分析`
  *   **市场路径(中文)**：`美容与护理 › 沐浴 › 穿洞和纹身用品 › 纹身用品 › 纹身套装`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`63`
  *   **新品平均价格**：`$ 28.93`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`199`
  *   **新品月均销售额**：`$5,966`
  *   **平均重量**：`1.52 pounds (691 g)`
  *   **平均体积**：`212.95 in³ (3,490 cm³)`
  *   **平均毛利率**：`59.37%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-25. Network & Cable Testers (网络)

- **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Network & Cable Testers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$119.03`
  *   **平均 Reviews (Avg Reviews)**：`426 个`
  *   **物理重量 (Weight)**：`0.61 lbs`
  *   **平均退货率 (Return Rate)**：`5.23%`
  *   **平均毛利率 (Profit Margin)**：`73.12%`
  *   **品牌集中度 (Brand Concentration)**：`64.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Network & Cable Testers  市场分析`
  *   **市场路径(中文)**：`工业类 › 测试，测量 › 网络`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`51`
  *   **新品平均价格**：`$ 57.29`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`239`
  *   **新品月均销售额**：`$9,859`
  *   **平均重量**：`0.61 pounds (278 g)`
  *   **平均体积**：`102.78 in³ (1,684 cm³)`
  *   **平均毛利率**：`73.12%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`9.3‰`

---

#### 🏆 🟢-26. Drill Bits (钻头)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.43`
  *   **平均 Reviews (Avg Reviews)**：`264 个`
  *   **物理重量 (Weight)**：`0.98 lbs`
  *   **平均退货率 (Return Rate)**：`2.68%`
  *   **平均毛利率 (Profit Margin)**：`60.11%`
  *   **品牌集中度 (Brand Concentration)**：`52.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 电动工具零件 › 电钻零件 › 钻头`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`45`
  *   **新品平均价格**：`$ 25.74`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`203`
  *   **新品月均销售额**：`$5,687`
  *   **平均重量**：`0.98 pounds (445 g)`
  *   **平均体积**：`60.72 in³ (995 cm³)`
  *   **平均毛利率**：`60.11%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`12.4‰`

---

#### 🏆 🟢-27. Cookbook Stands (菜谱架)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Accessories › Cookbook Stands & Recipe Holders › Cookbook Stands  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.65`
  *   **平均 Reviews (Avg Reviews)**：`712 个`
  *   **物理重量 (Weight)**：`1.87 lbs`
  *   **平均退货率 (Return Rate)**：`6.17%`
  *   **平均毛利率 (Profit Margin)**：`54.54%`
  *   **品牌集中度 (Brand Concentration)**：`54.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Accessories › Cookbook Stands & Recipe Holders › Cookbook Stands  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 厨房配件 › 菜谱架 › 菜谱架`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`20`
  *   **新品平均价格**：`$ 19.86`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`176`
  *   **新品月均销售额**：`$3,244`
  *   **平均重量**：`1.87 pounds (849 g)`
  *   **平均体积**：`451.70 in³ (7,402 cm³)`
  *   **平均毛利率**：`54.54%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`7.0‰`

---

#### 🏆 🟢-28. Countersink Drill Bits (沉孔钻头)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits › Countersink Drill Bits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.48`
  *   **平均 Reviews (Avg Reviews)**：`588 个`
  *   **物理重量 (Weight)**：`0.49 lbs`
  *   **平均退货率 (Return Rate)**：`1.85%`
  *   **平均毛利率 (Profit Margin)**：`62.05%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits › Countersink Drill Bits  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 电动工具零件 › 电钻零件 › 钻头 › 沉孔钻头`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`50`
  *   **新品平均价格**：`$ 22.32`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`238`
  *   **新品月均销售额**：`$5,475`
  *   **平均重量**：`0.49 pounds (221 g)`
  *   **平均体积**：`31.70 in³ (519 cm³)`
  *   **平均毛利率**：`62.05%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`10.5‰`

---

#### 🏆 🟢-29. Tie-Downs (栓系器具)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Trailer Accessories › Tie-Downs  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.48`
  *   **平均 Reviews (Avg Reviews)**：`548 个`
  *   **物理重量 (Weight)**：`1.60 lbs`
  *   **平均退货率 (Return Rate)**：`3.74%`
  *   **平均毛利率 (Profit Margin)**：`58.58%`
  *   **品牌集中度 (Brand Concentration)**：`59.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`51.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Trailer Accessories › Tie-Downs  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 拖船配件 › 栓系器具`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`131`
  *   **新品平均价格**：`$ 31.15`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`294`
  *   **新品月均销售额**：`$9,735`
  *   **平均重量**：`1.60 pounds (726 g)`
  *   **平均体积**：`56.60 in³ (927 cm³)`
  *   **平均毛利率**：`58.58%`
  *   **卖家所属地**：`中国|51.0%`
  *   **搜索购买比**：`10.5‰`

---

#### 🏆 🟢-30. Exterior Lighting (外部照明)

- **完整市场路径**：`Automotive › RV Parts & Accessories › Power & Electrical › Lighting › Exterior Lighting  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.81`
  *   **平均 Reviews (Avg Reviews)**：`523 个`
  *   **物理重量 (Weight)**：`0.77 lbs`
  *   **平均退货率 (Return Rate)**：`4.66%`
  *   **平均毛利率 (Profit Margin)**：`62.28%`
  *   **品牌集中度 (Brand Concentration)**：`52.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › RV Parts & Accessories › Power & Electrical › Lighting › Exterior Lighting  市场分析`
  *   **市场路径(中文)**：`汽车 › 房车配件 › 权力 › 照明 › 外部照明`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`663`
  *   **新品平均价格**：`$ 32.08`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`187`
  *   **新品月均销售额**：`$5,971`
  *   **平均重量**：`0.77 pounds (349 g)`
  *   **平均体积**：`137.58 in³ (2,254 cm³)`
  *   **平均毛利率**：`62.28%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟢-31. Deburring Cutters (去毛刺刀具)

- **完整市场路径**：`Industrial & Scientific › Cutting Tools › Deburring Cutters  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.36`
  *   **平均 Reviews (Avg Reviews)**：`370 个`
  *   **物理重量 (Weight)**：`0.47 lbs`
  *   **平均退货率 (Return Rate)**：`1.93%`
  *   **平均毛利率 (Profit Margin)**：`63.45%`
  *   **品牌集中度 (Brand Concentration)**：`63.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`59.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Cutting Tools › Deburring Cutters  市场分析`
  *   **市场路径(中文)**：`工业类 › 切割工具 › 去毛刺刀具`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 19.31`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`151`
  *   **新品月均销售额**：`$2,467`
  *   **平均重量**：`0.47 pounds (213 g)`
  *   **平均体积**：`38.90 in³ (637 cm³)`
  *   **平均毛利率**：`63.45%`
  *   **卖家所属地**：`中国|59.0%`
  *   **搜索购买比**：`14.2‰`

---

#### 🏆 🟢-32. Bar Tools & Drinkware (酒吧工具)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Bar Tools & Drinkware  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.94`
  *   **平均 Reviews (Avg Reviews)**：`365 个`
  *   **物理重量 (Weight)**：`1.27 lbs`
  *   **平均退货率 (Return Rate)**：`5.44%`
  *   **平均毛利率 (Profit Margin)**：`58.57%`
  *   **品牌集中度 (Brand Concentration)**：`53.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`61.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Bar Tools & Drinkware  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 酒吧工具`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 20.95`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`121`
  *   **新品月均销售额**：`$2,979`
  *   **平均重量**：`1.27 pounds (576 g)`
  *   **平均体积**：`310.33 in³ (5,085 cm³)`
  *   **平均毛利率**：`58.57%`
  *   **卖家所属地**：`中国|61.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟢-33. Wood Burning Tools (木材燃烧工具)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Woodcrafts › Wood Burning Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.55`
  *   **平均 Reviews (Avg Reviews)**：`567 个`
  *   **物理重量 (Weight)**：`1.07 lbs`
  *   **平均退货率 (Return Rate)**：`4.0%`
  *   **平均毛利率 (Profit Margin)**：`65.51%`
  *   **品牌集中度 (Brand Concentration)**：`54.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Woodcrafts › Wood Burning Tools  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 木制工艺品 › 木材燃烧工具`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`81`
  *   **新品平均价格**：`$ 27.65`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`290`
  *   **新品月均销售额**：`$4,996`
  *   **平均重量**：`1.07 pounds (486 g)`
  *   **平均体积**：`73.35 in³ (1,202 cm³)`
  *   **平均毛利率**：`65.51%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-34. Sound Therapy (声音疗法)

- **完整市场路径**：`Health & Household › Health Care › Alternative Medicine › Sound Therapy  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$54.87`
  *   **平均 Reviews (Avg Reviews)**：`254 个`
  *   **物理重量 (Weight)**：`0.96 lbs`
  *   **平均退货率 (Return Rate)**：`6.32%`
  *   **平均毛利率 (Profit Margin)**：`66.97%`
  *   **品牌集中度 (Brand Concentration)**：`45.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Alternative Medicine › Sound Therapy  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 替代药物 › 声音疗法`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`32`
  *   **新品平均价格**：`$ 32.11`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`199`
  *   **新品月均销售额**：`$6,953`
  *   **平均重量**：`0.96 pounds (433 g)`
  *   **平均体积**：`85.15 in³ (1,395 cm³)`
  *   **平均毛利率**：`66.97%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`10.1‰`

---

#### 🏆 🟢-35. Pond Lights (池塘灯)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Water Gardens & Ponds › Pond Lights  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$46.35`
  *   **平均 Reviews (Avg Reviews)**：`235 个`
  *   **物理重量 (Weight)**：`1.53 lbs`
  *   **平均退货率 (Return Rate)**：`6.15%`
  *   **平均毛利率 (Profit Margin)**：`66.84%`
  *   **品牌集中度 (Brand Concentration)**：`64.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Water Gardens & Ponds › Pond Lights  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 池塘、喷泉 › 池塘灯`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`115`
  *   **新品平均价格**：`$ 50.99`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`202`
  *   **新品月均销售额**：`$9,446`
  *   **平均重量**：`1.53 pounds (692 g)`
  *   **平均体积**：`198.14 in³ (3,247 cm³)`
  *   **平均毛利率**：`66.84%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟢-36. Paint Roller Extension Poles (油漆滚筒加长杆)

- **完整市场路径**：`Tools & Home Improvement › Paint, Wall Treatments & Supplies › Painting Supplies & Tools › Paint Application Tools › Paint Roller Extension Poles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.17`
  *   **平均 Reviews (Avg Reviews)**：`354 个`
  *   **物理重量 (Weight)**：`2.00 lbs`
  *   **平均退货率 (Return Rate)**：`4.55%`
  *   **平均毛利率 (Profit Margin)**：`54.28%`
  *   **品牌集中度 (Brand Concentration)**：`56.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Paint, Wall Treatments & Supplies › Painting Supplies & Tools › Paint Application Tools › Paint Roller Extension Poles  市场分析`
  *   **市场路径(中文)**：`工具 › 正面，正面照 › 绘画用品 › 油漆应用 › 油漆滚筒加长杆`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 54.9`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`103`
  *   **新品月均销售额**：`$6,193`
  *   **平均重量**：`2.00 pounds (908 g)`
  *   **平均体积**：`173.65 in³ (2,846 cm³)`
  *   **平均毛利率**：`54.28%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`9.4‰`

---

#### 🏆 🟢-37. Angle Grinder Wheels (角磨机砂轮)

- **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Angle Grinder Wheels  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.63`
  *   **平均 Reviews (Avg Reviews)**：`165 个`
  *   **物理重量 (Weight)**：`1.54 lbs`
  *   **平均退货率 (Return Rate)**：`2.41%`
  *   **平均毛利率 (Profit Margin)**：`63.38%`
  *   **品牌集中度 (Brand Concentration)**：`58.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Angle Grinder Wheels  市场分析`
  *   **市场路径(中文)**：`工业类 › 磨削加工 › 研磨砂轮 › 角磨机砂轮`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`28`
  *   **新品平均价格**：`$ 23.29`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`188`
  *   **新品月均销售额**：`$4,209`
  *   **平均重量**：`1.54 pounds (701 g)`
  *   **平均体积**：`52.75 in³ (864 cm³)`
  *   **平均毛利率**：`63.38%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`15.4‰`

---

#### 🏆 🟢-38. Scoreboards & Timers (记分牌和计时器)

- **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Coach & Referee Gear › Scoreboards & Timers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$52.27`
  *   **平均 Reviews (Avg Reviews)**：`352 个`
  *   **物理重量 (Weight)**：`1.54 lbs`
  *   **平均退货率 (Return Rate)**：`5.13%`
  *   **平均毛利率 (Profit Margin)**：`65.5%`
  *   **品牌集中度 (Brand Concentration)**：`54.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Coach & Referee Gear › Scoreboards & Timers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 辅料 › 教练 › 记分牌和计时器`
  *   **A+数量占比**：`79%`
  *   **新品平均评分数**：`26`
  *   **新品平均价格**：`$ 34.78`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`164`
  *   **新品月均销售额**：`$5,876`
  *   **平均重量**：`1.54 pounds (698 g)`
  *   **平均体积**：`216.17 in³ (3,542 cm³)`
  *   **平均毛利率**：`65.5%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`7.1‰`

---

#### 🏆 🟢-39. Brake Controls (制动控制装置)

- **完整市场路径**：`Automotive › Exterior Accessories › Trailer Accessories › Brake Controls  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$87.23`
  *   **平均 Reviews (Avg Reviews)**：`308 个`
  *   **物理重量 (Weight)**：`1.22 lbs`
  *   **平均退货率 (Return Rate)**：`6.05%`
  *   **平均毛利率 (Profit Margin)**：`70.8%`
  *   **品牌集中度 (Brand Concentration)**：`59.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`56.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Exterior Accessories › Trailer Accessories › Brake Controls  市场分析`
  *   **市场路径(中文)**：`汽车 › 外部配件 › 拖车配件 › 制动控制装置`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`14`
  *   **新品平均价格**：`$ 105.92`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`159`
  *   **新品月均销售额**：`$16,625`
  *   **平均重量**：`1.22 pounds (555 g)`
  *   **平均体积**：`132.33 in³ (2,169 cm³)`
  *   **平均毛利率**：`70.8%`
  *   **卖家所属地**：`中国|56.0%`
  *   **搜索购买比**：`9.0‰`

---

#### 🏆 🟢-40. Seat Covers (摩托车座套)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Seat Covers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.10`
  *   **平均 Reviews (Avg Reviews)**：`316 个`
  *   **物理重量 (Weight)**：`1.15 lbs`
  *   **平均退货率 (Return Rate)**：`5.29%`
  *   **平均毛利率 (Profit Margin)**：`64.58%`
  *   **品牌集中度 (Brand Concentration)**：`50.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`88.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Seat Covers  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 辅料 › 摩托车座套`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`35`
  *   **新品平均价格**：`$ 30.22`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`169`
  *   **新品月均销售额**：`$5,030`
  *   **平均重量**：`1.15 pounds (520 g)`
  *   **平均体积**：`279.26 in³ (4,576 cm³)`
  *   **平均毛利率**：`64.58%`
  *   **卖家所属地**：`中国|88.0%`
  *   **搜索购买比**：`3.0‰`

---

#### 🏆 🟢-41. Float Valves (浮阀)

- **完整市场路径**：`Industrial & Scientific › Hydraulics, Pneumatics & Plumbing › Fittings › Valves › Float Valves  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.85`
  *   **平均 Reviews (Avg Reviews)**：`183 个`
  *   **物理重量 (Weight)**：`0.67 lbs`
  *   **平均退货率 (Return Rate)**：`4.44%`
  *   **平均毛利率 (Profit Margin)**：`61.28%`
  *   **品牌集中度 (Brand Concentration)**：`43.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Hydraulics, Pneumatics & Plumbing › Fittings › Valves › Float Valves  市场分析`
  *   **市场路径(中文)**：`工业类 › 液压系统、气动系统 › 配件 › 阀门 › 浮阀`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 21.8`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`166`
  *   **新品月均销售额**：`$3,432`
  *   **平均重量**：`0.67 pounds (304 g)`
  *   **平均体积**：`110.66 in³ (1,813 cm³)`
  *   **平均毛利率**：`61.28%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`15.7‰`

---

#### 🏆 🟢-42. Weaving Looms (织机)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Weaving & Spinning › Weaving Looms  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.49`
  *   **平均 Reviews (Avg Reviews)**：`311 个`
  *   **物理重量 (Weight)**：`1.01 lbs`
  *   **平均退货率 (Return Rate)**：`3.33%`
  *   **平均毛利率 (Profit Margin)**：`55.9%`
  *   **品牌集中度 (Brand Concentration)**：`57.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Weaving & Spinning › Weaving Looms  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 纺织 › 织机`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`16`
  *   **新品平均价格**：`$ 17.68`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`84`
  *   **新品月均销售额**：`$1,345`
  *   **平均重量**：`1.01 pounds (459 g)`
  *   **平均体积**：`105.21 in³ (1,724 cm³)`
  *   **平均毛利率**：`55.9%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`5.6‰`

---

#### 🏆 🟢-43. Leak Detection Tools (泄漏检测工具)

- **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Inspection & Analysis › Leak Detection Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$100.92`
  *   **平均 Reviews (Avg Reviews)**：`154 个`
  *   **物理重量 (Weight)**：`1.45 lbs`
  *   **平均退货率 (Return Rate)**：`4.3%`
  *   **平均毛利率 (Profit Margin)**：`69.31%`
  *   **品牌集中度 (Brand Concentration)**：`53.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`47.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Inspection & Analysis › Leak Detection Tools  市场分析`
  *   **市场路径(中文)**：`工业类 › 测试，测量 › 检查 › 泄漏检测工具`
  *   **A+数量占比**：`66%`
  *   **新品平均评分数**：`27`
  *   **新品平均价格**：`$ 86.38`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`331`
  *   **新品月均销售额**：`$10,235`
  *   **平均重量**：`1.45 pounds (655 g)`
  *   **平均体积**：`212.00 in³ (3,474 cm³)`
  *   **平均毛利率**：`69.31%`
  *   **卖家所属地**：`美国|53.0%`
  *   **搜索购买比**：`12.8‰`

---

#### 🏆 🟢-44. Optics Accessories (光学配件)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Shooting › Optics › Optics Accessories  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.88`
  *   **平均 Reviews (Avg Reviews)**：`354 个`
  *   **物理重量 (Weight)**：`0.20 lbs`
  *   **平均退货率 (Return Rate)**：`5.63%`
  *   **平均毛利率 (Profit Margin)**：`65.6%`
  *   **品牌集中度 (Brand Concentration)**：`52.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`44.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Shooting › Optics › Optics Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 射击 › 光学元件 › 光学配件`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 14.96`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`156`
  *   **新品月均销售额**：`$2,362`
  *   **平均重量**：`0.20 pounds (92 g)`
  *   **平均体积**：`30.48 in³ (499 cm³)`
  *   **平均毛利率**：`65.6%`
  *   **卖家所属地**：`美国|56.0%`
  *   **搜索购买比**：`6.2‰`

---

#### 🏆 🟢-45. Bait Traps (诱饵陷阱)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Baits & Accessories › Bait Traps  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.88`
  *   **平均 Reviews (Avg Reviews)**：`284 个`
  *   **物理重量 (Weight)**：`1.68 lbs`
  *   **平均退货率 (Return Rate)**：`3.31%`
  *   **平均毛利率 (Profit Margin)**：`54.09%`
  *   **品牌集中度 (Brand Concentration)**：`60.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Baits & Accessories › Bait Traps  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 钓鱼 › 鱼饵和配件 › 诱饵陷阱`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`4`
  *   **新品平均价格**：`$ 30.53`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`94`
  *   **新品月均销售额**：`$2,798`
  *   **平均重量**：`1.68 pounds (761 g)`
  *   **平均体积**：`551.17 in³ (9,032 cm³)`
  *   **平均毛利率**：`54.09%`
  *   **卖家所属地**：`中国|55.0%`
  *   **搜索购买比**：`4.5‰`

---

#### 🏆 🟢-46. Fly Tying Equipment (绑蝇设备)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Fly Fishing › Accessories › Fly Tying Equipment  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.02`
  *   **平均 Reviews (Avg Reviews)**：`478 个`
  *   **物理重量 (Weight)**：`0.30 lbs`
  *   **平均退货率 (Return Rate)**：`2.84%`
  *   **平均毛利率 (Profit Margin)**：`60.98%`
  *   **品牌集中度 (Brand Concentration)**：`62.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`53.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Fly Fishing › Accessories › Fly Tying Equipment  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 钓鱼 › 飞钓 › 配件 › 绑蝇设备`
  *   **A+数量占比**：`46%`
  *   **新品平均评分数**：`10`
  *   **新品平均价格**：`$ 15.17`
  *   **新品平均星级**：`2.3`
  *   **新品月均销量**：`107`
  *   **新品月均销售额**：`$1,603`
  *   **平均重量**：`0.30 pounds (135 g)`
  *   **平均体积**：`41.21 in³ (675 cm³)`
  *   **平均毛利率**：`60.98%`
  *   **卖家所属地**：`中国|53.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟢-47. Flags (标志)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Cabin Products › Flags  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.28`
  *   **平均 Reviews (Avg Reviews)**：`223 个`
  *   **物理重量 (Weight)**：`0.60 lbs`
  *   **平均退货率 (Return Rate)**：`2.61%`
  *   **平均毛利率 (Profit Margin)**：`60.53%`
  *   **品牌集中度 (Brand Concentration)**：`62.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Cabin Products › Flags  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 船用家具 › 标志`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 19.93`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`199`
  *   **新品月均销售额**：`$3,723`
  *   **平均重量**：`0.60 pounds (274 g)`
  *   **平均体积**：`132.06 in³ (2,164 cm³)`
  *   **平均毛利率**：`60.53%`
  *   **卖家所属地**：`中国|54.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟢-48. Growth Charts (身高墙贴)

- **完整市场路径**：`Baby Products › Nursery › Décor › Wall Décor › Growth Charts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.12`
  *   **平均 Reviews (Avg Reviews)**：`416 个`
  *   **物理重量 (Weight)**：`0.80 lbs`
  *   **平均退货率 (Return Rate)**：`3.72%`
  *   **平均毛利率 (Profit Margin)**：`57.59%`
  *   **品牌集中度 (Brand Concentration)**：`47.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Baby Products › Nursery › Décor › Wall Décor › Growth Charts  市场分析`
  *   **市场路径(中文)**：`婴儿产品 › 苗圃 › 装饰品 › 墙面装饰 › 身高墙贴`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 14.44`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`77`
  *   **新品月均销售额**：`$1,186`
  *   **平均重量**：`0.80 pounds (362 g)`
  *   **平均体积**：`254.76 in³ (4,175 cm³)`
  *   **平均毛利率**：`57.59%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟢-49. Tortilla Servers (玉米饼服务员)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Tortilla Servers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.25`
  *   **平均 Reviews (Avg Reviews)**：`454 个`
  *   **物理重量 (Weight)**：`1.57 lbs`
  *   **平均退货率 (Return Rate)**：`6.26%`
  *   **平均毛利率 (Profit Margin)**：`52.31%`
  *   **品牌集中度 (Brand Concentration)**：`58.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`38.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Tortilla Servers  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 小甜甜 › 碗碟 › 玉米饼服务员`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`16`
  *   **新品平均价格**：`$ 21.64`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`67`
  *   **新品月均销售额**：`$1,344`
  *   **平均重量**：`1.57 pounds (714 g)`
  *   **平均体积**：`143.50 in³ (2,352 cm³)`
  *   **平均毛利率**：`52.31%`
  *   **卖家所属地**：`中国|38.0%`
  *   **搜索购买比**：`6.5‰`

---

#### 🏆 🟢-50. Devotional Candles (祈祷蜡烛)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Candles & Holders › Candles › Specialty Candles › Devotional Candles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.95`
  *   **平均 Reviews (Avg Reviews)**：`191 个`
  *   **物理重量 (Weight)**：`1.74 lbs`
  *   **平均退货率 (Return Rate)**：`4.08%`
  *   **平均毛利率 (Profit Margin)**：`60.28%`
  *   **品牌集中度 (Brand Concentration)**：`61.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`56.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Candles & Holders › Candles › Specialty Candles › Devotional Candles  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 蜡烛 › 蜡烛 › 特种蜡烛 › 祈祷蜡烛`
  *   **A+数量占比**：`46%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 33.24`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`124`
  *   **新品月均销售额**：`$4,017`
  *   **平均重量**：`1.74 pounds (790 g)`
  *   **平均体积**：`14.22 in³ (233 cm³)`
  *   **平均毛利率**：`60.28%`
  *   **卖家所属地**：`美国|44.0%`
  *   **搜索购买比**：`5.8‰`

---

#### 🏆 🟢-51. Trim (装饰)

- **完整市场路径**：`Power & Hand Tools › Power Tool Parts & Accessories › Router Parts & Accessories › Router Bits › Straight, Spiral & Trim Bits › Trim  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.56`
  *   **平均 Reviews (Avg Reviews)**：`248 个`
  *   **物理重量 (Weight)**：`0.27 lbs`
  *   **平均退货率 (Return Rate)**：`2.44%`
  *   **平均毛利率 (Profit Margin)**：`67.05%`
  *   **品牌集中度 (Brand Concentration)**：`61.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Power & Hand Tools › Power Tool Parts & Accessories › Router Parts & Accessories › Router Bits › Straight, Spiral & Trim Bits › Trim  市场分析`
  *   **市场路径(中文)**：`电动和手动工具 › 电动工具零件 › 刳刨机零件 › 刳刨機鑽頭 › 直钻头、螺旋钻头和修整钻头 › 装饰`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`27`
  *   **新品平均价格**：`$ 36.54`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`119`
  *   **新品月均销售额**：`$4,349`
  *   **平均重量**：`0.27 pounds (122 g)`
  *   **平均体积**：`23.36 in³ (383 cm³)`
  *   **平均毛利率**：`67.05%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`11.3‰`

---

#### 🏆 🟢-52. Tools (工具)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Maintenance Supplies › Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.49`
  *   **平均 Reviews (Avg Reviews)**：`187 个`
  *   **物理重量 (Weight)**：`1.44 lbs`
  *   **平均退货率 (Return Rate)**：`3.64%`
  *   **平均毛利率 (Profit Margin)**：`63.11%`
  *   **品牌集中度 (Brand Concentration)**：`46.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Maintenance Supplies › Tools  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 维修器材 › 工具`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`11`
  *   **新品平均价格**：`$ 32.92`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`146`
  *   **新品月均销售额**：`$4,227`
  *   **平均重量**：`1.44 pounds (655 g)`
  *   **平均体积**：`97.76 in³ (1,602 cm³)`
  *   **平均毛利率**：`63.11%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`9.5‰`

---

#### 🏆 🟢-53. License Plate Frames (摩托车牌照架)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Body & Frame Parts › License Plate Frames  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.31`
  *   **平均 Reviews (Avg Reviews)**：`146 个`
  *   **物理重量 (Weight)**：`0.57 lbs`
  *   **平均退货率 (Return Rate)**：`4.18%`
  *   **平均毛利率 (Profit Margin)**：`57.56%`
  *   **品牌集中度 (Brand Concentration)**：`54.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Body & Frame Parts › License Plate Frames  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 部分 › 身体 › 摩托车牌照架`
  *   **A+数量占比**：`58%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 16.03`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`213`
  *   **新品月均销售额**：`$3,888`
  *   **平均重量**：`0.57 pounds (261 g)`
  *   **平均体积**：`60.92 in³ (998 cm³)`
  *   **平均毛利率**：`57.56%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`3.4‰`

---

#### 🏆 🟢-54. Gutters (排水沟)

- **完整市场路径**：`Tools & Home Improvement › Building Supplies › Building Materials › Roofing › Gutters & Accessories › Gutters  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.76`
  *   **平均 Reviews (Avg Reviews)**：`136 个`
  *   **物理重量 (Weight)**：`1.75 lbs`
  *   **平均退货率 (Return Rate)**：`5.02%`
  *   **平均毛利率 (Profit Margin)**：`54.67%`
  *   **品牌集中度 (Brand Concentration)**：`53.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Building Supplies › Building Materials › Roofing › Gutters & Accessories › Gutters  市场分析`
  *   **市场路径(中文)**：`工具 › 建筑用品 › 建筑材料 › 屋顶工程 › 排水沟 › 排水沟`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`14`
  *   **新品平均价格**：`$ 25.97`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`100`
  *   **新品月均销售额**：`$2,693`
  *   **平均重量**：`1.75 pounds (794 g)`
  *   **平均体积**：`444.24 in³ (7,280 cm³)`
  *   **平均毛利率**：`54.67%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`10.7‰`

---

#### 🏆 🟢-55. Fuel System (燃油系统)

- **完整市场路径**：`Automotive › Replacement Parts › Fuel System  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.65`
  *   **平均 Reviews (Avg Reviews)**：`98 个`
  *   **物理重量 (Weight)**：`0.65 lbs`
  *   **平均退货率 (Return Rate)**：`4.31%`
  *   **平均毛利率 (Profit Margin)**：`60.37%`
  *   **品牌集中度 (Brand Concentration)**：`49.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Fuel System  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 燃油系统`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`5`
  *   **新品平均价格**：`$ 29.57`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`104`
  *   **新品月均销售额**：`$2,835`
  *   **平均重量**：`0.65 pounds (294 g)`
  *   **平均体积**：`175.91 in³ (2,883 cm³)`
  *   **平均毛利率**：`60.37%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`12.3‰`

---

#### 🏆 🟢-56. Car Rack Parts & Accessories (汽车货架零件和配件)

- **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Accessories › Car Racks & Carriers › Car Rack Parts & Accessories  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$45.21`
  *   **平均 Reviews (Avg Reviews)**：`240 个`
  *   **物理重量 (Weight)**：`1.33 lbs`
  *   **平均退货率 (Return Rate)**：`6.72%`
  *   **平均毛利率 (Profit Margin)**：`63.92%`
  *   **品牌集中度 (Brand Concentration)**：`46.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`51.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Accessories › Car Racks & Carriers › Car Rack Parts & Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 外出休闲 › 配件 › 汽车货架和运输工具 › 汽车货架零件和配件`
  *   **A+数量占比**：`64%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 33.6`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`147`
  *   **新品月均销售额**：`$3,939`
  *   **平均重量**：`1.33 pounds (602 g)`
  *   **平均体积**：`470.07 in³ (7,703 cm³)`
  *   **平均毛利率**：`63.92%`
  *   **卖家所属地**：`中国|51.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟢-57. Serveware (碗碟)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Novelty › Serveware  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.08`
  *   **平均 Reviews (Avg Reviews)**：`429 个`
  *   **物理重量 (Weight)**：`1.49 lbs`
  *   **平均退货率 (Return Rate)**：`5.33%`
  *   **平均毛利率 (Profit Margin)**：`56.23%`
  *   **品牌集中度 (Brand Concentration)**：`57.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`58.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Novelty › Serveware  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 新颖性 › 碗碟`
  *   **A+数量占比**：`58%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 24.01`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`107`
  *   **新品月均销售额**：`$2,392`
  *   **平均重量**：`1.49 pounds (678 g)`
  *   **平均体积**：`316.57 in³ (5,188 cm³)`
  *   **平均毛利率**：`56.23%`
  *   **卖家所属地**：`中国|58.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟢-58. Collectible Vehicles (交通工具摆件)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Collectible Vehicles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.98`
  *   **平均 Reviews (Avg Reviews)**：`213 个`
  *   **物理重量 (Weight)**：`0.89 lbs`
  *   **平均退货率 (Return Rate)**：`5.81%`
  *   **平均毛利率 (Profit Margin)**：`57.46%`
  *   **品牌集中度 (Brand Concentration)**：`63.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Collectible Vehicles  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 交通工具摆件`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`33`
  *   **新品平均价格**：`$ 17.47`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`184`
  *   **新品月均销售额**：`$2,949`
  *   **平均重量**：`0.89 pounds (406 g)`
  *   **平均体积**：`165.98 in³ (2,720 cm³)`
  *   **平均毛利率**：`57.46%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟢-59. 3D Printer Extruders (3D打印机挤出机)

- **完整市场路径**：`Industrial & Scientific › Additive Manufacturing Products › 3D Printer Parts & Accessories › 3D Printer Extruders  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.77`
  *   **平均 Reviews (Avg Reviews)**：`157 个`
  *   **物理重量 (Weight)**：`0.18 lbs`
  *   **平均退货率 (Return Rate)**：`4.99%`
  *   **平均毛利率 (Profit Margin)**：`68.78%`
  *   **品牌集中度 (Brand Concentration)**：`58.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Additive Manufacturing Products › 3D Printer Parts & Accessories › 3D Printer Extruders  市场分析`
  *   **市场路径(中文)**：`工业类 › 增材制造产品 › 3D打印机零件 › 3D打印机挤出机`
  *   **A+数量占比**：`66%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 33.91`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`129`
  *   **新品月均销售额**：`$4,002`
  *   **平均重量**：`0.18 pounds (82 g)`
  *   **平均体积**：`18.60 in³ (305 cm³)`
  *   **平均毛利率**：`68.78%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`8.8‰`

---

#### 🏆 🟢-60. Mailbox Hardware (信箱硬件)

- **完整市场路径**：`Tools & Home Improvement › Hardware › Mailboxes & Accessories › Mailbox Accessories & Hardware › Mailbox Hardware  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.44`
  *   **平均 Reviews (Avg Reviews)**：`201 个`
  *   **物理重量 (Weight)**：`1.11 lbs`
  *   **平均退货率 (Return Rate)**：`7.65%`
  *   **平均毛利率 (Profit Margin)**：`57.05%`
  *   **品牌集中度 (Brand Concentration)**：`55.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Hardware › Mailboxes & Accessories › Mailbox Accessories & Hardware › Mailbox Hardware  市场分析`
  *   **市场路径(中文)**：`工具 › 硬件设施 › 邮箱 › 信箱配件 › 信箱硬件`
  *   **A+数量占比**：`49%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 21.61`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`75`
  *   **新品月均销售额**：`$1,486`
  *   **平均重量**：`1.11 pounds (504 g)`
  *   **平均体积**：`119.14 in³ (1,952 cm³)`
  *   **平均毛利率**：`57.05%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`14.4‰`

---

#### 🏆 🟢-61. Grill Lighting (点火器)

- **完整市场路径**：`Patio, Lawn & Garden › Grills & Outdoor Cooking › Outdoor Cooking Tools & Accessories › Grill Lighting  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$37.59`
  *   **平均 Reviews (Avg Reviews)**：`607 个`
  *   **物理重量 (Weight)**：`1.29 lbs`
  *   **平均退货率 (Return Rate)**：`5.43%`
  *   **平均毛利率 (Profit Margin)**：`63.44%`
  *   **品牌集中度 (Brand Concentration)**：`53.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`58.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Grills & Outdoor Cooking › Outdoor Cooking Tools & Accessories › Grill Lighting  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 烧烤用具 › 烤炉配件 › 点火器`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`20`
  *   **新品平均价格**：`$ 39.94`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`61`
  *   **新品月均销售额**：`$1,984`
  *   **平均重量**：`1.29 pounds (586 g)`
  *   **平均体积**：`233.91 in³ (3,833 cm³)`
  *   **平均毛利率**：`63.44%`
  *   **卖家所属地**：`中国|58.0%`
  *   **搜索购买比**：`6.3‰`

---

#### 🏆 🟢-62. Fuel (燃油表)

- **完整市场路径**：`Automotive › Replacement Parts › Lighting & Electrical › Electrical › Gauges › Fuel  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.69`
  *   **平均 Reviews (Avg Reviews)**：`107 个`
  *   **物理重量 (Weight)**：`0.38 lbs`
  *   **平均退货率 (Return Rate)**：`4.87%`
  *   **平均毛利率 (Profit Margin)**：`64.9%`
  *   **品牌集中度 (Brand Concentration)**：`51.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Lighting & Electrical › Electrical › Gauges › Fuel  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 照明及电气 › 电气 › 计量器 › 燃油表`
  *   **A+数量占比**：`66%`
  *   **新品平均评分数**：`5`
  *   **新品平均价格**：`$ 20.79`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`215`
  *   **新品月均销售额**：`$3,292`
  *   **平均重量**：`0.38 pounds (173 g)`
  *   **平均体积**：`62.51 in³ (1,024 cm³)`
  *   **平均毛利率**：`64.9%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`8.2‰`

---

#### 🏆 🟢-63. Deviled Egg Plates (咸蛋盘)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Dinnerware › Plates › Specialty Plates › Deviled Egg Plates  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.00`
  *   **平均 Reviews (Avg Reviews)**：`349 个`
  *   **物理重量 (Weight)**：`1.87 lbs`
  *   **平均退货率 (Return Rate)**：`5.01%`
  *   **平均毛利率 (Profit Margin)**：`51.41%`
  *   **品牌集中度 (Brand Concentration)**：`59.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`61.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Dinnerware › Plates › Specialty Plates › Deviled Egg Plates  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房和餐厅 › 餐饮与娱乐 › 餐具 › 餐具 › 板材 › 特色餐盘 › 咸蛋盘`
  *   **A+数量占比**：`78%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 23.97`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`86`
  *   **新品月均销售额**：`$2,049`
  *   **平均重量**：`1.87 pounds (848 g)`
  *   **平均体积**：`325.67 in³ (5,337 cm³)`
  *   **平均毛利率**：`51.41%`
  *   **卖家所属地**：`中国|61.0%`
  *   **搜索购买比**：`7.7‰`

---

#### 🏆 🟢-64. Aprons (围裙)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Gloves & Protective Gear › Aprons  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.00`
  *   **平均 Reviews (Avg Reviews)**：`72 个`
  *   **物理重量 (Weight)**：`0.75 lbs`
  *   **平均退货率 (Return Rate)**：`3.04%`
  *   **平均毛利率 (Profit Margin)**：`58.44%`
  *   **品牌集中度 (Brand Concentration)**：`58.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Gloves & Protective Gear › Aprons  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 手套和防护用具 › 围裙`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`6`
  *   **新品平均价格**：`$ 26.55`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`78`
  *   **新品月均销售额**：`$2,215`
  *   **平均重量**：`0.75 pounds (341 g)`
  *   **平均体积**：`254.96 in³ (4,178 cm³)`
  *   **平均毛利率**：`58.44%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`8.4‰`

---

#### 🏆 🟢-65. Nail Pullers (羊角起钉钳)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Nail Pullers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.20`
  *   **平均 Reviews (Avg Reviews)**：`371 个`
  *   **物理重量 (Weight)**：`1.20 lbs`
  *   **平均退货率 (Return Rate)**：`2.27%`
  *   **平均毛利率 (Profit Margin)**：`54.75%`
  *   **品牌集中度 (Brand Concentration)**：`61.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Nail Pullers  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具 › 羊角起钉钳`
  *   **A+数量占比**：`62%`
  *   **新品平均评分数**：`12`
  *   **新品平均价格**：`$ 10.91`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`99`
  *   **新品月均销售额**：`$836`
  *   **平均重量**：`1.20 pounds (546 g)`
  *   **平均体积**：`75.79 in³ (1,242 cm³)`
  *   **平均毛利率**：`54.75%`
  *   **卖家所属地**：`中国|55.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟢-66. Cheese Knives (奶酪刀)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Specialty Knives › Cheese Knives  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.33`
  *   **平均 Reviews (Avg Reviews)**：`542 个`
  *   **物理重量 (Weight)**：`0.65 lbs`
  *   **平均退货率 (Return Rate)**：`4.02%`
  *   **平均毛利率 (Profit Margin)**：`57.11%`
  *   **品牌集中度 (Brand Concentration)**：`47.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Specialty Knives › Cheese Knives  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 刀具厨房及配件 › 特种刀 › 奶酪刀`
  *   **A+数量占比**：`66%`
  *   **新品平均评分数**：`38`
  *   **新品平均价格**：`$ 17.45`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`61`
  *   **新品月均销售额**：`$915`
  *   **平均重量**：`0.65 pounds (293 g)`
  *   **平均体积**：`81.76 in³ (1,340 cm³)`
  *   **平均毛利率**：`57.11%`
  *   **卖家所属地**：`中国|48.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟢-67. Angle (角规)

- **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Dimensional Measurement › Gauges › Angle  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.14`
  *   **平均 Reviews (Avg Reviews)**：`386 个`
  *   **物理重量 (Weight)**：`0.56 lbs`
  *   **平均退货率 (Return Rate)**：`2.9%`
  *   **平均毛利率 (Profit Margin)**：`65.79%`
  *   **品牌集中度 (Brand Concentration)**：`60.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Dimensional Measurement › Gauges › Angle  市场分析`
  *   **市场路径(中文)**：`工业类 › 测试，测量 › 尺寸测量 › 计量器 › 角规`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 21.46`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`59`
  *   **新品月均销售额**：`$1,359`
  *   **平均重量**：`0.56 pounds (253 g)`
  *   **平均体积**：`27.85 in³ (456 cm³)`
  *   **平均毛利率**：`65.79%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`11.4‰`

---

#### 🏆 🟢-68. Card Playing (纸牌游戏)

- **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Mobility & Daily Living Aids › Low Strength Aids › Card Playing  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.06`
  *   **平均 Reviews (Avg Reviews)**：`198 个`
  *   **物理重量 (Weight)**：`0.78 lbs`
  *   **平均退货率 (Return Rate)**：`4.78%`
  *   **平均毛利率 (Profit Margin)**：`58.76%`
  *   **品牌集中度 (Brand Concentration)**：`58.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Mobility & Daily Living Aids › Low Strength Aids › Card Playing  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 医疗用品和设备 › 行动和日常生活辅助工具 › 力量辅助用品 › 纸牌游戏`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 20.55`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`100`
  *   **新品月均销售额**：`$2,014`
  *   **平均重量**：`0.78 pounds (354 g)`
  *   **平均体积**：`76.96 in³ (1,261 cm³)`
  *   **平均毛利率**：`58.76%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`10.3‰`

---

#### 🏆 🟢-69. Brazing Rods (钎杆)

- **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Soldering & Brazing Equipment › Solder & Flux › Brazing Rods  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$37.36`
  *   **平均 Reviews (Avg Reviews)**：`158 个`
  *   **物理重量 (Weight)**：`0.66 lbs`
  *   **平均退货率 (Return Rate)**：`2.03%`
  *   **平均毛利率 (Profit Margin)**：`62.88%`
  *   **品牌集中度 (Brand Concentration)**：`62.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`53.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Soldering & Brazing Equipment › Solder & Flux › Brazing Rods  市场分析`
  *   **市场路径(中文)**：`工具 › 焊接 › 焊接 › 焊接 › 钎杆`
  *   **A+数量占比**：`59%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 23.05`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`120`
  *   **新品月均销售额**：`$3,281`
  *   **平均重量**：`0.66 pounds (300 g)`
  *   **平均体积**：`24.82 in³ (407 cm³)`
  *   **平均毛利率**：`62.88%`
  *   **卖家所属地**：`中国|53.0%`
  *   **搜索购买比**：`10.0‰`

---

#### 🏆 🟢-70. Fixed-Blade Knives (固定刀刃的刀具)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Knives, Parts & Accessories › Knives › Fixed-Blade Knives  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$46.05`
  *   **平均 Reviews (Avg Reviews)**：`714 个`
  *   **物理重量 (Weight)**：`0.61 lbs`
  *   **平均退货率 (Return Rate)**：`3.09%`
  *   **平均毛利率 (Profit Margin)**：`69.51%`
  *   **品牌集中度 (Brand Concentration)**：`58.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`34.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Knives, Parts & Accessories › Knives › Fixed-Blade Knives  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具 › 刀具，零件 › 刀具 › 固定刀刃的刀具`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`42`
  *   **新品平均价格**：`$ 65.86`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`93`
  *   **新品月均销售额**：`$5,921`
  *   **平均重量**：`0.61 pounds (276 g)`
  *   **平均体积**：`148.87 in³ (2,440 cm³)`
  *   **平均毛利率**：`69.51%`
  *   **卖家所属地**：`美国|66.0%`
  *   **搜索购买比**：`2.7‰`

---

#### 🏆 🟢-71. Knitting Looms & Boards (编织机、织布机)

- **完整市场路径**：`Arts, Crafts & Sewing › Knitting & Crochet › Knitting Looms & Boards  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.48`
  *   **平均 Reviews (Avg Reviews)**：`453 个`
  *   **物理重量 (Weight)**：`1.77 lbs`
  *   **平均退货率 (Return Rate)**：`5.9%`
  *   **平均毛利率 (Profit Margin)**：`57.76%`
  *   **品牌集中度 (Brand Concentration)**：`49.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Knitting & Crochet › Knitting Looms & Boards  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 编织 › 编织机、织布机`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 33.3`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`73`
  *   **新品月均销售额**：`$2,489`
  *   **平均重量**：`1.77 pounds (802 g)`
  *   **平均体积**：`427.85 in³ (7,011 cm³)`
  *   **平均毛利率**：`57.76%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟢-72. Sheets (桌子)

- **完整市场路径**：`Industrial & Scientific › Raw Materials › Metals & Alloys › Stainless Steel › Sheets  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.11`
  *   **平均 Reviews (Avg Reviews)**：`89 个`
  *   **物理重量 (Weight)**：`1.94 lbs`
  *   **平均退货率 (Return Rate)**：`7.07%`
  *   **平均毛利率 (Profit Margin)**：`56.73%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Raw Materials › Metals & Alloys › Stainless Steel › Sheets  市场分析`
  *   **市场路径(中文)**：`工业类 › 素材 › 金属 › 不锈钢 › 桌子`
  *   **A+数量占比**：`58%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 73.39`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`85`
  *   **新品月均销售额**：`$4,688`
  *   **平均重量**：`1.94 pounds (878 g)`
  *   **平均体积**：`112.42 in³ (1,842 cm³)`
  *   **平均毛利率**：`56.73%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟢-73. Oil Pressure Tools (油压工具)

- **完整市场路径**：`Automotive › Tools & Equipment › Engine Tools › Oil Pressure Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.75`
  *   **平均 Reviews (Avg Reviews)**：`123 个`
  *   **物理重量 (Weight)**：`1.03 lbs`
  *   **平均退货率 (Return Rate)**：`5.44%`
  *   **平均毛利率 (Profit Margin)**：`58.97%`
  *   **品牌集中度 (Brand Concentration)**：`53.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Engine Tools › Oil Pressure Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 发动机工具 › 油压工具`
  *   **A+数量占比**：`60%`
  *   **新品平均评分数**：`10`
  *   **新品平均价格**：`$ 25.11`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`53`
  *   **新品月均销售额**：`$1,266`
  *   **平均重量**：`1.03 pounds (468 g)`
  *   **平均体积**：`93.53 in³ (1,533 cm³)`
  *   **平均毛利率**：`58.97%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`11.7‰`

---

#### 🏆 🟢-74. Carriers (外带用品)

- **完整市场路径**：`Pet Supplies › Small Animals › Carriers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.52`
  *   **平均 Reviews (Avg Reviews)**：`231 个`
  *   **物理重量 (Weight)**：`1.31 lbs`
  *   **平均退货率 (Return Rate)**：`6.02%`
  *   **平均毛利率 (Profit Margin)**：`53.29%`
  *   **品牌集中度 (Brand Concentration)**：`53.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Small Animals › Carriers  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 小宠用品 › 外带用品`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`11`
  *   **新品平均价格**：`$ 24.81`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`54`
  *   **新品月均销售额**：`$1,322`
  *   **平均重量**：`1.31 pounds (593 g)`
  *   **平均体积**：`795.79 in³ (13,041 cm³)`
  *   **平均毛利率**：`53.29%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`5.6‰`

---

#### 🏆 🟢-75. Embroidery Storage (绣花收纳)

- **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Embroidery Storage  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.36`
  *   **平均 Reviews (Avg Reviews)**：`194 个`
  *   **物理重量 (Weight)**：`1.37 lbs`
  *   **平均退货率 (Return Rate)**：`4.95%`
  *   **平均毛利率 (Profit Margin)**：`56.88%`
  *   **品牌集中度 (Brand Concentration)**：`53.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`87.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Embroidery Storage  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 组织，存储 › 工艺品 › 绣花收纳`
  *   **A+数量占比**：`51%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 24.63`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`51`
  *   **新品月均销售额**：`$1,135`
  *   **平均重量**：`1.37 pounds (619 g)`
  *   **平均体积**：`215.39 in³ (3,530 cm³)`
  *   **平均毛利率**：`56.88%`
  *   **卖家所属地**：`中国|87.0%`
  *   **搜索购买比**：`7.6‰`

---

#### 🏆 🟢-76. Hunting Dog Equipment (猎犬装备)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Hunting › Hunting Dog Equipment  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.83`
  *   **平均 Reviews (Avg Reviews)**：`278 个`
  *   **物理重量 (Weight)**：`0.95 lbs`
  *   **平均退货率 (Return Rate)**：`5.22%`
  *   **平均毛利率 (Profit Margin)**：`60.31%`
  *   **品牌集中度 (Brand Concentration)**：`60.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`42.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Hunting › Hunting Dog Equipment  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 惺惺相惜 › 猎犬装备`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 31.57`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`53`
  *   **新品月均销售额**：`$1,376`
  *   **平均重量**：`0.95 pounds (433 g)`
  *   **平均体积**：`273.86 in³ (4,488 cm³)`
  *   **平均毛利率**：`60.31%`
  *   **卖家所属地**：`美国|58.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-77. UV Phone Sterilizer Boxes (紫外线手机消毒盒)

- **完整市场路径**：`Cell Phones & Accessories › Accessories › UV Phone Sterilizer Boxes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$62.46`
  *   **平均 Reviews (Avg Reviews)**：`341 个`
  *   **物理重量 (Weight)**：`1.97 lbs`
  *   **平均退货率 (Return Rate)**：`7.51%`
  *   **平均毛利率 (Profit Margin)**：`73.72%`
  *   **品牌集中度 (Brand Concentration)**：`63.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`27.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Cell Phones & Accessories › Accessories › UV Phone Sterilizer Boxes  市场分析`
  *   **市场路径(中文)**：`手机 › 辅料 › 紫外线手机消毒盒`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`11`
  *   **新品平均价格**：`$ 49.22`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`31`
  *   **新品月均销售额**：`$1,451`
  *   **平均重量**：`1.97 pounds (894 g)`
  *   **平均体积**：`471.85 in³ (7,732 cm³)`
  *   **平均毛利率**：`73.72%`
  *   **卖家所属地**：`美国|73.0%`
  *   **搜索购买比**：`9.5‰`

---

#### 🏆 🟢-78. Paper Craft Tools (纸工艺工具)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Paper & Paper Crafts › Paper Craft Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.65`
  *   **平均 Reviews (Avg Reviews)**：`306 个`
  *   **物理重量 (Weight)**：`1.78 lbs`
  *   **平均退货率 (Return Rate)**：`4.13%`
  *   **平均毛利率 (Profit Margin)**：`59.71%`
  *   **品牌集中度 (Brand Concentration)**：`58.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`49.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Paper & Paper Crafts › Paper Craft Tools  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 报纸 › 纸工艺工具`
  *   **A+数量占比**：`62%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 46.75`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`87`
  *   **新品月均销售额**：`$4,263`
  *   **平均重量**：`1.78 pounds (808 g)`
  *   **平均体积**：`199.53 in³ (3,270 cm³)`
  *   **平均毛利率**：`59.71%`
  *   **卖家所属地**：`中国|49.0%`
  *   **搜索购买比**：`9.2‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Outdoor Statues (户外雕像)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Outdoor Statues  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.31`
  *   **平均 Reviews (Avg Reviews)**：`918 个`
  *   **物理重量 (Weight)**：`1.11 lbs`
  *   **平均退货率 (Return Rate)**：`2.98%`
  *   **平均毛利率 (Profit Margin)**：`56.91%`
  *   **品牌集中度 (Brand Concentration)**：`45.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Outdoor Statues  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 雕塑、雕像 › 户外雕像`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`64`
  *   **新品平均价格**：`$ 22.95`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`1,291`
  *   **新品月均销售额**：`$28,254`
  *   **平均重量**：`1.11 pounds (503 g)`
  *   **平均体积**：`457.58 in³ (7,498 cm³)`
  *   **平均毛利率**：`56.91%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`5.1‰`

---

#### 🏆 🟡-2. Liver Extracts (肝脏提取物)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Glandular Extracts › Liver Extracts  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.26`
  *   **平均 Reviews (Avg Reviews)**：`843 个`
  *   **物理重量 (Weight)**：`0.28 lbs`
  *   **平均退货率 (Return Rate)**：`0.31%`
  *   **平均毛利率 (Profit Margin)**：`68.49%`
  *   **品牌集中度 (Brand Concentration)**：`63.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`18.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Glandular Extracts › Liver Extracts  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 身、泳和附剂 › 圣诞体提取物 › 肝脏提取物`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`66`
  *   **新品平均价格**：`$ 30.85`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`1,049`
  *   **新品月均销售额**：`$34,768`
  *   **平均重量**：`0.28 pounds (126 g)`
  *   **平均体积**：`44.94 in³ (736 cm³)`
  *   **平均毛利率**：`68.49%`
  *   **卖家所属地**：`美国|82.0%`
  *   **搜索购买比**：`22.9‰`

---

#### 🏆 🟡-3. Squirt Guns (水枪)

- **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.30`
  *   **平均 Reviews (Avg Reviews)**：`616 个`
  *   **物理重量 (Weight)**：`1.54 lbs`
  *   **平均退货率 (Return Rate)**：`3.93%`
  *   **平均毛利率 (Profit Margin)**：`53.31%`
  *   **品牌集中度 (Brand Concentration)**：`51.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
  *   **市场路径(中文)**：`玩具 › 体育 › 游泳池 › 水枪`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`140`
  *   **新品平均价格**：`$ 31.86`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`1,440`
  *   **新品月均销售额**：`$41,866`
  *   **平均重量**：`1.54 pounds (700 g)`
  *   **平均体积**：`324.80 in³ (5,323 cm³)`
  *   **平均毛利率**：`53.31%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`5.7‰`

---

#### 🏆 🟡-4. Grill Pads & Floor Mats (烤炉垫和地垫)

- **完整市场路径**：`Patio, Lawn & Garden › Grills & Outdoor Cooking › Outdoor Cooking Tools & Accessories › Grill Pads & Floor Mats  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.02`
  *   **平均 Reviews (Avg Reviews)**：`976 个`
  *   **物理重量 (Weight)**：`1.73 lbs`
  *   **平均退货率 (Return Rate)**：`3.25%`
  *   **平均毛利率 (Profit Margin)**：`54.47%`
  *   **品牌集中度 (Brand Concentration)**：`50.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Grills & Outdoor Cooking › Outdoor Cooking Tools & Accessories › Grill Pads & Floor Mats  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 烧烤用具 › 烤炉配件 › 烤炉垫和地垫`
  *   **A+数量占比**：`92%`
  *   **新品平均评分数**：`142`
  *   **新品平均价格**：`$ 23`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`1,410`
  *   **新品月均销售额**：`$28,177`
  *   **平均重量**：`1.73 pounds (787 g)`
  *   **平均体积**：`422.91 in³ (6,930 cm³)`
  *   **平均毛利率**：`54.47%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`11.6‰`

---

#### 🏆 🟡-5. Self-Watering Stakes (自浇水桩)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Pots, Planters & Container Accessories › Plant Container Accessories › Self-Watering Stakes  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.73`
  *   **平均 Reviews (Avg Reviews)**：`840 个`
  *   **物理重量 (Weight)**：`1.49 lbs`
  *   **平均退货率 (Return Rate)**：`2.8%`
  *   **平均毛利率 (Profit Margin)**：`52.69%`
  *   **品牌集中度 (Brand Concentration)**：`53.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Pots, Planters & Container Accessories › Plant Container Accessories › Self-Watering Stakes  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 花盆、花架、育苗盘 › 花盆配件 › 自浇水桩`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`463`
  *   **新品平均价格**：`$ 20.43`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`643`
  *   **新品月均销售额**：`$12,745`
  *   **平均重量**：`1.49 pounds (676 g)`
  *   **平均体积**：`141.70 in³ (2,322 cm³)`
  *   **平均毛利率**：`52.69%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`12.2‰`

---

#### 🏆 🟡-6. Bread Knives (面包刀)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Bread Knives  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.57`
  *   **平均 Reviews (Avg Reviews)**：`998 个`
  *   **物理重量 (Weight)**：`0.81 lbs`
  *   **平均退货率 (Return Rate)**：`2.92%`
  *   **平均毛利率 (Profit Margin)**：`54.32%`
  *   **品牌集中度 (Brand Concentration)**：`52.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Bread Knives  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 刀具厨房及配件 › 面包刀`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`107`
  *   **新品平均价格**：`$ 17.46`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`617`
  *   **新品月均销售额**：`$9,688`
  *   **平均重量**：`0.81 pounds (368 g)`
  *   **平均体积**：`152.33 in³ (2,496 cm³)`
  *   **平均毛利率**：`54.32%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`13.5‰`

---

#### 🏆 🟡-7. Pool & Deck Repair Products (油漆及密封产品)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.75`
  *   **平均 Reviews (Avg Reviews)**：`679 个`
  *   **物理重量 (Weight)**：`2.41 lbs`
  *   **平均退货率 (Return Rate)**：`1.93%`
  *   **平均毛利率 (Profit Margin)**：`58.52%`
  *   **品牌集中度 (Brand Concentration)**：`56.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`47.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Pool & Deck Repair Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 油漆及密封产品`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`56`
  *   **新品平均价格**：`$ 19.64`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`631`
  *   **新品月均销售额**：`$12,599`
  *   **平均重量**：`2.41 pounds (1,094 g)`
  *   **平均体积**：`638.63 in³ (10,465 cm³)`
  *   **平均毛利率**：`58.52%`
  *   **卖家所属地**：`美国|53.0%`
  *   **搜索购买比**：`23.2‰`

---

#### 🏆 🟡-8. Fountains (喷泉)

- **完整市场路径**：`Pet Supplies › Dogs › Feeding & Watering Supplies › Fountains  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.99`
  *   **平均 Reviews (Avg Reviews)**：`961 个`
  *   **物理重量 (Weight)**：`2.18 lbs`
  *   **平均退货率 (Return Rate)**：`4.78%`
  *   **平均毛利率 (Profit Margin)**：`63.77%`
  *   **品牌集中度 (Brand Concentration)**：`56.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Dogs › Feeding & Watering Supplies › Fountains  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 犬类 › 喂食 › 喷泉`
  *   **A+数量占比**：`93%`
  *   **新品平均评分数**：`61`
  *   **新品平均价格**：`$ 45.07`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`549`
  *   **新品月均销售额**：`$24,431`
  *   **平均重量**：`2.18 pounds (990 g)`
  *   **平均体积**：`541.69 in³ (8,877 cm³)`
  *   **平均毛利率**：`63.77%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`10.2‰`

---

#### 🏆 🟡-9. Trays & Bags (托盘、口袋)

- **完整市场路径**：`Automotive › Interior Accessories › Consoles & Organizers › Trays & Bags  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.80`
  *   **平均 Reviews (Avg Reviews)**：`874 个`
  *   **物理重量 (Weight)**：`1.19 lbs`
  *   **平均退货率 (Return Rate)**：`9.42%`
  *   **平均毛利率 (Profit Margin)**：`55.88%`
  *   **品牌集中度 (Brand Concentration)**：`46.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`89.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Interior Accessories › Consoles & Organizers › Trays & Bags  市场分析`
  *   **市场路径(中文)**：`汽车 › 内部配件 › 控制台 › 托盘、口袋`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`163`
  *   **新品平均价格**：`$ 17.42`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`654`
  *   **新品月均销售额**：`$11,743`
  *   **平均重量**：`1.19 pounds (541 g)`
  *   **平均体积**：`300.72 in³ (4,928 cm³)`
  *   **平均毛利率**：`55.88%`
  *   **卖家所属地**：`中国|89.0%`
  *   **搜索购买比**：`5.9‰`

---

#### 🏆 🟡-10. Glasses & Goggles (眼镜和护目镜)

- **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Glasses & Goggles  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.58`
  *   **平均 Reviews (Avg Reviews)**：`887 个`
  *   **物理重量 (Weight)**：`0.23 lbs`
  *   **平均退货率 (Return Rate)**：`6.05%`
  *   **平均毛利率 (Profit Margin)**：`63.74%`
  *   **品牌集中度 (Brand Concentration)**：`55.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`88.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Glasses & Goggles  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 骑自行车 › 眼镜和护目镜`
  *   **A+数量占比**：`94%`
  *   **新品平均评分数**：`60`
  *   **新品平均价格**：`$ 19.05`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`726`
  *   **新品月均销售额**：`$10,263`
  *   **平均重量**：`0.23 pounds (106 g)`
  *   **平均体积**：`64.46 in³ (1,056 cm³)`
  *   **平均毛利率**：`63.74%`
  *   **卖家所属地**：`中国|88.0%`
  *   **搜索购买比**：`6.3‰`

---

#### 🏆 🟡-11. Compressed Air Dusters (压缩除尘罐)

- **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$34.09`
  *   **平均 Reviews (Avg Reviews)**：`349 个`
  *   **物理重量 (Weight)**：`0.87 lbs`
  *   **平均退货率 (Return Rate)**：`3.16%`
  *   **平均毛利率 (Profit Margin)**：`73.6%`
  *   **品牌集中度 (Brand Concentration)**：`60.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
  *   **市场路径(中文)**：`电子产品 › 计算机 › 电脑配件 › 清洁 › 压缩除尘罐`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`126`
  *   **新品平均价格**：`$ 32.03`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`521`
  *   **新品月均销售额**：`$15,746`
  *   **平均重量**：`0.87 pounds (396 g)`
  *   **平均体积**：`44.91 in³ (736 cm³)`
  *   **平均毛利率**：`73.6%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`13.0‰`

---

#### 🏆 🟡-12. Wind Spinners (Wind Spinners)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.21`
  *   **平均 Reviews (Avg Reviews)**：`472 个`
  *   **物理重量 (Weight)**：`2.48 lbs`
  *   **平均退货率 (Return Rate)**：`3.09%`
  *   **平均毛利率 (Profit Margin)**：`59.39%`
  *   **品牌集中度 (Brand Concentration)**：`53.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`92.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Wind Sculptures & Spinners › Wind Spinners`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`50`
  *   **新品平均价格**：`$ 20.62`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`742`
  *   **新品月均销售额**：`$12,317`
  *   **平均重量**：`2.48 pounds (1,126 g)`
  *   **平均体积**：`258.08 in³ (4,229 cm³)`
  *   **平均毛利率**：`59.39%`
  *   **卖家所属地**：`中国|92.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟡-13. Birdhouses (鸟屋)

- **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Birds › Birdhouses  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.93`
  *   **平均 Reviews (Avg Reviews)**：`620 个`
  *   **物理重量 (Weight)**：`2.16 lbs`
  *   **平均退货率 (Return Rate)**：`2.92%`
  *   **平均毛利率 (Profit Margin)**：`56.69%`
  *   **品牌集中度 (Brand Concentration)**：`52.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Birds › Birdhouses  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Birds › 鸟屋`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`37`
  *   **新品平均价格**：`$ 24.17`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`517`
  *   **新品月均销售额**：`$11,474`
  *   **平均重量**：`2.16 pounds (981 g)`
  *   **平均体积**：`573.61 in³ (9,400 cm³)`
  *   **平均毛利率**：`56.69%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`7.2‰`

---

#### 🏆 🟡-14. Batteries & Battery Chargers (电池和电池)

- **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.82`
  *   **平均 Reviews (Avg Reviews)**：`482 个`
  *   **物理重量 (Weight)**：`0.96 lbs`
  *   **平均退货率 (Return Rate)**：`9.83%`
  *   **平均毛利率 (Profit Margin)**：`62.31%`
  *   **品牌集中度 (Brand Concentration)**：`61.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`85.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 溜冰鞋、滑板和滑板车 › 自行车车 › 自行车车配件 › 电池和电池`
  *   **A+数量占比**：`78%`
  *   **新品平均评分数**：`64`
  *   **新品平均价格**：`$ 24.85`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`508`
  *   **新品月均销售额**：`$13,199`
  *   **平均重量**：`0.96 pounds (433 g)`
  *   **平均体积**：`56.73 in³ (930 cm³)`
  *   **平均毛利率**：`62.31%`
  *   **卖家所属地**：`中国|85.0%`
  *   **搜索购买比**：`9.9‰`

---

#### 🏆 🟡-15. Battery Switches (接线柱)

- **完整市场路径**：`Automotive › Replacement Parts › Batteries & Accessories › Battery Accessories › Battery Switches  市场分析`
- **触发警示项**：`带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.79`
  *   **平均 Reviews (Avg Reviews)**：`602 个`
  *   **物理重量 (Weight)**：`0.66 lbs`
  *   **平均退货率 (Return Rate)**：`5.58%`
  *   **平均毛利率 (Profit Margin)**：`58.75%`
  *   **品牌集中度 (Brand Concentration)**：`54.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Batteries & Accessories › Battery Accessories › Battery Switches  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 电池 › 电池配件 › 接线柱`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`36`
  *   **新品平均价格**：`$ 15.48`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`583`
  *   **新品月均销售额**：`$8,409`
  *   **平均重量**：`0.66 pounds (300 g)`
  *   **平均体积**：`34.63 in³ (567 cm³)`
  *   **平均毛利率**：`58.75%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`12.7‰`

---

#### 🏆 🟡-16. Paddleboard Accessories (冲浪板配件)

- **完整市场路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$53.14`
  *   **平均 Reviews (Avg Reviews)**：`345 个`
  *   **物理重量 (Weight)**：`2.42 lbs`
  *   **平均退货率 (Return Rate)**：`4.17%`
  *   **平均毛利率 (Profit Margin)**：`64.7%`
  *   **品牌集中度 (Brand Concentration)**：`44.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Water Sports › Stand-Up Paddleboarding › Paddleboard Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 划船和你 › 立式单肩肩背 › 冲浪板配件`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`33`
  *   **新品平均价格**：`$ 76.21`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`595`
  *   **新品月均销售额**：`$45,046`
  *   **平均重量**：`2.42 pounds (1,096 g)`
  *   **平均体积**：`448.52 in³ (7,350 cm³)`
  *   **平均毛利率**：`64.7%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟡-17. Poultry Fountains & Waterers (家禽自动喂水器和饮水器)

- **完整市场路径**：`Patio, Lawn & Garden › Farm & Ranch › Poultry Care › Poultry Feeding & Watering Supplies › Poultry Fountains & Waterers  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.74`
  *   **平均 Reviews (Avg Reviews)**：`615 个`
  *   **物理重量 (Weight)**：`2.19 lbs`
  *   **平均退货率 (Return Rate)**：`2.74%`
  *   **平均毛利率 (Profit Margin)**：`51.17%`
  *   **品牌集中度 (Brand Concentration)**：`56.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Farm & Ranch › Poultry Care › Poultry Feeding & Watering Supplies › Poultry Fountains & Waterers  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 农场和牧场 › 家禽养护 › 家禽喂食喂水用具 › 家禽自动喂水器和饮水器`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`33`
  *   **新品平均价格**：`$ 45.45`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`361`
  *   **新品月均销售额**：`$15,569`
  *   **平均重量**：`2.19 pounds (993 g)`
  *   **平均体积**：`770.61 in³ (12,628 cm³)`
  *   **平均毛利率**：`51.17%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`9.7‰`

---

#### 🏆 🟡-18. Replacement Sensors (更换传感器)

- **完整市场路径**：`Automotive › Tires & Wheels › Accessories & Parts › Tire Pressure Monitoring Systems (TPMS) › Replacement Sensors  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$46.99`
  *   **平均 Reviews (Avg Reviews)**：`999 个`
  *   **物理重量 (Weight)**：`0.47 lbs`
  *   **平均退货率 (Return Rate)**：`9.2%`
  *   **平均毛利率 (Profit Margin)**：`68.09%`
  *   **品牌集中度 (Brand Concentration)**：`61.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tires & Wheels › Accessories & Parts › Tire Pressure Monitoring Systems (TPMS) › Replacement Sensors  市场分析`
  *   **市场路径(中文)**：`汽车 › 轮胎轮胎 › 辅料 › 轮胎压力监测系统 (TPMS) › 更换传感器`
  *   **A+数量占比**：`93%`
  *   **新品平均评分数**：`64`
  *   **新品平均价格**：`$ 16.29`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`430`
  *   **新品月均销售额**：`$7,442`
  *   **平均重量**：`0.47 pounds (212 g)`
  *   **平均体积**：`43.03 in³ (705 cm³)`
  *   **平均毛利率**：`68.09%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`10.2‰`

---

#### 🏆 🟡-19. Neon Accent Lights (霓虹灯)

- **完整市场路径**：`Automotive › Lights, Bulbs & Indicators › Accent & Off Road Lighting › LED & Neon Lights › Neon Accent Lights  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.14`
  *   **平均 Reviews (Avg Reviews)**：`944 个`
  *   **物理重量 (Weight)**：`0.83 lbs`
  *   **平均退货率 (Return Rate)**：`6.23%`
  *   **平均毛利率 (Profit Margin)**：`61.7%`
  *   **品牌集中度 (Brand Concentration)**：`53.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`87.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Lights, Bulbs & Indicators › Accent & Off Road Lighting › LED & Neon Lights › Neon Accent Lights  市场分析`
  *   **市场路径(中文)**：`汽车 › 灯光 › 重音 › LED › 霓虹灯`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`304`
  *   **新品平均价格**：`$ 23.97`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`596`
  *   **新品月均销售额**：`$15,354`
  *   **平均重量**：`0.83 pounds (375 g)`
  *   **平均体积**：`74.50 in³ (1,221 cm³)`
  *   **平均毛利率**：`61.7%`
  *   **卖家所属地**：`中国|87.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟡-20. Hand Tools (手动工具)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.88`
  *   **平均 Reviews (Avg Reviews)**：`945 个`
  *   **物理重量 (Weight)**：`1.46 lbs`
  *   **平均退货率 (Return Rate)**：`3.71%`
  *   **平均毛利率 (Profit Margin)**：`56.79%`
  *   **品牌集中度 (Brand Concentration)**：`48.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`51.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`57`
  *   **新品平均价格**：`$ 25.07`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`447`
  *   **新品月均销售额**：`$8,997`
  *   **平均重量**：`1.46 pounds (663 g)`
  *   **平均体积**：`160.89 in³ (2,637 cm³)`
  *   **平均毛利率**：`56.79%`
  *   **卖家所属地**：`中国|51.0%`
  *   **搜索购买比**：`14.6‰`

---

#### 🏆 🟡-21. Decorative Trays (装饰性托盘)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.03`
  *   **平均 Reviews (Avg Reviews)**：`492 个`
  *   **物理重量 (Weight)**：`1.52 lbs`
  *   **平均退货率 (Return Rate)**：`9.52%`
  *   **平均毛利率 (Profit Margin)**：`57.22%`
  *   **品牌集中度 (Brand Concentration)**：`43.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰性托盘`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`128`
  *   **新品平均价格**：`$ 19.9`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`933`
  *   **新品月均销售额**：`$16,296`
  *   **平均重量**：`1.52 pounds (688 g)`
  *   **平均体积**：`214.31 in³ (3,512 cm³)`
  *   **平均毛利率**：`57.22%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟡-22. Trucks (卡车)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Trucks  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$67.37`
  *   **平均 Reviews (Avg Reviews)**：`868 个`
  *   **物理重量 (Weight)**：`2.48 lbs`
  *   **平均退货率 (Return Rate)**：`7.79%`
  *   **平均毛利率 (Profit Margin)**：`67.1%`
  *   **品牌集中度 (Brand Concentration)**：`48.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Trucks  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 卡车`
  *   **A+数量占比**：`96%`
  *   **新品平均评分数**：`147`
  *   **新品平均价格**：`$ 74.16`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`290`
  *   **新品月均销售额**：`$18,262`
  *   **平均重量**：`2.48 pounds (1,126 g)`
  *   **平均体积**：`440.11 in³ (7,212 cm³)`
  *   **平均毛利率**：`67.1%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`1.9‰`

---

#### 🏆 🟡-23. Game Mats & Boards (游戏垫和游戏板)

- **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.04`
  *   **平均 Reviews (Avg Reviews)**：`326 个`
  *   **物理重量 (Weight)**：`2.47 lbs`
  *   **平均退货率 (Return Rate)**：`7.5%`
  *   **平均毛利率 (Profit Margin)**：`58.17%`
  *   **品牌集中度 (Brand Concentration)**：`42.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Mats & Boards  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 游戏配件 › 游戏垫和游戏板`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`30`
  *   **新品平均价格**：`$ 34.12`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`371`
  *   **新品月均销售额**：`$12,491`
  *   **平均重量**：`2.47 pounds (1,121 g)`
  *   **平均体积**：`317.34 in³ (5,200 cm³)`
  *   **平均毛利率**：`58.17%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`3.8‰`

---

#### 🏆 🟡-24. Hand Exercisers (手部锻炼器具)

- **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Occupational & Physical Therapy Aids › Hand Exercisers  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.96`
  *   **平均 Reviews (Avg Reviews)**：`806 个`
  *   **物理重量 (Weight)**：`1.35 lbs`
  *   **平均退货率 (Return Rate)**：`5.3%`
  *   **平均毛利率 (Profit Margin)**：`59.52%`
  *   **品牌集中度 (Brand Concentration)**：`63.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Occupational & Physical Therapy Aids › Hand Exercisers  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 医疗用品和设备 › 职业和物理疗法辅助用品 › 手部锻炼器具`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 38.91`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`147`
  *   **新品月均销售额**：`$4,686`
  *   **平均重量**：`1.35 pounds (613 g)`
  *   **平均体积**：`121.47 in³ (1,991 cm³)`
  *   **平均毛利率**：`59.52%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`9.3‰`

---

#### 🏆 🟡-25. Motion Detectors (生命探测器)

- **完整市场路径**：`Electronics › Security & Surveillance › Motion Detectors  市场分析`
- **触发警示项**：`Reviews偏高 (>800), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.80`
  *   **平均 Reviews (Avg Reviews)**：`899 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`6.68%`
  *   **平均毛利率 (Profit Margin)**：`76.74%`
  *   **品牌集中度 (Brand Concentration)**：`60.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Security & Surveillance › Motion Detectors  市场分析`
  *   **市场路径(中文)**：`电子产品 › 安全问题 › 生命探测器`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`71`
  *   **新品平均价格**：`$ 34.74`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`263`
  *   **新品月均销售额**：`$10,162`
  *   **平均重量**：`0.71 pounds (321 g)`
  *   **平均体积**：`82.35 in³ (1,350 cm³)`
  *   **平均毛利率**：`76.74%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟡-26. Airbrush Sets (喷漆套装)

- **完整市场路径**：`Arts, Crafts & Sewing › Painting, Drawing & Art Supplies › Painting › Airbrush Materials › Airbrush Sets  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$51.53`
  *   **平均 Reviews (Avg Reviews)**：`901 个`
  *   **物理重量 (Weight)**：`2.50 lbs`
  *   **平均退货率 (Return Rate)**：`4.67%`
  *   **平均毛利率 (Profit Margin)**：`67.57%`
  *   **品牌集中度 (Brand Concentration)**：`58.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Painting, Drawing & Art Supplies › Painting › Airbrush Materials › Airbrush Sets  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 油画、素描 › 绘画 › 喷漆材料 › 喷漆套装`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`128`
  *   **新品平均价格**：`$ 44.75`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`244`
  *   **新品月均销售额**：`$11,966`
  *   **平均重量**：`2.50 pounds (1,133 g)`
  *   **平均体积**：`397.46 in³ (6,513 cm³)`
  *   **平均毛利率**：`67.57%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`5.3‰`

---

#### 🏆 🟡-27. Welding Helmets (焊接头盔)

- **完整市场路径**：`Tools & Home Improvement › Safety & Security › Personal Protective Equipment › Head Protection › Welding Helmets  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$61.89`
  *   **平均 Reviews (Avg Reviews)**：`874 个`
  *   **物理重量 (Weight)**：`1.16 lbs`
  *   **平均退货率 (Return Rate)**：`3.46%`
  *   **平均毛利率 (Profit Margin)**：`64.55%`
  *   **品牌集中度 (Brand Concentration)**：`62.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Safety & Security › Personal Protective Equipment › Head Protection › Welding Helmets  市场分析`
  *   **市场路径(中文)**：`工具 › 安全问题 › 个人防护设备 › 头部保护 › 焊接头盔`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`221`
  *   **新品平均价格**：`$ 76.02`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`247`
  *   **新品月均销售额**：`$19,661`
  *   **平均重量**：`1.16 pounds (526 g)`
  *   **平均体积**：`524.95 in³ (8,602 cm³)`
  *   **平均毛利率**：`64.55%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`5.0‰`

---

#### 🏆 🟡-28. Alternative Medicine (替代药物)

- **完整市场路径**：`Health & Household › Health Care › Alternative Medicine  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$39.92`
  *   **平均 Reviews (Avg Reviews)**：`940 个`
  *   **物理重量 (Weight)**：`0.54 lbs`
  *   **平均退货率 (Return Rate)**：`2.58%`
  *   **平均毛利率 (Profit Margin)**：`68.42%`
  *   **品牌集中度 (Brand Concentration)**：`58.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Alternative Medicine  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 替代药物`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`16`
  *   **新品平均价格**：`$ 55.13`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`227`
  *   **新品月均销售额**：`$7,246`
  *   **平均重量**：`0.54 pounds (243 g)`
  *   **平均体积**：`100.15 in³ (1,641 cm³)`
  *   **平均毛利率**：`68.42%`
  *   **卖家所属地**：`美国|52.0%`
  *   **搜索购买比**：`15.3‰`

---

#### 🏆 🟡-29. Handlebar Mounts (Handlebar Mounts)

- **完整市场路径**：`Cell Phones & Accessories › Accessories › Mounts › Handlebar Mounts  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.03`
  *   **平均 Reviews (Avg Reviews)**：`851 个`
  *   **物理重量 (Weight)**：`0.86 lbs`
  *   **平均退货率 (Return Rate)**：`5.37%`
  *   **平均毛利率 (Profit Margin)**：`68.85%`
  *   **品牌集中度 (Brand Concentration)**：`61.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Cell Phones & Accessories › Accessories › Mounts › Handlebar Mounts  市场分析`
  *   **市场路径(中文)**：`Cell Phones & Accessories › Accessories › Mounts › Handlebar Mounts`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`69`
  *   **新品平均价格**：`$ 17.98`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`179`
  *   **新品月均销售额**：`$3,030`
  *   **平均重量**：`0.86 pounds (390 g)`
  *   **平均体积**：`43.53 in³ (713 cm³)`
  *   **平均毛利率**：`68.85%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`8.0‰`

---

#### 🏆 🟡-30. Boats (船)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$56.23`
  *   **平均 Reviews (Avg Reviews)**：`338 个`
  *   **物理重量 (Weight)**：`1.49 lbs`
  *   **平均退货率 (Return Rate)**：`6.03%`
  *   **平均毛利率 (Profit Margin)**：`68.92%`
  *   **品牌集中度 (Brand Concentration)**：`61.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 船`
  *   **A+数量占比**：`96%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 55.97`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`308`
  *   **新品月均销售额**：`$14,868`
  *   **平均重量**：`1.49 pounds (676 g)`
  *   **平均体积**：`317.49 in³ (5,203 cm³)`
  *   **平均毛利率**：`68.92%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`2.9‰`

---

#### 🏆 🟡-31. Remote & App Controlled Vehicle Batteries (遥控)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicle Parts › Remote & App Controlled Vehicle Batteries  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.60`
  *   **平均 Reviews (Avg Reviews)**：`455 个`
  *   **物理重量 (Weight)**：`0.38 lbs`
  *   **平均退货率 (Return Rate)**：`6.27%`
  *   **平均毛利率 (Profit Margin)**：`66.93%`
  *   **品牌集中度 (Brand Concentration)**：`58.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicle Parts › Remote & App Controlled Vehicle Batteries  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 遥控`
  *   **A+数量占比**：`62%`
  *   **新品平均评分数**：`37`
  *   **新品平均价格**：`$ 35.14`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`308`
  *   **新品月均销售额**：`$10,425`
  *   **平均重量**：`0.38 pounds (171 g)`
  *   **平均体积**：`26.41 in³ (433 cm³)`
  *   **平均毛利率**：`66.93%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟡-32. Sewing Storage (缝纫用品收纳用品)

- **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Sewing Storage  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.93`
  *   **平均 Reviews (Avg Reviews)**：`929 个`
  *   **物理重量 (Weight)**：`2.12 lbs`
  *   **平均退货率 (Return Rate)**：`5.03%`
  *   **平均毛利率 (Profit Margin)**：`52.53%`
  *   **品牌集中度 (Brand Concentration)**：`50.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Sewing Storage  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 组织，存储 › 工艺品 › 缝纫用品收纳用品`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`25`
  *   **新品平均价格**：`$ 18.28`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`237`
  *   **新品月均销售额**：`$4,886`
  *   **平均重量**：`2.12 pounds (961 g)`
  *   **平均体积**：`782.96 in³ (12,830 cm³)`
  *   **平均毛利率**：`52.53%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`7.6‰`

---

#### 🏆 🟡-33. Battery Chargers (电池充电器)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicle Parts › Battery Chargers  市场分析`
- **触发警示项**：`谨慎认证类目路径, 带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.92`
  *   **平均 Reviews (Avg Reviews)**：`379 个`
  *   **物理重量 (Weight)**：`0.50 lbs`
  *   **平均退货率 (Return Rate)**：`6.99%`
  *   **平均毛利率 (Profit Margin)**：`61.5%`
  *   **品牌集中度 (Brand Concentration)**：`45.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicle Parts › Battery Chargers  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 电池充电器`
  *   **A+数量占比**：`59%`
  *   **新品平均评分数**：`20`
  *   **新品平均价格**：`$ 24.74`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`232`
  *   **新品月均销售额**：`$5,357`
  *   **平均重量**：`0.50 pounds (228 g)`
  *   **平均体积**：`33.04 in³ (541 cm³)`
  *   **平均毛利率**：`61.5%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`8.5‰`

---

#### 🏆 🟡-34. Flower Pressing (压花)

- **完整市场路径**：`Toys & Games › Arts & Crafts › Craft Kits › Flower Pressing  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.48`
  *   **平均 Reviews (Avg Reviews)**：`175 个`
  *   **物理重量 (Weight)**：`1.69 lbs`
  *   **平均退货率 (Return Rate)**：`2.87%`
  *   **平均毛利率 (Profit Margin)**：`55.13%`
  *   **品牌集中度 (Brand Concentration)**：`60.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Arts & Crafts › Craft Kits › Flower Pressing  市场分析`
  *   **市场路径(中文)**：`玩具 › 艺术 › 工艺品套装 › 压花`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`14`
  *   **新品平均价格**：`$ 19.59`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`109`
  *   **新品月均销售额**：`$1,877`
  *   **平均重量**：`1.69 pounds (768 g)`
  *   **平均体积**：`153.96 in³ (2,523 cm³)`
  *   **平均毛利率**：`55.13%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`8.6‰`

---

#### 🏆 🟡-35. Tea Storage Chests (茶叶罐)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Coffee, Tea & Espresso › Tea Accessories › Tea Storage Chests  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.40`
  *   **平均 Reviews (Avg Reviews)**：`657 个`
  *   **物理重量 (Weight)**：`2.44 lbs`
  *   **平均退货率 (Return Rate)**：`6.54%`
  *   **平均毛利率 (Profit Margin)**：`53.62%`
  *   **品牌集中度 (Brand Concentration)**：`45.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Coffee, Tea & Espresso › Tea Accessories › Tea Storage Chests  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 咖啡、茶 › 茶叶配件 › 茶叶罐`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`50`
  *   **新品平均价格**：`$ 22.66`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`194`
  *   **新品月均销售额**：`$4,188`
  *   **平均重量**：`2.44 pounds (1,107 g)`
  *   **平均体积**：`377.32 in³ (6,183 cm³)`
  *   **平均毛利率**：`53.62%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`6.4‰`

---

#### 🏆 🟡-36. Guitars & Strings (吉他)

- **完整市场路径**：`Toys & Games › Learning & Education › Musical Instruments › Guitars & Strings  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.38`
  *   **平均 Reviews (Avg Reviews)**：`625 个`
  *   **物理重量 (Weight)**：`1.30 lbs`
  *   **平均退货率 (Return Rate)**：`5.12%`
  *   **平均毛利率 (Profit Margin)**：`54.25%`
  *   **品牌集中度 (Brand Concentration)**：`58.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Learning & Education › Musical Instruments › Guitars & Strings  市场分析`
  *   **市场路径(中文)**：`玩具 › 学习 › 乐器 › 吉他`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`113`
  *   **新品平均价格**：`$ 30.81`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`89`
  *   **新品月均销售额**：`$2,841`
  *   **平均重量**：`1.30 pounds (590 g)`
  *   **平均体积**：`458.30 in³ (7,510 cm³)`
  *   **平均毛利率**：`54.25%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟡-37. Rods (杆)

- **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Welding Equipment › Welding Equipment & Accessories › Arc Welding Equipment › Rods  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.66`
  *   **平均 Reviews (Avg Reviews)**：`278 个`
  *   **物理重量 (Weight)**：`2.23 lbs`
  *   **平均退货率 (Return Rate)**：`1.94%`
  *   **平均毛利率 (Profit Margin)**：`59.65%`
  *   **品牌集中度 (Brand Concentration)**：`58.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Welding Equipment › Welding Equipment & Accessories › Arc Welding Equipment › Rods  市场分析`
  *   **市场路径(中文)**：`工具 › 焊接 › 焊接设备 › 焊接设备 › 电弧焊接设备 › 杆`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`6`
  *   **新品平均价格**：`$ 15`
  *   **新品平均星级**：`2.9`
  *   **新品月均销量**：`206`
  *   **新品月均销售额**：`$2,975`
  *   **平均重量**：`2.23 pounds (1,011 g)`
  *   **平均体积**：`69.95 in³ (1,146 cm³)`
  *   **平均毛利率**：`59.65%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`11.9‰`

---

#### 🏆 🟡-38. Airplanes & Jets (飞机)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Airplanes & Jets  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$57.95`
  *   **平均 Reviews (Avg Reviews)**：`256 个`
  *   **物理重量 (Weight)**：`0.94 lbs`
  *   **平均退货率 (Return Rate)**：`8.46%`
  *   **平均毛利率 (Profit Margin)**：`67.22%`
  *   **品牌集中度 (Brand Concentration)**：`61.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Airplanes & Jets  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 飞机`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`70`
  *   **新品平均价格**：`$ 35.15`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`216`
  *   **新品月均销售额**：`$7,210`
  *   **平均重量**：`0.94 pounds (425 g)`
  *   **平均体积**：`627.79 in³ (10,288 cm³)`
  *   **平均毛利率**：`67.22%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`2.2‰`

---

#### 🏆 🟡-39. Gaiters (护腿、护脚)

- **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Footwear & Accessories › Gaiters  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.12`
  *   **平均 Reviews (Avg Reviews)**：`386 个`
  *   **物理重量 (Weight)**：`0.68 lbs`
  *   **平均退货率 (Return Rate)**：`8.64%`
  *   **平均毛利率 (Profit Margin)**：`64.26%`
  *   **品牌集中度 (Brand Concentration)**：`56.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Footwear & Accessories › Gaiters  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 外出休闲 › 露营和远足 › 鞋类及配件 › 护腿、护脚`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`39`
  *   **新品平均价格**：`$ 31.67`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`159`
  *   **新品月均销售额**：`$4,490`
  *   **平均重量**：`0.68 pounds (310 g)`
  *   **平均体积**：`210.92 in³ (3,456 cm³)`
  *   **平均毛利率**：`64.26%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`7.2‰`

---

#### 🏆 🟡-40. Cream Chargers & Whippers (奶油充电器)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Specialty Tools & Gadgets › Cream Chargers & Whippers  市场分析`
- **触发警示项**：`带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.45`
  *   **平均 Reviews (Avg Reviews)**：`438 个`
  *   **物理重量 (Weight)**：`1.50 lbs`
  *   **平均退货率 (Return Rate)**：`2.63%`
  *   **平均毛利率 (Profit Margin)**：`66.91%`
  *   **品牌集中度 (Brand Concentration)**：`62.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`51.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Specialty Tools & Gadgets › Cream Chargers & Whippers  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 专业工具 › 奶油充电器`
  *   **A+数量占比**：`66%`
  *   **新品平均评分数**：`12`
  *   **新品平均价格**：`$ 29.53`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`250`
  *   **新品月均销售额**：`$5,569`
  *   **平均重量**：`1.50 pounds (679 g)`
  *   **平均体积**：`135.65 in³ (2,223 cm³)`
  *   **平均毛利率**：`66.91%`
  *   **卖家所属地**：`中国|51.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟡-41. Metric Inserts & Kits (米制刀片和套件)

- **完整市场路径**：`Automotive › Tools & Equipment › Thread Repair Kits › Metric Inserts & Kits  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$43.87`
  *   **平均 Reviews (Avg Reviews)**：`196 个`
  *   **物理重量 (Weight)**：`2.49 lbs`
  *   **平均退货率 (Return Rate)**：`5.6%`
  *   **平均毛利率 (Profit Margin)**：`66.73%`
  *   **品牌集中度 (Brand Concentration)**：`60.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Thread Repair Kits › Metric Inserts & Kits  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 螺纹修理包 › 米制刀片和套件`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`51`
  *   **新品平均价格**：`$ 52.09`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`136`
  *   **新品月均销售额**：`$7,995`
  *   **平均重量**：`2.49 pounds (1,129 g)`
  *   **平均体积**：`152.01 in³ (2,491 cm³)`
  *   **平均毛利率**：`66.73%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`9.2‰`

---

#### 🏆 🟡-42. Monoculars (单筒望远镜)

- **完整市场路径**：`Electronics › Camera & Photo › Binoculars & Scopes › Monoculars  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$72.01`
  *   **平均 Reviews (Avg Reviews)**：`620 个`
  *   **物理重量 (Weight)**：`0.74 lbs`
  *   **平均退货率 (Return Rate)**：`7.05%`
  *   **平均毛利率 (Profit Margin)**：`77.27%`
  *   **品牌集中度 (Brand Concentration)**：`64.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Camera & Photo › Binoculars & Scopes › Monoculars  市场分析`
  *   **市场路径(中文)**：`电子产品 › 摄像机 › 双筒望远镜 › 单筒望远镜`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`45`
  *   **新品平均价格**：`$ 41.3`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`235`
  *   **新品月均销售额**：`$8,084`
  *   **平均重量**：`0.74 pounds (336 g)`
  *   **平均体积**：`54.48 in³ (893 cm³)`
  *   **平均毛利率**：`77.27%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`7.5‰`

---

#### 🏆 🟡-43. Alarms & Anti-Theft (摩托车防盗器)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Electronics › Alarms & Anti-Theft  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.91`
  *   **平均 Reviews (Avg Reviews)**：`705 个`
  *   **物理重量 (Weight)**：`0.89 lbs`
  *   **平均退货率 (Return Rate)**：`4.72%`
  *   **平均毛利率 (Profit Margin)**：`63.33%`
  *   **品牌集中度 (Brand Concentration)**：`48.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Electronics › Alarms & Anti-Theft  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 辅料 › 电子产品 › 摩托车防盗器`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 48.4`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`111`
  *   **新品月均销售额**：`$4,379`
  *   **平均重量**：`0.89 pounds (406 g)`
  *   **平均体积**：`39.07 in³ (640 cm³)`
  *   **平均毛利率**：`63.33%`
  *   **卖家所属地**：`中国|55.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟡-44. Replacement Wheels (备用轮)

- **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Replacement Wheels  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.50`
  *   **平均 Reviews (Avg Reviews)**：`298 个`
  *   **物理重量 (Weight)**：`2.05 lbs`
  *   **平均退货率 (Return Rate)**：`8.59%`
  *   **平均毛利率 (Profit Margin)**：`57.61%`
  *   **品牌集中度 (Brand Concentration)**：`64.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`84.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Replacement Wheels  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 溜冰鞋、滑板和滑板车 › 自行车车 › 自行车车配件 › 备用轮`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`14`
  *   **新品平均价格**：`$ 19.99`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`119`
  *   **新品月均销售额**：`$2,331`
  *   **平均重量**：`2.05 pounds (931 g)`
  *   **平均体积**：`232.88 in³ (3,816 cm³)`
  *   **平均毛利率**：`57.61%`
  *   **卖家所属地**：`中国|84.0%`
  *   **搜索购买比**：`6.5‰`

---

#### 🏆 🟡-45. Hair Dryer Stands (吹风机支架)

- **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Mobility & Daily Living Aids › Bathroom Safety, Aids & Accessories › Hair Dryer Stands  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.87`
  *   **平均 Reviews (Avg Reviews)**：`219 个`
  *   **物理重量 (Weight)**：`1.34 lbs`
  *   **平均退货率 (Return Rate)**：`8.66%`
  *   **平均毛利率 (Profit Margin)**：`54.67%`
  *   **品牌集中度 (Brand Concentration)**：`50.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Mobility & Daily Living Aids › Bathroom Safety, Aids & Accessories › Hair Dryer Stands  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 医疗用品和设备 › 行动和日常生活辅助工具 › 卫浴用品 › 吹风机支架`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 21.04`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`116`
  *   **新品月均销售额**：`$2,284`
  *   **平均重量**：`1.34 pounds (610 g)`
  *   **平均体积**：`581.35 in³ (9,527 cm³)`
  *   **平均毛利率**：`54.67%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`7.5‰`

---

#### 🏆 🟡-46. Bats (蝙蝠)

- **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Bats  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$34.37`
  *   **平均 Reviews (Avg Reviews)**：`344 个`
  *   **物理重量 (Weight)**：`2.19 lbs`
  *   **平均退货率 (Return Rate)**：`2.61%`
  *   **平均毛利率 (Profit Margin)**：`59.54%`
  *   **品牌集中度 (Brand Concentration)**：`55.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`47.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Bats  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › 蝙蝠`
  *   **A+数量占比**：`65%`
  *   **新品平均评分数**：`6`
  *   **新品平均价格**：`$ 35.25`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`80`
  *   **新品月均销售额**：`$2,522`
  *   **平均重量**：`2.19 pounds (995 g)`
  *   **平均体积**：`479.49 in³ (7,858 cm³)`
  *   **平均毛利率**：`59.54%`
  *   **卖家所属地**：`中国|47.0%`
  *   **搜索购买比**：`14.5‰`

---

#### 🏆 🟡-47. Bulb Planters (球茎栽植器)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Hand Tools › Bulb Planters  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.92`
  *   **平均 Reviews (Avg Reviews)**：`295 个`
  *   **物理重量 (Weight)**：`2.32 lbs`
  *   **平均退货率 (Return Rate)**：`2.9%`
  *   **平均毛利率 (Profit Margin)**：`52.2%`
  *   **品牌集中度 (Brand Concentration)**：`48.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Hand Tools › Bulb Planters  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 手动园艺工具 › 球茎栽植器`
  *   **A+数量占比**：`65%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 22.76`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`117`
  *   **新品月均销售额**：`$2,289`
  *   **平均重量**：`2.32 pounds (1,052 g)`
  *   **平均体积**：`610.31 in³ (10,001 cm³)`
  *   **平均毛利率**：`52.2%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`13.1‰`

---

#### 🏆 🟡-48. Speedometers (车速里程表)

- **完整市场路径**：`Automotive › Replacement Parts › Lighting & Electrical › Electrical › Gauges › Speedometers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$46.69`
  *   **平均 Reviews (Avg Reviews)**：`173 个`
  *   **物理重量 (Weight)**：`0.39 lbs`
  *   **平均退货率 (Return Rate)**：`9.17%`
  *   **平均毛利率 (Profit Margin)**：`67.63%`
  *   **品牌集中度 (Brand Concentration)**：`63.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Lighting & Electrical › Electrical › Gauges › Speedometers  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 照明及电气 › 电气 › 计量器 › 车速里程表`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 22.2`
  *   **新品平均星级**：`3.6`
  *   **新品月均销量**：`155`
  *   **新品月均销售额**：`$3,130`
  *   **平均重量**：`0.39 pounds (179 g)`
  *   **平均体积**：`59.86 in³ (981 cm³)`
  *   **平均毛利率**：`67.63%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`3.0‰`

---

#### 🏆 🟡-49. Food Processor Parts & Accessories (食物处理器零件)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Small Appliance Parts & Accessories › Food Processor Parts & Accessories  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.23`
  *   **平均 Reviews (Avg Reviews)**：`313 个`
  *   **物理重量 (Weight)**：`1.08 lbs`
  *   **平均退货率 (Return Rate)**：`8.72%`
  *   **平均毛利率 (Profit Margin)**：`61.51%`
  *   **品牌集中度 (Brand Concentration)**：`36.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`56.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Small Appliance Parts & Accessories › Food Processor Parts & Accessories  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 小家电配件 › 食物处理器零件`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`27`
  *   **新品平均价格**：`$ 25.97`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`228`
  *   **新品月均销售额**：`$4,753`
  *   **平均重量**：`1.08 pounds (488 g)`
  *   **平均体积**：`234.94 in³ (3,850 cm³)`
  *   **平均毛利率**：`61.51%`
  *   **卖家所属地**：`中国|56.0%`
  *   **搜索购买比**：`12.8‰`

---

#### 🏆 🟡-50. Amplifiers (放大器)

- **完整市场路径**：`Electronics › Headphones, Earbuds & Accessories › Amplifiers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$90.53`
  *   **平均 Reviews (Avg Reviews)**：`647 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`9.82%`
  *   **平均毛利率 (Profit Margin)**：`82.76%`
  *   **品牌集中度 (Brand Concentration)**：`64.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`57.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Headphones, Earbuds & Accessories › Amplifiers  市场分析`
  *   **市场路径(中文)**：`电子产品 › 耳机、耳塞及配件 › 放大器`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`25`
  *   **新品平均价格**：`$ 91.08`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`101`
  *   **新品月均销售额**：`$10,032`
  *   **平均重量**：`0.71 pounds (321 g)`
  *   **平均体积**：`49.67 in³ (814 cm³)`
  *   **平均毛利率**：`82.76%`
  *   **卖家所属地**：`美国|43.0%`
  *   **搜索购买比**：`4.6‰`

---

#### 🏆 🟡-51. Kick Plates (踢脚板)

- **完整市场路径**：`Tools & Home Improvement › Hardware › Door Hardware & Locks › Kick Plates  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.06`
  *   **平均 Reviews (Avg Reviews)**：`111 个`
  *   **物理重量 (Weight)**：`1.56 lbs`
  *   **平均退货率 (Return Rate)**：`8.07%`
  *   **平均毛利率 (Profit Margin)**：`54.94%`
  *   **品牌集中度 (Brand Concentration)**：`62.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`59.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Hardware › Door Hardware & Locks › Kick Plates  市场分析`
  *   **市场路径(中文)**：`工具 › 硬件设施 › 门五金 › 踢脚板`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 17.39`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`144`
  *   **新品月均销售额**：`$2,161`
  *   **平均重量**：`1.56 pounds (708 g)`
  *   **平均体积**：`170.06 in³ (2,787 cm³)`
  *   **平均毛利率**：`54.94%`
  *   **卖家所属地**：`中国|59.0%`
  *   **搜索购买比**：`10.7‰`

---

#### 🏆 🟡-52. Breast Pump Carrying Bags (奶泵携带包)

- **完整市场路径**：`Baby Products › Feeding › Breastfeeding › Breast Pump Carrying Bags  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.50`
  *   **平均 Reviews (Avg Reviews)**：`154 个`
  *   **物理重量 (Weight)**：`1.23 lbs`
  *   **平均退货率 (Return Rate)**：`9.17%`
  *   **平均毛利率 (Profit Margin)**：`62.11%`
  *   **品牌集中度 (Brand Concentration)**：`58.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Baby Products › Feeding › Breastfeeding › Breast Pump Carrying Bags  市场分析`
  *   **市场路径(中文)**：`婴儿产品 › 喂养 › 母乳喂养 › 奶泵携带包`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`46`
  *   **新品平均价格**：`$ 28.34`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`152`
  *   **新品月均销售额**：`$4,302`
  *   **平均重量**：`1.23 pounds (559 g)`
  *   **平均体积**：`688.83 in³ (11,288 cm³)`
  *   **平均毛利率**：`62.11%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`5.3‰`

---

#### 🏆 🟡-53. Fenders (挡泥板)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Body & Frame Parts › Body Work › Bumpers & Fenders › Fenders  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$41.60`
  *   **平均 Reviews (Avg Reviews)**：`127 个`
  *   **物理重量 (Weight)**：`2.25 lbs`
  *   **平均退货率 (Return Rate)**：`5.43%`
  *   **平均毛利率 (Profit Margin)**：`58.18%`
  *   **品牌集中度 (Brand Concentration)**：`44.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Body & Frame Parts › Body Work › Bumpers & Fenders › Fenders  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 部分 › 身体 › 身体工作 › 保险杠 › 挡泥板`
  *   **A+数量占比**：`63%`
  *   **新品平均评分数**：`4`
  *   **新品平均价格**：`$ 40.55`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`101`
  *   **新品月均销售额**：`$3,787`
  *   **平均重量**：`2.25 pounds (1,023 g)`
  *   **平均体积**：`783.01 in³ (12,831 cm³)`
  *   **平均毛利率**：`58.18%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`2.6‰`

---

#### 🏆 🟡-54. Helicopters (直升机)

- **完整市场路径**：`Toys & Games › Vehicles › Helicopters  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.11`
  *   **平均 Reviews (Avg Reviews)**：`296 个`
  *   **物理重量 (Weight)**：`0.77 lbs`
  *   **平均退货率 (Return Rate)**：`3.29%`
  *   **平均毛利率 (Profit Margin)**：`55.0%`
  *   **品牌集中度 (Brand Concentration)**：`53.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Vehicles › Helicopters  市场分析`
  *   **市场路径(中文)**：`玩具 › 车辆 › 直升机`
  *   **A+数量占比**：`48%`
  *   **新品平均评分数**：`6`
  *   **新品平均价格**：`$ 20.28`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`31`
  *   **新品月均销售额**：`$627`
  *   **平均重量**：`0.77 pounds (351 g)`
  *   **平均体积**：`362.16 in³ (5,935 cm³)`
  *   **平均毛利率**：`55%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`9.5‰`

---

#### 🏆 🟡-55. Dice Bags & Boxes (骰袋和骰盒)

- **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Dice & Accessories › Dice Bags & Boxes  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.43`
  *   **平均 Reviews (Avg Reviews)**：`430 个`
  *   **物理重量 (Weight)**：`0.73 lbs`
  *   **平均退货率 (Return Rate)**：`3.93%`
  *   **平均毛利率 (Profit Margin)**：`59.66%`
  *   **品牌集中度 (Brand Concentration)**：`42.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Dice & Accessories › Dice Bags & Boxes  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 游戏配件 › 骰子和配件 › 骰袋和骰盒`
  *   **A+数量占比**：`63%`
  *   **新品平均评分数**：`28`
  *   **新品平均价格**：`$ 14.49`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`98`
  *   **新品月均销售额**：`$1,354`
  *   **平均重量**：`0.73 pounds (329 g)`
  *   **平均体积**：`218.58 in³ (3,582 cm³)`
  *   **平均毛利率**：`59.66%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`4.5‰`

---

#### 🏆 🟡-56. Heating & Temperature Control (暖气)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Home Brewing & Wine Making › Fermentation & More › Heating & Temperature Control  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.94`
  *   **平均 Reviews (Avg Reviews)**：`140 个`
  *   **物理重量 (Weight)**：`1.09 lbs`
  *   **平均退货率 (Return Rate)**：`9.98%`
  *   **平均毛利率 (Profit Margin)**：`60.28%`
  *   **品牌集中度 (Brand Concentration)**：`59.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Home Brewing & Wine Making › Fermentation & More › Heating & Temperature Control  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 家庭酿造 › 发酵 › 暖气`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`26`
  *   **新品平均价格**：`$ 28.32`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`70`
  *   **新品月均销售额**：`$2,318`
  *   **平均重量**：`1.09 pounds (496 g)`
  *   **平均体积**：`199.96 in³ (3,277 cm³)`
  *   **平均毛利率**：`60.28%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`9.3‰`

---

## 四、SellerSprite Excel 导出完整字段

> 来源：`Market-research(200)WorkoutTop&BottomSets-US-Last-30-days.xlsx`
> Excel 包含 **200** 个类目、**37** 个字段；其中 **196** 个类目名称可与当前市场报告直接匹配。

### Workout Top & Bottom Sets (服装套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Workout Top & Bottom Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 服装套装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Active:Sets:Workout Top & Bottom Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：50 <br> 卖家：51 |
| Listing样本数(TOP100) / 月总销量 | 432355.0 |
| Listing样本数(TOP100) / 月均销量 | 4323.0 |
| Listing样本数(TOP100) / 月均销售额($) | 124690.0 |
| Listing样本数(TOP100) / 平均价格($) | 28.92 |
| Listing样本数(TOP100) / 平均评分数 | 695.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 37742.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 98%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.309 |
| Listing样本数(TOP100) / 品牌集中度 | 0.577 |
| Listing样本数(TOP100) / 卖家集中度 | 0.561 |
| Listing样本数(TOP100) / 商品总数 | 3038.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5775 |
| Listing样本数(TOP100) / 平均体积(in³) | 130.481 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.96 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 82.0% |
| 头部Listing数(TOP10) / 月均销量 | 13369.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 379562.0 |
| 头部Listing数(TOP10) / 平均BSR | 2236.0 |
| 新品(半年内上架) / 新品数量 | 26.0 |
| 新品(半年内上架) / 新品占比 | 0.26 |
| 新品(半年内上架) / 月均销量 | 4031.0 |
| 新品(半年内上架) / 月均销售额($) | 108942.0 |
| 新品(半年内上架) / 平均价格($) | 26.82 |
| 新品(半年内上架) / 平均评分数 | 112.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.179375 |
| 所有Listing(半年内) / 同类目退货率 | 0.123008005 |
| 所有Listing(半年内) / 搜索购买比 | 4.01962 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06877 |

### Sandals (时装凉鞋、凉拖)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Sandals |
| Listing样本数(TOP100) / 细分市场(翻译) | 时装凉鞋、凉拖 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Shoes:Sandals |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：58 <br> 卖家：55 |
| Listing样本数(TOP100) / 月总销量 | 388768.0 |
| Listing样本数(TOP100) / 月均销量 | 3887.0 |
| Listing样本数(TOP100) / 月均销售额($) | 78177.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.89 |
| Listing样本数(TOP100) / 平均评分数 | 1125.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 16653.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 77%  <br> AMZ: 17%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.405 |
| Listing样本数(TOP100) / 品牌集中度 | 0.6 |
| Listing样本数(TOP100) / 卖家集中度 | 0.633 |
| Listing样本数(TOP100) / 商品总数 | 2853.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5212 |
| Listing样本数(TOP100) / 平均体积(in³) | 131.6465 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.97 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 15766.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 259300.0 |
| 头部Listing数(TOP10) / 平均BSR | 3024.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 2282.0 |
| 新品(半年内上架) / 月均销售额($) | 47957.0 |
| 新品(半年内上架) / 平均价格($) | 22.2 |
| 新品(半年内上架) / 平均评分数 | 152.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.151503 |
| 所有Listing(半年内) / 同类目退货率 | 0.163986 |
| 所有Listing(半年内) / 搜索购买比 | 5.93098 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04086 |

### Shrugs (女装短针织衫)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Shrugs |
| Listing样本数(TOP100) / 细分市场(翻译) | 女装短针织衫 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Sweaters:Shrugs |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：64 <br> 卖家：65 |
| Listing样本数(TOP100) / 月总销量 | 292212.0 |
| Listing样本数(TOP100) / 月均销量 | 2922.0 |
| Listing样本数(TOP100) / 月均销售额($) | 60808.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.28 |
| Listing样本数(TOP100) / 平均评分数 | 875.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 36483.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 99%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.274 |
| Listing样本数(TOP100) / 品牌集中度 | 0.479 |
| Listing样本数(TOP100) / 卖家集中度 | 0.465 |
| Listing样本数(TOP100) / 商品总数 | 1603.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4068 |
| Listing样本数(TOP100) / 平均体积(in³) | 83.9729 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.97 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 55.0% |
| 头部Listing数(TOP10) / 月均销量 | 8011.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 173171.0 |
| 头部Listing数(TOP10) / 平均BSR | 69666.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 3249.0 |
| 新品(半年内上架) / 月均销售额($) | 69456.0 |
| 新品(半年内上架) / 平均价格($) | 20.87 |
| 新品(半年内上架) / 平均评分数 | 126.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.209571 |
| 所有Listing(半年内) / 同类目退货率 | 0.24188499 |
| 所有Listing(半年内) / 搜索购买比 | 5.40429 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0629 |

### One-Pieces (连体泳衣)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | One-Pieces |
| Listing样本数(TOP100) / 细分市场(翻译) | 连体泳衣 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing:Swim:One-Pieces |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：68 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 228151.0 |
| Listing样本数(TOP100) / 月均销量 | 2281.0 |
| Listing样本数(TOP100) / 月均销售额($) | 46269.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.25 |
| Listing样本数(TOP100) / 平均评分数 | 622.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 21923.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 12%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.313 |
| Listing样本数(TOP100) / 品牌集中度 | 0.413 |
| Listing样本数(TOP100) / 卖家集中度 | 0.506 |
| Listing样本数(TOP100) / 商品总数 | 2583.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2562 |
| Listing样本数(TOP100) / 平均体积(in³) | 68.2831 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.94 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 70.0% |
| 头部Listing数(TOP10) / 月均销量 | 7132.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 117363.0 |
| 头部Listing数(TOP10) / 平均BSR | 4055.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 1469.0 |
| 新品(半年内上架) / 月均销售额($) | 36563.0 |
| 新品(半年内上架) / 平均价格($) | 25.31 |
| 新品(半年内上架) / 平均评分数 | 80.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.131053 |
| 所有Listing(半年内) / 同类目退货率 | 0.215473 |
| 所有Listing(半年内) / 搜索购买比 | 5.67267 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05444 |

### Outdoor Statues (户外雕像)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Outdoor Statues |
| Listing样本数(TOP100) / 细分市场(翻译) | 户外雕像 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Outdoor Décor:Garden Sculptures & Statues:Outdoor Statues |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 193889.0 |
| Listing样本数(TOP100) / 月均销量 | 1938.0 |
| Listing样本数(TOP100) / 月均销售额($) | 53610.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.31 |
| Listing样本数(TOP100) / 平均评分数 | 918.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 12447.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 3%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.365 |
| Listing样本数(TOP100) / 品牌集中度 | 0.455 |
| Listing样本数(TOP100) / 卖家集中度 | 0.469 |
| Listing样本数(TOP100) / 商品总数 | 12058.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.1085 |
| Listing样本数(TOP100) / 平均体积(in³) | 457.5768 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.85 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 7075.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 239291.0 |
| 头部Listing数(TOP10) / 平均BSR | 1705.0 |
| 新品(半年内上架) / 新品数量 | 19.0 |
| 新品(半年内上架) / 新品占比 | 0.19 |
| 新品(半年内上架) / 月均销量 | 1291.0 |
| 新品(半年内上架) / 月均销售额($) | 28254.0 |
| 新品(半年内上架) / 平均价格($) | 22.95 |
| 新品(半年内上架) / 平均评分数 | 64.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.029799 |
| 所有Listing(半年内) / 同类目退货率 | 0.038448 |
| 所有Listing(半年内) / 搜索购买比 | 5.13294 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.048 |

### Tankini Sets (坦基尼套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tankini Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 坦基尼套装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing:Swim:Two-Pieces:Tankinis:Tankini Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：66 <br> 卖家：66 |
| Listing样本数(TOP100) / 月总销量 | 191538.0 |
| Listing样本数(TOP100) / 月均销量 | 1915.0 |
| Listing样本数(TOP100) / 月均销售额($) | 40762.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.45 |
| Listing样本数(TOP100) / 平均评分数 | 582.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 38336.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 5%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.338 |
| Listing样本数(TOP100) / 品牌集中度 | 0.477 |
| Listing样本数(TOP100) / 卖家集中度 | 0.495 |
| Listing样本数(TOP100) / 商品总数 | 689.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3014 |
| Listing样本数(TOP100) / 平均体积(in³) | 68.3313 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.95 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 6476.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 114237.0 |
| 头部Listing数(TOP10) / 平均BSR | 3501.0 |
| 新品(半年内上架) / 新品数量 | 36.0 |
| 新品(半年内上架) / 新品占比 | 0.36 |
| 新品(半年内上架) / 月均销量 | 1334.0 |
| 新品(半年内上架) / 月均销售额($) | 33489.0 |
| 新品(半年内上架) / 平均价格($) | 25.15 |
| 新品(半年内上架) / 平均评分数 | 56.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.153125 |
| 所有Listing(半年内) / 同类目退货率 | 0.215473 |
| 所有Listing(半年内) / 搜索购买比 | 5.44915 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05444 |

### Liver Extracts (肝脏提取物)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Liver Extracts |
| Listing样本数(TOP100) / 细分市场(翻译) | 肝脏提取物 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Vitamins, Minerals & Supplements:Glandular Extracts:Liver Extracts |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：79 |
| Listing样本数(TOP100) / 月总销量 | 190747.0 |
| Listing样本数(TOP100) / 月均销量 | 1907.0 |
| Listing样本数(TOP100) / 月均销售额($) | 68800.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.26 |
| Listing样本数(TOP100) / 平均评分数 | 843.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 39293.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 3%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.601 |
| Listing样本数(TOP100) / 品牌集中度 | 0.631 |
| Listing样本数(TOP100) / 卖家集中度 | 0.634 |
| Listing样本数(TOP100) / 商品总数 | 516.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2785 |
| Listing样本数(TOP100) / 平均体积(in³) | 44.9379 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 82.0% |
| 头部Listing数(TOP10) / 月均销量 | 11466.0 |
| 头部Listing数(TOP10) / 垄断度 | 6.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 455095.0 |
| 头部Listing数(TOP10) / 平均BSR | 7378.0 |
| 新品(半年内上架) / 新品数量 | 16.0 |
| 新品(半年内上架) / 新品占比 | 0.16 |
| 新品(半年内上架) / 月均销量 | 1049.0 |
| 新品(半年内上架) / 月均销售额($) | 34768.0 |
| 新品(半年内上架) / 平均价格($) | 30.85 |
| 新品(半年内上架) / 平均评分数 | 66.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.00308 |
| 所有Listing(半年内) / 同类目退货率 | 0.0030790002 |
| 所有Listing(半年内) / 搜索购买比 | 22.90128 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.24225001 |

### Squirt Guns (水枪)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Squirt Guns |
| Listing样本数(TOP100) / 细分市场(翻译) | 水枪 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Sports & Outdoor Play:Pools & Water Toys:Squirt Guns |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：63 |
| Listing样本数(TOP100) / 月总销量 | 187124.0 |
| Listing样本数(TOP100) / 月均销量 | 1871.0 |
| Listing样本数(TOP100) / 月均销售额($) | 45271.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.3 |
| Listing样本数(TOP100) / 平均评分数 | 616.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 12910.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 6%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.313 |
| Listing样本数(TOP100) / 品牌集中度 | 0.518 |
| Listing样本数(TOP100) / 卖家集中度 | 0.502 |
| Listing样本数(TOP100) / 商品总数 | 1084.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5422 |
| Listing样本数(TOP100) / 平均体积(in³) | 324.8037 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 74.0% |
| 头部Listing数(TOP10) / 月均销量 | 5863.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 129515.0 |
| 头部Listing数(TOP10) / 平均BSR | 1204.0 |
| 新品(半年内上架) / 新品数量 | 49.0 |
| 新品(半年内上架) / 新品占比 | 0.49 |
| 新品(半年内上架) / 月均销量 | 1440.0 |
| 新品(半年内上架) / 月均销售额($) | 41866.0 |
| 新品(半年内上架) / 平均价格($) | 31.86 |
| 新品(半年内上架) / 平均评分数 | 140.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.039259 |
| 所有Listing(半年内) / 同类目退货率 | 0.044108 |
| 所有Listing(半年内) / 搜索购买比 | 5.73047 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04113 |

### Shorts (短裤)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Shorts |
| Listing样本数(TOP100) / 细分市场(翻译) | 短裤 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Shorts |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：68 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 185044.0 |
| Listing样本数(TOP100) / 月均销量 | 1850.0 |
| Listing样本数(TOP100) / 月均销售额($) | 51474.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.75 |
| Listing样本数(TOP100) / 平均评分数 | 937.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 62720.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 6%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.534 |
| Listing样本数(TOP100) / 品牌集中度 | 0.647 |
| Listing样本数(TOP100) / 卖家集中度 | 0.65 |
| Listing样本数(TOP100) / 商品总数 | 10307.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5204 |
| Listing样本数(TOP100) / 平均体积(in³) | 85.1226 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.82 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 75.0% |
| 头部Listing数(TOP10) / 月均销量 | 9880.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 291034.0 |
| 头部Listing数(TOP10) / 平均BSR | 3659.0 |
| 新品(半年内上架) / 新品数量 | 35.0 |
| 新品(半年内上架) / 新品占比 | 0.35 |
| 新品(半年内上架) / 月均销量 | 1306.0 |
| 新品(半年内上架) / 月均销售额($) | 28377.0 |
| 新品(半年内上架) / 平均价格($) | 23.95 |
| 新品(半年内上架) / 平均评分数 | 530.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.221191 |
| 所有Listing(半年内) / 同类目退货率 | 0.123385 |
| 所有Listing(半年内) / 搜索购买比 | 5.00261 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.086169995 |

### Rash Guard Sets (Rash Guard Sets)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Rash Guard Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | Rash Guard Sets |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing:Swim:Swimwear Sets:Rash Guard Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：49 <br> 卖家：50 |
| Listing样本数(TOP100) / 月总销量 | 173320.0 |
| Listing样本数(TOP100) / 月均销量 | 1733.0 |
| Listing样本数(TOP100) / 月均销售额($) | 36436.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.18 |
| Listing样本数(TOP100) / 平均评分数 | 446.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 88950.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 4%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.333 |
| Listing样本数(TOP100) / 品牌集中度 | 0.584 |
| Listing样本数(TOP100) / 卖家集中度 | 0.592 |
| Listing样本数(TOP100) / 商品总数 | 571.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3381 |
| Listing样本数(TOP100) / 平均体积(in³) | 62.3949 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.96 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 5779.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 112486.0 |
| 头部Listing数(TOP10) / 平均BSR | 5414.0 |
| 新品(半年内上架) / 新品数量 | 34.0 |
| 新品(半年内上架) / 新品占比 | 0.34 |
| 新品(半年内上架) / 月均销量 | 1323.0 |
| 新品(半年内上架) / 月均销售额($) | 26847.0 |
| 新品(半年内上架) / 平均价格($) | 20.99 |
| 新品(半年内上架) / 平均评分数 | 52.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.097993 |
| 所有Listing(半年内) / 同类目退货率 | 0.215473 |
| 所有Listing(半年内) / 搜索购买比 | 6.21023 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05444 |

### Sets (套)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 套 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing:Swim:Two-Pieces:Bikinis:Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：64 <br> 卖家：59 |
| Listing样本数(TOP100) / 月总销量 | 166964.0 |
| Listing样本数(TOP100) / 月均销量 | 1669.0 |
| Listing样本数(TOP100) / 月均销售额($) | 41525.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.64 |
| Listing样本数(TOP100) / 平均评分数 | 332.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 28434.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 6%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.271 |
| Listing样本数(TOP100) / 品牌集中度 | 0.452 |
| Listing样本数(TOP100) / 卖家集中度 | 0.524 |
| Listing样本数(TOP100) / 商品总数 | 1610.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2917 |
| Listing样本数(TOP100) / 平均体积(in³) | 82.2722 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.92 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 79.0% |
| 头部Listing数(TOP10) / 月均销量 | 4522.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 114262.0 |
| 头部Listing数(TOP10) / 平均BSR | 7872.0 |
| 新品(半年内上架) / 新品数量 | 29.0 |
| 新品(半年内上架) / 新品占比 | 0.29 |
| 新品(半年内上架) / 月均销量 | 1402.0 |
| 新品(半年内上架) / 月均销售额($) | 34073.0 |
| 新品(半年内上架) / 平均价格($) | 24.42 |
| 新品(半年内上架) / 平均评分数 | 76.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.17863701 |
| 所有Listing(半年内) / 同类目退货率 | 0.215473 |
| 所有Listing(半年内) / 搜索购买比 | 4.69256 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05444 |

### Figurine Lights (雕像灯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Figurine Lights |
| Listing样本数(TOP100) / 细分市场(翻译) | 雕像灯 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Lighting & Ceiling Fans:Outdoor Lighting:Landscape Lighting:Figurine Lights |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：77 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 166695.0 |
| Listing样本数(TOP100) / 月均销量 | 1666.0 |
| Listing样本数(TOP100) / 月均销售额($) | 42795.0 |
| Listing样本数(TOP100) / 平均价格($) | 25.18 |
| Listing样本数(TOP100) / 平均评分数 | 1093.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 20779.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 1%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.482 |
| Listing样本数(TOP100) / 品牌集中度 | 0.564 |
| Listing样本数(TOP100) / 卖家集中度 | 0.549 |
| Listing样本数(TOP100) / 商品总数 | 1481.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3882 |
| Listing样本数(TOP100) / 平均体积(in³) | 285.0834 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.98 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 84.0% |
| 头部Listing数(TOP10) / 月均销量 | 8030.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 208906.0 |
| 头部Listing数(TOP10) / 平均BSR | 14496.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 1198.0 |
| 新品(半年内上架) / 月均销售额($) | 26627.0 |
| 新品(半年内上架) / 平均价格($) | 23.12 |
| 新品(半年内上架) / 平均评分数 | 93.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.023387 |
| 所有Listing(半年内) / 同类目退货率 | 0.066659 |
| 所有Listing(半年内) / 搜索购买比 | 4.85448 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04982 |

### Skirt Sets (裙装套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Skirt Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 裙装套装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Clothing Sets:Skirt Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：45 <br> 卖家：47 |
| Listing样本数(TOP100) / 月总销量 | 160911.0 |
| Listing样本数(TOP100) / 月均销量 | 1609.0 |
| Listing样本数(TOP100) / 月均销售额($) | 56135.0 |
| Listing样本数(TOP100) / 平均价格($) | 34.96 |
| Listing样本数(TOP100) / 平均评分数 | 166.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 64351.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 74%  <br> AMZ: 1%  <br> FBM: 25% |
| Listing样本数(TOP100) / 商品集中度 | 0.343 |
| Listing样本数(TOP100) / 品牌集中度 | 0.613 |
| Listing样本数(TOP100) / 卖家集中度 | 0.608 |
| Listing样本数(TOP100) / 商品总数 | 3810.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6941 |
| Listing样本数(TOP100) / 平均体积(in³) | 113.7702 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.69 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 92.0% |
| 头部Listing数(TOP10) / 月均销量 | 5523.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 194096.0 |
| 头部Listing数(TOP10) / 平均BSR | 7741.0 |
| 新品(半年内上架) / 新品数量 | 52.0 |
| 新品(半年内上架) / 新品占比 | 0.52 |
| 新品(半年内上架) / 月均销量 | 1530.0 |
| 新品(半年内上架) / 月均销售额($) | 53391.0 |
| 新品(半年内上架) / 平均价格($) | 34.31 |
| 新品(半年内上架) / 平均评分数 | 46.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.304688 |
| 所有Listing(半年内) / 同类目退货率 | 0.152695 |
| 所有Listing(半年内) / 搜索购买比 | 3.2316 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04593 |

### Grill Pads & Floor Mats (烤炉垫和地垫)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Grill Pads & Floor Mats |
| Listing样本数(TOP100) / 细分市场(翻译) | 烤炉垫和地垫 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Grills & Outdoor Cooking:Outdoor Cooking Tools & Accessories:Grill Pads & Floor Mats |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：75 |
| Listing样本数(TOP100) / 月总销量 | 157343.0 |
| Listing样本数(TOP100) / 月均销量 | 1573.0 |
| Listing样本数(TOP100) / 月均销售额($) | 32728.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.02 |
| Listing样本数(TOP100) / 平均评分数 | 976.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 18003.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 9%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.435 |
| Listing样本数(TOP100) / 品牌集中度 | 0.505 |
| Listing样本数(TOP100) / 卖家集中度 | 0.55 |
| Listing样本数(TOP100) / 商品总数 | 701.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.7349 |
| Listing样本数(TOP100) / 平均体积(in³) | 422.9092 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.92 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 6846.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 152642.0 |
| 头部Listing数(TOP10) / 平均BSR | 1627.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 1410.0 |
| 新品(半年内上架) / 月均销售额($) | 28177.0 |
| 新品(半年内上架) / 平均价格($) | 23.0 |
| 新品(半年内上架) / 平均评分数 | 142.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.032541 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 11.64775 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Clothing (服装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Clothing |
| Listing样本数(TOP100) / 细分市场(翻译) | 服装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：71 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 137922.0 |
| Listing样本数(TOP100) / 月均销量 | 1379.0 |
| Listing样本数(TOP100) / 月均销售额($) | 32481.0 |
| Listing样本数(TOP100) / 平均价格($) | 25.12 |
| Listing样本数(TOP100) / 平均评分数 | 602.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 71093.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 3%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.372 |
| Listing样本数(TOP100) / 品牌集中度 | 0.558 |
| Listing样本数(TOP100) / 卖家集中度 | 0.582 |
| Listing样本数(TOP100) / 商品总数 | 68934.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4873 |
| Listing样本数(TOP100) / 平均体积(in³) | 194.3338 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.92 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 78.0% |
| 头部Listing数(TOP10) / 月均销量 | 5136.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 107808.0 |
| 头部Listing数(TOP10) / 平均BSR | 8835.0 |
| 新品(半年内上架) / 新品数量 | 48.0 |
| 新品(半年内上架) / 新品占比 | 0.48 |
| 新品(半年内上架) / 月均销量 | 980.0 |
| 新品(半年内上架) / 月均销售额($) | 20067.0 |
| 新品(半年内上架) / 平均价格($) | 22.3 |
| 新品(半年内上架) / 平均评分数 | 80.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | N/A |
| 所有Listing(半年内) / 同类目退货率 | N/A |
| 所有Listing(半年内) / 搜索购买比 | N/A |
| 所有Listing(半年内) / 同类目搜索购买比 | N/A |

### Drip Irrigation Kits (滴灌套件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Drip Irrigation Kits |
| Listing样本数(TOP100) / 细分市场(翻译) | 滴灌套件 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Gardening & Lawn Care:Watering Equipment:Automatic Irrigation Equipment:Drip Irrigation Kits |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：64 <br> 卖家：66 |
| Listing样本数(TOP100) / 月总销量 | 134747.0 |
| Listing样本数(TOP100) / 月均销量 | 1347.0 |
| Listing样本数(TOP100) / 月均销售额($) | 42936.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.72 |
| Listing样本数(TOP100) / 平均评分数 | 606.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 18137.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 6%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.315 |
| Listing样本数(TOP100) / 品牌集中度 | 0.516 |
| Listing样本数(TOP100) / 卖家集中度 | 0.46 |
| Listing样本数(TOP100) / 商品总数 | 1639.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.5237 |
| Listing样本数(TOP100) / 平均体积(in³) | 339.8577 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 4246.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 131037.0 |
| 头部Listing数(TOP10) / 平均BSR | 2724.0 |
| 新品(半年内上架) / 新品数量 | 33.0 |
| 新品(半年内上架) / 新品占比 | 0.33 |
| 新品(半年内上架) / 月均销量 | 1104.0 |
| 新品(半年内上架) / 月均销售额($) | 35237.0 |
| 新品(半年内上架) / 平均价格($) | 34.17 |
| 新品(半年内上架) / 平均评分数 | 123.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.033673998 |
| 所有Listing(半年内) / 同类目退货率 | 0.033673998 |
| 所有Listing(半年内) / 搜索购买比 | 8.58333 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08583 |

### Self-Watering Stakes (自浇水桩)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Self-Watering Stakes |
| Listing样本数(TOP100) / 细分市场(翻译) | 自浇水桩 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Gardening & Lawn Care:Pots, Planters & Container Accessories:Plant Container Accessories:Self-Watering Stakes |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 131556.0 |
| Listing样本数(TOP100) / 月均销量 | 1315.0 |
| Listing样本数(TOP100) / 月均销售额($) | 26505.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.73 |
| Listing样本数(TOP100) / 平均评分数 | 840.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 20220.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 1%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.458 |
| Listing样本数(TOP100) / 品牌集中度 | 0.534 |
| Listing样本数(TOP100) / 卖家集中度 | 0.515 |
| Listing样本数(TOP100) / 商品总数 | 929.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4898 |
| Listing样本数(TOP100) / 平均体积(in³) | 141.7026 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 74.0% |
| 头部Listing数(TOP10) / 月均销量 | 6021.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 112856.0 |
| 头部Listing数(TOP10) / 平均BSR | 2275.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 643.0 |
| 新品(半年内上架) / 月均销售额($) | 12745.0 |
| 新品(半年内上架) / 平均价格($) | 20.43 |
| 新品(半年内上架) / 平均评分数 | 463.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.027969 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 12.23124 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Swing Trainers (室内练习器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Swing Trainers |
| Listing样本数(TOP100) / 细分市场(翻译) | 室内练习器 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Golf:Training Equipment:Swing Trainers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：63 |
| Listing样本数(TOP100) / 月总销量 | 128432.0 |
| Listing样本数(TOP100) / 月均销量 | 1284.0 |
| Listing样本数(TOP100) / 月均销售额($) | 36222.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.65 |
| Listing样本数(TOP100) / 平均评分数 | 444.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 29799.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 66%  <br> AMZ: 9%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.365 |
| Listing样本数(TOP100) / 品牌集中度 | 0.599 |
| Listing样本数(TOP100) / 卖家集中度 | 0.639 |
| Listing样本数(TOP100) / 商品总数 | 1853.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7049 |
| Listing样本数(TOP100) / 平均体积(in³) | 148.4409 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 67.0% |
| 头部Listing数(TOP10) / 月均销量 | 4692.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 71493.0 |
| 头部Listing数(TOP10) / 平均BSR | 41119.0 |
| 新品(半年内上架) / 新品数量 | 30.0 |
| 新品(半年内上架) / 新品占比 | 0.3 |
| 新品(半年内上架) / 月均销量 | 1141.0 |
| 新品(半年内上架) / 月均销售额($) | 16418.0 |
| 新品(半年内上架) / 平均价格($) | 19.19 |
| 新品(半年内上架) / 平均评分数 | 22.0 |
| 新品(半年内上架) / 平均星级 | 3.4 |
| 所有Listing(半年内) / 退货率 | 0.043748002 |
| 所有Listing(半年内) / 同类目退货率 | 0.045063 |
| 所有Listing(半年内) / 搜索购买比 | 7.43701 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07428 |

### Light Therapy (光照疗法)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Light Therapy |
| Listing样本数(TOP100) / 细分市场(翻译) | 光照疗法 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Health Care:Alternative Medicine:Light Therapy |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：64 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 127138.0 |
| Listing样本数(TOP100) / 月均销量 | 1271.0 |
| Listing样本数(TOP100) / 月均销售额($) | 86428.0 |
| Listing样本数(TOP100) / 平均价格($) | 72.14 |
| Listing样本数(TOP100) / 平均评分数 | 787.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 63899.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 3%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.295 |
| Listing样本数(TOP100) / 品牌集中度 | 0.501 |
| Listing样本数(TOP100) / 卖家集中度 | 0.463 |
| Listing样本数(TOP100) / 商品总数 | 2608.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.0005 |
| Listing样本数(TOP100) / 平均体积(in³) | 558.535 |
| Listing样本数(TOP100) / 平均毛利率 | 0.72 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 3753.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 214136.0 |
| 头部Listing数(TOP10) / 平均BSR | 15747.0 |
| 新品(半年内上架) / 新品数量 | 28.0 |
| 新品(半年内上架) / 新品占比 | 0.28 |
| 新品(半年内上架) / 月均销量 | 1047.0 |
| 新品(半年内上架) / 月均销售额($) | 80803.0 |
| 新品(半年内上架) / 平均价格($) | 78.34 |
| 新品(半年内上架) / 平均评分数 | 60.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.102919 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 4.50757 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Pants (长裤)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Pants |
| Listing样本数(TOP100) / 细分市场(翻译) | 长裤 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Pants |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：79 |
| Listing样本数(TOP100) / 月总销量 | 123963.0 |
| Listing样本数(TOP100) / 月均销量 | 1239.0 |
| Listing样本数(TOP100) / 月均销售额($) | 32874.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.63 |
| Listing样本数(TOP100) / 平均评分数 | 1158.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 111108.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 5%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.348 |
| Listing样本数(TOP100) / 品牌集中度 | 0.547 |
| Listing样本数(TOP100) / 卖家集中度 | 0.478 |
| Listing样本数(TOP100) / 商品总数 | 20643.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6659 |
| Listing样本数(TOP100) / 平均体积(in³) | 125.8438 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 76.0% |
| 头部Listing数(TOP10) / 月均销量 | 4309.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 106919.0 |
| 头部Listing数(TOP10) / 平均BSR | 9712.0 |
| 新品(半年内上架) / 新品数量 | 25.0 |
| 新品(半年内上架) / 新品占比 | 0.25 |
| 新品(半年内上架) / 月均销量 | 1031.0 |
| 新品(半年内上架) / 月均销售额($) | 26677.0 |
| 新品(半年内上架) / 平均价格($) | 27.02 |
| 新品(半年内上架) / 平均评分数 | 46.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.254043 |
| 所有Listing(半年内) / 同类目退货率 | 0.21090001 |
| 所有Listing(半年内) / 搜索购买比 | 6.83362 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07519 |

### Bread Proofing Baskets (面包发酵篮)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bread Proofing Baskets |
| Listing样本数(TOP100) / 细分市场(翻译) | 面包发酵篮 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Bakeware:Baking Tools & Accessories:Baking & Pastry Utensils:Bread Proofing Baskets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：71 <br> 卖家：75 |
| Listing样本数(TOP100) / 月总销量 | 117453.0 |
| Listing样本数(TOP100) / 月均销量 | 1174.0 |
| Listing样本数(TOP100) / 月均销售额($) | 31037.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.88 |
| Listing样本数(TOP100) / 平均评分数 | 570.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 18024.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.427 |
| Listing样本数(TOP100) / 品牌集中度 | 0.539 |
| Listing样本数(TOP100) / 卖家集中度 | 0.535 |
| Listing样本数(TOP100) / 商品总数 | 1023.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.8781 |
| Listing样本数(TOP100) / 平均体积(in³) | 409.0568 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 5020.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 130769.0 |
| 头部Listing数(TOP10) / 平均BSR | 2025.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 604.0 |
| 新品(半年内上架) / 月均销售额($) | 16777.0 |
| 新品(半年内上架) / 平均价格($) | 27.2 |
| 新品(半年内上架) / 平均评分数 | 78.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.040874 |
| 所有Listing(半年内) / 同类目退货率 | 0.061525002 |
| 所有Listing(半年内) / 搜索购买比 | 9.56301 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06256 |

### Snorkeling Packages (套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Snorkeling Packages |
| Listing样本数(TOP100) / 细分市场(翻译) | 套装 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Water Sports:Diving & Snorkeling:Snorkeling Packages |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：58 <br> 卖家：62 |
| Listing样本数(TOP100) / 月总销量 | 116960.0 |
| Listing样本数(TOP100) / 月均销量 | 1169.0 |
| Listing样本数(TOP100) / 月均销售额($) | 34593.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.66 |
| Listing样本数(TOP100) / 平均评分数 | 1064.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 29056.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 8%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.442 |
| Listing样本数(TOP100) / 品牌集中度 | 0.59 |
| Listing样本数(TOP100) / 卖家集中度 | 0.594 |
| Listing样本数(TOP100) / 商品总数 | 610.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.6407 |
| Listing样本数(TOP100) / 平均体积(in³) | 394.123 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.94 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 5169.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 144548.0 |
| 头部Listing数(TOP10) / 平均BSR | 23396.0 |
| 新品(半年内上架) / 新品数量 | 25.0 |
| 新品(半年内上架) / 新品占比 | 0.25 |
| 新品(半年内上架) / 月均销量 | 1116.0 |
| 新品(半年内上架) / 月均销售额($) | 24854.0 |
| 新品(半年内上架) / 平均价格($) | 26.32 |
| 新品(半年内上架) / 平均评分数 | 78.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.104648 |
| 所有Listing(半年内) / 同类目退货率 | 0.104648 |
| 所有Listing(半年内) / 搜索购买比 | 10.74434 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10744 |

### Bread Knives (面包刀)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bread Knives |
| Listing样本数(TOP100) / 细分市场(翻译) | 面包刀 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Kitchen Utensils & Gadgets:Kitchen Knives & Accessories:Bread Knives |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 107908.0 |
| Listing样本数(TOP100) / 月均销量 | 1079.0 |
| Listing样本数(TOP100) / 月均销售额($) | 23603.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.57 |
| Listing样本数(TOP100) / 平均评分数 | 998.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 29854.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 82%  <br> AMZ: 13%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.468 |
| Listing样本数(TOP100) / 品牌集中度 | 0.525 |
| Listing样本数(TOP100) / 卖家集中度 | 0.586 |
| Listing样本数(TOP100) / 商品总数 | 1026.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8113 |
| Listing样本数(TOP100) / 平均体积(in³) | 152.3348 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 5046.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 125642.0 |
| 头部Listing数(TOP10) / 平均BSR | 2953.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 617.0 |
| 新品(半年内上架) / 月均销售额($) | 9688.0 |
| 新品(半年内上架) / 平均价格($) | 17.46 |
| 新品(半年内上架) / 平均评分数 | 107.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.029209001 |
| 所有Listing(半年内) / 同类目退货率 | 0.02952 |
| 所有Listing(半年内) / 搜索购买比 | 13.49718 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0692 |

### Lighting Products (水底灯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Lighting Products |
| Listing样本数(TOP100) / 细分市场(翻译) | 水底灯 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Pools, Hot Tubs & Supplies:Parts & Accessories:Lighting Products |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：71 <br> 卖家：70 |
| Listing样本数(TOP100) / 月总销量 | 103104.0 |
| Listing样本数(TOP100) / 月均销量 | 1031.0 |
| Listing样本数(TOP100) / 月均销售额($) | 50243.0 |
| Listing样本数(TOP100) / 平均价格($) | 49.41 |
| Listing样本数(TOP100) / 平均评分数 | 475.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 19479.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.328 |
| Listing样本数(TOP100) / 品牌集中度 | 0.515 |
| Listing样本数(TOP100) / 卖家集中度 | 0.542 |
| Listing样本数(TOP100) / 商品总数 | 1238.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.7026 |
| Listing样本数(TOP100) / 平均体积(in³) | 635.4793 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.97 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 76.0% |
| 头部Listing数(TOP10) / 月均销量 | 3378.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 209750.0 |
| 头部Listing数(TOP10) / 平均BSR | 3725.0 |
| 新品(半年内上架) / 新品数量 | 55.0 |
| 新品(半年内上架) / 新品占比 | 0.55 |
| 新品(半年内上架) / 月均销量 | 1109.0 |
| 新品(半年内上架) / 月均销售额($) | 61518.0 |
| 新品(半年内上架) / 平均价格($) | 51.02 |
| 新品(半年内上架) / 平均评分数 | 60.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.067492 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 5.4537 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Casual Jackets (休闲夹克)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Casual Jackets |
| Listing样本数(TOP100) / 细分市场(翻译) | 休闲夹克 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Coats, Jackets & Vests:Casual Jackets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：71 |
| Listing样本数(TOP100) / 月总销量 | 102635.0 |
| Listing样本数(TOP100) / 月均销量 | 1026.0 |
| Listing样本数(TOP100) / 月均销售额($) | 38205.0 |
| Listing样本数(TOP100) / 平均价格($) | 37.65 |
| Listing样本数(TOP100) / 平均评分数 | 833.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 80554.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 5%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.332 |
| Listing样本数(TOP100) / 品牌集中度 | 0.446 |
| Listing样本数(TOP100) / 卖家集中度 | 0.436 |
| Listing样本数(TOP100) / 商品总数 | 6743.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7892 |
| Listing样本数(TOP100) / 平均体积(in³) | 188.2375 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.96 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 3405.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 135138.0 |
| 头部Listing数(TOP10) / 平均BSR | 18783.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 800.0 |
| 新品(半年内上架) / 月均销售额($) | 27087.0 |
| 新品(半年内上架) / 平均价格($) | 35.9 |
| 新品(半年内上架) / 平均评分数 | 55.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.27815902 |
| 所有Listing(半年内) / 同类目退货率 | 0.244967 |
| 所有Listing(半年内) / 搜索购买比 | 3.99269 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04205 |

### Shilajit (Shilajit)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Shilajit |
| Listing样本数(TOP100) / 细分市场(翻译) | Shilajit |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Vitamins, Minerals & Supplements:Herbal Supplements:Shilajit |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 100999.0 |
| Listing样本数(TOP100) / 月均销量 | 1009.0 |
| Listing样本数(TOP100) / 月均销售额($) | 28921.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.19 |
| Listing样本数(TOP100) / 平均评分数 | 714.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 67607.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 2%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.523 |
| Listing样本数(TOP100) / 品牌集中度 | 0.632 |
| Listing样本数(TOP100) / 卖家集中度 | 0.616 |
| Listing样本数(TOP100) / 商品总数 | 572.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4008 |
| Listing样本数(TOP100) / 平均体积(in³) | 56.8467 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.94 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 59.0% |
| 头部Listing数(TOP10) / 月均销量 | 5285.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 140052.0 |
| 头部Listing数(TOP10) / 平均BSR | 31120.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 326.0 |
| 新品(半年内上架) / 月均销售额($) | 10296.0 |
| 新品(半年内上架) / 平均价格($) | 30.85 |
| 新品(半年内上架) / 平均评分数 | 24.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.003367 |
| 所有Listing(半年内) / 同类目退货率 | 0.002946 |
| 所有Listing(半年内) / 搜索购买比 | 15.2522 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.22895001 |

### Decorative Boxes (装饰盒)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Decorative Boxes |
| Listing样本数(TOP100) / 细分市场(翻译) | 装饰盒 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Home Décor Accents:Decorative Accessories:Decorative Boxes |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 99269.0 |
| Listing样本数(TOP100) / 月均销量 | 992.0 |
| Listing样本数(TOP100) / 月均销售额($) | 23827.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.84 |
| Listing样本数(TOP100) / 平均评分数 | 680.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 74338.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 2%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.313 |
| Listing样本数(TOP100) / 品牌集中度 | 0.491 |
| Listing样本数(TOP100) / 卖家集中度 | 0.491 |
| Listing样本数(TOP100) / 商品总数 | 6415.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.6565 |
| Listing样本数(TOP100) / 平均体积(in³) | 381.8847 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 67.0% |
| 头部Listing数(TOP10) / 月均销量 | 3103.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 70630.0 |
| 头部Listing数(TOP10) / 平均BSR | 72300.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 788.0 |
| 新品(半年内上架) / 月均销售额($) | 17579.0 |
| 新品(半年内上架) / 平均价格($) | 23.16 |
| 新品(半年内上架) / 平均评分数 | 67.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.079139 |
| 所有Listing(半年内) / 同类目退货率 | 0.050359998 |
| 所有Listing(半年内) / 搜索购买比 | 4.45329 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06534 |

### Pool & Deck Repair Products (油漆及密封产品)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Pool & Deck Repair Products |
| Listing样本数(TOP100) / 细分市场(翻译) | 油漆及密封产品 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Pools, Hot Tubs & Supplies:Parts & Accessories:Pool & Deck Repair Products |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：77 <br> 卖家：71 |
| Listing样本数(TOP100) / 月总销量 | 92366.0 |
| Listing样本数(TOP100) / 月均销量 | 923.0 |
| Listing样本数(TOP100) / 月均销售额($) | 24783.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.75 |
| Listing样本数(TOP100) / 平均评分数 | 679.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 28212.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 6%  <br> FBM: 10% |
| Listing样本数(TOP100) / 商品集中度 | 0.489 |
| Listing样本数(TOP100) / 品牌集中度 | 0.566 |
| Listing样本数(TOP100) / 卖家集中度 | 0.615 |
| Listing样本数(TOP100) / 商品总数 | 591.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4125 |
| Listing样本数(TOP100) / 平均体积(in³) | 638.6256 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.7 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 53.0% |
| 头部Listing数(TOP10) / 月均销量 | 4513.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 84256.0 |
| 头部Listing数(TOP10) / 平均BSR | 2411.0 |
| 新品(半年内上架) / 新品数量 | 23.0 |
| 新品(半年内上架) / 新品占比 | 0.23 |
| 新品(半年内上架) / 月均销量 | 631.0 |
| 新品(半年内上架) / 月均销售额($) | 12599.0 |
| 新品(半年内上架) / 平均价格($) | 19.64 |
| 新品(半年内上架) / 平均评分数 | 56.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.019322 |
| 所有Listing(半年内) / 同类目退货率 | 0.029515 |
| 所有Listing(半年内) / 搜索购买比 | 23.19476 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12637 |

### Fountains (喷泉)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Fountains |
| Listing样本数(TOP100) / 细分市场(翻译) | 喷泉 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Dogs:Feeding & Watering Supplies:Fountains |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：66 <br> 卖家：65 |
| Listing样本数(TOP100) / 月总销量 | 91637.0 |
| Listing样本数(TOP100) / 月均销量 | 916.0 |
| Listing样本数(TOP100) / 月均销售额($) | 34974.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.99 |
| Listing样本数(TOP100) / 平均评分数 | 961.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 17269.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 8%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.404 |
| Listing样本数(TOP100) / 品牌集中度 | 0.562 |
| Listing样本数(TOP100) / 卖家集中度 | 0.576 |
| Listing样本数(TOP100) / 商品总数 | 634.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.1817 |
| Listing样本数(TOP100) / 平均体积(in³) | 541.6858 |
| Listing样本数(TOP100) / 平均毛利率 | 0.64 |
| Listing样本数(TOP100) / A+占比 | 0.93 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 3702.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 138861.0 |
| 头部Listing数(TOP10) / 平均BSR | 3812.0 |
| 新品(半年内上架) / 新品数量 | 34.0 |
| 新品(半年内上架) / 新品占比 | 0.34 |
| 新品(半年内上架) / 月均销量 | 549.0 |
| 新品(半年内上架) / 月均销售额($) | 24431.0 |
| 新品(半年内上架) / 平均价格($) | 45.07 |
| 新品(半年内上架) / 平均评分数 | 61.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.04779 |
| 所有Listing(半年内) / 同类目退货率 | 0.038934 |
| 所有Listing(半年内) / 搜索购买比 | 10.23547 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13913 |

### Button-Down Shirts (扣角领衬衫)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Button-Down Shirts |
| Listing样本数(TOP100) / 细分市场(翻译) | 扣角领衬衫 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Novelty & More:Clothing:Novelty:Men:Shirts:Button-Down Shirts |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：60 |
| Listing样本数(TOP100) / 月总销量 | 90189.0 |
| Listing样本数(TOP100) / 月均销量 | 901.0 |
| Listing样本数(TOP100) / 月均销售额($) | 17672.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.38 |
| Listing样本数(TOP100) / 平均评分数 | 319.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 104403.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 1%  <br> FBM: 12% |
| Listing样本数(TOP100) / 商品集中度 | 0.304 |
| Listing样本数(TOP100) / 品牌集中度 | 0.603 |
| Listing样本数(TOP100) / 卖家集中度 | 0.594 |
| Listing样本数(TOP100) / 商品总数 | 4262.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4197 |
| Listing样本数(TOP100) / 平均体积(in³) | 88.0823 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 2746.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 56739.0 |
| 头部Listing数(TOP10) / 平均BSR | 108585.0 |
| 新品(半年内上架) / 新品数量 | 22.0 |
| 新品(半年内上架) / 新品占比 | 0.22 |
| 新品(半年内上架) / 月均销量 | 729.0 |
| 新品(半年内上架) / 月均销售额($) | 13908.0 |
| 新品(半年内上架) / 平均价格($) | 20.28 |
| 新品(半年内上架) / 平均评分数 | 34.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.140108 |
| 所有Listing(半年内) / 同类目退货率 | 0.140002 |
| 所有Listing(半年内) / 搜索购买比 | 4.18863 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.058819998 |

### Trays & Bags (托盘、口袋)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Trays & Bags |
| Listing样本数(TOP100) / 细分市场(翻译) | 托盘、口袋 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Interior Accessories:Consoles & Organizers:Trays & Bags |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 88726.0 |
| Listing样本数(TOP100) / 月均销量 | 887.0 |
| Listing样本数(TOP100) / 月均销售额($) | 18752.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.8 |
| Listing样本数(TOP100) / 平均评分数 | 874.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 24743.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 96%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.377 |
| Listing样本数(TOP100) / 品牌集中度 | 0.463 |
| Listing样本数(TOP100) / 卖家集中度 | 0.464 |
| Listing样本数(TOP100) / 商品总数 | 4414.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.192 |
| Listing样本数(TOP100) / 平均体积(in³) | 300.7238 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.83 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 89.0% |
| 头部Listing数(TOP10) / 月均销量 | 3349.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 53426.0 |
| 头部Listing数(TOP10) / 平均BSR | 79351.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 654.0 |
| 新品(半年内上架) / 月均销售额($) | 11743.0 |
| 新品(半年内上架) / 平均价格($) | 17.42 |
| 新品(半年内上架) / 平均评分数 | 163.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.09416799 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 5.9015 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Hand Fuel Pumps (手动燃油泵)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hand Fuel Pumps |
| Listing样本数(TOP100) / 细分市场(翻译) | 手动燃油泵 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Tools & Equipment:Garage & Shop:Barrel & Hand Pumps:Hand Fuel Pumps |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：82 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 88286.0 |
| Listing样本数(TOP100) / 月均销量 | 882.0 |
| Listing样本数(TOP100) / 月均销售额($) | 21856.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.24 |
| Listing样本数(TOP100) / 平均评分数 | 1023.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 51758.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 2%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.417 |
| Listing样本数(TOP100) / 品牌集中度 | 0.535 |
| Listing样本数(TOP100) / 卖家集中度 | 0.535 |
| Listing样本数(TOP100) / 商品总数 | 855.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5784 |
| Listing样本数(TOP100) / 平均体积(in³) | 415.5113 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.95 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 3678.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 61549.0 |
| 头部Listing数(TOP10) / 平均BSR | 2053.0 |
| 新品(半年内上架) / 新品数量 | 25.0 |
| 新品(半年内上架) / 新品占比 | 0.25 |
| 新品(半年内上架) / 月均销量 | 988.0 |
| 新品(半年内上架) / 月均销售额($) | 31452.0 |
| 新品(半年内上架) / 平均价格($) | 37.54 |
| 新品(半年内上架) / 平均评分数 | 154.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.042313 |
| 所有Listing(半年内) / 同类目退货率 | 0.058748998 |
| 所有Listing(半年内) / 搜索购买比 | 9.7877 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09074 |

### Casual (休闲类)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Casual |
| Listing样本数(TOP100) / 细分市场(翻译) | 休闲类 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Maternity:Dresses:Casual |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：55 <br> 卖家：55 |
| Listing样本数(TOP100) / 月总销量 | 87685.0 |
| Listing样本数(TOP100) / 月均销量 | 876.0 |
| Listing样本数(TOP100) / 月均销售额($) | 29900.0 |
| Listing样本数(TOP100) / 平均价格($) | 37.65 |
| Listing样本数(TOP100) / 平均评分数 | 860.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 136979.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 0%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.433 |
| Listing样本数(TOP100) / 品牌集中度 | 0.622 |
| Listing样本数(TOP100) / 卖家集中度 | 0.589 |
| Listing样本数(TOP100) / 商品总数 | 919.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7087 |
| Listing样本数(TOP100) / 平均体积(in³) | 149.2702 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.84 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 81.0% |
| 头部Listing数(TOP10) / 月均销量 | 3795.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 116471.0 |
| 头部Listing数(TOP10) / 平均BSR | 10643.0 |
| 新品(半年内上架) / 新品数量 | 26.0 |
| 新品(半年内上架) / 新品占比 | 0.26 |
| 新品(半年内上架) / 月均销量 | 436.0 |
| 新品(半年内上架) / 月均销售额($) | 19913.0 |
| 新品(半年内上架) / 平均价格($) | 45.68 |
| 新品(半年内上架) / 平均评分数 | 20.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | N/A |
| 所有Listing(半年内) / 同类目退货率 | N/A |
| 所有Listing(半年内) / 搜索购买比 | N/A |
| 所有Listing(半年内) / 同类目搜索购买比 | N/A |

### Beneficial Insects (益虫)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Beneficial Insects |
| Listing样本数(TOP100) / 细分市场(翻译) | 益虫 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Pest Control:Beneficial Insects |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：58 <br> 卖家：54 |
| Listing样本数(TOP100) / 月总销量 | 85364.0 |
| Listing样本数(TOP100) / 月均销量 | 853.0 |
| Listing样本数(TOP100) / 月均销售额($) | 25571.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.29 |
| Listing样本数(TOP100) / 平均评分数 | 724.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 34622.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 45%  <br> AMZ: 6%  <br> FBM: 37% |
| Listing样本数(TOP100) / 商品集中度 | 0.369 |
| Listing样本数(TOP100) / 品牌集中度 | 0.584 |
| Listing样本数(TOP100) / 卖家集中度 | 0.572 |
| Listing样本数(TOP100) / 商品总数 | 470.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.8895 |
| Listing样本数(TOP100) / 平均体积(in³) | 221.1628 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.53 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 92.0% |
| 头部Listing数(TOP10) / 月均销量 | 3149.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 98890.0 |
| 头部Listing数(TOP10) / 平均BSR | 2915.0 |
| 新品(半年内上架) / 新品数量 | 30.0 |
| 新品(半年内上架) / 新品占比 | 0.3 |
| 新品(半年内上架) / 月均销量 | 744.0 |
| 新品(半年内上架) / 月均销售额($) | 23064.0 |
| 新品(半年内上架) / 平均价格($) | 28.05 |
| 新品(半年内上架) / 平均评分数 | 34.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.007845 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 19.02987 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Nozzles (喷嘴)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Nozzles |
| Listing样本数(TOP100) / 细分市场(翻译) | 喷嘴 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Outdoor Power Tools:Replacement Parts & Accessories:Pressure Washer Parts & Accessories:Nozzles |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 84951.0 |
| Listing样本数(TOP100) / 月均销量 | 849.0 |
| Listing样本数(TOP100) / 月均销售额($) | 19384.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.98 |
| Listing样本数(TOP100) / 平均评分数 | 497.0 |
| Listing样本数(TOP100) / 平均星级 | 3.4 |
| Listing样本数(TOP100) / 平均BSR | 53028.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 61%  <br> AMZ: 5%  <br> FBM: 19% |
| Listing样本数(TOP100) / 商品集中度 | 0.493 |
| Listing样本数(TOP100) / 品牌集中度 | 0.549 |
| Listing样本数(TOP100) / 卖家集中度 | 0.575 |
| Listing样本数(TOP100) / 商品总数 | 1031.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4424 |
| Listing样本数(TOP100) / 平均体积(in³) | 66.3163 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.72 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 4186.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 79610.0 |
| 头部Listing数(TOP10) / 平均BSR | 8518.0 |
| 新品(半年内上架) / 新品数量 | 58.0 |
| 新品(半年内上架) / 新品占比 | 0.58 |
| 新品(半年内上架) / 月均销量 | 818.0 |
| 新品(半年内上架) / 月均销售额($) | 23991.0 |
| 新品(半年内上架) / 平均价格($) | 33.14 |
| 新品(半年内上架) / 平均评分数 | 54.0 |
| 新品(半年内上架) / 平均星级 | 2.6 |
| 所有Listing(半年内) / 退货率 | 0.026326 |
| 所有Listing(半年内) / 同类目退货率 | 0.049943 |
| 所有Listing(半年内) / 搜索购买比 | 13.48396 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.16228001 |

### Pantsuits (裤装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Pantsuits |
| Listing样本数(TOP100) / 细分市场(翻译) | 裤装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Suiting & Blazers:Suit Sets:Pantsuits |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：44 <br> 卖家：48 |
| Listing样本数(TOP100) / 月总销量 | 84603.0 |
| Listing样本数(TOP100) / 月均销量 | 846.0 |
| Listing样本数(TOP100) / 月均销售额($) | 47597.0 |
| Listing样本数(TOP100) / 平均价格($) | 57.91 |
| Listing样本数(TOP100) / 平均评分数 | 451.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 99570.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 2%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.442 |
| Listing样本数(TOP100) / 品牌集中度 | 0.644 |
| Listing样本数(TOP100) / 卖家集中度 | 0.615 |
| Listing样本数(TOP100) / 商品总数 | 3264.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4607 |
| Listing样本数(TOP100) / 平均体积(in³) | 264.0857 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.95 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 88.0% |
| 头部Listing数(TOP10) / 月均销量 | 3738.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 212678.0 |
| 头部Listing数(TOP10) / 平均BSR | 16242.0 |
| 新品(半年内上架) / 新品数量 | 30.0 |
| 新品(半年内上架) / 新品占比 | 0.3 |
| 新品(半年内上架) / 月均销量 | 631.0 |
| 新品(半年内上架) / 月均销售额($) | 37742.0 |
| 新品(半年内上架) / 平均价格($) | 59.95 |
| 新品(半年内上架) / 平均评分数 | 54.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.31881902 |
| 所有Listing(半年内) / 同类目退货率 | 0.260849 |
| 所有Listing(半年内) / 搜索购买比 | 2.07344 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03096 |

### Glasses & Goggles (眼镜和护目镜)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Glasses & Goggles |
| Listing样本数(TOP100) / 细分市场(翻译) | 眼镜和护目镜 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Cycling:Glasses & Goggles |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：55 <br> 卖家：58 |
| Listing样本数(TOP100) / 月总销量 | 83961.0 |
| Listing样本数(TOP100) / 月均销量 | 839.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16373.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.58 |
| Listing样本数(TOP100) / 平均评分数 | 887.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 78997.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 0%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.402 |
| Listing样本数(TOP100) / 品牌集中度 | 0.555 |
| Listing样本数(TOP100) / 卖家集中度 | 0.51 |
| Listing样本数(TOP100) / 商品总数 | 1032.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2331 |
| Listing样本数(TOP100) / 平均体积(in³) | 64.4557 |
| Listing样本数(TOP100) / 平均毛利率 | 0.64 |
| Listing样本数(TOP100) / A+占比 | 0.94 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 88.0% |
| 头部Listing数(TOP10) / 月均销量 | 3377.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 55541.0 |
| 头部Listing数(TOP10) / 平均BSR | 3211.0 |
| 新品(半年内上架) / 新品数量 | 16.0 |
| 新品(半年内上架) / 新品占比 | 0.16 |
| 新品(半年内上架) / 月均销量 | 726.0 |
| 新品(半年内上架) / 月均销售额($) | 10263.0 |
| 新品(半年内上架) / 平均价格($) | 19.05 |
| 新品(半年内上架) / 平均评分数 | 60.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.060467 |
| 所有Listing(半年内) / 同类目退货率 | 0.052837 |
| 所有Listing(半年内) / 搜索购买比 | 6.27508 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12039 |

### Cups (杯子)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Cups |
| Listing样本数(TOP100) / 细分市场(翻译) | 杯子 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Event & Party Supplies:Tableware:Cups |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：71 |
| Listing样本数(TOP100) / 月总销量 | 82408.0 |
| Listing样本数(TOP100) / 月均销量 | 824.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16989.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.43 |
| Listing样本数(TOP100) / 平均评分数 | 487.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 133559.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 8%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.469 |
| Listing样本数(TOP100) / 品牌集中度 | 0.562 |
| Listing样本数(TOP100) / 卖家集中度 | 0.636 |
| Listing样本数(TOP100) / 商品总数 | 2371.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3085 |
| Listing样本数(TOP100) / 平均体积(in³) | 39.9236 |
| Listing样本数(TOP100) / 平均毛利率 | 0.51 |
| Listing样本数(TOP100) / A+占比 | 0.65 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 3868.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 72562.0 |
| 头部Listing数(TOP10) / 平均BSR | 17266.0 |
| 新品(半年内上架) / 新品数量 | 27.0 |
| 新品(半年内上架) / 新品占比 | 0.27 |
| 新品(半年内上架) / 月均销量 | 1221.0 |
| 新品(半年内上架) / 月均销售额($) | 29126.0 |
| 新品(半年内上架) / 平均价格($) | 26.68 |
| 新品(半年内上架) / 平均评分数 | 523.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.039497003 |
| 所有Listing(半年内) / 同类目退货率 | 0.037998 |
| 所有Listing(半年内) / 搜索购买比 | 8.63317 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0766 |

### Compressed Air Dusters (压缩除尘罐)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Compressed Air Dusters |
| Listing样本数(TOP100) / 细分市场(翻译) | 压缩除尘罐 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Computers & Accessories:Computer Accessories & Peripherals:Cleaning & Repair:Compressed Air Dusters |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 81347.0 |
| Listing样本数(TOP100) / 月均销量 | 813.0 |
| Listing样本数(TOP100) / 月均销售额($) | 32612.0 |
| Listing样本数(TOP100) / 平均价格($) | 34.09 |
| Listing样本数(TOP100) / 平均评分数 | 349.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 33285.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 5%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.509 |
| Listing样本数(TOP100) / 品牌集中度 | 0.605 |
| Listing样本数(TOP100) / 卖家集中度 | 0.605 |
| Listing样本数(TOP100) / 商品总数 | 11555.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8729 |
| Listing样本数(TOP100) / 平均体积(in³) | 44.9147 |
| Listing样本数(TOP100) / 平均毛利率 | 0.74 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 76.0% |
| 头部Listing数(TOP10) / 月均销量 | 4137.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 202795.0 |
| 头部Listing数(TOP10) / 平均BSR | 3407.0 |
| 新品(半年内上架) / 新品数量 | 42.0 |
| 新品(半年内上架) / 新品占比 | 0.42 |
| 新品(半年内上架) / 月均销量 | 521.0 |
| 新品(半年内上架) / 月均销售额($) | 15746.0 |
| 新品(半年内上架) / 平均价格($) | 32.03 |
| 新品(半年内上架) / 平均评分数 | 126.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.031646 |
| 所有Listing(半年内) / 同类目退货率 | 0.031956002 |
| 所有Listing(半年内) / 搜索购买比 | 12.97452 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12949 |

### Wrinkle & Anti-Aging Devices (皱纹和抗衰老设备)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Wrinkle & Anti-Aging Devices |
| Listing样本数(TOP100) / 细分市场(翻译) | 皱纹和抗衰老设备 |
| Listing样本数(TOP100) / 市场路径 | Beauty & Personal Care:Tools & Accessories:Skin Care Tools:Wrinkle & Anti-Aging Devices |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：75 |
| Listing样本数(TOP100) / 月总销量 | 78129.0 |
| Listing样本数(TOP100) / 月均销量 | 781.0 |
| Listing样本数(TOP100) / 月均销售额($) | 116400.0 |
| Listing样本数(TOP100) / 平均价格($) | 112.68 |
| Listing样本数(TOP100) / 平均评分数 | 536.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 64944.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 1%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.44 |
| Listing样本数(TOP100) / 品牌集中度 | 0.573 |
| Listing样本数(TOP100) / 卖家集中度 | 0.559 |
| Listing样本数(TOP100) / 商品总数 | 881.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.9317 |
| Listing样本数(TOP100) / 平均体积(in³) | 156.5241 |
| Listing样本数(TOP100) / 平均毛利率 | 0.72 |
| Listing样本数(TOP100) / A+占比 | 0.95 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 49.0% |
| 头部Listing数(TOP10) / 月均销量 | 3439.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 653192.0 |
| 头部Listing数(TOP10) / 平均BSR | 12449.0 |
| 新品(半年内上架) / 新品数量 | 29.0 |
| 新品(半年内上架) / 新品占比 | 0.29 |
| 新品(半年内上架) / 月均销量 | 625.0 |
| 新品(半年内上架) / 月均销售额($) | 61177.0 |
| 新品(半年内上架) / 平均价格($) | 83.01 |
| 新品(半年内上架) / 平均评分数 | 48.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.103866994 |
| 所有Listing(半年内) / 同类目退货率 | 0.02199 |
| 所有Listing(半年内) / 搜索购买比 | 3.6745 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13852 |

### Herbal Supplements (草药补充剂)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Herbal Supplements |
| Listing样本数(TOP100) / 细分市场(翻译) | 草药补充剂 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Cats:Health Supplies:Supplements & Vitamins:Herbal Supplements |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 77591.0 |
| Listing样本数(TOP100) / 月均销量 | 775.0 |
| Listing样本数(TOP100) / 月均销售额($) | 17453.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.63 |
| Listing样本数(TOP100) / 平均评分数 | 1137.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 23373.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 5%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.521 |
| Listing样本数(TOP100) / 品牌集中度 | 0.615 |
| Listing样本数(TOP100) / 卖家集中度 | 0.633 |
| Listing样本数(TOP100) / 商品总数 | 390.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2954 |
| Listing样本数(TOP100) / 平均体积(in³) | 37.5723 |
| Listing样本数(TOP100) / 平均毛利率 | 0.64 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 47.0% |
| 头部Listing数(TOP10) / 月均销量 | 4045.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 92391.0 |
| 头部Listing数(TOP10) / 平均BSR | 5656.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 319.0 |
| 新品(半年内上架) / 月均销售额($) | 8061.0 |
| 新品(半年内上架) / 平均价格($) | 25.64 |
| 新品(半年内上架) / 平均评分数 | 42.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.004651 |
| 所有Listing(半年内) / 同类目退货率 | 0.002954 |
| 所有Listing(半年内) / 搜索购买比 | 19.57385 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.30277002 |

### Wind Spinners (Wind Spinners)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Wind Spinners |
| Listing样本数(TOP100) / 细分市场(翻译) | Wind Spinners |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Outdoor Décor:Garden Sculptures & Statues:Wind Sculptures & Spinners:Wind Spinners |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 76376.0 |
| Listing样本数(TOP100) / 月均销量 | 763.0 |
| Listing样本数(TOP100) / 月均销售额($) | 19108.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.21 |
| Listing样本数(TOP100) / 平均评分数 | 472.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 32572.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 97%  <br> AMZ: 0%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.425 |
| Listing样本数(TOP100) / 品牌集中度 | 0.53 |
| Listing样本数(TOP100) / 卖家集中度 | 0.53 |
| Listing样本数(TOP100) / 商品总数 | 1935.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4816 |
| Listing样本数(TOP100) / 平均体积(in³) | 258.0761 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 92.0% |
| 头部Listing数(TOP10) / 月均销量 | 3247.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 50245.0 |
| 头部Listing数(TOP10) / 平均BSR | 4568.0 |
| 新品(半年内上架) / 新品数量 | 22.0 |
| 新品(半年内上架) / 新品占比 | 0.22 |
| 新品(半年内上架) / 月均销量 | 742.0 |
| 新品(半年内上架) / 月均销售额($) | 12317.0 |
| 新品(半年内上架) / 平均价格($) | 20.62 |
| 新品(半年内上架) / 平均评分数 | 50.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.030934999 |
| 所有Listing(半年内) / 同类目退货率 | 0.031362 |
| 所有Listing(半年内) / 搜索购买比 | 6.56758 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06785 |

### Old Fashioned Glasses (古典杯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Old Fashioned Glasses |
| Listing样本数(TOP100) / 细分市场(翻译) | 古典杯 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Dining & Entertaining:Glassware & Drinkware:Cocktail Drinkware:Old Fashioned Glasses |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 76284.0 |
| Listing样本数(TOP100) / 月均销量 | 762.0 |
| Listing样本数(TOP100) / 月均销售额($) | 19106.0 |
| Listing样本数(TOP100) / 平均价格($) | 25.55 |
| Listing样本数(TOP100) / 平均评分数 | 1132.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 22046.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 4%  <br> FBM: 10% |
| Listing样本数(TOP100) / 商品集中度 | 0.332 |
| Listing样本数(TOP100) / 品牌集中度 | 0.44 |
| Listing样本数(TOP100) / 卖家集中度 | 0.424 |
| Listing样本数(TOP100) / 商品总数 | 4310.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.9443 |
| Listing样本数(TOP100) / 平均体积(in³) | 12.1614 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.93 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 51.0% |
| 头部Listing数(TOP10) / 月均销量 | 2534.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 62915.0 |
| 头部Listing数(TOP10) / 平均BSR | 3514.0 |
| 新品(半年内上架) / 新品数量 | 29.0 |
| 新品(半年内上架) / 新品占比 | 0.29 |
| 新品(半年内上架) / 月均销量 | 634.0 |
| 新品(半年内上架) / 月均销售额($) | 13954.0 |
| 新品(半年内上架) / 平均价格($) | 21.99 |
| 新品(半年内上架) / 平均评分数 | 31.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.046109 |
| 所有Listing(半年内) / 同类目退货率 | 0.037998 |
| 所有Listing(半年内) / 搜索购买比 | 5.61362 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0766 |

### Active Pants (运动裤)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Active Pants |
| Listing样本数(TOP100) / 细分市场(翻译) | 运动裤 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Men:Clothing:Active:Active Pants |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 75750.0 |
| Listing样本数(TOP100) / 月均销量 | 757.0 |
| Listing样本数(TOP100) / 月均销售额($) | 23005.0 |
| Listing样本数(TOP100) / 平均价格($) | 33.26 |
| Listing样本数(TOP100) / 平均评分数 | 243.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 73893.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 7%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.457 |
| Listing样本数(TOP100) / 品牌集中度 | 0.57 |
| Listing样本数(TOP100) / 卖家集中度 | 0.573 |
| Listing样本数(TOP100) / 商品总数 | 8352.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8228 |
| Listing样本数(TOP100) / 平均体积(in³) | 141.6489 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 3462.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 97775.0 |
| 头部Listing数(TOP10) / 平均BSR | 88603.0 |
| 新品(半年内上架) / 新品数量 | 35.0 |
| 新品(半年内上架) / 新品占比 | 0.35 |
| 新品(半年内上架) / 月均销量 | 569.0 |
| 新品(半年内上架) / 月均销售额($) | 19696.0 |
| 新品(半年内上架) / 平均价格($) | 35.02 |
| 新品(半年内上架) / 平均评分数 | 94.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.132312 |
| 所有Listing(半年内) / 同类目退货率 | 0.21090001 |
| 所有Listing(半年内) / 搜索购买比 | 7.0169 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07519 |

### Dresses (连衣裙)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Dresses |
| Listing样本数(TOP100) / 细分市场(翻译) | 连衣裙 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Novelty & More:Clothing:Novelty:Women:Dresses |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 73823.0 |
| Listing样本数(TOP100) / 月均销量 | 738.0 |
| Listing样本数(TOP100) / 月均销售额($) | 28962.0 |
| Listing样本数(TOP100) / 平均价格($) | 36.48 |
| Listing样本数(TOP100) / 平均评分数 | 649.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 115517.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 0%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.392 |
| Listing样本数(TOP100) / 品牌集中度 | 0.629 |
| Listing样本数(TOP100) / 卖家集中度 | 0.612 |
| Listing样本数(TOP100) / 商品总数 | 9364.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6845 |
| Listing样本数(TOP100) / 平均体积(in³) | 158.7447 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 81.0% |
| 头部Listing数(TOP10) / 月均销量 | 2892.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 122473.0 |
| 头部Listing数(TOP10) / 平均BSR | 17833.0 |
| 新品(半年内上架) / 新品数量 | 30.0 |
| 新品(半年内上架) / 新品占比 | 0.3 |
| 新品(半年内上架) / 月均销量 | 762.0 |
| 新品(半年内上架) / 月均销售额($) | 29796.0 |
| 新品(半年内上架) / 平均价格($) | 36.09 |
| 新品(半年内上架) / 平均评分数 | 46.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.26729602 |
| 所有Listing(半年内) / 同类目退货率 | 0.249143 |
| 所有Listing(半年内) / 搜索购买比 | 2.24781 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.036259998 |

### Closet Rods (壁橱杆)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Closet Rods |
| Listing样本数(TOP100) / 细分市场(翻译) | 壁橱杆 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Storage & Organization:Clothing & Closet Storage:Closet Rods & Shelves:Closet Rods |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：54 <br> 卖家：55 |
| Listing样本数(TOP100) / 月总销量 | 71017.0 |
| Listing样本数(TOP100) / 月均销量 | 710.0 |
| Listing样本数(TOP100) / 月均销售额($) | 14993.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.98 |
| Listing样本数(TOP100) / 平均评分数 | 562.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 193928.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 4%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.468 |
| Listing样本数(TOP100) / 品牌集中度 | 0.649 |
| Listing样本数(TOP100) / 卖家集中度 | 0.637 |
| Listing样本数(TOP100) / 商品总数 | 770.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.2912 |
| Listing样本数(TOP100) / 平均体积(in³) | 88.1543 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 3324.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 68926.0 |
| 头部Listing数(TOP10) / 平均BSR | 14232.0 |
| 新品(半年内上架) / 新品数量 | 20.0 |
| 新品(半年内上架) / 新品占比 | 0.2 |
| 新品(半年内上架) / 月均销量 | 498.0 |
| 新品(半年内上架) / 月均销售额($) | 11283.0 |
| 新品(半年内上架) / 平均价格($) | 22.8 |
| 新品(半年内上架) / 平均评分数 | 31.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.090714 |
| 所有Listing(半年内) / 同类目退货率 | 0.08773 |
| 所有Listing(半年内) / 搜索购买比 | 13.76511 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12696 |

### Fluid Evacuators (流体抽出器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Fluid Evacuators |
| Listing样本数(TOP100) / 细分市场(翻译) | 流体抽出器 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Tools & Equipment:Garage & Shop:Fluid Evacuators |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：68 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 70309.0 |
| Listing样本数(TOP100) / 月均销量 | 703.0 |
| Listing样本数(TOP100) / 月均销售额($) | 22097.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.01 |
| Listing样本数(TOP100) / 平均评分数 | 515.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 32078.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 64%  <br> AMZ: 6%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.399 |
| Listing样本数(TOP100) / 品牌集中度 | 0.508 |
| Listing样本数(TOP100) / 卖家集中度 | 0.492 |
| Listing样本数(TOP100) / 商品总数 | 720.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.8408 |
| Listing样本数(TOP100) / 平均体积(in³) | 638.7391 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.8 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 2808.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 51876.0 |
| 头部Listing数(TOP10) / 平均BSR | 2195.0 |
| 新品(半年内上架) / 新品数量 | 27.0 |
| 新品(半年内上架) / 新品占比 | 0.27 |
| 新品(半年内上架) / 月均销量 | 389.0 |
| 新品(半年内上架) / 月均销售额($) | 11305.0 |
| 新品(半年内上架) / 平均价格($) | 27.56 |
| 新品(半年内上架) / 平均评分数 | 37.0 |
| 新品(半年内上架) / 平均星级 | 3.1 |
| 所有Listing(半年内) / 退货率 | 0.039566 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 9.88068 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### GPS Trackers (GPS 追踪器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | GPS Trackers |
| Listing样本数(TOP100) / 细分市场(翻译) | GPS 追踪器 |
| Listing样本数(TOP100) / 市场路径 | Electronics:GPS, Finders & Accessories:GPS Trackers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 69500.0 |
| Listing样本数(TOP100) / 月均销量 | 695.0 |
| Listing样本数(TOP100) / 月均销售额($) | 25452.0 |
| Listing样本数(TOP100) / 平均价格($) | 39.52 |
| Listing样本数(TOP100) / 平均评分数 | 1028.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 14759.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 0%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.448 |
| Listing样本数(TOP100) / 品牌集中度 | 0.561 |
| Listing样本数(TOP100) / 卖家集中度 | 0.573 |
| Listing样本数(TOP100) / 商品总数 | 1135.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2596 |
| Listing样本数(TOP100) / 平均体积(in³) | 13.3642 |
| Listing样本数(TOP100) / 平均毛利率 | 0.74 |
| Listing样本数(TOP100) / A+占比 | 0.93 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 49.0% |
| 头部Listing数(TOP10) / 月均销量 | 3116.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 102012.0 |
| 头部Listing数(TOP10) / 平均BSR | 2576.0 |
| 新品(半年内上架) / 新品数量 | 43.0 |
| 新品(半年内上架) / 新品占比 | 0.43 |
| 新品(半年内上架) / 月均销量 | 461.0 |
| 新品(半年内上架) / 月均销售额($) | 13063.0 |
| 新品(半年内上架) / 平均价格($) | 29.68 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.081705 |
| 所有Listing(半年内) / 同类目退货率 | 0.081705 |
| 所有Listing(半年内) / 搜索购买比 | 5.29135 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05291 |

### Birdhouses (鸟屋)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Birdhouses |
| Listing样本数(TOP100) / 细分市场(翻译) | 鸟屋 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Backyard Birding & Wildlife:Birds:Birdhouses |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：57 |
| Listing样本数(TOP100) / 月总销量 | 66827.0 |
| Listing样本数(TOP100) / 月均销量 | 668.0 |
| Listing样本数(TOP100) / 月均销售额($) | 17648.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.93 |
| Listing样本数(TOP100) / 平均评分数 | 620.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 39555.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 3%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.362 |
| Listing样本数(TOP100) / 品牌集中度 | 0.525 |
| Listing样本数(TOP100) / 卖家集中度 | 0.525 |
| Listing样本数(TOP100) / 商品总数 | 1997.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.1636 |
| Listing样本数(TOP100) / 平均体积(in³) | 573.6122 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.85 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 69.0% |
| 头部Listing数(TOP10) / 月均销量 | 2419.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 51042.0 |
| 头部Listing数(TOP10) / 平均BSR | 8857.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 517.0 |
| 新品(半年内上架) / 月均销售额($) | 11474.0 |
| 新品(半年内上架) / 平均价格($) | 24.17 |
| 新品(半年内上架) / 平均评分数 | 37.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.029214 |
| 所有Listing(半年内) / 同类目退货率 | 0.055819 |
| 所有Listing(半年内) / 搜索购买比 | 7.22348 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04222 |

### Batteries & Battery Chargers (电池和电池)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Batteries & Battery Chargers |
| Listing样本数(TOP100) / 细分市场(翻译) | 电池和电池 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Skates, Skateboards & Scooters:Scooters & Equipment:Components & Parts:Batteries & Battery Chargers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：52 <br> 卖家：53 |
| Listing样本数(TOP100) / 月总销量 | 66611.0 |
| Listing样本数(TOP100) / 月均销量 | 666.0 |
| Listing样本数(TOP100) / 月均销售额($) | 14858.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.82 |
| Listing样本数(TOP100) / 平均评分数 | 482.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 24208.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 2%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.388 |
| Listing样本数(TOP100) / 品牌集中度 | 0.611 |
| Listing样本数(TOP100) / 卖家集中度 | 0.587 |
| Listing样本数(TOP100) / 商品总数 | 1811.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.9553 |
| Listing样本数(TOP100) / 平均体积(in³) | 56.7264 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.78 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 85.0% |
| 头部Listing数(TOP10) / 月均销量 | 2587.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 55812.0 |
| 头部Listing数(TOP10) / 平均BSR | 3996.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 508.0 |
| 新品(半年内上架) / 月均销售额($) | 13199.0 |
| 新品(半年内上架) / 平均价格($) | 24.85 |
| 新品(半年内上架) / 平均评分数 | 64.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.098332 |
| 所有Listing(半年内) / 同类目退货率 | 0.042597 |
| 所有Listing(半年内) / 搜索购买比 | 9.9352 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09342 |

### Car Stereo Receivers (汽车音响)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Car Stereo Receivers |
| Listing样本数(TOP100) / 细分市场(翻译) | 汽车音响 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Car & Vehicle Electronics:Car Electronics:Car Audio:Car Stereo Receivers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：66 <br> 卖家：75 |
| Listing样本数(TOP100) / 月总销量 | 66546.0 |
| Listing样本数(TOP100) / 月均销量 | 665.0 |
| Listing样本数(TOP100) / 月均销售额($) | 60197.0 |
| Listing样本数(TOP100) / 平均价格($) | 105.06 |
| Listing样本数(TOP100) / 平均评分数 | 967.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 9182.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 2%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.334 |
| Listing样本数(TOP100) / 品牌集中度 | 0.503 |
| Listing样本数(TOP100) / 卖家集中度 | 0.417 |
| Listing样本数(TOP100) / 商品总数 | 5625.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.0295 |
| Listing样本数(TOP100) / 平均体积(in³) | 257.7875 |
| Listing样本数(TOP100) / 平均毛利率 | 0.82 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 62.0% |
| 头部Listing数(TOP10) / 月均销量 | 2220.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 129238.0 |
| 头部Listing数(TOP10) / 平均BSR | 2067.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 558.0 |
| 新品(半年内上架) / 月均销售额($) | 33172.0 |
| 新品(半年内上架) / 平均价格($) | 79.75 |
| 新品(半年内上架) / 平均评分数 | 215.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.146601 |
| 所有Listing(半年内) / 同类目退货率 | 0.143941 |
| 所有Listing(半年内) / 搜索购买比 | 2.01565 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.022839999 |

### Battery Switches (接线柱)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Battery Switches |
| Listing样本数(TOP100) / 细分市场(翻译) | 接线柱 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Replacement Parts:Batteries & Accessories:Battery Accessories:Battery Switches |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：66 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 64762.0 |
| Listing样本数(TOP100) / 月均销量 | 647.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12304.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.79 |
| Listing样本数(TOP100) / 平均评分数 | 602.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 24456.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 4%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.439 |
| Listing样本数(TOP100) / 品牌集中度 | 0.549 |
| Listing样本数(TOP100) / 卖家集中度 | 0.554 |
| Listing样本数(TOP100) / 商品总数 | 1216.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6609 |
| Listing样本数(TOP100) / 平均体积(in³) | 34.6255 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 2846.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 42284.0 |
| 头部Listing数(TOP10) / 平均BSR | 2754.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 583.0 |
| 新品(半年内上架) / 月均销售额($) | 8409.0 |
| 新品(半年内上架) / 平均价格($) | 15.48 |
| 新品(半年内上架) / 平均评分数 | 36.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.055841 |
| 所有Listing(半年内) / 同类目退货率 | 0.074346 |
| 所有Listing(半年内) / 搜索购买比 | 12.72877 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.119090006 |

### Paddleboard Accessories (冲浪板配件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Paddleboard Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 冲浪板配件 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Water Sports:Stand-Up Paddleboarding:Paddleboard Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：81 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 62013.0 |
| Listing样本数(TOP100) / 月均销量 | 620.0 |
| Listing样本数(TOP100) / 月均销售额($) | 34916.0 |
| Listing样本数(TOP100) / 平均价格($) | 53.14 |
| Listing样本数(TOP100) / 平均评分数 | 345.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 26895.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 2%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.35 |
| Listing样本数(TOP100) / 品牌集中度 | 0.443 |
| Listing样本数(TOP100) / 卖家集中度 | 0.443 |
| Listing样本数(TOP100) / 商品总数 | 886.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4156 |
| Listing样本数(TOP100) / 平均体积(in³) | 448.519 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 69.0% |
| 头部Listing数(TOP10) / 月均销量 | 2172.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 165242.0 |
| 头部Listing数(TOP10) / 平均BSR | 4212.0 |
| 新品(半年内上架) / 新品数量 | 27.0 |
| 新品(半年内上架) / 新品占比 | 0.27 |
| 新品(半年内上架) / 月均销量 | 595.0 |
| 新品(半年内上架) / 月均销售额($) | 45046.0 |
| 新品(半年内上架) / 平均价格($) | 76.21 |
| 新品(半年内上架) / 平均评分数 | 33.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.041704997 |
| 所有Listing(半年内) / 同类目退货率 | 0.045576 |
| 所有Listing(半年内) / 搜索购买比 | 6.0687 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08298001 |

### Tap Extractors (分接抽水机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tap Extractors |
| Listing样本数(TOP100) / 细分市场(翻译) | 分接抽水机 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Power & Hand Tools:Hand Tools:Taps & Dies:Tap Extractors |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：70 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 61443.0 |
| Listing样本数(TOP100) / 月均销量 | 614.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13195.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.16 |
| Listing样本数(TOP100) / 平均评分数 | 796.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 45275.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 10%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.5 |
| Listing样本数(TOP100) / 品牌集中度 | 0.605 |
| Listing样本数(TOP100) / 卖家集中度 | 0.623 |
| Listing样本数(TOP100) / 商品总数 | 1033.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4178 |
| Listing样本数(TOP100) / 平均体积(in³) | 59.4481 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 3071.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 52022.0 |
| 头部Listing数(TOP10) / 平均BSR | 7047.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 379.0 |
| 新品(半年内上架) / 月均销售额($) | 6451.0 |
| 新品(半年内上架) / 平均价格($) | 16.04 |
| 新品(半年内上架) / 平均评分数 | 395.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.048892997 |
| 所有Listing(半年内) / 同类目退货率 | 0.04438 |
| 所有Listing(半年内) / 搜索购买比 | 8.29979 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.083170004 |

### Poultry Fountains & Waterers (家禽自动喂水器和饮水器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Poultry Fountains & Waterers |
| Listing样本数(TOP100) / 细分市场(翻译) | 家禽自动喂水器和饮水器 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Farm & Ranch:Poultry Care:Poultry Feeding & Watering Supplies:Poultry Fountains & Waterers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：58 |
| Listing样本数(TOP100) / 月总销量 | 60759.0 |
| Listing样本数(TOP100) / 月均销量 | 607.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13051.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.74 |
| Listing样本数(TOP100) / 平均评分数 | 615.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 36037.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 2%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.407 |
| Listing样本数(TOP100) / 品牌集中度 | 0.561 |
| Listing样本数(TOP100) / 卖家集中度 | 0.561 |
| Listing样本数(TOP100) / 商品总数 | 1076.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.1883 |
| Listing样本数(TOP100) / 平均体积(in³) | 770.6084 |
| Listing样本数(TOP100) / 平均毛利率 | 0.51 |
| Listing样本数(TOP100) / A+占比 | 0.84 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 2471.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 38793.0 |
| 头部Listing数(TOP10) / 平均BSR | 5476.0 |
| 新品(半年内上架) / 新品数量 | 24.0 |
| 新品(半年内上架) / 新品占比 | 0.24 |
| 新品(半年内上架) / 月均销量 | 361.0 |
| 新品(半年内上架) / 月均销售额($) | 15569.0 |
| 新品(半年内上架) / 平均价格($) | 45.45 |
| 新品(半年内上架) / 平均评分数 | 33.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.02743 |
| 所有Listing(半年内) / 同类目退货率 | 0.038934 |
| 所有Listing(半年内) / 搜索购买比 | 9.71253 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13913 |

### Replacement Sensors (更换传感器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Replacement Sensors |
| Listing样本数(TOP100) / 细分市场(翻译) | 更换传感器 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Tires & Wheels:Accessories & Parts:Tire Pressure Monitoring Systems (TPMS):Replacement Sensors |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：48 <br> 卖家：53 |
| Listing样本数(TOP100) / 月总销量 | 60721.0 |
| Listing样本数(TOP100) / 月均销量 | 607.0 |
| Listing样本数(TOP100) / 月均销售额($) | 21887.0 |
| Listing样本数(TOP100) / 平均价格($) | 46.99 |
| Listing样本数(TOP100) / 平均评分数 | 999.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 23168.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 3%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.366 |
| Listing样本数(TOP100) / 品牌集中度 | 0.619 |
| Listing样本数(TOP100) / 卖家集中度 | 0.606 |
| Listing样本数(TOP100) / 商品总数 | 3701.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4672 |
| Listing样本数(TOP100) / 平均体积(in³) | 43.0272 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.93 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 81.0% |
| 头部Listing数(TOP10) / 月均销量 | 2224.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 38754.0 |
| 头部Listing数(TOP10) / 平均BSR | 2815.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 430.0 |
| 新品(半年内上架) / 月均销售额($) | 7442.0 |
| 新品(半年内上架) / 平均价格($) | 16.29 |
| 新品(半年内上架) / 平均评分数 | 64.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.09197699 |
| 所有Listing(半年内) / 同类目退货率 | 0.088016994 |
| 所有Listing(半年内) / 搜索购买比 | 10.17792 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10689 |

### Herb & Spice Mills (草本植物)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Herb & Spice Mills |
| Listing样本数(TOP100) / 细分市场(翻译) | 草本植物 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Kitchen Utensils & Gadgets:Seasoning & Spice Tools:Herb & Spice Mills |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：70 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 59139.0 |
| Listing样本数(TOP100) / 月均销量 | 591.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12316.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.71 |
| Listing样本数(TOP100) / 平均评分数 | 759.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 34879.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 3%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.415 |
| Listing样本数(TOP100) / 品牌集中度 | 0.595 |
| Listing样本数(TOP100) / 卖家集中度 | 0.546 |
| Listing样本数(TOP100) / 商品总数 | 602.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5679 |
| Listing样本数(TOP100) / 平均体积(in³) | 28.6049 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.58 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 54.0% |
| 头部Listing数(TOP10) / 月均销量 | 2454.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 42897.0 |
| 头部Listing数(TOP10) / 平均BSR | 14995.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 871.0 |
| 新品(半年内上架) / 月均销售额($) | 13068.0 |
| 新品(半年内上架) / 平均价格($) | 15.92 |
| 新品(半年内上架) / 平均评分数 | 49.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.035457 |
| 所有Listing(半年内) / 同类目退货率 | 0.047296 |
| 所有Listing(半年内) / 搜索购买比 | 4.86349 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08383001 |

### Dash Covers (仪表盘罩)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Dash Covers |
| Listing样本数(TOP100) / 细分市场(翻译) | 仪表盘罩 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Interior Accessories:Covers:Dash Covers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：60 <br> 卖家：59 |
| Listing样本数(TOP100) / 月总销量 | 59074.0 |
| Listing样本数(TOP100) / 月均销量 | 590.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16560.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.26 |
| Listing样本数(TOP100) / 平均评分数 | 787.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 57116.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 0%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.377 |
| Listing样本数(TOP100) / 品牌集中度 | 0.629 |
| Listing样本数(TOP100) / 卖家集中度 | 0.629 |
| Listing样本数(TOP100) / 商品总数 | 7539.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.198 |
| Listing样本数(TOP100) / 平均体积(in³) | 585.4123 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 89.0% |
| 头部Listing数(TOP10) / 月均销量 | 2227.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 58386.0 |
| 头部Listing数(TOP10) / 平均BSR | 2316.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 630.0 |
| 新品(半年内上架) / 月均销售额($) | 16632.0 |
| 新品(半年内上架) / 平均价格($) | 24.66 |
| 新品(半年内上架) / 平均评分数 | 249.0 |
| 新品(半年内上架) / 平均星级 | 3.7 |
| 所有Listing(半年内) / 退货率 | 0.065544 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 4.32373 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Pant Sets (长裤套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Pant Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 长裤套装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing:Clothing Sets:Pant Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：62 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 59031.0 |
| Listing样本数(TOP100) / 月均销量 | 590.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13728.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.95 |
| Listing样本数(TOP100) / 平均评分数 | 505.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 89787.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 98%  <br> AMZ: 1%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.235 |
| Listing样本数(TOP100) / 品牌集中度 | 0.421 |
| Listing样本数(TOP100) / 卖家集中度 | 0.421 |
| Listing样本数(TOP100) / 商品总数 | 2653.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4967 |
| Listing样本数(TOP100) / 平均体积(in³) | 100.8222 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 79.0% |
| 头部Listing数(TOP10) / 月均销量 | 1387.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 33709.0 |
| 头部Listing数(TOP10) / 平均BSR | 34298.0 |
| 新品(半年内上架) / 新品数量 | 46.0 |
| 新品(半年内上架) / 新品占比 | 0.46 |
| 新品(半年内上架) / 月均销量 | 597.0 |
| 新品(半年内上架) / 月均销售额($) | 13100.0 |
| 新品(半年内上架) / 平均价格($) | 21.06 |
| 新品(半年内上架) / 平均评分数 | 86.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.109931 |
| 所有Listing(半年内) / 同类目退货率 | 0.152695 |
| 所有Listing(半年内) / 搜索购买比 | 3.7099 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04593 |

### Neon Accent Lights (霓虹灯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Neon Accent Lights |
| Listing样本数(TOP100) / 细分市场(翻译) | 霓虹灯 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Lights, Bulbs & Indicators:Accent & Off Road Lighting:LED & Neon Lights:Neon Accent Lights |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：79 |
| Listing样本数(TOP100) / 月总销量 | 58977.0 |
| Listing样本数(TOP100) / 月均销量 | 589.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13221.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.14 |
| Listing样本数(TOP100) / 平均评分数 | 944.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 35215.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 3%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.408 |
| Listing样本数(TOP100) / 品牌集中度 | 0.534 |
| Listing样本数(TOP100) / 卖家集中度 | 0.534 |
| Listing样本数(TOP100) / 商品总数 | 1755.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8278 |
| Listing样本数(TOP100) / 平均体积(in³) | 74.4996 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.85 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 87.0% |
| 头部Listing数(TOP10) / 月均销量 | 2408.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 40101.0 |
| 头部Listing数(TOP10) / 平均BSR | 2818.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 596.0 |
| 新品(半年内上架) / 月均销售额($) | 15354.0 |
| 新品(半年内上架) / 平均价格($) | 23.97 |
| 新品(半年内上架) / 平均评分数 | 304.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.06229 |
| 所有Listing(半年内) / 同类目退货率 | 0.064829 |
| 所有Listing(半年内) / 搜索购买比 | 4.21436 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03628 |

### Bladder Control Devices (膀胱控制设备)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bladder Control Devices |
| Listing样本数(TOP100) / 细分市场(翻译) | 膀胱控制设备 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Health Care:Incontinence & Ostomy:Bladder Control Devices |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 57187.0 |
| Listing样本数(TOP100) / 月均销量 | 571.0 |
| Listing样本数(TOP100) / 月均销售额($) | 21135.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.65 |
| Listing样本数(TOP100) / 平均评分数 | 499.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 53902.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 0%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.325 |
| Listing样本数(TOP100) / 品牌集中度 | 0.468 |
| Listing样本数(TOP100) / 卖家集中度 | 0.461 |
| Listing样本数(TOP100) / 商品总数 | 1870.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5626 |
| Listing样本数(TOP100) / 平均体积(in³) | 135.6869 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.76 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 60.0% |
| 头部Listing数(TOP10) / 月均销量 | 1857.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 99000.0 |
| 头部Listing数(TOP10) / 平均BSR | 21160.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 346.0 |
| 新品(半年内上架) / 月均销售额($) | 12286.0 |
| 新品(半年内上架) / 平均价格($) | 38.93 |
| 新品(半年内上架) / 平均评分数 | 218.0 |
| 新品(半年内上架) / 平均星级 | 3.7 |
| 所有Listing(半年内) / 退货率 | 0.038963 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 10.63875 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Hand Tools (手动工具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hand Tools |
| Listing样本数(TOP100) / 细分市场(翻译) | 手动工具 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Power & Hand Tools:Hand Tools |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：85 <br> 卖家：79 |
| Listing样本数(TOP100) / 月总销量 | 56330.0 |
| Listing样本数(TOP100) / 月均销量 | 563.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9458.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.88 |
| Listing样本数(TOP100) / 平均评分数 | 945.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 52895.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 79%  <br> AMZ: 11%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.443 |
| Listing样本数(TOP100) / 品牌集中度 | 0.48 |
| Listing样本数(TOP100) / 卖家集中度 | 0.569 |
| Listing样本数(TOP100) / 商品总数 | 61573.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4615 |
| Listing样本数(TOP100) / 平均体积(in³) | 160.8946 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.72 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 51.0% |
| 头部Listing数(TOP10) / 月均销量 | 2496.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 23726.0 |
| 头部Listing数(TOP10) / 平均BSR | 5400.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 447.0 |
| 新品(半年内上架) / 月均销售额($) | 8997.0 |
| 新品(半年内上架) / 平均价格($) | 25.07 |
| 新品(半年内上架) / 平均评分数 | 57.0 |
| 新品(半年内上架) / 平均星级 | 3.9 |
| 所有Listing(半年内) / 退货率 | 0.037121 |
| 所有Listing(半年内) / 同类目退货率 | 0.03838 |
| 所有Listing(半年内) / 搜索购买比 | 14.62036 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.11303 |

### Night Out (晚宴裙装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Night Out |
| Listing样本数(TOP100) / 细分市场(翻译) | 晚宴裙装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Skirts:Night Out |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：71 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 55337.0 |
| Listing样本数(TOP100) / 月均销量 | 553.0 |
| Listing样本数(TOP100) / 月均销售额($) | 15735.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.93 |
| Listing样本数(TOP100) / 平均评分数 | 542.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 131661.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 98%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.373 |
| Listing样本数(TOP100) / 品牌集中度 | 0.472 |
| Listing样本数(TOP100) / 卖家集中度 | 0.45 |
| Listing样本数(TOP100) / 商品总数 | 1942.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4668 |
| Listing样本数(TOP100) / 平均体积(in³) | 162.7265 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.78 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 86.0% |
| 头部Listing数(TOP10) / 月均销量 | 2066.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 59019.0 |
| 头部Listing数(TOP10) / 平均BSR | 29613.0 |
| 新品(半年内上架) / 新品数量 | 19.0 |
| 新品(半年内上架) / 新品占比 | 0.19 |
| 新品(半年内上架) / 月均销量 | 702.0 |
| 新品(半年内上架) / 月均销售额($) | 21191.0 |
| 新品(半年内上架) / 平均价格($) | 25.62 |
| 新品(半年内上架) / 平均评分数 | 125.0 |
| 新品(半年内上架) / 平均星级 | 3.9 |
| 所有Listing(半年内) / 退货率 | N/A |
| 所有Listing(半年内) / 同类目退货率 | N/A |
| 所有Listing(半年内) / 搜索购买比 | N/A |
| 所有Listing(半年内) / 同类目搜索购买比 | N/A |

### Battery Jumper Cables (电池跳线)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Battery Jumper Cables |
| Listing样本数(TOP100) / 细分市场(翻译) | 电池跳线 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Replacement Parts:Batteries & Accessories:Battery Accessories:Battery Jumper Cables |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 54792.0 |
| Listing样本数(TOP100) / 月均销量 | 547.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12164.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.58 |
| Listing样本数(TOP100) / 平均评分数 | 1156.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 46651.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 5%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.513 |
| Listing样本数(TOP100) / 品牌集中度 | 0.632 |
| Listing样本数(TOP100) / 卖家集中度 | 0.634 |
| Listing样本数(TOP100) / 商品总数 | 777.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4383 |
| Listing样本数(TOP100) / 平均体积(in³) | 244.5923 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.79 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 2810.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 59197.0 |
| 头部Listing数(TOP10) / 平均BSR | 3318.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 352.0 |
| 新品(半年内上架) / 月均销售额($) | 8576.0 |
| 新品(半年内上架) / 平均价格($) | 16.25 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.034912 |
| 所有Listing(半年内) / 同类目退货率 | 0.034912 |
| 所有Listing(半年内) / 搜索购买比 | 13.79707 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13797 |

### Costumes (装扮服饰)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Costumes |
| Listing样本数(TOP100) / 细分市场(翻译) | 装扮服饰 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Costumes & Accessories:Men:Costumes & Cosplay Apparel:Costumes |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 53804.0 |
| Listing样本数(TOP100) / 月均销量 | 538.0 |
| Listing样本数(TOP100) / 月均销售额($) | 19174.0 |
| Listing样本数(TOP100) / 平均价格($) | 37.4 |
| Listing样本数(TOP100) / 平均评分数 | 1007.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 95434.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 6%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.229 |
| Listing样本数(TOP100) / 品牌集中度 | 0.323 |
| Listing样本数(TOP100) / 卖家集中度 | 0.349 |
| Listing样本数(TOP100) / 商品总数 | 12579.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3581 |
| Listing样本数(TOP100) / 平均体积(in³) | 326.2726 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 1232.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 36305.0 |
| 头部Listing数(TOP10) / 平均BSR | 40873.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 579.0 |
| 新品(半年内上架) / 月均销售额($) | 17275.0 |
| 新品(半年内上架) / 平均价格($) | 33.99 |
| 新品(半年内上架) / 平均评分数 | 36.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.162536 |
| 所有Listing(半年内) / 同类目退货率 | 0.156655 |
| 所有Listing(半年内) / 搜索购买比 | 3.10572 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03512 |

### Feeders (喂食器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Feeders |
| Listing样本数(TOP100) / 细分市场(翻译) | 喂食器 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Birds:Feeding & Watering Supplies:Feeders |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：79 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 52962.0 |
| Listing样本数(TOP100) / 月均销量 | 529.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10702.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.98 |
| Listing样本数(TOP100) / 平均评分数 | 572.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 34351.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 3%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.449 |
| Listing样本数(TOP100) / 品牌集中度 | 0.48 |
| Listing样本数(TOP100) / 卖家集中度 | 0.48 |
| Listing样本数(TOP100) / 商品总数 | 1574.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0801 |
| Listing样本数(TOP100) / 平均体积(in³) | 195.9973 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.82 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 83.0% |
| 头部Listing数(TOP10) / 月均销量 | 2380.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 41378.0 |
| 头部Listing数(TOP10) / 平均BSR | 14884.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 552.0 |
| 新品(半年内上架) / 月均销售额($) | 17891.0 |
| 新品(半年内上架) / 平均价格($) | 44.42 |
| 新品(半年内上架) / 平均评分数 | 207.0 |
| 新品(半年内上架) / 平均星级 | 3.4 |
| 所有Listing(半年内) / 退货率 | 0.054422997 |
| 所有Listing(半年内) / 同类目退货率 | 0.065731004 |
| 所有Listing(半年内) / 搜索购买比 | 9.63352 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09192 |

### Emblems (车标)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Emblems |
| Listing样本数(TOP100) / 细分市场(翻译) | 车标 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Exterior Accessories:Emblems |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：63 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 52875.0 |
| Listing样本数(TOP100) / 月均销量 | 528.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10436.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.84 |
| Listing样本数(TOP100) / 平均评分数 | 582.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 18838.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 78%  <br> AMZ: 1%  <br> FBM: 18% |
| Listing样本数(TOP100) / 商品集中度 | 0.262 |
| Listing样本数(TOP100) / 品牌集中度 | 0.465 |
| Listing样本数(TOP100) / 卖家集中度 | 0.35 |
| Listing样本数(TOP100) / 商品总数 | 10756.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.1222 |
| Listing样本数(TOP100) / 平均体积(in³) | 32.4585 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.38 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 45.0% |
| 头部Listing数(TOP10) / 月均销量 | 1383.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 22190.0 |
| 头部Listing数(TOP10) / 平均BSR | 5284.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 384.0 |
| 新品(半年内上架) / 月均销售额($) | 5511.0 |
| 新品(半年内上架) / 平均价格($) | 14.74 |
| 新品(半年内上架) / 平均评分数 | 22.0 |
| 新品(半年内上架) / 平均星级 | 3.9 |
| 所有Listing(半年内) / 退货率 | 0.047126003 |
| 所有Listing(半年内) / 同类目退货率 | 0.046543002 |
| 所有Listing(半年内) / 搜索购买比 | 3.83814 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0394 |

### Assortments & Variety Gifts (种类)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Assortments & Variety Gifts |
| Listing样本数(TOP100) / 细分市场(翻译) | 种类 |
| Listing样本数(TOP100) / 市场路径 | Grocery & Gourmet Food:Food & Beverage Gifts:Assortments & Variety Gifts |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：48 <br> 卖家：53 |
| Listing样本数(TOP100) / 月总销量 | 51572.0 |
| Listing样本数(TOP100) / 月均销量 | 515.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16701.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.24 |
| Listing样本数(TOP100) / 平均评分数 | 1060.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 32026.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 4%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.377 |
| Listing样本数(TOP100) / 品牌集中度 | 0.635 |
| Listing样本数(TOP100) / 卖家集中度 | 0.611 |
| Listing样本数(TOP100) / 商品总数 | 840.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4656 |
| Listing样本数(TOP100) / 平均体积(in³) | 397.6106 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.51 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 100.0% |
| 头部Listing数(TOP10) / 月均销量 | 1945.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 64636.0 |
| 头部Listing数(TOP10) / 平均BSR | 9594.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 485.0 |
| 新品(半年内上架) / 月均销售额($) | 14167.0 |
| 新品(半年内上架) / 平均价格($) | 26.44 |
| 新品(半年内上架) / 平均评分数 | 29.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.003725 |
| 所有Listing(半年内) / 同类目退货率 | 0.001907 |
| 所有Listing(半年内) / 搜索购买比 | 6.64183 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.29152 |

### Candlestick Holders (烛台座)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Candlestick Holders |
| Listing样本数(TOP100) / 细分市场(翻译) | 烛台座 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Candles & Holders:Candleholders:Candlestick Holders |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：73 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 50007.0 |
| Listing样本数(TOP100) / 月均销量 | 500.0 |
| Listing样本数(TOP100) / 月均销售额($) | 11840.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.25 |
| Listing样本数(TOP100) / 平均评分数 | 462.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 115851.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 99%  <br> AMZ: 1%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.198 |
| Listing样本数(TOP100) / 品牌集中度 | 0.392 |
| Listing样本数(TOP100) / 卖家集中度 | 0.392 |
| Listing样本数(TOP100) / 商品总数 | 4826.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.911 |
| Listing样本数(TOP100) / 平均体积(in³) | 276.9239 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.8 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 95.0% |
| 头部Listing数(TOP10) / 月均销量 | 989.0 |
| 头部Listing数(TOP10) / 垄断度 | 1.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 16355.0 |
| 头部Listing数(TOP10) / 平均BSR | 48150.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 536.0 |
| 新品(半年内上架) / 月均销售额($) | 12002.0 |
| 新品(半年内上架) / 平均价格($) | 23.32 |
| 新品(半年内上架) / 平均评分数 | 70.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.129071 |
| 所有Listing(半年内) / 同类目退货率 | 0.084172 |
| 所有Listing(半年内) / 搜索购买比 | 5.05856 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05765 |

### Decorative Trays (装饰性托盘)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Decorative Trays |
| Listing样本数(TOP100) / 细分市场(翻译) | 装饰性托盘 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Home Décor Accents:Decorative Accessories:Decorative Trays |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：83 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 49936.0 |
| Listing样本数(TOP100) / 月均销量 | 499.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10256.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.03 |
| Listing样本数(TOP100) / 平均评分数 | 492.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 184526.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 2%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.354 |
| Listing样本数(TOP100) / 品牌集中度 | 0.43 |
| Listing样本数(TOP100) / 卖家集中度 | 0.435 |
| Listing样本数(TOP100) / 商品总数 | 2833.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.517 |
| Listing样本数(TOP100) / 平均体积(in³) | 214.3129 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 78.0% |
| 头部Listing数(TOP10) / 月均销量 | 1770.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 29613.0 |
| 头部Listing数(TOP10) / 平均BSR | 55840.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 933.0 |
| 新品(半年内上架) / 月均销售额($) | 16296.0 |
| 新品(半年内上架) / 平均价格($) | 19.9 |
| 新品(半年内上架) / 平均评分数 | 128.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.095189 |
| 所有Listing(半年内) / 同类目退货率 | 0.075026006 |
| 所有Listing(半年内) / 搜索购买比 | 4.18514 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06061 |

### Trucks (卡车)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Trucks |
| Listing样本数(TOP100) / 细分市场(翻译) | 卡车 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Remote & App Controlled Vehicles & Parts:Remote & App Controlled Vehicles:Trucks |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 49678.0 |
| Listing样本数(TOP100) / 月均销量 | 496.0 |
| Listing样本数(TOP100) / 月均销售额($) | 33136.0 |
| Listing样本数(TOP100) / 平均价格($) | 67.37 |
| Listing样本数(TOP100) / 平均评分数 | 868.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 37254.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 6%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.333 |
| Listing样本数(TOP100) / 品牌集中度 | 0.481 |
| Listing样本数(TOP100) / 卖家集中度 | 0.484 |
| Listing样本数(TOP100) / 商品总数 | 1478.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4816 |
| Listing样本数(TOP100) / 平均体积(in³) | 440.1105 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.96 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 82.0% |
| 头部Listing数(TOP10) / 月均销量 | 1652.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 123247.0 |
| 头部Listing数(TOP10) / 平均BSR | 5726.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 290.0 |
| 新品(半年内上架) / 月均销售额($) | 18262.0 |
| 新品(半年内上架) / 平均价格($) | 74.16 |
| 新品(半年内上架) / 平均评分数 | 147.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.077851 |
| 所有Listing(半年内) / 同类目退货率 | 0.041058 |
| 所有Listing(半年内) / 搜索购买比 | 1.85213 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0448 |

### Plaques & Wall Art (装饰墙)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Plaques & Wall Art |
| Listing样本数(TOP100) / 细分市场(翻译) | 装饰墙 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Outdoor Décor:Plaques & Wall Art |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：70 |
| Listing样本数(TOP100) / 月总销量 | 48871.0 |
| Listing样本数(TOP100) / 月均销量 | 488.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9093.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.35 |
| Listing样本数(TOP100) / 平均评分数 | 619.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 38533.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 0%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.329 |
| Listing样本数(TOP100) / 品牌集中度 | 0.461 |
| Listing样本数(TOP100) / 卖家集中度 | 0.461 |
| Listing样本数(TOP100) / 商品总数 | 3329.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0387 |
| Listing样本数(TOP100) / 平均体积(in³) | 69.791 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 88.0% |
| 头部Listing数(TOP10) / 月均销量 | 1608.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 26682.0 |
| 头部Listing数(TOP10) / 平均BSR | 9628.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 374.0 |
| 新品(半年内上架) / 月均销售额($) | 7183.0 |
| 新品(半年内上架) / 平均价格($) | 18.84 |
| 新品(半年内上架) / 平均评分数 | 148.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.028861001 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 4.87427 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Accessories (配件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 配件 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Interior Accessories:Anti-Theft:Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：61 <br> 卖家：63 |
| Listing样本数(TOP100) / 月总销量 | 48526.0 |
| Listing样本数(TOP100) / 月均销量 | 485.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8291.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.81 |
| Listing样本数(TOP100) / 平均评分数 | 1152.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 48007.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 0%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.457 |
| Listing样本数(TOP100) / 品牌集中度 | 0.56 |
| Listing样本数(TOP100) / 卖家集中度 | 0.539 |
| Listing样本数(TOP100) / 商品总数 | 2364.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.32 |
| Listing样本数(TOP100) / 平均体积(in³) | 39.5641 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 2219.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 29872.0 |
| 头部Listing数(TOP10) / 平均BSR | 2771.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 389.0 |
| 新品(半年内上架) / 月均销售额($) | 7036.0 |
| 新品(半年内上架) / 平均价格($) | 17.61 |
| 新品(半年内上架) / 平均评分数 | 68.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.063157 |
| 所有Listing(半年内) / 同类目退货率 | 0.065605 |
| 所有Listing(半年内) / 搜索购买比 | 8.94816 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07604 |

### Bustiers & Corsets (紧身衣)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bustiers & Corsets |
| Listing样本数(TOP100) / 细分市场(翻译) | 紧身衣 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Novelty & More:Clothing:Exotic Apparel:Women:Bustiers & Corsets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：57 <br> 卖家：59 |
| Listing样本数(TOP100) / 月总销量 | 47618.0 |
| Listing样本数(TOP100) / 月均销量 | 476.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12807.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.64 |
| Listing样本数(TOP100) / 平均评分数 | 1015.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 188129.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 0%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.414 |
| Listing样本数(TOP100) / 品牌集中度 | 0.629 |
| Listing样本数(TOP100) / 卖家集中度 | 0.622 |
| Listing样本数(TOP100) / 商品总数 | 1456.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3558 |
| Listing样本数(TOP100) / 平均体积(in³) | 135.4105 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.75 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 1972.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 57328.0 |
| 头部Listing数(TOP10) / 平均BSR | 30348.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 268.0 |
| 新品(半年内上架) / 月均销售额($) | 7115.0 |
| 新品(半年内上架) / 平均价格($) | 28.41 |
| 新品(半年内上架) / 平均评分数 | 37.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.255296 |
| 所有Listing(半年内) / 同类目退货率 | 0.25410998 |
| 所有Listing(半年内) / 搜索购买比 | 2.51206 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.02606 |

### Electrical System Tools (电气系统工具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Electrical System Tools |
| Listing样本数(TOP100) / 细分市场(翻译) | 电气系统工具 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Tools & Equipment:Electrical System Tools |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 47594.0 |
| Listing样本数(TOP100) / 月均销量 | 475.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12366.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.23 |
| Listing样本数(TOP100) / 平均评分数 | 489.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 26151.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 3%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.336 |
| Listing样本数(TOP100) / 品牌集中度 | 0.449 |
| Listing样本数(TOP100) / 卖家集中度 | 0.413 |
| Listing样本数(TOP100) / 商品总数 | 1398.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0037 |
| Listing样本数(TOP100) / 平均体积(in³) | 319.2793 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.84 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 81.0% |
| 头部Listing数(TOP10) / 月均销量 | 1599.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 27029.0 |
| 头部Listing数(TOP10) / 平均BSR | 4591.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 367.0 |
| 新品(半年内上架) / 月均销售额($) | 7072.0 |
| 新品(半年内上架) / 平均价格($) | 18.34 |
| 新品(半年内上架) / 平均评分数 | 46.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.023756001 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 9.05046 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Brake System Bleeding Tools (刹车排气)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Brake System Bleeding Tools |
| Listing样本数(TOP100) / 细分市场(翻译) | 刹车排气 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Tools & Equipment:Brake Tools:Brake System Bleeding Tools |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：70 <br> 卖家：70 |
| Listing样本数(TOP100) / 月总销量 | 47424.0 |
| Listing样本数(TOP100) / 月均销量 | 474.0 |
| Listing样本数(TOP100) / 月均销售额($) | 11533.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.56 |
| Listing样本数(TOP100) / 平均评分数 | 474.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 34378.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 7%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.347 |
| Listing样本数(TOP100) / 品牌集中度 | 0.504 |
| Listing样本数(TOP100) / 卖家集中度 | 0.512 |
| Listing样本数(TOP100) / 商品总数 | 1024.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.58 |
| Listing样本数(TOP100) / 平均体积(in³) | 308.8778 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 82.0% |
| 头部Listing数(TOP10) / 月均销量 | 1645.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 25801.0 |
| 头部Listing数(TOP10) / 平均BSR | 4701.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 378.0 |
| 新品(半年内上架) / 月均销售额($) | 7390.0 |
| 新品(半年内上架) / 平均价格($) | 18.55 |
| 新品(半年内上架) / 平均评分数 | 34.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.046921 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 8.85293 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Kava Kava (卡瓦胡椒)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Kava Kava |
| Listing样本数(TOP100) / 细分市场(翻译) | 卡瓦胡椒 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Vitamins, Minerals & Supplements:Herbal Supplements:Kava Kava |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 46884.0 |
| Listing样本数(TOP100) / 月均销量 | 468.0 |
| Listing样本数(TOP100) / 月均销售额($) | 17609.0 |
| Listing样本数(TOP100) / 平均价格($) | 35.87 |
| Listing样本数(TOP100) / 平均评分数 | 295.0 |
| Listing样本数(TOP100) / 平均星级 | 3.9 |
| Listing样本数(TOP100) / 平均BSR | 94403.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 58%  <br> AMZ: 2%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.563 |
| Listing样本数(TOP100) / 品牌集中度 | 0.634 |
| Listing样本数(TOP100) / 卖家集中度 | 0.633 |
| Listing样本数(TOP100) / 商品总数 | 336.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6461 |
| Listing样本数(TOP100) / 平均体积(in³) | 73.6447 |
| Listing样本数(TOP100) / 平均毛利率 | 0.69 |
| Listing样本数(TOP100) / A+占比 | 0.87 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 86.0% |
| 头部Listing数(TOP10) / 月均销量 | 2639.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 98436.0 |
| 头部Listing数(TOP10) / 平均BSR | 18507.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 261.0 |
| 新品(半年内上架) / 月均销售额($) | 7018.0 |
| 新品(半年内上架) / 平均价格($) | 26.98 |
| 新品(半年内上架) / 平均评分数 | 28.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.0038839998 |
| 所有Listing(半年内) / 同类目退货率 | 0.002946 |
| 所有Listing(半年内) / 搜索购买比 | 12.21349 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.22895001 |

### Cup Carriers (外卖杯托盘)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Cup Carriers |
| Listing样本数(TOP100) / 细分市场(翻译) | 外卖杯托盘 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Food Service Equipment & Supplies:Disposables:Take Out Containers:Cup Carriers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：83 <br> 卖家：82 |
| Listing样本数(TOP100) / 月总销量 | 46881.0 |
| Listing样本数(TOP100) / 月均销量 | 468.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9079.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.15 |
| Listing样本数(TOP100) / 平均评分数 | 431.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 26684.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 5%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.4 |
| Listing样本数(TOP100) / 品牌集中度 | 0.454 |
| Listing样本数(TOP100) / 卖家集中度 | 0.47 |
| Listing样本数(TOP100) / 商品总数 | 955.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6871 |
| Listing样本数(TOP100) / 平均体积(in³) | 426.7775 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.79 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 1874.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 31862.0 |
| 头部Listing数(TOP10) / 平均BSR | 4063.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 275.0 |
| 新品(半年内上架) / 月均销售额($) | 3931.0 |
| 新品(半年内上架) / 平均价格($) | 15.74 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.04599 |
| 所有Listing(半年内) / 同类目退货率 | 0.057114 |
| 所有Listing(半年内) / 搜索购买比 | 8.43054 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07751 |

### Hands Free Leashes (免手持牵绳)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hands Free Leashes |
| Listing样本数(TOP100) / 细分市场(翻译) | 免手持牵绳 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Dogs:Collars, Harnesses & Leashes:Leashes:Hands Free Leashes |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 46292.0 |
| Listing样本数(TOP100) / 月均销量 | 462.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9687.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.9 |
| Listing样本数(TOP100) / 平均评分数 | 769.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 37371.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 2%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.579 |
| Listing样本数(TOP100) / 品牌集中度 | 0.648 |
| Listing样本数(TOP100) / 卖家集中度 | 0.648 |
| Listing样本数(TOP100) / 商品总数 | 379.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7365 |
| Listing样本数(TOP100) / 平均体积(in³) | 106.9587 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.97 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 50.0% |
| 头部Listing数(TOP10) / 月均销量 | 2679.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 50221.0 |
| 头部Listing数(TOP10) / 平均BSR | 7911.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 194.0 |
| 新品(半年内上架) / 月均销售额($) | 4100.0 |
| 新品(半年内上架) / 平均价格($) | 21.15 |
| 新品(半年内上架) / 平均评分数 | 66.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.064411 |
| 所有Listing(半年内) / 同类目退货率 | 0.055361 |
| 所有Listing(半年内) / 搜索购买比 | 8.65104 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.14361 |

### Game Mats & Boards (游戏垫和游戏板)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Game Mats & Boards |
| Listing样本数(TOP100) / 细分市场(翻译) | 游戏垫和游戏板 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Games & Accessories:Game Accessories:Game Mats & Boards |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 45504.0 |
| Listing样本数(TOP100) / 月均销量 | 455.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13601.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.04 |
| Listing样本数(TOP100) / 平均评分数 | 326.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 38034.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.316 |
| Listing样本数(TOP100) / 品牌集中度 | 0.42 |
| Listing样本数(TOP100) / 卖家集中度 | 0.42 |
| Listing样本数(TOP100) / 商品总数 | 1336.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4704 |
| Listing样本数(TOP100) / 平均体积(in³) | 317.3393 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 81.0% |
| 头部Listing数(TOP10) / 月均销量 | 1437.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 42619.0 |
| 头部Listing数(TOP10) / 平均BSR | 8418.0 |
| 新品(半年内上架) / 新品数量 | 31.0 |
| 新品(半年内上架) / 新品占比 | 0.31 |
| 新品(半年内上架) / 月均销量 | 371.0 |
| 新品(半年内上架) / 月均销售额($) | 12491.0 |
| 新品(半年内上架) / 平均价格($) | 34.12 |
| 新品(半年内上架) / 平均评分数 | 30.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.075034 |
| 所有Listing(半年内) / 同类目退货率 | 0.042433 |
| 所有Listing(半年内) / 搜索购买比 | 3.76317 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05271 |

### Hand Exercisers (手部锻炼器具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hand Exercisers |
| Listing样本数(TOP100) / 细分市场(翻译) | 手部锻炼器具 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Medical Supplies & Equipment:Occupational & Physical Therapy Aids:Hand Exercisers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 43567.0 |
| Listing样本数(TOP100) / 月均销量 | 435.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9400.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.96 |
| Listing样本数(TOP100) / 平均评分数 | 806.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 97698.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 7%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.568 |
| Listing样本数(TOP100) / 品牌集中度 | 0.634 |
| Listing样本数(TOP100) / 卖家集中度 | 0.631 |
| Listing样本数(TOP100) / 商品总数 | 651.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3524 |
| Listing样本数(TOP100) / 平均体积(in³) | 121.4708 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.8 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 60.0% |
| 头部Listing数(TOP10) / 月均销量 | 2475.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 43307.0 |
| 头部Listing数(TOP10) / 平均BSR | 22890.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 147.0 |
| 新品(半年内上架) / 月均销售额($) | 4686.0 |
| 新品(半年内上架) / 平均价格($) | 38.91 |
| 新品(半年内上架) / 平均评分数 | 17.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.052963 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 9.32081 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Robots (机器人)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Robots |
| Listing样本数(TOP100) / 细分市场(翻译) | 机器人 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Remote & App Controlled Vehicles & Parts:Robots |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：83 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 43366.0 |
| Listing样本数(TOP100) / 月均销量 | 433.0 |
| Listing样本数(TOP100) / 月均销售额($) | 20017.0 |
| Listing样本数(TOP100) / 平均价格($) | 51.95 |
| Listing样本数(TOP100) / 平均评分数 | 1070.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 37578.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 7%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.4 |
| Listing样本数(TOP100) / 品牌集中度 | 0.499 |
| Listing样本数(TOP100) / 卖家集中度 | 0.509 |
| Listing样本数(TOP100) / 商品总数 | 780.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3485 |
| Listing样本数(TOP100) / 平均体积(in³) | 556.6451 |
| Listing样本数(TOP100) / 平均毛利率 | 0.66 |
| Listing样本数(TOP100) / A+占比 | 1.0 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 1733.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 59590.0 |
| 头部Listing数(TOP10) / 平均BSR | 5619.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 307.0 |
| 新品(半年内上架) / 月均销售额($) | 12776.0 |
| 新品(半年内上架) / 平均价格($) | 34.46 |
| 新品(半年内上架) / 平均评分数 | 125.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.064048 |
| 所有Listing(半年内) / 同类目退货率 | 0.033138 |
| 所有Listing(半年内) / 搜索购买比 | 2.88997 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.044650003 |

### Nut & Bolt Assortment Sets (螺母和螺栓套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Nut & Bolt Assortment Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 螺母和螺栓套装 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Fasteners:Nut & Bolt Assortment Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 43247.0 |
| Listing样本数(TOP100) / 月均销量 | 432.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8803.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.09 |
| Listing样本数(TOP100) / 平均评分数 | 279.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 21931.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 99%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.305 |
| Listing样本数(TOP100) / 品牌集中度 | 0.405 |
| Listing样本数(TOP100) / 卖家集中度 | 0.405 |
| Listing样本数(TOP100) / 商品总数 | 2413.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6433 |
| Listing样本数(TOP100) / 平均体积(in³) | 101.7498 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.8 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 84.0% |
| 头部Listing数(TOP10) / 月均销量 | 1321.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 30356.0 |
| 头部Listing数(TOP10) / 平均BSR | 4798.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 320.0 |
| 新品(半年内上架) / 月均销售额($) | 3895.0 |
| 新品(半年内上架) / 平均价格($) | 12.58 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.046125997 |
| 所有Listing(半年内) / 同类目退货率 | 0.038383998 |
| 所有Listing(半年内) / 搜索购买比 | 11.30983 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13971 |

### Motion Detectors (生命探测器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Motion Detectors |
| Listing样本数(TOP100) / 细分市场(翻译) | 生命探测器 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Security & Surveillance:Motion Detectors |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：55 <br> 卖家：58 |
| Listing样本数(TOP100) / 月总销量 | 43181.0 |
| Listing样本数(TOP100) / 月均销量 | 431.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16707.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.8 |
| Listing样本数(TOP100) / 平均评分数 | 899.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 15995.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 96%  <br> AMZ: 1%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.392 |
| Listing样本数(TOP100) / 品牌集中度 | 0.609 |
| Listing样本数(TOP100) / 卖家集中度 | 0.592 |
| Listing样本数(TOP100) / 商品总数 | 1142.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7074 |
| Listing样本数(TOP100) / 平均体积(in³) | 82.3528 |
| Listing样本数(TOP100) / 平均毛利率 | 0.77 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 1694.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 69779.0 |
| 头部Listing数(TOP10) / 平均BSR | 3207.0 |
| 新品(半年内上架) / 新品数量 | 16.0 |
| 新品(半年内上架) / 新品占比 | 0.16 |
| 新品(半年内上架) / 月均销量 | 263.0 |
| 新品(半年内上架) / 月均销售额($) | 10162.0 |
| 新品(半年内上架) / 平均价格($) | 34.74 |
| 新品(半年内上架) / 平均评分数 | 71.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.06685 |
| 所有Listing(半年内) / 同类目退货率 | 0.06685 |
| 所有Listing(半年内) / 搜索购买比 | 9.56472 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.095649995 |

### Livestock Health Supplies (牲畜健康用品)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Livestock Health Supplies |
| Listing样本数(TOP100) / 细分市场(翻译) | 牲畜健康用品 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Farm & Ranch:Livestock Supplies:Livestock Health Supplies |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 43097.0 |
| Listing样本数(TOP100) / 月均销量 | 430.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13311.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.45 |
| Listing样本数(TOP100) / 平均评分数 | 361.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 45195.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 67%  <br> AMZ: 18%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.406 |
| Listing样本数(TOP100) / 品牌集中度 | 0.513 |
| Listing样本数(TOP100) / 卖家集中度 | 0.566 |
| Listing样本数(TOP100) / 商品总数 | 1474.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.1962 |
| Listing样本数(TOP100) / 平均体积(in³) | 103.8661 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.52 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 54.0% |
| 头部Listing数(TOP10) / 月均销量 | 1751.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 45596.0 |
| 头部Listing数(TOP10) / 平均BSR | 7387.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 313.0 |
| 新品(半年内上架) / 月均销售额($) | 10630.0 |
| 新品(半年内上架) / 平均价格($) | 32.61 |
| 新品(半年内上架) / 平均评分数 | 11.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.017842 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 10.39151 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Honey Jars (蜂蜜罐子)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Honey Jars |
| Listing样本数(TOP100) / 细分市场(翻译) | 蜂蜜罐子 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Dining & Entertaining:Dinnerware & Serveware:Serveware:Honey Jars |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 42955.0 |
| Listing样本数(TOP100) / 月均销量 | 429.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9120.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.74 |
| Listing样本数(TOP100) / 平均评分数 | 662.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 43367.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 2%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.427 |
| Listing样本数(TOP100) / 品牌集中度 | 0.524 |
| Listing样本数(TOP100) / 卖家集中度 | 0.546 |
| Listing样本数(TOP100) / 商品总数 | 707.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.8319 |
| Listing样本数(TOP100) / 平均体积(in³) | 185.7807 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 75.0% |
| 头部Listing数(TOP10) / 月均销量 | 1835.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 40082.0 |
| 头部Listing数(TOP10) / 平均BSR | 6901.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 210.0 |
| 新品(半年内上架) / 月均销售额($) | 3924.0 |
| 新品(半年内上架) / 平均价格($) | 18.29 |
| 新品(半年内上架) / 平均评分数 | 24.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.053978 |
| 所有Listing(半年内) / 同类目退货率 | 0.046366 |
| 所有Listing(半年内) / 搜索购买比 | 7.79161 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08969 |

### Trophies (奖杯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Trophies |
| Listing样本数(TOP100) / 细分市场(翻译) | 奖杯 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports & Outdoor Recreation Accessories:Trophies, Medals & Awards:Trophies |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：64 |
| Listing样本数(TOP100) / 月总销量 | 42954.0 |
| Listing样本数(TOP100) / 月均销量 | 429.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9270.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.41 |
| Listing样本数(TOP100) / 平均评分数 | 291.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 31343.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 71%  <br> AMZ: 1%  <br> FBM: 26% |
| Listing样本数(TOP100) / 商品集中度 | 0.276 |
| Listing样本数(TOP100) / 品牌集中度 | 0.46 |
| Listing样本数(TOP100) / 卖家集中度 | 0.467 |
| Listing样本数(TOP100) / 商品总数 | 6638.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.9705 |
| Listing样本数(TOP100) / 平均体积(in³) | 172.1132 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 54.0% |
| 头部Listing数(TOP10) / 月均销量 | 1187.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 20612.0 |
| 头部Listing数(TOP10) / 平均BSR | 7997.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 337.0 |
| 新品(半年内上架) / 月均销售额($) | 11024.0 |
| 新品(半年内上架) / 平均价格($) | 29.89 |
| 新品(半年内上架) / 平均评分数 | 29.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.025889002 |
| 所有Listing(半年内) / 同类目退货率 | 0.045063 |
| 所有Listing(半年内) / 搜索购买比 | 6.49451 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07428 |

### Decorative Candle Lanterns (装饰性点烛灯笼)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Decorative Candle Lanterns |
| Listing样本数(TOP100) / 细分市场(翻译) | 装饰性点烛灯笼 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Candles & Holders:Candleholders:Decorative Candle Lanterns |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：60 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 42606.0 |
| Listing样本数(TOP100) / 月均销量 | 426.0 |
| Listing样本数(TOP100) / 月均销售额($) | 14991.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.49 |
| Listing样本数(TOP100) / 平均评分数 | 823.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 144523.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 2%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.284 |
| Listing样本数(TOP100) / 品牌集中度 | 0.452 |
| Listing样本数(TOP100) / 卖家集中度 | 0.441 |
| Listing样本数(TOP100) / 商品总数 | 1615.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.5817 |
| Listing样本数(TOP100) / 平均体积(in³) | 515.0843 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 78.0% |
| 头部Listing数(TOP10) / 月均销量 | 1212.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 32810.0 |
| 头部Listing数(TOP10) / 平均BSR | 35281.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 377.0 |
| 新品(半年内上架) / 月均销售额($) | 16712.0 |
| 新品(半年内上架) / 平均价格($) | 44.48 |
| 新品(半年内上架) / 平均评分数 | 39.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.103667 |
| 所有Listing(半年内) / 同类目退货率 | 0.084172 |
| 所有Listing(半年内) / 搜索购买比 | 4.02434 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05765 |

### Hair Accessories (头饰)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hair Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 头饰 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Dogs:Apparel & Accessories:Hair Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 41956.0 |
| Listing样本数(TOP100) / 月均销量 | 419.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8273.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.96 |
| Listing样本数(TOP100) / 平均评分数 | 657.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 23769.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 0%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.316 |
| Listing样本数(TOP100) / 品牌集中度 | 0.366 |
| Listing样本数(TOP100) / 卖家集中度 | 0.366 |
| Listing样本数(TOP100) / 商品总数 | 1528.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6684 |
| Listing样本数(TOP100) / 平均体积(in³) | 756.9769 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 76.0% |
| 头部Listing数(TOP10) / 月均销量 | 1325.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13220.0 |
| 头部Listing数(TOP10) / 平均BSR | 7178.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 299.0 |
| 新品(半年内上架) / 月均销售额($) | 8860.0 |
| 新品(半年内上架) / 平均价格($) | 35.07 |
| 新品(半年内上架) / 平均评分数 | 31.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.043555997 |
| 所有Listing(半年内) / 同类目退货率 | 0.028313 |
| 所有Listing(半年内) / 搜索购买比 | 7.71337 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.16683 |

### Horns & Sirens (喇叭)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Horns & Sirens |
| Listing样本数(TOP100) / 细分市场(翻译) | 喇叭 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Security & Surveillance:Horns & Sirens |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 41443.0 |
| Listing样本数(TOP100) / 月均销量 | 414.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9857.0 |
| Listing样本数(TOP100) / 平均价格($) | 28.33 |
| Listing样本数(TOP100) / 平均评分数 | 1160.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 18629.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 5%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.497 |
| Listing样本数(TOP100) / 品牌集中度 | 0.602 |
| Listing样本数(TOP100) / 卖家集中度 | 0.563 |
| Listing样本数(TOP100) / 商品总数 | 1147.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0219 |
| Listing样本数(TOP100) / 平均体积(in³) | 78.991 |
| Listing样本数(TOP100) / 平均毛利率 | 0.71 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 62.0% |
| 头部Listing数(TOP10) / 月均销量 | 2057.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 41993.0 |
| 头部Listing数(TOP10) / 平均BSR | 2198.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 209.0 |
| 新品(半年内上架) / 月均销售额($) | 6369.0 |
| 新品(半年内上架) / 平均价格($) | 29.01 |
| 新品(半年内上架) / 平均评分数 | 28.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.038929 |
| 所有Listing(半年内) / 同类目退货率 | 0.07509 |
| 所有Listing(半年内) / 搜索购买比 | 6.78307 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08597 |

### Book Stands (书架)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Book Stands |
| Listing样本数(TOP100) / 细分市场(翻译) | 书架 |
| Listing样本数(TOP100) / 市场路径 | Office Products:Office & School Supplies:Desk Accessories & Workspace Organizers:Platforms, Stands & Shelves:Book Stands |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：81 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 41297.0 |
| Listing样本数(TOP100) / 月均销量 | 412.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9173.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.06 |
| Listing样本数(TOP100) / 平均评分数 | 797.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 51717.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 98%  <br> AMZ: 1%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.595 |
| Listing样本数(TOP100) / 品牌集中度 | 0.642 |
| Listing样本数(TOP100) / 卖家集中度 | 0.642 |
| Listing样本数(TOP100) / 商品总数 | 668.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6461 |
| Listing样本数(TOP100) / 平均体积(in³) | 788.1802 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 75.0% |
| 头部Listing数(TOP10) / 月均销量 | 2457.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 47089.0 |
| 头部Listing数(TOP10) / 平均BSR | 6339.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 179.0 |
| 新品(半年内上架) / 月均销售额($) | 4263.0 |
| 新品(半年内上架) / 平均价格($) | 25.56 |
| 新品(半年内上架) / 平均评分数 | 33.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.0596 |
| 所有Listing(半年内) / 同类目退货率 | 0.052835997 |
| 所有Listing(半年内) / 搜索购买比 | 7.91137 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092939995 |

### Airbrush Sets (喷漆套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Airbrush Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 喷漆套装 |
| Listing样本数(TOP100) / 市场路径 | Arts, Crafts & Sewing:Painting, Drawing & Art Supplies:Painting:Airbrush Materials:Airbrush Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：62 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 41210.0 |
| Listing样本数(TOP100) / 月均销量 | 412.0 |
| Listing样本数(TOP100) / 月均销售额($) | 18576.0 |
| Listing样本数(TOP100) / 平均价格($) | 51.53 |
| Listing样本数(TOP100) / 平均评分数 | 901.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 23002.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 1%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.349 |
| Listing样本数(TOP100) / 品牌集中度 | 0.586 |
| Listing样本数(TOP100) / 卖家集中度 | 0.596 |
| Listing样本数(TOP100) / 商品总数 | 1267.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4975 |
| Listing样本数(TOP100) / 平均体积(in³) | 397.4592 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 1439.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 45391.0 |
| 头部Listing数(TOP10) / 平均BSR | 4447.0 |
| 新品(半年内上架) / 新品数量 | 16.0 |
| 新品(半年内上架) / 新品占比 | 0.16 |
| 新品(半年内上架) / 月均销量 | 244.0 |
| 新品(半年内上架) / 月均销售额($) | 11966.0 |
| 新品(半年内上架) / 平均价格($) | 44.75 |
| 新品(半年内上架) / 平均评分数 | 128.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.046711996 |
| 所有Listing(半年内) / 同类目退货率 | 0.037488 |
| 所有Listing(半年内) / 搜索购买比 | 5.26168 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10263 |

### Welding Helmets (焊接头盔)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Welding Helmets |
| Listing样本数(TOP100) / 细分市场(翻译) | 焊接头盔 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Safety & Security:Personal Protective Equipment:Head Protection:Welding Helmets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：55 <br> 卖家：56 |
| Listing样本数(TOP100) / 月总销量 | 40737.0 |
| Listing样本数(TOP100) / 月均销量 | 407.0 |
| Listing样本数(TOP100) / 月均销售额($) | 22685.0 |
| Listing样本数(TOP100) / 平均价格($) | 61.89 |
| Listing样本数(TOP100) / 平均评分数 | 874.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 56686.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 9%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.418 |
| Listing样本数(TOP100) / 品牌集中度 | 0.627 |
| Listing样本数(TOP100) / 卖家集中度 | 0.646 |
| Listing样本数(TOP100) / 商品总数 | 1614.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.1588 |
| Listing样本数(TOP100) / 平均体积(in³) | 524.947 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 1704.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 83958.0 |
| 头部Listing数(TOP10) / 平均BSR | 10057.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 247.0 |
| 新品(半年内上架) / 月均销售额($) | 19661.0 |
| 新品(半年内上架) / 平均价格($) | 76.02 |
| 新品(半年内上架) / 平均评分数 | 221.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.034581 |
| 所有Listing(半年内) / 同类目退货率 | 0.035314 |
| 所有Listing(半年内) / 搜索购买比 | 4.95592 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09945 |

### Insulin Injectors (胰岛素注射器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Insulin Injectors |
| Listing样本数(TOP100) / 细分市场(翻译) | 胰岛素注射器 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Health Care:Diabetes Care:Insulin Injectors |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：56 <br> 卖家：62 |
| Listing样本数(TOP100) / 月总销量 | 40295.0 |
| Listing样本数(TOP100) / 月均销量 | 402.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8501.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.29 |
| Listing样本数(TOP100) / 平均评分数 | 479.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 90650.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 59%  <br> AMZ: 1%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.43 |
| Listing样本数(TOP100) / 品牌集中度 | 0.64 |
| Listing样本数(TOP100) / 卖家集中度 | 0.573 |
| Listing样本数(TOP100) / 商品总数 | 285.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4666 |
| Listing样本数(TOP100) / 平均体积(in³) | 125.0889 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.51 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 62.0% |
| 头部Listing数(TOP10) / 月均销量 | 1733.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 26450.0 |
| 头部Listing数(TOP10) / 平均BSR | 24106.0 |
| 新品(半年内上架) / 新品数量 | 36.0 |
| 新品(半年内上架) / 新品占比 | 0.36 |
| 新品(半年内上架) / 月均销量 | 299.0 |
| 新品(半年内上架) / 月均销售额($) | 9075.0 |
| 新品(半年内上架) / 平均价格($) | 29.79 |
| 新品(半年内上架) / 平均评分数 | 92.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.014974001 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 24.85349 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Alternative Medicine (替代药物)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Alternative Medicine |
| Listing样本数(TOP100) / 细分市场(翻译) | 替代药物 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Health Care:Alternative Medicine |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：86 |
| Listing样本数(TOP100) / 月总销量 | 40156.0 |
| Listing样本数(TOP100) / 月均销量 | 401.0 |
| Listing样本数(TOP100) / 月均销售额($) | 11359.0 |
| Listing样本数(TOP100) / 平均价格($) | 39.92 |
| Listing样本数(TOP100) / 平均评分数 | 940.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 163785.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 68%  <br> AMZ: 4%  <br> FBM: 24% |
| Listing样本数(TOP100) / 商品集中度 | 0.555 |
| Listing样本数(TOP100) / 品牌集中度 | 0.589 |
| Listing样本数(TOP100) / 卖家集中度 | 0.592 |
| Listing样本数(TOP100) / 商品总数 | 37769.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5354 |
| Listing样本数(TOP100) / 平均体积(in³) | 100.1454 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.61 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 52.0% |
| 头部Listing数(TOP10) / 月均销量 | 2230.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 47119.0 |
| 头部Listing数(TOP10) / 平均BSR | 18370.0 |
| 新品(半年内上架) / 新品数量 | 30.0 |
| 新品(半年内上架) / 新品占比 | 0.3 |
| 新品(半年内上架) / 月均销量 | 227.0 |
| 新品(半年内上架) / 月均销售额($) | 7246.0 |
| 新品(半年内上架) / 平均价格($) | 55.13 |
| 新品(半年内上架) / 平均评分数 | 16.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.025834 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 15.26167 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Candle Sets (蜡烛套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Candle Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 蜡烛套装 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Candles & Holders:Candles:Candle Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 39253.0 |
| Listing样本数(TOP100) / 月均销量 | 392.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8411.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.04 |
| Listing样本数(TOP100) / 平均评分数 | 1132.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 205328.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 99%  <br> AMZ: 1%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.463 |
| Listing样本数(TOP100) / 品牌集中度 | 0.545 |
| Listing样本数(TOP100) / 卖家集中度 | 0.544 |
| Listing样本数(TOP100) / 商品总数 | 1042.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.6433 |
| Listing样本数(TOP100) / 平均体积(in³) | 18.9338 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.73 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 54.0% |
| 头部Listing数(TOP10) / 月均销量 | 1816.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 38567.0 |
| 头部Listing数(TOP10) / 平均BSR | 39543.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 379.0 |
| 新品(半年内上架) / 月均销售额($) | 9101.0 |
| 新品(半年内上架) / 平均价格($) | 28.83 |
| 新品(半年内上架) / 平均评分数 | 1018.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.052092 |
| 所有Listing(半年内) / 同类目退货率 | 0.034018 |
| 所有Listing(半年内) / 搜索购买比 | 6.19824 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.100389995 |

### Oolong (乌龙)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Oolong |
| Listing样本数(TOP100) / 细分市场(翻译) | 乌龙 |
| Listing样本数(TOP100) / 市场路径 | Grocery & Gourmet Food:Beverages:Tea:Oolong |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：62 <br> 卖家：60 |
| Listing样本数(TOP100) / 月总销量 | 38516.0 |
| Listing样本数(TOP100) / 月均销量 | 385.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7430.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.14 |
| Listing样本数(TOP100) / 平均评分数 | 464.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 51432.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 69%  <br> AMZ: 10%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.479 |
| Listing样本数(TOP100) / 品牌集中度 | 0.597 |
| Listing样本数(TOP100) / 卖家集中度 | 0.615 |
| Listing样本数(TOP100) / 商品总数 | 572.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4608 |
| Listing样本数(TOP100) / 平均体积(in³) | 111.8742 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.73 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 51.0% |
| 头部Listing数(TOP10) / 月均销量 | 1845.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 33581.0 |
| 头部Listing数(TOP10) / 平均BSR | 11372.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 278.0 |
| 新品(半年内上架) / 月均销售额($) | 7272.0 |
| 新品(半年内上架) / 平均价格($) | 25.23 |
| 新品(半年内上架) / 平均评分数 | 35.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.002602 |
| 所有Listing(半年内) / 同类目退货率 | 0.002361 |
| 所有Listing(半年内) / 搜索购买比 | 18.169 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.24787001 |

### Headlights (车头灯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Headlights |
| Listing样本数(TOP100) / 细分市场(翻译) | 车头灯 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Cycling:Accessories:Lights & Reflectors:Headlights |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 35959.0 |
| Listing样本数(TOP100) / 月均销量 | 359.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10229.0 |
| Listing样本数(TOP100) / 平均价格($) | 33.78 |
| Listing样本数(TOP100) / 平均评分数 | 557.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 55894.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 2%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.499 |
| Listing样本数(TOP100) / 品牌集中度 | 0.578 |
| Listing样本数(TOP100) / 卖家集中度 | 0.544 |
| Listing样本数(TOP100) / 商品总数 | 896.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4668 |
| Listing样本数(TOP100) / 平均体积(in³) | 32.3035 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 1794.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 40775.0 |
| 头部Listing数(TOP10) / 平均BSR | 9732.0 |
| 新品(半年内上架) / 新品数量 | 16.0 |
| 新品(半年内上架) / 新品占比 | 0.16 |
| 新品(半年内上架) / 月均销量 | 268.0 |
| 新品(半年内上架) / 月均销售额($) | 5944.0 |
| 新品(半年内上架) / 平均价格($) | 24.41 |
| 新品(半年内上架) / 平均评分数 | 29.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.052114 |
| 所有Listing(半年内) / 同类目退货率 | 0.042093 |
| 所有Listing(半年内) / 搜索购买比 | 4.69257 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05573 |

### Handlebar Mounts (Handlebar Mounts)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Handlebar Mounts |
| Listing样本数(TOP100) / 细分市场(翻译) | Handlebar Mounts |
| Listing样本数(TOP100) / 市场路径 | Cell Phones & Accessories:Accessories:Mounts:Handlebar Mounts |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：75 |
| Listing样本数(TOP100) / 月总销量 | 35620.0 |
| Listing样本数(TOP100) / 月均销量 | 356.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7344.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.03 |
| Listing样本数(TOP100) / 平均评分数 | 851.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 21341.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 3%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.558 |
| Listing样本数(TOP100) / 品牌集中度 | 0.619 |
| Listing样本数(TOP100) / 卖家集中度 | 0.616 |
| Listing样本数(TOP100) / 商品总数 | 625.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.859 |
| Listing样本数(TOP100) / 平均体积(in³) | 43.5258 |
| Listing样本数(TOP100) / 平均毛利率 | 0.69 |
| Listing样本数(TOP100) / A+占比 | 0.83 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 1986.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 34670.0 |
| 头部Listing数(TOP10) / 平均BSR | 4545.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 179.0 |
| 新品(半年内上架) / 月均销售额($) | 3030.0 |
| 新品(半年内上架) / 平均价格($) | 17.98 |
| 新品(半年内上架) / 平均评分数 | 69.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.05366 |
| 所有Listing(半年内) / 同类目退货率 | 0.065120004 |
| 所有Listing(半年内) / 搜索购买比 | 8.00432 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10348 |

### Shoes (鞋)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Shoes |
| Listing样本数(TOP100) / 细分市场(翻译) | 鞋 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Shoes |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 34925.0 |
| Listing样本数(TOP100) / 月均销量 | 349.0 |
| Listing样本数(TOP100) / 月均销售额($) | 17107.0 |
| Listing样本数(TOP100) / 平均价格($) | 49.29 |
| Listing样本数(TOP100) / 平均评分数 | 271.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 446056.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 61%  <br> AMZ: 16%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.438 |
| Listing样本数(TOP100) / 品牌集中度 | 0.518 |
| Listing样本数(TOP100) / 卖家集中度 | 0.589 |
| Listing样本数(TOP100) / 商品总数 | 69884.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.47 |
| Listing样本数(TOP100) / 平均体积(in³) | 330.9647 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.71 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 50.0% |
| 头部Listing数(TOP10) / 月均销量 | 1530.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 74542.0 |
| 头部Listing数(TOP10) / 平均BSR | 83062.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 671.0 |
| 新品(半年内上架) / 月均销售额($) | 24355.0 |
| 新品(半年内上架) / 平均价格($) | 37.81 |
| 新品(半年内上架) / 平均评分数 | 30.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.215588 |
| 所有Listing(半年内) / 同类目退货率 | 0.182274 |
| 所有Listing(半年内) / 搜索购买比 | 3.0016 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03855 |

### Clutches (手拿包)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Clutches |
| Listing样本数(TOP100) / 细分市场(翻译) | 手拿包 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Handbags & Wallets:Clutches & Evening Bags:Clutches |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 34462.0 |
| Listing样本数(TOP100) / 月均销量 | 344.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9659.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.44 |
| Listing样本数(TOP100) / 平均评分数 | 452.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 194876.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 6%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.447 |
| Listing样本数(TOP100) / 品牌集中度 | 0.498 |
| Listing样本数(TOP100) / 卖家集中度 | 0.502 |
| Listing样本数(TOP100) / 商品总数 | 1282.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5782 |
| Listing样本数(TOP100) / 平均体积(in³) | 148.9852 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.78 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 1539.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 38482.0 |
| 头部Listing数(TOP10) / 平均BSR | 34774.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 320.0 |
| 新品(半年内上架) / 月均销售额($) | 7368.0 |
| 新品(半年内上架) / 平均价格($) | 21.48 |
| 新品(半年内上架) / 平均评分数 | 176.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.159632 |
| 所有Listing(半年内) / 同类目退货率 | 0.133267 |
| 所有Listing(半年内) / 搜索购买比 | 2.82445 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.02784 |

### Boats (船)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Boats |
| Listing样本数(TOP100) / 细分市场(翻译) | 船 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Remote & App Controlled Vehicles & Parts:Remote & App Controlled Vehicles:Boats |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：62 |
| Listing样本数(TOP100) / 月总销量 | 33825.0 |
| Listing样本数(TOP100) / 月均销量 | 338.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16315.0 |
| Listing样本数(TOP100) / 平均价格($) | 56.23 |
| Listing样本数(TOP100) / 平均评分数 | 338.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 51340.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 4%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.401 |
| Listing样本数(TOP100) / 品牌集中度 | 0.615 |
| Listing样本数(TOP100) / 卖家集中度 | 0.589 |
| Listing样本数(TOP100) / 商品总数 | 837.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4895 |
| Listing样本数(TOP100) / 平均体积(in³) | 317.4907 |
| Listing样本数(TOP100) / 平均毛利率 | 0.69 |
| Listing样本数(TOP100) / A+占比 | 0.96 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 69.0% |
| 头部Listing数(TOP10) / 月均销量 | 1356.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 60780.0 |
| 头部Listing数(TOP10) / 平均BSR | 6367.0 |
| 新品(半年内上架) / 新品数量 | 30.0 |
| 新品(半年内上架) / 新品占比 | 0.3 |
| 新品(半年内上架) / 月均销量 | 308.0 |
| 新品(半年内上架) / 月均销售额($) | 14868.0 |
| 新品(半年内上架) / 平均价格($) | 55.97 |
| 新品(半年内上架) / 平均评分数 | 29.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.060324997 |
| 所有Listing(半年内) / 同类目退货率 | 0.041058 |
| 所有Listing(半年内) / 搜索购买比 | 2.9031 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0448 |

### Tattoo Kits (纹身套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tattoo Kits |
| Listing样本数(TOP100) / 细分市场(翻译) | 纹身套装 |
| Listing样本数(TOP100) / 市场路径 | Beauty & Personal Care:Personal Care:Piercing & Tattoo Supplies:Tattoo Supplies:Tattoo Kits |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：48 <br> 卖家：53 |
| Listing样本数(TOP100) / 月总销量 | 33682.0 |
| Listing样本数(TOP100) / 月均销量 | 336.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10048.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.8 |
| Listing样本数(TOP100) / 平均评分数 | 530.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 83155.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 1%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.409 |
| Listing样本数(TOP100) / 品牌集中度 | 0.633 |
| Listing样本数(TOP100) / 卖家集中度 | 0.573 |
| Listing样本数(TOP100) / 商品总数 | 500.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5237 |
| Listing样本数(TOP100) / 平均体积(in³) | 212.9521 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 1377.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 34461.0 |
| 头部Listing数(TOP10) / 平均BSR | 20157.0 |
| 新品(半年内上架) / 新品数量 | 23.0 |
| 新品(半年内上架) / 新品占比 | 0.23 |
| 新品(半年内上架) / 月均销量 | 199.0 |
| 新品(半年内上架) / 月均销售额($) | 5966.0 |
| 新品(半年内上架) / 平均价格($) | 28.93 |
| 新品(半年内上架) / 平均评分数 | 63.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.020937 |
| 所有Listing(半年内) / 同类目退货率 | 0.02199 |
| 所有Listing(半年内) / 搜索购买比 | 5.5302 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13852 |

### Remote & App Controlled Vehicle Batteries (遥控)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Remote & App Controlled Vehicle Batteries |
| Listing样本数(TOP100) / 细分市场(翻译) | 遥控 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Remote & App Controlled Vehicles & Parts:Remote & App Controlled Vehicle Parts:Remote & App Controlled Vehicle Batteries |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：50 <br> 卖家：56 |
| Listing样本数(TOP100) / 月总销量 | 32797.0 |
| Listing样本数(TOP100) / 月均销量 | 327.0 |
| Listing样本数(TOP100) / 月均销售额($) | 11301.0 |
| Listing样本数(TOP100) / 平均价格($) | 35.6 |
| Listing样本数(TOP100) / 平均评分数 | 455.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 34359.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 73%  <br> AMZ: 6%  <br> FBM: 9% |
| Listing样本数(TOP100) / 商品集中度 | 0.234 |
| Listing样本数(TOP100) / 品牌集中度 | 0.586 |
| Listing样本数(TOP100) / 卖家集中度 | 0.524 |
| Listing样本数(TOP100) / 商品总数 | 6310.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3771 |
| Listing样本数(TOP100) / 平均体积(in³) | 26.4068 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.62 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 70.0% |
| 头部Listing数(TOP10) / 月均销量 | 766.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 24932.0 |
| 头部Listing数(TOP10) / 平均BSR | 12168.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 308.0 |
| 新品(半年内上架) / 月均销售额($) | 10425.0 |
| 新品(半年内上架) / 平均价格($) | 35.14 |
| 新品(半年内上架) / 平均评分数 | 37.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.062655 |
| 所有Listing(半年内) / 同类目退货率 | 0.020329 |
| 所有Listing(半年内) / 搜索购买比 | 6.65393 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.23034 |

### Network & Cable Testers (网络)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Network & Cable Testers |
| Listing样本数(TOP100) / 细分市场(翻译) | 网络 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Test, Measure & Inspect:Network & Cable Testers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：62 |
| Listing样本数(TOP100) / 月总销量 | 32621.0 |
| Listing样本数(TOP100) / 月均销量 | 326.0 |
| Listing样本数(TOP100) / 月均销售额($) | 25059.0 |
| Listing样本数(TOP100) / 平均价格($) | 119.03 |
| Listing样本数(TOP100) / 平均评分数 | 426.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 28907.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 17%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.397 |
| Listing样本数(TOP100) / 品牌集中度 | 0.645 |
| Listing样本数(TOP100) / 卖家集中度 | 0.616 |
| Listing样本数(TOP100) / 商品总数 | 1329.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6134 |
| Listing样本数(TOP100) / 平均体积(in³) | 102.7811 |
| Listing样本数(TOP100) / 平均毛利率 | 0.73 |
| Listing样本数(TOP100) / A+占比 | 0.85 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 70.0% |
| 头部Listing数(TOP10) / 月均销量 | 1294.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 73046.0 |
| 头部Listing数(TOP10) / 平均BSR | 5785.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 239.0 |
| 新品(半年内上架) / 月均销售额($) | 9859.0 |
| 新品(半年内上架) / 平均价格($) | 57.29 |
| 新品(半年内上架) / 平均评分数 | 51.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.052297 |
| 所有Listing(半年内) / 同类目退货率 | 0.044552002 |
| 所有Listing(半年内) / 搜索购买比 | 9.25091 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09328 |

### Sewing Storage (缝纫用品收纳用品)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Sewing Storage |
| Listing样本数(TOP100) / 细分市场(翻译) | 缝纫用品收纳用品 |
| Listing样本数(TOP100) / 市场路径 | Arts, Crafts & Sewing:Organization, Storage & Transport:Craft & Sewing Supplies Storage:Sewing Storage |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：83 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 32296.0 |
| Listing样本数(TOP100) / 月均销量 | 322.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6763.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.93 |
| Listing样本数(TOP100) / 平均评分数 | 929.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 29168.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 9%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.405 |
| Listing样本数(TOP100) / 品牌集中度 | 0.505 |
| Listing样本数(TOP100) / 卖家集中度 | 0.504 |
| Listing样本数(TOP100) / 商品总数 | 1250.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.1178 |
| Listing样本数(TOP100) / 平均体积(in³) | 782.9602 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.71 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 69.0% |
| 头部Listing数(TOP10) / 月均销量 | 1307.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 21305.0 |
| 头部Listing数(TOP10) / 平均BSR | 5822.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 237.0 |
| 新品(半年内上架) / 月均销售额($) | 4886.0 |
| 新品(半年内上架) / 平均价格($) | 18.28 |
| 新品(半年内上架) / 平均评分数 | 25.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.050293002 |
| 所有Listing(半年内) / 同类目退货率 | 0.037488 |
| 所有Listing(半年内) / 搜索购买比 | 7.59038 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10263 |

### Raincoats (雨衣)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Raincoats |
| Listing样本数(TOP100) / 细分市场(翻译) | 雨衣 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Dogs:Apparel & Accessories:Raincoats |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 32189.0 |
| Listing样本数(TOP100) / 月均销量 | 321.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7989.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.83 |
| Listing样本数(TOP100) / 平均评分数 | 842.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 50912.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 96%  <br> AMZ: 3%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.554 |
| Listing样本数(TOP100) / 品牌集中度 | 0.611 |
| Listing样本数(TOP100) / 卖家集中度 | 0.593 |
| Listing样本数(TOP100) / 商品总数 | 479.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8495 |
| Listing样本数(TOP100) / 平均体积(in³) | 107.8662 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 1783.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 44198.0 |
| 头部Listing数(TOP10) / 平均BSR | 10551.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 102.0 |
| 新品(半年内上架) / 月均销售额($) | 1908.0 |
| 新品(半年内上架) / 平均价格($) | 17.44 |
| 新品(半年内上架) / 平均评分数 | 22.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.213681 |
| 所有Listing(半年内) / 同类目退货率 | 0.166577 |
| 所有Listing(半年内) / 搜索购买比 | 8.816 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06894 |

### Drill Bits (钻头)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Drill Bits |
| Listing样本数(TOP100) / 细分市场(翻译) | 钻头 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Power & Hand Tools:Power Tool Parts & Accessories:Power Drill Parts & Accessories:Drill Bits |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 31378.0 |
| Listing样本数(TOP100) / 月均销量 | 313.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6380.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.43 |
| Listing样本数(TOP100) / 平均评分数 | 264.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 43177.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 9%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.48 |
| Listing样本数(TOP100) / 品牌集中度 | 0.529 |
| Listing样本数(TOP100) / 卖家集中度 | 0.546 |
| Listing样本数(TOP100) / 商品总数 | 12681.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.9811 |
| Listing样本数(TOP100) / 平均体积(in³) | 60.7192 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 74.0% |
| 头部Listing数(TOP10) / 月均销量 | 1504.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 20311.0 |
| 头部Listing数(TOP10) / 平均BSR | 8252.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 203.0 |
| 新品(半年内上架) / 月均销售额($) | 5687.0 |
| 新品(半年内上架) / 平均价格($) | 25.74 |
| 新品(半年内上架) / 平均评分数 | 45.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.026814 |
| 所有Listing(半年内) / 同类目退货率 | 0.028178 |
| 所有Listing(半年内) / 搜索购买比 | 12.41791 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12810001 |

### Battery Chargers (电池充电器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Battery Chargers |
| Listing样本数(TOP100) / 细分市场(翻译) | 电池充电器 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Remote & App Controlled Vehicles & Parts:Remote & App Controlled Vehicle Parts:Battery Chargers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：62 <br> 卖家：63 |
| Listing样本数(TOP100) / 月总销量 | 31004.0 |
| Listing样本数(TOP100) / 月均销量 | 310.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8070.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.92 |
| Listing样本数(TOP100) / 平均评分数 | 379.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 43828.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 5%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.257 |
| Listing样本数(TOP100) / 品牌集中度 | 0.449 |
| Listing样本数(TOP100) / 卖家集中度 | 0.454 |
| Listing样本数(TOP100) / 商品总数 | 1891.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5027 |
| Listing样本数(TOP100) / 平均体积(in³) | 33.0419 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.59 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 74.0% |
| 头部Listing数(TOP10) / 月均销量 | 796.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 11978.0 |
| 头部Listing数(TOP10) / 平均BSR | 12349.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 232.0 |
| 新品(半年内上架) / 月均销售额($) | 5357.0 |
| 新品(半年内上架) / 平均价格($) | 24.74 |
| 新品(半年内上架) / 平均评分数 | 20.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.069878995 |
| 所有Listing(半年内) / 同类目退货率 | 0.064268 |
| 所有Listing(半年内) / 搜索购买比 | 8.51874 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10186 |

### Jerseys (球衣)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Jerseys |
| Listing样本数(TOP100) / 细分市场(翻译) | 球衣 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Sport Specific Clothing:Soccer & Futsal:Men:Jerseys |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：47 <br> 卖家：53 |
| Listing样本数(TOP100) / 月总销量 | 30954.0 |
| Listing样本数(TOP100) / 月均销量 | 309.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10745.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.1 |
| Listing样本数(TOP100) / 平均评分数 | 130.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 197210.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 40%  <br> AMZ: 9%  <br> FBM: 37% |
| Listing样本数(TOP100) / 商品集中度 | 0.44 |
| Listing样本数(TOP100) / 品牌集中度 | 0.63 |
| Listing样本数(TOP100) / 卖家集中度 | 0.633 |
| Listing样本数(TOP100) / 商品总数 | 1436.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.519 |
| Listing样本数(TOP100) / 平均体积(in³) | 204.5082 |
| Listing样本数(TOP100) / 平均毛利率 | 0.66 |
| Listing样本数(TOP100) / A+占比 | 0.45 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 48.0% |
| 头部Listing数(TOP10) / 月均销量 | 1360.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 44069.0 |
| 头部Listing数(TOP10) / 平均BSR | 45357.0 |
| 新品(半年内上架) / 新品数量 | 29.0 |
| 新品(半年内上架) / 新品占比 | 0.29 |
| 新品(半年内上架) / 月均销量 | 341.0 |
| 新品(半年内上架) / 月均销售额($) | 11972.0 |
| 新品(半年内上架) / 平均价格($) | 47.92 |
| 新品(半年内上架) / 平均评分数 | 17.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.072272 |
| 所有Listing(半年内) / 同类目退货率 | 0.140002 |
| 所有Listing(半年内) / 搜索购买比 | 1.97889 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.058819998 |

### Cookbook Stands (菜谱架)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Cookbook Stands |
| Listing样本数(TOP100) / 细分市场(翻译) | 菜谱架 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Kitchen Utensils & Gadgets:Kitchen Accessories:Cookbook Stands & Recipe Holders:Cookbook Stands |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：85 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 30565.0 |
| Listing样本数(TOP100) / 月均销量 | 305.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5395.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.65 |
| Listing样本数(TOP100) / 平均评分数 | 712.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 70218.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 6%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.474 |
| Listing样本数(TOP100) / 品牌集中度 | 0.547 |
| Listing样本数(TOP100) / 卖家集中度 | 0.55 |
| Listing样本数(TOP100) / 商品总数 | 404.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.871 |
| Listing样本数(TOP100) / 平均体积(in³) | 451.7014 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.85 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 1450.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 17199.0 |
| 头部Listing数(TOP10) / 平均BSR | 10174.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 176.0 |
| 新品(半年内上架) / 月均销售额($) | 3244.0 |
| 新品(半年内上架) / 平均价格($) | 19.86 |
| 新品(半年内上架) / 平均评分数 | 20.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.061661 |
| 所有Listing(半年内) / 同类目退货率 | 0.052835997 |
| 所有Listing(半年内) / 搜索购买比 | 7.01673 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092939995 |

### Countersink Drill Bits (沉孔钻头)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Countersink Drill Bits |
| Listing样本数(TOP100) / 细分市场(翻译) | 沉孔钻头 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Power & Hand Tools:Power Tool Parts & Accessories:Power Drill Parts & Accessories:Drill Bits:Countersink Drill Bits |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：70 |
| Listing样本数(TOP100) / 月总销量 | 30325.0 |
| Listing样本数(TOP100) / 月均销量 | 303.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6043.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.48 |
| Listing样本数(TOP100) / 平均评分数 | 588.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 63995.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 6%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.377 |
| Listing样本数(TOP100) / 品牌集中度 | 0.538 |
| Listing样本数(TOP100) / 卖家集中度 | 0.535 |
| Listing样本数(TOP100) / 商品总数 | 1185.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4876 |
| Listing样本数(TOP100) / 平均体积(in³) | 31.7012 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 1143.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 19668.0 |
| 头部Listing数(TOP10) / 平均BSR | 11751.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 238.0 |
| 新品(半年内上架) / 月均销售额($) | 5475.0 |
| 新品(半年内上架) / 平均价格($) | 22.32 |
| 新品(半年内上架) / 平均评分数 | 50.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.018471 |
| 所有Listing(半年内) / 同类目退货率 | 0.028178 |
| 所有Listing(半年内) / 搜索购买比 | 10.46125 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12810001 |

### Trench Coats (风雨衣)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Trench Coats |
| Listing样本数(TOP100) / 细分市场(翻译) | 风雨衣 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Coats, Jackets & Vests:Trench, Rain & Anoraks:Trench Coats |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：57 |
| Listing样本数(TOP100) / 月总销量 | 30117.0 |
| Listing样本数(TOP100) / 月均销量 | 301.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16220.0 |
| Listing样本数(TOP100) / 平均价格($) | 54.77 |
| Listing样本数(TOP100) / 平均评分数 | 624.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 281584.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 7%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.424 |
| Listing样本数(TOP100) / 品牌集中度 | 0.617 |
| Listing样本数(TOP100) / 卖家集中度 | 0.612 |
| Listing样本数(TOP100) / 商品总数 | 750.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.281 |
| Listing样本数(TOP100) / 平均体积(in³) | 238.4692 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.93 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 1276.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 62721.0 |
| 头部Listing数(TOP10) / 平均BSR | 70344.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 203.0 |
| 新品(半年内上架) / 月均销售额($) | 12887.0 |
| 新品(半年内上架) / 平均价格($) | 56.86 |
| 新品(半年内上架) / 平均评分数 | 36.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.344029 |
| 所有Listing(半年内) / 同类目退货率 | 0.244967 |
| 所有Listing(半年内) / 搜索购买比 | 3.80846 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04205 |

### Home Décor Products (家居装饰)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Home Décor Products |
| Listing样本数(TOP100) / 细分市场(翻译) | 家居装饰 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：89 <br> 卖家：88 |
| Listing样本数(TOP100) / 月总销量 | 29977.0 |
| Listing样本数(TOP100) / 月均销量 | 299.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5117.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.56 |
| Listing样本数(TOP100) / 平均评分数 | 406.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 242209.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 4%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.463 |
| Listing样本数(TOP100) / 品牌集中度 | 0.501 |
| Listing样本数(TOP100) / 卖家集中度 | 0.516 |
| Listing样本数(TOP100) / 商品总数 | 66564.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.925 |
| Listing样本数(TOP100) / 平均体积(in³) | 396.8471 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.72 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 74.0% |
| 头部Listing数(TOP10) / 月均销量 | 1389.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 17928.0 |
| 头部Listing数(TOP10) / 平均BSR | 47119.0 |
| 新品(半年内上架) / 新品数量 | 20.0 |
| 新品(半年内上架) / 新品占比 | 0.2 |
| 新品(半年内上架) / 月均销量 | 263.0 |
| 新品(半年内上架) / 月均销售额($) | 5166.0 |
| 新品(半年内上架) / 平均价格($) | 20.16 |
| 新品(半年内上架) / 平均评分数 | 35.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.121415004 |
| 所有Listing(半年内) / 同类目退货率 | 0.065816 |
| 所有Listing(半年内) / 搜索购买比 | 7.252 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0717 |

### Sweatpants (Sweatpants)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Sweatpants |
| Listing样本数(TOP100) / 细分市场(翻译) | Sweatpants |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing:Active:Active Pants:Sweatpants |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：49 <br> 卖家：46 |
| Listing样本数(TOP100) / 月总销量 | 29766.0 |
| Listing样本数(TOP100) / 月均销量 | 297.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7954.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.22 |
| Listing样本数(TOP100) / 平均评分数 | 337.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 206798.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 8%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.267 |
| Listing样本数(TOP100) / 品牌集中度 | 0.538 |
| Listing样本数(TOP100) / 卖家集中度 | 0.57 |
| Listing样本数(TOP100) / 商品总数 | 833.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0401 |
| Listing样本数(TOP100) / 平均体积(in³) | 214.6107 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.76 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 794.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 17340.0 |
| 头部Listing数(TOP10) / 平均BSR | 187447.0 |
| 新品(半年内上架) / 新品数量 | 29.0 |
| 新品(半年内上架) / 新品占比 | 0.29 |
| 新品(半年内上架) / 月均销量 | 308.0 |
| 新品(半年内上架) / 月均销售额($) | 8756.0 |
| 新品(半年内上架) / 平均价格($) | 28.46 |
| 新品(半年内上架) / 平均评分数 | 28.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.178071 |
| 所有Listing(半年内) / 同类目退货率 | 0.21090001 |
| 所有Listing(半年内) / 搜索购买比 | 3.76654 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07519 |

### Tie-Downs (栓系器具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tie-Downs |
| Listing样本数(TOP100) / 细分市场(翻译) | 栓系器具 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Boating & Sailing:Boating:Boat Trailer Accessories:Tie-Downs |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：62 |
| Listing样本数(TOP100) / 月总销量 | 29685.0 |
| Listing样本数(TOP100) / 月均销量 | 296.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8356.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.48 |
| Listing样本数(TOP100) / 平均评分数 | 548.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 78914.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 10%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.443 |
| Listing样本数(TOP100) / 品牌集中度 | 0.591 |
| Listing样本数(TOP100) / 卖家集中度 | 0.573 |
| Listing样本数(TOP100) / 商品总数 | 310.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.6008 |
| Listing样本数(TOP100) / 平均体积(in³) | 56.5989 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.68 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 51.0% |
| 头部Listing数(TOP10) / 月均销量 | 1316.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 38876.0 |
| 头部Listing数(TOP10) / 平均BSR | 8231.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 294.0 |
| 新品(半年内上架) / 月均销售额($) | 9735.0 |
| 新品(半年内上架) / 平均价格($) | 31.15 |
| 新品(半年内上架) / 平均评分数 | 131.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.037388 |
| 所有Listing(半年内) / 同类目退货率 | 0.049112 |
| 所有Listing(半年内) / 搜索购买比 | 10.47648 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09599 |

### Protective Gear (防护装备)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Protective Gear |
| Listing样本数(TOP100) / 细分市场(翻译) | 防护装备 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Farm & Ranch:Beekeeping Supplies:Protective Gear |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：55 <br> 卖家：57 |
| Listing样本数(TOP100) / 月总销量 | 29432.0 |
| Listing样本数(TOP100) / 月均销量 | 294.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12794.0 |
| Listing样本数(TOP100) / 平均价格($) | 41.94 |
| Listing样本数(TOP100) / 平均评分数 | 277.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 64274.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 1%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.381 |
| Listing样本数(TOP100) / 品牌集中度 | 0.602 |
| Listing样本数(TOP100) / 卖家集中度 | 0.593 |
| Listing样本数(TOP100) / 商品总数 | 913.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6728 |
| Listing样本数(TOP100) / 平均体积(in³) | 456.3728 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.74 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 61.0% |
| 头部Listing数(TOP10) / 月均销量 | 1121.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 55300.0 |
| 头部Listing数(TOP10) / 平均BSR | 16752.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 214.0 |
| 新品(半年内上架) / 月均销售额($) | 7550.0 |
| 新品(半年内上架) / 平均价格($) | 39.3 |
| 新品(半年内上架) / 平均评分数 | 34.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.039453 |
| 所有Listing(半年内) / 同类目退货率 | 0.038427 |
| 所有Listing(半年内) / 搜索购买比 | 9.67869 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10492 |

### Exterior Lighting (外部照明)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Exterior Lighting |
| Listing样本数(TOP100) / 细分市场(翻译) | 外部照明 |
| Listing样本数(TOP100) / 市场路径 | Automotive:RV Parts & Accessories:Power & Electrical:Lighting:Exterior Lighting |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：64 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 28905.0 |
| Listing样本数(TOP100) / 月均销量 | 289.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6176.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.81 |
| Listing样本数(TOP100) / 平均评分数 | 523.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 83361.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 10%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.386 |
| Listing样本数(TOP100) / 品牌集中度 | 0.525 |
| Listing样本数(TOP100) / 卖家集中度 | 0.555 |
| Listing样本数(TOP100) / 商品总数 | 663.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7703 |
| Listing样本数(TOP100) / 平均体积(in³) | 137.5774 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 67.0% |
| 头部Listing数(TOP10) / 月均销量 | 1115.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 19358.0 |
| 头部Listing数(TOP10) / 平均BSR | 7419.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 187.0 |
| 新品(半年内上架) / 月均销售额($) | 5971.0 |
| 新品(半年内上架) / 平均价格($) | 32.08 |
| 新品(半年内上架) / 平均评分数 | 663.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.046566 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 6.89688 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Deburring Cutters (去毛刺刀具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Deburring Cutters |
| Listing样本数(TOP100) / 细分市场(翻译) | 去毛刺刀具 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Cutting Tools:Deburring Cutters |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 28786.0 |
| Listing样本数(TOP100) / 月均销量 | 287.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4577.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.36 |
| Listing样本数(TOP100) / 平均评分数 | 370.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 43574.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 2%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.558 |
| Listing样本数(TOP100) / 品牌集中度 | 0.634 |
| Listing样本数(TOP100) / 卖家集中度 | 0.634 |
| Listing样本数(TOP100) / 商品总数 | 837.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.4687 |
| Listing样本数(TOP100) / 平均体积(in³) | 38.8996 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.74 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 59.0% |
| 头部Listing数(TOP10) / 月均销量 | 1607.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 15558.0 |
| 头部Listing数(TOP10) / 平均BSR | 6943.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 151.0 |
| 新品(半年内上架) / 月均销售额($) | 2467.0 |
| 新品(半年内上架) / 平均价格($) | 19.31 |
| 新品(半年内上架) / 平均评分数 | 22.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.019297 |
| 所有Listing(半年内) / 同类目退货率 | 0.032465998 |
| 所有Listing(半年内) / 搜索购买比 | 14.22869 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12100001 |

### Bag Sealers (封袋机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bag Sealers |
| Listing样本数(TOP100) / 细分市场(翻译) | 封袋机 |
| Listing样本数(TOP100) / 市场路径 | Restaurant Appliances & Equipment:Commercial Food Preparation Equipment:Commercial Food Packaging Equipment:Bag Sealers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 28305.0 |
| Listing样本数(TOP100) / 月均销量 | 283.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6470.0 |
| Listing样本数(TOP100) / 平均价格($) | 41.2 |
| Listing样本数(TOP100) / 平均评分数 | 469.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 71338.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 3%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.576 |
| Listing样本数(TOP100) / 品牌集中度 | 0.616 |
| Listing样本数(TOP100) / 卖家集中度 | 0.616 |
| Listing样本数(TOP100) / 商品总数 | 686.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.561 |
| Listing样本数(TOP100) / 平均体积(in³) | 385.0659 |
| Listing样本数(TOP100) / 平均毛利率 | 0.71 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 78.0% |
| 头部Listing数(TOP10) / 月均销量 | 1630.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 30377.0 |
| 头部Listing数(TOP10) / 平均BSR | 5637.0 |
| 新品(半年内上架) / 新品数量 | 24.0 |
| 新品(半年内上架) / 新品占比 | 0.24 |
| 新品(半年内上架) / 月均销量 | 172.0 |
| 新品(半年内上架) / 月均销售额($) | 3898.0 |
| 新品(半年内上架) / 平均价格($) | 49.96 |
| 新品(半年内上架) / 平均评分数 | 57.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.060935 |
| 所有Listing(半年内) / 同类目退货率 | 0.049214 |
| 所有Listing(半年内) / 搜索购买比 | 14.25708 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.105129994 |

### Hearing Amplifiers (助听扩音器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hearing Amplifiers |
| Listing样本数(TOP100) / 细分市场(翻译) | 助听扩音器 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Medical Supplies & Equipment:Mobility & Daily Living Aids:Hearing Aids, Amplifiers & Accessories:Hearing Amplifiers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：59 <br> 卖家：60 |
| Listing样本数(TOP100) / 月总销量 | 28221.0 |
| Listing样本数(TOP100) / 月均销量 | 282.0 |
| Listing样本数(TOP100) / 月均销售额($) | 39516.0 |
| Listing样本数(TOP100) / 平均价格($) | 121.96 |
| Listing样本数(TOP100) / 平均评分数 | 567.0 |
| Listing样本数(TOP100) / 平均星级 | 3.9 |
| Listing样本数(TOP100) / 平均BSR | 121727.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 79%  <br> AMZ: 7%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.309 |
| Listing样本数(TOP100) / 品牌集中度 | 0.498 |
| Listing样本数(TOP100) / 卖家集中度 | 0.474 |
| Listing样本数(TOP100) / 商品总数 | 840.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.1472 |
| Listing样本数(TOP100) / 平均体积(in³) | 47.1207 |
| Listing样本数(TOP100) / 平均毛利率 | 0.76 |
| Listing样本数(TOP100) / A+占比 | 0.84 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 52.0% |
| 头部Listing数(TOP10) / 月均销量 | 872.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 181898.0 |
| 头部Listing数(TOP10) / 平均BSR | 34407.0 |
| 新品(半年内上架) / 新品数量 | 36.0 |
| 新品(半年内上架) / 新品占比 | 0.36 |
| 新品(半年内上架) / 月均销量 | 295.0 |
| 新品(半年内上架) / 月均销售额($) | 41566.0 |
| 新品(半年内上架) / 平均价格($) | 123.22 |
| 新品(半年内上架) / 平均评分数 | 59.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.21188 |
| 所有Listing(半年内) / 同类目退货率 | 0.21188 |
| 所有Listing(半年内) / 搜索购买比 | 4.8272 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.048270002 |

### Tops (Tops)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tops |
| Listing样本数(TOP100) / 细分市场(翻译) | Tops |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Sport Specific Clothing:Dance:Women:Tops |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：75 |
| Listing样本数(TOP100) / 月总销量 | 28102.0 |
| Listing样本数(TOP100) / 月均销量 | 281.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5848.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.08 |
| Listing样本数(TOP100) / 平均评分数 | 183.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 374749.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 4%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.562 |
| Listing样本数(TOP100) / 品牌集中度 | 0.642 |
| Listing样本数(TOP100) / 卖家集中度 | 0.634 |
| Listing样本数(TOP100) / 商品总数 | 883.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3309 |
| Listing样本数(TOP100) / 平均体积(in³) | 91.3184 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.71 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 1579.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 31892.0 |
| 头部Listing数(TOP10) / 平均BSR | 45043.0 |
| 新品(半年内上架) / 新品数量 | 24.0 |
| 新品(半年内上架) / 新品占比 | 0.24 |
| 新品(半年内上架) / 月均销量 | 229.0 |
| 新品(半年内上架) / 月均销售额($) | 4091.0 |
| 新品(半年内上架) / 平均价格($) | 18.13 |
| 新品(半年内上架) / 平均评分数 | 12.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.206045 |
| 所有Listing(半年内) / 同类目退货率 | 0.140002 |
| 所有Listing(半年内) / 搜索购买比 | 4.80622 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.058819998 |

### Flower Pressing (压花)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Flower Pressing |
| Listing样本数(TOP100) / 细分市场(翻译) | 压花 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Arts & Crafts:Craft Kits:Flower Pressing |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：79 <br> 卖家：84 |
| Listing样本数(TOP100) / 月总销量 | 27001.0 |
| Listing样本数(TOP100) / 月均销量 | 270.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6515.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.48 |
| Listing样本数(TOP100) / 平均评分数 | 175.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 94092.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 1%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.523 |
| Listing样本数(TOP100) / 品牌集中度 | 0.599 |
| Listing样本数(TOP100) / 卖家集中度 | 0.599 |
| Listing样本数(TOP100) / 商品总数 | 156.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.6926 |
| Listing样本数(TOP100) / 平均体积(in³) | 153.9598 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.87 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 1412.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 37675.0 |
| 头部Listing数(TOP10) / 平均BSR | 12634.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 109.0 |
| 新品(半年内上架) / 月均销售额($) | 1877.0 |
| 新品(半年内上架) / 平均价格($) | 19.59 |
| 新品(半年内上架) / 平均评分数 | 14.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.028703999 |
| 所有Listing(半年内) / 同类目退货率 | 0.026326 |
| 所有Listing(半年内) / 搜索购买比 | 8.59741 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07379 |

### Bar Tools & Drinkware (酒吧工具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bar Tools & Drinkware |
| Listing样本数(TOP100) / 细分市场(翻译) | 酒吧工具 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Dining & Entertaining:Bar Tools & Drinkware |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：93 <br> 卖家：90 |
| Listing样本数(TOP100) / 月总销量 | 26803.0 |
| Listing样本数(TOP100) / 月均销量 | 268.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6642.0 |
| Listing样本数(TOP100) / 平均价格($) | 25.94 |
| Listing样本数(TOP100) / 平均评分数 | 365.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 63733.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 4%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.51 |
| Listing样本数(TOP100) / 品牌集中度 | 0.534 |
| Listing样本数(TOP100) / 卖家集中度 | 0.548 |
| Listing样本数(TOP100) / 商品总数 | 51814.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.2702 |
| Listing样本数(TOP100) / 平均体积(in³) | 310.3259 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.74 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 61.0% |
| 头部Listing数(TOP10) / 月均销量 | 1366.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 36348.0 |
| 头部Listing数(TOP10) / 平均BSR | 17315.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 121.0 |
| 新品(半年内上架) / 月均销售额($) | 2979.0 |
| 新品(半年内上架) / 平均价格($) | 20.95 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.054355998 |
| 所有Listing(半年内) / 同类目退货率 | 0.052106 |
| 所有Listing(半年内) / 搜索购买比 | 6.62142 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10187 |

### Wood Burning Tools (木材燃烧工具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Wood Burning Tools |
| Listing样本数(TOP100) / 细分市场(翻译) | 木材燃烧工具 |
| Listing样本数(TOP100) / 市场路径 | Arts, Crafts & Sewing:Crafting:Woodcrafts:Wood Burning Tools |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：61 <br> 卖家：62 |
| Listing样本数(TOP100) / 月总销量 | 26503.0 |
| Listing样本数(TOP100) / 月均销量 | 265.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6574.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.55 |
| Listing样本数(TOP100) / 平均评分数 | 567.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 42309.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 75%  <br> AMZ: 1%  <br> FBM: 20% |
| Listing样本数(TOP100) / 商品集中度 | 0.406 |
| Listing样本数(TOP100) / 品牌集中度 | 0.54 |
| Listing样本数(TOP100) / 卖家集中度 | 0.538 |
| Listing样本数(TOP100) / 商品总数 | 648.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.072 |
| Listing样本数(TOP100) / 平均体积(in³) | 73.3475 |
| Listing样本数(TOP100) / 平均毛利率 | 0.66 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 1076.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 21566.0 |
| 头部Listing数(TOP10) / 平均BSR | 8376.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 290.0 |
| 新品(半年内上架) / 月均销售额($) | 4996.0 |
| 新品(半年内上架) / 平均价格($) | 27.65 |
| 新品(半年内上架) / 平均评分数 | 81.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.039968 |
| 所有Listing(半年内) / 同类目退货率 | 0.037488 |
| 所有Listing(半年内) / 搜索购买比 | 5.54442 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10263 |

### Tea Storage Chests (茶叶罐)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tea Storage Chests |
| Listing样本数(TOP100) / 细分市场(翻译) | 茶叶罐 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Coffee, Tea & Espresso:Tea Accessories:Tea Storage Chests |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：83 <br> 卖家：83 |
| Listing样本数(TOP100) / 月总销量 | 26400.0 |
| Listing样本数(TOP100) / 月均销量 | 264.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5800.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.4 |
| Listing样本数(TOP100) / 平均评分数 | 657.0 |
| Listing样本数(TOP100) / 平均星级 | 4.6 |
| Listing样本数(TOP100) / 平均BSR | 242968.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 95%  <br> AMZ: 3%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.397 |
| Listing样本数(TOP100) / 品牌集中度 | 0.458 |
| Listing样本数(TOP100) / 卖家集中度 | 0.48 |
| Listing样本数(TOP100) / 商品总数 | 663.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4397 |
| Listing样本数(TOP100) / 平均体积(in³) | 377.3232 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 71.0% |
| 头部Listing数(TOP10) / 月均销量 | 1049.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 19502.0 |
| 头部Listing数(TOP10) / 平均BSR | 45584.0 |
| 新品(半年内上架) / 新品数量 | 16.0 |
| 新品(半年内上架) / 新品占比 | 0.16 |
| 新品(半年内上架) / 月均销量 | 194.0 |
| 新品(半年内上架) / 月均销售额($) | 4188.0 |
| 新品(半年内上架) / 平均价格($) | 22.66 |
| 新品(半年内上架) / 平均评分数 | 50.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.065422 |
| 所有Listing(半年内) / 同类目退货率 | 0.035095 |
| 所有Listing(半年内) / 搜索购买比 | 6.37846 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10854 |

### Floor Molding & Trim (地板压条和镶边)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Floor Molding & Trim |
| Listing样本数(TOP100) / 细分市场(翻译) | 地板压条和镶边 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Building Supplies:Building Materials:Millwork:Moldings & Trims:Floor Molding & Trim |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：60 <br> 卖家：64 |
| Listing样本数(TOP100) / 月总销量 | 24530.0 |
| Listing样本数(TOP100) / 月均销量 | 245.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5348.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.66 |
| Listing样本数(TOP100) / 平均评分数 | 389.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 102015.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 78%  <br> AMZ: 2%  <br> FBM: 9% |
| Listing样本数(TOP100) / 商品集中度 | 0.427 |
| Listing样本数(TOP100) / 品牌集中度 | 0.549 |
| Listing样本数(TOP100) / 卖家集中度 | 0.543 |
| Listing样本数(TOP100) / 商品总数 | 621.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6133 |
| Listing样本数(TOP100) / 平均体积(in³) | 125.3806 |
| Listing样本数(TOP100) / 平均毛利率 | 0.52 |
| Listing样本数(TOP100) / A+占比 | 0.82 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 61.0% |
| 头部Listing数(TOP10) / 月均销量 | 1046.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 19468.0 |
| 头部Listing数(TOP10) / 平均BSR | 13898.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 136.0 |
| 新品(半年内上架) / 月均销售额($) | 2757.0 |
| 新品(半年内上架) / 平均价格($) | 23.31 |
| 新品(半年内上架) / 平均评分数 | 48.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.108365 |
| 所有Listing(半年内) / 同类目退货率 | 0.12484 |
| 所有Listing(半年内) / 搜索购买比 | 6.79561 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.056750003 |

### Sound Therapy (声音疗法)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Sound Therapy |
| Listing样本数(TOP100) / 细分市场(翻译) | 声音疗法 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Health Care:Alternative Medicine:Sound Therapy |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：81 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 24359.0 |
| Listing样本数(TOP100) / 月均销量 | 243.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12392.0 |
| Listing样本数(TOP100) / 平均价格($) | 54.87 |
| Listing样本数(TOP100) / 平均评分数 | 254.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 118716.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 3%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.391 |
| Listing样本数(TOP100) / 品牌集中度 | 0.454 |
| Listing样本数(TOP100) / 卖家集中度 | 0.46 |
| Listing样本数(TOP100) / 商品总数 | 551.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.9551 |
| Listing样本数(TOP100) / 平均体积(in³) | 85.1531 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.87 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 75.0% |
| 头部Listing数(TOP10) / 月均销量 | 953.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 38375.0 |
| 头部Listing数(TOP10) / 平均BSR | 46155.0 |
| 新品(半年内上架) / 新品数量 | 33.0 |
| 新品(半年内上架) / 新品占比 | 0.33 |
| 新品(半年内上架) / 月均销量 | 199.0 |
| 新品(半年内上架) / 月均销售额($) | 6953.0 |
| 新品(半年内上架) / 平均价格($) | 32.11 |
| 新品(半年内上架) / 平均评分数 | 32.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.063163 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 10.13834 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Pond Lights (池塘灯)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Pond Lights |
| Listing样本数(TOP100) / 细分市场(翻译) | 池塘灯 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Outdoor Décor:Water Gardens & Ponds:Pond Lights |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 24128.0 |
| Listing样本数(TOP100) / 月均销量 | 241.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7740.0 |
| Listing样本数(TOP100) / 平均价格($) | 46.35 |
| Listing样本数(TOP100) / 平均评分数 | 235.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 87206.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 5%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.429 |
| Listing样本数(TOP100) / 品牌集中度 | 0.646 |
| Listing样本数(TOP100) / 卖家集中度 | 0.613 |
| Listing样本数(TOP100) / 商品总数 | 439.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5263 |
| Listing样本数(TOP100) / 平均体积(in³) | 198.1374 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.72 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 1034.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 21138.0 |
| 头部Listing数(TOP10) / 平均BSR | 15162.0 |
| 新品(半年内上架) / 新品数量 | 19.0 |
| 新品(半年内上架) / 新品占比 | 0.19 |
| 新品(半年内上架) / 月均销量 | 202.0 |
| 新品(半年内上架) / 月均销售额($) | 9446.0 |
| 新品(半年内上架) / 平均价格($) | 50.99 |
| 新品(半年内上架) / 平均评分数 | 115.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.06151 |
| 所有Listing(半年内) / 同类目退货率 | 0.078448 |
| 所有Listing(半年内) / 搜索购买比 | 6.08684 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05737 |

### Workout Top & Bottom Sets (服装套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Workout Top & Bottom Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 服装套装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Men:Clothing:Active:Sets:Workout Top & Bottom Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 23985.0 |
| Listing样本数(TOP100) / 月均销量 | 239.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7757.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.51 |
| Listing样本数(TOP100) / 平均评分数 | 243.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 359837.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 1%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.371 |
| Listing样本数(TOP100) / 品牌集中度 | 0.576 |
| Listing样本数(TOP100) / 卖家集中度 | 0.568 |
| Listing样本数(TOP100) / 商品总数 | 1046.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0849 |
| Listing样本数(TOP100) / 平均体积(in³) | 289.9098 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.89 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 91.0% |
| 头部Listing数(TOP10) / 月均销量 | 888.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 30573.0 |
| 头部Listing数(TOP10) / 平均BSR | 56557.0 |
| 新品(半年内上架) / 新品数量 | 24.0 |
| 新品(半年内上架) / 新品占比 | 0.24 |
| 新品(半年内上架) / 月均销量 | 335.0 |
| 新品(半年内上架) / 月均销售额($) | 10731.0 |
| 新品(半年内上架) / 平均价格($) | 30.13 |
| 新品(半年内上架) / 平均评分数 | 33.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.100486 |
| 所有Listing(半年内) / 同类目退货率 | 0.123008005 |
| 所有Listing(半年内) / 搜索购买比 | 5.22788 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06877 |

### Paint Roller Extension Poles (油漆滚筒加长杆)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Paint Roller Extension Poles |
| Listing样本数(TOP100) / 细分市场(翻译) | 油漆滚筒加长杆 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Paint, Wall Treatments & Supplies:Painting Supplies & Tools:Paint Application Tools:Paint Roller Extension Poles |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：82 <br> 卖家：85 |
| Listing样本数(TOP100) / 月总销量 | 23766.0 |
| Listing样本数(TOP100) / 月均销量 | 237.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9260.0 |
| Listing样本数(TOP100) / 平均价格($) | 36.17 |
| Listing样本数(TOP100) / 平均评分数 | 354.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 120895.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 5%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.524 |
| Listing样本数(TOP100) / 品牌集中度 | 0.561 |
| Listing样本数(TOP100) / 卖家集中度 | 0.594 |
| Listing样本数(TOP100) / 商品总数 | 393.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.0025 |
| Listing样本数(TOP100) / 平均体积(in³) | 173.6479 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.73 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 1245.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 50620.0 |
| 头部Listing数(TOP10) / 平均BSR | 14185.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 103.0 |
| 新品(半年内上架) / 月均销售额($) | 6193.0 |
| 新品(半年内上架) / 平均价格($) | 54.9 |
| 新品(半年内上架) / 平均评分数 | 18.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.045532 |
| 所有Listing(半年内) / 同类目退货率 | 0.064237 |
| 所有Listing(半年内) / 搜索购买比 | 9.36944 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10077 |

### Guitars & Strings (吉他)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Guitars & Strings |
| Listing样本数(TOP100) / 细分市场(翻译) | 吉他 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Learning & Education:Musical Instruments:Guitars & Strings |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：77 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 23669.0 |
| Listing样本数(TOP100) / 月均销量 | 236.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5589.0 |
| Listing样本数(TOP100) / 平均价格($) | 29.38 |
| Listing样本数(TOP100) / 平均评分数 | 625.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 92572.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 78%  <br> AMZ: 3%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.545 |
| Listing样本数(TOP100) / 品牌集中度 | 0.584 |
| Listing样本数(TOP100) / 卖家集中度 | 0.625 |
| Listing样本数(TOP100) / 商品总数 | 212.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3004 |
| Listing样本数(TOP100) / 平均体积(in³) | 458.2987 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 67.0% |
| 头部Listing数(TOP10) / 月均销量 | 1289.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 21946.0 |
| 头部Listing数(TOP10) / 平均BSR | 9186.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 89.0 |
| 新品(半年内上架) / 月均销售额($) | 2841.0 |
| 新品(半年内上架) / 平均价格($) | 30.81 |
| 新品(半年内上架) / 平均评分数 | 113.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.051227003 |
| 所有Listing(半年内) / 同类目退货率 | 0.04776 |
| 所有Listing(半年内) / 搜索购买比 | 6.70833 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.058319997 |

### Pant Sets (长裤套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Pant Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 长裤套装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Boys:Clothing:Clothing Sets:Pant Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：60 <br> 卖家：51 |
| Listing样本数(TOP100) / 月总销量 | 23640.0 |
| Listing样本数(TOP100) / 月均销量 | 236.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5778.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.24 |
| Listing样本数(TOP100) / 平均评分数 | 365.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 251306.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 7%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.293 |
| Listing样本数(TOP100) / 品牌集中度 | 0.415 |
| Listing样本数(TOP100) / 卖家集中度 | 0.544 |
| Listing样本数(TOP100) / 商品总数 | 1174.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5686 |
| Listing样本数(TOP100) / 平均体积(in³) | 141.7276 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 56.0% |
| 头部Listing数(TOP10) / 月均销量 | 693.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 20066.0 |
| 头部Listing数(TOP10) / 平均BSR | 74857.0 |
| 新品(半年内上架) / 新品数量 | 22.0 |
| 新品(半年内上架) / 新品占比 | 0.22 |
| 新品(半年内上架) / 月均销量 | 223.0 |
| 新品(半年内上架) / 月均销售额($) | 4303.0 |
| 新品(半年内上架) / 平均价格($) | 17.96 |
| 新品(半年内上架) / 平均评分数 | 26.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.108081 |
| 所有Listing(半年内) / 同类目退货率 | 0.152695 |
| 所有Listing(半年内) / 搜索购买比 | 4.28689 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04593 |

### Angle Grinder Wheels (角磨机砂轮)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Angle Grinder Wheels |
| Listing样本数(TOP100) / 细分市场(翻译) | 角磨机砂轮 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Abrasive & Finishing Products:Abrasive Wheels & Discs:Angle Grinder Wheels |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：71 |
| Listing样本数(TOP100) / 月总销量 | 23383.0 |
| Listing样本数(TOP100) / 月均销量 | 233.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5444.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.63 |
| Listing样本数(TOP100) / 平均评分数 | 165.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 62962.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 52%  <br> AMZ: 12%  <br> FBM: 14% |
| Listing样本数(TOP100) / 商品集中度 | 0.493 |
| Listing样本数(TOP100) / 品牌集中度 | 0.582 |
| Listing样本数(TOP100) / 卖家集中度 | 0.603 |
| Listing样本数(TOP100) / 商品总数 | 417.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5449 |
| Listing样本数(TOP100) / 平均体积(in³) | 52.7489 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.61 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 75.0% |
| 头部Listing数(TOP10) / 月均销量 | 1152.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 28364.0 |
| 头部Listing数(TOP10) / 平均BSR | 18576.0 |
| 新品(半年内上架) / 新品数量 | 32.0 |
| 新品(半年内上架) / 新品占比 | 0.32 |
| 新品(半年内上架) / 月均销量 | 188.0 |
| 新品(半年内上架) / 月均销售额($) | 4209.0 |
| 新品(半年内上架) / 平均价格($) | 23.29 |
| 新品(半年内上架) / 平均评分数 | 28.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.024115 |
| 所有Listing(半年内) / 同类目退货率 | 0.021143 |
| 所有Listing(半年内) / 搜索购买比 | 15.38827 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.19758 |

### In-Dash Navigation (内置车载导航)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | In-Dash Navigation |
| Listing样本数(TOP100) / 细分市场(翻译) | 内置车载导航 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Car & Vehicle Electronics:Car Electronics:Car Video:In-Dash Navigation |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：52 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 23277.0 |
| Listing样本数(TOP100) / 月均销量 | 232.0 |
| Listing样本数(TOP100) / 月均销售额($) | 29003.0 |
| Listing样本数(TOP100) / 平均价格($) | 111.94 |
| Listing样本数(TOP100) / 平均评分数 | 176.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 20784.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 1%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.291 |
| Listing样本数(TOP100) / 品牌集中度 | 0.577 |
| Listing样本数(TOP100) / 卖家集中度 | 0.457 |
| Listing样本数(TOP100) / 商品总数 | 11204.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4059 |
| Listing样本数(TOP100) / 平均体积(in³) | 396.6958 |
| Listing样本数(TOP100) / 平均毛利率 | 0.83 |
| Listing样本数(TOP100) / A+占比 | 0.83 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 677.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 107550.0 |
| 头部Listing数(TOP10) / 平均BSR | 10183.0 |
| 新品(半年内上架) / 新品数量 | 25.0 |
| 新品(半年内上架) / 新品占比 | 0.25 |
| 新品(半年内上架) / 月均销量 | 230.0 |
| 新品(半年内上架) / 月均销售额($) | 17207.0 |
| 新品(半年内上架) / 平均价格($) | 81.59 |
| 新品(半年内上架) / 平均评分数 | 38.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.149223 |
| 所有Listing(半年内) / 同类目退货率 | 0.124781996 |
| 所有Listing(半年内) / 搜索购买比 | 2.28683 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.028369999 |

### Rods (杆)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Rods |
| Listing样本数(TOP100) / 细分市场(翻译) | 杆 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Welding & Soldering:Welding Equipment:Welding Equipment & Accessories:Arc Welding Equipment:Rods |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：62 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 22977.0 |
| Listing样本数(TOP100) / 月均销量 | 229.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4745.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.66 |
| Listing样本数(TOP100) / 平均评分数 | 278.0 |
| Listing样本数(TOP100) / 平均星级 | 3.7 |
| Listing样本数(TOP100) / 平均BSR | 117211.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 64%  <br> AMZ: 1%  <br> FBM: 25% |
| Listing样本数(TOP100) / 商品集中度 | 0.403 |
| Listing样本数(TOP100) / 品牌集中度 | 0.582 |
| Listing样本数(TOP100) / 卖家集中度 | 0.513 |
| Listing样本数(TOP100) / 商品总数 | 763.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.2283 |
| Listing样本数(TOP100) / 平均体积(in³) | 69.9515 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.69 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 925.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 19948.0 |
| 头部Listing数(TOP10) / 平均BSR | 39990.0 |
| 新品(半年内上架) / 新品数量 | 37.0 |
| 新品(半年内上架) / 新品占比 | 0.37 |
| 新品(半年内上架) / 月均销量 | 206.0 |
| 新品(半年内上架) / 月均销售额($) | 2975.0 |
| 新品(半年内上架) / 平均价格($) | 15.0 |
| 新品(半年内上架) / 平均评分数 | 6.0 |
| 新品(半年内上架) / 平均星级 | 2.9 |
| 所有Listing(半年内) / 退货率 | 0.019449001 |
| 所有Listing(半年内) / 同类目退货率 | 0.035314 |
| 所有Listing(半年内) / 搜索购买比 | 11.92538 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09945 |

### Airplanes & Jets (飞机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Airplanes & Jets |
| Listing样本数(TOP100) / 细分市场(翻译) | 飞机 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Remote & App Controlled Vehicles & Parts:Remote & App Controlled Vehicles:Airplanes & Jets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：52 <br> 卖家：54 |
| Listing样本数(TOP100) / 月总销量 | 22767.0 |
| Listing样本数(TOP100) / 月均销量 | 227.0 |
| Listing样本数(TOP100) / 月均销售额($) | 11252.0 |
| Listing样本数(TOP100) / 平均价格($) | 57.95 |
| Listing样本数(TOP100) / 平均评分数 | 256.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 72347.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 5%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.416 |
| Listing样本数(TOP100) / 品牌集中度 | 0.613 |
| Listing样本数(TOP100) / 卖家集中度 | 0.602 |
| Listing样本数(TOP100) / 商品总数 | 1045.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.936 |
| Listing样本数(TOP100) / 平均体积(in³) | 627.7872 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 947.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 37344.0 |
| 头部Listing数(TOP10) / 平均BSR | 34056.0 |
| 新品(半年内上架) / 新品数量 | 25.0 |
| 新品(半年内上架) / 新品占比 | 0.25 |
| 新品(半年内上架) / 月均销量 | 216.0 |
| 新品(半年内上架) / 月均销售额($) | 7210.0 |
| 新品(半年内上架) / 平均价格($) | 35.15 |
| 新品(半年内上架) / 平均评分数 | 70.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.084557 |
| 所有Listing(半年内) / 同类目退货率 | 0.041058 |
| 所有Listing(半年内) / 搜索购买比 | 2.21546 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0448 |

### Scoreboards & Timers (记分牌和计时器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Scoreboards & Timers |
| Listing样本数(TOP100) / 细分市场(翻译) | 记分牌和计时器 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports & Outdoor Recreation Accessories:Coach & Referee Gear:Scoreboards & Timers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 22707.0 |
| Listing样本数(TOP100) / 月均销量 | 227.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7566.0 |
| Listing样本数(TOP100) / 平均价格($) | 52.27 |
| Listing样本数(TOP100) / 平均评分数 | 352.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 73372.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 89%  <br> AMZ: 5%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.448 |
| Listing样本数(TOP100) / 品牌集中度 | 0.541 |
| Listing样本数(TOP100) / 卖家集中度 | 0.541 |
| Listing样本数(TOP100) / 商品总数 | 543.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5395 |
| Listing样本数(TOP100) / 平均体积(in³) | 216.1668 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.79 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 72.0% |
| 头部Listing数(TOP10) / 月均销量 | 1017.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 20580.0 |
| 头部Listing数(TOP10) / 平均BSR | 9459.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 164.0 |
| 新品(半年内上架) / 月均销售额($) | 5876.0 |
| 新品(半年内上架) / 平均价格($) | 34.78 |
| 新品(半年内上架) / 平均评分数 | 26.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.051342 |
| 所有Listing(半年内) / 同类目退货率 | 0.045063 |
| 所有Listing(半年内) / 搜索购买比 | 7.05015 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07428 |

### AV Receivers & Amplifiers (AV接收机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | AV Receivers & Amplifiers |
| Listing样本数(TOP100) / 细分市场(翻译) | AV接收机 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Television & Video:AV Receivers & Amplifiers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：65 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 22678.0 |
| Listing样本数(TOP100) / 月均销量 | 226.0 |
| Listing样本数(TOP100) / 月均销售额($) | 18561.0 |
| Listing样本数(TOP100) / 平均价格($) | 112.01 |
| Listing样本数(TOP100) / 平均评分数 | 294.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 32042.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 71%  <br> AMZ: 8%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.459 |
| Listing样本数(TOP100) / 品牌集中度 | 0.555 |
| Listing样本数(TOP100) / 卖家集中度 | 0.542 |
| Listing样本数(TOP100) / 商品总数 | 605.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.1327 |
| Listing样本数(TOP100) / 平均体积(in³) | 192.2913 |
| Listing样本数(TOP100) / 平均毛利率 | 0.82 |
| Listing样本数(TOP100) / A+占比 | 0.84 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 1041.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 57625.0 |
| 头部Listing数(TOP10) / 平均BSR | 4323.0 |
| 新品(半年内上架) / 新品数量 | 34.0 |
| 新品(半年内上架) / 新品占比 | 0.34 |
| 新品(半年内上架) / 月均销量 | 242.0 |
| 新品(半年内上架) / 月均销售额($) | 15504.0 |
| 新品(半年内上架) / 平均价格($) | 92.59 |
| 新品(半年内上架) / 平均评分数 | 32.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.128353 |
| 所有Listing(半年内) / 同类目退货率 | 0.143941 |
| 所有Listing(半年内) / 搜索购买比 | 5.62869 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.022839999 |

### Training Heads (培训负责人)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Training Heads |
| Listing样本数(TOP100) / 细分市场(翻译) | 培训负责人 |
| Listing样本数(TOP100) / 市场路径 | Beauty & Personal Care:Salon & Spa Equipment:Training Heads |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：57 <br> 卖家：59 |
| Listing样本数(TOP100) / 月总销量 | 22442.0 |
| Listing样本数(TOP100) / 月均销量 | 224.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6398.0 |
| Listing样本数(TOP100) / 平均价格($) | 28.46 |
| Listing样本数(TOP100) / 平均评分数 | 712.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 96436.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 100%  <br> AMZ: 0%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.407 |
| Listing样本数(TOP100) / 品牌集中度 | 0.542 |
| Listing样本数(TOP100) / 卖家集中度 | 0.511 |
| Listing样本数(TOP100) / 商品总数 | 191.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.8607 |
| Listing样本数(TOP100) / 平均体积(in³) | 512.0935 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 98.0% |
| 头部Listing数(TOP10) / 月均销量 | 912.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 26347.0 |
| 头部Listing数(TOP10) / 平均BSR | 27550.0 |
| 新品(半年内上架) / 新品数量 | 20.0 |
| 新品(半年内上架) / 新品占比 | 0.2 |
| 新品(半年内上架) / 月均销量 | 140.0 |
| 新品(半年内上架) / 月均销售额($) | 3690.0 |
| 新品(半年内上架) / 平均价格($) | 26.42 |
| 新品(半年内上架) / 平均评分数 | 71.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | N/A |
| 所有Listing(半年内) / 同类目退货率 | N/A |
| 所有Listing(半年内) / 搜索购买比 | N/A |
| 所有Listing(半年内) / 同类目搜索购买比 | N/A |

### Gaiters (护腿、护脚)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Gaiters |
| Listing样本数(TOP100) / 细分市场(翻译) | 护腿、护脚 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Outdoor Recreation:Camping & Hiking:Footwear & Accessories:Gaiters |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：67 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 22440.0 |
| Listing样本数(TOP100) / 月均销量 | 224.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6772.0 |
| Listing样本数(TOP100) / 平均价格($) | 33.12 |
| Listing样本数(TOP100) / 平均评分数 | 386.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 73070.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 0%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.445 |
| Listing样本数(TOP100) / 品牌集中度 | 0.561 |
| Listing样本数(TOP100) / 卖家集中度 | 0.57 |
| Listing样本数(TOP100) / 商品总数 | 422.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6839 |
| Listing样本数(TOP100) / 平均体积(in³) | 210.9182 |
| Listing样本数(TOP100) / 平均毛利率 | 0.64 |
| Listing样本数(TOP100) / A+占比 | 0.82 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 998.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 28908.0 |
| 头部Listing数(TOP10) / 平均BSR | 9704.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 159.0 |
| 新品(半年内上架) / 月均销售额($) | 4490.0 |
| 新品(半年内上架) / 平均价格($) | 31.67 |
| 新品(半年内上架) / 平均评分数 | 39.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.086393006 |
| 所有Listing(半年内) / 同类目退货率 | 0.045576 |
| 所有Listing(半年内) / 搜索购买比 | 7.24924 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08298001 |

### Wormers (虫子)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Wormers |
| Listing样本数(TOP100) / 细分市场(翻译) | 虫子 |
| Listing样本数(TOP100) / 市场路径 | Pet Supplies:Cats:Health Supplies:Wormers |
| Listing样本数(TOP100) / 样本数量 | 商品：84 <br> 品牌：49 <br> 卖家：50 |
| Listing样本数(TOP100) / 月总销量 | 22159.0 |
| Listing样本数(TOP100) / 月均销量 | 263.0 |
| Listing样本数(TOP100) / 月均销售额($) | 10689.0 |
| Listing样本数(TOP100) / 平均价格($) | 39.21 |
| Listing样本数(TOP100) / 平均评分数 | 68.0 |
| Listing样本数(TOP100) / 平均星级 | 3.9 |
| Listing样本数(TOP100) / 平均BSR | 46486.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 1%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.476 |
| Listing样本数(TOP100) / 品牌集中度 | 0.58 |
| Listing样本数(TOP100) / 卖家集中度 | 0.56 |
| Listing样本数(TOP100) / 商品总数 | 76.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2045 |
| Listing样本数(TOP100) / 平均体积(in³) | 18.7026 |
| Listing样本数(TOP100) / 平均毛利率 | 0.74 |
| Listing样本数(TOP100) / A+占比 | 0.33 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 69.0% |
| 头部Listing数(TOP10) / 月均销量 | 1055.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 41357.0 |
| 头部Listing数(TOP10) / 平均BSR | 9327.0 |
| 新品(半年内上架) / 新品数量 | 71.0 |
| 新品(半年内上架) / 新品占比 | 0.85 |
| 新品(半年内上架) / 月均销量 | 275.0 |
| 新品(半年内上架) / 月均销售额($) | 10631.0 |
| 新品(半年内上架) / 平均价格($) | 37.17 |
| 新品(半年内上架) / 平均评分数 | 12.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.012824 |
| 所有Listing(半年内) / 同类目退货率 | 0.009148 |
| 所有Listing(半年内) / 搜索购买比 | 12.86586 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.20378 |

### Cream Chargers & Whippers (奶油充电器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Cream Chargers & Whippers |
| Listing样本数(TOP100) / 细分市场(翻译) | 奶油充电器 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Kitchen Utensils & Gadgets:Specialty Tools & Gadgets:Cream Chargers & Whippers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：61 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 21944.0 |
| Listing样本数(TOP100) / 月均销量 | 219.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6757.0 |
| Listing样本数(TOP100) / 平均价格($) | 38.45 |
| Listing样本数(TOP100) / 平均评分数 | 438.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 83176.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 68%  <br> AMZ: 0%  <br> FBM: 21% |
| Listing样本数(TOP100) / 商品集中度 | 0.469 |
| Listing样本数(TOP100) / 品牌集中度 | 0.62 |
| Listing样本数(TOP100) / 卖家集中度 | 0.542 |
| Listing样本数(TOP100) / 商品总数 | 268.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4966 |
| Listing样本数(TOP100) / 平均体积(in³) | 135.6527 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.66 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 51.0% |
| 头部Listing数(TOP10) / 月均销量 | 1029.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 23820.0 |
| 头部Listing数(TOP10) / 平均BSR | 18940.0 |
| 新品(半年内上架) / 新品数量 | 38.0 |
| 新品(半年内上架) / 新品占比 | 0.38 |
| 新品(半年内上架) / 月均销量 | 250.0 |
| 新品(半年内上架) / 月均销售额($) | 5569.0 |
| 新品(半年内上架) / 平均价格($) | 29.53 |
| 新品(半年内上架) / 平均评分数 | 12.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.026313 |
| 所有Listing(半年内) / 同类目退货率 | 0.035095 |
| 所有Listing(半年内) / 搜索购买比 | 9.11699 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10854 |

### Brake Controls (制动控制装置)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Brake Controls |
| Listing样本数(TOP100) / 细分市场(翻译) | 制动控制装置 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Exterior Accessories:Trailer Accessories:Brake Controls |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：60 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 21878.0 |
| Listing样本数(TOP100) / 月均销量 | 218.0 |
| Listing样本数(TOP100) / 月均销售额($) | 19868.0 |
| Listing样本数(TOP100) / 平均价格($) | 87.23 |
| Listing样本数(TOP100) / 平均评分数 | 308.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 88443.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 75%  <br> AMZ: 11%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.377 |
| Listing样本数(TOP100) / 品牌集中度 | 0.591 |
| Listing样本数(TOP100) / 卖家集中度 | 0.536 |
| Listing样本数(TOP100) / 商品总数 | 700.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.2233 |
| Listing样本数(TOP100) / 平均体积(in³) | 132.3349 |
| Listing样本数(TOP100) / 平均毛利率 | 0.71 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 56.0% |
| 头部Listing数(TOP10) / 月均销量 | 824.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 70215.0 |
| 头部Listing数(TOP10) / 平均BSR | 11789.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 159.0 |
| 新品(半年内上架) / 月均销售额($) | 16625.0 |
| 新品(半年内上架) / 平均价格($) | 105.92 |
| 新品(半年内上架) / 平均评分数 | 14.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.060507998 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 9.02048 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Metric Inserts & Kits (米制刀片和套件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Metric Inserts & Kits |
| Listing样本数(TOP100) / 细分市场(翻译) | 米制刀片和套件 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Tools & Equipment:Thread Repair Kits:Metric Inserts & Kits |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：61 <br> 卖家：63 |
| Listing样本数(TOP100) / 月总销量 | 21461.0 |
| Listing样本数(TOP100) / 月均销量 | 214.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7905.0 |
| Listing样本数(TOP100) / 平均价格($) | 43.87 |
| Listing样本数(TOP100) / 平均评分数 | 196.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 142807.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 7%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.49 |
| Listing样本数(TOP100) / 品牌集中度 | 0.602 |
| Listing样本数(TOP100) / 卖家集中度 | 0.626 |
| Listing样本数(TOP100) / 商品总数 | 656.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.4889 |
| Listing样本数(TOP100) / 平均体积(in³) | 152.012 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.67 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 1052.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 29582.0 |
| 头部Listing数(TOP10) / 平均BSR | 15551.0 |
| 新品(半年内上架) / 新品数量 | 13.0 |
| 新品(半年内上架) / 新品占比 | 0.13 |
| 新品(半年内上架) / 月均销量 | 136.0 |
| 新品(半年内上架) / 月均销售额($) | 7995.0 |
| 新品(半年内上架) / 平均价格($) | 52.09 |
| 新品(半年内上架) / 平均评分数 | 51.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.055958 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 9.17915 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Manual Pasta Makers (手动面条机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Manual Pasta Makers |
| Listing样本数(TOP100) / 细分市场(翻译) | 手动面条机 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Kitchen Utensils & Gadgets:Pasta & Pizza Tools:Pasta Makers & Accessories:Manual Pasta Makers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：84 <br> 卖家：82 |
| Listing样本数(TOP100) / 月总销量 | 21185.0 |
| Listing样本数(TOP100) / 月均销量 | 211.0 |
| Listing样本数(TOP100) / 月均销售额($) | 8471.0 |
| Listing样本数(TOP100) / 平均价格($) | 29.23 |
| Listing样本数(TOP100) / 平均评分数 | 1110.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 75929.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 5%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.444 |
| Listing样本数(TOP100) / 品牌集中度 | 0.524 |
| Listing样本数(TOP100) / 卖家集中度 | 0.553 |
| Listing样本数(TOP100) / 商品总数 | 926.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.3435 |
| Listing样本数(TOP100) / 平均体积(in³) | 357.0627 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 58.0% |
| 头部Listing数(TOP10) / 月均销量 | 940.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 49641.0 |
| 头部Listing数(TOP10) / 平均BSR | 14032.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 102.0 |
| 新品(半年内上架) / 月均销售额($) | 2510.0 |
| 新品(半年内上架) / 平均价格($) | 22.85 |
| 新品(半年内上架) / 平均评分数 | 15.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.054752003 |
| 所有Listing(半年内) / 同类目退货率 | 0.060334 |
| 所有Listing(半年内) / 搜索购买比 | 6.61402 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05948 |

### Hoodies (帽衫)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hoodies |
| Listing样本数(TOP100) / 细分市场(翻译) | 帽衫 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Novelty & More:Clothing:Novelty:Women:Hoodies |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：67 |
| Listing样本数(TOP100) / 月总销量 | 21172.0 |
| Listing样本数(TOP100) / 月均销量 | 211.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7701.0 |
| Listing样本数(TOP100) / 平均价格($) | 37.42 |
| Listing样本数(TOP100) / 平均评分数 | 257.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 277663.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 50%  <br> AMZ: 15%  <br> FBM: 17% |
| Listing样本数(TOP100) / 商品集中度 | 0.274 |
| Listing样本数(TOP100) / 品牌集中度 | 0.421 |
| Listing样本数(TOP100) / 卖家集中度 | 0.52 |
| Listing样本数(TOP100) / 商品总数 | 57144.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8422 |
| Listing样本数(TOP100) / 平均体积(in³) | 302.1462 |
| Listing样本数(TOP100) / 平均毛利率 | 0.64 |
| Listing样本数(TOP100) / A+占比 | 0.55 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 49.0% |
| 头部Listing数(TOP10) / 月均销量 | 580.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 20113.0 |
| 头部Listing数(TOP10) / 平均BSR | 99251.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 169.0 |
| 新品(半年内上架) / 月均销售额($) | 4663.0 |
| 新品(半年内上架) / 平均价格($) | 31.48 |
| 新品(半年内上架) / 平均评分数 | 30.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.058125 |
| 所有Listing(半年内) / 同类目退货率 | 0.139157 |
| 所有Listing(半年内) / 搜索购买比 | 1.88664 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03983 |

### Seat Covers (摩托车座套)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Seat Covers |
| Listing样本数(TOP100) / 细分市场(翻译) | 摩托车座套 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Motorcycle & Powersports:Accessories:Seat Covers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：61 <br> 卖家：63 |
| Listing样本数(TOP100) / 月总销量 | 21007.0 |
| Listing样本数(TOP100) / 月均销量 | 210.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6574.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.1 |
| Listing样本数(TOP100) / 平均评分数 | 316.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 73287.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 2%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.278 |
| Listing样本数(TOP100) / 品牌集中度 | 0.503 |
| Listing样本数(TOP100) / 卖家集中度 | 0.472 |
| Listing样本数(TOP100) / 商品总数 | 3614.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.1461 |
| Listing样本数(TOP100) / 平均体积(in³) | 279.2556 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 88.0% |
| 头部Listing数(TOP10) / 月均销量 | 584.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 19557.0 |
| 头部Listing数(TOP10) / 平均BSR | 13233.0 |
| 新品(半年内上架) / 新品数量 | 19.0 |
| 新品(半年内上架) / 新品占比 | 0.19 |
| 新品(半年内上架) / 月均销量 | 169.0 |
| 新品(半年内上架) / 月均销售额($) | 5030.0 |
| 新品(半年内上架) / 平均价格($) | 30.22 |
| 新品(半年内上架) / 平均评分数 | 35.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.052945 |
| 所有Listing(半年内) / 同类目退货率 | 0.073850006 |
| 所有Listing(半年内) / 搜索购买比 | 3.03603 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03401 |

### Shoulder Bags (单肩包)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Shoulder Bags |
| Listing样本数(TOP100) / 细分市场(翻译) | 单肩包 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Men:Handbags & Shoulder Bags:Shoulder Bags |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 20998.0 |
| Listing样本数(TOP100) / 月均销量 | 209.0 |
| Listing样本数(TOP100) / 月均销售额($) | 7937.0 |
| Listing样本数(TOP100) / 平均价格($) | 43.52 |
| Listing样本数(TOP100) / 平均评分数 | 477.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 296135.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 7%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.448 |
| Listing样本数(TOP100) / 品牌集中度 | 0.56 |
| Listing样本数(TOP100) / 卖家集中度 | 0.571 |
| Listing样本数(TOP100) / 商品总数 | 1042.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.9422 |
| Listing样本数(TOP100) / 平均体积(in³) | 296.7517 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.84 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 941.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 32513.0 |
| 头部Listing数(TOP10) / 平均BSR | 60795.0 |
| 新品(半年内上架) / 新品数量 | 31.0 |
| 新品(半年内上架) / 新品占比 | 0.31 |
| 新品(半年内上架) / 月均销量 | 153.0 |
| 新品(半年内上架) / 月均销售额($) | 5844.0 |
| 新品(半年内上架) / 平均价格($) | 54.82 |
| 新品(半年内上架) / 平均评分数 | 46.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.08689299 |
| 所有Listing(半年内) / 同类目退货率 | 0.133267 |
| 所有Listing(半年内) / 搜索购买比 | 4.37901 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.02784 |

### Monoculars (单筒望远镜)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Monoculars |
| Listing样本数(TOP100) / 细分市场(翻译) | 单筒望远镜 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Camera & Photo:Binoculars & Scopes:Monoculars |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：64 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 20613.0 |
| Listing样本数(TOP100) / 月均销量 | 206.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12621.0 |
| Listing样本数(TOP100) / 平均价格($) | 72.01 |
| Listing样本数(TOP100) / 平均评分数 | 620.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 1219.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 8%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.42 |
| Listing样本数(TOP100) / 品牌集中度 | 0.643 |
| Listing样本数(TOP100) / 卖家集中度 | 0.547 |
| Listing样本数(TOP100) / 商品总数 | 49675.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7406 |
| Listing样本数(TOP100) / 平均体积(in³) | 54.4832 |
| Listing样本数(TOP100) / 平均毛利率 | 0.77 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 866.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 53744.0 |
| 头部Listing数(TOP10) / 平均BSR | 146.0 |
| 新品(半年内上架) / 新品数量 | 22.0 |
| 新品(半年内上架) / 新品占比 | 0.22 |
| 新品(半年内上架) / 月均销量 | 235.0 |
| 新品(半年内上架) / 月均销售额($) | 8084.0 |
| 新品(半年内上架) / 平均价格($) | 41.3 |
| 新品(半年内上架) / 平均评分数 | 45.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.070458 |
| 所有Listing(半年内) / 同类目退货率 | 0.083923995 |
| 所有Listing(半年内) / 搜索购买比 | 7.48953 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04019 |

### Float Valves (浮阀)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Float Valves |
| Listing样本数(TOP100) / 细分市场(翻译) | 浮阀 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Hydraulics, Pneumatics & Plumbing:Fittings:Valves:Float Valves |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 20605.0 |
| Listing样本数(TOP100) / 月均销量 | 206.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4138.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.85 |
| Listing样本数(TOP100) / 平均评分数 | 183.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 41180.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 7%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.326 |
| Listing样本数(TOP100) / 品牌集中度 | 0.43 |
| Listing样本数(TOP100) / 卖家集中度 | 0.42 |
| Listing样本数(TOP100) / 商品总数 | 705.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6712 |
| Listing样本数(TOP100) / 平均体积(in³) | 110.6617 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.73 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 63.0% |
| 头部Listing数(TOP10) / 月均销量 | 671.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13549.0 |
| 头部Listing数(TOP10) / 平均BSR | 9864.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 166.0 |
| 新品(半年内上架) / 月均销售额($) | 3432.0 |
| 新品(半年内上架) / 平均价格($) | 21.8 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.044407 |
| 所有Listing(半年内) / 同类目退货率 | 0.047612 |
| 所有Listing(半年内) / 搜索购买比 | 15.71186 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.16524 |

### Alarms & Anti-Theft (摩托车防盗器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Alarms & Anti-Theft |
| Listing样本数(TOP100) / 细分市场(翻译) | 摩托车防盗器 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Motorcycle & Powersports:Accessories:Electronics:Alarms & Anti-Theft |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：77 <br> 卖家：76 |
| Listing样本数(TOP100) / 月总销量 | 20236.0 |
| Listing样本数(TOP100) / 月均销量 | 202.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5858.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.91 |
| Listing样本数(TOP100) / 平均评分数 | 705.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 82447.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 4%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.389 |
| Listing样本数(TOP100) / 品牌集中度 | 0.489 |
| Listing样本数(TOP100) / 卖家集中度 | 0.47 |
| Listing样本数(TOP100) / 商品总数 | 1018.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8944 |
| Listing样本数(TOP100) / 平均体积(in³) | 39.0662 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 55.0% |
| 头部Listing数(TOP10) / 月均销量 | 786.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 22480.0 |
| 头部Listing数(TOP10) / 平均BSR | 12196.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 111.0 |
| 新品(半年内上架) / 月均销售额($) | 4379.0 |
| 新品(半年内上架) / 平均价格($) | 48.4 |
| 新品(半年内上架) / 平均评分数 | 18.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.047220003 |
| 所有Listing(半年内) / 同类目退货率 | 0.049115 |
| 所有Listing(半年内) / 搜索购买比 | 6.89648 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05711 |

### Weaving Looms (织机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Weaving Looms |
| Listing样本数(TOP100) / 细分市场(翻译) | 织机 |
| Listing样本数(TOP100) / 市场路径 | Arts, Crafts & Sewing:Crafting:Weaving & Spinning:Weaving Looms |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：85 <br> 卖家：83 |
| Listing样本数(TOP100) / 月总销量 | 20155.0 |
| Listing样本数(TOP100) / 月均销量 | 201.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4602.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.49 |
| Listing样本数(TOP100) / 平均评分数 | 311.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 74774.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 4%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.543 |
| Listing样本数(TOP100) / 品牌集中度 | 0.575 |
| Listing样本数(TOP100) / 卖家集中度 | 0.602 |
| Listing样本数(TOP100) / 商品总数 | 502.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0109 |
| Listing样本数(TOP100) / 平均体积(in³) | 105.2123 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.8 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 1094.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 26590.0 |
| 头部Listing数(TOP10) / 平均BSR | 7114.0 |
| 新品(半年内上架) / 新品数量 | 28.0 |
| 新品(半年内上架) / 新品占比 | 0.28 |
| 新品(半年内上架) / 月均销量 | 84.0 |
| 新品(半年内上架) / 月均销售额($) | 1345.0 |
| 新品(半年内上架) / 平均价格($) | 17.68 |
| 新品(半年内上架) / 平均评分数 | 16.0 |
| 新品(半年内上架) / 平均星级 | 3.9 |
| 所有Listing(半年内) / 退货率 | 0.033328 |
| 所有Listing(半年内) / 同类目退货率 | 0.037488 |
| 所有Listing(半年内) / 搜索购买比 | 5.56731 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10263 |

### Leak Detection Tools (泄漏检测工具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Leak Detection Tools |
| Listing样本数(TOP100) / 细分市场(翻译) | 泄漏检测工具 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Test, Measure & Inspect:Inspection & Analysis:Leak Detection Tools |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：77 <br> 卖家：81 |
| Listing样本数(TOP100) / 月总销量 | 19719.0 |
| Listing样本数(TOP100) / 月均销量 | 197.0 |
| Listing样本数(TOP100) / 月均销售额($) | 9699.0 |
| Listing样本数(TOP100) / 平均价格($) | 100.92 |
| Listing样本数(TOP100) / 平均评分数 | 154.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 67545.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 70%  <br> AMZ: 3%  <br> FBM: 9% |
| Listing样本数(TOP100) / 商品集中度 | 0.512 |
| Listing样本数(TOP100) / 品牌集中度 | 0.539 |
| Listing样本数(TOP100) / 卖家集中度 | 0.539 |
| Listing样本数(TOP100) / 商品总数 | 462.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.445 |
| Listing样本数(TOP100) / 平均体积(in³) | 212.0001 |
| Listing样本数(TOP100) / 平均毛利率 | 0.69 |
| Listing样本数(TOP100) / A+占比 | 0.66 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 53.0% |
| 头部Listing数(TOP10) / 月均销量 | 1009.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 24181.0 |
| 头部Listing数(TOP10) / 平均BSR | 7592.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 331.0 |
| 新品(半年内上架) / 月均销售额($) | 10235.0 |
| 新品(半年内上架) / 平均价格($) | 86.38 |
| 新品(半年内上架) / 平均评分数 | 27.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.042957 |
| 所有Listing(半年内) / 同类目退货率 | 0.054436997 |
| 所有Listing(半年内) / 搜索购买比 | 12.84958 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10694 |

### Wedding Dresses (婚纱)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Wedding Dresses |
| Listing样本数(TOP100) / 细分市场(翻译) | 婚纱 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Women:Clothing:Dresses:Wedding Dresses |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：53 <br> 卖家：57 |
| Listing样本数(TOP100) / 月总销量 | 19688.0 |
| Listing样本数(TOP100) / 月均销量 | 196.0 |
| Listing样本数(TOP100) / 月均销售额($) | 14782.0 |
| Listing样本数(TOP100) / 平均价格($) | 82.75 |
| Listing样本数(TOP100) / 平均评分数 | 171.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 648744.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 51%  <br> AMZ: 0%  <br> FBM: 38% |
| Listing样本数(TOP100) / 商品集中度 | 0.308 |
| Listing样本数(TOP100) / 品牌集中度 | 0.616 |
| Listing样本数(TOP100) / 卖家集中度 | 0.571 |
| Listing样本数(TOP100) / 商品总数 | 2587.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4243 |
| Listing样本数(TOP100) / 平均体积(in³) | 238.1708 |
| Listing样本数(TOP100) / 平均毛利率 | 0.73 |
| Listing样本数(TOP100) / A+占比 | 0.9 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 95.0% |
| 头部Listing数(TOP10) / 月均销量 | 606.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 41695.0 |
| 头部Listing数(TOP10) / 平均BSR | 82170.0 |
| 新品(半年内上架) / 新品数量 | 32.0 |
| 新品(半年内上架) / 新品占比 | 0.32 |
| 新品(半年内上架) / 月均销量 | 236.0 |
| 新品(半年内上架) / 月均销售额($) | 15451.0 |
| 新品(半年内上架) / 平均价格($) | 69.93 |
| 新品(半年内上架) / 平均评分数 | 24.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | N/A |
| 所有Listing(半年内) / 同类目退货率 | N/A |
| 所有Listing(半年内) / 搜索购买比 | N/A |
| 所有Listing(半年内) / 同类目搜索购买比 | N/A |

### Optics Accessories (光学配件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Optics Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 光学配件 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Hunting & Fishing:Shooting:Optics:Optics Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：52 <br> 卖家：57 |
| Listing样本数(TOP100) / 月总销量 | 19349.0 |
| Listing样本数(TOP100) / 月均销量 | 193.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5682.0 |
| Listing样本数(TOP100) / 平均价格($) | 32.88 |
| Listing样本数(TOP100) / 平均评分数 | 354.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 61686.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 5%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.27 |
| Listing样本数(TOP100) / 品牌集中度 | 0.525 |
| Listing样本数(TOP100) / 卖家集中度 | 0.508 |
| Listing样本数(TOP100) / 商品总数 | 1524.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2033 |
| Listing样本数(TOP100) / 平均体积(in³) | 30.4807 |
| Listing样本数(TOP100) / 平均毛利率 | 0.66 |
| Listing样本数(TOP100) / A+占比 | 0.69 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 56.0% |
| 头部Listing数(TOP10) / 月均销量 | 522.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13719.0 |
| 头部Listing数(TOP10) / 平均BSR | 19847.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 156.0 |
| 新品(半年内上架) / 月均销售额($) | 2362.0 |
| 新品(半年内上架) / 平均价格($) | 14.96 |
| 新品(半年内上架) / 平均评分数 | 18.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.056332998 |
| 所有Listing(半年内) / 同类目退货率 | 0.045063 |
| 所有Listing(半年内) / 搜索购买比 | 6.16364 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07428 |

### Bait Traps (诱饵陷阱)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bait Traps |
| Listing样本数(TOP100) / 细分市场(翻译) | 诱饵陷阱 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Hunting & Fishing:Fishing:Baits & Accessories:Bait Traps |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：60 <br> 卖家：66 |
| Listing样本数(TOP100) / 月总销量 | 19010.0 |
| Listing样本数(TOP100) / 月均销量 | 190.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4077.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.88 |
| Listing样本数(TOP100) / 平均评分数 | 284.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 72798.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 3%  <br> FBM: 10% |
| Listing样本数(TOP100) / 商品集中度 | 0.46 |
| Listing样本数(TOP100) / 品牌集中度 | 0.609 |
| Listing样本数(TOP100) / 卖家集中度 | 0.568 |
| Listing样本数(TOP100) / 商品总数 | 588.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.6779 |
| Listing样本数(TOP100) / 平均体积(in³) | 551.175 |
| Listing样本数(TOP100) / 平均毛利率 | 0.54 |
| Listing样本数(TOP100) / A+占比 | 0.71 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 55.0% |
| 头部Listing数(TOP10) / 月均销量 | 875.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 14126.0 |
| 头部Listing数(TOP10) / 平均BSR | 13355.0 |
| 新品(半年内上架) / 新品数量 | 11.0 |
| 新品(半年内上架) / 新品占比 | 0.11 |
| 新品(半年内上架) / 月均销量 | 94.0 |
| 新品(半年内上架) / 月均销售额($) | 2798.0 |
| 新品(半年内上架) / 平均价格($) | 30.53 |
| 新品(半年内上架) / 平均评分数 | 4.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.033126 |
| 所有Listing(半年内) / 同类目退货率 | 0.054621 |
| 所有Listing(半年内) / 搜索购买比 | 4.49488 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06323 |

### Replacement Wheels (备用轮)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Replacement Wheels |
| Listing样本数(TOP100) / 细分市场(翻译) | 备用轮 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Skates, Skateboards & Scooters:Scooters & Equipment:Components & Parts:Replacement Wheels |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：45 <br> 卖家：45 |
| Listing样本数(TOP100) / 月总销量 | 18854.0 |
| Listing样本数(TOP100) / 月均销量 | 188.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4357.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.5 |
| Listing样本数(TOP100) / 平均评分数 | 298.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 73113.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 3%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.337 |
| Listing样本数(TOP100) / 品牌集中度 | 0.645 |
| Listing样本数(TOP100) / 卖家集中度 | 0.645 |
| Listing样本数(TOP100) / 商品总数 | 1473.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.0516 |
| Listing样本数(TOP100) / 平均体积(in³) | 232.8788 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.7 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 84.0% |
| 头部Listing数(TOP10) / 月均销量 | 635.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 12999.0 |
| 头部Listing数(TOP10) / 平均BSR | 14786.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 119.0 |
| 新品(半年内上架) / 月均销售额($) | 2331.0 |
| 新品(半年内上架) / 平均价格($) | 19.99 |
| 新品(半年内上架) / 平均评分数 | 14.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.08586799 |
| 所有Listing(半年内) / 同类目退货率 | 0.060827 |
| 所有Listing(半年内) / 搜索购买比 | 6.49609 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06768 |

### Fly Tying Equipment (绑蝇设备)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Fly Tying Equipment |
| Listing样本数(TOP100) / 细分市场(翻译) | 绑蝇设备 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Hunting & Fishing:Fishing:Fly Fishing:Accessories:Fly Tying Equipment |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：58 <br> 卖家：64 |
| Listing样本数(TOP100) / 月总销量 | 18675.0 |
| Listing样本数(TOP100) / 月均销量 | 186.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3221.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.02 |
| Listing样本数(TOP100) / 平均评分数 | 478.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 93912.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 1%  <br> FBM: 11% |
| Listing样本数(TOP100) / 商品集中度 | 0.472 |
| Listing样本数(TOP100) / 品牌集中度 | 0.627 |
| Listing样本数(TOP100) / 卖家集中度 | 0.633 |
| Listing样本数(TOP100) / 商品总数 | 1118.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2986 |
| Listing样本数(TOP100) / 平均体积(in³) | 41.2118 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.46 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 53.0% |
| 头部Listing数(TOP10) / 月均销量 | 882.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 11629.0 |
| 头部Listing数(TOP10) / 平均BSR | 22179.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 107.0 |
| 新品(半年内上架) / 月均销售额($) | 1603.0 |
| 新品(半年内上架) / 平均价格($) | 15.17 |
| 新品(半年内上架) / 平均评分数 | 10.0 |
| 新品(半年内上架) / 平均星级 | 2.3 |
| 所有Listing(半年内) / 退货率 | 0.028448999 |
| 所有Listing(半年内) / 同类目退货率 | 0.054621 |
| 所有Listing(半年内) / 搜索购买比 | 6.14312 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06323 |

### Hair Dryer Stands (吹风机支架)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Hair Dryer Stands |
| Listing样本数(TOP100) / 细分市场(翻译) | 吹风机支架 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Medical Supplies & Equipment:Mobility & Daily Living Aids:Bathroom Safety, Aids & Accessories:Hair Dryer Stands |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：70 <br> 卖家：71 |
| Listing样本数(TOP100) / 月总销量 | 18590.0 |
| Listing样本数(TOP100) / 月均销量 | 185.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3318.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.87 |
| Listing样本数(TOP100) / 平均评分数 | 219.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 140717.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 94%  <br> AMZ: 0%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.431 |
| Listing样本数(TOP100) / 品牌集中度 | 0.506 |
| Listing样本数(TOP100) / 卖家集中度 | 0.506 |
| Listing样本数(TOP100) / 商品总数 | 557.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3448 |
| Listing样本数(TOP100) / 平均体积(in³) | 581.3536 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.81 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 81.0% |
| 头部Listing数(TOP10) / 月均销量 | 801.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 11547.0 |
| 头部Listing数(TOP10) / 平均BSR | 43849.0 |
| 新品(半年内上架) / 新品数量 | 29.0 |
| 新品(半年内上架) / 新品占比 | 0.29 |
| 新品(半年内上架) / 月均销量 | 116.0 |
| 新品(半年内上架) / 月均销售额($) | 2284.0 |
| 新品(半年内上架) / 平均价格($) | 21.04 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.086644 |
| 所有Listing(半年内) / 同类目退货率 | 0.068347 |
| 所有Listing(半年内) / 搜索购买比 | 7.50379 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.078449994 |

### Flags (标志)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Flags |
| Listing样本数(TOP100) / 细分市场(翻译) | 标志 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Boating & Sailing:Boating:Boat Cabin Products:Flags |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：66 <br> 卖家：68 |
| Listing样本数(TOP100) / 月总销量 | 18506.0 |
| Listing样本数(TOP100) / 月均销量 | 185.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3724.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.28 |
| Listing样本数(TOP100) / 平均评分数 | 223.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 93041.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 67%  <br> AMZ: 14%  <br> FBM: 12% |
| Listing样本数(TOP100) / 商品集中度 | 0.379 |
| Listing样本数(TOP100) / 品牌集中度 | 0.627 |
| Listing样本数(TOP100) / 卖家集中度 | 0.602 |
| Listing样本数(TOP100) / 商品总数 | 421.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6035 |
| Listing样本数(TOP100) / 平均体积(in³) | 132.0584 |
| Listing样本数(TOP100) / 平均毛利率 | 0.61 |
| Listing样本数(TOP100) / A+占比 | 0.67 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 54.0% |
| 头部Listing数(TOP10) / 月均销量 | 701.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13717.0 |
| 头部Listing数(TOP10) / 平均BSR | 11252.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 199.0 |
| 新品(半年内上架) / 月均销售额($) | 3723.0 |
| 新品(半年内上架) / 平均价格($) | 19.93 |
| 新品(半年内上架) / 平均评分数 | 9.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.026122 |
| 所有Listing(半年内) / 同类目退货率 | 0.043670997 |
| 所有Listing(半年内) / 搜索购买比 | 8.33724 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0947 |

### Clothing (服装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Clothing |
| Listing样本数(TOP100) / 细分市场(翻译) | 服装 |
| Listing样本数(TOP100) / 市场路径 | Clothing, Shoes & Jewelry:Girls:Clothing |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：69 |
| Listing样本数(TOP100) / 月总销量 | 18458.0 |
| Listing样本数(TOP100) / 月均销量 | 184.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3515.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.36 |
| Listing样本数(TOP100) / 平均评分数 | 95.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 369089.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 77%  <br> AMZ: 16%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.501 |
| Listing样本数(TOP100) / 品牌集中度 | 0.56 |
| Listing样本数(TOP100) / 卖家集中度 | 0.633 |
| Listing样本数(TOP100) / 商品总数 | 54689.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3975 |
| Listing样本数(TOP100) / 平均体积(in³) | 113.0001 |
| Listing样本数(TOP100) / 平均毛利率 | 0.53 |
| Listing样本数(TOP100) / A+占比 | 0.69 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 925.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 17617.0 |
| 头部Listing数(TOP10) / 平均BSR | 69255.0 |
| 新品(半年内上架) / 新品数量 | 31.0 |
| 新品(半年内上架) / 新品占比 | 0.31 |
| 新品(半年内上架) / 月均销量 | 135.0 |
| 新品(半年内上架) / 月均销售额($) | 3064.0 |
| 新品(半年内上架) / 平均价格($) | 21.97 |
| 新品(半年内上架) / 平均评分数 | 45.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | N/A |
| 所有Listing(半年内) / 同类目退货率 | N/A |
| 所有Listing(半年内) / 搜索购买比 | N/A |
| 所有Listing(半年内) / 同类目搜索购买比 | N/A |

### Foot Warmers (暖脚)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Foot Warmers |
| Listing样本数(TOP100) / 细分市场(翻译) | 暖脚 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Outdoor Recreation:Camping & Hiking:Safety & Survival:Hand & Foot Warmers:Foot Warmers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：68 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 18208.0 |
| Listing样本数(TOP100) / 月均销量 | 182.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4698.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.0 |
| Listing样本数(TOP100) / 平均评分数 | 894.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 103346.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 91%  <br> AMZ: 6%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.481 |
| Listing样本数(TOP100) / 品牌集中度 | 0.608 |
| Listing样本数(TOP100) / 卖家集中度 | 0.557 |
| Listing样本数(TOP100) / 商品总数 | 529.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3418 |
| Listing样本数(TOP100) / 平均体积(in³) | 157.5383 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 53.0% |
| 头部Listing数(TOP10) / 月均销量 | 875.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 20065.0 |
| 头部Listing数(TOP10) / 平均BSR | 19277.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 112.0 |
| 新品(半年内上架) / 月均销售额($) | 2795.0 |
| 新品(半年内上架) / 平均价格($) | 24.11 |
| 新品(半年内上架) / 平均评分数 | 80.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.232944 |
| 所有Listing(半年内) / 同类目退货率 | 0.161117 |
| 所有Listing(半年内) / 搜索购买比 | 10.45943 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13136 |

### Bats (蝙蝠)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bats |
| Listing样本数(TOP100) / 细分市场(翻译) | 蝙蝠 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Backyard Birding & Wildlife:Bats |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：79 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 18073.0 |
| Listing样本数(TOP100) / 月均销量 | 180.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5230.0 |
| Listing样本数(TOP100) / 平均价格($) | 34.37 |
| Listing样本数(TOP100) / 平均评分数 | 344.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 144743.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 82%  <br> AMZ: 5%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.54 |
| Listing样本数(TOP100) / 品牌集中度 | 0.559 |
| Listing样本数(TOP100) / 卖家集中度 | 0.556 |
| Listing样本数(TOP100) / 商品总数 | 216.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.1939 |
| Listing样本数(TOP100) / 平均体积(in³) | 479.494 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.65 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 47.0% |
| 头部Listing数(TOP10) / 月均销量 | 975.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 27371.0 |
| 头部Listing数(TOP10) / 平均BSR | 16017.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 80.0 |
| 新品(半年内上架) / 月均销售额($) | 2522.0 |
| 新品(半年内上架) / 平均价格($) | 35.25 |
| 新品(半年内上架) / 平均评分数 | 6.0 |
| 新品(半年内上架) / 平均星级 | 3.7 |
| 所有Listing(半年内) / 退货率 | 0.026055 |
| 所有Listing(半年内) / 同类目退货率 | 0.029515 |
| 所有Listing(半年内) / 搜索购买比 | 14.51753 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12637 |

### Growth Charts (身高墙贴)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Growth Charts |
| Listing样本数(TOP100) / 细分市场(翻译) | 身高墙贴 |
| Listing样本数(TOP100) / 市场路径 | Baby Products:Nursery:Décor:Wall Décor:Growth Charts |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 17946.0 |
| Listing样本数(TOP100) / 月均销量 | 179.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3344.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.12 |
| Listing样本数(TOP100) / 平均评分数 | 416.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 21450.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 1%  <br> FBM: 11% |
| Listing样本数(TOP100) / 商品集中度 | 0.434 |
| Listing样本数(TOP100) / 品牌集中度 | 0.474 |
| Listing样本数(TOP100) / 卖家集中度 | 0.474 |
| Listing样本数(TOP100) / 商品总数 | 406.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7985 |
| Listing样本数(TOP100) / 平均体积(in³) | 254.7582 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.7 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 66.0% |
| 头部Listing数(TOP10) / 月均销量 | 779.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13259.0 |
| 头部Listing数(TOP10) / 平均BSR | 8158.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 77.0 |
| 新品(半年内上架) / 月均销售额($) | 1186.0 |
| 新品(半年内上架) / 平均价格($) | 14.44 |
| 新品(半年内上架) / 平均评分数 | 8.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.037173 |
| 所有Listing(半年内) / 同类目退货率 | 0.047842003 |
| 所有Listing(半年内) / 搜索购买比 | 6.9049 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.108509995 |

### Candle Sconces (壁突式烛台)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Candle Sconces |
| Listing样本数(TOP100) / 细分市场(翻译) | 壁突式烛台 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Candles & Holders:Candleholders:Candle Sconces |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：61 <br> 卖家：60 |
| Listing样本数(TOP100) / 月总销量 | 17754.0 |
| Listing样本数(TOP100) / 月均销量 | 177.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4778.0 |
| Listing样本数(TOP100) / 平均价格($) | 28.03 |
| Listing样本数(TOP100) / 平均评分数 | 346.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 291536.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 99%  <br> AMZ: 0%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.352 |
| Listing样本数(TOP100) / 品牌集中度 | 0.509 |
| Listing样本数(TOP100) / 卖家集中度 | 0.516 |
| Listing样本数(TOP100) / 商品总数 | 585.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.884 |
| Listing样本数(TOP100) / 平均体积(in³) | 344.7286 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 85.0% |
| 头部Listing数(TOP10) / 月均销量 | 625.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13988.0 |
| 头部Listing数(TOP10) / 平均BSR | 64481.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 166.0 |
| 新品(半年内上架) / 月均销售额($) | 4230.0 |
| 新品(半年内上架) / 平均价格($) | 26.71 |
| 新品(半年内上架) / 平均评分数 | 56.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.102694996 |
| 所有Listing(半年内) / 同类目退货率 | 0.084172 |
| 所有Listing(半年内) / 搜索购买比 | 2.92451 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05765 |

### Tortilla Servers (玉米饼服务员)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tortilla Servers |
| Listing样本数(TOP100) / 细分市场(翻译) | 玉米饼服务员 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Dining & Entertaining:Dinnerware & Serveware:Serveware:Tortilla Servers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：84 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 17739.0 |
| Listing样本数(TOP100) / 月均销量 | 177.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3354.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.25 |
| Listing样本数(TOP100) / 平均评分数 | 454.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 122531.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 86%  <br> AMZ: 8%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.558 |
| Listing样本数(TOP100) / 品牌集中度 | 0.58 |
| Listing样本数(TOP100) / 卖家集中度 | 0.65 |
| Listing样本数(TOP100) / 商品总数 | 212.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5748 |
| Listing样本数(TOP100) / 平均体积(in³) | 143.4979 |
| Listing样本数(TOP100) / 平均毛利率 | 0.52 |
| Listing样本数(TOP100) / A+占比 | 0.7 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 38.0% |
| 头部Listing数(TOP10) / 月均销量 | 990.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 17107.0 |
| 头部Listing数(TOP10) / 平均BSR | 16080.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 67.0 |
| 新品(半年内上架) / 月均销售额($) | 1344.0 |
| 新品(半年内上架) / 平均价格($) | 21.64 |
| 新品(半年内上架) / 平均评分数 | 16.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.062607996 |
| 所有Listing(半年内) / 同类目退货率 | 0.053512998 |
| 所有Listing(半年内) / 搜索购买比 | 6.45042 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07874 |

### Devotional Candles (祈祷蜡烛)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Devotional Candles |
| Listing样本数(TOP100) / 细分市场(翻译) | 祈祷蜡烛 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Candles & Holders:Candles:Specialty Candles:Devotional Candles |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：47 <br> 卖家：45 |
| Listing样本数(TOP100) / 月总销量 | 17570.0 |
| Listing样本数(TOP100) / 月均销量 | 175.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4539.0 |
| Listing样本数(TOP100) / 平均价格($) | 25.95 |
| Listing样本数(TOP100) / 平均评分数 | 191.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 371515.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 4%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.355 |
| Listing样本数(TOP100) / 品牌集中度 | 0.611 |
| Listing样本数(TOP100) / 卖家集中度 | 0.645 |
| Listing样本数(TOP100) / 商品总数 | 831.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.7427 |
| Listing样本数(TOP100) / 平均体积(in³) | 14.2222 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.46 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 44.0% |
| 头部Listing数(TOP10) / 月均销量 | 623.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 15306.0 |
| 头部Listing数(TOP10) / 平均BSR | 90195.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 124.0 |
| 新品(半年内上架) / 月均销售额($) | 4017.0 |
| 新品(半年内上架) / 平均价格($) | 33.24 |
| 新品(半年内上架) / 平均评分数 | 8.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.040833 |
| 所有Listing(半年内) / 同类目退货率 | 0.034018 |
| 所有Listing(半年内) / 搜索购买比 | 5.77389 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.100389995 |

### Bulb Planters (球茎栽植器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Bulb Planters |
| Listing样本数(TOP100) / 细分市场(翻译) | 球茎栽植器 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Gardening & Lawn Care:Hand Tools:Bulb Planters |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 17280.0 |
| Listing样本数(TOP100) / 月均销量 | 172.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4189.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.92 |
| Listing样本数(TOP100) / 平均评分数 | 295.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 157053.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 4%  <br> FBM: 7% |
| Listing样本数(TOP100) / 商品集中度 | 0.419 |
| Listing样本数(TOP100) / 品牌集中度 | 0.481 |
| Listing样本数(TOP100) / 卖家集中度 | 0.474 |
| Listing样本数(TOP100) / 商品总数 | 201.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.3184 |
| Listing样本数(TOP100) / 平均体积(in³) | 610.3125 |
| Listing样本数(TOP100) / 平均毛利率 | 0.52 |
| Listing样本数(TOP100) / A+占比 | 0.65 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 724.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 18675.0 |
| 头部Listing数(TOP10) / 平均BSR | 26194.0 |
| 新品(半年内上架) / 新品数量 | 26.0 |
| 新品(半年内上架) / 新品占比 | 0.26 |
| 新品(半年内上架) / 月均销量 | 117.0 |
| 新品(半年内上架) / 月均销售额($) | 2289.0 |
| 新品(半年内上架) / 平均价格($) | 22.76 |
| 新品(半年内上架) / 平均评分数 | 17.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.028978 |
| 所有Listing(半年内) / 同类目退货率 | 0.035097 |
| 所有Listing(半年内) / 搜索购买比 | 13.11661 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555999 |

### Trim (装饰)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Trim |
| Listing样本数(TOP100) / 细分市场(翻译) | 装饰 |
| Listing样本数(TOP100) / 市场路径 | Power & Hand Tools:Power Tool Parts & Accessories:Router Parts & Accessories:Router Bits:Straight, Spiral & Trim Bits:Trim |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：54 <br> 卖家：56 |
| Listing样本数(TOP100) / 月总销量 | 17275.0 |
| Listing样本数(TOP100) / 月均销量 | 172.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5000.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.56 |
| Listing样本数(TOP100) / 平均评分数 | 248.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 120967.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 11%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.43 |
| Listing样本数(TOP100) / 品牌集中度 | 0.619 |
| Listing样本数(TOP100) / 卖家集中度 | 0.623 |
| Listing样本数(TOP100) / 商品总数 | 680.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2691 |
| Listing样本数(TOP100) / 平均体积(in³) | 23.3611 |
| Listing样本数(TOP100) / 平均毛利率 | 0.67 |
| Listing样本数(TOP100) / A+占比 | 0.76 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 743.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 23591.0 |
| 头部Listing数(TOP10) / 平均BSR | 22418.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 119.0 |
| 新品(半年内上架) / 月均销售额($) | 4349.0 |
| 新品(半年内上架) / 平均价格($) | 36.54 |
| 新品(半年内上架) / 平均评分数 | 27.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.024424 |
| 所有Listing(半年内) / 同类目退货率 | 0.030009 |
| 所有Listing(半年内) / 搜索购买比 | 11.25348 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09904 |

### Urinal Accessories (小便池配件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Urinal Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 小便池配件 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Kitchen & Bath Fixtures:Bathroom Fixtures:Urinals & Urinal Parts:Urinal Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：77 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 16896.0 |
| Listing样本数(TOP100) / 月均销量 | 168.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5998.0 |
| Listing样本数(TOP100) / 平均价格($) | 33.42 |
| Listing样本数(TOP100) / 平均评分数 | 83.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 149784.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 68%  <br> AMZ: 5%  <br> FBM: 11% |
| Listing样本数(TOP100) / 商品集中度 | 0.458 |
| Listing样本数(TOP100) / 品牌集中度 | 0.548 |
| Listing样本数(TOP100) / 卖家集中度 | 0.592 |
| Listing样本数(TOP100) / 商品总数 | 509.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.641 |
| Listing样本数(TOP100) / 平均体积(in³) | 226.1168 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.69 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 49.0% |
| 头部Listing数(TOP10) / 月均销量 | 773.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 31145.0 |
| 头部Listing数(TOP10) / 平均BSR | 100383.0 |
| 新品(半年内上架) / 新品数量 | 25.0 |
| 新品(半年内上架) / 新品占比 | 0.25 |
| 新品(半年内上架) / 月均销量 | 152.0 |
| 新品(半年内上架) / 月均销售额($) | 5240.0 |
| 新品(半年内上架) / 平均价格($) | 26.61 |
| 新品(半年内上架) / 平均评分数 | 11.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.018725 |
| 所有Listing(半年内) / 同类目退货率 | 0.071948 |
| 所有Listing(半年内) / 搜索购买比 | 25.32871 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.13555 |

### Tools (工具)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Tools |
| Listing样本数(TOP100) / 细分市场(翻译) | 工具 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Sports:Boating & Sailing:Boating:Maintenance Supplies:Tools |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 16668.0 |
| Listing样本数(TOP100) / 月均销量 | 166.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4500.0 |
| Listing样本数(TOP100) / 平均价格($) | 33.49 |
| Listing样本数(TOP100) / 平均评分数 | 187.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 84281.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 7%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.389 |
| Listing样本数(TOP100) / 品牌集中度 | 0.463 |
| Listing样本数(TOP100) / 卖家集中度 | 0.468 |
| Listing样本数(TOP100) / 商品总数 | 843.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4432 |
| Listing样本数(TOP100) / 平均体积(in³) | 97.7625 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.76 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 648.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 10759.0 |
| 头部Listing数(TOP10) / 平均BSR | 17239.0 |
| 新品(半年内上架) / 新品数量 | 21.0 |
| 新品(半年内上架) / 新品占比 | 0.21 |
| 新品(半年内上架) / 月均销量 | 146.0 |
| 新品(半年内上架) / 月均销售额($) | 4227.0 |
| 新品(半年内上架) / 平均价格($) | 32.92 |
| 新品(半年内上架) / 平均评分数 | 11.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.036353 |
| 所有Listing(半年内) / 同类目退货率 | 0.054621 |
| 所有Listing(半年内) / 搜索购买比 | 9.54719 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.06323 |

### License Plate Frames (摩托车牌照架)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | License Plate Frames |
| Listing样本数(TOP100) / 细分市场(翻译) | 摩托车牌照架 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Motorcycle & Powersports:Parts:Body & Frame Parts:License Plate Frames |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：69 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 16515.0 |
| Listing样本数(TOP100) / 月均销量 | 165.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3098.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.31 |
| Listing样本数(TOP100) / 平均评分数 | 146.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 116187.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 5%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.403 |
| Listing样本数(TOP100) / 品牌集中度 | 0.548 |
| Listing样本数(TOP100) / 卖家集中度 | 0.541 |
| Listing样本数(TOP100) / 商品总数 | 1293.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5747 |
| Listing样本数(TOP100) / 平均体积(in³) | 60.9151 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.58 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 78.0% |
| 头部Listing数(TOP10) / 月均销量 | 665.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 12524.0 |
| 头部Listing数(TOP10) / 平均BSR | 13982.0 |
| 新品(半年内上架) / 新品数量 | 23.0 |
| 新品(半年内上架) / 新品占比 | 0.23 |
| 新品(半年内上架) / 月均销量 | 213.0 |
| 新品(半年内上架) / 月均销售额($) | 3888.0 |
| 新品(半年内上架) / 平均价格($) | 16.03 |
| 新品(半年内上架) / 平均评分数 | 8.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.041805 |
| 所有Listing(半年内) / 同类目退货率 | 0.046999 |
| 所有Listing(半年内) / 搜索购买比 | 3.37068 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.054530002 |

### Speedometers (车速里程表)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Speedometers |
| Listing样本数(TOP100) / 细分市场(翻译) | 车速里程表 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Replacement Parts:Lighting & Electrical:Electrical:Gauges:Speedometers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：53 <br> 卖家：58 |
| Listing样本数(TOP100) / 月总销量 | 16359.0 |
| Listing样本数(TOP100) / 月均销量 | 163.0 |
| Listing样本数(TOP100) / 月均销售额($) | 5995.0 |
| Listing样本数(TOP100) / 平均价格($) | 46.69 |
| Listing样本数(TOP100) / 平均评分数 | 173.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 108983.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.2 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 2%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.374 |
| Listing样本数(TOP100) / 品牌集中度 | 0.634 |
| Listing样本数(TOP100) / 卖家集中度 | 0.616 |
| Listing样本数(TOP100) / 商品总数 | 1361.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3943 |
| Listing样本数(TOP100) / 平均体积(in³) | 59.8588 |
| Listing样本数(TOP100) / 平均毛利率 | 0.68 |
| Listing样本数(TOP100) / A+占比 | 0.82 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 612.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13910.0 |
| 头部Listing数(TOP10) / 平均BSR | 12418.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 155.0 |
| 新品(半年内上架) / 月均销售额($) | 3130.0 |
| 新品(半年内上架) / 平均价格($) | 22.2 |
| 新品(半年内上架) / 平均评分数 | 23.0 |
| 新品(半年内上架) / 平均星级 | 3.6 |
| 所有Listing(半年内) / 退货率 | 0.091709 |
| 所有Listing(半年内) / 同类目退货率 | 0.040142003 |
| 所有Listing(半年内) / 搜索购买比 | 3.01926 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.098000005 |

### Food Processor Parts & Accessories (食物处理器零件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Food Processor Parts & Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 食物处理器零件 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Small Appliance Parts & Accessories:Food Processor Parts & Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：70 |
| Listing样本数(TOP100) / 月总销量 | 16119.0 |
| Listing样本数(TOP100) / 月均销量 | 161.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4811.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.23 |
| Listing样本数(TOP100) / 平均评分数 | 313.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 281564.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 80%  <br> AMZ: 10%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.269 |
| Listing样本数(TOP100) / 品牌集中度 | 0.36 |
| Listing样本数(TOP100) / 卖家集中度 | 0.416 |
| Listing样本数(TOP100) / 商品总数 | 2770.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.0756 |
| Listing样本数(TOP100) / 平均体积(in³) | 234.9414 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.61 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 56.0% |
| 头部Listing数(TOP10) / 月均销量 | 433.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 10595.0 |
| 头部Listing数(TOP10) / 平均BSR | 135437.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 228.0 |
| 新品(半年内上架) / 月均销售额($) | 4753.0 |
| 新品(半年内上架) / 平均价格($) | 25.97 |
| 新品(半年内上架) / 平均评分数 | 27.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.087177 |
| 所有Listing(半年内) / 同类目退货率 | 0.052034 |
| 所有Listing(半年内) / 搜索购买比 | 12.76149 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.106759995 |

### Amplifiers (放大器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Amplifiers |
| Listing样本数(TOP100) / 细分市场(翻译) | 放大器 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Headphones, Earbuds & Accessories:Amplifiers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：52 <br> 卖家：60 |
| Listing样本数(TOP100) / 月总销量 | 15913.0 |
| Listing样本数(TOP100) / 月均销量 | 159.0 |
| Listing样本数(TOP100) / 月均销售额($) | 13260.0 |
| Listing样本数(TOP100) / 平均价格($) | 90.53 |
| Listing样本数(TOP100) / 平均评分数 | 647.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 34279.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.3 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 5%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.341 |
| Listing样本数(TOP100) / 品牌集中度 | 0.644 |
| Listing样本数(TOP100) / 卖家集中度 | 0.553 |
| Listing样本数(TOP100) / 商品总数 | 443.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.707 |
| Listing样本数(TOP100) / 平均体积(in³) | 49.6678 |
| Listing样本数(TOP100) / 平均毛利率 | 0.83 |
| Listing样本数(TOP100) / A+占比 | 0.87 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 43.0% |
| 头部Listing数(TOP10) / 月均销量 | 542.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 42067.0 |
| 头部Listing数(TOP10) / 平均BSR | 8526.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 101.0 |
| 新品(半年内上架) / 月均销售额($) | 10032.0 |
| 新品(半年内上架) / 平均价格($) | 91.08 |
| 新品(半年内上架) / 平均评分数 | 25.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.098239005 |
| 所有Listing(半年内) / 同类目退货率 | 0.086538 |
| 所有Listing(半年内) / 搜索购买比 | 4.61405 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03304 |

### Kick Plates (踢脚板)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Kick Plates |
| Listing样本数(TOP100) / 细分市场(翻译) | 踢脚板 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Hardware:Door Hardware & Locks:Kick Plates |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：50 <br> 卖家：49 |
| Listing样本数(TOP100) / 月总销量 | 15899.0 |
| Listing样本数(TOP100) / 月均销量 | 158.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4124.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.06 |
| Listing样本数(TOP100) / 平均评分数 | 111.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 110386.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 6%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.272 |
| Listing样本数(TOP100) / 品牌集中度 | 0.628 |
| Listing样本数(TOP100) / 卖家集中度 | 0.642 |
| Listing样本数(TOP100) / 商品总数 | 648.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.5619 |
| Listing样本数(TOP100) / 平均体积(in³) | 170.0634 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.77 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 59.0% |
| 头部Listing数(TOP10) / 月均销量 | 432.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 8159.0 |
| 头部Listing数(TOP10) / 平均BSR | 30653.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 144.0 |
| 新品(半年内上架) / 月均销售额($) | 2161.0 |
| 新品(半年内上架) / 平均价格($) | 17.39 |
| 新品(半年内上架) / 平均评分数 | 22.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.080662005 |
| 所有Listing(半年内) / 同类目退货率 | 0.070356004 |
| 所有Listing(半年内) / 搜索购买比 | 10.65599 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12026 |

### Gutters (排水沟)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Gutters |
| Listing样本数(TOP100) / 细分市场(翻译) | 排水沟 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Building Supplies:Building Materials:Roofing:Gutters & Accessories:Gutters |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：82 <br> 卖家：82 |
| Listing样本数(TOP100) / 月总销量 | 15742.0 |
| Listing样本数(TOP100) / 月均销量 | 157.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3954.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.76 |
| Listing样本数(TOP100) / 平均评分数 | 136.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 152528.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 78%  <br> AMZ: 5%  <br> FBM: 9% |
| Listing样本数(TOP100) / 商品集中度 | 0.481 |
| Listing样本数(TOP100) / 品牌集中度 | 0.532 |
| Listing样本数(TOP100) / 卖家集中度 | 0.55 |
| Listing样本数(TOP100) / 商品总数 | 698.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.7514 |
| Listing样本数(TOP100) / 平均体积(in³) | 444.2394 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.68 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 67.0% |
| 头部Listing数(TOP10) / 月均销量 | 756.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 18968.0 |
| 头部Listing数(TOP10) / 平均BSR | 57918.0 |
| 新品(半年内上架) / 新品数量 | 35.0 |
| 新品(半年内上架) / 新品占比 | 0.35 |
| 新品(半年内上架) / 月均销量 | 100.0 |
| 新品(半年内上架) / 月均销售额($) | 2693.0 |
| 新品(半年内上架) / 平均价格($) | 25.97 |
| 新品(半年内上架) / 平均评分数 | 14.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.050187003 |
| 所有Listing(半年内) / 同类目退货率 | 0.035314 |
| 所有Listing(半年内) / 搜索购买比 | 10.69917 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09945 |

### Fuel System (燃油系统)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Fuel System |
| Listing样本数(TOP100) / 细分市场(翻译) | 燃油系统 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Replacement Parts:Fuel System |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：89 <br> 卖家：86 |
| Listing样本数(TOP100) / 月总销量 | 15558.0 |
| Listing样本数(TOP100) / 月均销量 | 155.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2957.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.65 |
| Listing样本数(TOP100) / 平均评分数 | 98.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 174021.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 90%  <br> AMZ: 5%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.495 |
| Listing样本数(TOP100) / 品牌集中度 | 0.495 |
| Listing样本数(TOP100) / 卖家集中度 | 0.516 |
| Listing样本数(TOP100) / 商品总数 | 60821.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6486 |
| Listing样本数(TOP100) / 平均体积(in³) | 175.9119 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.74 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 76.0% |
| 头部Listing数(TOP10) / 月均销量 | 769.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 12492.0 |
| 头部Listing数(TOP10) / 平均BSR | 12949.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 104.0 |
| 新品(半年内上架) / 月均销售额($) | 2835.0 |
| 新品(半年内上架) / 平均价格($) | 29.57 |
| 新品(半年内上架) / 平均评分数 | 5.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.043139 |
| 所有Listing(半年内) / 同类目退货率 | 0.067567 |
| 所有Listing(半年内) / 搜索购买比 | 12.28586 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.076230004 |

### Car Rack Parts & Accessories (汽车货架零件和配件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Car Rack Parts & Accessories |
| Listing样本数(TOP100) / 细分市场(翻译) | 汽车货架零件和配件 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Outdoor Recreation:Accessories:Car Racks & Carriers:Car Rack Parts & Accessories |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：80 |
| Listing样本数(TOP100) / 月总销量 | 15481.0 |
| Listing样本数(TOP100) / 月均销量 | 154.0 |
| Listing样本数(TOP100) / 月均销售额($) | 6436.0 |
| Listing样本数(TOP100) / 平均价格($) | 45.21 |
| Listing样本数(TOP100) / 平均评分数 | 240.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 92676.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.4 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 71%  <br> AMZ: 10%  <br> FBM: 14% |
| Listing样本数(TOP100) / 商品集中度 | 0.321 |
| Listing样本数(TOP100) / 品牌集中度 | 0.469 |
| Listing样本数(TOP100) / 卖家集中度 | 0.437 |
| Listing样本数(TOP100) / 商品总数 | 1003.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3273 |
| Listing样本数(TOP100) / 平均体积(in³) | 470.0701 |
| Listing样本数(TOP100) / 平均毛利率 | 0.64 |
| Listing样本数(TOP100) / A+占比 | 0.64 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 51.0% |
| 头部Listing数(TOP10) / 月均销量 | 497.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 18653.0 |
| 头部Listing数(TOP10) / 平均BSR | 20150.0 |
| 新品(半年内上架) / 新品数量 | 14.0 |
| 新品(半年内上架) / 新品占比 | 0.14 |
| 新品(半年内上架) / 月均销量 | 147.0 |
| 新品(半年内上架) / 月均销售额($) | 3939.0 |
| 新品(半年内上架) / 平均价格($) | 33.6 |
| 新品(半年内上架) / 平均评分数 | 7.0 |
| 新品(半年内上架) / 平均星级 | 3.8 |
| 所有Listing(半年内) / 退货率 | 0.067189 |
| 所有Listing(半年内) / 同类目退货率 | 0.038714003 |
| 所有Listing(半年内) / 搜索购买比 | 6.6665 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.092889994 |

### Candleholder Sets (烛台套装)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Candleholder Sets |
| Listing样本数(TOP100) / 细分市场(翻译) | 烛台套装 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Candles & Holders:Candleholders:Candleholder Sets |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：83 <br> 卖家：79 |
| Listing样本数(TOP100) / 月总销量 | 15455.0 |
| Listing样本数(TOP100) / 月均销量 | 154.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4644.0 |
| Listing样本数(TOP100) / 平均价格($) | 30.23 |
| Listing样本数(TOP100) / 平均评分数 | 354.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 333905.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 7%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.271 |
| Listing样本数(TOP100) / 品牌集中度 | 0.332 |
| Listing样本数(TOP100) / 卖家集中度 | 0.378 |
| Listing样本数(TOP100) / 商品总数 | 1067.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.2481 |
| Listing样本数(TOP100) / 平均体积(in³) | 141.9992 |
| Listing样本数(TOP100) / 平均毛利率 | 0.6 |
| Listing样本数(TOP100) / A+占比 | 0.73 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 419.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 12511.0 |
| 头部Listing数(TOP10) / 平均BSR | 88617.0 |
| 新品(半年内上架) / 新品数量 | 28.0 |
| 新品(半年内上架) / 新品占比 | 0.28 |
| 新品(半年内上架) / 月均销量 | 133.0 |
| 新品(半年内上架) / 月均销售额($) | 2479.0 |
| 新品(半年内上架) / 平均价格($) | 20.91 |
| 新品(半年内上架) / 平均评分数 | 20.0 |
| 新品(半年内上架) / 平均星级 | 4.0 |
| 所有Listing(半年内) / 退货率 | 0.116616 |
| 所有Listing(半年内) / 同类目退货率 | 0.084172 |
| 所有Listing(半年内) / 搜索购买比 | 4.25897 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05765 |

### Digital Media Receivers (数字媒体接收器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Digital Media Receivers |
| Listing样本数(TOP100) / 细分市场(翻译) | 数字媒体接收器 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Car & Vehicle Electronics:Car Electronics:Car Audio:Digital Media Receivers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：73 <br> 卖家：72 |
| Listing样本数(TOP100) / 月总销量 | 15305.0 |
| Listing样本数(TOP100) / 月均销量 | 153.0 |
| Listing样本数(TOP100) / 月均销售额($) | 16092.0 |
| Listing样本数(TOP100) / 平均价格($) | 157.23 |
| Listing样本数(TOP100) / 平均评分数 | 143.0 |
| Listing样本数(TOP100) / 平均星级 | 4.1 |
| Listing样本数(TOP100) / 平均BSR | 41896.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 88%  <br> AMZ: 0%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.433 |
| Listing样本数(TOP100) / 品牌集中度 | 0.585 |
| Listing样本数(TOP100) / 卖家集中度 | 0.573 |
| Listing样本数(TOP100) / 商品总数 | 1247.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.9583 |
| Listing样本数(TOP100) / 平均体积(in³) | 418.1743 |
| Listing样本数(TOP100) / 平均毛利率 | 0.85 |
| Listing样本数(TOP100) / A+占比 | 0.88 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 67.0% |
| 头部Listing数(TOP10) / 月均销量 | 663.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 36138.0 |
| 头部Listing数(TOP10) / 平均BSR | 12099.0 |
| 新品(半年内上架) / 新品数量 | 33.0 |
| 新品(半年内上架) / 新品占比 | 0.33 |
| 新品(半年内上架) / 月均销量 | 143.0 |
| 新品(半年内上架) / 月均销售额($) | 13247.0 |
| 新品(半年内上架) / 平均价格($) | 109.5 |
| 新品(半年内上架) / 平均评分数 | 48.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.19026199 |
| 所有Listing(半年内) / 同类目退货率 | 0.143941 |
| 所有Listing(半年内) / 搜索购买比 | 2.31932 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.022839999 |

### Serveware (碗碟)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Serveware |
| Listing样本数(TOP100) / 细分市场(翻译) | 碗碟 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Dining & Entertaining:Novelty:Serveware |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：86 <br> 卖家：85 |
| Listing样本数(TOP100) / 月总销量 | 14774.0 |
| Listing样本数(TOP100) / 月均销量 | 147.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3201.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.08 |
| Listing样本数(TOP100) / 平均评分数 | 429.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 123797.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 84%  <br> AMZ: 5%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.527 |
| Listing样本数(TOP100) / 品牌集中度 | 0.577 |
| Listing样本数(TOP100) / 卖家集中度 | 0.58 |
| Listing样本数(TOP100) / 商品总数 | 512.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.4948 |
| Listing样本数(TOP100) / 平均体积(in³) | 316.5735 |
| Listing样本数(TOP100) / 平均毛利率 | 0.56 |
| Listing样本数(TOP100) / A+占比 | 0.58 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 58.0% |
| 头部Listing数(TOP10) / 月均销量 | 778.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 15844.0 |
| 头部Listing数(TOP10) / 平均BSR | 15477.0 |
| 新品(半年内上架) / 新品数量 | 37.0 |
| 新品(半年内上架) / 新品占比 | 0.37 |
| 新品(半年内上架) / 月均销量 | 107.0 |
| 新品(半年内上架) / 月均销售额($) | 2392.0 |
| 新品(半年内上架) / 平均价格($) | 24.01 |
| 新品(半年内上架) / 平均评分数 | 9.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.053335 |
| 所有Listing(半年内) / 同类目退货率 | 0.050301 |
| 所有Listing(半年内) / 搜索购买比 | 6.64098 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.085200004 |

### Breast Pump Carrying Bags (奶泵携带包)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Breast Pump Carrying Bags |
| Listing样本数(TOP100) / 细分市场(翻译) | 奶泵携带包 |
| Listing样本数(TOP100) / 市场路径 | Baby Products:Feeding:Breastfeeding:Breast Pump Carrying Bags |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：58 <br> 卖家：60 |
| Listing样本数(TOP100) / 月总销量 | 14543.0 |
| Listing样本数(TOP100) / 月均销量 | 145.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4705.0 |
| Listing样本数(TOP100) / 平均价格($) | 36.5 |
| Listing样本数(TOP100) / 平均评分数 | 154.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 27900.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 3%  <br> FBM: 0% |
| Listing样本数(TOP100) / 商品集中度 | 0.51 |
| Listing样本数(TOP100) / 品牌集中度 | 0.586 |
| Listing样本数(TOP100) / 卖家集中度 | 0.586 |
| Listing样本数(TOP100) / 商品总数 | 155.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.2332 |
| Listing样本数(TOP100) / 平均体积(in³) | 688.8293 |
| Listing样本数(TOP100) / 平均毛利率 | 0.62 |
| Listing样本数(TOP100) / A+占比 | 0.91 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 741.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 24010.0 |
| 头部Listing数(TOP10) / 平均BSR | 6449.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 152.0 |
| 新品(半年内上架) / 月均销售额($) | 4302.0 |
| 新品(半年内上架) / 平均价格($) | 28.34 |
| 新品(半年内上架) / 平均评分数 | 46.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.091712 |
| 所有Listing(半年内) / 同类目退货率 | 0.053469 |
| 所有Listing(半年内) / 搜索购买比 | 5.26499 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0777 |

### Collectible Vehicles (交通工具摆件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Collectible Vehicles |
| Listing样本数(TOP100) / 细分市场(翻译) | 交通工具摆件 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Home Décor Products:Home Décor Accents:Collectible Vehicles |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：76 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 14539.0 |
| Listing样本数(TOP100) / 月均销量 | 145.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2575.0 |
| Listing样本数(TOP100) / 平均价格($) | 23.98 |
| Listing样本数(TOP100) / 平均评分数 | 213.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 411008.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 92%  <br> AMZ: 2%  <br> FBM: 4% |
| Listing样本数(TOP100) / 商品集中度 | 0.52 |
| Listing样本数(TOP100) / 品牌集中度 | 0.637 |
| Listing样本数(TOP100) / 卖家集中度 | 0.648 |
| Listing样本数(TOP100) / 商品总数 | 840.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.8947 |
| Listing样本数(TOP100) / 平均体积(in³) | 165.9766 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.68 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 83.0% |
| 头部Listing数(TOP10) / 月均销量 | 756.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 9538.0 |
| 头部Listing数(TOP10) / 平均BSR | 77265.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 184.0 |
| 新品(半年内上架) / 月均销售额($) | 2949.0 |
| 新品(半年内上架) / 平均价格($) | 17.47 |
| 新品(半年内上架) / 平均评分数 | 33.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.058077 |
| 所有Listing(半年内) / 同类目退货率 | 0.050387003 |
| 所有Listing(半年内) / 搜索购买比 | 4.22353 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09386 |

### 3D Printer Extruders (3D打印机挤出机)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | 3D Printer Extruders |
| Listing样本数(TOP100) / 细分市场(翻译) | 3D打印机挤出机 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Additive Manufacturing Products:3D Printer Parts & Accessories:3D Printer Extruders |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：41 <br> 卖家：46 |
| Listing样本数(TOP100) / 月总销量 | 13613.0 |
| Listing样本数(TOP100) / 月均销量 | 136.0 |
| Listing样本数(TOP100) / 月均销售额($) | 4012.0 |
| Listing样本数(TOP100) / 平均价格($) | 27.77 |
| Listing样本数(TOP100) / 平均评分数 | 157.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 65048.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 93%  <br> AMZ: 2%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.295 |
| Listing样本数(TOP100) / 品牌集中度 | 0.587 |
| Listing样本数(TOP100) / 卖家集中度 | 0.553 |
| Listing样本数(TOP100) / 商品总数 | 802.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.1814 |
| Listing样本数(TOP100) / 平均体积(in³) | 18.6019 |
| Listing样本数(TOP100) / 平均毛利率 | 0.69 |
| Listing样本数(TOP100) / A+占比 | 0.66 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 80.0% |
| 头部Listing数(TOP10) / 月均销量 | 401.0 |
| 头部Listing数(TOP10) / 垄断度 | 2.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 12728.0 |
| 头部Listing数(TOP10) / 平均BSR | 13717.0 |
| 新品(半年内上架) / 新品数量 | 41.0 |
| 新品(半年内上架) / 新品占比 | 0.41 |
| 新品(半年内上架) / 月均销量 | 129.0 |
| 新品(半年内上架) / 月均销售额($) | 4002.0 |
| 新品(半年内上架) / 平均价格($) | 33.91 |
| 新品(半年内上架) / 平均评分数 | 22.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.049936 |
| 所有Listing(半年内) / 同类目退货率 | 0.049794998 |
| 所有Listing(半年内) / 搜索购买比 | 8.83752 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.115380004 |

### Mailbox Hardware (信箱硬件)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Mailbox Hardware |
| Listing样本数(TOP100) / 细分市场(翻译) | 信箱硬件 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Hardware:Mailboxes & Accessories:Mailbox Accessories & Hardware:Mailbox Hardware |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：71 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 13464.0 |
| Listing样本数(TOP100) / 月均销量 | 134.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2414.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.44 |
| Listing样本数(TOP100) / 平均评分数 | 201.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 166859.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 6%  <br> FBM: 6% |
| Listing样本数(TOP100) / 商品集中度 | 0.467 |
| Listing样本数(TOP100) / 品牌集中度 | 0.555 |
| Listing样本数(TOP100) / 卖家集中度 | 0.544 |
| Listing样本数(TOP100) / 商品总数 | 274.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.1111 |
| Listing样本数(TOP100) / 平均体积(in³) | 119.144 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.49 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 65.0% |
| 头部Listing数(TOP10) / 月均销量 | 628.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 8144.0 |
| 头部Listing数(TOP10) / 平均BSR | 28155.0 |
| 新品(半年内上架) / 新品数量 | 26.0 |
| 新品(半年内上架) / 新品占比 | 0.26 |
| 新品(半年内上架) / 月均销量 | 75.0 |
| 新品(半年内上架) / 月均销售额($) | 1486.0 |
| 新品(半年内上架) / 平均价格($) | 21.61 |
| 新品(半年内上架) / 平均评分数 | 13.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.076511 |
| 所有Listing(半年内) / 同类目退货率 | 0.070356004 |
| 所有Listing(半年内) / 搜索购买比 | 14.36528 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.12026 |

### Night Vision Binoculars & Goggles (夜视双筒望远镜和护目镜)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Night Vision Binoculars & Goggles |
| Listing样本数(TOP100) / 细分市场(翻译) | 夜视双筒望远镜和护目镜 |
| Listing样本数(TOP100) / 市场路径 | Sports & Outdoors:Hunting & Fishing:Shooting:Optics:Night Vision:Night Vision Binoculars & Goggles |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：74 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 13374.0 |
| Listing样本数(TOP100) / 月均销量 | 133.0 |
| Listing样本数(TOP100) / 月均销售额($) | 12879.0 |
| Listing样本数(TOP100) / 平均价格($) | 99.79 |
| Listing样本数(TOP100) / 平均评分数 | 238.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 117788.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 81%  <br> AMZ: 2%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.469 |
| Listing样本数(TOP100) / 品牌集中度 | 0.549 |
| Listing样本数(TOP100) / 卖家集中度 | 0.564 |
| Listing样本数(TOP100) / 商品总数 | 412.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.3421 |
| Listing样本数(TOP100) / 平均体积(in³) | 147.9124 |
| Listing样本数(TOP100) / 平均毛利率 | 0.76 |
| Listing样本数(TOP100) / A+占比 | 0.86 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 626.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 46581.0 |
| 头部Listing数(TOP10) / 平均BSR | 22335.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 186.0 |
| 新品(半年内上架) / 月均销售额($) | 18855.0 |
| 新品(半年内上架) / 平均价格($) | 117.59 |
| 新品(半年内上架) / 平均评分数 | 131.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.15598899 |
| 所有Listing(半年内) / 同类目退货率 | 0.045063 |
| 所有Listing(半年内) / 搜索购买比 | 1.90393 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.07428 |

### Grill Lighting (点火器)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Grill Lighting |
| Listing样本数(TOP100) / 细分市场(翻译) | 点火器 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Grills & Outdoor Cooking:Outdoor Cooking Tools & Accessories:Grill Lighting |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：81 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 13285.0 |
| Listing样本数(TOP100) / 月均销量 | 132.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3537.0 |
| Listing样本数(TOP100) / 平均价格($) | 37.59 |
| Listing样本数(TOP100) / 平均评分数 | 607.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 138405.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 83%  <br> AMZ: 7%  <br> FBM: 5% |
| Listing样本数(TOP100) / 商品集中度 | 0.475 |
| Listing样本数(TOP100) / 品牌集中度 | 0.539 |
| Listing样本数(TOP100) / 卖家集中度 | 0.549 |
| Listing样本数(TOP100) / 商品总数 | 301.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.2916 |
| Listing样本数(TOP100) / 平均体积(in³) | 233.9064 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.83 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 58.0% |
| 头部Listing数(TOP10) / 月均销量 | 631.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 15369.0 |
| 头部Listing数(TOP10) / 平均BSR | 23155.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 61.0 |
| 新品(半年内上架) / 月均销售额($) | 1984.0 |
| 新品(半年内上架) / 平均价格($) | 39.94 |
| 新品(半年内上架) / 平均评分数 | 20.0 |
| 新品(半年内上架) / 平均星级 | 4.5 |
| 所有Listing(半年内) / 退货率 | 0.054316 |
| 所有Listing(半年内) / 同类目退货率 | 0.062280003 |
| 所有Listing(半年内) / 搜索购买比 | 6.2651 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.05408 |

### Fuel (燃油表)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Fuel |
| Listing样本数(TOP100) / 细分市场(翻译) | 燃油表 |
| Listing样本数(TOP100) / 市场路径 | Automotive:Replacement Parts:Lighting & Electrical:Electrical:Gauges:Fuel |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 13179.0 |
| Listing样本数(TOP100) / 月均销量 | 131.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3519.0 |
| Listing样本数(TOP100) / 平均价格($) | 31.69 |
| Listing样本数(TOP100) / 平均评分数 | 107.0 |
| Listing样本数(TOP100) / 平均星级 | 4.2 |
| Listing样本数(TOP100) / 平均BSR | 160533.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.5 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 62%  <br> AMZ: 4%  <br> FBM: 10% |
| Listing样本数(TOP100) / 商品集中度 | 0.466 |
| Listing样本数(TOP100) / 品牌集中度 | 0.513 |
| Listing样本数(TOP100) / 卖家集中度 | 0.517 |
| Listing样本数(TOP100) / 商品总数 | 690.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.3818 |
| Listing样本数(TOP100) / 平均体积(in³) | 62.5127 |
| Listing样本数(TOP100) / 平均毛利率 | 0.65 |
| Listing样本数(TOP100) / A+占比 | 0.66 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 68.0% |
| 头部Listing数(TOP10) / 月均销量 | 613.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 13747.0 |
| 头部Listing数(TOP10) / 平均BSR | 23842.0 |
| 新品(半年内上架) / 新品数量 | 18.0 |
| 新品(半年内上架) / 新品占比 | 0.18 |
| 新品(半年内上架) / 月均销量 | 215.0 |
| 新品(半年内上架) / 月均销售额($) | 3292.0 |
| 新品(半年内上架) / 平均价格($) | 20.79 |
| 新品(半年内上架) / 平均评分数 | 5.0 |
| 新品(半年内上架) / 平均星级 | 3.9 |
| 所有Listing(半年内) / 退货率 | 0.048652 |
| 所有Listing(半年内) / 同类目退货率 | 0.040142003 |
| 所有Listing(半年内) / 搜索购买比 | 8.20823 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.098000005 |

### Deviled Egg Plates (咸蛋盘)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Deviled Egg Plates |
| Listing样本数(TOP100) / 细分市场(翻译) | 咸蛋盘 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Dining & Entertaining:Dinnerware & Serveware:Dinnerware:Plates:Specialty Plates:Deviled Egg Plates |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：82 <br> 卖家：77 |
| Listing样本数(TOP100) / 月总销量 | 13115.0 |
| Listing样本数(TOP100) / 月均销量 | 131.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2795.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.0 |
| Listing样本数(TOP100) / 平均评分数 | 349.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 130495.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.8 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 87%  <br> AMZ: 6%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.528 |
| Listing样本数(TOP100) / 品牌集中度 | 0.591 |
| Listing样本数(TOP100) / 卖家集中度 | 0.606 |
| Listing样本数(TOP100) / 商品总数 | 303.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.8687 |
| Listing样本数(TOP100) / 平均体积(in³) | 325.6678 |
| Listing样本数(TOP100) / 平均毛利率 | 0.51 |
| Listing样本数(TOP100) / A+占比 | 0.78 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 61.0% |
| 头部Listing数(TOP10) / 月均销量 | 692.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 14522.0 |
| 头部Listing数(TOP10) / 平均BSR | 22517.0 |
| 新品(半年内上架) / 新品数量 | 28.0 |
| 新品(半年内上架) / 新品占比 | 0.28 |
| 新品(半年内上架) / 月均销量 | 86.0 |
| 新品(半年内上架) / 月均销售额($) | 2049.0 |
| 新品(半年内上架) / 平均价格($) | 23.97 |
| 新品(半年内上架) / 平均评分数 | 29.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.050064996 |
| 所有Listing(半年内) / 同类目退货率 | 0.035328 |
| 所有Listing(半年内) / 搜索购买比 | 7.68335 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.122729994 |

### Masonry Chisels (砌筑用凿子)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Masonry Chisels |
| Listing样本数(TOP100) / 细分市场(翻译) | 砌筑用凿子 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Power & Hand Tools:Hand Tools:Chisels:Masonry Chisels |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：70 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 13053.0 |
| Listing样本数(TOP100) / 月均销量 | 130.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3124.0 |
| Listing样本数(TOP100) / 平均价格($) | 26.8 |
| Listing样本数(TOP100) / 平均评分数 | 246.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 179350.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 75%  <br> AMZ: 15%  <br> FBM: 1% |
| Listing样本数(TOP100) / 商品集中度 | 0.401 |
| Listing样本数(TOP100) / 品牌集中度 | 0.498 |
| Listing样本数(TOP100) / 卖家集中度 | 0.624 |
| Listing样本数(TOP100) / 商品总数 | 357.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.6329 |
| Listing样本数(TOP100) / 平均体积(in³) | 81.4154 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.71 |
| Listing样本数(TOP100) / 卖家所属地 | 美国 <br> 47.0% |
| 头部Listing数(TOP10) / 月均销量 | 523.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 9847.0 |
| 头部Listing数(TOP10) / 平均BSR | 31239.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 80.0 |
| 新品(半年内上架) / 月均销售额($) | 1491.0 |
| 新品(半年内上架) / 平均价格($) | 16.86 |
| 新品(半年内上架) / 平均评分数 | 12.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.038862 |
| 所有Listing(半年内) / 同类目退货率 | 0.030409 |
| 所有Listing(半年内) / 搜索购买比 | 9.66844 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.08355 |

### Aprons (围裙)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Aprons |
| Listing样本数(TOP100) / 细分市场(翻译) | 围裙 |
| Listing样本数(TOP100) / 市场路径 | Patio, Lawn & Garden:Gardening & Lawn Care:Gloves & Protective Gear:Aprons |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：80 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 12747.0 |
| Listing样本数(TOP100) / 月均销量 | 127.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3279.0 |
| Listing样本数(TOP100) / 平均价格($) | 22.0 |
| Listing样本数(TOP100) / 平均评分数 | 72.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 212750.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 77%  <br> AMZ: 8%  <br> FBM: 11% |
| Listing样本数(TOP100) / 商品集中度 | 0.519 |
| Listing样本数(TOP100) / 品牌集中度 | 0.588 |
| Listing样本数(TOP100) / 卖家集中度 | 0.589 |
| Listing样本数(TOP100) / 商品总数 | 171.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7518 |
| Listing样本数(TOP100) / 平均体积(in³) | 254.9572 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.76 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 77.0% |
| 头部Listing数(TOP10) / 月均销量 | 661.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 18888.0 |
| 头部Listing数(TOP10) / 平均BSR | 41194.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 78.0 |
| 新品(半年内上架) / 月均销售额($) | 2215.0 |
| 新品(半年内上架) / 平均价格($) | 26.55 |
| 新品(半年内上架) / 平均评分数 | 6.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.03039 |
| 所有Listing(半年内) / 同类目退货率 | 0.047964 |
| 所有Listing(半年内) / 搜索购买比 | 8.44775 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.080469996 |

### Nail Pullers (羊角起钉钳)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Nail Pullers |
| Listing样本数(TOP100) / 细分市场(翻译) | 羊角起钉钳 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Power & Hand Tools:Hand Tools:Nail Pullers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：78 <br> 卖家：73 |
| Listing样本数(TOP100) / 月总销量 | 12692.0 |
| Listing样本数(TOP100) / 月均销量 | 126.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2369.0 |
| Listing样本数(TOP100) / 平均价格($) | 24.2 |
| Listing样本数(TOP100) / 平均评分数 | 371.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 191406.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.7 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 79%  <br> AMZ: 9%  <br> FBM: 3% |
| Listing样本数(TOP100) / 商品集中度 | 0.444 |
| Listing样本数(TOP100) / 品牌集中度 | 0.619 |
| Listing样本数(TOP100) / 卖家集中度 | 0.647 |
| Listing样本数(TOP100) / 商品总数 | 266.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 1.204 |
| Listing样本数(TOP100) / 平均体积(in³) | 75.789 |
| Listing样本数(TOP100) / 平均毛利率 | 0.55 |
| Listing样本数(TOP100) / A+占比 | 0.62 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 55.0% |
| 头部Listing数(TOP10) / 月均销量 | 563.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 7136.0 |
| 头部Listing数(TOP10) / 平均BSR | 36042.0 |
| 新品(半年内上架) / 新品数量 | 12.0 |
| 新品(半年内上架) / 新品占比 | 0.12 |
| 新品(半年内上架) / 月均销量 | 99.0 |
| 新品(半年内上架) / 月均销售额($) | 836.0 |
| 新品(半年内上架) / 平均价格($) | 10.91 |
| 新品(半年内上架) / 平均评分数 | 12.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.022732 |
| 所有Listing(半年内) / 同类目退货率 | 0.035314 |
| 所有Listing(半年内) / 搜索购买比 | 9.56538 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09945 |

### Cheese Knives (奶酪刀)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Cheese Knives |
| Listing样本数(TOP100) / 细分市场(翻译) | 奶酪刀 |
| Listing样本数(TOP100) / 市场路径 | Home & Kitchen:Kitchen & Dining:Kitchen Utensils & Gadgets:Kitchen Knives & Accessories:Specialty Knives:Cheese Knives |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：82 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 12550.0 |
| Listing样本数(TOP100) / 月均销量 | 125.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2095.0 |
| Listing样本数(TOP100) / 平均价格($) | 21.33 |
| Listing样本数(TOP100) / 平均评分数 | 542.0 |
| Listing样本数(TOP100) / 平均星级 | 4.5 |
| Listing样本数(TOP100) / 平均BSR | 104638.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 79%  <br> AMZ: 11%  <br> FBM: 2% |
| Listing样本数(TOP100) / 商品集中度 | 0.433 |
| Listing样本数(TOP100) / 品牌集中度 | 0.476 |
| Listing样本数(TOP100) / 卖家集中度 | 0.547 |
| Listing样本数(TOP100) / 商品总数 | 490.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.647 |
| Listing样本数(TOP100) / 平均体积(in³) | 81.7627 |
| Listing样本数(TOP100) / 平均毛利率 | 0.57 |
| Listing样本数(TOP100) / A+占比 | 0.66 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 48.0% |
| 头部Listing数(TOP10) / 月均销量 | 543.0 |
| 头部Listing数(TOP10) / 垄断度 | 4.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 6451.0 |
| 头部Listing数(TOP10) / 平均BSR | 23257.0 |
| 新品(半年内上架) / 新品数量 | 10.0 |
| 新品(半年内上架) / 新品占比 | 0.1 |
| 新品(半年内上架) / 月均销量 | 61.0 |
| 新品(半年内上架) / 月均销售额($) | 915.0 |
| 新品(半年内上架) / 平均价格($) | 17.45 |
| 新品(半年内上架) / 平均评分数 | 38.0 |
| 新品(半年内上架) / 平均星级 | 4.4 |
| 所有Listing(半年内) / 退货率 | 0.040209997 |
| 所有Listing(半年内) / 同类目退货率 | 0.02952 |
| 所有Listing(半年内) / 搜索购买比 | 8.3324 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.0692 |

### Angle (角规)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Angle |
| Listing样本数(TOP100) / 细分市场(翻译) | 角规 |
| Listing样本数(TOP100) / 市场路径 | Industrial & Scientific:Test, Measure & Inspect:Dimensional Measurement:Gauges:Angle |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：82 <br> 卖家：84 |
| Listing样本数(TOP100) / 月总销量 | 12544.0 |
| Listing样本数(TOP100) / 月均销量 | 125.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2378.0 |
| Listing样本数(TOP100) / 平均价格($) | 25.14 |
| Listing样本数(TOP100) / 平均评分数 | 386.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 99452.0 |
| Listing样本数(TOP100) / 平均卖家数 | 2.0 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 79%  <br> AMZ: 8%  <br> FBM: 8% |
| Listing样本数(TOP100) / 商品集中度 | 0.551 |
| Listing样本数(TOP100) / 品牌集中度 | 0.606 |
| Listing样本数(TOP100) / 卖家集中度 | 0.624 |
| Listing样本数(TOP100) / 商品总数 | 504.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.5578 |
| Listing样本数(TOP100) / 平均体积(in³) | 27.8457 |
| Listing样本数(TOP100) / 平均毛利率 | 0.66 |
| Listing样本数(TOP100) / A+占比 | 0.72 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 64.0% |
| 头部Listing数(TOP10) / 月均销量 | 691.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 11737.0 |
| 头部Listing数(TOP10) / 平均BSR | 11022.0 |
| 新品(半年内上架) / 新品数量 | 15.0 |
| 新品(半年内上架) / 新品占比 | 0.15 |
| 新品(半年内上架) / 月均销量 | 59.0 |
| 新品(半年内上架) / 月均销售额($) | 1359.0 |
| 新品(半年内上架) / 平均价格($) | 21.46 |
| 新品(半年内上架) / 平均评分数 | 24.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.028968 |
| 所有Listing(半年内) / 同类目退货率 | 0.054436997 |
| 所有Listing(半年内) / 搜索购买比 | 11.41902 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.10694 |

### In-Dash DVD & Video Receivers (仪表盘视频)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | In-Dash DVD & Video Receivers |
| Listing样本数(TOP100) / 细分市场(翻译) | 仪表盘视频 |
| Listing样本数(TOP100) / 市场路径 | Electronics:Car & Vehicle Electronics:Car Electronics:Car Video:In-Dash DVD & Video Receivers |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：82 |
| Listing样本数(TOP100) / 月总销量 | 12492.0 |
| Listing样本数(TOP100) / 月均销量 | 124.0 |
| Listing样本数(TOP100) / 月均销售额($) | 14899.0 |
| Listing样本数(TOP100) / 平均价格($) | 150.46 |
| Listing样本数(TOP100) / 平均评分数 | 189.0 |
| Listing样本数(TOP100) / 平均星级 | 4.0 |
| Listing样本数(TOP100) / 平均BSR | 59098.0 |
| Listing样本数(TOP100) / 平均卖家数 | 3.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 75%  <br> AMZ: 1%  <br> FBM: 15% |
| Listing样本数(TOP100) / 商品集中度 | 0.552 |
| Listing样本数(TOP100) / 品牌集中度 | 0.6 |
| Listing样本数(TOP100) / 卖家集中度 | 0.58 |
| Listing样本数(TOP100) / 商品总数 | 344.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 2.7385 |
| Listing样本数(TOP100) / 平均体积(in³) | 375.6274 |
| Listing样本数(TOP100) / 平均毛利率 | 0.85 |
| Listing样本数(TOP100) / A+占比 | 0.87 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 60.0% |
| 头部Listing数(TOP10) / 月均销量 | 690.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 71019.0 |
| 头部Listing数(TOP10) / 平均BSR | 8401.0 |
| 新品(半年内上架) / 新品数量 | 17.0 |
| 新品(半年内上架) / 新品占比 | 0.17 |
| 新品(半年内上架) / 月均销量 | 83.0 |
| 新品(半年内上架) / 月均销售额($) | 8004.0 |
| 新品(半年内上架) / 平均价格($) | 105.71 |
| 新品(半年内上架) / 平均评分数 | 38.0 |
| 新品(半年内上架) / 平均星级 | 4.2 |
| 所有Listing(半年内) / 退货率 | 0.156541 |
| 所有Listing(半年内) / 同类目退货率 | 0.15377499 |
| 所有Listing(半年内) / 搜索购买比 | 2.51937 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.03101 |

### Card Playing (纸牌游戏)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Card Playing |
| Listing样本数(TOP100) / 细分市场(翻译) | 纸牌游戏 |
| Listing样本数(TOP100) / 市场路径 | Health & Household:Medical Supplies & Equipment:Mobility & Daily Living Aids:Low Strength Aids:Card Playing |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：75 <br> 卖家：78 |
| Listing样本数(TOP100) / 月总销量 | 12293.0 |
| Listing样本数(TOP100) / 月均销量 | 122.0 |
| Listing样本数(TOP100) / 月均销售额($) | 2236.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.06 |
| Listing样本数(TOP100) / 平均评分数 | 198.0 |
| Listing样本数(TOP100) / 平均星级 | 4.3 |
| Listing样本数(TOP100) / 平均BSR | 221826.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.1 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 75%  <br> AMZ: 2%  <br> FBM: 15% |
| Listing样本数(TOP100) / 商品集中度 | 0.497 |
| Listing样本数(TOP100) / 品牌集中度 | 0.589 |
| Listing样本数(TOP100) / 卖家集中度 | 0.589 |
| Listing样本数(TOP100) / 商品总数 | 149.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.7804 |
| Listing样本数(TOP100) / 平均体积(in³) | 76.9631 |
| Listing样本数(TOP100) / 平均毛利率 | 0.59 |
| Listing样本数(TOP100) / A+占比 | 0.61 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 73.0% |
| 头部Listing数(TOP10) / 月均销量 | 611.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 10365.0 |
| 头部Listing数(TOP10) / 平均BSR | 65089.0 |
| 新品(半年内上架) / 新品数量 | 42.0 |
| 新品(半年内上架) / 新品占比 | 0.42 |
| 新品(半年内上架) / 月均销量 | 100.0 |
| 新品(半年内上架) / 月均销售额($) | 2014.0 |
| 新品(半年内上架) / 平均价格($) | 20.55 |
| 新品(半年内上架) / 平均评分数 | 18.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.047792003 |
| 所有Listing(半年内) / 同类目退货率 | 0.027781999 |
| 所有Listing(半年内) / 搜索购买比 | 10.29684 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.15804 |

### Brazing Rods (钎杆)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Brazing Rods |
| Listing样本数(TOP100) / 细分市场(翻译) | 钎杆 |
| Listing样本数(TOP100) / 市场路径 | Tools & Home Improvement:Welding & Soldering:Soldering & Brazing Equipment:Solder & Flux:Brazing Rods |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：53 <br> 卖家：61 |
| Listing样本数(TOP100) / 月总销量 | 12263.0 |
| Listing样本数(TOP100) / 月均销量 | 122.0 |
| Listing样本数(TOP100) / 月均销售额($) | 3242.0 |
| Listing样本数(TOP100) / 平均价格($) | 37.36 |
| Listing样本数(TOP100) / 平均评分数 | 158.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 119697.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.9 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 61%  <br> AMZ: 3%  <br> FBM: 26% |
| Listing样本数(TOP100) / 商品集中度 | 0.547 |
| Listing样本数(TOP100) / 品牌集中度 | 0.627 |
| Listing样本数(TOP100) / 卖家集中度 | 0.614 |
| Listing样本数(TOP100) / 商品总数 | 294.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.6607 |
| Listing样本数(TOP100) / 平均体积(in³) | 24.8196 |
| Listing样本数(TOP100) / 平均毛利率 | 0.63 |
| Listing样本数(TOP100) / A+占比 | 0.59 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 53.0% |
| 头部Listing数(TOP10) / 月均销量 | 671.0 |
| 头部Listing数(TOP10) / 垄断度 | 5.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 17961.0 |
| 头部Listing数(TOP10) / 平均BSR | 17745.0 |
| 新品(半年内上架) / 新品数量 | 22.0 |
| 新品(半年内上架) / 新品占比 | 0.22 |
| 新品(半年内上架) / 月均销量 | 120.0 |
| 新品(半年内上架) / 月均销售额($) | 3281.0 |
| 新品(半年内上架) / 平均价格($) | 23.05 |
| 新品(半年内上架) / 平均评分数 | 17.0 |
| 新品(半年内上架) / 平均星级 | 4.1 |
| 所有Listing(半年内) / 退货率 | 0.020267999 |
| 所有Listing(半年内) / 同类目退货率 | 0.035314 |
| 所有Listing(半年内) / 搜索购买比 | 9.99121 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.09945 |

### Clothing (衣服)

| 字段 | 值 |
| :--- | :--- |
| Listing样本数(TOP100) / 细分市场 | Clothing |
| Listing样本数(TOP100) / 细分市场(翻译) | 衣服 |
| Listing样本数(TOP100) / 市场路径 | Toys & Games:Stuffed Animals & Plush Toys:Stuffed Animal Clothing & Accessories:Clothing |
| Listing样本数(TOP100) / 样本数量 | 商品：100 <br> 品牌：72 <br> 卖家：74 |
| Listing样本数(TOP100) / 月总销量 | 12068.0 |
| Listing样本数(TOP100) / 月均销量 | 120.0 |
| Listing样本数(TOP100) / 月均销售额($) | 1961.0 |
| Listing样本数(TOP100) / 平均价格($) | 20.7 |
| Listing样本数(TOP100) / 平均评分数 | 76.0 |
| Listing样本数(TOP100) / 平均星级 | 4.4 |
| Listing样本数(TOP100) / 平均BSR | 123504.0 |
| Listing样本数(TOP100) / 平均卖家数 | 1.6 |
| Listing样本数(TOP100) / 卖家类型 | FBA: 85%  <br> AMZ: 1%  <br> FBM: 12% |
| Listing样本数(TOP100) / 商品集中度 | 0.392 |
| Listing样本数(TOP100) / 品牌集中度 | 0.533 |
| Listing样本数(TOP100) / 卖家集中度 | 0.522 |
| Listing样本数(TOP100) / 商品总数 | 885.0 |
| Listing样本数(TOP100) / 平均重量(pounds) | 0.2856 |
| Listing样本数(TOP100) / 平均体积(in³) | 51.3246 |
| Listing样本数(TOP100) / 平均毛利率 | 0.58 |
| Listing样本数(TOP100) / A+占比 | 0.47 |
| Listing样本数(TOP100) / 卖家所属地 | 中国 <br> 74.0% |
| 头部Listing数(TOP10) / 月均销量 | 473.0 |
| 头部Listing数(TOP10) / 垄断度 | 3.0 |
| 头部Listing数(TOP10) / 月均销售额($) | 5916.0 |
| 头部Listing数(TOP10) / 平均BSR | 36444.0 |
| 新品(半年内上架) / 新品数量 | 20.0 |
| 新品(半年内上架) / 新品占比 | 0.2 |
| 新品(半年内上架) / 月均销量 | 101.0 |
| 新品(半年内上架) / 月均销售额($) | 1576.0 |
| 新品(半年内上架) / 平均价格($) | 19.1 |
| 新品(半年内上架) / 平均评分数 | 8.0 |
| 新品(半年内上架) / 平均星级 | 4.3 |
| 所有Listing(半年内) / 退货率 | 0.060521998 |
| 所有Listing(半年内) / 同类目退货率 | 0.041888 |
| 所有Listing(半年内) / 搜索购买比 | 4.0541 |
| 所有Listing(半年内) / 同类目搜索购买比 | 0.04645 |
