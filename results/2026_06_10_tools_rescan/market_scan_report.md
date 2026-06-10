# 亚马逊选市场扫描与评估报告 (2026-06-10)

> [!IMPORTANT]
> 本报告基于配置文件 `scripts/market_config.json` 中设定的过滤与风控规则进行生成。今日共分析了 **151** 个符合基本条件的子类目，其中最终筛选出 **65** 个适合新手的 🟢 绿色推荐赛道。
> **数量审计**：当前候选类目有 95 个，超过目标上限 15。建议提高基础过滤门槛或收紧黄色/绿色风控规则，而不是截断为固定 Top-K。
> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。

## 一、 风控分类结果概览

- **绿色通道 (推荐) 🟢**：共 **65** 个。满足所有风控参数，建议重点关注。
- **黄色通道 (谨慎) 🟡**：共 **30** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。
- **红色通道 (避坑) 🔴**：共 **56** 个。触发硬风控规则，已自动排除。

## 二、 推荐与候选子类目核心列表

### 1. 🟢 绿色推荐类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Decorative Garden Stakes** | 装饰园艺桩 | $20.07 | 373 | 0.73 lbs | 2.04% | 55.5% | 90.0% |
| 2 | **Lighting Products** | 水底灯 | $50.99 | 476 | 1.71 lbs | 6.75% | 55.2% | 75.0% |
| 3 | **Brake System Bleeding Tools** | 刹车排气 | $26.18 | 421 | 1.48 lbs | 4.69% | 49.4% | 83.0% |
| 4 | **Nozzles** | 喷嘴 | $20.16 | 200 | 0.31 lbs | 1.98% | 59.6% | 64.0% |
| 5 | **Feeders** | 喂食器 | $26.31 | 448 | 1.26 lbs | 5.44% | 37.4% | 80.0% |
| 6 | **Electrical System Tools** | 电气系统工具 | $31.78 | 442 | 1.00 lbs | 2.38% | 42.2% | 72.0% |
| 7 | **Trophies** | 奖杯 | $25.00 | 296 | 0.95 lbs | 2.59% | 46.8% | 51.0% |
| 8 | **Deck Hardware** | 五金件 | $29.38 | 440 | 1.66 lbs | 4.94% | 46.3% | 74.0% |
| 9 | **Drill Bits** | 钻头 | $26.27 | 281 | 0.96 lbs | 2.68% | 52.8% | 74.0% |
| 10 | **Grinding Discs** | 磨片 | $25.59 | 343 | 1.97 lbs | 2.13% | 45.2% | 80.0% |
| 11 | **Exterior Lighting** | 外部照明 | $24.24 | 478 | 0.77 lbs | 4.66% | 52.4% | 69.0% |
| 12 | **Pipe Clamps** | 管夹 | $20.87 | 282 | 1.85 lbs | 5.92% | 42.9% | 71.0% |
| 13 | **Headlights** | 车头灯 | $32.36 | 449 | 0.46 lbs | 5.21% | 46.5% | 75.0% |
| 14 | **Float Valves** | 浮阀 | $21.24 | 185 | 0.66 lbs | 4.44% | 40.9% | 67.0% |
| 15 | **Seat Belts** | 安全带 | $33.72 | 198 | 1.52 lbs | 5.78% | 54.0% | 76.0% |
| 16 | **Leak Detection Tools** | 泄漏检测工具 | $99.91 | 146 | 1.46 lbs | 4.3% | 52.6% | 48.0% |
| 17 | **Seat Covers** | 摩托车座套 | $30.50 | 305 | 1.09 lbs | 5.29% | 49.4% | 82.0% |
| 18 | **Angle Grinder Wheels** | 角磨机砂轮 | $24.63 | 142 | 1.51 lbs | 2.41% | 50.5% | 81.0% |
| 19 | **Tortilla Servers** | 玉米饼服务员 | $20.62 | 474 | 1.57 lbs | 6.26% | 57.4% | 39.0% |
| 20 | **Optics Accessories** | 光学配件 | $31.80 | 353 | 0.20 lbs | 5.63% | 51.9% | 40.0% |
| 21 | **Weaving Looms** | 织机 | $24.17 | 389 | 1.06 lbs | 3.33% | 57.3% | 70.0% |
| 22 | **Canvas Tools & Accessories** | 帆布工具 | $21.57 | 268 | 1.07 lbs | 7.32% | 51.3% | 64.0% |
| 23 | **Growth Charts** | 身高墙贴 | $20.53 | 419 | 0.79 lbs | 3.72% | 48.4% | 64.0% |
| 24 | **Bumper Guards** | 保险杠防护装置 | $35.16 | 466 | 1.67 lbs | 7.85% | 38.7% | 66.0% |
| 25 | **Fly Tying Equipment** | 绑蝇设备 | $20.38 | 489 | 0.25 lbs | 2.84% | 61.0% | 50.0% |
| 26 | **Trim** | 装饰 | $27.92 | 252 | 0.27 lbs | 2.44% | 62.4% | 68.0% |
| 27 | **Gutters** | 排水沟 | $24.12 | 159 | 1.61 lbs | 5.02% | 52.1% | 66.0% |
| 28 | **Bait Traps** | 诱饵陷阱 | $26.98 | 291 | 1.75 lbs | 3.31% | 57.3% | 57.0% |
| 29 | **Flags** | 标志 | $23.22 | 222 | 0.56 lbs | 2.61% | 60.6% | 52.0% |
| 30 | **Bags & Cases** | 麦克风箱包 | $27.22 | 235 | 1.01 lbs | 6.87% | 50.3% | 63.0% |
| 31 | **Tools** | 工具 | $31.56 | 210 | 1.33 lbs | 3.64% | 45.3% | 59.0% |
| 32 | **Pressure Regulators** | 压力调节器 | $33.79 | 291 | 0.71 lbs | 5.93% | 53.1% | 74.0% |
| 33 | **Fuel System** | 燃油系统 | $23.87 | 97 | 0.60 lbs | 4.31% | 49.8% | 81.0% |
| 34 | **Trash Can Lids** | 垃圾桶盖 | $23.55 | 148 | 1.37 lbs | 5.21% | 54.5% | 55.0% |
| 35 | **Pool Heater & Heat Pump Parts** | 气筒气泵 | $84.07 | 96 | 1.99 lbs | 6.71% | 46.5% | 70.0% |
| 36 | **Collectible Vehicles** | 交通工具摆件 | $24.27 | 226 | 0.96 lbs | 5.81% | 63.8% | 87.0% |
| 37 | **Automatic Feeders** | 自动食盆 | $20.93 | 224 | 1.33 lbs | 7.46% | 43.6% | 90.0% |
| 38 | **Car Rack Parts & Accessories** | 汽车货架零件和配件 | $42.76 | 219 | 1.33 lbs | 6.72% | 44.8% | 57.0% |
| 39 | **3D Printer Extruders** | 3D打印机挤出机 | $29.04 | 158 | 0.18 lbs | 4.99% | 61.2% | 80.0% |
| 40 | **Guitar & Bass Accessories** | 吉他 | $39.96 | 447 | 0.70 lbs | 3.89% | 60.3% | 54.2% |
| 41 | **Wine Decanters** | 醒酒器 | $45.82 | 398 | 1.82 lbs | 5.52% | 58.5% | 45.0% |
| 42 | **Deviled Egg Plates** | 咸蛋盘 | $22.22 | 338 | 1.92 lbs | 5.01% | 58.2% | 62.0% |
| 43 | **Brazing Rods** | 钎杆 | $38.39 | 178 | 0.65 lbs | 2.03% | 61.6% | 55.0% |
| 44 | **Fuel** | 燃油表 | $32.90 | 113 | 0.42 lbs | 4.87% | 52.2% | 67.0% |
| 45 | **Angle** | 角规 | $25.40 | 404 | 0.54 lbs | 2.9% | 60.0% | 64.0% |
| 46 | **Nail Pullers** | 羊角起钉钳 | $23.71 | 366 | 1.29 lbs | 2.27% | 61.3% | 60.0% |
| 47 | **Controls** | 控制装置 | $37.09 | 147 | 0.94 lbs | 6.59% | 39.5% | 83.0% |
| 48 | **Tools** | 工具 | $35.71 | 143 | 1.63 lbs | 2.89% | 56.7% | 73.0% |
| 49 | **Brake Levers** | 刹车握把 | $25.84 | 293 | 0.48 lbs | 6.24% | 54.9% | 62.0% |
| 50 | **Latch Hook Kits** | 锁钩套件 | $20.76 | 223 | 0.86 lbs | 2.72% | 64.8% | 89.0% |
| 51 | **Tailgate Locks** | 后挡板锁 | $36.87 | 280 | 1.21 lbs | 6.56% | 58.7% | 65.0% |
| 52 | **Dispensing Bottles** | 点胶瓶 | $20.01 | 191 | 1.36 lbs | 4.29% | 64.6% | 51.0% |
| 53 | **Oil Pressure Tools** | 油压工具 | $29.19 | 133 | 1.03 lbs | 5.44% | 51.9% | 77.0% |
| 54 | **Relief Valves** | 减压阀 | $38.54 | 130 | 0.71 lbs | 6.22% | 53.0% | 47.0% |
| 55 | **Multifunction Tools** | 多功能工具 | $26.55 | 473 | 0.44 lbs | 3.33% | 64.2% | 55.0% |
| 56 | **Embroidery Storage** | 绣花收纳 | $23.24 | 223 | 1.33 lbs | 4.95% | 53.3% | 89.0% |
| 57 | **Carriers** | 外带用品 | $23.05 | 227 | 1.35 lbs | 6.02% | 53.0% | 78.0% |
| 58 | **French Bread & Baguette Pans** | 法式面包 | $22.35 | 321 | 1.37 lbs | 3.64% | 62.9% | 76.8% |
| 59 | **Knitting Looms & Boards** | 编织机、织布机 | $29.44 | 386 | 1.81 lbs | 5.9% | 49.9% | 83.0% |
| 60 | **Wiring Harnesses** | 线束 | $30.28 | 142 | 1.34 lbs | 5.2% | 58.1% | 82.0% |
| 61 | **Hunting Dog Equipment** | 猎犬装备 | $32.34 | 284 | 0.99 lbs | 5.22% | 57.7% | 43.0% |
| 62 | **UV Phone Sterilizer Boxes** | 紫外线手机消毒盒 | $57.83 | 356 | 1.83 lbs | 7.51% | 62.0% | 27.0% |
| 63 | **Surface Grinding Wheels** | 表面磨轮 | $33.05 | 161 | 1.13 lbs | 3.73% | 59.3% | 56.0% |
| 64 | **Handles** | 手柄 | $24.60 | 285 | 0.49 lbs | 7.11% | 46.2% | 73.0% |
| 65 | **Paper Craft Tools** | 纸工艺工具 | $36.65 | 283 | 1.55 lbs | 4.13% | 58.7% | 57.0% |

