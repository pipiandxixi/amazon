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
