# 亚马逊选市场扫描与评估报告 (2026-06-09)

> [!IMPORTANT]
> 本报告基于配置文件 `scripts/market_config.json` 中设定的过滤与风控规则进行生成。今日共分析了 **250** 个符合基本条件的子类目，其中最终筛选出 **86** 个适合新手的 🟢 绿色推荐赛道。
> **数量审计**：当前候选类目有 153 个，超过目标上限 15。建议提高基础过滤门槛或收紧黄色/绿色风控规则，而不是截断为固定 Top-K。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **86** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **67** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **97** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Outdoor Statues** | 户外雕像 | $23.98 | 751 | 1.11 lbs | 2.98% | 40.6% | 75.0% |
| 2 | **Decorative Garden Stakes** | 装饰园艺桩 | $20.07 | 373 | 0.73 lbs | 2.04% | 55.5% | 90.0% |
| 3 | **Bread Knives** | 面包刀 | $22.34 | 772 | 0.94 lbs | 2.92% | 53.5% | 67.0% |
| 4 | **Shilajit** | Shilajit | $31.77 | 638 | 0.41 lbs | 0.34% | 62.2% | 40.0% |
| 5 | **Lighting Products** | 水底灯 | $50.99 | 476 | 1.71 lbs | 6.75% | 55.2% | 75.0% |
| 6 | **Decorative Boxes** | 装饰盒 | $24.55 | 676 | 1.61 lbs | 7.91% | 47.5% | 63.0% |
| 7 | **Nozzles** | 喷嘴 | $28.04 | 552 | 0.44 lbs | 2.63% | 55.7% | 73.0% |
| 8 | **Cayenne** | 辣椒 | $20.89 | 709 | 0.36 lbs | 0.32% | 58.6% | 54.0% |
| 9 | **Tap Extractors** | 分接抽水机 | $25.96 | 798 | 1.29 lbs | 4.89% | 59.4% | 73.0% |
| 10 | **Scissors & Shears** | 工业剪 | $23.92 | 773 | 0.88 lbs | 2.68% | 55.9% | 48.0% |
| 11 | **Herb & Spice Mills** | 草本植物 | $22.79 | 747 | 0.57 lbs | 3.55% | 56.3% | 56.0% |
| 12 | **Bladder Control Devices** | 膀胱控制设备 | $30.82 | 515 | 0.57 lbs | 3.9% | 46.7% | 60.0% |
| 13 | **Chocolate Drink Mixes** | 巧克力饮料混合物 | $26.45 | 735 | 1.83 lbs | 0.21% | 65.0% | 13.0% |
| 14 | **Weather Stripping** | 挡风雨条 | $22.85 | 523 | 1.66 lbs | 6.26% | 42.8% | 90.0% |
| 15 | **Plaques & Wall Art** | 装饰墙 | $20.45 | 594 | 1.04 lbs | 2.89% | 47.1% | 86.0% |
| 16 | **Brake System Bleeding Tools** | 刹车排气 | $26.18 | 421 | 1.48 lbs | 4.69% | 49.4% | 83.0% |
| 17 | **Nozzles** | 喷嘴 | $20.16 | 200 | 0.31 lbs | 1.98% | 59.6% | 64.0% |
| 18 | **Feeders** | 喂食器 | $26.31 | 448 | 1.26 lbs | 5.44% | 37.4% | 80.0% |
| 19 | **Toilet Spare Parts** | 马桶配件 | $21.10 | 534 | 0.39 lbs | 4.02% | 60.0% | 62.0% |
| 20 | **Electrical System Tools** | 电气系统工具 | $31.78 | 442 | 1.00 lbs | 2.38% | 42.2% | 72.0% |
| 21 | **Trophies** | 奖杯 | $25.00 | 296 | 0.95 lbs | 2.59% | 46.8% | 51.0% |
| 22 | **Diamond Blades** | 钻石刀片 | $20.43 | 531 | 0.75 lbs | 2.39% | 57.2% | 74.0% |
| 23 | **Smokeless Inhalers** | 无烟吸入器 | $20.87 | 385 | 0.14 lbs | 2.22% | 62.3% | 41.0% |
| 24 | **Desk & Shelf Clocks** | 台钟和座钟 | $38.40 | 727 | 1.50 lbs | 7.44% | 62.3% | 69.0% |
| 25 | **Oolong** | 乌龙 | $20.90 | 447 | 0.46 lbs | 0.26% | 60.9% | 53.0% |
| 26 | **Locks** | 锁具 | $44.51 | 639 | 1.72 lbs | 5.73% | 59.8% | 69.0% |
| 27 | **Insulin Injectors** | 胰岛素注射器 | $23.72 | 463 | 0.43 lbs | 1.5% | 64.1% | 41.0% |
| 28 | **Honey Jars** | 蜂蜜罐子 | $21.84 | 648 | 1.92 lbs | 5.4% | 47.0% | 75.0% |
| 29 | **Repair Kits** | 维修套件 | $23.87 | 638 | 0.21 lbs | 5.69% | 64.2% | 72.0% |
| 30 | **Welding Helmets** | 焊接头盔 | $60.23 | 756 | 1.18 lbs | 3.46% | 61.6% | 73.0% |
| 31 | **Tattoo Kits** | 纹身套装 | $31.97 | 487 | 1.48 lbs | 2.09% | 63.8% | 73.0% |
| 32 | **Deck Hardware** | 五金件 | $29.38 | 440 | 1.66 lbs | 4.94% | 46.3% | 74.0% |
| 33 | **Drill Bits** | 钻头 | $26.27 | 281 | 0.96 lbs | 2.68% | 52.8% | 74.0% |
| 34 | **Grinding Discs** | 磨片 | $25.59 | 343 | 1.97 lbs | 2.13% | 45.2% | 80.0% |
| 35 | **Countersink Drill Bits** | 沉孔钻头 | $22.35 | 572 | 0.47 lbs | 1.85% | 53.2% | 64.0% |
| 36 | **Soap & Lotion Dispensers** | 肥皂 | $24.89 | 683 | 1.69 lbs | 5.55% | 55.3% | 50.0% |
| 37 | **Turn Signal Assemblies & Lenses** | 转向信号组件 | $28.47 | 567 | 0.73 lbs | 6.77% | 59.4% | 85.0% |
| 38 | **Handlebar Mounts** | Handlebar Mounts | $25.60 | 589 | 0.58 lbs | 5.37% | 55.6% | 63.0% |
| 39 | **Tie-Downs** | 栓系器具 | $26.67 | 552 | 1.59 lbs | 3.74% | 58.5% | 52.0% |
| 40 | **Exterior Lighting** | 外部照明 | $24.24 | 478 | 0.77 lbs | 4.66% | 52.4% | 69.0% |
| 41 | **Wood Burning Tools** | 木材燃烧工具 | $32.81 | 567 | 1.05 lbs | 4.0% | 53.0% | 82.0% |
| 42 | **Pipe Clamps** | 管夹 | $20.87 | 282 | 1.85 lbs | 5.92% | 42.9% | 71.0% |
| 43 | **Headlights** | 车头灯 | $32.36 | 449 | 0.46 lbs | 5.21% | 46.5% | 75.0% |
| 44 | **Cookbook Stands** | 菜谱架 | $24.94 | 565 | 1.95 lbs | 6.17% | 48.7% | 60.0% |
| 45 | **Forstner Drill Bits** | 费式钻头 | $25.80 | 510 | 0.72 lbs | 4.11% | 57.7% | 71.0% |
| 46 | **Sound Therapy** | 声音疗法 | $43.04 | 249 | 0.95 lbs | 6.32% | 44.4% | 75.0% |
| 47 | **Recipe Holders** | 食谱夹子 | $20.04 | 511 | 1.39 lbs | 5.89% | 45.0% | 48.0% |
| 48 | **Meat Cleavers** | 切肉刀 | $45.22 | 644 | 1.49 lbs | 3.99% | 63.6% | 71.0% |
| 49 | **Cooking Utensils** | 厨具 | $29.82 | 692 | 1.77 lbs | 3.17% | 56.4% | 44.0% |
| 50 | **Float Valves** | 浮阀 | $21.24 | 185 | 0.66 lbs | 4.44% | 40.9% | 67.0% |
| 51 | **Seat Belts** | 安全带 | $33.72 | 198 | 1.52 lbs | 5.78% | 54.0% | 76.0% |
| 52 | **Leak Detection Tools** | 泄漏检测工具 | $99.91 | 146 | 1.46 lbs | 4.3% | 52.6% | 48.0% |
| 53 | **Tactical Vests** | 战术背心 | $48.58 | 537 | 1.50 lbs | 7.91% | 55.2% | 73.0% |
| 54 | **Seat Covers** | 摩托车座套 | $30.50 | 305 | 1.09 lbs | 5.29% | 49.4% | 82.0% |
| 55 | **Angle Grinder Wheels** | 角磨机砂轮 | $24.63 | 142 | 1.51 lbs | 2.41% | 50.5% | 81.0% |
| 56 | **Tortilla Servers** | 玉米饼服务员 | $20.62 | 474 | 1.57 lbs | 6.26% | 57.4% | 39.0% |
| 57 | **Optics Accessories** | 光学配件 | $31.80 | 353 | 0.20 lbs | 5.63% | 51.9% | 40.0% |
| 58 | **Weaving Looms** | 织机 | $24.17 | 389 | 1.06 lbs | 3.33% | 57.3% | 70.0% |
| 59 | **Canvas Tools & Accessories** | 帆布工具 | $21.57 | 268 | 1.07 lbs | 7.32% | 51.3% | 64.0% |
| 60 | **Growth Charts** | 身高墙贴 | $20.53 | 419 | 0.79 lbs | 3.72% | 48.4% | 64.0% |
| 61 | **Bumper Guards** | 保险杠防护装置 | $35.16 | 466 | 1.67 lbs | 7.85% | 38.7% | 66.0% |
| 62 | **Fly Tying Equipment** | 绑蝇设备 | $20.38 | 489 | 0.25 lbs | 2.84% | 61.0% | 50.0% |
| 63 | **Trim** | 装饰 | $27.92 | 252 | 0.27 lbs | 2.44% | 62.4% | 68.0% |
| 64 | **Gutters** | 排水沟 | $24.12 | 159 | 1.61 lbs | 5.02% | 52.1% | 66.0% |
| 65 | **Bait Traps** | 诱饵陷阱 | $26.98 | 291 | 1.75 lbs | 3.31% | 57.3% | 57.0% |
| 66 | **Flags** | 标志 | $23.22 | 222 | 0.56 lbs | 2.61% | 60.6% | 52.0% |
| 67 | **Bags & Cases** | 麦克风箱包 | $27.22 | 235 | 1.01 lbs | 6.87% | 50.3% | 63.0% |
| 68 | **Tools** | 工具 | $31.56 | 210 | 1.33 lbs | 3.64% | 45.3% | 59.0% |
| 69 | **Pressure Regulators** | 压力调节器 | $33.79 | 291 | 0.71 lbs | 5.93% | 53.1% | 74.0% |
| 70 | **Fuel System** | 燃油系统 | $23.87 | 97 | 0.60 lbs | 4.31% | 49.8% | 81.0% |
| 71 | **Trash Can Lids** | 垃圾桶盖 | $23.55 | 148 | 1.37 lbs | 5.21% | 54.5% | 55.0% |
| 72 | **Pool Heater & Heat Pump Parts** | 气筒气泵 | $84.07 | 96 | 1.99 lbs | 6.71% | 46.5% | 70.0% |
| 73 | **Cables & Adapters** | 电缆和适配器 | $25.17 | 591 | 0.35 lbs | 6.58% | 53.8% | 77.0% |
| 74 | **Collectible Vehicles** | 交通工具摆件 | $24.27 | 226 | 0.96 lbs | 5.81% | 63.8% | 87.0% |
| 75 | **Automatic Feeders** | 自动食盆 | $20.93 | 224 | 1.33 lbs | 7.46% | 43.6% | 90.0% |
| 76 | **Car Rack Parts & Accessories** | 汽车货架零件和配件 | $42.76 | 219 | 1.33 lbs | 6.72% | 44.8% | 57.0% |
| 77 | **3D Printer Extruders** | 3D打印机挤出机 | $29.04 | 158 | 0.18 lbs | 4.99% | 61.2% | 80.0% |
| 78 | **Guitar & Bass Accessories** | 吉他 | $39.96 | 447 | 0.70 lbs | 3.89% | 60.3% | 54.2% |
| 79 | **Wine Decanters** | 醒酒器 | $45.82 | 398 | 1.82 lbs | 5.52% | 58.5% | 45.0% |
| 80 | **Deviled Egg Plates** | 咸蛋盘 | $22.22 | 338 | 1.92 lbs | 5.01% | 58.2% | 62.0% |
| 81 | **Grill Lighting** | 点火器 | $30.71 | 593 | 1.27 lbs | 5.43% | 53.6% | 60.0% |
| 82 | **Cheese Knives** | 奶酪刀 | $20.74 | 525 | 0.57 lbs | 4.02% | 45.3% | 53.0% |
| 83 | **Brazing Rods** | 钎杆 | $38.39 | 178 | 0.65 lbs | 2.03% | 61.6% | 55.0% |
| 84 | **Fuel** | 燃油表 | $32.90 | 113 | 0.42 lbs | 4.87% | 52.2% | 67.0% |
| 85 | **Angle** | 角规 | $25.40 | 404 | 0.54 lbs | 2.9% | 60.0% | 64.0% |
| 86 | **Nail Pullers** | 羊角起钉钳 | $23.71 | 366 | 1.29 lbs | 2.27% | 61.3% | 60.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Liver Extracts** | 肝脏提取物 | $31.11 | 838 | 0.30 lbs | 0.31% | Reviews偏高 (>800) |
| 2 | **Figurine Lights** | 雕像灯 | $25.37 | 839 | 1.34 lbs | 2.34% | Reviews偏高 (>800) |
| 3 | **Squirt Guns** | 水枪 | $28.72 | 564 | 1.57 lbs | 3.93% | 谨慎认证类目路径 |
| 4 | **Self-Watering Stakes** | 自浇水桩 | $22.75 | 801 | 1.49 lbs | 2.8% | Reviews偏高 (>800) |
| 5 | **Fountains** | 喷泉 | $40.94 | 590 | 2.30 lbs | 4.78% | 重量偏重 (>2.0 lbs) |
| 6 | **Compressed Air Dusters** | 压缩除尘罐 | $33.30 | 379 | 0.88 lbs | 3.16% | 谨慎认证类目路径 |
| 7 | **Trays & Bags** | 托盘、口袋 | $23.54 | 916 | 1.21 lbs | 9.42% | 退货率偏高 (>8.0%), Reviews偏高 (>800) |
| 8 | **Glasses & Goggles** | 眼镜和护目镜 | $21.98 | 850 | 0.22 lbs | 6.05% | Reviews偏高 (>800) |
| 9 | **Birdhouses** | 鸟屋 | $30.19 | 663 | 2.12 lbs | 2.92% | 重量偏重 (>2.0 lbs) |
| 10 | **Hand Tools** | 手动工具 | $23.62 | 969 | 1.50 lbs | 3.71% | Reviews偏高 (>800) |
| 11 | **Battery Switches** | 接线柱 | $20.40 | 610 | 0.61 lbs | 5.58% | 带电/合规资质敏感关键字 |
| 12 | **Batteries & Battery Chargers** | 电池和电池 | $23.68 | 483 | 0.94 lbs | 9.83% | 退货率偏高 (>8.0%), 带电/合规资质敏感关键字 |
| 13 | **Air Ionizers** | 负离子空气净化器 | $57.13 | 993 | 2.20 lbs | 6.98% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |
| 14 | **Replacement Sensors** | 更换传感器 | $46.06 | 984 | 0.47 lbs | 9.2% | 退货率偏高 (>8.0%), Reviews偏高 (>800) |
| 15 | **Neon Accent Lights** | 霓虹灯 | $27.02 | 958 | 0.79 lbs | 6.23% | Reviews偏高 (>800) |
| 16 | **Champagne Glasses** | 香槟酒杯 | $30.05 | 871 | 1.80 lbs | 7.64% | Reviews偏高 (>800) |
| 17 | **Door Entry Guard** | 门禁 | $20.99 | 923 | 1.03 lbs | 6.12% | Reviews偏高 (>800) |
| 18 | **Deck Lights** | 甲板灯 | $46.86 | 907 | 2.24 lbs | 4.76% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |
| 19 | **Decorative Trays** | 装饰性托盘 | $23.97 | 477 | 1.60 lbs | 9.52% | 退货率偏高 (>8.0%) |
| 20 | **Money & Banking** | 奖金 | $21.17 | 757 | 1.02 lbs | 4.08% | 谨慎认证类目路径 |
| 21 | **Poultry Fountains & Waterers** | 家禽自动喂水器和饮水器 | $27.36 | 533 | 2.30 lbs | 2.74% | 重量偏重 (>2.0 lbs) |
| 22 | **Cup Carriers** | 外卖杯托盘 | $22.00 | 447 | 2.43 lbs | 4.6% | 重量偏重 (>2.0 lbs) |
| 23 | **Tool Sets** | 汽车维修工具套装 | $25.24 | 654 | 2.23 lbs | 3.65% | 重量偏重 (>2.0 lbs) |
| 24 | **Head & Body Supports** | 头枕 | $20.07 | 876 | 0.89 lbs | 7.72% | Reviews偏高 (>800) |
| 25 | **Hands Free Leashes** | 免手持牵绳 | $22.55 | 830 | 0.71 lbs | 6.44% | Reviews偏高 (>800) |
| 26 | **Hand Exercisers** | 手部锻炼器具 | $31.33 | 811 | 1.40 lbs | 5.3% | Reviews偏高 (>800) |
| 27 | **Motion Detectors** | 生命探测器 | $39.99 | 895 | 0.68 lbs | 6.68% | Reviews偏高 (>800), 谨慎认证类目路径 |
| 28 | **Alternative Medicine** | 替代药物 | $38.59 | 918 | 0.53 lbs | 2.58% | Reviews偏高 (>800) |
| 29 | **Airbrush Sets** | 喷漆套装 | $51.37 | 824 | 2.36 lbs | 4.67% | 重量偏重 (>2.0 lbs), Reviews偏高 (>800) |
| 30 | **Robots** | 机器人 | $50.55 | 956 | 1.30 lbs | 6.4% | Reviews偏高 (>800), 谨慎认证类目路径 |
| 31 | **Camping Fans** | 露营爱好者 | $38.29 | 248 | 2.18 lbs | 4.56% | 重量偏重 (>2.0 lbs) |
| 32 | **Sewing Storage** | 缝纫用品收纳用品 | $23.66 | 846 | 1.85 lbs | 5.03% | Reviews偏高 (>800) |
| 33 | **Game Pieces** | 棋子 | $31.59 | 810 | 0.71 lbs | 2.83% | Reviews偏高 (>800), 谨慎认证类目路径 |
| 34 | **Card Shufflers** | 洗牌机 | $41.91 | 526 | 1.47 lbs | 9.17% | 退货率偏高 (>8.0%), 谨慎认证类目路径 |
| 35 | **Remote & App Controlled Vehicle Batteries** | 遥控 | $34.49 | 432 | 0.37 lbs | 6.27% | 谨慎认证类目路径 |
| 36 | **Cooking & Baking Kits** | 烹饪和烘焙套件 | $30.75 | 580 | 2.29 lbs | 2.98% | 重量偏重 (>2.0 lbs), 谨慎认证类目路径 |
| 37 | **Boats** | 船 | $53.66 | 336 | 1.42 lbs | 6.03% | 谨慎认证类目路径 |
| 38 | **Accessories** | 辅料 | $20.05 | 277 | 2.20 lbs | 4.87% | 重量偏重 (>2.0 lbs) |
| 39 | **Bed Mats** | 床垫 | $20.00 | 970 | 1.00 lbs | 8.45% | 退货率偏高 (>8.0%), Reviews偏高 (>800) |
| 40 | **Bag Sealers** | 封袋机 | $39.84 | 476 | 2.48 lbs | 6.09% | 重量偏重 (>2.0 lbs) |
| 41 | **Wands** | Wands | $22.15 | 817 | 0.65 lbs | 5.37% | Reviews偏高 (>800), 谨慎认证类目路径 |
| 42 | **Spa Slippers** | 温泉拖鞋 | $25.37 | 270 | 2.03 lbs | 6.02% | 重量偏重 (>2.0 lbs) |
| 43 | **Flower Pressing** | 压花 | $22.67 | 174 | 1.71 lbs | 2.87% | 谨慎认证类目路径 |
| 44 | **Trim & Repair Kits** | 修整和维修套件 | $38.19 | 375 | 0.70 lbs | 9.84% | 退货率偏高 (>8.0%) |
| 45 | **Excavators** | 挖掘机 | $39.89 | 560 | 1.58 lbs | 4.33% | 谨慎认证类目路径 |
| 46 | **Gun Belts** | 枪带 | $38.00 | 744 | 0.81 lbs | 9.02% | 退货率偏高 (>8.0%) |
| 47 | **Locking Devices** | 防盗锁 | $40.20 | 757 | 2.43 lbs | 7.5% | 重量偏重 (>2.0 lbs) |
| 48 | **Rods** | 杆 | $22.17 | 253 | 2.46 lbs | 1.94% | 重量偏重 (>2.0 lbs) |
| 49 | **Cue Sticks** | 台球杆 | $66.23 | 520 | 2.46 lbs | 5.31% | 重量偏重 (>2.0 lbs) |
| 50 | **Guitars & Strings** | 吉他 | $28.07 | 625 | 1.30 lbs | 5.12% | 谨慎认证类目路径 |
| 51 | **Airplanes & Jets** | 飞机 | $59.91 | 255 | 1.07 lbs | 8.46% | 退货率偏高 (>8.0%), 谨慎认证类目路径 |
| 52 | **Cream Chargers & Whippers** | 奶油充电器 | $36.66 | 452 | 1.40 lbs | 2.63% | 带电/合规资质敏感关键字 |
| 53 | **Metric Inserts & Kits** | 米制刀片和套件 | $44.60 | 179 | 2.37 lbs | 5.6% | 重量偏重 (>2.0 lbs) |
| 54 | **Gaiters** | 护腿、护脚 | $32.91 | 417 | 0.65 lbs | 8.64% | 退货率偏高 (>8.0%) |
| 55 | **Protractors** | 分光镜 | $23.63 | 803 | 0.45 lbs | 2.95% | Reviews偏高 (>800) |
| 56 | **Monoculars** | 单筒望远镜 | $75.79 | 599 | 0.69 lbs | 7.05% | 谨慎认证类目路径 |
| 57 | **Paint Roller Extension Poles** | 油漆滚筒加长杆 | $36.88 | 301 | 2.04 lbs | 4.55% | 重量偏重 (>2.0 lbs) |
| 58 | **Alarms & Anti-Theft** | 摩托车防盗器 | $31.22 | 685 | 0.83 lbs | 4.72% | 谨慎认证类目路径 |
| 59 | **Game Table Accessories** | 游戏桌配件 | $28.45 | 223 | 1.51 lbs | 7.43% | 谨慎认证类目路径 |
| 60 | **Bats** | 蝙蝠 | $35.56 | 352 | 2.25 lbs | 2.61% | 重量偏重 (>2.0 lbs) |
| 61 | **Bulb Planters** | 球茎栽植器 | $23.70 | 299 | 2.30 lbs | 2.9% | 重量偏重 (>2.0 lbs) |
| 62 | **Battery Chargers** | 电池充电器 | $37.89 | 396 | 1.50 lbs | 6.24% | 带电/合规资质敏感关键字 |
| 63 | **Kick Plates** | 踢脚板 | $27.91 | 100 | 1.53 lbs | 8.07% | 退货率偏高 (>8.0%) |
| 64 | **Food Processor Parts & Accessories** | 食物处理器零件 | $31.76 | 305 | 0.99 lbs | 8.72% | 退货率偏高 (>8.0%) |
| 65 | **Air Conditioning & Heater Control** | 空调与加热器控制 | $32.09 | 190 | 0.41 lbs | 9.39% | 退货率偏高 (>8.0%) |
| 66 | **Armrest Lids** | 扶手盖 | $33.61 | 266 | 2.27 lbs | 6.52% | 重量偏重 (>2.0 lbs) |
| 67 | **Breast Pump Carrying Bags** | 奶泵携带包 | $36.83 | 153 | 1.23 lbs | 9.17% | 退货率偏高 (>8.0%) |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Workout Top & Bottom Sets** | 服装套装 | $27.94 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 2 | **Lanterns** | 灯笼 | $28.10 | Review护城河太深 (>1000) |
| 3 | **Resveratrol** | 白藜芦醇 | $29.32 | Review护城河太深 (>1000) |
| 4 | **Suits** | 套装 | $49.21 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 5 | **Skirt Sets** | 裙装套装 | $34.63 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 6 | **Tankini Sets** | 坦基尼套装 | $21.91 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 7 | **Sets** | 套 | $24.02 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 8 | **Rash Guard Sets** | Rash Guard Sets | $20.58 | 高风险类目路径过滤 |
| 9 | **Posters & Prints** | 海报和印刷品 | $24.19 | Review护城河太深 (>1000) |
| 10 | **Grill Pads & Floor Mats** | 烤炉垫和地垫 | $22.41 | Review护城河太深 (>1000) |
| 11 | **Clothing** | 服装 | $24.87 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 12 | **Light Therapy** | 光照疗法 | $69.38 | 退货率过高 (>10.0%) |
| 13 | **Drip Irrigation Kits** | 滴灌套件 | $36.53 | 重量超标 (>2.5 lbs) |
| 14 | **Pants** | 长裤 | $26.36 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 15 | **Casual Jackets** | 休闲夹克 | $37.24 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 16 | **Snorkeling Packages** | 套装 | $31.97 | 退货率过高 (>10.0%), Review护城河太深 (>1000) |
| 17 | **Track & Active Jackets** | 风衣、夹克 | $29.73 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 18 | **Active Pants** | 运动裤 | $32.22 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 19 | **Hand Fuel Pumps** | 手动燃油泵 | $32.41 | Review护城河太深 (>1000) |
| 20 | **Button-Down Shirts** | 扣角领衬衫 | $20.66 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 21 | **Wrinkle & Anti-Aging Devices** | 皱纹和抗衰老设备 | $105.48 | 退货率过高 (>10.0%) |
| 22 | **Costumes** | 装扮服饰 | $34.97 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 23 | **Walkie Talkies** | 对讲机 | $24.92 | Review护城河太深 (>1000) |
| 24 | **Casual** | 休闲类 | $38.78 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 25 | **Dresses** | 连衣裙 | $36.92 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 26 | **Beneficial Insects** | 益虫 | $32.04 | 排除类关键字过滤 |
| 27 | **Old Fashioned Glasses** | 古典杯 | $26.52 | Review护城河太深 (>1000) |
| 28 | **Herbal Supplements** | 草药补充剂 | $24.01 | Review护城河太深 (>1000) |
| 29 | **Jumpsuits & Rompers** | 连身裤 | $21.14 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 30 | **Grease Guns** | 油脂枪 | $43.16 | 重量超标 (>2.5 lbs) |
| 31 | **Car Stereo Receivers** | 汽车音响 | $107.10 | 退货率过高 (>10.0%) |
| 32 | **Pant Sets** | 长裤套装 | $23.27 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 33 | **Assortments & Variety Gifts** | 种类 | $29.72 | Review护城河太深 (>1000) |
| 34 | **Mary Jane** | 玛丽珍鞋 | $20.74 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 35 | **Night Out** | 晚宴裙装 | $28.52 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 36 | **Battery Jumper Cables** | 电池跳线 | $23.91 | 重量超标 (>2.5 lbs), Review护城河太深 (>1000) |
| 37 | **Camping Pillows** | 睡袋配件 | $27.59 | Review护城河太深 (>1000) |
| 38 | **Sweatpants** | 运动裤 | $29.43 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 39 | **Wall Molding & Trim** | 墙压条和镶边 | $20.31 | 退货率过高 (>10.0%) |
| 40 | **Wristlets** | 腕包 | $30.11 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 41 | **Candlestick Holders** | 烛台座 | $24.44 | 退货率过高 (>10.0%) |
| 42 | **Bustiers & Corsets** | 紧身衣 | $26.05 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 43 | **Strands** | 线式项链 | $20.19 | 高风险类目路径过滤 |
| 44 | **Jerseys** | Jerseys | $25.07 | 高风险类目路径过滤 |
| 45 | **Paddleboard Accessories** | 冲浪板配件 | $55.98 | 重量超标 (>2.5 lbs) |
| 46 | **Trucks** | 卡车 | $69.24 | 重量超标 (>2.5 lbs) |
| 47 | **Decorative Candle Lanterns** | 装饰性点烛灯笼 | $38.31 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 48 | **Home Décor Products** | 家居装饰 | $20.89 | 退货率过高 (>10.0%) |
| 49 | **Candle Sets** | 蜡烛套装 | $22.83 | Review护城河太深 (>1000) |
| 50 | **Hair Accessories** | 头饰 | $22.50 | 重量超标 (>2.5 lbs) |
| 51 | **Decorative Bookends** | 装饰性书挡 | $27.19 | 重量超标 (>2.5 lbs) |
| 52 | **Brake Adjusting Tools** | 制动器调整工具 | $20.61 | 重量超标 (>2.5 lbs) |
| 53 | **Trench Coats** | 风雨衣 | $55.21 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 54 | **Horns & Sirens** | 喇叭 | $28.42 | Review护城河太深 (>1000) |
| 55 | **Accessories** | 辅料 | $29.29 | Review护城河太深 (>1000) |
| 56 | **Clutches** | 手拿包 | $34.11 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 57 | **Picture Frames** | 画框 | $28.79 | 重量超标 (>2.5 lbs) |
| 58 | **Sweatpants** | Sweatpants | $26.89 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 59 | **Protective Gear** | 防护装备 | $38.53 | 重量超标 (>2.5 lbs) |
| 60 | **Hoes** | 园艺锄 | $29.39 | 重量超标 (>2.5 lbs) |
| 61 | **Tops** | Tops | $21.42 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 62 | **Hearing Amplifiers** | 助听扩音器 | $128.27 | 退货率过高 (>10.0%) |
| 63 | **Jerseys** | 球衣 | $34.74 | 高风险类目路径过滤 |
| 64 | **Syrup & Honey Dispensers** | 饮料桶嘴 | $21.80 | 退货率过高 (>10.0%) |
| 65 | **Angle Clamps** | 角夹钳 | $36.06 | 重量超标 (>2.5 lbs) |
| 66 | **Hoodies** | 帽衫 | $38.53 | 高风险类目路径过滤 |
| 67 | **Faucets** | 水龙头 | $29.41 | 退货率过高 (>10.0%) |
| 68 | **Floor Molding & Trim** | 地板压条和镶边 | $25.44 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 69 | **Pant Sets** | 长裤套装 | $23.16 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 70 | **Oxygen** | 氧气 | $42.95 | 退货率过高 (>10.0%) |
| 71 | **In-Dash Navigation** | 内置车载导航 | $111.36 | 退货率过高 (>10.0%) |
| 72 | **Workout Top & Bottom Sets** | 服装套装 | $32.35 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 73 | **Signal Converters** | 信号转换器 | $30.27 | 退货率过高 (>10.0%) |
| 74 | **Mounts** | 减震器 | $21.64 | Review护城河太深 (>1000) |
| 75 | **Training Heads** | 培训负责人 | $28.51 | 退货率过高 (>10.0%) |
| 76 | **AV Receivers & Amplifiers** | AV接收机 | $117.53 | 退货率过高 (>10.0%) |
| 77 | **Hoodies** | 帽衫 | $54.57 | 高风险类目路径过滤 |
| 78 | **Post Light Accessories** | 柱灯配件 | $31.05 | 重量超标 (>2.5 lbs) |
| 79 | **Wormers** | 虫子 | $39.87 | 排除类关键字过滤 |
| 80 | **Manual Pasta Makers** | 手动面条机 | $31.92 | Review护城河太深 (>1000) |
| 81 | **Lockets** | 盒式吊坠 | $26.62 | 高风险类目路径过滤 |
| 82 | **Clothing** | 服装 | $20.81 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 83 | **Foot Warmers** | 暖脚 | $30.55 | 退货率过高 (>10.0%) |
| 84 | **Shoulder Bags** | 单肩包 | $43.81 | 高风险类目路径过滤 |
| 85 | **Candle Sconces** | 壁突式烛台 | $27.93 | 退货率过高 (>10.0%) |
| 86 | **Urinal Accessories** | 小便池配件 | $34.73 | 重量超标 (>2.5 lbs) |
| 87 | **Lab Supply Dispensers** | 实验室用品分配器 | $32.42 | 重量超标 (>2.5 lbs) |
| 88 | **Fur & Faux Fur** | 毛绒和人造毛皮 | $46.21 | 退货率过高 (>10.0%), Review护城河太深 (>1000), 高风险类目路径过滤 |
| 89 | **Digital Media Receivers** | 数字媒体接收器 | $149.04 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 90 | **Candleholder Sets** | 烛台套装 | $30.61 | 退货率过高 (>10.0%) |
| 91 | **Jerseys** | Jerseys | $20.81 | 高风险类目路径过滤 |
| 92 | **Night Vision Binoculars & Goggles** | 夜视双筒望远镜和护目镜 | $103.29 | 退货率过高 (>10.0%) |
| 93 | **Accessories** | 辅料 | $21.50 | 重量超标 (>2.5 lbs) |
| 94 | **Vests** | 单马甲 | $25.13 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 95 | **In-Dash DVD & Video Receivers** | 仪表盘视频 | $153.19 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 96 | **Footwear** | 鞋靴 | $38.53 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 97 | **One-Piece Pajamas** | 连体睡衣 | $31.61 | 退货率过高 (>10.0%), 高风险类目路径过滤 |