### 2. 🟡 黄色候选类目

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Compressed Air Dusters** | 压缩除尘罐 | $33.30 | 379 | 0.88 lbs | 3.16% | 谨慎认证类目路径 |
| 2 | **Batteries & Battery Chargers** | 电池和电池 | $23.68 | 483 | 0.94 lbs | 9.83% | 退货率偏高 (>8.0%), 带电/合规资质敏感关键字 |
| 3 | **Decorative Trays** | 装饰性托盘 | $23.97 | 477 | 1.60 lbs | 9.52% | 退货率偏高 (>8.0%) |
| 4 | **Cup Carriers** | 外卖杯托盘 | $22.00 | 447 | 2.43 lbs | 4.6% | 重量偏重 (>2.0 lbs) |
| 5 | **Camping Fans** | 露营爱好者 | $38.29 | 248 | 2.18 lbs | 4.56% | 重量偏重 (>2.0 lbs) |
| 6 | **Remote & App Controlled Vehicle Batteries** | 遥控 | $34.49 | 432 | 0.37 lbs | 6.27% | 谨慎认证类目路径 |
| 7 | **Boats** | 船 | $53.66 | 336 | 1.42 lbs | 6.03% | 谨慎认证类目路径 |
| 8 | **Accessories** | 辅料 | $20.05 | 277 | 2.20 lbs | 4.87% | 重量偏重 (>2.0 lbs) |
| 9 | **Bag Sealers** | 封袋机 | $39.84 | 476 | 2.48 lbs | 6.09% | 重量偏重 (>2.0 lbs) |
| 10 | **Spa Slippers** | 温泉拖鞋 | $25.37 | 270 | 2.03 lbs | 6.02% | 重量偏重 (>2.0 lbs) |
| 11 | **Flower Pressing** | 压花 | $22.67 | 174 | 1.71 lbs | 2.87% | 谨慎认证类目路径 |
| 12 | **Trim & Repair Kits** | 修整和维修套件 | $38.19 | 375 | 0.70 lbs | 9.84% | 退货率偏高 (>8.0%) |
| 13 | **Rods** | 杆 | $22.17 | 253 | 2.46 lbs | 1.94% | 重量偏重 (>2.0 lbs) |
| 14 | **Airplanes & Jets** | 飞机 | $59.91 | 255 | 1.07 lbs | 8.46% | 退货率偏高 (>8.0%), 谨慎认证类目路径 |
| 15 | **Cream Chargers & Whippers** | 奶油充电器 | $36.66 | 452 | 1.40 lbs | 2.63% | 带电/合规资质敏感关键字 |
| 16 | **Metric Inserts & Kits** | 米制刀片和套件 | $44.60 | 179 | 2.37 lbs | 5.6% | 重量偏重 (>2.0 lbs) |
| 17 | **Gaiters** | 护腿、护脚 | $32.91 | 417 | 0.65 lbs | 8.64% | 退货率偏高 (>8.0%) |
| 18 | **Paint Roller Extension Poles** | 油漆滚筒加长杆 | $36.88 | 301 | 2.04 lbs | 4.55% | 重量偏重 (>2.0 lbs) |
| 19 | **Game Table Accessories** | 游戏桌配件 | $28.45 | 223 | 1.51 lbs | 7.43% | 谨慎认证类目路径 |
| 20 | **Bats** | 蝙蝠 | $35.56 | 352 | 2.25 lbs | 2.61% | 重量偏重 (>2.0 lbs) |
| 21 | **Bulb Planters** | 球茎栽植器 | $23.70 | 299 | 2.30 lbs | 2.9% | 重量偏重 (>2.0 lbs) |
| 22 | **Battery Chargers** | 电池充电器 | $37.89 | 396 | 1.50 lbs | 6.24% | 带电/合规资质敏感关键字 |
| 23 | **Kick Plates** | 踢脚板 | $27.91 | 100 | 1.53 lbs | 8.07% | 退货率偏高 (>8.0%) |
| 24 | **Food Processor Parts & Accessories** | 食物处理器零件 | $31.76 | 305 | 0.99 lbs | 8.72% | 退货率偏高 (>8.0%) |
| 25 | **Air Conditioning & Heater Control** | 空调与加热器控制 | $32.09 | 190 | 0.41 lbs | 9.39% | 退货率偏高 (>8.0%) |
| 26 | **Armrest Lids** | 扶手盖 | $33.61 | 266 | 2.27 lbs | 6.52% | 重量偏重 (>2.0 lbs) |
| 27 | **Breast Pump Carrying Bags** | 奶泵携带包 | $36.83 | 153 | 1.23 lbs | 9.17% | 退货率偏高 (>8.0%) |
| 28 | **Doors** | 门 | $34.68 | 294 | 1.48 lbs | 9.72% | 退货率偏高 (>8.0%) |
| 29 | **Heating & Temperature Control** | 暖气 | $25.19 | 128 | 1.09 lbs | 9.98% | 退货率偏高 (>8.0%) |
| 30 | **Dice Bags & Boxes** | 骰袋和骰盒 | $22.05 | 440 | 0.70 lbs | 3.93% | 谨慎认证类目路径 |

### 3. 🔴 红色排除类目摘要

| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Skirt Sets** | 裙装套装 | $34.63 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 2 | **Tankini Sets** | 坦基尼套装 | $21.91 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 3 | **Sets** | 套 | $24.02 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 4 | **Rash Guard Sets** | Rash Guard Sets | $20.58 | 高风险类目路径过滤 |
| 5 | **Active Pants** | 运动裤 | $32.22 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 6 | **Button-Down Shirts** | 扣角领衬衫 | $20.66 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 7 | **Jumpsuits & Rompers** | 连身裤 | $21.14 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 8 | **Wall Molding & Trim** | 墙压条和镶边 | $20.31 | 退货率过高 (>10.0%) |
| 9 | **Candlestick Holders** | 烛台座 | $24.44 | 退货率过高 (>10.0%) |
| 10 | **Paddleboard Accessories** | 冲浪板配件 | $55.98 | 重量超标 (>2.5 lbs) |
| 11 | **Smokeless Inhalers** | 无烟吸入器 | $20.87 | 排除类关键字过滤 |
| 12 | **Home Décor Products** | 家居装饰 | $20.89 | 退货率过高 (>10.0%) |
| 13 | **Oolong** | 乌龙 | $20.90 | 高风险类目路径过滤 |
| 14 | **Insulin Injectors** | 胰岛素注射器 | $23.72 | 排除类关键字过滤, 高风险类目路径过滤 |
| 15 | **Brake Adjusting Tools** | 制动器调整工具 | $20.61 | 重量超标 (>2.5 lbs) |
| 16 | **Tattoo Kits** | 纹身套装 | $31.97 | 高风险类目路径过滤 |
| 17 | **Clutches** | 手拿包 | $34.11 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 18 | **Picture Frames** | 画框 | $28.79 | 重量超标 (>2.5 lbs) |
| 19 | **Sweatpants** | Sweatpants | $26.89 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 20 | **Protective Gear** | 防护装备 | $38.53 | 重量超标 (>2.5 lbs) |
| 21 | **Hoes** | 园艺锄 | $29.39 | 重量超标 (>2.5 lbs) |
| 22 | **Tops** | Tops | $21.42 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 23 | **Jerseys** | 球衣 | $34.74 | 高风险类目路径过滤 |
| 24 | **Syrup & Honey Dispensers** | 饮料桶嘴 | $21.80 | 退货率过高 (>10.0%) |
| 25 | **Hoodies** | 帽衫 | $38.53 | 高风险类目路径过滤 |
| 26 | **Faucets** | 水龙头 | $29.41 | 退货率过高 (>10.0%) |
| 27 | **Floor Molding & Trim** | 地板压条和镶边 | $25.44 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 28 | **Pant Sets** | 长裤套装 | $23.16 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 29 | **Sound Therapy** | 声音疗法 | $43.04 | 高风险类目路径过滤 |
| 30 | **Oxygen** | 氧气 | $42.95 | 退货率过高 (>10.0%) |
| 31 | **In-Dash Navigation** | 内置车载导航 | $111.36 | 退货率过高 (>10.0%) |
| 32 | **Workout Top & Bottom Sets** | 服装套装 | $32.35 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 33 | **Signal Converters** | 信号转换器 | $30.27 | 退货率过高 (>10.0%) |
| 34 | **AV Receivers & Amplifiers** | AV接收机 | $117.53 | 退货率过高 (>10.0%) |
| 35 | **Post Light Accessories** | 柱灯配件 | $31.05 | 重量超标 (>2.5 lbs) |
| 36 | **Wormers** | 虫子 | $39.87 | 排除类关键字过滤 |
| 37 | **Clothing** | 服装 | $20.81 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 38 | **Shoulder Bags** | 单肩包 | $43.81 | 高风险类目路径过滤 |
| 39 | **Candle Sconces** | 壁突式烛台 | $27.93 | 退货率过高 (>10.0%) |
| 40 | **Urinal Accessories** | 小便池配件 | $34.73 | 重量超标 (>2.5 lbs) |
| 41 | **Lab Supply Dispensers** | 实验室用品分配器 | $32.42 | 重量超标 (>2.5 lbs) |
| 42 | **Digital Media Receivers** | 数字媒体接收器 | $149.04 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 43 | **Candleholder Sets** | 烛台套装 | $30.61 | 退货率过高 (>10.0%) |
| 44 | **Jerseys** | Jerseys | $20.81 | 高风险类目路径过滤 |
| 45 | **Night Vision Binoculars & Goggles** | 夜视双筒望远镜和护目镜 | $103.29 | 退货率过高 (>10.0%) |
| 46 | **Accessories** | 辅料 | $21.50 | 重量超标 (>2.5 lbs) |
| 47 | **Vests** | 单马甲 | $25.13 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 48 | **In-Dash DVD & Video Receivers** | 仪表盘视频 | $153.19 | 退货率过高 (>10.0%), 重量超标 (>2.5 lbs) |
| 49 | **Footwear** | 鞋靴 | $38.53 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 50 | **One-Piece Pajamas** | 连体睡衣 | $31.61 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 51 | **Clothing** | 衣服 | $20.88 | 高风险类目路径过滤 |
| 52 | **Card Playing** | 纸牌游戏 | $20.47 | 高风险类目路径过滤 |
| 53 | **Pocket Watches** | 怀表 | $29.56 | 高风险类目路径过滤 |
| 54 | **Tools** | 工具 | $46.19 | 重量超标 (>2.5 lbs) |
| 55 | **Ostomy Belts** | 造口术束带 | $25.01 | 退货率过高 (>10.0%), 高风险类目路径过滤 |
| 56 | **Christening** | 洗礼服 | $31.71 | 退货率过高 (>10.0%), 高风险类目路径过滤 |