## 三、 候选类目详细数据指标画像 (供大模型分析使用)

以下为入选的绿色与黄色子类目的完整数据指标。您可以将这些数据输入大模型（如 Gemini、Claude），让其结合具体品类特性进行深入的入选原因、产品特征及商业机会评估。

### 🟢 绿色类目详情列表

#### 🏆 🟢-1. Outdoor Statues (户外雕像)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Outdoor Statues  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.98`
  *   **平均 Reviews (Avg Reviews)**：`751 个`
  *   **物理重量 (Weight)**：`1.11 lbs`
  *   **平均退货率 (Return Rate)**：`2.98%`
  *   **平均毛利率 (Profit Margin)**：`57.23%`
  *   **品牌集中度 (Brand Concentration)**：`40.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Garden Sculptures & Statues › Outdoor Statues  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 雕塑、雕像 › 户外雕像`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`49`
  *   **新品平均价格**：`$ 22.51`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`1,282`
  *   **新品月均销售额**：`$29,438`
  *   **平均重量**：`1.11 pounds (505 g)`
  *   **平均体积**：`427.12 in³ (6,999 cm³)`
  *   **平均毛利率**：`57.23%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`5.1‰`

---

#### 🏆 🟢-2. Decorative Garden Stakes (装饰园艺桩)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Decorative Garden Stakes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.07`
  *   **平均 Reviews (Avg Reviews)**：`373 个`
  *   **物理重量 (Weight)**：`0.73 lbs`
  *   **平均退货率 (Return Rate)**：`2.04%`
  *   **平均毛利率 (Profit Margin)**：`57.76%`
  *   **品牌集中度 (Brand Concentration)**：`55.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`90.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Decorative Garden Stakes  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 装饰园艺桩`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`33`
  *   **新品平均价格**：`$ 22.15`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`1,192`
  *   **新品月均销售额**：`$28,344`
  *   **平均重量**：`0.73 pounds (331 g)`
  *   **平均体积**：`303.75 in³ (4,978 cm³)`
  *   **平均毛利率**：`57.76%`
  *   **卖家所属地**：`中国|90.0%`
  *   **搜索购买比**：`8.6‰`

---

#### 🏆 🟢-3. Bread Knives (面包刀)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Bread Knives  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.34`
  *   **平均 Reviews (Avg Reviews)**：`772 个`
  *   **物理重量 (Weight)**：`0.94 lbs`
  *   **平均退货率 (Return Rate)**：`2.92%`
  *   **平均毛利率 (Profit Margin)**：`54.8%`
  *   **品牌集中度 (Brand Concentration)**：`53.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Bread Knives  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 刀具厨房及配件 › 面包刀`
  *   **A+数量占比**：`92%`
  *   **新品平均评分数**：`116`
  *   **新品平均价格**：`$ 19.68`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`639`
  *   **新品月均销售额**：`$12,117`
  *   **平均重量**：`0.94 pounds (428 g)`
  *   **平均体积**：`156.22 in³ (2,560 cm³)`
  *   **平均毛利率**：`54.8%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`13.5‰`

---

#### 🏆 🟢-4. Shilajit (Shilajit)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Shilajit  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.77`
  *   **平均 Reviews (Avg Reviews)**：`638 个`
  *   **物理重量 (Weight)**：`0.41 lbs`
  *   **平均退货率 (Return Rate)**：`0.34%`
  *   **平均毛利率 (Profit Margin)**：`68.14%`
  *   **品牌集中度 (Brand Concentration)**：`62.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`40.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Shilajit  市场分析`
  *   **市场路径(中文)**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Shilajit`
  *   **A+数量占比**：`94%`
  *   **新品平均评分数**：`46`
  *   **新品平均价格**：`$ 30.26`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`736`
  *   **新品月均销售额**：`$23,340`
  *   **平均重量**：`0.41 pounds (185 g)`
  *   **平均体积**：`57.37 in³ (940 cm³)`
  *   **平均毛利率**：`68.14%`
  *   **卖家所属地**：`美国|60.0%`
  *   **搜索购买比**：`15.3‰`

---

#### 🏆 🟢-5. Lighting Products (水底灯)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$50.99`
  *   **平均 Reviews (Avg Reviews)**：`476 个`
  *   **物理重量 (Weight)**：`1.71 lbs`
  *   **平均退货率 (Return Rate)**：`6.75%`
  *   **平均毛利率 (Profit Margin)**：`67.26%`
  *   **品牌集中度 (Brand Concentration)**：`55.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Parts & Accessories › Lighting Products  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 零配件 › 水底灯`
  *   **A+数量占比**：`98%`
  *   **新品平均评分数**：`56`
  *   **新品平均价格**：`$ 51.56`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`1,153`
  *   **新品月均销售额**：`$67,451`
  *   **平均重量**：`1.71 pounds (774 g)`
  *   **平均体积**：`640.36 in³ (10,494 cm³)`
  *   **平均毛利率**：`67.26%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-6. Decorative Boxes (装饰盒)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.55`
  *   **平均 Reviews (Avg Reviews)**：`676 个`
  *   **物理重量 (Weight)**：`1.61 lbs`
  *   **平均退货率 (Return Rate)**：`7.91%`
  *   **平均毛利率 (Profit Margin)**：`57.78%`
  *   **品牌集中度 (Brand Concentration)**：`47.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Boxes  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰盒`
  *   **A+数量占比**：`75%`
  *   **新品平均评分数**：`62`
  *   **新品平均价格**：`$ 23.42`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`773`
  *   **新品月均销售额**：`$17,734`
  *   **平均重量**：`1.61 pounds (730 g)`
  *   **平均体积**：`346.38 in³ (5,676 cm³)`
  *   **平均毛利率**：`57.78%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`4.5‰`

---

#### 🏆 🟢-7. Nozzles (喷嘴)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.04`
  *   **平均 Reviews (Avg Reviews)**：`552 个`
  *   **物理重量 (Weight)**：`0.44 lbs`
  *   **平均退货率 (Return Rate)**：`2.63%`
  *   **平均毛利率 (Profit Margin)**：`64.8%`
  *   **品牌集中度 (Brand Concentration)**：`55.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Power Tools › Replacement Parts & Accessories › Pressure Washer Parts & Accessories › Nozzles  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 电动工具 › 替换件和配件 › 高压清洗机配件 › 喷嘴`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`101`
  *   **新品平均价格**：`$ 33.62`
  *   **新品平均星级**：`3.0`
  *   **新品月均销量**：`725`
  *   **新品月均销售额**：`$23,546`
  *   **平均重量**：`0.44 pounds (200 g)`
  *   **平均体积**：`170.20 in³ (2,789 cm³)`
  *   **平均毛利率**：`64.8%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`13.5‰`

---

#### 🏆 🟢-8. Cayenne (辣椒)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Cayenne  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.89`
  *   **平均 Reviews (Avg Reviews)**：`709 个`
  *   **物理重量 (Weight)**：`0.36 lbs`
  *   **平均退货率 (Return Rate)**：`0.32%`
  *   **平均毛利率 (Profit Margin)**：`62.96%`
  *   **品牌集中度 (Brand Concentration)**：`58.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Herbal Supplements › Cayenne  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 身、泳和附剂 › 草本补充 › 辣椒`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`48`
  *   **新品平均价格**：`$ 25.23`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`488`
  *   **新品月均销售额**：`$11,975`
  *   **平均重量**：`0.36 pounds (163 g)`
  *   **平均体积**：`34.57 in³ (566 cm³)`
  *   **平均毛利率**：`62.96%`
  *   **卖家所属地**：`美国|46.0%`
  *   **搜索购买比**：`16.4‰`

---

#### 🏆 🟢-9. Tap Extractors (分接抽水机)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Taps & Dies › Tap Extractors  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.96`
  *   **平均 Reviews (Avg Reviews)**：`798 个`
  *   **物理重量 (Weight)**：`1.29 lbs`
  *   **平均退货率 (Return Rate)**：`4.89%`
  *   **平均毛利率 (Profit Margin)**：`59.8%`
  *   **品牌集中度 (Brand Concentration)**：`59.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Taps & Dies › Tap Extractors  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具 › 水龙头 › 分接抽水机`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`414`
  *   **新品平均价格**：`$ 18.5`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`434`
  *   **新品月均销售额**：`$8,589`
  *   **平均重量**：`1.29 pounds (584 g)`
  *   **平均体积**：`53.87 in³ (883 cm³)`
  *   **平均毛利率**：`59.8%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟢-10. Scissors & Shears (工业剪)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Scissors & Shears  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.92`
  *   **平均 Reviews (Avg Reviews)**：`773 个`
  *   **物理重量 (Weight)**：`0.88 lbs`
  *   **平均退货率 (Return Rate)**：`2.68%`
  *   **平均毛利率 (Profit Margin)**：`61.44%`
  *   **品牌集中度 (Brand Concentration)**：`55.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Scissors & Shears  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具 › 工业剪`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`95`
  *   **新品平均价格**：`$ 18.77`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`816`
  *   **新品月均销售额**：`$10,203`
  *   **平均重量**：`0.88 pounds (400 g)`
  *   **平均体积**：`74.27 in³ (1,217 cm³)`
  *   **平均毛利率**：`61.44%`
  *   **卖家所属地**：`美国|52.0%`
  *   **搜索购买比**：`11.5‰`

---

#### 🏆 🟢-11. Herb & Spice Mills (草本植物)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Seasoning & Spice Tools › Herb & Spice Mills  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.79`
  *   **平均 Reviews (Avg Reviews)**：`747 个`
  *   **物理重量 (Weight)**：`0.57 lbs`
  *   **平均退货率 (Return Rate)**：`3.55%`
  *   **平均毛利率 (Profit Margin)**：`60.66%`
  *   **品牌集中度 (Brand Concentration)**：`56.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`56.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Seasoning & Spice Tools › Herb & Spice Mills  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 调味品 › 草本植物`
  *   **A+数量占比**：`57%`
  *   **新品平均评分数**：`52`
  *   **新品平均价格**：`$ 14.37`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`721`
  *   **新品月均销售额**：`$9,080`
  *   **平均重量**：`0.57 pounds (259 g)`
  *   **平均体积**：`34.98 in³ (573 cm³)`
  *   **平均毛利率**：`60.66%`
  *   **卖家所属地**：`中国|56.0%`
  *   **搜索购买比**：`4.9‰`

---

#### 🏆 🟢-12. Bladder Control Devices (膀胱控制设备)

- **完整市场路径**：`Health & Household › Health Care › Incontinence & Ostomy › Bladder Control Devices  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.82`
  *   **平均 Reviews (Avg Reviews)**：`515 个`
  *   **物理重量 (Weight)**：`0.57 lbs`
  *   **平均退货率 (Return Rate)**：`3.9%`
  *   **平均毛利率 (Profit Margin)**：`62.14%`
  *   **品牌集中度 (Brand Concentration)**：`46.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Incontinence & Ostomy › Bladder Control Devices  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 成人失禁用品 › 膀胱控制设备`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`341`
  *   **新品平均价格**：`$ 33.51`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`344`
  *   **新品月均销售额**：`$10,985`
  *   **平均重量**：`0.57 pounds (257 g)`
  *   **平均体积**：`129.67 in³ (2,125 cm³)`
  *   **平均毛利率**：`62.14%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`10.6‰`

---

#### 🏆 🟢-13. Chocolate Drink Mixes (巧克力饮料混合物)

- **完整市场路径**：`Grocery & Gourmet Food › Beverages › Bottled Beverages, Water & Drink Mixes › Powdered Drink Mixes & Flavorings › Chocolate Drink Mixes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.45`
  *   **平均 Reviews (Avg Reviews)**：`735 个`
  *   **物理重量 (Weight)**：`1.83 lbs`
  *   **平均退货率 (Return Rate)**：`0.21%`
  *   **平均毛利率 (Profit Margin)**：`55.82%`
  *   **品牌集中度 (Brand Concentration)**：`65.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`13.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Grocery & Gourmet Food › Beverages › Bottled Beverages, Water & Drink Mixes › Powdered Drink Mixes & Flavorings › Chocolate Drink Mixes  市场分析`
  *   **市场路径(中文)**：`杂货店 › 饮料 › 瓶装饮料，水 › 粉状饮料混合物 › 巧克力饮料混合物`
  *   **A+数量占比**：`54%`
  *   **新品平均评分数**：`57`
  *   **新品平均价格**：`$ 36.72`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`232`
  *   **新品月均销售额**：`$8,430`
  *   **平均重量**：`1.83 pounds (828 g)`
  *   **平均体积**：`178.94 in³ (2,932 cm³)`
  *   **平均毛利率**：`55.82%`
  *   **卖家所属地**：`美国|87.0%`
  *   **搜索购买比**：`13.4‰`

---

#### 🏆 🟢-14. Weather Stripping (挡风雨条)

- **完整市场路径**：`Automotive › Replacement Parts › Body & Trim › Trim › Weather Stripping  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.85`
  *   **平均 Reviews (Avg Reviews)**：`523 个`
  *   **物理重量 (Weight)**：`1.66 lbs`
  *   **平均退货率 (Return Rate)**：`6.26%`
  *   **平均毛利率 (Profit Margin)**：`53.52%`
  *   **品牌集中度 (Brand Concentration)**：`42.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`90.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Body & Trim › Trim › Weather Stripping  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 身体 › 饰面 › 挡风雨条`
  *   **A+数量占比**：`78%`
  *   **新品平均评分数**：`65`
  *   **新品平均价格**：`$ 18.61`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`423`
  *   **新品月均销售额**：`$7,698`
  *   **平均重量**：`1.66 pounds (753 g)`
  *   **平均体积**：`88.28 in³ (1,447 cm³)`
  *   **平均毛利率**：`53.52%`
  *   **卖家所属地**：`中国|90.0%`
  *   **搜索购买比**：`8.2‰`

---

#### 🏆 🟢-15. Plaques & Wall Art (装饰墙)

- **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Plaques & Wall Art  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.45`
  *   **平均 Reviews (Avg Reviews)**：`594 个`
  *   **物理重量 (Weight)**：`1.04 lbs`
  *   **平均退货率 (Return Rate)**：`2.89%`
  *   **平均毛利率 (Profit Margin)**：`58.38%`
  *   **品牌集中度 (Brand Concentration)**：`47.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`86.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Outdoor Décor › Plaques & Wall Art  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 彩绘装饰 › 装饰墙`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`143`
  *   **新品平均价格**：`$ 18.45`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`361`
  *   **新品月均销售额**：`$7,021`
  *   **平均重量**：`1.04 pounds (473 g)`
  *   **平均体积**：`88.85 in³ (1,456 cm³)`
  *   **平均毛利率**：`58.38%`
  *   **卖家所属地**：`中国|86.0%`
  *   **搜索购买比**：`4.9‰`

---

#### 🏆 🟢-16. Brake System Bleeding Tools (刹车排气)

- **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.18`
  *   **平均 Reviews (Avg Reviews)**：`421 个`
  *   **物理重量 (Weight)**：`1.48 lbs`
  *   **平均退货率 (Return Rate)**：`4.69%`
  *   **平均毛利率 (Profit Margin)**：`54.6%`
  *   **品牌集中度 (Brand Concentration)**：`49.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Brake Tools › Brake System Bleeding Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 制动工具 › 刹车排气`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`52`
  *   **新品平均价格**：`$ 19.11`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`452`
  *   **新品月均销售额**：`$8,814`
  *   **平均重量**：`1.48 pounds (670 g)`
  *   **平均体积**：`288.88 in³ (4,734 cm³)`
  *   **平均毛利率**：`54.6%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`8.9‰`

---

#### 🏆 🟢-17. Nozzles (喷嘴)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Sprayers & Accessories › Nozzles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.16`
  *   **平均 Reviews (Avg Reviews)**：`200 个`
  *   **物理重量 (Weight)**：`0.31 lbs`
  *   **平均退货率 (Return Rate)**：`1.98%`
  *   **平均毛利率 (Profit Margin)**：`60.3%`
  *   **品牌集中度 (Brand Concentration)**：`59.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Sprayers & Accessories › Nozzles  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 喷雾器 › 喷嘴`
  *   **A+数量占比**：`53%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 25.56`
  *   **新品平均星级**：`2.7`
  *   **新品月均销量**：`451`
  *   **新品月均销售额**：`$11,222`
  *   **平均重量**：`0.31 pounds (139 g)`
  *   **平均体积**：`98.39 in³ (1,612 cm³)`
  *   **平均毛利率**：`60.3%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`16.6‰`

---

#### 🏆 🟢-18. Feeders (喂食器)

- **完整市场路径**：`Pet Supplies › Birds › Feeding & Watering Supplies › Feeders  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.31`
  *   **平均 Reviews (Avg Reviews)**：`448 个`
  *   **物理重量 (Weight)**：`1.26 lbs`
  *   **平均退货率 (Return Rate)**：`5.44%`
  *   **平均毛利率 (Profit Margin)**：`52.97%`
  *   **品牌集中度 (Brand Concentration)**：`37.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Birds › Feeding & Watering Supplies › Feeders  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 鸟类 › 喂食 › 喂食器`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`187`
  *   **新品平均价格**：`$ 30.19`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`517`
  *   **新品月均销售额**：`$14,029`
  *   **平均重量**：`1.26 pounds (571 g)`
  *   **平均体积**：`220.26 in³ (3,609 cm³)`
  *   **平均毛利率**：`52.97%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟢-19. Toilet Spare Parts (马桶配件)

- **完整市场路径**：`Automotive › RV Parts & Accessories › Interior › Bath › Toilets & Parts › Toilet Spare Parts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.10`
  *   **平均 Reviews (Avg Reviews)**：`534 个`
  *   **物理重量 (Weight)**：`0.39 lbs`
  *   **平均退货率 (Return Rate)**：`4.02%`
  *   **平均毛利率 (Profit Margin)**：`60.02%`
  *   **品牌集中度 (Brand Concentration)**：`60.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › RV Parts & Accessories › Interior › Bath › Toilets & Parts › Toilet Spare Parts  市场分析`
  *   **市场路径(中文)**：`汽车 › 房车配件 › 家具 › 浴缸 › 厕所 › 马桶配件`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 23.03`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`225`
  *   **新品月均销售额**：`$3,984`
  *   **平均重量**：`0.39 pounds (177 g)`
  *   **平均体积**：`117.22 in³ (1,921 cm³)`
  *   **平均毛利率**：`60.02%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`17.6‰`

---

#### 🏆 🟢-20. Electrical System Tools (电气系统工具)

- **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.78`
  *   **平均 Reviews (Avg Reviews)**：`442 个`
  *   **物理重量 (Weight)**：`1.00 lbs`
  *   **平均退货率 (Return Rate)**：`2.38%`
  *   **平均毛利率 (Profit Margin)**：`56.17%`
  *   **品牌集中度 (Brand Concentration)**：`42.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Electrical System Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 电气系统工具`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`58`
  *   **新品平均价格**：`$ 19.62`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`408`
  *   **新品月均销售额**：`$9,263`
  *   **平均重量**：`1.00 pounds (453 g)`
  *   **平均体积**：`318.23 in³ (5,215 cm³)`
  *   **平均毛利率**：`56.17%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟢-21. Trophies (奖杯)

- **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.00`
  *   **平均 Reviews (Avg Reviews)**：`296 个`
  *   **物理重量 (Weight)**：`0.95 lbs`
  *   **平均退货率 (Return Rate)**：`2.59%`
  *   **平均毛利率 (Profit Margin)**：`62.07%`
  *   **品牌集中度 (Brand Concentration)**：`46.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`51.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports & Outdoor Recreation Accessories › Trophies, Medals & Awards › Trophies  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 辅料 › 、奖牌 › 奖杯`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`46`
  *   **新品平均价格**：`$ 30.21`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`442`
  *   **新品月均销售额**：`$13,640`
  *   **平均重量**：`0.95 pounds (431 g)`
  *   **平均体积**：`161.76 in³ (2,651 cm³)`
  *   **平均毛利率**：`62.07%`
  *   **卖家所属地**：`中国|51.0%`
  *   **搜索购买比**：`6.5‰`

---

#### 🏆 🟢-22. Diamond Blades (钻石刀片)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Saw Blades, Parts & Accessories › Blades › Diamond Blades  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.43`
  *   **平均 Reviews (Avg Reviews)**：`531 个`
  *   **物理重量 (Weight)**：`0.75 lbs`
  *   **平均退货率 (Return Rate)**：`2.39%`
  *   **平均毛利率 (Profit Margin)**：`61.29%`
  *   **品牌集中度 (Brand Concentration)**：`57.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Saw Blades, Parts & Accessories › Blades › Diamond Blades  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 电动工具零件 › 锯片，零件 › 刀片 › 钻石刀片`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`45`
  *   **新品平均价格**：`$ 16.41`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`266`
  *   **新品月均销售额**：`$4,387`
  *   **平均重量**：`0.75 pounds (339 g)`
  *   **平均体积**：`9.85 in³ (161 cm³)`
  *   **平均毛利率**：`61.29%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`12.4‰`

---

#### 🏆 🟢-23. Smokeless Inhalers (无烟吸入器)

- **完整市场路径**：`Health & Household › Health Care › Smoking Cessation › Smokeless Inhalers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.87`
  *   **平均 Reviews (Avg Reviews)**：`385 个`
  *   **物理重量 (Weight)**：`0.14 lbs`
  *   **平均退货率 (Return Rate)**：`2.22%`
  *   **平均毛利率 (Profit Margin)**：`63.63%`
  *   **品牌集中度 (Brand Concentration)**：`62.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`41.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Smoking Cessation › Smokeless Inhalers  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 戒烟 › 无烟吸入器`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`41`
  *   **新品平均价格**：`$ 18.01`
  *   **新品平均星级**：`3.5`
  *   **新品月均销量**：`381`
  *   **新品月均销售额**：`$6,384`
  *   **平均重量**：`0.14 pounds (64 g)`
  *   **平均体积**：`14.64 in³ (240 cm³)`
  *   **平均毛利率**：`63.63%`
  *   **卖家所属地**：`美国|59.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-24. Desk & Shelf Clocks (台钟和座钟)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Clocks › Desk & Shelf Clocks  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.40`
  *   **平均 Reviews (Avg Reviews)**：`727 个`
  *   **物理重量 (Weight)**：`1.50 lbs`
  *   **平均退货率 (Return Rate)**：`7.44%`
  *   **平均毛利率 (Profit Margin)**：`66.36%`
  *   **品牌集中度 (Brand Concentration)**：`62.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Clocks › Desk & Shelf Clocks  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 钟表 › 台钟和座钟`
  *   **A+数量占比**：`75%`
  *   **新品平均评分数**：`52`
  *   **新品平均价格**：`$ 40.84`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`213`
  *   **新品月均销售额**：`$8,284`
  *   **平均重量**：`1.50 pounds (679 g)`
  *   **平均体积**：`99.37 in³ (1,628 cm³)`
  *   **平均毛利率**：`66.36%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`3.8‰`

---

#### 🏆 🟢-25. Oolong (乌龙)

- **完整市场路径**：`Grocery & Gourmet Food › Beverages › Tea › Oolong  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.90`
  *   **平均 Reviews (Avg Reviews)**：`447 个`
  *   **物理重量 (Weight)**：`0.46 lbs`
  *   **平均退货率 (Return Rate)**：`0.26%`
  *   **平均毛利率 (Profit Margin)**：`59.09%`
  *   **品牌集中度 (Brand Concentration)**：`60.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`53.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Grocery & Gourmet Food › Beverages › Tea › Oolong  市场分析`
  *   **市场路径(中文)**：`杂货店 › 饮料 › 茶叶 › 乌龙`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`57`
  *   **新品平均价格**：`$ 24.99`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`423`
  *   **新品月均销售额**：`$11,423`
  *   **平均重量**：`0.46 pounds (211 g)`
  *   **平均体积**：`113.03 in³ (1,852 cm³)`
  *   **平均毛利率**：`59.09%`
  *   **卖家所属地**：`美国|47.0%`
  *   **搜索购买比**：`18.2‰`

---

#### 🏆 🟢-26. Locks (锁具)

- **完整市场路径**：`Automotive › RV Parts & Accessories › Safety & Security › Locks  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$44.51`
  *   **平均 Reviews (Avg Reviews)**：`639 个`
  *   **物理重量 (Weight)**：`1.72 lbs`
  *   **平均退货率 (Return Rate)**：`5.73%`
  *   **平均毛利率 (Profit Margin)**：`59.26%`
  *   **品牌集中度 (Brand Concentration)**：`59.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › RV Parts & Accessories › Safety & Security › Locks  市场分析`
  *   **市场路径(中文)**：`汽车 › 房车配件 › 安全问题 › 锁具`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 40.66`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`280`
  *   **新品月均销售额**：`$6,660`
  *   **平均重量**：`1.72 pounds (780 g)`
  *   **平均体积**：`72.50 in³ (1,188 cm³)`
  *   **平均毛利率**：`59.26%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`9.2‰`

---

#### 🏆 🟢-27. Insulin Injectors (胰岛素注射器)

- **完整市场路径**：`Health & Household › Health Care › Diabetes Care › Insulin Injectors  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.72`
  *   **平均 Reviews (Avg Reviews)**：`463 个`
  *   **物理重量 (Weight)**：`0.43 lbs`
  *   **平均退货率 (Return Rate)**：`1.5%`
  *   **平均毛利率 (Profit Margin)**：`61.22%`
  *   **品牌集中度 (Brand Concentration)**：`64.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`41.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Diabetes Care › Insulin Injectors  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 糖尿病护理 › 胰岛素注射器`
  *   **A+数量占比**：`51%`
  *   **新品平均评分数**：`99`
  *   **新品平均价格**：`$ 26.64`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`309`
  *   **新品月均销售额**：`$7,889`
  *   **平均重量**：`0.43 pounds (195 g)`
  *   **平均体积**：`119.09 in³ (1,951 cm³)`
  *   **平均毛利率**：`61.22%`
  *   **卖家所属地**：`美国|59.0%`
  *   **搜索购买比**：`24.9‰`

---

#### 🏆 🟢-28. Honey Jars (蜂蜜罐子)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Honey Jars  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.84`
  *   **平均 Reviews (Avg Reviews)**：`648 个`
  *   **物理重量 (Weight)**：`1.92 lbs`
  *   **平均退货率 (Return Rate)**：`5.4%`
  *   **平均毛利率 (Profit Margin)**：`53.88%`
  *   **品牌集中度 (Brand Concentration)**：`47.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Honey Jars  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 小甜甜 › 碗碟 › 蜂蜜罐子`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`26`
  *   **新品平均价格**：`$ 16.96`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`209`
  *   **新品月均销售额**：`$3,695`
  *   **平均重量**：`1.92 pounds (873 g)`
  *   **平均体积**：`125.08 in³ (2,050 cm³)`
  *   **平均毛利率**：`53.88%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`7.8‰`

---

#### 🏆 🟢-29. Repair Kits (维修套件)

- **完整市场路径**：`Cell Phones & Accessories › Accessories › Maintenance, Upkeep & Repairs › Repair Kits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.87`
  *   **平均 Reviews (Avg Reviews)**：`638 个`
  *   **物理重量 (Weight)**：`0.21 lbs`
  *   **平均退货率 (Return Rate)**：`5.69%`
  *   **平均毛利率 (Profit Margin)**：`69.23%`
  *   **品牌集中度 (Brand Concentration)**：`64.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Cell Phones & Accessories › Accessories › Maintenance, Upkeep & Repairs › Repair Kits  市场分析`
  *   **市场路径(中文)**：`手机 › 辅料 › 维护，保养 › 维修套件`
  *   **A+数量占比**：`57%`
  *   **新品平均评分数**：`59`
  *   **新品平均价格**：`$ 53.16`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`181`
  *   **新品月均销售额**：`$10,163`
  *   **平均重量**：`0.21 pounds (97 g)`
  *   **平均体积**：`31.03 in³ (508 cm³)`
  *   **平均毛利率**：`69.23%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`13.8‰`

---

#### 🏆 🟢-30. Welding Helmets (焊接头盔)

- **完整市场路径**：`Tools & Home Improvement › Safety & Security › Personal Protective Equipment › Head Protection › Welding Helmets  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$60.23`
  *   **平均 Reviews (Avg Reviews)**：`756 个`
  *   **物理重量 (Weight)**：`1.18 lbs`
  *   **平均退货率 (Return Rate)**：`3.46%`
  *   **平均毛利率 (Profit Margin)**：`64.28%`
  *   **品牌集中度 (Brand Concentration)**：`61.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Safety & Security › Personal Protective Equipment › Head Protection › Welding Helmets  市场分析`
  *   **市场路径(中文)**：`工具 › 安全问题 › 个人防护设备 › 头部保护 › 焊接头盔`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`180`
  *   **新品平均价格**：`$ 72.97`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`243`
  *   **新品月均销售额**：`$17,197`
  *   **平均重量**：`1.18 pounds (534 g)`
  *   **平均体积**：`516.08 in³ (8,457 cm³)`
  *   **平均毛利率**：`64.28%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`5.0‰`

---

#### 🏆 🟢-31. Tattoo Kits (纹身套装)

- **完整市场路径**：`Beauty & Personal Care › Personal Care › Piercing & Tattoo Supplies › Tattoo Supplies › Tattoo Kits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.97`
  *   **平均 Reviews (Avg Reviews)**：`487 个`
  *   **物理重量 (Weight)**：`1.48 lbs`
  *   **平均退货率 (Return Rate)**：`2.09%`
  *   **平均毛利率 (Profit Margin)**：`59.15%`
  *   **品牌集中度 (Brand Concentration)**：`63.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Beauty & Personal Care › Personal Care › Piercing & Tattoo Supplies › Tattoo Supplies › Tattoo Kits  市场分析`
  *   **市场路径(中文)**：`美容与护理 › 沐浴 › 穿洞和纹身用品 › 纹身用品 › 纹身套装`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`64`
  *   **新品平均价格**：`$ 33.17`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`189`
  *   **新品月均销售额**：`$6,063`
  *   **平均重量**：`1.48 pounds (673 g)`
  *   **平均体积**：`208.91 in³ (3,423 cm³)`
  *   **平均毛利率**：`59.15%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-32. Deck Hardware (五金件)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Hardware › Deck Hardware  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.38`
  *   **平均 Reviews (Avg Reviews)**：`440 个`
  *   **物理重量 (Weight)**：`1.66 lbs`
  *   **平均退货率 (Return Rate)**：`4.94%`
  *   **平均毛利率 (Profit Margin)**：`58.66%`
  *   **品牌集中度 (Brand Concentration)**：`46.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Hardware › Deck Hardware  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 船五金 › 五金件`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`33`
  *   **新品平均价格**：`$ 31.42`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`345`
  *   **新品月均销售额**：`$12,190`
  *   **平均重量**：`1.66 pounds (751 g)`
  *   **平均体积**：`588.86 in³ (9,650 cm³)`
  *   **平均毛利率**：`58.66%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟢-33. Drill Bits (钻头)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.27`
  *   **平均 Reviews (Avg Reviews)**：`281 个`
  *   **物理重量 (Weight)**：`0.96 lbs`
  *   **平均退货率 (Return Rate)**：`2.68%`
  *   **平均毛利率 (Profit Margin)**：`59.57%`
  *   **品牌集中度 (Brand Concentration)**：`52.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 电动工具零件 › 电钻零件 › 钻头`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`82`
  *   **新品平均价格**：`$ 22.24`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`240`
  *   **新品月均销售额**：`$5,107`
  *   **平均重量**：`0.96 pounds (437 g)`
  *   **平均体积**：`73.11 in³ (1,198 cm³)`
  *   **平均毛利率**：`59.57%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`12.4‰`

---

#### 🏆 🟢-34. Grinding Discs (磨片)

- **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.59`
  *   **平均 Reviews (Avg Reviews)**：`343 个`
  *   **物理重量 (Weight)**：`1.97 lbs`
  *   **平均退货率 (Return Rate)**：`2.13%`
  *   **平均毛利率 (Profit Margin)**：`61.78%`
  *   **品牌集中度 (Brand Concentration)**：`45.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Grinding Discs  市场分析`
  *   **市场路径(中文)**：`工业类 › 磨削加工 › 研磨砂轮 › 磨片`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`46`
  *   **新品平均价格**：`$ 23.03`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`236`
  *   **新品月均销售额**：`$5,441`
  *   **平均重量**：`1.97 pounds (894 g)`
  *   **平均体积**：`11.27 in³ (185 cm³)`
  *   **平均毛利率**：`61.78%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`15.0‰`

---

#### 🏆 🟢-35. Countersink Drill Bits (沉孔钻头)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits › Countersink Drill Bits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.35`
  *   **平均 Reviews (Avg Reviews)**：`572 个`
  *   **物理重量 (Weight)**：`0.47 lbs`
  *   **平均退货率 (Return Rate)**：`1.85%`
  *   **平均毛利率 (Profit Margin)**：`62.67%`
  *   **品牌集中度 (Brand Concentration)**：`53.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits › Countersink Drill Bits  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 电动工具零件 › 电钻零件 › 钻头 › 沉孔钻头`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`47`
  *   **新品平均价格**：`$ 23.19`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`244`
  *   **新品月均销售额**：`$5,777`
  *   **平均重量**：`0.47 pounds (212 g)`
  *   **平均体积**：`32.10 in³ (526 cm³)`
  *   **平均毛利率**：`62.67%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`10.5‰`

---

#### 🏆 🟢-36. Soap & Lotion Dispensers (肥皂)

- **完整市场路径**：`Industrial & Scientific › Janitorial & Sanitation Supplies › Personal Care Products › Soap & Lotion Dispensers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.89`
  *   **平均 Reviews (Avg Reviews)**：`683 个`
  *   **物理重量 (Weight)**：`1.69 lbs`
  *   **平均退货率 (Return Rate)**：`5.55%`
  *   **平均毛利率 (Profit Margin)**：`57.84%`
  *   **品牌集中度 (Brand Concentration)**：`55.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`50.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Janitorial & Sanitation Supplies › Personal Care Products › Soap & Lotion Dispensers  市场分析`
  *   **市场路径(中文)**：`工业类 › 门卫 › 个人护理产品 › 肥皂`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 17.82`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`208`
  *   **新品月均销售额**：`$3,147`
  *   **平均重量**：`1.69 pounds (767 g)`
  *   **平均体积**：`267.13 in³ (4,377 cm³)`
  *   **平均毛利率**：`57.84%`
  *   **卖家所属地**：`中国|50.0%`
  *   **搜索购买比**：`11.7‰`

---

#### 🏆 🟢-37. Turn Signal Assemblies & Lenses (转向信号组件)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Lights › Turn Signal Assemblies & Lenses  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.47`
  *   **平均 Reviews (Avg Reviews)**：`567 个`
  *   **物理重量 (Weight)**：`0.73 lbs`
  *   **平均退货率 (Return Rate)**：`6.77%`
  *   **平均毛利率 (Profit Margin)**：`62.6%`
  *   **品牌集中度 (Brand Concentration)**：`59.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`85.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Lights › Turn Signal Assemblies & Lenses  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 部分 › 灯光 › 转向信号组件`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`120`
  *   **新品平均价格**：`$ 59.11`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`756`
  *   **新品月均销售额**：`$40,127`
  *   **平均重量**：`0.73 pounds (332 g)`
  *   **平均体积**：`82.20 in³ (1,347 cm³)`
  *   **平均毛利率**：`62.6%`
  *   **卖家所属地**：`中国|85.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟢-38. Handlebar Mounts (Handlebar Mounts)