## 三、 候选类目详细数据指标画像 (供大模型分析使用)

以下为入选的绿色与黄色子类目的完整数据指标。您可以将这些数据输入大模型（如 Gemini、Claude），让其结合具体品类特性进行深入的入选原因、产品特征及商业机会评估。

### 🟢 绿色类目详情列表

#### 🏆 🟢-1. Decorative Garden Stakes (装饰园艺桩)

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

#### 🏆 🟢-2. Lighting Products (水底灯)

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

#### 🏆 🟢-3. Brake System Bleeding Tools (刹车排气)

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

#### 🏆 🟢-4. Nozzles (喷嘴)

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

#### 🏆 🟢-5. Feeders (喂食器)

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

#### 🏆 🟢-6. Electrical System Tools (电气系统工具)

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

#### 🏆 🟢-7. Trophies (奖杯)

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

#### 🏆 🟢-8. Deck Hardware (五金件)

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

#### 🏆 🟢-9. Drill Bits (钻头)

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

#### 🏆 🟢-10. Grinding Discs (磨片)

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

#### 🏆 🟢-11. Exterior Lighting (外部照明)

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

#### 🏆 🟢-12. Pipe Clamps (管夹)

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

#### 🏆 🟢-13. Headlights (车头灯)

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

#### 🏆 🟢-14. Float Valves (浮阀)

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

#### 🏆 🟢-15. Seat Belts (安全带)

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

#### 🏆 🟢-16. Leak Detection Tools (泄漏检测工具)

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

#### 🏆 🟢-17. Seat Covers (摩托车座套)

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

#### 🏆 🟢-18. Angle Grinder Wheels (角磨机砂轮)

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

#### 🏆 🟢-19. Tortilla Servers (玉米饼服务员)

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

#### 🏆 🟢-20. Optics Accessories (光学配件)

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

#### 🏆 🟢-21. Weaving Looms (织机)

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

#### 🏆 🟢-22. Canvas Tools & Accessories (帆布工具)

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

#### 🏆 🟢-23. Growth Charts (身高墙贴)

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

#### 🏆 🟢-24. Bumper Guards (保险杠防护装置)

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

#### 🏆 🟢-25. Fly Tying Equipment (绑蝇设备)

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

#### 🏆 🟢-26. Trim (装饰)

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

#### 🏆 🟢-27. Gutters (排水沟)

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

#### 🏆 🟢-28. Bait Traps (诱饵陷阱)

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

#### 🏆 🟢-29. Flags (标志)

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

#### 🏆 🟢-30. Bags & Cases (麦克风箱包)

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

#### 🏆 🟢-31. Tools (工具)

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

#### 🏆 🟢-32. Pressure Regulators (压力调节器)

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

#### 🏆 🟢-33. Fuel System (燃油系统)

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

#### 🏆 🟢-34. Trash Can Lids (垃圾桶盖)

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

#### 🏆 🟢-35. Pool Heater & Heat Pump Parts (气筒气泵)

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

#### 🏆 🟢-36. Collectible Vehicles (交通工具摆件)

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

#### 🏆 🟢-37. Automatic Feeders (自动食盆)

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

#### 🏆 🟢-38. Car Rack Parts & Accessories (汽车货架零件和配件)

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

#### 🏆 🟢-39. 3D Printer Extruders (3D打印机挤出机)

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

#### 🏆 🟢-40. Guitar & Bass Accessories (吉他)

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

#### 🏆 🟢-41. Wine Decanters (醒酒器)

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

#### 🏆 🟢-42. Deviled Egg Plates (咸蛋盘)

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

#### 🏆 🟢-43. Brazing Rods (钎杆)

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

#### 🏆 🟢-44. Fuel (燃油表)

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

#### 🏆 🟢-45. Angle (角规)

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

#### 🏆 🟢-46. Nail Pullers (羊角起钉钳)

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

#### 🏆 🟢-47. Controls (控制装置)