- **完整市场路径**：`Cell Phones & Accessories › Accessories › Mounts › Handlebar Mounts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.60`
  *   **平均 Reviews (Avg Reviews)**：`589 个`
  *   **物理重量 (Weight)**：`0.58 lbs`
  *   **平均退货率 (Return Rate)**：`5.37%`
  *   **平均毛利率 (Profit Margin)**：`69.23%`
  *   **品牌集中度 (Brand Concentration)**：`55.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Cell Phones & Accessories › Accessories › Mounts › Handlebar Mounts  市场分析`
  *   **市场路径(中文)**：`Cell Phones & Accessories › Accessories › Mounts › Handlebar Mounts`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`61`
  *   **新品平均价格**：`$ 22.46`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`162`
  *   **新品月均销售额**：`$3,131`
  *   **平均重量**：`0.58 pounds (261 g)`
  *   **平均体积**：`43.64 in³ (715 cm³)`
  *   **平均毛利率**：`69.23%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`8.0‰`

---

#### 🏆 🟢-39. Tie-Downs (栓系器具)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Trailer Accessories › Tie-Downs  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.67`
  *   **平均 Reviews (Avg Reviews)**：`552 个`
  *   **物理重量 (Weight)**：`1.59 lbs`
  *   **平均退货率 (Return Rate)**：`3.74%`
  *   **平均毛利率 (Profit Margin)**：`58.56%`
  *   **品牌集中度 (Brand Concentration)**：`58.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`52.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Trailer Accessories › Tie-Downs  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 拖船配件 › 栓系器具`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`119`
  *   **新品平均价格**：`$ 33.65`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`277`
  *   **新品月均销售额**：`$9,612`
  *   **平均重量**：`1.59 pounds (721 g)`
  *   **平均体积**：`146.45 in³ (2,400 cm³)`
  *   **平均毛利率**：`58.56%`
  *   **卖家所属地**：`中国|52.0%`
  *   **搜索购买比**：`10.5‰`

---

#### 🏆 🟢-40. Exterior Lighting (外部照明)

- **完整市场路径**：`Automotive › RV Parts & Accessories › Power & Electrical › Lighting › Exterior Lighting  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.24`
  *   **平均 Reviews (Avg Reviews)**：`478 个`
  *   **物理重量 (Weight)**：`0.77 lbs`
  *   **平均退货率 (Return Rate)**：`4.66%`
  *   **平均毛利率 (Profit Margin)**：`62.34%`
  *   **品牌集中度 (Brand Concentration)**：`52.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › RV Parts & Accessories › Power & Electrical › Lighting › Exterior Lighting  市场分析`
  *   **市场路径(中文)**：`汽车 › 房车配件 › 权力 › 照明 › 外部照明`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`448`
  *   **新品平均价格**：`$ 30.54`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`222`
  *   **新品月均销售额**：`$6,779`
  *   **平均重量**：`0.77 pounds (351 g)`
  *   **平均体积**：`200.34 in³ (3,283 cm³)`
  *   **平均毛利率**：`62.34%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟢-41. Wood Burning Tools (木材燃烧工具)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Woodcrafts › Wood Burning Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.81`
  *   **平均 Reviews (Avg Reviews)**：`567 个`
  *   **物理重量 (Weight)**：`1.05 lbs`
  *   **平均退货率 (Return Rate)**：`4.0%`
  *   **平均毛利率 (Profit Margin)**：`65.41%`
  *   **品牌集中度 (Brand Concentration)**：`53.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Woodcrafts › Wood Burning Tools  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 木制工艺品 › 木材燃烧工具`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`77`
  *   **新品平均价格**：`$ 22.07`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`311`
  *   **新品月均销售额**：`$5,006`
  *   **平均重量**：`1.05 pounds (475 g)`
  *   **平均体积**：`74.39 in³ (1,219 cm³)`
  *   **平均毛利率**：`65.41%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-42. Pipe Clamps (管夹)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Workholding Devices › Clamps › Pipe Clamps  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.87`
  *   **平均 Reviews (Avg Reviews)**：`282 个`
  *   **物理重量 (Weight)**：`1.85 lbs`
  *   **平均退货率 (Return Rate)**：`5.92%`
  *   **平均毛利率 (Profit Margin)**：`54.68%`
  *   **品牌集中度 (Brand Concentration)**：`42.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Workholding Devices › Clamps › Pipe Clamps  市场分析`
  *   **市场路径(中文)**：`工具和家庭装修 › 电动和手动工具 › 手动工具 › 工件夹持装置 › 夹钳 › 管夹`
  *   **A+数量占比**：`64%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 24.77`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`140`
  *   **新品月均销售额**：`$3,155`
  *   **平均重量**：`1.85 pounds (838 g)`
  *   **平均体积**：`82.34 in³ (1,349 cm³)`
  *   **平均毛利率**：`54.68%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`11.9‰`

---

#### 🏆 🟢-43. Headlights (车头灯)

- **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Accessories › Lights & Reflectors › Headlights  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.36`
  *   **平均 Reviews (Avg Reviews)**：`449 个`
  *   **物理重量 (Weight)**：`0.46 lbs`
  *   **平均退货率 (Return Rate)**：`5.21%`
  *   **平均毛利率 (Profit Margin)**：`66.96%`
  *   **品牌集中度 (Brand Concentration)**：`46.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Accessories › Lights & Reflectors › Headlights  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 骑自行车 › 配件 › 车灯、镜面反射 › 车头灯`
  *   **A+数量占比**：`93%`
  *   **新品平均评分数**：`48`
  *   **新品平均价格**：`$ 24.27`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`337`
  *   **新品月均销售额**：`$7,188`
  *   **平均重量**：`0.46 pounds (210 g)`
  *   **平均体积**：`27.05 in³ (443 cm³)`
  *   **平均毛利率**：`66.96%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`4.7‰`

---

#### 🏆 🟢-44. Cookbook Stands (菜谱架)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Accessories › Cookbook Stands & Recipe Holders › Cookbook Stands  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.94`
  *   **平均 Reviews (Avg Reviews)**：`565 个`
  *   **物理重量 (Weight)**：`1.95 lbs`
  *   **平均退货率 (Return Rate)**：`6.17%`
  *   **平均毛利率 (Profit Margin)**：`55.13%`
  *   **品牌集中度 (Brand Concentration)**：`48.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Accessories › Cookbook Stands & Recipe Holders › Cookbook Stands  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 厨房配件 › 菜谱架 › 菜谱架`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 19.21`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`193`
  *   **新品月均销售额**：`$3,074`
  *   **平均重量**：`1.95 pounds (884 g)`
  *   **平均体积**：`539.84 in³ (8,846 cm³)`
  *   **平均毛利率**：`55.13%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`7.0‰`

---

#### 🏆 🟢-45. Forstner Drill Bits (费式钻头)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits › Forstner Drill Bits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.80`
  *   **平均 Reviews (Avg Reviews)**：`510 个`
  *   **物理重量 (Weight)**：`0.72 lbs`
  *   **平均退货率 (Return Rate)**：`4.11%`
  *   **平均毛利率 (Profit Margin)**：`57.69%`
  *   **品牌集中度 (Brand Concentration)**：`57.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Power Tool Parts & Accessories › Power Drill Parts & Accessories › Drill Bits › Forstner Drill Bits  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 电动工具零件 › 电钻零件 › 钻头 › 费式钻头`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`202`
  *   **新品平均价格**：`$ 17.8`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`264`
  *   **新品月均销售额**：`$5,018`
  *   **平均重量**：`0.72 pounds (329 g)`
  *   **平均体积**：`65.62 in³ (1,075 cm³)`
  *   **平均毛利率**：`57.69%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`12.0‰`

---

#### 🏆 🟢-46. Sound Therapy (声音疗法)

- **完整市场路径**：`Health & Household › Health Care › Alternative Medicine › Sound Therapy  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$43.04`
  *   **平均 Reviews (Avg Reviews)**：`249 个`
  *   **物理重量 (Weight)**：`0.95 lbs`
  *   **平均退货率 (Return Rate)**：`6.32%`
  *   **平均毛利率 (Profit Margin)**：`67.13%`
  *   **品牌集中度 (Brand Concentration)**：`44.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Alternative Medicine › Sound Therapy  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 替代药物 › 声音疗法`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`51`
  *   **新品平均价格**：`$ 35.62`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`237`
  *   **新品月均销售额**：`$8,529`
  *   **平均重量**：`0.95 pounds (429 g)`
  *   **平均体积**：`95.71 in³ (1,568 cm³)`
  *   **平均毛利率**：`67.13%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`10.1‰`

---

#### 🏆 🟢-47. Recipe Holders (食谱夹子)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Accessories › Cookbook Stands & Recipe Holders › Recipe Holders  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.04`
  *   **平均 Reviews (Avg Reviews)**：`511 个`
  *   **物理重量 (Weight)**：`1.39 lbs`
  *   **平均退货率 (Return Rate)**：`5.89%`
  *   **平均毛利率 (Profit Margin)**：`56.71%`
  *   **品牌集中度 (Brand Concentration)**：`45.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Accessories › Cookbook Stands & Recipe Holders › Recipe Holders  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 厨房配件 › 菜谱架 › 食谱夹子`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`42`
  *   **新品平均价格**：`$ 18.47`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`220`
  *   **新品月均销售额**：`$4,465`
  *   **平均重量**：`1.39 pounds (632 g)`
  *   **平均体积**：`128.68 in³ (2,109 cm³)`
  *   **平均毛利率**：`56.71%`
  *   **卖家所属地**：`中国|48.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟢-48. Meat Cleavers (切肉刀)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Cleavers › Meat Cleavers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$45.22`
  *   **平均 Reviews (Avg Reviews)**：`644 个`
  *   **物理重量 (Weight)**：`1.49 lbs`
  *   **平均退货率 (Return Rate)**：`3.99%`
  *   **平均毛利率 (Profit Margin)**：`65.77%`
  *   **品牌集中度 (Brand Concentration)**：`63.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Cleavers › Meat Cleavers  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 刀具厨房及配件 › 切肉刀 › 切肉刀`
  *   **A+数量占比**：`97%`
  *   **新品平均评分数**：`20`
  *   **新品平均价格**：`$ 32.19`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`149`
  *   **新品月均销售额**：`$4,502`
  *   **平均重量**：`1.49 pounds (675 g)`
  *   **平均体积**：`132.95 in³ (2,179 cm³)`
  *   **平均毛利率**：`65.77%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`4.7‰`

---

#### 🏆 🟢-49. Cooking Utensils (厨具)

- **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Camp Kitchen › Cooking Utensils  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.82`
  *   **平均 Reviews (Avg Reviews)**：`692 个`
  *   **物理重量 (Weight)**：`1.77 lbs`
  *   **平均退货率 (Return Rate)**：`3.17%`
  *   **平均毛利率 (Profit Margin)**：`59.56%`
  *   **品牌集中度 (Brand Concentration)**：`56.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`44.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Camp Kitchen › Cooking Utensils  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 外出休闲 › 露营和远足 › 露营炊具 › 厨具`
  *   **A+数量占比**：`79%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 24.4`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`128`
  *   **新品月均销售额**：`$3,045`
  *   **平均重量**：`1.77 pounds (802 g)`
  *   **平均体积**：`370.17 in³ (6,066 cm³)`
  *   **平均毛利率**：`59.56%`
  *   **卖家所属地**：`中国|44.0%`
  *   **搜索购买比**：`5.3‰`

---

#### 🏆 🟢-50. Float Valves (浮阀)

- **完整市场路径**：`Industrial & Scientific › Hydraulics, Pneumatics & Plumbing › Fittings › Valves › Float Valves  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.24`
  *   **平均 Reviews (Avg Reviews)**：`185 个`
  *   **物理重量 (Weight)**：`0.66 lbs`
  *   **平均退货率 (Return Rate)**：`4.44%`
  *   **平均毛利率 (Profit Margin)**：`61.24%`
  *   **品牌集中度 (Brand Concentration)**：`40.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Hydraulics, Pneumatics & Plumbing › Fittings › Valves › Float Valves  市场分析`
  *   **市场路径(中文)**：`工业类 › 液压系统、气动系统 › 配件 › 阀门 › 浮阀`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`23`
  *   **新品平均价格**：`$ 22.28`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`182`
  *   **新品月均销售额**：`$3,845`
  *   **平均重量**：`0.66 pounds (299 g)`
  *   **平均体积**：`107.34 in³ (1,759 cm³)`
  *   **平均毛利率**：`61.24%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`15.7‰`

---

#### 🏆 🟢-51. Seat Belts (安全带)

- **完整市场路径**：`Automotive › Replacement Parts › Body & Trim › Trim › Interior › Seat Belts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.72`
  *   **平均 Reviews (Avg Reviews)**：`198 个`
  *   **物理重量 (Weight)**：`1.52 lbs`
  *   **平均退货率 (Return Rate)**：`5.78%`
  *   **平均毛利率 (Profit Margin)**：`59.06%`
  *   **品牌集中度 (Brand Concentration)**：`54.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Body & Trim › Trim › Interior › Seat Belts  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 身体 › 饰面 › 室内 › 安全带`
  *   **A+数量占比**：`53%`
  *   **新品平均评分数**：`36`
  *   **新品平均价格**：`$ 23.28`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`332`
  *   **新品月均销售额**：`$7,030`
  *   **平均重量**：`1.52 pounds (690 g)`
  *   **平均体积**：`312.04 in³ (5,113 cm³)`
  *   **平均毛利率**：`59.06%`
  *   **卖家所属地**：`中国|76.0%`
  *   **搜索购买比**：`4.3‰`

---

#### 🏆 🟢-52. Leak Detection Tools (泄漏检测工具)

- **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Inspection & Analysis › Leak Detection Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$99.91`
  *   **平均 Reviews (Avg Reviews)**：`146 个`
  *   **物理重量 (Weight)**：`1.46 lbs`
  *   **平均退货率 (Return Rate)**：`4.3%`
  *   **平均毛利率 (Profit Margin)**：`69.15%`
  *   **品牌集中度 (Brand Concentration)**：`52.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`48.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Inspection & Analysis › Leak Detection Tools  市场分析`
  *   **市场路径(中文)**：`工业类 › 测试，测量 › 检查 › 泄漏检测工具`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`28`
  *   **新品平均价格**：`$ 81.17`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`323`
  *   **新品月均销售额**：`$10,720`
  *   **平均重量**：`1.46 pounds (663 g)`
  *   **平均体积**：`194.48 in³ (3,187 cm³)`
  *   **平均毛利率**：`69.15%`
  *   **卖家所属地**：`中国|48.0%`
  *   **搜索购买比**：`12.8‰`

---

#### 🏆 🟢-53. Tactical Vests (战术背心)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Tactical & Personal Defense › Protective Body Equipment › Tactical Vests  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$48.58`
  *   **平均 Reviews (Avg Reviews)**：`537 个`
  *   **物理重量 (Weight)**：`1.50 lbs`
  *   **平均退货率 (Return Rate)**：`7.91%`
  *   **平均毛利率 (Profit Margin)**：`63.73%`
  *   **品牌集中度 (Brand Concentration)**：`55.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Tactical & Personal Defense › Protective Body Equipment › Tactical Vests  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 战术性 › 防护身体装备 › 战术背心`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`112`
  *   **新品平均价格**：`$ 51.89`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`173`
  *   **新品月均销售额**：`$7,487`
  *   **平均重量**：`1.50 pounds (681 g)`
  *   **平均体积**：`573.52 in³ (9,398 cm³)`
  *   **平均毛利率**：`63.73%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`2.0‰`

---

#### 🏆 🟢-54. Seat Covers (摩托车座套)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Seat Covers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.50`
  *   **平均 Reviews (Avg Reviews)**：`305 个`
  *   **物理重量 (Weight)**：`1.09 lbs`
  *   **平均退货率 (Return Rate)**：`5.29%`
  *   **平均毛利率 (Profit Margin)**：`63.96%`
  *   **品牌集中度 (Brand Concentration)**：`49.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Seat Covers  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 辅料 › 摩托车座套`
  *   **A+数量占比**：`78%`
  *   **新品平均评分数**：`39`
  *   **新品平均价格**：`$ 26.98`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`169`
  *   **新品月均销售额**：`$4,500`
  *   **平均重量**：`1.09 pounds (495 g)`
  *   **平均体积**：`252.04 in³ (4,130 cm³)`
  *   **平均毛利率**：`63.96%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`3.0‰`

---

#### 🏆 🟢-55. Angle Grinder Wheels (角磨机砂轮)

- **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Angle Grinder Wheels  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.63`
  *   **平均 Reviews (Avg Reviews)**：`142 个`
  *   **物理重量 (Weight)**：`1.51 lbs`
  *   **平均退货率 (Return Rate)**：`2.41%`
  *   **平均毛利率 (Profit Margin)**：`63.12%`
  *   **品牌集中度 (Brand Concentration)**：`50.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Angle Grinder Wheels  市场分析`
  *   **市场路径(中文)**：`工业类 › 磨削加工 › 研磨砂轮 › 角磨机砂轮`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`5`
  *   **新品平均价格**：`$ 24.12`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`110`
  *   **新品月均销售额**：`$2,469`
  *   **平均重量**：`1.51 pounds (686 g)`
  *   **平均体积**：`14.09 in³ (231 cm³)`
  *   **平均毛利率**：`63.12%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`15.4‰`

---

#### 🏆 🟢-56. Tortilla Servers (玉米饼服务员)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Tortilla Servers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.62`
  *   **平均 Reviews (Avg Reviews)**：`474 个`
  *   **物理重量 (Weight)**：`1.57 lbs`
  *   **平均退货率 (Return Rate)**：`6.26%`
  *   **平均毛利率 (Profit Margin)**：`51.8%`
  *   **品牌集中度 (Brand Concentration)**：`57.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`39.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Tortilla Servers  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 小甜甜 › 碗碟 › 玉米饼服务员`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 20.06`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`85`
  *   **新品月均销售额**：`$1,619`
  *   **平均重量**：`1.57 pounds (711 g)`
  *   **平均体积**：`293.64 in³ (4,812 cm³)`
  *   **平均毛利率**：`51.8%`
  *   **卖家所属地**：`中国|39.0%`
  *   **搜索购买比**：`6.5‰`

---

#### 🏆 🟢-57. Optics Accessories (光学配件)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Shooting › Optics › Optics Accessories  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.80`
  *   **平均 Reviews (Avg Reviews)**：`353 个`
  *   **物理重量 (Weight)**：`0.20 lbs`
  *   **平均退货率 (Return Rate)**：`5.63%`
  *   **平均毛利率 (Profit Margin)**：`65.29%`
  *   **品牌集中度 (Brand Concentration)**：`51.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`40.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Shooting › Optics › Optics Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 射击 › 光学元件 › 光学配件`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 14.73`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`149`
  *   **新品月均销售额**：`$2,215`
  *   **平均重量**：`0.20 pounds (89 g)`
  *   **平均体积**：`21.21 in³ (348 cm³)`
  *   **平均毛利率**：`65.29%`
  *   **卖家所属地**：`美国|60.0%`
  *   **搜索购买比**：`6.2‰`

---

#### 🏆 🟢-58. Weaving Looms (织机)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Weaving & Spinning › Weaving Looms  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.17`
  *   **平均 Reviews (Avg Reviews)**：`389 个`
  *   **物理重量 (Weight)**：`1.06 lbs`
  *   **平均退货率 (Return Rate)**：`3.33%`
  *   **平均毛利率 (Profit Margin)**：`55.73%`
  *   **品牌集中度 (Brand Concentration)**：`57.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Weaving & Spinning › Weaving Looms  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 纺织 › 织机`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 18.94`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`94`
  *   **新品月均销售额**：`$1,634`
  *   **平均重量**：`1.06 pounds (479 g)`
  *   **平均体积**：`111.68 in³ (1,830 cm³)`
  *   **平均毛利率**：`55.73%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`5.6‰`

---

#### 🏆 🟢-59. Canvas Tools & Accessories (帆布工具)

- **完整市场路径**：`Arts, Crafts & Sewing › Painting, Drawing & Art Supplies › Boards & Canvas › Canvas Tools & Accessories  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.57`
  *   **平均 Reviews (Avg Reviews)**：`268 个`
  *   **物理重量 (Weight)**：`1.07 lbs`
  *   **平均退货率 (Return Rate)**：`7.32%`
  *   **平均毛利率 (Profit Margin)**：`53.75%`
  *   **品牌集中度 (Brand Concentration)**：`51.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Painting, Drawing & Art Supplies › Boards & Canvas › Canvas Tools & Accessories  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 油画、素描 › 板块 › 帆布工具`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`14`
  *   **新品平均价格**：`$ 22.2`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`144`
  *   **新品月均销售额**：`$3,258`
  *   **平均重量**：`1.07 pounds (485 g)`
  *   **平均体积**：`205.36 in³ (3,365 cm³)`
  *   **平均毛利率**：`53.75%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`8.1‰`

---

#### 🏆 🟢-60. Growth Charts (身高墙贴)

- **完整市场路径**：`Baby Products › Nursery › Décor › Wall Décor › Growth Charts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.53`
  *   **平均 Reviews (Avg Reviews)**：`419 个`
  *   **物理重量 (Weight)**：`0.79 lbs`
  *   **平均退货率 (Return Rate)**：`3.72%`
  *   **平均毛利率 (Profit Margin)**：`57.97%`
  *   **品牌集中度 (Brand Concentration)**：`48.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Baby Products › Nursery › Décor › Wall Décor › Growth Charts  市场分析`
  *   **市场路径(中文)**：`婴儿产品 › 苗圃 › 装饰品 › 墙面装饰 › 身高墙贴`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`10`
  *   **新品平均价格**：`$ 15.38`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`75`
  *   **新品月均销售额**：`$1,211`
  *   **平均重量**：`0.79 pounds (359 g)`
  *   **平均体积**：`254.91 in³ (4,177 cm³)`
  *   **平均毛利率**：`57.97%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟢-61. Bumper Guards (保险杠防护装置)

- **完整市场路径**：`Automotive › Exterior Accessories › Bumpers & Bumper Accessories › Bumper Guards  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.16`
  *   **平均 Reviews (Avg Reviews)**：`466 个`
  *   **物理重量 (Weight)**：`1.67 lbs`
  *   **平均退货率 (Return Rate)**：`7.85%`
  *   **平均毛利率 (Profit Margin)**：`58.0%`
  *   **品牌集中度 (Brand Concentration)**：`38.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Exterior Accessories › Bumpers & Bumper Accessories › Bumper Guards  市场分析`
  *   **市场路径(中文)**：`汽车 › 外部配件 › 保险杠 › 保险杠防护装置`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 32.93`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`131`
  *   **新品月均销售额**：`$3,884`
  *   **平均重量**：`1.67 pounds (758 g)`
  *   **平均体积**：`422.96 in³ (6,931 cm³)`
  *   **平均毛利率**：`58%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`4.3‰`

---

#### 🏆 🟢-62. Fly Tying Equipment (绑蝇设备)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Fly Fishing › Accessories › Fly Tying Equipment  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.38`
  *   **平均 Reviews (Avg Reviews)**：`489 个`
  *   **物理重量 (Weight)**：`0.25 lbs`
  *   **平均退货率 (Return Rate)**：`2.84%`
  *   **平均毛利率 (Profit Margin)**：`60.79%`
  *   **品牌集中度 (Brand Concentration)**：`61.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`50.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Fly Fishing › Accessories › Fly Tying Equipment  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 钓鱼 › 飞钓 › 配件 › 绑蝇设备`
  *   **A+数量占比**：`46%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 17.35`
  *   **新品平均星级**：`2.7`
  *   **新品月均销量**：`119`
  *   **新品月均销售额**：`$1,991`
  *   **平均重量**：`0.25 pounds (115 g)`
  *   **平均体积**：`46.03 in³ (754 cm³)`
  *   **平均毛利率**：`60.79%`
  *   **卖家所属地**：`中国|50.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟢-63. Trim (装饰)

- **完整市场路径**：`Power & Hand Tools › Power Tool Parts & Accessories › Router Parts & Accessories › Router Bits › Straight, Spiral & Trim Bits › Trim  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.92`
  *   **平均 Reviews (Avg Reviews)**：`252 个`
  *   **物理重量 (Weight)**：`0.27 lbs`
  *   **平均退货率 (Return Rate)**：`2.44%`
  *   **平均毛利率 (Profit Margin)**：`66.38%`
  *   **品牌集中度 (Brand Concentration)**：`62.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Power & Hand Tools › Power Tool Parts & Accessories › Router Parts & Accessories › Router Bits › Straight, Spiral & Trim Bits › Trim  市场分析`
  *   **市场路径(中文)**：`电动和手动工具 › 电动工具零件 › 刳刨机零件 › 刳刨機鑽頭 › 直钻头、螺旋钻头和修整钻头 › 装饰`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`31`
  *   **新品平均价格**：`$ 34.89`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`123`
  *   **新品月均销售额**：`$4,274`
  *   **平均重量**：`0.27 pounds (124 g)`
  *   **平均体积**：`23.18 in³ (380 cm³)`
  *   **平均毛利率**：`66.38%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`11.3‰`

---

#### 🏆 🟢-64. Gutters (排水沟)

- **完整市场路径**：`Tools & Home Improvement › Building Supplies › Building Materials › Roofing › Gutters & Accessories › Gutters  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.12`
  *   **平均 Reviews (Avg Reviews)**：`159 个`
  *   **物理重量 (Weight)**：`1.61 lbs`
  *   **平均退货率 (Return Rate)**：`5.02%`
  *   **平均毛利率 (Profit Margin)**：`54.88%`
  *   **品牌集中度 (Brand Concentration)**：`52.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Building Supplies › Building Materials › Roofing › Gutters & Accessories › Gutters  市场分析`
  *   **市场路径(中文)**：`工具 › 建筑用品 › 建筑材料 › 屋顶工程 › 排水沟 › 排水沟`
  *   **A+数量占比**：`65%`
  *   **新品平均评分数**：`16`
  *   **新品平均价格**：`$ 27.27`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`109`
  *   **新品月均销售额**：`$2,975`
  *   **平均重量**：`1.61 pounds (730 g)`
  *   **平均体积**：`716.09 in³ (11,735 cm³)`
  *   **平均毛利率**：`54.88%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`10.7‰`

---

#### 🏆 🟢-65. Bait Traps (诱饵陷阱)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Baits & Accessories › Bait Traps  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.98`
  *   **平均 Reviews (Avg Reviews)**：`291 个`
  *   **物理重量 (Weight)**：`1.75 lbs`
  *   **平均退货率 (Return Rate)**：`3.31%`
  *   **平均毛利率 (Profit Margin)**：`53.45%`
  *   **品牌集中度 (Brand Concentration)**：`57.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`57.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Fishing › Baits & Accessories › Bait Traps  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 钓鱼 › 鱼饵和配件 › 诱饵陷阱`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`6`
  *   **新品平均价格**：`$ 27.59`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`94`
  *   **新品月均销售额**：`$2,404`
  *   **平均重量**：`1.75 pounds (793 g)`
  *   **平均体积**：`647.75 in³ (10,615 cm³)`
  *   **平均毛利率**：`53.45%`
  *   **卖家所属地**：`中国|57.0%`
  *   **搜索购买比**：`4.5‰`

---

#### 🏆 🟢-66. Flags (标志)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Cabin Products › Flags  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.22`
  *   **平均 Reviews (Avg Reviews)**：`222 个`
  *   **物理重量 (Weight)**：`0.56 lbs`
  *   **平均退货率 (Return Rate)**：`2.61%`
  *   **平均毛利率 (Profit Margin)**：`60.66%`
  *   **品牌集中度 (Brand Concentration)**：`60.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`52.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Boat Cabin Products › Flags  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 船用家具 › 标志`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`11`
  *   **新品平均价格**：`$ 22.32`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`245`
  *   **新品月均销售额**：`$5,810`
  *   **平均重量**：`0.56 pounds (254 g)`
  *   **平均体积**：`140.47 in³ (2,302 cm³)`
  *   **平均毛利率**：`60.66%`
  *   **卖家所属地**：`中国|52.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟢-67. Bags & Cases (麦克风箱包)

- **完整市场路径**：`Musical Instruments › Microphones & Accessories › Accessories › Bags & Cases  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.22`
  *   **平均 Reviews (Avg Reviews)**：`235 个`
  *   **物理重量 (Weight)**：`1.01 lbs`
  *   **平均退货率 (Return Rate)**：`6.87%`
  *   **平均毛利率 (Profit Margin)**：`58.53%`
  *   **品牌集中度 (Brand Concentration)**：`50.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Musical Instruments › Microphones & Accessories › Accessories › Bags & Cases  市场分析`
  *   **市场路径(中文)**：`乐器 › 显微镜 › 辅料 › 麦克风箱包`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 19.49`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`134`
  *   **新品月均销售额**：`$2,715`
  *   **平均重量**：`1.01 pounds (458 g)`
  *   **平均体积**：`370.82 in³ (6,077 cm³)`
  *   **平均毛利率**：`58.53%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟢-68. Tools (工具)

- **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Maintenance Supplies › Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.56`
  *   **平均 Reviews (Avg Reviews)**：`210 个`
  *   **物理重量 (Weight)**：`1.33 lbs`
  *   **平均退货率 (Return Rate)**：`3.64%`
  *   **平均毛利率 (Profit Margin)**：`62.81%`
  *   **品牌集中度 (Brand Concentration)**：`45.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`59.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Boating & Sailing › Boating › Maintenance Supplies › Tools  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 划船和珊瑚 › 划船 › 维修器材 › 工具`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`11`
  *   **新品平均价格**：`$ 33.98`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`151`
  *   **新品月均销售额**：`$4,414`
  *   **平均重量**：`1.33 pounds (603 g)`
  *   **平均体积**：`397.76 in³ (6,518 cm³)`
  *   **平均毛利率**：`62.81%`
  *   **卖家所属地**：`中国|59.0%`
  *   **搜索购买比**：`9.5‰`

---

#### 🏆 🟢-69. Pressure Regulators (压力调节器)

- **完整市场路径**：`Automotive › Replacement Parts › Fuel System › Fuel Injection › Pressure Regulators & Accessories › Pressure Regulators  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.79`
  *   **平均 Reviews (Avg Reviews)**：`291 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`5.93%`
  *   **平均毛利率 (Profit Margin)**：`66.66%`
  *   **品牌集中度 (Brand Concentration)**：`53.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Fuel System › Fuel Injection › Pressure Regulators & Accessories › Pressure Regulators  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 燃油系统 › 燃油喷射 › 压力调节器 › 压力调节器`
  *   **A+数量占比**：`66%`
  *   **新品平均评分数**：`26`
  *   **新品平均价格**：`$ 35.98`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`156`
  *   **新品月均销售额**：`$6,205`
  *   **平均重量**：`0.71 pounds (321 g)`
  *   **平均体积**：`78.65 in³ (1,289 cm³)`
  *   **平均毛利率**：`66.66%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`8.6‰`

---

#### 🏆 🟢-70. Fuel System (燃油系统)

- **完整市场路径**：`Automotive › Replacement Parts › Fuel System  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.87`
  *   **平均 Reviews (Avg Reviews)**：`97 个`
  *   **物理重量 (Weight)**：`0.60 lbs`
  *   **平均退货率 (Return Rate)**：`4.31%`
  *   **平均毛利率 (Profit Margin)**：`59.24%`
  *   **品牌集中度 (Brand Concentration)**：`49.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Fuel System  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 燃油系统`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 22.99`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`109`
  *   **新品月均销售额**：`$1,791`
  *   **平均重量**：`0.60 pounds (274 g)`
  *   **平均体积**：`166.17 in³ (2,723 cm³)`
  *   **平均毛利率**：`59.24%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`12.3‰`

---

#### 🏆 🟢-71. Trash Can Lids (垃圾桶盖)

- **完整市场路径**：`Home & Kitchen › Storage & Organization › Trash, Recycling & Compost › Trash Can Lids  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.55`
  *   **平均 Reviews (Avg Reviews)**：`148 个`
  *   **物理重量 (Weight)**：`1.37 lbs`
  *   **平均退货率 (Return Rate)**：`5.21%`
  *   **平均毛利率 (Profit Margin)**：`57.33%`
  *   **品牌集中度 (Brand Concentration)**：`54.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Storage & Organization › Trash, Recycling & Compost › Trash Can Lids  市场分析`
  *   **市场路径(中文)**：`家居用品 › 储存 › 垃圾，回收 › 垃圾桶盖`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`17`
  *   **新品平均价格**：`$ 23.61`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`117`
  *   **新品月均销售额**：`$2,987`
  *   **平均重量**：`1.37 pounds (622 g)`
  *   **平均体积**：`375.02 in³ (6,145 cm³)`
  *   **平均毛利率**：`57.33%`
  *   **卖家所属地**：`中国|55.0%`
  *   **搜索购买比**：`10.7‰`

---

#### 🏆 🟢-72. Pool Heater & Heat Pump Parts (气筒气泵)

- **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Heaters & Accessories › Pool Heater Parts & Accessories › Pool Heater & Heat Pump Parts  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$84.07`
  *   **平均 Reviews (Avg Reviews)**：`96 个`
  *   **物理重量 (Weight)**：`1.99 lbs`
  *   **平均退货率 (Return Rate)**：`6.71%`
  *   **平均毛利率 (Profit Margin)**：`69.79%`
  *   **品牌集中度 (Brand Concentration)**：`46.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Pools, Hot Tubs & Supplies › Heaters & Accessories › Pool Heater Parts & Accessories › Pool Heater & Heat Pump Parts  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 泳池及配件 › 加热器及配件 › 泳池加热器零配件 › 气筒气泵`
  *   **A+数量占比**：`65%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 36.06`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`103`
  *   **新品月均销售额**：`$3,714`
  *   **平均重量**：`1.99 pounds (905 g)`
  *   **平均体积**：`219.06 in³ (3,590 cm³)`
  *   **平均毛利率**：`69.79%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`19.2‰`

---

#### 🏆 🟢-73. Cables & Adapters (电缆和适配器)

- **完整市场路径**：`Video Games › Nintendo Switch › Accessories › Cables & Adapters  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.17`
  *   **平均 Reviews (Avg Reviews)**：`591 个`
  *   **物理重量 (Weight)**：`0.35 lbs`
  *   **平均退货率 (Return Rate)**：`6.58%`
  *   **平均毛利率 (Profit Margin)**：`67.98%`
  *   **品牌集中度 (Brand Concentration)**：`53.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Video Games › Nintendo Switch › Accessories › Cables & Adapters  市场分析`
  *   **市场路径(中文)**：`视频游戏 › 任天堂开关 › 配件 › 电缆和适配器`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`68`
  *   **新品平均价格**：`$ 32.27`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`232`
  *   **新品月均销售额**：`$8,278`
  *   **平均重量**：`0.35 pounds (158 g)`
  *   **平均体积**：`46.23 in³ (758 cm³)`
  *   **平均毛利率**：`67.98%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-74. Collectible Vehicles (交通工具摆件)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Collectible Vehicles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.27`
  *   **平均 Reviews (Avg Reviews)**：`226 个`
  *   **物理重量 (Weight)**：`0.96 lbs`
  *   **平均退货率 (Return Rate)**：`5.81%`
  *   **平均毛利率 (Profit Margin)**：`57.82%`
  *   **品牌集中度 (Brand Concentration)**：`63.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`87.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Collectible Vehicles  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 交通工具摆件`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 20.16`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`148`
  *   **新品月均销售额**：`$2,590`
  *   **平均重量**：`0.96 pounds (434 g)`
  *   **平均体积**：`169.56 in³ (2,779 cm³)`
  *   **平均毛利率**：`57.82%`
  *   **卖家所属地**：`中国|87.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟢-75. Automatic Feeders (自动食盆)

- **完整市场路径**：`Pet Supplies › Small Animals › Feeding & Watering Supplies › Automatic Feeders  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.93`
  *   **平均 Reviews (Avg Reviews)**：`224 个`
  *   **物理重量 (Weight)**：`1.33 lbs`
  *   **平均退货率 (Return Rate)**：`7.46%`
  *   **平均毛利率 (Profit Margin)**：`52.49%`
  *   **品牌集中度 (Brand Concentration)**：`43.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`90.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Small Animals › Feeding & Watering Supplies › Automatic Feeders  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 小宠用品 › 喂食、喂水器 › 自动食盆`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`12`
  *   **新品平均价格**：`$ 20.59`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`92`
  *   **新品月均销售额**：`$1,902`
  *   **平均重量**：`1.33 pounds (605 g)`
  *   **平均体积**：`319.32 in³ (5,233 cm³)`
  *   **平均毛利率**：`52.49%`
  *   **卖家所属地**：`中国|90.0%`
  *   **搜索购买比**：`7.0‰`

---

#### 🏆 🟢-76. Car Rack Parts & Accessories (汽车货架零件和配件)

- **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Accessories › Car Racks & Carriers › Car Rack Parts & Accessories  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$42.76`
  *   **平均 Reviews (Avg Reviews)**：`219 个`
  *   **物理重量 (Weight)**：`1.33 lbs`
  *   **平均退货率 (Return Rate)**：`6.72%`
  *   **平均毛利率 (Profit Margin)**：`63.74%`
  *   **品牌集中度 (Brand Concentration)**：`44.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`57.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Accessories › Car Racks & Carriers › Car Rack Parts & Accessories  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 外出休闲 › 配件 › 汽车货架和运输工具 › 汽车货架零件和配件`
  *   **A+数量占比**：`63%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 32.98`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`127`
  *   **新品月均销售额**：`$3,607`
  *   **平均重量**：`1.33 pounds (604 g)`
  *   **平均体积**：`477.71 in³ (7,828 cm³)`
  *   **平均毛利率**：`63.74%`
  *   **卖家所属地**：`中国|57.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟢-77. 3D Printer Extruders (3D打印机挤出机)

- **完整市场路径**：`Industrial & Scientific › Additive Manufacturing Products › 3D Printer Parts & Accessories › 3D Printer Extruders  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.04`
  *   **平均 Reviews (Avg Reviews)**：`158 个`
  *   **物理重量 (Weight)**：`0.18 lbs`
  *   **平均退货率 (Return Rate)**：`4.99%`
  *   **平均毛利率 (Profit Margin)**：`68.13%`
  *   **品牌集中度 (Brand Concentration)**：`61.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Additive Manufacturing Products › 3D Printer Parts & Accessories › 3D Printer Extruders  市场分析`
  *   **市场路径(中文)**：`工业类 › 增材制造产品 › 3D打印机零件 › 3D打印机挤出机`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 35.63`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`159`
  *   **新品月均销售额**：`$5,773`
  *   **平均重量**：`0.18 pounds (80 g)`
  *   **平均体积**：`17.54 in³ (287 cm³)`
  *   **平均毛利率**：`68.13%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`8.8‰`

---

#### 🏆 🟢-78. Guitar & Bass Accessories (吉他)

- **完整市场路径**：`Musical Instruments › Instrument Accessories › Guitar & Bass Accessories  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$39.96`
  *   **平均 Reviews (Avg Reviews)**：`447 个`
  *   **物理重量 (Weight)**：`0.70 lbs`
  *   **平均退货率 (Return Rate)**：`3.89%`
  *   **平均毛利率 (Profit Margin)**：`58.26%`
  *   **品牌集中度 (Brand Concentration)**：`60.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.2%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Musical Instruments › Instrument Accessories › Guitar & Bass Accessories  市场分析`
  *   **市场路径(中文)**：`乐器 › 仪器配件 › 吉他`
  *   **A+数量占比**：`35.42%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 43.65`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`31`
  *   **新品月均销售额**：`$535`
  *   **平均重量**：`0.70 pounds (318 g)`
  *   **平均体积**：`132.18 in³ (2,166 cm³)`
  *   **平均毛利率**：`58.26%`
  *   **卖家所属地**：`中国|54.2%`
  *   **搜索购买比**：`10.6‰`

---

#### 🏆 🟢-79. Wine Decanters (醒酒器)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Beverage Serveware › Wine Decanters  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$45.82`
  *   **平均 Reviews (Avg Reviews)**：`398 个`
  *   **物理重量 (Weight)**：`1.82 lbs`
  *   **平均退货率 (Return Rate)**：`5.52%`
  *   **平均毛利率 (Profit Margin)**：`61.86%`
  *   **品牌集中度 (Brand Concentration)**：`58.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`45.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Serveware › Beverage Serveware › Wine Decanters  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房和餐厅 › 餐饮与娱乐 › 餐具 › 餐具 › 饮料餐具 › 醒酒器`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 65.65`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`59`
  *   **新品月均销售额**：`$3,774`
  *   **平均重量**：`1.82 pounds (824 g)`
  *   **平均体积**：`403.92 in³ (6,619 cm³)`
  *   **平均毛利率**：`61.86%`
  *   **卖家所属地**：`中国|45.0%`
  *   **搜索购买比**：`5.3‰`

---

#### 🏆 🟢-80. Deviled Egg Plates (咸蛋盘)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Dinnerware › Plates › Specialty Plates › Deviled Egg Plates  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.22`
  *   **平均 Reviews (Avg Reviews)**：`338 个`
  *   **物理重量 (Weight)**：`1.92 lbs`
  *   **平均退货率 (Return Rate)**：`5.01%`
  *   **平均毛利率 (Profit Margin)**：`51.72%`
  *   **品牌集中度 (Brand Concentration)**：`58.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Dinnerware & Serveware › Dinnerware › Plates › Specialty Plates › Deviled Egg Plates  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房和餐厅 › 餐饮与娱乐 › 餐具 › 餐具 › 板材 › 特色餐盘 › 咸蛋盘`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`36`
  *   **新品平均价格**：`$ 23.08`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`134`
  *   **新品月均销售额**：`$3,190`
  *   **平均重量**：`1.92 pounds (872 g)`
  *   **平均体积**：`375.23 in³ (6,149 cm³)`
  *   **平均毛利率**：`51.72%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`7.7‰`

---

#### 🏆 🟢-81. Grill Lighting (点火器)

- **完整市场路径**：`Patio, Lawn & Garden › Grills & Outdoor Cooking › Outdoor Cooking Tools & Accessories › Grill Lighting  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.71`
  *   **平均 Reviews (Avg Reviews)**：`593 个`
  *   **物理重量 (Weight)**：`1.27 lbs`
  *   **平均退货率 (Return Rate)**：`5.43%`
  *   **平均毛利率 (Profit Margin)**：`63.75%`
  *   **品牌集中度 (Brand Concentration)**：`53.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Grills & Outdoor Cooking › Outdoor Cooking Tools & Accessories › Grill Lighting  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 烧烤用具 › 烤炉配件 › 点火器`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`244`
  *   **新品平均价格**：`$ 39.19`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`76`
  *   **新品月均销售额**：`$2,283`
  *   **平均重量**：`1.27 pounds (578 g)`
  *   **平均体积**：`233.98 in³ (3,834 cm³)`
  *   **平均毛利率**：`63.75%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`6.3‰`

---

#### 🏆 🟢-82. Cheese Knives (奶酪刀)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Specialty Knives › Cheese Knives  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.74`
  *   **平均 Reviews (Avg Reviews)**：`525 个`
  *   **物理重量 (Weight)**：`0.57 lbs`
  *   **平均退货率 (Return Rate)**：`4.02%`
  *   **平均毛利率 (Profit Margin)**：`56.69%`
  *   **品牌集中度 (Brand Concentration)**：`45.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`53.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Kitchen Knives & Accessories › Specialty Knives › Cheese Knives  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 刀具厨房及配件 › 特种刀 › 奶酪刀`
  *   **A+数量占比**：`71%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 15.05`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`87`
  *   **新品月均销售额**：`$1,280`
  *   **平均重量**：`0.57 pounds (260 g)`
  *   **平均体积**：`55.36 in³ (907 cm³)`
  *   **平均毛利率**：`56.69%`
  *   **卖家所属地**：`中国|53.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟢-83. Brazing Rods (钎杆)

- **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Soldering & Brazing Equipment › Solder & Flux › Brazing Rods  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.39`
  *   **平均 Reviews (Avg Reviews)**：`178 个`
  *   **物理重量 (Weight)**：`0.65 lbs`
  *   **平均退货率 (Return Rate)**：`2.03%`
  *   **平均毛利率 (Profit Margin)**：`62.49%`
  *   **品牌集中度 (Brand Concentration)**：`61.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Soldering & Brazing Equipment › Solder & Flux › Brazing Rods  市场分析`
  *   **市场路径(中文)**：`工具 › 焊接 › 焊接 › 焊接 › 钎杆`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 29.06`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`137`
  *   **新品月均销售额**：`$4,654`
  *   **平均重量**：`0.65 pounds (294 g)`
  *   **平均体积**：`24.29 in³ (398 cm³)`
  *   **平均毛利率**：`62.49%`
  *   **卖家所属地**：`中国|55.0%`
  *   **搜索购买比**：`10.0‰`

---

#### 🏆 🟢-84. Fuel (燃油表)

- **完整市场路径**：`Automotive › Replacement Parts › Lighting & Electrical › Electrical › Gauges › Fuel  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.90`
  *   **平均 Reviews (Avg Reviews)**：`113 个`
  *   **物理重量 (Weight)**：`0.42 lbs`
  *   **平均退货率 (Return Rate)**：`4.87%`
  *   **平均毛利率 (Profit Margin)**：`65.58%`
  *   **品牌集中度 (Brand Concentration)**：`52.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Lighting & Electrical › Electrical › Gauges › Fuel  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 照明及电气 › 电气 › 计量器 › 燃油表`
  *   **A+数量占比**：`65%`
  *   **新品平均评分数**：`4`
  *   **新品平均价格**：`$ 22.67`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`128`
  *   **新品月均销售额**：`$2,529`
  *   **平均重量**：`0.42 pounds (191 g)`
  *   **平均体积**：`69.87 in³ (1,145 cm³)`
  *   **平均毛利率**：`65.58%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`8.2‰`

---

#### 🏆 🟢-85. Angle (角规)

- **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Dimensional Measurement › Gauges › Angle  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.40`
  *   **平均 Reviews (Avg Reviews)**：`404 个`
  *   **物理重量 (Weight)**：`0.54 lbs`
  *   **平均退货率 (Return Rate)**：`2.9%`
  *   **平均毛利率 (Profit Margin)**：`66.51%`
  *   **品牌集中度 (Brand Concentration)**：`60.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Test, Measure & Inspect › Dimensional Measurement › Gauges › Angle  市场分析`
  *   **市场路径(中文)**：`工业类 › 测试，测量 › 尺寸测量 › 计量器 › 角规`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`76`
  *   **新品平均价格**：`$ 22.6`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`66`
  *   **新品月均销售额**：`$1,361`
  *   **平均重量**：`0.54 pounds (244 g)`
  *   **平均体积**：`32.21 in³ (528 cm³)`
  *   **平均毛利率**：`66.51%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`11.4‰`

---

#### 🏆 🟢-86. Nail Pullers (羊角起钉钳)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Nail Pullers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.71`
  *   **平均 Reviews (Avg Reviews)**：`366 个`
  *   **物理重量 (Weight)**：`1.29 lbs`
  *   **平均退货率 (Return Rate)**：`2.27%`
  *   **平均毛利率 (Profit Margin)**：`54.73%`
  *   **品牌集中度 (Brand Concentration)**：`61.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`60.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools › Nail Pullers  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具 › 羊角起钉钳`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 12.7`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`102`
  *   **新品月均销售额**：`$1,054`
  *   **平均重量**：`1.29 pounds (585 g)`
  *   **平均体积**：`86.17 in³ (1,412 cm³)`
  *   **平均毛利率**：`54.73%`
  *   **卖家所属地**：`中国|60.0%`
  *   **搜索购买比**：`9.6‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Liver Extracts (肝脏提取物)

- **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Glandular Extracts › Liver Extracts  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.11`
  *   **平均 Reviews (Avg Reviews)**：`838 个`
  *   **物理重量 (Weight)**：`0.30 lbs`
  *   **平均退货率 (Return Rate)**：`0.31%`
  *   **平均毛利率 (Profit Margin)**：`68.88%`
  *   **品牌集中度 (Brand Concentration)**：`62.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`16.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Vitamins, Minerals & Supplements › Glandular Extracts › Liver Extracts  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 身、泳和附剂 › 圣诞体提取物 › 肝脏提取物`
  *   **A+数量占比**：`92%`
  *   **新品平均评分数**：`63`
  *   **新品平均价格**：`$ 31.6`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`1,020`
  *   **新品月均销售额**：`$34,670`
  *   **平均重量**：`0.30 pounds (136 g)`
  *   **平均体积**：`45.60 in³ (747 cm³)`
  *   **平均毛利率**：`68.88%`
  *   **卖家所属地**：`美国|84.0%`
  *   **搜索购买比**：`22.9‰`

---

#### 🏆 🟡-2. Figurine Lights (雕像灯)

- **完整市场路径**：`Tools & Home Improvement › Lighting & Ceiling Fans › Outdoor Lighting › Landscape Lighting › Figurine Lights  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.37`
  *   **平均 Reviews (Avg Reviews)**：`839 个`
  *   **物理重量 (Weight)**：`1.34 lbs`
  *   **平均退货率 (Return Rate)**：`2.34%`
  *   **平均毛利率 (Profit Margin)**：`56.89%`
  *   **品牌集中度 (Brand Concentration)**：`52.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`85.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Lighting & Ceiling Fans › Outdoor Lighting › Landscape Lighting › Figurine Lights  市场分析`
  *   **市场路径(中文)**：`工具 › 照明 › 户外照明 › 景观照明 › 雕像灯`
  *   **A+数量占比**：`99%`
  *   **新品平均评分数**：`82`
  *   **新品平均价格**：`$ 24.82`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`1,237`
  *   **新品月均销售额**：`$31,216`
  *   **平均重量**：`1.34 pounds (608 g)`
  *   **平均体积**：`273.54 in³ (4,483 cm³)`
  *   **平均毛利率**：`56.89%`
  *   **卖家所属地**：`中国|85.0%`
  *   **搜索购买比**：`4.9‰`