- **完整市场路径**：`Tools & Home Improvement › Electrical › Electric Motors › Mounts & Accessories › Controls  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$37.09`
  *   **平均 Reviews (Avg Reviews)**：`147 个`
  *   **物理重量 (Weight)**：`0.94 lbs`
  *   **平均退货率 (Return Rate)**：`6.59%`
  *   **平均毛利率 (Profit Margin)**：`62.97%`
  *   **品牌集中度 (Brand Concentration)**：`39.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Tools & Home Improvement › Electrical › Electric Motors › Mounts & Accessories › Controls  市场分析`
  *   **市场路径(中文)**：`工具 › 电气 › 电动马达 › 悬架 › 控制装置`
  *   **A+数量占比**：`63%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 23.54`
  *   **新品平均星级**：`3.7`
  *   **新品月均销量**：`109`
  *   **新品月均销售额**：`$2,401`
  *   **平均重量**：`0.94 pounds (425 g)`
  *   **平均体积**：`164.59 in³ (2,697 cm³)`
  *   **平均毛利率**：`62.97%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`9.0‰`

---

#### 🏆 🟢-48. Tools (工具)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Stained Glass Making › Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$35.71`
  *   **平均 Reviews (Avg Reviews)**：`143 个`
  *   **物理重量 (Weight)**：`1.63 lbs`
  *   **平均退货率 (Return Rate)**：`2.89%`
  *   **平均毛利率 (Profit Margin)**：`61.69%`
  *   **品牌集中度 (Brand Concentration)**：`56.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Stained Glass Making › Tools  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 彩色玻璃制作 › 工具`
  *   **A+数量占比**：`56%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 43.04`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`79`
  *   **新品月均销售额**：`$2,801`
  *   **平均重量**：`1.63 pounds (739 g)`
  *   **平均体积**：`195.69 in³ (3,207 cm³)`
  *   **平均毛利率**：`61.69%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`8.0‰`

---

#### 🏆 🟢-49. Brake Levers (刹车握把)

- **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Parts & Components › Bike Brakes & Parts › Brake Parts › Brake Levers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.84`
  *   **平均 Reviews (Avg Reviews)**：`293 个`
  *   **物理重量 (Weight)**：`0.48 lbs`
  *   **平均退货率 (Return Rate)**：`6.24%`
  *   **平均毛利率 (Profit Margin)**：`59.61%`
  *   **品牌集中度 (Brand Concentration)**：`54.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`62.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Parts & Components › Bike Brakes & Parts › Brake Parts › Brake Levers  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 骑自行车 › 喜欢 › 锂电池 › 投诉 › 刹车握把`
  *   **A+数量占比**：`44%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 18.27`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`105`
  *   **新品月均销售额**：`$1,982`
  *   **平均重量**：`0.48 pounds (219 g)`
  *   **平均体积**：`84.48 in³ (1,384 cm³)`
  *   **平均毛利率**：`59.61%`
  *   **卖家所属地**：`中国|62.0%`
  *   **搜索购买比**：`5.5‰`

---

#### 🏆 🟢-50. Latch Hook Kits (锁钩套件)

- **完整市场路径**：`Arts, Crafts & Sewing › Needlework › Latch Hook › Latch Hook Kits  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.76`
  *   **平均 Reviews (Avg Reviews)**：`223 个`
  *   **物理重量 (Weight)**：`0.86 lbs`
  *   **平均退货率 (Return Rate)**：`2.72%`
  *   **平均毛利率 (Profit Margin)**：`57.12%`
  *   **品牌集中度 (Brand Concentration)**：`64.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`89.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Needlework › Latch Hook › Latch Hook Kits  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 针线活 › 插销钩 › 锁钩套件`
  *   **A+数量占比**：`55%`
  *   **新品平均评分数**：`16`
  *   **新品平均价格**：`$ 21.7`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`98`
  *   **新品月均销售额**：`$2,000`
  *   **平均重量**：`0.86 pounds (392 g)`
  *   **平均体积**：`229.80 in³ (3,766 cm³)`
  *   **平均毛利率**：`57.12%`
  *   **卖家所属地**：`中国|89.0%`
  *   **搜索购买比**：`4.3‰`

---

#### 🏆 🟢-51. Tailgate Locks (后挡板锁)

- **完整市场路径**：`Automotive › Exterior Accessories › Truck Bed & Tailgate Accessories › Tailgate Locks  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.87`
  *   **平均 Reviews (Avg Reviews)**：`280 个`
  *   **物理重量 (Weight)**：`1.21 lbs`
  *   **平均退货率 (Return Rate)**：`6.56%`
  *   **平均毛利率 (Profit Margin)**：`65.55%`
  *   **品牌集中度 (Brand Concentration)**：`58.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`65.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Exterior Accessories › Truck Bed & Tailgate Accessories › Tailgate Locks  市场分析`
  *   **市场路径(中文)**：`汽车 › 外部配件 › 卡车床 › 后挡板锁`
  *   **A+数量占比**：`76%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 24.62`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`111`
  *   **新品月均销售额**：`$2,903`
  *   **平均重量**：`1.21 pounds (549 g)`
  *   **平均体积**：`86.38 in³ (1,416 cm³)`
  *   **平均毛利率**：`65.55%`
  *   **卖家所属地**：`中国|65.0%`
  *   **搜索购买比**：`9.2‰`

---

#### 🏆 🟢-52. Dispensing Bottles (点胶瓶)

- **完整市场路径**：`Industrial & Scientific › Lab & Scientific Products › Glassware & Labware › Lab Bottles & Jars › Dispensing Bottles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$20.01`
  *   **平均 Reviews (Avg Reviews)**：`191 个`
  *   **物理重量 (Weight)**：`1.36 lbs`
  *   **平均退货率 (Return Rate)**：`4.29%`
  *   **平均毛利率 (Profit Margin)**：`54.8%`
  *   **品牌集中度 (Brand Concentration)**：`64.6%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`51.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Lab & Scientific Products › Glassware & Labware › Lab Bottles & Jars › Dispensing Bottles  市场分析`
  *   **市场路径(中文)**：`工业类 › 实验室 › 玻璃器皿 › 实验瓶 › 点胶瓶`
  *   **A+数量占比**：`35%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 16.93`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`60`
  *   **新品月均销售额**：`$811`
  *   **平均重量**：`1.36 pounds (619 g)`
  *   **平均体积**：`84.46 in³ (1,384 cm³)`
  *   **平均毛利率**：`54.8%`
  *   **卖家所属地**：`中国|51.0%`
  *   **搜索购买比**：`13.1‰`

---

#### 🏆 🟢-53. Oil Pressure Tools (油压工具)

- **完整市场路径**：`Automotive › Tools & Equipment › Engine Tools › Oil Pressure Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.19`
  *   **平均 Reviews (Avg Reviews)**：`133 个`
  *   **物理重量 (Weight)**：`1.03 lbs`
  *   **平均退货率 (Return Rate)**：`5.44%`
  *   **平均毛利率 (Profit Margin)**：`58.63%`
  *   **品牌集中度 (Brand Concentration)**：`51.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`77.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Tools & Equipment › Engine Tools › Oil Pressure Tools  市场分析`
  *   **市场路径(中文)**：`汽车 › 工具 › 发动机工具 › 油压工具`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`10`
  *   **新品平均价格**：`$ 28.01`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`46`
  *   **新品月均销售额**：`$1,224`
  *   **平均重量**：`1.03 pounds (466 g)`
  *   **平均体积**：`95.55 in³ (1,566 cm³)`
  *   **平均毛利率**：`58.63%`
  *   **卖家所属地**：`中国|77.0%`
  *   **搜索购买比**：`11.7‰`

---

#### 🏆 🟢-54. Relief Valves (减压阀)

- **完整市场路径**：`Industrial & Scientific › Hydraulics, Pneumatics & Plumbing › Fittings › Valves › Relief Valves  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$38.54`
  *   **平均 Reviews (Avg Reviews)**：`130 个`
  *   **物理重量 (Weight)**：`0.71 lbs`
  *   **平均退货率 (Return Rate)**：`6.22%`
  *   **平均毛利率 (Profit Margin)**：`69.11%`
  *   **品牌集中度 (Brand Concentration)**：`53.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`47.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Hydraulics, Pneumatics & Plumbing › Fittings › Valves › Relief Valves  市场分析`
  *   **市场路径(中文)**：`工业类 › 液压系统、气动系统 › 配件 › 阀门 › 减压阀`
  *   **A+数量占比**：`51%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 36.89`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`64`
  *   **新品月均销售额**：`$2,245`
  *   **平均重量**：`0.71 pounds (324 g)`
  *   **平均体积**：`37.78 in³ (619 cm³)`
  *   **平均毛利率**：`69.11%`
  *   **卖家所属地**：`美国|53.0%`
  *   **搜索购买比**：`19.4‰`

---

#### 🏆 🟢-55. Multifunction Tools (多功能工具)

- **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Bike Tools & Maintenance › Multifunction Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$26.55`
  *   **平均 Reviews (Avg Reviews)**：`473 个`
  *   **物理重量 (Weight)**：`0.44 lbs`
  *   **平均退货率 (Return Rate)**：`3.33%`
  *   **平均毛利率 (Profit Margin)**：`63.69%`
  *   **品牌集中度 (Brand Concentration)**：`64.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`55.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Sports › Cycling › Bike Tools & Maintenance › Multifunction Tools  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 运动的 › 骑自行车 › 跑步者装备 › 多功能工具`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 15.99`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`75`
  *   **新品月均销售额**：`$1,172`
  *   **平均重量**：`0.44 pounds (198 g)`
  *   **平均体积**：`27.27 in³ (447 cm³)`
  *   **平均毛利率**：`63.69%`
  *   **卖家所属地**：`中国|55.0%`
  *   **搜索购买比**：`6.6‰`

---

#### 🏆 🟢-56. Embroidery Storage (绣花收纳)

- **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Embroidery Storage  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.24`
  *   **平均 Reviews (Avg Reviews)**：`223 个`
  *   **物理重量 (Weight)**：`1.33 lbs`
  *   **平均退货率 (Return Rate)**：`4.95%`
  *   **平均毛利率 (Profit Margin)**：`57.08%`
  *   **品牌集中度 (Brand Concentration)**：`53.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`89.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Organization, Storage & Transport › Craft & Sewing Supplies Storage › Embroidery Storage  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 组织，存储 › 工艺品 › 绣花收纳`
  *   **A+数量占比**：`58%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 25.19`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`54`
  *   **新品月均销售额**：`$1,251`
  *   **平均重量**：`1.33 pounds (604 g)`
  *   **平均体积**：`226.74 in³ (3,716 cm³)`
  *   **平均毛利率**：`57.08%`
  *   **卖家所属地**：`中国|89.0%`
  *   **搜索购买比**：`7.6‰`

---

#### 🏆 🟢-57. Carriers (外带用品)

- **完整市场路径**：`Pet Supplies › Small Animals › Carriers  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$23.05`
  *   **平均 Reviews (Avg Reviews)**：`227 个`
  *   **物理重量 (Weight)**：`1.35 lbs`
  *   **平均退货率 (Return Rate)**：`6.02%`
  *   **平均毛利率 (Profit Margin)**：`53.05%`
  *   **品牌集中度 (Brand Concentration)**：`53.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`78.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Pet Supplies › Small Animals › Carriers  市场分析`
  *   **市场路径(中文)**：`宠物用品 › 小宠用品 › 外带用品`
  *   **A+数量占比**：`69%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 28.33`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`58`
  *   **新品月均销售额**：`$1,540`
  *   **平均重量**：`1.35 pounds (613 g)`
  *   **平均体积**：`780.77 in³ (12,795 cm³)`
  *   **平均毛利率**：`53.05%`
  *   **卖家所属地**：`中国|78.0%`
  *   **搜索购买比**：`5.6‰`

---

#### 🏆 🟢-58. French Bread & Baguette Pans (法式面包)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Bread & Loaf Pans › French Bread & Baguette Pans  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.35`
  *   **平均 Reviews (Avg Reviews)**：`321 个`
  *   **物理重量 (Weight)**：`1.37 lbs`
  *   **平均退货率 (Return Rate)**：`3.64%`
  *   **平均毛利率 (Profit Margin)**：`53.86%`
  *   **品牌集中度 (Brand Concentration)**：`62.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`76.8%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Bakeware › Bread & Loaf Pans › French Bread & Baguette Pans  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 烘焙用具 › 麵包 › 法式面包`
  *   **A+数量占比**：`59.6%`
  *   **新品平均评分数**：`9`
  *   **新品平均价格**：`$ 18.02`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`27`
  *   **新品月均销售额**：`$477`
  *   **平均重量**：`1.37 pounds (622 g)`
  *   **平均体积**：`554.29 in³ (9,083 cm³)`
  *   **平均毛利率**：`53.86%`
  *   **卖家所属地**：`中国|76.8%`
  *   **搜索购买比**：`13.0‰`

---

#### 🏆 🟢-59. Knitting Looms & Boards (编织机、织布机)

- **完整市场路径**：`Arts, Crafts & Sewing › Knitting & Crochet › Knitting Looms & Boards  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$29.44`
  *   **平均 Reviews (Avg Reviews)**：`386 个`
  *   **物理重量 (Weight)**：`1.81 lbs`
  *   **平均退货率 (Return Rate)**：`5.9%`
  *   **平均毛利率 (Profit Margin)**：`57.62%`
  *   **品牌集中度 (Brand Concentration)**：`49.9%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`83.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Knitting & Crochet › Knitting Looms & Boards  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 编织 › 编织机、织布机`
  *   **A+数量占比**：`75%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 32.37`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`107`
  *   **新品月均销售额**：`$3,250`
  *   **平均重量**：`1.81 pounds (822 g)`
  *   **平均体积**：`385.15 in³ (6,311 cm³)`
  *   **平均毛利率**：`57.62%`
  *   **卖家所属地**：`中国|83.0%`
  *   **搜索购买比**：`6.7‰`

---

#### 🏆 🟢-60. Wiring Harnesses (线束)