---

#### 🏆 🟡-3. Squirt Guns (水枪)

- **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.72`
  *   **平均 Reviews (Avg Reviews)**：`564 个`
  *   **物理重量 (Weight)**：`1.57 lbs`
  *   **平均退货率 (Return Rate)**：`3.93%`
  *   **平均毛利率 (Profit Margin)**：`53.58%`
  *   **品牌集中度 (Brand Concentration)**：`47.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Sports & Outdoor Play › Pools & Water Toys › Squirt Guns  市场分析`
  *   **市场路径(中文)**：`玩具 › 体育 › 游泳池 › 水枪`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`138`
  *   **新品平均价格**：`$ 30.88`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`1,357`
  *   **新品月均销售额**：`$39,613`
  *   **平均重量**：`1.57 pounds (713 g)`
  *   **平均体积**：`325.38 in³ (5,332 cm³)`
  *   **平均毛利率**：`53.58%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`5.7‰`

---

#### 🏆 🟡-4. Self-Watering Stakes (自浇水桩)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Pots, Planters & Container Accessories › Plant Container Accessories › Self-Watering Stakes  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.75`
  *   **平均 Reviews (Avg Reviews)**：`801 个`
  *   **物理重量 (Weight)**：`1.49 lbs`
  *   **平均退货率 (Return Rate)**：`2.8%`
  *   **平均毛利率 (Profit Margin)**：`53.33%`
  *   **品牌集中度 (Brand Concentration)**：`53.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Pots, Planters & Container Accessories › Plant Container Accessories › Self-Watering Stakes  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 花盆、花架、育苗盘 › 花盆配件 › 自浇水桩`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`459`
  *   **新品平均价格**：`$ 24.19`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`600`
  *   **新品月均销售额**：`$14,031`
  *   **平均重量**：`1.49 pounds (676 g)`
  *   **平均体积**：`153.43 in³ (2,514 cm³)`
  *   **平均毛利率**：`53.33%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`12.2‰`

---

#### 🏆 🟡-5. Fountains (喷泉)

- **完整市场路径**：`Pet Supplies › Dogs › Feeding & Watering Supplies › Fountains  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$40.94`
  *   **平均 Reviews (Avg Reviews)**：`590 个`
  *   **物理重量 (Weight)**：`2.30 lbs`
  *   **平均退货率 (Return Rate)**：`4.78%`
  *   **平均毛利率 (Profit Margin)**：`63.27%`
  *   **品牌集中度 (Brand Concentration)**：`55.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Dogs › Feeding & Watering Supplies › Fountains  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 犬类 › 喂食 › 喷泉`
  *   **A+数量占比**：`94%`
  *   **新品平均评分数**：`74`
  *   **新品平均价格**：`$ 49.58`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`583`
  *   **新品月均销售额**：`$29,594`
  *   **平均重量**：`2.30 pounds (1,041 g)`
  *   **平均体积**：`608.30 in³ (9,968 cm³)`
  *   **平均毛利率**：`63.27%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`10.2‰`

---

#### 🏆 🟡-6. Compressed Air Dusters (压缩除尘罐)

- **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.30`
  *   **平均 Reviews (Avg Reviews)**：`379 个`
  *   **物理重量 (Weight)**：`0.88 lbs`
  *   **平均退货率 (Return Rate)**：`3.16%`
  *   **平均毛利率 (Profit Margin)**：`73.38%`
  *   **品牌集中度 (Brand Concentration)**：`61.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Computers & Accessories › Computer Accessories & Peripherals › Cleaning & Repair › Compressed Air Dusters  市场分析`
  *   **市场路径(中文)**：`电子产品 › 计算机 › 电脑配件 › 清洁 › 压缩除尘罐`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`207`
  *   **新品平均价格**：`$ 31.58`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`573`
  *   **新品月均销售额**：`$18,580`
  *   **平均重量**：`0.88 pounds (397 g)`
  *   **平均体积**：`92.17 in³ (1,510 cm³)`
  *   **平均毛利率**：`73.38%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`13.0‰`

---

#### 🏆 🟡-7. Trays & Bags (托盘、口袋)

- **完整市场路径**：`Automotive › Interior Accessories › Consoles & Organizers › Trays & Bags  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.54`
  *   **平均 Reviews (Avg Reviews)**：`916 个`
  *   **物理重量 (Weight)**：`1.21 lbs`
  *   **平均退货率 (Return Rate)**：`9.42%`
  *   **平均毛利率 (Profit Margin)**：`55.86%`
  *   **品牌集中度 (Brand Concentration)**：`38.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`86.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Interior Accessories › Consoles & Organizers › Trays & Bags  市场分析`
  *   **市场路径(中文)**：`汽车 › 内部配件 › 控制台 › 托盘、口袋`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`143`
  *   **新品平均价格**：`$ 16.21`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`681`
  *   **新品月均销售额**：`$9,699`
  *   **平均重量**：`1.21 pounds (551 g)`
  *   **平均体积**：`334.05 in³ (5,474 cm³)`
  *   **平均毛利率**：`55.86%`
  *   **卖家所属地**：`中国|86.0%`
  *   **搜索购买比**：`5.9‰`

---

#### 🏆 🟡-8. Glasses & Goggles (眼镜和护目镜)

- **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Glasses & Goggles  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.98`
  *   **平均 Reviews (Avg Reviews)**：`850 个`
  *   **物理重量 (Weight)**：`0.22 lbs`
  *   **平均退货率 (Return Rate)**：`6.05%`
  *   **平均毛利率 (Profit Margin)**：`63.06%`
  *   **品牌集中度 (Brand Concentration)**：`55.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`88.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Glasses & Goggles  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 骑自行车 › 眼镜和护目镜`
  *   **A+数量占比**：`95%`
  *   **新品平均评分数**：`70`
  *   **新品平均价格**：`$ 17.99`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`792`
  *   **新品月均销售额**：`$11,858`
  *   **平均重量**：`0.22 pounds (99 g)`
  *   **平均体积**：`61.93 in³ (1,015 cm³)`
  *   **平均毛利率**：`63.06%`
  *   **卖家所属地**：`中国|88.0%`
  *   **搜索购买比**：`6.3‰`

---

#### 🏆 🟡-9. Birdhouses (鸟屋)

- **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Birds › Birdhouses  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.19`
  *   **平均 Reviews (Avg Reviews)**：`663 个`
  *   **物理重量 (Weight)**：`2.12 lbs`
  *   **平均退货率 (Return Rate)**：`2.92%`
  *   **平均毛利率 (Profit Margin)**：`56.67%`
  *   **品牌集中度 (Brand Concentration)**：`52.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Birds › Birdhouses  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Birds › 鸟屋`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`83`
  *   **新品平均价格**：`$ 24.44`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`613`
  *   **新品月均销售额**：`$15,238`
  *   **平均重量**：`2.12 pounds (964 g)`
  *   **平均体积**：`565.79 in³ (9,272 cm³)`
  *   **平均毛利率**：`56.67%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`7.2‰`

---

#### 🏆 🟡-10. Hand Tools (手动工具)

- **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.62`
  *   **平均 Reviews (Avg Reviews)**：`969 个`
  *   **物理重量 (Weight)**：`1.50 lbs`
  *   **平均退货率 (Return Rate)**：`3.71%`
  *   **平均毛利率 (Profit Margin)**：`56.9%`
  *   **品牌集中度 (Brand Concentration)**：`49.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`49.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Power & Hand Tools › Hand Tools  市场分析`
  *   **市场路径(中文)**：`工具 › 权力 › 手动工具`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`65`
  *   **新品平均价格**：`$ 25.16`
  *   **新品平均星级**：`3.9`
  *   **新品月均销量**：`467`
  *   **新品月均销售额**：`$10,456`
  *   **平均重量**：`1.50 pounds (683 g)`
  *   **平均体积**：`179.55 in³ (2,942 cm³)`
  *   **平均毛利率**：`56.9%`
  *   **卖家所属地**：`中国|49.0%`
  *   **搜索购买比**：`14.6‰`

---

#### 🏆 🟡-11. Battery Switches (接线柱)

- **完整市场路径**：`Automotive › Replacement Parts › Batteries & Accessories › Battery Accessories › Battery Switches  市场分析`
- **触发警示项**：`带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.40`
  *   **平均 Reviews (Avg Reviews)**：`610 个`
  *   **物理重量 (Weight)**：`0.61 lbs`
  *   **平均退货率 (Return Rate)**：`5.58%`
  *   **平均毛利率 (Profit Margin)**：`57.71%`
  *   **品牌集中度 (Brand Concentration)**：`55.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Batteries & Accessories › Battery Accessories › Battery Switches  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 电池 › 电池配件 › 接线柱`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`56`
  *   **新品平均价格**：`$ 16.07`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`700`
  *   **新品月均销售额**：`$10,068`
  *   **平均重量**：`0.61 pounds (275 g)`
  *   **平均体积**：`31.55 in³ (517 cm³)`
  *   **平均毛利率**：`57.71%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`12.7‰`

---

#### 🏆 🟡-12. Batteries & Battery Chargers (电池和电池)

- **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.68`
  *   **平均 Reviews (Avg Reviews)**：`483 个`
  *   **物理重量 (Weight)**：`0.94 lbs`
  *   **平均退货率 (Return Rate)**：`9.83%`
  *   **平均毛利率 (Profit Margin)**：`62.09%`
  *   **品牌集中度 (Brand Concentration)**：`59.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Skates, Skateboards & Scooters › Scooters & Equipment › Components & Parts › Batteries & Battery Chargers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 溜冰鞋、滑板和滑板车 › 自行车车 › 自行车车配件 › 电池和电池`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`72`
  *   **新品平均价格**：`$ 23.23`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`593`
  *   **新品月均销售额**：`$13,888`
  *   **平均重量**：`0.94 pounds (426 g)`
  *   **平均体积**：`72.07 in³ (1,181 cm³)`
  *   **平均毛利率**：`62.09%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`9.9‰`

---

#### 🏆 🟡-13. Air Ionizers (负离子空气净化器)

- **完整市场路径**：`Home & Kitchen › Heating, Cooling & Air Quality › Air Purifiers › Air Ionizers  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$57.13`
  *   **平均 Reviews (Avg Reviews)**：`993 个`
  *   **物理重量 (Weight)**：`2.20 lbs`
  *   **平均退货率 (Return Rate)**：`6.98%`
  *   **平均毛利率 (Profit Margin)**：`70.63%`
  *   **品牌集中度 (Brand Concentration)**：`58.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Heating, Cooling & Air Quality › Air Purifiers › Air Ionizers  市场分析`
  *   **市场路径(中文)**：`家居用品 › 供暖、制冷 › 空气净化器 › 负离子空气净化器`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`109`
  *   **新品平均价格**：`$ 41.34`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`639`
  *   **新品月均销售额**：`$31,281`
  *   **平均重量**：`2.20 pounds (998 g)`
  *   **平均体积**：`200.72 in³ (3,289 cm³)`
  *   **平均毛利率**：`70.63%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟡-14. Replacement Sensors (更换传感器)

- **完整市场路径**：`Automotive › Tires & Wheels › Accessories & Parts › Tire Pressure Monitoring Systems (TPMS) › Replacement Sensors  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$46.06`
  *   **平均 Reviews (Avg Reviews)**：`984 个`
  *   **物理重量 (Weight)**：`0.47 lbs`
  *   **平均退货率 (Return Rate)**：`9.2%`
  *   **平均毛利率 (Profit Margin)**：`67.88%`
  *   **品牌集中度 (Brand Concentration)**：`60.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tires & Wheels › Accessories & Parts › Tire Pressure Monitoring Systems (TPMS) › Replacement Sensors  市场分析`
  *   **市场路径(中文)**：`汽车 › 轮胎轮胎 › 辅料 › 轮胎压力监测系统 (TPMS) › 更换传感器`
  *   **A+数量占比**：`93%`
  *   **新品平均评分数**：`61`
  *   **新品平均价格**：`$ 16.52`
  *   **新品平均星级**：`3.8`
  *   **新品月均销量**：`429`
  *   **新品月均销售额**：`$7,538`
  *   **平均重量**：`0.47 pounds (212 g)`
  *   **平均体积**：`41.61 in³ (682 cm³)`
  *   **平均毛利率**：`67.88%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`10.2‰`

---

#### 🏆 🟡-15. Neon Accent Lights (霓虹灯)

- **完整市场路径**：`Automotive › Lights, Bulbs & Indicators › Accent & Off Road Lighting › LED & Neon Lights › Neon Accent Lights  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.02`
  *   **平均 Reviews (Avg Reviews)**：`958 个`
  *   **物理重量 (Weight)**：`0.79 lbs`
  *   **平均退货率 (Return Rate)**：`6.23%`
  *   **平均毛利率 (Profit Margin)**：`61.52%`
  *   **品牌集中度 (Brand Concentration)**：`53.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Lights, Bulbs & Indicators › Accent & Off Road Lighting › LED & Neon Lights › Neon Accent Lights  市场分析`
  *   **市场路径(中文)**：`汽车 › 灯光 › 重音 › LED › 霓虹灯`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`345`
  *   **新品平均价格**：`$ 22.91`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`601`
  *   **新品月均销售额**：`$14,665`
  *   **平均重量**：`0.79 pounds (359 g)`
  *   **平均体积**：`131.21 in³ (2,150 cm³)`
  *   **平均毛利率**：`61.52%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟡-16. Champagne Glasses (香槟酒杯)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Glassware & Drinkware › Wine & Champagne Glasses › Champagne Glasses  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.05`
  *   **平均 Reviews (Avg Reviews)**：`871 个`
  *   **物理重量 (Weight)**：`1.80 lbs`
  *   **平均退货率 (Return Rate)**：`7.64%`
  *   **平均毛利率 (Profit Margin)**：`56.65%`
  *   **品牌集中度 (Brand Concentration)**：`48.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`59.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Dining & Entertaining › Glassware & Drinkware › Wine & Champagne Glasses › Champagne Glasses  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 美食购物 › 玻璃器皿 › 葡萄酒 › 香槟酒杯`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`28`
  *   **新品平均价格**：`$ 32.54`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`369`
  *   **新品月均销售额**：`$11,458`
  *   **平均重量**：`1.80 pounds (816 g)`
  *   **平均体积**：`163.83 in³ (2,685 cm³)`
  *   **平均毛利率**：`56.65%`
  *   **卖家所属地**：`中国|59.0%`
  *   **搜索购买比**：`6.8‰`

---

#### 🏆 🟡-17. Door Entry Guard (门禁)

- **完整市场路径**：`Automotive › Interior Accessories › Door Entry Guard  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.99`
  *   **平均 Reviews (Avg Reviews)**：`923 个`
  *   **物理重量 (Weight)**：`1.03 lbs`
  *   **平均退货率 (Return Rate)**：`6.12%`
  *   **平均毛利率 (Profit Margin)**：`54.47%`
  *   **品牌集中度 (Brand Concentration)**：`34.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Interior Accessories › Door Entry Guard  市场分析`
  *   **市场路径(中文)**：`汽车 › 内部配件 › 门禁`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`56`
  *   **新品平均价格**：`$ 40.9`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`365`
  *   **新品月均销售额**：`$15,346`
  *   **平均重量**：`1.03 pounds (468 g)`
  *   **平均体积**：`369.51 in³ (6,055 cm³)`
  *   **平均毛利率**：`54.47%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`6.4‰`

---

#### 🏆 🟡-18. Deck Lights (甲板灯)

- **完整市场路径**：`Tools & Home Improvement › Lighting & Ceiling Fans › Outdoor Lighting › Landscape Lighting › Deck Lights  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$46.86`
  *   **平均 Reviews (Avg Reviews)**：`907 个`
  *   **物理重量 (Weight)**：`2.24 lbs`
  *   **平均退货率 (Return Rate)**：`4.76%`
  *   **平均毛利率 (Profit Margin)**：`67.02%`
  *   **品牌集中度 (Brand Concentration)**：`59.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`72.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Lighting & Ceiling Fans › Outdoor Lighting › Landscape Lighting › Deck Lights  市场分析`
  *   **市场路径(中文)**：`工具 › 照明 › 户外照明 › 景观照明 › 甲板灯`
  *   **A+数量占比**：`96%`
  *   **新品平均评分数**：`38`
  *   **新品平均价格**：`$ 37.12`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`348`
  *   **新品月均销售额**：`$12,396`
  *   **平均重量**：`2.24 pounds (1,016 g)`
  *   **平均体积**：`90.91 in³ (1,490 cm³)`
  *   **平均毛利率**：`67.02%`
  *   **卖家所属地**：`中国|72.0%`
  *   **搜索购买比**：`5.4‰`

---

#### 🏆 🟡-19. Decorative Trays (装饰性托盘)

- **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.97`
  *   **平均 Reviews (Avg Reviews)**：`477 个`
  *   **物理重量 (Weight)**：`1.60 lbs`
  *   **平均退货率 (Return Rate)**：`9.52%`
  *   **平均毛利率 (Profit Margin)**：`56.96%`
  *   **品牌集中度 (Brand Concentration)**：`44.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Home Décor Products › Home Décor Accents › Decorative Accessories › Decorative Trays  市场分析`
  *   **市场路径(中文)**：`家居用品 › 家居装饰 › 家居装饰品 › 装饰配件 › 装饰性托盘`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`116`
  *   **新品平均价格**：`$ 21.83`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`688`
  *   **新品月均销售额**：`$14,790`
  *   **平均重量**：`1.60 pounds (727 g)`
  *   **平均体积**：`290.13 in³ (4,754 cm³)`
  *   **平均毛利率**：`56.96%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`4.2‰`

---

#### 🏆 🟡-20. Money & Banking (奖金)

- **完整市场路径**：`Toys & Games › Dress Up & Pretend Play › Money & Banking  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$21.17`
  *   **平均 Reviews (Avg Reviews)**：`757 个`
  *   **物理重量 (Weight)**：`1.02 lbs`
  *   **平均退货率 (Return Rate)**：`4.08%`
  *   **平均毛利率 (Profit Margin)**：`56.72%`
  *   **品牌集中度 (Brand Concentration)**：`48.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Dress Up & Pretend Play › Money & Banking  市场分析`
  *   **市场路径(中文)**：`玩具 › 扮靓 › 奖金`
  *   **A+数量占比**：`73%`
  *   **新品平均评分数**：`166`
  *   **新品平均价格**：`$ 20.27`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`479`
  *   **新品月均销售额**：`$8,826`
  *   **平均重量**：`1.02 pounds (461 g)`
  *   **平均体积**：`207.23 in³ (3,396 cm³)`
  *   **平均毛利率**：`56.72%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`7.7‰`

---

#### 🏆 🟡-21. Poultry Fountains & Waterers (家禽自动喂水器和饮水器)

- **完整市场路径**：`Patio, Lawn & Garden › Farm & Ranch › Poultry Care › Poultry Feeding & Watering Supplies › Poultry Fountains & Waterers  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.36`
  *   **平均 Reviews (Avg Reviews)**：`533 个`
  *   **物理重量 (Weight)**：`2.30 lbs`
  *   **平均退货率 (Return Rate)**：`2.74%`
  *   **平均毛利率 (Profit Margin)**：`52.0%`
  *   **品牌集中度 (Brand Concentration)**：`48.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Farm & Ranch › Poultry Care › Poultry Feeding & Watering Supplies › Poultry Fountains & Waterers  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 农场和牧场 › 家禽养护 › 家禽喂食喂水用具 › 家禽自动喂水器和饮水器`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`32`
  *   **新品平均价格**：`$ 45.72`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`361`
  *   **新品月均销售额**：`$15,572`
  *   **平均重量**：`2.30 pounds (1,042 g)`
  *   **平均体积**：`745.68 in³ (12,220 cm³)`
  *   **平均毛利率**：`52%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`9.7‰`

---

#### 🏆 🟡-22. Cup Carriers (外卖杯托盘)

- **完整市场路径**：`Industrial & Scientific › Food Service Equipment & Supplies › Disposables › Take Out Containers › Cup Carriers  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.00`
  *   **平均 Reviews (Avg Reviews)**：`447 个`
  *   **物理重量 (Weight)**：`2.43 lbs`
  *   **平均退货率 (Return Rate)**：`4.6%`
  *   **平均毛利率 (Profit Margin)**：`53.59%`
  *   **品牌集中度 (Brand Concentration)**：`47.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Food Service Equipment & Supplies › Disposables › Take Out Containers › Cup Carriers  市场分析`
  *   **市场路径(中文)**：`工业类 › 食品服务设备 › 一次性用品 › 外卖容器 › 外卖杯托盘`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`29`
  *   **新品平均价格**：`$ 15.52`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`301`
  *   **新品月均销售额**：`$4,502`
  *   **平均重量**：`2.43 pounds (1,100 g)`
  *   **平均体积**：`499.35 in³ (8,183 cm³)`
  *   **平均毛利率**：`53.59%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`8.4‰`

---

#### 🏆 🟡-23. Tool Sets (汽车维修工具套装)

- **完整市场路径**：`Automotive › Tools & Equipment › Tool Sets  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.24`
  *   **平均 Reviews (Avg Reviews)**：`654 个`
  *   **物理重量 (Weight)**：`2.23 lbs`
  *   **平均退货率 (Return Rate)**：`3.65%`
  *   **平均毛利率 (Profit Margin)**：`55.1%`
  *   **品牌集中度 (Brand Concentration)**：`40.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`80.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Tool Sets  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 汽车维修工具套装`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`92`
  *   **新品平均价格**：`$ 20.88`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`492`
  *   **新品月均销售额**：`$9,903`
  *   **平均重量**：`2.23 pounds (1,011 g)`
  *   **平均体积**：`210.98 in³ (3,457 cm³)`
  *   **平均毛利率**：`55.1%`
  *   **卖家所属地**：`中国|80.0%`
  *   **搜索购买比**：`8.3‰`

---

#### 🏆 🟡-24. Head & Body Supports (头枕)

- **完整市场路径**：`Baby Products › Car Seats & Accessories › Accessories › Head & Body Supports  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.07`
  *   **平均 Reviews (Avg Reviews)**：`876 个`
  *   **物理重量 (Weight)**：`0.89 lbs`
  *   **平均退货率 (Return Rate)**：`7.72%`
  *   **平均毛利率 (Profit Margin)**：`54.53%`
  *   **品牌集中度 (Brand Concentration)**：`54.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`87.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Baby Products › Car Seats & Accessories › Accessories › Head & Body Supports  市场分析`
  *   **市场路径(中文)**：`婴儿产品 › 汽车座椅 › 辅料 › 头枕`
  *   **A+数量占比**：`88%`
  *   **新品平均评分数**：`25`
  *   **新品平均价格**：`$ 18.74`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`178`
  *   **新品月均销售额**：`$3,506`
  *   **平均重量**：`0.89 pounds (403 g)`
  *   **平均体积**：`241.62 in³ (3,959 cm³)`
  *   **平均毛利率**：`54.53%`
  *   **卖家所属地**：`中国|87.0%`
  *   **搜索购买比**：`6.0‰`