- **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Electrical & Batteries › Wiring Harnesses  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$30.28`
  *   **平均 Reviews (Avg Reviews)**：`142 个`
  *   **物理重量 (Weight)**：`1.34 lbs`
  *   **平均退货率 (Return Rate)**：`5.2%`
  *   **平均毛利率 (Profit Margin)**：`63.28%`
  *   **品牌集中度 (Brand Concentration)**：`58.1%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`82.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Automotive › Motorcycle & Powersports › Parts › Electrical & Batteries › Wiring Harnesses  市场分析`
  *   **市场路径(中文)**：`汽车 › 摩托车和动力运动 › 部分 › 电气 › 线束`
  *   **A+数量占比**：`61%`
  *   **新品平均评分数**：`7`
  *   **新品平均价格**：`$ 27.78`
  *   **新品平均星级**：`4.0`
  *   **新品月均销量**：`58`
  *   **新品月均销售额**：`$1,532`
  *   **平均重量**：`1.34 pounds (609 g)`
  *   **平均体积**：`144.75 in³ (2,372 cm³)`
  *   **平均毛利率**：`63.28%`
  *   **卖家所属地**：`中国|82.0%`
  *   **搜索购买比**：`6.8‰`

---

#### 🏆 🟢-61. Hunting Dog Equipment (猎犬装备)

- **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Hunting › Hunting Dog Equipment  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$32.34`
  *   **平均 Reviews (Avg Reviews)**：`284 个`
  *   **物理重量 (Weight)**：`0.99 lbs`
  *   **平均退货率 (Return Rate)**：`5.22%`
  *   **平均毛利率 (Profit Margin)**：`60.97%`
  *   **品牌集中度 (Brand Concentration)**：`57.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`43.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Sports & Outdoors › Hunting & Fishing › Hunting › Hunting Dog Equipment  市场分析`
  *   **市场路径(中文)**：`运动与户外 › 狩猎和钓鱼 › 惺惺相惜 › 猎犬装备`
  *   **A+数量占比**：`75%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 20.46`
  *   **新品平均星级**：`4.2`
  *   **新品月均销量**：`55`
  *   **新品月均销售额**：`$1,166`
  *   **平均重量**：`0.99 pounds (451 g)`
  *   **平均体积**：`598.69 in³ (9,811 cm³)`
  *   **平均毛利率**：`60.97%`
  *   **卖家所属地**：`美国|57.0%`
  *   **搜索购买比**：`7.4‰`

---

#### 🏆 🟢-62. UV Phone Sterilizer Boxes (紫外线手机消毒盒)

- **完整市场路径**：`Cell Phones & Accessories › Accessories › UV Phone Sterilizer Boxes  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$57.83`
  *   **平均 Reviews (Avg Reviews)**：`356 个`
  *   **物理重量 (Weight)**：`1.83 lbs`
  *   **平均退货率 (Return Rate)**：`7.51%`
  *   **平均毛利率 (Profit Margin)**：`72.68%`
  *   **品牌集中度 (Brand Concentration)**：`62.0%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`27.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Cell Phones & Accessories › Accessories › UV Phone Sterilizer Boxes  市场分析`
  *   **市场路径(中文)**：`手机 › 辅料 › 紫外线手机消毒盒`
  *   **A+数量占比**：`72%`
  *   **新品平均评分数**：`8`
  *   **新品平均价格**：`$ 54.17`
  *   **新品平均星级**：`4.1`
  *   **新品月均销量**：`33`
  *   **新品月均销售额**：`$1,744`
  *   **平均重量**：`1.83 pounds (831 g)`
  *   **平均体积**：`516.26 in³ (8,460 cm³)`
  *   **平均毛利率**：`72.68%`
  *   **卖家所属地**：`美国|73.0%`
  *   **搜索购买比**：`9.5‰`

---

#### 🏆 🟢-63. Surface Grinding Wheels (表面磨轮)

- **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Surface Grinding Wheels  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$33.05`
  *   **平均 Reviews (Avg Reviews)**：`161 个`
  *   **物理重量 (Weight)**：`1.13 lbs`
  *   **平均退货率 (Return Rate)**：`3.73%`
  *   **平均毛利率 (Profit Margin)**：`64.86%`
  *   **品牌集中度 (Brand Concentration)**：`59.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`56.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Industrial & Scientific › Abrasive & Finishing Products › Abrasive Wheels & Discs › Surface Grinding Wheels  市场分析`
  *   **市场路径(中文)**：`工业类 › 磨削加工 › 研磨砂轮 › 表面磨轮`
  *   **A+数量占比**：`70%`
  *   **新品平均评分数**：`13`
  *   **新品平均价格**：`$ 26.74`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`102`
  *   **新品月均销售额**：`$2,319`
  *   **平均重量**：`1.13 pounds (512 g)`
  *   **平均体积**：`16.04 in³ (263 cm³)`
  *   **平均毛利率**：`64.86%`
  *   **卖家所属地**：`中国|56.0%`
  *   **搜索购买比**：`16.2‰`

---

#### 🏆 🟢-64. Handles (手柄)

- **完整市场路径**：`Appliances › Parts & Accessories › Refrigerator Parts & Accessories › Handles  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$24.60`
  *   **平均 Reviews (Avg Reviews)**：`285 个`
  *   **物理重量 (Weight)**：`0.49 lbs`
  *   **平均退货率 (Return Rate)**：`7.11%`
  *   **平均毛利率 (Profit Margin)**：`58.18%`
  *   **品牌集中度 (Brand Concentration)**：`46.2%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`73.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Appliances › Parts & Accessories › Refrigerator Parts & Accessories › Handles  市场分析`
  *   **市场路径(中文)**：`家电 › 零件 › 冰箱配件 › 手柄`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`6`
  *   **新品平均价格**：`$ 36.69`
  *   **新品平均星级**：`4.5`
  *   **新品月均销量**：`78`
  *   **新品月均销售额**：`$2,594`
  *   **平均重量**：`0.49 pounds (223 g)`
  *   **平均体积**：`169.16 in³ (2,772 cm³)`
  *   **平均毛利率**：`58.18%`
  *   **卖家所属地**：`中国|73.0%`
  *   **搜索购买比**：`11.3‰`

---

#### 🏆 🟢-65. Paper Craft Tools (纸工艺工具)