---

#### 🏆 🟡-25. Hands Free Leashes (免手持牵绳)

- **完整市场路径**：`Pet Supplies › Dogs › Collars, Harnesses & Leashes › Leashes › Hands Free Leashes  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.55`
  *   **平均 Reviews (Avg Reviews)**：`830 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`6.44%`
  *   **平均毛利率 (Profit Margin)**：`60.55%`
  *   **品牌集中度 (Brand Concentration)**：`61.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`52.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Dogs › Collars, Harnesses & Leashes › Leashes › Hands Free Leashes  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 犬类 › 项圈、背带 › 绳索 › 免手持牵绳`
  *   **A+数量占比**：`93%`
  *   **新品平均评分数**：`83`
  *   **新品平均价格**：`$ 23.34`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`252`
  *   **新品月均销售额**：`$5,703`
  *   **平均重量**：`0.71 pounds (322 g)`
  *   **平均体积**：`152.36 in³ (2,497 cm³)`
  *   **平均毛利率**：`60.55%`
  *   **卖家所属地**：`中国|52.0%`
  *   **搜索购买比**：`8.7‰`

---

#### 🏆 🟡-26. Hand Exercisers (手部锻炼器具)

- **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Occupational & Physical Therapy Aids › Hand Exercisers  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.33`
  *   **平均 Reviews (Avg Reviews)**：`811 个`
  *   **物理重量 (Weight)**：`1.40 lbs`
  *   **平均退货率 (Return Rate)**：`5.3%`
  *   **平均毛利率 (Profit Margin)**：`59.72%`
  *   **品牌集中度 (Brand Concentration)**：`62.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`61.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Medical Supplies & Equipment › Occupational & Physical Therapy Aids › Hand Exercisers  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 医疗用品和设备 › 职业和物理疗法辅助用品 › 手部锻炼器具`
  *   **A+数量占比**：`80%`
  *   **新品平均评分数**：`24`
  *   **新品平均价格**：`$ 47.59`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`136`
  *   **新品月均销售额**：`$5,075`
  *   **平均重量**：`1.40 pounds (635 g)`
  *   **平均体积**：`138.62 in³ (2,272 cm³)`
  *   **平均毛利率**：`59.72%`
  *   **卖家所属地**：`中国|61.0%`
  *   **搜索购买比**：`9.3‰`

---

#### 🏆 🟡-27. Motion Detectors (生命探测器)

- **完整市场路径**：`Electronics › Security & Surveillance › Motion Detectors  市场分析`
- **触发警示项**：`Reviews偏高 (>800), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$39.99`
  *   **平均 Reviews (Avg Reviews)**：`895 个`
  *   **物理重量 (Weight)**：`0.68 lbs`
  *   **平均退货率 (Return Rate)**：`6.68%`
  *   **平均毛利率 (Profit Margin)**：`76.93%`
  *   **品牌集中度 (Brand Concentration)**：`59.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Security & Surveillance › Motion Detectors  市场分析`
  *   **市场路径(中文)**：`电子产品 › 安全问题 › 生命探测器`
  *   **A+数量占比**：`85%`
  *   **新品平均评分数**：`55`
  *   **新品平均价格**：`$ 34.88`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`258`
  *   **新品月均销售额**：`$9,182`
  *   **平均重量**：`0.68 pounds (308 g)`
  *   **平均体积**：`90.13 in³ (1,477 cm³)`
  *   **平均毛利率**：`76.93%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`9.6‰`

---

#### 🏆 🟡-28. Alternative Medicine (替代药物)

- **完整市场路径**：`Health & Household › Health Care › Alternative Medicine  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.59`
  *   **平均 Reviews (Avg Reviews)**：`918 个`
  *   **物理重量 (Weight)**：`0.53 lbs`
  *   **平均退货率 (Return Rate)**：`2.58%`
  *   **平均毛利率 (Profit Margin)**：`67.17%`
  *   **品牌集中度 (Brand Concentration)**：`56.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`49.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Health & Household › Health Care › Alternative Medicine  市场分析`
  *   **市场路径(中文)**：`健康与家居 › 卫生保健 › 替代药物`
  *   **A+数量占比**：`64%`
  *   **新品平均评分数**：`25`
  *   **新品平均价格**：`$ 51.94`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`272`
  *   **新品月均销售额**：`$8,244`
  *   **平均重量**：`0.53 pounds (242 g)`
  *   **平均体积**：`91.06 in³ (1,492 cm³)`
  *   **平均毛利率**：`67.17%`
  *   **卖家所属地**：`美国|51.0%`
  *   **搜索购买比**：`15.3‰`

---

#### 🏆 🟡-29. Airbrush Sets (喷漆套装)

- **完整市场路径**：`Arts, Crafts & Sewing › Painting, Drawing & Art Supplies › Painting › Airbrush Materials › Airbrush Sets  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$51.37`
  *   **平均 Reviews (Avg Reviews)**：`824 个`
  *   **物理重量 (Weight)**：`2.36 lbs`
  *   **平均退货率 (Return Rate)**：`4.67%`
  *   **平均毛利率 (Profit Margin)**：`67.83%`
  *   **品牌集中度 (Brand Concentration)**：`55.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Painting, Drawing & Art Supplies › Painting › Airbrush Materials › Airbrush Sets  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 油画、素描 › 绘画 › 喷漆材料 › 喷漆套装`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`130`
  *   **新品平均价格**：`$ 45.31`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`234`
  *   **新品月均销售额**：`$11,609`
  *   **平均重量**：`2.36 pounds (1,069 g)`
  *   **平均体积**：`378.69 in³ (6,206 cm³)`
  *   **平均毛利率**：`67.83%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`5.3‰`

---

#### 🏆 🟡-30. Robots (机器人)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Robots  市场分析`
- **触发警示项**：`Reviews偏高 (>800), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$50.55`
  *   **平均 Reviews (Avg Reviews)**：`956 个`
  *   **物理重量 (Weight)**：`1.30 lbs`
  *   **平均退货率 (Return Rate)**：`6.4%`
  *   **平均毛利率 (Profit Margin)**：`64.86%`
  *   **品牌集中度 (Brand Concentration)**：`42.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Robots  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 机器人`
  *   **A+数量占比**：`99%`
  *   **新品平均评分数**：`132`
  *   **新品平均价格**：`$ 33.2`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`292`
  *   **新品月均销售额**：`$12,130`
  *   **平均重量**：`1.30 pounds (591 g)`
  *   **平均体积**：`491.49 in³ (8,054 cm³)`
  *   **平均毛利率**：`64.86%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`2.9‰`

---

#### 🏆 🟡-31. Camping Fans (露营爱好者)

- **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Camping Fans  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.29`
  *   **平均 Reviews (Avg Reviews)**：`248 个`
  *   **物理重量 (Weight)**：`2.18 lbs`
  *   **平均退货率 (Return Rate)**：`4.56%`
  *   **平均毛利率 (Profit Margin)**：`63.87%`
  *   **品牌集中度 (Brand Concentration)**：`50.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`85.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Camping Fans  市场分析`
  *   **市场路径(中文)**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › 露营爱好者`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`28`
  *   **新品平均价格**：`$ 40.79`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`278`
  *   **新品月均销售额**：`$10,821`
  *   **平均重量**：`2.18 pounds (989 g)`
  *   **平均体积**：`538.02 in³ (8,816 cm³)`
  *   **平均毛利率**：`63.87%`
  *   **卖家所属地**：`中国|85.0%`
  *   **搜索购买比**：`5.8‰`

---

#### 🏆 🟡-32. Sewing Storage (缝纫用品收纳用品)

- **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Sewing Storage  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.66`
  *   **平均 Reviews (Avg Reviews)**：`846 个`
  *   **物理重量 (Weight)**：`1.85 lbs`
  *   **平均退货率 (Return Rate)**：`5.03%`
  *   **平均毛利率 (Profit Margin)**：`52.83%`
  *   **品牌集中度 (Brand Concentration)**：`50.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Sewing Storage  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 组织，存储 › 工艺品 › 缝纫用品收纳用品`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`31`
  *   **新品平均价格**：`$ 20.24`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`262`
  *   **新品月均销售额**：`$5,916`
  *   **平均重量**：`1.85 pounds (840 g)`
  *   **平均体积**：`676.35 in³ (11,083 cm³)`
  *   **平均毛利率**：`52.83%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`7.6‰`

---

#### 🏆 🟡-33. Game Pieces (棋子)

- **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Pieces  市场分析`
- **触发警示项**：`Reviews偏高 (>800), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.59`
  *   **平均 Reviews (Avg Reviews)**：`810 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`2.83%`
  *   **平均毛利率 (Profit Margin)**：`62.58%`
  *   **品牌集中度 (Brand Concentration)**：`59.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`44.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Game Pieces  市场分析`
  *   **市场路径(中文)**：`玩具 › 游戏 › 游戏配件 › 棋子`
  *   **A+数量占比**：`59%`
  *   **新品平均评分数**：`27`
  *   **新品平均价格**：`$ 47.73`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`335`
  *   **新品月均销售额**：`$15,830`
  *   **平均重量**：`0.71 pounds (322 g)`
  *   **平均体积**：`84.11 in³ (1,378 cm³)`
  *   **平均毛利率**：`62.58%`
  *   **卖家所属地**：`美国|56.0%`
  *   **搜索购买比**：`5.6‰`

---

#### 🏆 🟡-34. Card Shufflers (洗牌机)

- **完整市场路径**：`Toys & Games › Games & Accessories › Casino Equipment › Cards & Equipment › Card Shufflers  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$41.91`
  *   **平均 Reviews (Avg Reviews)**：`526 个`
  *   **物理重量 (Weight)**：`1.47 lbs`
  *   **平均退货率 (Return Rate)**：`9.17%`
  *   **平均毛利率 (Profit Margin)**：`63.62%`
  *   **品牌集中度 (Brand Concentration)**：`60.4%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Casino Equipment › Cards & Equipment › Card Shufflers  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 赌场设备 › 卡片和设备 › 洗牌机`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`57`
  *   **新品平均价格**：`$ 49.62`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`201`
  *   **新品月均销售额**：`$7,452`
  *   **平均重量**：`1.47 pounds (669 g)`
  *   **平均体积**：`183.27 in³ (3,003 cm³)`
  *   **平均毛利率**：`63.62%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟡-35. Remote & App Controlled Vehicle Batteries (遥控)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicle Parts › Remote & App Controlled Vehicle Batteries  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$34.49`
  *   **平均 Reviews (Avg Reviews)**：`432 个`
  *   **物理重量 (Weight)**：`0.37 lbs`
  *   **平均退货率 (Return Rate)**：`6.27%`
  *   **平均毛利率 (Profit Margin)**：`65.32%`
  *   **品牌集中度 (Brand Concentration)**：`58.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicle Parts › Remote & App Controlled Vehicle Batteries  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 遥控`
  *   **A+数量占比**：`62%`
  *   **新品平均评分数**：`42`
  *   **新品平均价格**：`$ 45.95`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`324`
  *   **新品月均销售额**：`$14,896`
  *   **平均重量**：`0.37 pounds (166 g)`
  *   **平均体积**：`28.58 in³ (468 cm³)`
  *   **平均毛利率**：`65.32%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟡-36. Cooking & Baking Kits (烹饪和烘焙套件)

- **完整市场路径**：`Toys & Games › Dress Up & Pretend Play › Kitchen Toys › Cooking & Baking Kits  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.75`
  *   **平均 Reviews (Avg Reviews)**：`580 个`
  *   **物理重量 (Weight)**：`2.29 lbs`
  *   **平均退货率 (Return Rate)**：`2.98%`
  *   **平均毛利率 (Profit Margin)**：`56.4%`
  *   **品牌集中度 (Brand Concentration)**：`64.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Dress Up & Pretend Play › Kitchen Toys › Cooking & Baking Kits  市场分析`
  *   **市场路径(中文)**：`玩具 › 扮靓 › 玩具厨房 › 烹饪和烘焙套件`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`277`
  *   **新品平均价格**：`$ 38.26`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`126`
  *   **新品月均销售额**：`$4,252`
  *   **平均重量**：`2.29 pounds (1,039 g)`
  *   **平均体积**：`534.96 in³ (8,766 cm³)`
  *   **平均毛利率**：`56.4%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`8.8‰`

---

#### 🏆 🟡-37. Boats (船)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$53.66`
  *   **平均 Reviews (Avg Reviews)**：`336 个`
  *   **物理重量 (Weight)**：`1.42 lbs`
  *   **平均退货率 (Return Rate)**：`6.03%`
  *   **平均毛利率 (Profit Margin)**：`68.9%`
  *   **品牌集中度 (Brand Concentration)**：`61.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`70.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Boats  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 船`
  *   **A+数量占比**：`95%`
  *   **新品平均评分数**：`30`
  *   **新品平均价格**：`$ 52.75`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`334`
  *   **新品月均销售额**：`$15,904`
  *   **平均重量**：`1.42 pounds (644 g)`
  *   **平均体积**：`297.40 in³ (4,874 cm³)`
  *   **平均毛利率**：`68.9%`
  *   **卖家所属地**：`中国|70.0%`
  *   **搜索购买比**：`2.9‰`

---

#### 🏆 🟡-38. Accessories (辅料)

- **完整市场路径**：`Industrial & Scientific › Material Handling Products › Pulling & Lifting › Jacks & Accessories › Accessories  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.05`
  *   **平均 Reviews (Avg Reviews)**：`277 个`
  *   **物理重量 (Weight)**：`2.20 lbs`
  *   **平均退货率 (Return Rate)**：`4.87%`
  *   **平均毛利率 (Profit Margin)**：`54.56%`
  *   **品牌集中度 (Brand Concentration)**：`40.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`84.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Material Handling Products › Pulling & Lifting › Jacks & Accessories › Accessories  市场分析`
  *   **市场路径(中文)**：`工业类 › 材料处理产品 › 拉动 › 鯵鱼 › 辅料`
  *   **A+数量占比**：`84%`
  *   **新品平均评分数**：`30`
  *   **新品平均价格**：`$ 19.14`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`267`
  *   **新品月均销售额**：`$4,568`
  *   **平均重量**：`2.20 pounds (999 g)`
  *   **平均体积**：`106.95 in³ (1,753 cm³)`
  *   **平均毛利率**：`54.56%`
  *   **卖家所属地**：`中国|84.0%`
  *   **搜索购买比**：`11.2‰`

---

#### 🏆 🟡-39. Bed Mats (床垫)

- **完整市场路径**：`Pet Supplies › Cats › Beds & Furniture › Bed Mats  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.00`
  *   **平均 Reviews (Avg Reviews)**：`970 个`
  *   **物理重量 (Weight)**：`1.00 lbs`
  *   **平均退货率 (Return Rate)**：`8.45%`
  *   **平均毛利率 (Profit Margin)**：`53.13%`
  *   **品牌集中度 (Brand Concentration)**：`60.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Cats › Beds & Furniture › Bed Mats  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 猫 › 床位 › 床垫`
  *   **A+数量占比**：`89%`
  *   **新品平均评分数**：`62`
  *   **新品平均价格**：`$ 20.38`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`140`
  *   **新品月均销售额**：`$2,951`
  *   **平均重量**：`1.00 pounds (454 g)`
  *   **平均体积**：`771.52 in³ (12,643 cm³)`
  *   **平均毛利率**：`53.13%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`8.5‰`

---

#### 🏆 🟡-40. Bag Sealers (封袋机)

- **完整市场路径**：`Restaurant Appliances & Equipment › Commercial Food Preparation Equipment › Commercial Food Packaging Equipment › Bag Sealers  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$39.84`
  *   **平均 Reviews (Avg Reviews)**：`476 个`
  *   **物理重量 (Weight)**：`2.48 lbs`
  *   **平均退货率 (Return Rate)**：`6.09%`
  *   **平均毛利率 (Profit Margin)**：`70.8%`
  *   **品牌集中度 (Brand Concentration)**：`60.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`84.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Restaurant Appliances & Equipment › Commercial Food Preparation Equipment › Commercial Food Packaging Equipment › Bag Sealers  市场分析`
  *   **市场路径(中文)**：`餐厅用具 › 商业食品制备设备 › 商业食品包装设备 › 封袋机`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`68`
  *   **新品平均价格**：`$ 59.47`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`194`
  *   **新品月均销售额**：`$4,734`
  *   **平均重量**：`2.48 pounds (1,125 g)`
  *   **平均体积**：`300.51 in³ (4,924 cm³)`
  *   **平均毛利率**：`70.8%`
  *   **卖家所属地**：`中国|84.0%`
  *   **搜索购买比**：`14.3‰`

---

#### 🏆 🟡-41. Wands (Wands)

- **完整市场路径**：`Toys & Games › Dress Up & Pretend Play › Dress-Up Accessories › Wands  市场分析`
- **触发警示项**：`Reviews偏高 (>800), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.15`
  *   **平均 Reviews (Avg Reviews)**：`817 个`
  *   **物理重量 (Weight)**：`0.65 lbs`
  *   **平均退货率 (Return Rate)**：`5.37%`
  *   **平均毛利率 (Profit Margin)**：`55.09%`
  *   **品牌集中度 (Brand Concentration)**：`36.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Dress Up & Pretend Play › Dress-Up Accessories › Wands  市场分析`
  *   **市场路径(中文)**：`Toys & Games › Dress Up & Pretend Play › Dress-Up Accessories › Wands`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`30`
  *   **新品平均价格**：`$ 21.62`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`181`
  *   **新品月均销售额**：`$3,736`
  *   **平均重量**：`0.65 pounds (293 g)`
  *   **平均体积**：`112.67 in³ (1,846 cm³)`
  *   **平均毛利率**：`55.09%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`4.6‰`

---

#### 🏆 🟡-42. Spa Slippers (温泉拖鞋)

- **完整市场路径**：`Beauty & Personal Care › Foot, Hand & Nail Care › Nail Art & Polish › Tools › Spa Slippers  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.37`
  *   **平均 Reviews (Avg Reviews)**：`270 个`
  *   **物理重量 (Weight)**：`2.03 lbs`
  *   **平均退货率 (Return Rate)**：`6.02%`
  *   **平均毛利率 (Profit Margin)**：`50.52%`
  *   **品牌集中度 (Brand Concentration)**：`49.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Beauty & Personal Care › Foot, Hand & Nail Care › Nail Art & Polish › Tools › Spa Slippers  市场分析`
  *   **市场路径(中文)**：`美容与护理 › 足部护理部、手部和皮肤 › 美甲 › 工具 › 温泉拖鞋`
  *   **A+数量占比**：`81%`
  *   **新品平均评分数**：`47`
  *   **新品平均价格**：`$ 21.25`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`275`
  *   **新品月均销售额**：`$5,815`
  *   **平均重量**：`2.03 pounds (919 g)`
  *   **平均体积**：`790.56 in³ (12,955 cm³)`
  *   **平均毛利率**：`50.52%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`6.1‰`

---

#### 🏆 🟡-43. Flower Pressing (压花)

- **完整市场路径**：`Toys & Games › Arts & Crafts › Craft Kits › Flower Pressing  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.67`
  *   **平均 Reviews (Avg Reviews)**：`174 个`
  *   **物理重量 (Weight)**：`1.71 lbs`
  *   **平均退货率 (Return Rate)**：`2.87%`
  *   **平均毛利率 (Profit Margin)**：`55.05%`
  *   **品牌集中度 (Brand Concentration)**：`60.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Arts & Crafts › Craft Kits › Flower Pressing  市场分析`
  *   **市场路径(中文)**：`玩具 › 艺术 › 工艺品套装 › 压花`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`16`
  *   **新品平均价格**：`$ 17.96`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`163`
  *   **新品月均销售额**：`$3,339`
  *   **平均重量**：`1.71 pounds (773 g)`
  *   **平均体积**：`156.25 in³ (2,560 cm³)`
  *   **平均毛利率**：`55.05%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`8.6‰`

---

#### 🏆 🟡-44. Trim & Repair Kits (修整和维修套件)

- **完整市场路径**：`Tools & Home Improvement › Plumbing › Faucet Parts › Trim & Repair Kits  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.19`
  *   **平均 Reviews (Avg Reviews)**：`375 个`
  *   **物理重量 (Weight)**：`0.70 lbs`
  *   **平均退货率 (Return Rate)**：`9.84%`
  *   **平均毛利率 (Profit Margin)**：`62.84%`
  *   **品牌集中度 (Brand Concentration)**：`52.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Plumbing › Faucet Parts › Trim & Repair Kits  市场分析`
  *   **市场路径(中文)**：`工具 › 粗糙的管道系统 › 水龙头配件 › 修整和维修套件`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`15`
  *   **新品平均价格**：`$ 31.16`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`174`
  *   **新品月均销售额**：`$4,555`
  *   **平均重量**：`0.70 pounds (316 g)`
  *   **平均体积**：`146.22 in³ (2,396 cm³)`
  *   **平均毛利率**：`62.84%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`12.9‰`

---

#### 🏆 🟡-45. Excavators (挖掘机)

- **完整市场路径**：`Toys & Games › Vehicles › Construction Vehicles › Excavators  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$39.89`
  *   **平均 Reviews (Avg Reviews)**：`560 个`
  *   **物理重量 (Weight)**：`1.58 lbs`
  *   **平均退货率 (Return Rate)**：`4.33%`
  *   **平均毛利率 (Profit Margin)**：`61.07%`
  *   **品牌集中度 (Brand Concentration)**：`58.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Vehicles › Construction Vehicles › Excavators  市场分析`
  *   **市场路径(中文)**：`玩具 › 车辆 › 建筑车辆 › 挖掘机`
  *   **A+数量占比**：`86%`
  *   **新品平均评分数**：`32`
  *   **新品平均价格**：`$ 47.6`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`152`
  *   **新品月均销售额**：`$5,934`
  *   **平均重量**：`1.58 pounds (717 g)`
  *   **平均体积**：`484.98 in³ (7,947 cm³)`
  *   **平均毛利率**：`61.07%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`3.4‰`

---

#### 🏆 🟡-46. Gun Belts (枪带)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Shooting › Gun Accessories, Maintenance & Storage › Gun Holsters, Cases & Bags › Gun Belts  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.00`
  *   **平均 Reviews (Avg Reviews)**：`744 个`
  *   **物理重量 (Weight)**：`0.81 lbs`
  *   **平均退货率 (Return Rate)**：`9.02%`
  *   **平均毛利率 (Profit Margin)**：`66.89%`
  *   **品牌集中度 (Brand Concentration)**：`64.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`52.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Shooting › Gun Accessories, Maintenance & Storage › Gun Holsters, Cases & Bags › Gun Belts  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 射击 › 枪配件、维护和储存 › 枪套、箱子 › 枪带`
  *   **A+数量占比**：`78%`
  *   **新品平均评分数**：`37`
  *   **新品平均价格**：`$ 34.52`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`163`
  *   **新品月均销售额**：`$5,643`
  *   **平均重量**：`0.81 pounds (369 g)`
  *   **平均体积**：`108.70 in³ (1,781 cm³)`
  *   **平均毛利率**：`66.89%`
  *   **卖家所属地**：`中国|52.0%`
  *   **搜索购买比**：`5.9‰`

---

#### 🏆 🟡-47. Locking Devices (防盗锁)

- **完整市场路径**：`Automotive › Interior Accessories › Anti-Theft › Locking Devices  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$40.20`
  *   **平均 Reviews (Avg Reviews)**：`757 个`
  *   **物理重量 (Weight)**：`2.43 lbs`
  *   **平均退货率 (Return Rate)**：`7.5%`
  *   **平均毛利率 (Profit Margin)**：`60.6%`
  *   **品牌集中度 (Brand Concentration)**：`59.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Interior Accessories › Anti-Theft › Locking Devices  市场分析`
  *   **市场路径(中文)**：`汽车 › 内部配件 › 防盗 › 防盗锁`
  *   **A+数量占比**：`79%`
  *   **新品平均评分数**：`15`
  *   **新品平均价格**：`$ 20.46`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`121`
  *   **新品月均销售额**：`$2,572`
  *   **平均重量**：`2.43 pounds (1,101 g)`
  *   **平均体积**：`379.27 in³ (6,215 cm³)`
  *   **平均毛利率**：`60.6%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟡-48. Rods (杆)