- **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Paper & Paper Crafts › Paper Craft Tools  市场分析`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$36.65`
  *   **平均 Reviews (Avg Reviews)**：`283 个`
  *   **物理重量 (Weight)**：`1.55 lbs`
  *   **平均退货率 (Return Rate)**：`4.13%`
  *   **平均毛利率 (Profit Margin)**：`60.05%`
  *   **品牌集中度 (Brand Concentration)**：`58.7%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`57.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Arts, Crafts & Sewing › Crafting › Paper & Paper Crafts › Paper Craft Tools  市场分析`
  *   **市场路径(中文)**：`艺术、手工艺 › 工艺 › 报纸 › 纸工艺工具`
  *   **A+数量占比**：`62%`
  *   **新品平均评分数**：`19`
  *   **新品平均价格**：`$ 57.76`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`77`
  *   **新品月均销售额**：`$4,487`
  *   **平均重量**：`1.55 pounds (704 g)`
  *   **平均体积**：`170.64 in³ (2,796 cm³)`
  *   **平均毛利率**：`60.05%`
  *   **卖家所属地**：`中国|57.0%`
  *   **搜索购买比**：`9.2‰`

---

### 🟡 黄色类目详情列表

#### 🏆 🟡-1. Compressed Air Dusters (压缩除尘罐)

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

#### 🏆 🟡-2. Batteries & Battery Chargers (电池和电池)

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

#### 🏆 🟡-3. Decorative Trays (装饰性托盘)

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

#### 🏆 🟡-4. Cup Carriers (外卖杯托盘)

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

#### 🏆 🟡-5. Camping Fans (露营爱好者)

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

#### 🏆 🟡-6. Remote & App Controlled Vehicle Batteries (遥控)

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

#### 🏆 🟡-7. Boats (船)

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

#### 🏆 🟡-8. Accessories (辅料)

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

#### 🏆 🟡-9. Bag Sealers (封袋机)

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

#### 🏆 🟡-10. Spa Slippers (温泉拖鞋)

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

#### 🏆 🟡-11. Flower Pressing (压花)

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

#### 🏆 🟡-12. Trim & Repair Kits (修整和维修套件)

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

#### 🏆 🟡-13. Rods (杆)

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

#### 🏆 🟡-14. Airplanes & Jets (飞机)

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

#### 🏆 🟡-15. Cream Chargers & Whippers (奶油充电器)

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

#### 🏆 🟡-16. Metric Inserts & Kits (米制刀片和套件)

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

#### 🏆 🟡-17. Gaiters (护腿、护脚)

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

#### 🏆 🟡-18. Paint Roller Extension Poles (油漆滚筒加长杆)

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

#### 🏆 🟡-19. Game Table Accessories (游戏桌配件)

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

#### 🏆 🟡-20. Bats (蝙蝠)

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

#### 🏆 🟡-21. Bulb Planters (球茎栽植器)

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

#### 🏆 🟡-22. Battery Chargers (电池充电器)

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

#### 🏆 🟡-23. Kick Plates (踢脚板)

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

#### 🏆 🟡-24. Food Processor Parts & Accessories (食物处理器零件)

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

#### 🏆 🟡-25. Air Conditioning & Heater Control (空调与加热器控制)

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

#### 🏆 🟡-26. Armrest Lids (扶手盖)

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

#### 🏆 🟡-27. Breast Pump Carrying Bags (奶泵携带包)

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

#### 🏆 🟡-28. Doors (门)

- **完整市场路径**：`Appliances › Parts & Accessories › Washer Parts & Accessories › Doors  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$34.68`
  *   **平均 Reviews (Avg Reviews)**：`294 个`
  *   **物理重量 (Weight)**：`1.48 lbs`
  *   **平均退货率 (Return Rate)**：`9.72%`
  *   **平均毛利率 (Profit Margin)**：`64.27%`
  *   **品牌集中度 (Brand Concentration)**：`34.5%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Appliances › Parts & Accessories › Washer Parts & Accessories › Doors  市场分析`
  *   **市场路径(中文)**：`家电 › 零件 › 洗衣机部件 › 门`
  *   **A+数量占比**：`77%`
  *   **新品平均评分数**：`102`
  *   **新品平均价格**：`$ 30.21`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`103`
  *   **新品月均销售额**：`$2,720`
  *   **平均重量**：`1.48 pounds (671 g)`
  *   **平均体积**：`338.41 in³ (5,545 cm³)`
  *   **平均毛利率**：`64.27%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`17.2‰`

---

#### 🏆 🟡-29. Heating & Temperature Control (暖气)

- **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Home Brewing & Wine Making › Fermentation & More › Heating & Temperature Control  市场分析`
- **触发警示项**：`退货率偏高 (>8.0%)`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$25.19`
  *   **平均 Reviews (Avg Reviews)**：`128 个`
  *   **物理重量 (Weight)**：`1.09 lbs`
  *   **平均退货率 (Return Rate)**：`9.98%`
  *   **平均毛利率 (Profit Margin)**：`60.21%`
  *   **品牌集中度 (Brand Concentration)**：`59.3%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`75.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Home & Kitchen › Kitchen & Dining › Home Brewing & Wine Making › Fermentation & More › Heating & Temperature Control  市场分析`
  *   **市场路径(中文)**：`家居用品 › 厨房 › 家庭酿造 › 发酵 › 暖气`
  *   **A+数量占比**：`79%`
  *   **新品平均评分数**：`26`
  *   **新品平均价格**：`$ 27.8`
  *   **新品平均星级**：`4.3`
  *   **新品月均销量**：`61`
  *   **新品月均销售额**：`$1,988`
  *   **平均重量**：`1.09 pounds (493 g)`
  *   **平均体积**：`199.72 in³ (3,273 cm³)`
  *   **平均毛利率**：`60.21%`
  *   **卖家所属地**：`中国|75.0%`
  *   **搜索购买比**：`9.3‰`

---

#### 🏆 🟡-30. Dice Bags & Boxes (骰袋和骰盒)

- **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Dice & Accessories › Dice Bags & Boxes  市场分析`
- **触发警示项**：`谨慎认证类目路径`
- **核心数据特征**：
  *   **平均客单价 (Avg Price)**：`$22.05`
  *   **平均 Reviews (Avg Reviews)**：`440 个`
  *   **物理重量 (Weight)**：`0.70 lbs`
  *   **平均退货率 (Return Rate)**：`3.93%`
  *   **平均毛利率 (Profit Margin)**：`59.21%`
  *   **品牌集中度 (Brand Concentration)**：`42.8%`
  *   **中国卖家比例 (Chinese Seller Ratio)**：`63.0%`
- **Sellersprite 抓取原始细节 (Scraped Details)**：
  *   **完整市场路径**：`Toys & Games › Games & Accessories › Game Accessories › Dice & Accessories › Dice Bags & Boxes  市场分析`
  *   **市场路径(中文)**：`玩具与游戏 › 游戏和配件 › 游戏配件 › 骰子和配件 › 骰袋和骰盒`
  *   **A+数量占比**：`58%`
  *   **新品平均评分数**：`14`
  *   **新品平均价格**：`$ 16.34`
  *   **新品平均星级**：`4.4`
  *   **新品月均销量**：`103`
  *   **新品月均销售额**：`$1,539`
  *   **平均重量**：`0.70 pounds (319 g)`
  *   **平均体积**：`209.52 in³ (3,433 cm³)`
  *   **平均毛利率**：`59.21%`
  *   **卖家所属地**：`中国|63.0%`
  *   **搜索购买比**：`4.5‰`

---