- **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Welding Equipment › Welding Equipment & Accessories › Arc Welding Equipment › Rods  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.17`
  *   **平均 Reviews (Avg Reviews)**：`253 个`
  *   **物理重量 (Weight)**：`2.46 lbs`
  *   **平均退货率 (Return Rate)**：`1.94%`
  *   **平均毛利率 (Profit Margin)**：`59.12%`
  *   **品牌集中度 (Brand Concentration)**：`58.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`79.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Welding & Soldering › Welding Equipment › Welding Equipment & Accessories › Arc Welding Equipment › Rods  市场分析`
  *   **市场路径(中文)**：`工具 › 焊接 › 焊接设备 › 焊接设备 › 电弧焊接设备 › 杆`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`12`
  *   **新品平均价格**：`$ 18.84`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`223`
  *   **新品月均销售额**：`$4,031`
  *   **平均重量**：`2.46 pounds (1,116 g)`
  *   **平均体积**：`78.02 in³ (1,279 cm³)`
  *   **平均毛利率**：`59.12%`
  *   **卖家所属地**：`中国|79.0%`
  *   **搜索购买比**：`11.9‰`

---

#### 🏆 🟡-49. Cue Sticks (台球杆)

- **完整市场路径**：`Sports & Outdoors › Sports › Leisure Sports & Game Room › Billiards & Pool › Cue Sticks & Accessories › Cue Sticks  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$66.23`
  *   **平均 Reviews (Avg Reviews)**：`520 个`
  *   **物理重量 (Weight)**：`2.46 lbs`
  *   **平均退货率 (Return Rate)**：`5.31%`
  *   **平均毛利率 (Profit Margin)**：`63.94%`
  *   **品牌集中度 (Brand Concentration)**：`58.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`67.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Leisure Sports & Game Room › Billiards & Pool › Cue Sticks & Accessories › Cue Sticks  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动与健身 › 休闲运动游戏室 › 台球 › 球杆和配件 › 台球杆`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`52`
  *   **新品平均价格**：`$ 76.45`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`146`
  *   **新品月均销售额**：`$10,615`
  *   **平均重量**：`2.46 pounds (1,115 g)`
  *   **平均体积**：`210.69 in³ (3,453 cm³)`
  *   **平均毛利率**：`63.94%`
  *   **卖家所属地**：`中国|67.0%`
  *   **搜索购买比**：`2.4‰`

---

#### 🏆 🟡-50. Guitars & Strings (吉他)

- **完整市场路径**：`Toys & Games › Learning & Education › Musical Instruments › Guitars & Strings  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.07`
  *   **平均 Reviews (Avg Reviews)**：`625 个`
  *   **物理重量 (Weight)**：`1.30 lbs`
  *   **平均退货率 (Return Rate)**：`5.12%`
  *   **平均毛利率 (Profit Margin)**：`54.18%`
  *   **品牌集中度 (Brand Concentration)**：`58.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`68.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Learning & Education › Musical Instruments › Guitars & Strings  市场分析`
  *   **市场路径(中文)**：`玩具 › 学习 › 乐器 › 吉他`
  *   **A+数量占比**：`82%`
  *   **新品平均评分数**：`95`
  *   **新品平均价格**：`$ 33.05`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`80`
  *   **新品月均销售额**：`$2,764`
  *   **平均重量**：`1.30 pounds (588 g)`
  *   **平均体积**：`469.06 in³ (7,686 cm³)`
  *   **平均毛利率**：`54.18%`
  *   **卖家所属地**：`中国|68.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟡-51. Airplanes & Jets (飞机)

- **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Airplanes & Jets  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%), 谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$59.91`
  *   **平均 Reviews (Avg Reviews)**：`255 个`
  *   **物理重量 (Weight)**：`1.07 lbs`
  *   **平均退货率 (Return Rate)**：`8.46%`
  *   **平均毛利率 (Profit Margin)**：`66.94%`
  *   **品牌集中度 (Brand Concentration)**：`60.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`74.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Remote & App Controlled Vehicles & Parts › Remote & App Controlled Vehicles › Airplanes & Jets  市场分析`
  *   **市场路径(中文)**：`玩具 › 遥控 › 遥控 › 飞机`
  *   **A+数量占比**：`87%`
  *   **新品平均评分数**：`72`
  *   **新品平均价格**：`$ 35.66`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`231`
  *   **新品月均销售额**：`$8,357`
  *   **平均重量**：`1.07 pounds (487 g)`
  *   **平均体积**：`646.53 in³ (10,595 cm³)`
  *   **平均毛利率**：`66.94%`
  *   **卖家所属地**：`中国|74.0%`
  *   **搜索购买比**：`2.2‰`

---

#### 🏆 🟡-52. Cream Chargers & Whippers (奶油充电器)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Specialty Tools & Gadgets › Cream Chargers & Whippers  市场分析`
- **触发警示项**：`带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.66`
  *   **平均 Reviews (Avg Reviews)**：`452 个`
  *   **物理重量 (Weight)**：`1.40 lbs`
  *   **平均退货率 (Return Rate)**：`2.63%`
  *   **平均毛利率 (Profit Margin)**：`66.16%`
  *   **品牌集中度 (Brand Concentration)**：`60.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`46.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Kitchen Utensils & Gadgets › Specialty Tools & Gadgets › Cream Chargers & Whippers  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 用具厨房 › 专业工具 › 奶油充电器`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 31.96`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`256`
  *   **新品月均销售额**：`$5,881`
  *   **平均重量**：`1.40 pounds (636 g)`
  *   **平均体积**：`133.70 in³ (2,191 cm³)`
  *   **平均毛利率**：`66.16%`
  *   **卖家所属地**：`中国|46.0%`
  *   **搜索购买比**：`9.1‰`

---

#### 🏆 🟡-53. Metric Inserts & Kits (米制刀片和套件)

- **完整市场路径**：`Automotive › Tools & Equipment › Thread Repair Kits › Metric Inserts & Kits  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$44.60`
  *   **平均 Reviews (Avg Reviews)**：`179 个`
  *   **物理重量 (Weight)**：`2.37 lbs`
  *   **平均退货率 (Return Rate)**：`5.6%`
  *   **平均毛利率 (Profit Margin)**：`67.01%`
  *   **品牌集中度 (Brand Concentration)**：`59.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`81.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Thread Repair Kits › Metric Inserts & Kits  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 螺纹修理包 › 米制刀片和套件`
  *   **A+数量占比**：`67%`
  *   **新品平均评分数**：`30`
  *   **新品平均价格**：`$ 45.41`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`161`
  *   **新品月均销售额**：`$7,312`
  *   **平均重量**：`2.37 pounds (1,077 g)`
  *   **平均体积**：`145.20 in³ (2,379 cm³)`
  *   **平均毛利率**：`67.01%`
  *   **卖家所属地**：`中国|81.0%`
  *   **搜索购买比**：`9.2‰`

---

#### 🏆 🟡-54. Gaiters (护腿、护脚)

- **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Footwear & Accessories › Gaiters  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.91`
  *   **平均 Reviews (Avg Reviews)**：`417 个`
  *   **物理重量 (Weight)**：`0.65 lbs`
  *   **平均退货率 (Return Rate)**：`8.64%`
  *   **平均毛利率 (Profit Margin)**：`64.06%`
  *   **品牌集中度 (Brand Concentration)**：`54.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`66.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Outdoor Recreation › Camping & Hiking › Footwear & Accessories › Gaiters  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 外出休闲 › 露营和远足 › 鞋类及配件 › 护腿、护脚`
  *   **A+数量占比**：`83%`
  *   **新品平均评分数**：`35`
  *   **新品平均价格**：`$ 35.86`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`167`
  *   **新品月均销售额**：`$5,001`
  *   **平均重量**：`0.65 pounds (297 g)`
  *   **平均体积**：`314.60 in³ (5,155 cm³)`
  *   **平均毛利率**：`64.06%`
  *   **卖家所属地**：`中国|66.0%`
  *   **搜索购买比**：`7.2‰`

---

#### 🏆 🟡-55. Protractors (分光镜)

- **完整市场路径**：`Tools & Home Improvement › Measuring & Layout Tools › Protractors  市场分析`
- **触发警示项**：`Reviews偏高 (>800)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.63`
  *   **平均 Reviews (Avg Reviews)**：`803 个`
  *   **物理重量 (Weight)**：`0.45 lbs`
  *   **平均退货率 (Return Rate)**：`2.95%`
  *   **平均毛利率 (Profit Margin)**：`59.82%`
  *   **品牌集中度 (Brand Concentration)**：`49.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Measuring & Layout Tools › Protractors  市场分析`
  *   **市场路径(中文)**：`工具 › 测量 › 分光镜`
  *   **A+数量占比**：`79%`
  *   **新品平均评分数**：`37`
  *   **新品平均价格**：`$ 18.19`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`136`
  *   **新品月均销售额**：`$2,519`
  *   **平均重量**：`0.45 pounds (204 g)`
  *   **平均体积**：`39.15 in³ (642 cm³)`
  *   **平均毛利率**：`59.82%`
  *   **卖家所属地**：`中国|54.0%`
  *   **搜索购买比**：`9.8‰`

---

#### 🏆 🟡-56. Monoculars (单筒望远镜)

- **完整市场路径**：`Electronics › Camera & Photo › Binoculars & Scopes › Monoculars  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$75.79`
  *   **平均 Reviews (Avg Reviews)**：`599 个`
  *   **物理重量 (Weight)**：`0.69 lbs`
  *   **平均退货率 (Return Rate)**：`7.05%`
  *   **平均毛利率 (Profit Margin)**：`76.84%`
  *   **品牌集中度 (Brand Concentration)**：`63.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`64.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Electronics › Camera & Photo › Binoculars & Scopes › Monoculars  市场分析`
  *   **市场路径(中文)**：`电子产品 › 摄像机 › 双筒望远镜 › 单筒望远镜`
  *   **A+数量占比**：`91%`
  *   **新品平均评分数**：`45`
  *   **新品平均价格**：`$ 49.18`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`310`
  *   **新品月均销售额**：`$22,262`
  *   **平均重量**：`0.69 pounds (313 g)`
  *   **平均体积**：`49.95 in³ (818 cm³)`
  *   **平均毛利率**：`76.84%`
  *   **卖家所属地**：`中国|64.0%`
  *   **搜索购买比**：`7.5‰`

---

#### 🏆 🟡-57. Paint Roller Extension Poles (油漆滚筒加长杆)

- **完整市场路径**：`Tools & Home Improvement › Paint, Wall Treatments & Supplies › Painting Supplies & Tools › Paint Application Tools › Paint Roller Extension Poles  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.88`
  *   **平均 Reviews (Avg Reviews)**：`301 个`
  *   **物理重量 (Weight)**：`2.04 lbs`
  *   **平均退货率 (Return Rate)**：`4.55%`
  *   **平均毛利率 (Profit Margin)**：`54.26%`
  *   **品牌集中度 (Brand Concentration)**：`52.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Paint, Wall Treatments & Supplies › Painting Supplies & Tools › Paint Application Tools › Paint Roller Extension Poles  市场分析`
  *   **市场路径(中文)**：`工具 › 正面，正面照 › 绘画用品 › 油漆应用 › 油漆滚筒加长杆`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 49.99`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`96`
  *   **新品月均销售额**：`$5,120`
  *   **平均重量**：`2.04 pounds (926 g)`
  *   **平均体积**：`200.91 in³ (3,292 cm³)`
  *   **平均毛利率**：`54.26%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`9.4‰`

---

#### 🏆 🟡-58. Alarms & Anti-Theft (摩托车防盗器)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Electronics › Alarms & Anti-Theft  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.22`
  *   **平均 Reviews (Avg Reviews)**：`685 个`
  *   **物理重量 (Weight)**：`0.83 lbs`
  *   **平均退货率 (Return Rate)**：`4.72%`
  *   **平均毛利率 (Profit Margin)**：`62.4%`
  *   **品牌集中度 (Brand Concentration)**：`48.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Electronics › Alarms & Anti-Theft  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 辅料 › 电子产品 › 摩托车防盗器`
  *   **A+数量占比**：`74%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 57.44`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`112`
  *   **新品月均销售额**：`$5,302`
  *   **平均重量**：`0.83 pounds (374 g)`
  *   **平均体积**：`38.72 in³ (635 cm³)`
  *   **平均毛利率**：`62.4%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`6.9‰`

---

#### 🏆 🟡-59. Game Table Accessories (游戏桌配件)

- **完整市场路径**：`Toys & Games › Games & Accessories › Casino Equipment › Game Table Accessories  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$28.45`
  *   **平均 Reviews (Avg Reviews)**：`223 个`
  *   **物理重量 (Weight)**：`1.51 lbs`
  *   **平均退货率 (Return Rate)**：`7.43%`
  *   **平均毛利率 (Profit Margin)**：`58.54%`
  *   **品牌集中度 (Brand Concentration)**：`54.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Casino Equipment › Game Table Accessories  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 赌场设备 › 游戏桌配件`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`40`
  *   **新品平均价格**：`$ 34.03`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`153`
  *   **新品月均销售额**：`$4,972`
  *   **平均重量**：`1.51 pounds (685 g)`
  *   **平均体积**：`734.67 in³ (12,039 cm³)`
  *   **平均毛利率**：`58.54%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`7.8‰`

---

#### 🏆 🟡-60. Bats (蝙蝠)

- **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Bats  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.56`
  *   **平均 Reviews (Avg Reviews)**：`352 个`
  *   **物理重量 (Weight)**：`2.25 lbs`
  *   **平均退货率 (Return Rate)**：`2.61%`
  *   **平均毛利率 (Profit Margin)**：`59.46%`
  *   **品牌集中度 (Brand Concentration)**：`55.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`54.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › Bats  市场分析`
  *   **市场路径(中文)**：`Patio, Lawn & Garden › Backyard Birding & Wildlife › 蝙蝠`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 35.95`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`96`
  *   **新品月均销售额**：`$2,854`
  *   **平均重量**：`2.25 pounds (1,019 g)`
  *   **平均体积**：`552.87 in³ (9,060 cm³)`
  *   **平均毛利率**：`59.46%`
  *   **卖家所属地**：`美国|46.0%`
  *   **搜索购买比**：`14.5‰`

---

#### 🏆 🟡-61. Bulb Planters (球茎栽植器)

- **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Hand Tools › Bulb Planters  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.70`
  *   **平均 Reviews (Avg Reviews)**：`299 个`
  *   **物理重量 (Weight)**：`2.30 lbs`
  *   **平均退货率 (Return Rate)**：`2.9%`
  *   **平均毛利率 (Profit Margin)**：`51.38%`
  *   **品牌集中度 (Brand Concentration)**：`47.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`71.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Patio, Lawn & Garden › Gardening & Lawn Care › Hand Tools › Bulb Planters  市场分析`
  *   **市场路径(中文)**：`庭院、草坪和园艺 › 园艺和微笑护理 › 手动园艺工具 › 球茎栽植器`
  *   **A+数量占比**：`68%`
  *   **新品平均评分数**：`15`
  *   **新品平均价格**：`$ 22.22`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`120`
  *   **新品月均销售额**：`$2,408`
  *   **平均重量**：`2.30 pounds (1,045 g)`
  *   **平均体积**：`586.33 in³ (9,608 cm³)`
  *   **平均毛利率**：`51.38%`
  *   **卖家所属地**：`中国|71.0%`
  *   **搜索购买比**：`13.1‰`

---

#### 🏆 🟡-62. Battery Chargers (电池充电器)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Battery Chargers  市场分析`
- **触发警示项**：`带电/合规资质敏感关键字`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$37.89`
  *   **平均 Reviews (Avg Reviews)**：`396 个`
  *   **物理重量 (Weight)**：`1.50 lbs`
  *   **平均退货率 (Return Rate)**：`6.24%`
  *   **平均毛利率 (Profit Margin)**：`65.48%`
  *   **品牌集中度 (Brand Concentration)**：`55.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`79.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Accessories › Battery Chargers  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 辅料 › 电池充电器`
  *   **A+数量占比**：`79%`
  *   **新品平均评分数**：`11`
  *   **新品平均价格**：`$ 42.89`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`110`
  *   **新品月均销售额**：`$4,241`
  *   **平均重量**：`1.50 pounds (681 g)`
  *   **平均体积**：`53.50 in³ (877 cm³)`
  *   **平均毛利率**：`65.48%`
  *   **卖家所属地**：`中国|79.0%`
  *   **搜索购买比**：`8.5‰`

---

#### 🏆 🟡-63. Kick Plates (踢脚板)

- **完整市场路径**：`Tools & Home Improvement › Hardware › Door Hardware & Locks › Kick Plates  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$27.91`
  *   **平均 Reviews (Avg Reviews)**：`100 个`
  *   **物理重量 (Weight)**：`1.53 lbs`
  *   **平均退货率 (Return Rate)**：`8.07%`
  *   **平均毛利率 (Profit Margin)**：`55.45%`
  *   **品牌集中度 (Brand Concentration)**：`61.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Hardware › Door Hardware & Locks › Kick Plates  市场分析`
  *   **市场路径(中文)**：`工具 › 硬件设施 › 门五金 › 踢脚板`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 15.27`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`124`
  *   **新品月均销售额**：`$1,690`
  *   **平均重量**：`1.53 pounds (696 g)`
  *   **平均体积**：`229.51 in³ (3,761 cm³)`
  *   **平均毛利率**：`55.45%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`10.7‰`

---

#### 🏆 🟡-64. Food Processor Parts & Accessories (食物处理器零件)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Small Appliance Parts & Accessories › Food Processor Parts & Accessories  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$31.76`
  *   **平均 Reviews (Avg Reviews)**：`305 个`
  *   **物理重量 (Weight)**：`0.99 lbs`
  *   **平均退货率 (Return Rate)**：`8.72%`
  *   **平均毛利率 (Profit Margin)**：`61.9%`
  *   **品牌集中度 (Brand Concentration)**：`38.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`58.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Small Appliance Parts & Accessories › Food Processor Parts & Accessories  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 小家电配件 › 食物处理器零件`
  *   **A+数量占比**：`62%`
  *   **新品平均评分数**：`22`
  *   **新品平均价格**：`$ 24.45`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`239`
  *   **新品月均销售额**：`$5,119`
  *   **平均重量**：`0.99 pounds (448 g)`
  *   **平均体积**：`232.89 in³ (3,816 cm³)`
  *   **平均毛利率**：`61.9%`
  *   **卖家所属地**：`中国|58.0%`
  *   **搜索购买比**：`12.8‰`

---

#### 🏆 🟡-65. Air Conditioning & Heater Control (空调与加热器控制)

- **完整市场路径**：`Automotive › Replacement Parts › Switches & Relays › Switches › Air Conditioning › Air Conditioning & Heater Control  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.09`
  *   **平均 Reviews (Avg Reviews)**：`190 个`
  *   **物理重量 (Weight)**：`0.41 lbs`
  *   **平均退货率 (Return Rate)**：`9.39%`
  *   **平均毛利率 (Profit Margin)**：`62.93%`
  *   **品牌集中度 (Brand Concentration)**：`37.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`85.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Switches & Relays › Switches › Air Conditioning › Air Conditioning & Heater Control  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 开关 › 开关 › 空调 › 空调与加热器控制`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`18`
  *   **新品平均价格**：`$ 77.07`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`108`
  *   **新品月均销售额**：`$8,206`
  *   **平均重量**：`0.41 pounds (187 g)`
  *   **平均体积**：`63.13 in³ (1,035 cm³)`
  *   **平均毛利率**：`62.93%`
  *   **卖家所属地**：`中国|85.0%`
  *   **搜索购买比**：`7.6‰`

---

#### 🏆 🟡-66. Armrest Lids (扶手盖)

- **完整市场路径**：`Automotive › Replacement Parts › Body & Trim › Trim › Interior › Armrests, Parts & Accessories › Armrest Lids  市场分析`
- **触发警示项**：`重量偏重 (>2.0 lbs)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.61`
  *   **平均 Reviews (Avg Reviews)**：`266 个`
  *   **物理重量 (Weight)**：`2.27 lbs`
  *   **平均退货率 (Return Rate)**：`6.52%`
  *   **平均毛利率 (Profit Margin)**：`58.9%`
  *   **品牌集中度 (Brand Concentration)**：`55.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`89.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Replacement Parts › Body & Trim › Trim › Interior › Armrests, Parts & Accessories › Armrest Lids  市场分析`
  *   **市场路径(中文)**：`汽车 › 替换零件 › 身体 › 饰面 › 室内 › 扶手，订货 › 扶手盖`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`193`
  *   **新品平均价格**：`$ 38.22`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`86`
  *   **新品月均销售额**：`$3,800`
  *   **平均重量**：`2.27 pounds (1,031 g)`
  *   **平均体积**：`450.45 in³ (7,382 cm³)`
  *   **平均毛利率**：`58.9%`
  *   **卖家所属地**：`中国|89.0%`
  *   **搜索购买比**：`7.0‰`

---

#### 🏆 🟡-67. Breast Pump Carrying Bags (奶泵携带包)

- **完整市场路径**：`Baby Products › Feeding › Breastfeeding › Breast Pump Carrying Bags  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.83`
  *   **平均 Reviews (Avg Reviews)**：`153 个`
  *   **物理重量 (Weight)**：`1.23 lbs`
  *   **平均退货率 (Return Rate)**：`9.17%`
  *   **平均毛利率 (Profit Margin)**：`62.36%`
  *   **品牌集中度 (Brand Concentration)**：`57.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`69.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Baby Products › Feeding › Breastfeeding › Breast Pump Carrying Bags  市场分析`
  *   **市场路径(中文)**：`婴儿产品 › 喂养 › 母乳喂养 › 奶泵携带包`
  *   **A+数量占比**：`90%`
  *   **新品平均评分数**：`47`
  *   **新品平均价格**：`$ 28.11`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`161`
  *   **新品月均销售额**：`$4,573`
  *   **平均重量**：`1.23 pounds (557 g)`
  *   **平均体积**：`717.60 in³ (11,759 cm³)`
  *   **平均毛利率**：`62.36%`
  *   **卖家所属地**：`中国|69.0%`
  *   **搜索购买比**：`5.3‰`

---
