import json
import os

def parse_results():
    json_path = "/Users/zhoufan/Public/workspace/amazon/shipping_restricted_results.json"
    output_path = "/Users/zhoufan/Public/workspace/amazon/shipping_restricted_beginner_results.md"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Categories classification & recommendation logic
    # Tiers:
    # 🟢 终极推荐 (Low return rate, simple structure, light & small, no batteries/hazmat/ingestibles)
    # 🟡 谨慎入局 (Electronics, Bags, Beauty devices - require moderate certifications or have moderate return rates)
    # 🔴 极高风险 / 避坑 (Apparel due to high returns/SKU variations, Ingestibles due to FDA, Hazmat batteries, Live insects)
    
    # We will write the markdown report
    markdown = []
    markdown.append("# 亚马逊跨境电商：轻小件与低物流成本（FBA/仓储限制）新手友好赛道筛选报告\n")
    markdown.append("本报告是针对跨境电商卖家（特别是从中国发货、使用亚马逊 FBA 模式的新手）定制的选市场报告。")
    markdown.append("在之前新手黄金指标的基础上，我们加入了严格的**物流与仓储成本限制**（重量 $\le 2.0$ lbs，体积 $\le 500$ in³），以确保商品符合亚马逊的“标准尺寸件”（Standard-size），最大程度降低国际头程运费、仓储费和 FBA 配送费。\n")
    
    markdown.append("---\n")
    markdown.append("## 一、 核心筛选指标与物流费用逻辑\n")
    
    markdown.append("### 1. 过滤指标汇总\n")
    markdown.append("*   **物流硬限制**：\n")
    markdown.append("    *   **平均重量** $\le 2.0$ 磅（约 900g），降低头程空运/海运费。\n")
    markdown.append("    *   **平均体积** $\le 500$ 立方英寸（约 8.2 升，对应尺寸远小于标准箱 18\"x 14\"x 8\"），降低 FBA 仓储费（Storage Fees）和配送费（Fulfillment Fees）。\n")
    markdown.append("*   **新手运营指标**：\n")
    markdown.append("    *   **月销量**：`100` ~ `10000` 件\n")
    markdown.append("    *   **平均价格** $\ge \\$30.0$（高客单价，保障广告利润空间）\n")
    markdown.append("    *   **商品数** $\ge 50$ 个\n")
    markdown.append("    *   **平均卖家数** $\le 60$ 个\n")
    markdown.append("    *   **品牌集中度** $\le 60.0%$ 且 **卖家集中度** $\le 60.0%$\n")
    markdown.append("    *   **亚马逊自营占比** $\le 30.0%$\n")
    markdown.append("    *   **新品数量占比** $\ge 8.0%$ 且 **新品平均星级** $\le 4.5$ 星\n")
    
    markdown.append("### 2. 物流与仓储费用优势分析\n")
    markdown.append("根据亚马逊当前的收费标准，重量在 2 lbs 以下且体积在 500 in³ 以下的商品具有极高的物流优势：\n")
    markdown.append("*   **FBA 配送费（Fulfillment Fee）**：通常属于 **小标准件（Small Standard）** 或 **大标准件低权重档（Large Standard - under 2 lbs）**，单件配送费通常在 $\\$3.50$ ~ $\\$6.00$ 之间，远低于大重件（$\\$10$ 以上）。\n")
    markdown.append("*   **月度仓储费（Monthly Storage Fee）**：$500$ in³ 约为 $0.29$ 立方英尺。在淡季（1-9月），每件商品的月度仓储费仅约 $\\$0.23$；即使在旺季（10-12月），单件仓储费也仅约 $\\$0.69$。这能极大减轻新手备货的资金流压力。\n")
    markdown.append("*   **退货损耗控制**：由于退货时卖家仍需支付退货处理费，低退货率的产品能省下巨额的二次上架与销毁费用。\n")
    
    markdown.append("---\n")
    markdown.append("## 二、 筛选结果汇总表 (30个细分市场)\n")
    markdown.append("| 序号 | 细分市场名称 | 完整中文路径 | 月销量 | 平均价格 | 平均毛利率 | 平均重量 | 平均体积 | 退货率 | 卖家分布 | 推荐指数 |\n")
    markdown.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    
    # Process each niche
    classified_data = []
    
    for item in data:
        idx = item["index"]
        niche_raw = item["niche"].replace("\n", " ")
        niche_cn = ""
        niche_en = niche_raw
        if "(" in niche_raw:
            parts = niche_raw.split("(")
            niche_en = parts[0].strip()
            niche_cn = parts[1].replace(")", "").strip()
            
        sales = item["monthlySales"]
        
        # Parse Price
        price_raw = item["avgSellersPrice"].split("\n")[-1]
        
        # Parse return rate
        ret_rate_raw = item["returnRate"].replace("\n", " / ")
        
        # Details
        details = item["details"]
        path_cn = details.get("市场路径(中文)", "").replace("市场分析", "").strip()
        weight = details.get("平均重量", "")
        volume = details.get("平均体积", "")
        margin = details.get("平均毛利率", "")
        origin = details.get("卖家所属地", "")
        
        # Classify and determine recommendation tier
        # Let's write rules based on keywords or path
        path_lower = details.get("完整市场路径", "").lower()
        niche_lower = niche_en.lower()
        
        reason = ""
        tier = ""
        badge = ""
        
        # 1. Ingestibles (supplements) -> High risk FDA
        if "diet & sports nutrition" in path_lower or "testosterone boosters" in niche_lower or "appetite" in niche_lower or "alternative medicine" in niche_lower:
            tier = "🔴 避坑 (资质壁垒)"
            badge = "★☆☆☆☆"
            reason = "属于膳食补充剂或口服药物。亚马逊类目审核极严，需 FDA 认证与第三方检测报告，且安全责任风险高，极不建议新手触碰。"
        # 2. Live animals / perishables
        elif "beneficial insects" in niche_lower or "live" in niche_lower:
            tier = "🔴 避坑 (活体/易腐)"
            badge = "★☆☆☆☆"
            reason = "活体昆虫，物流运输极其复杂，死亡率高，无法通过跨境头程进行常规售卖。"
        # 3. Batteries / pure hazmat
        elif "battery packs" in niche_lower or "battery chargers" in niche_lower or "vehicle batteries" in niche_lower:
            tier = "🔴 避坑 (电池危险品)"
            badge = "★★☆☆☆"
            reason = "纯锂电池或带强电产品，属于带电危险品 (Hazmat)，空运和海运限制极多，需要 UN38.3、MSDS 等复杂认证，物流成本高且容易被扣关。"
        # 4. Apparel
        elif "clothing, shoes & jewelry" in path_lower:
            # Check if handbag
            if "handbags" in path_lower or "clutches" in niche_lower or "bags" in niche_lower:
                tier = "🟡 谨慎 (中度退货)"
                badge = "★★★☆☆"
                reason = "箱包类产品。相比普通服装退货率稍低 (约 13-16%)，且无尺码问题，但设计款式更新快，需具备一定的选款审美。"
            else:
                tier = "🔴 避坑 (服装高退货)"
                badge = "★☆☆☆☆"
                reason = "服装类产品（连衣裙、马甲、夹克、童装）。退货率极高 (普遍在 15% - 31% 之间)，且尺码和颜色 SKU 极多，极易造成资金积压和库存滞销。"
        # 5. Electronics
        elif "electronics" in path_lower or "electric massagers" in path_lower or "gps" in niche_lower or "detectors" in niche_lower:
            tier = "🟡 谨慎 (电子认证)"
            badge = "★★★☆☆"
            reason = "电子仪器或探测设备。需要 FCC/UL 等电子电器认证，且售后退货率（约 6-10%）较普通硬件高，电子件故障率需要严格品控。"
        # 6. Medical/health tools
        elif "health & household" in path_lower and ("massage" in path_lower or "bladder" in niche_lower or "acoustics" in niche_lower):
            if "bladder" in niche_lower:
                tier = "🟡 谨慎 (医疗资质)"
                badge = "★★★☆☆"
                reason = "失禁/膀胱控制仪器。可能涉及 Class I/II 医疗器械等级划定，需要 FDA 注册登记，新手资质审核门槛较高。"
            elif "massager" in niche_lower:
                tier = "🟡 谨慎 (电子/按摩器)"
                badge = "★★★☆☆"
                reason = "手持按摩器。属于带电按摩设备，退货率在 7% 左右，需要 FCC 等基本电子电器认证。"
            else:
                tier = "🟡 谨慎 (个人护理)"
                badge = "★★★☆☆"
                reason = "个护健康产品，注意资质监管和售后使用反馈。"
        # 7. Tools, Outdoor, Lawn & Garden (Simple physical items)
        else:
            tier = "🟢 终极推荐 (轻小标品)"
            badge = "★★★★★"
            if "preserved flowers" in niche_lower:
                reason = "保鲜花/永生花。礼品属性，退货率极低 (仅 2.75%)。毛利率高达 63.76%，客单价 $34+。重量 1.08 lbs。非常适合视觉精细化运营。"
            elif "grill brushes" in niche_lower:
                reason = "烤炉清洁刷。结构简单（无电子元器件），重量仅 0.94 lbs。退货率极低 (仅 2.25%)，新品占比高达 25%，市场接受度极好。"
            elif "fuel pumps" in niche_lower:
                reason = "手动燃油泵。汽配工具，纯机械结构，无复杂认证。重量 1.58 lbs。退货率低 (4.23%)，竞争相对温和。"
            elif "electrical system tools" in niche_lower:
                reason = "汽车电气检测工具。客单价 $31+，重量仅 0.99 lbs，退货率仅 2.38%。属于低退货、重专业壁垒的优质标品。"
            elif "headlights" in niche_lower:
                reason = "自行车头灯/骑行灯。属于运动配件，虽然带USB充电，但体积极小（32 in³），重量极轻（0.47 lbs），退货率在 5% 左右，属于轻小件爆款。"
            else:
                reason = "物理标品，结构简单，重量体积符合 FBA 轻小限制，退货率相对较低，适合新手切入。"
                
        classified_data.append({
            "idx": idx,
            "niche_en": niche_en,
            "niche_cn": niche_cn,
            "path_cn": path_cn,
            "sales": sales,
            "price": price_raw,
            "margin": margin,
            "weight": weight,
            "volume": volume,
            "ret_rate": ret_rate_raw,
            "origin": origin,
            "tier": tier,
            "badge": badge,
            "reason": reason
        })
        
        # Append to table
        markdown.append(f"| {idx} | **{niche_en}**<br>({niche_cn}) | {path_cn} | {sales} | {price_raw} | {margin} | {weight.split('(')[0].strip()} | {volume.split('(')[0].strip()} | {ret_rate_raw} | {origin} | {badge}<br>{tier.split()[0]} |\n")
        
    markdown.append("\n---\n")
    markdown.append("## 三、 细分赛道分级剖析与运营建议\n")
    
    # 🟢 终极推荐
    markdown.append("### 🟢 第一梯队：新手终极推荐（五星赛道，利润高、退货极低、运费极省）\n")
    for item in classified_data:
        if "🟢" in item["tier"]:
            markdown.append(f"#### {item['idx']}. {item['niche_en']} ({item['niche_cn']})\n")
            markdown.append(f"*   **核心数据**：月销量 `{item['sales']}` 件 | 平均客单价 `{item['price']}` | 平均毛利率 `{item['margin']}` | 退货率 `{item['ret_rate']}`\n")
            markdown.append(f"*   **物流优势**：平均重量 `{item['weight']}` | 平均体积 `{item['volume']}`。属于超轻标准件，FBA 单件配送费预估为 $\\$4$ 左右，仓储费每月低于 $\\$0.1$。\n")
            markdown.append(f"*   **新手避坑建议**：{item['reason']}\n")
            
    # 🟡 谨慎入局
    markdown.append("\n### 🟡 第二梯队：中等难度/谨慎入局（三星赛道，具有认证门槛或中度退货率）\n")
    for item in classified_data:
        if "🟡" in item["tier"]:
            markdown.append(f"#### {item['idx']}. {item['niche_en']} ({item['niche_cn']})\n")
            markdown.append(f"*   **核心数据**：月销量 `{item['sales']}` 件 | 平均客单价 `{item['price']}` | 平均毛利率 `{item['margin']}` | 退货率 `{item['ret_rate']}`\n")
            markdown.append(f"*   **物流优势**：平均重量 `{item['weight']}` | 平均体积 `{item['volume']}`\n")
            markdown.append(f"*   **核心挑战与红线**：{item['reason']}\n")
            
    # 🔴 避坑
    markdown.append("\n### 🔴 第三梯队：高危深坑/强烈建议新手避开（一星/二星赛道，资金占用或审核风险极高）\n")
    for item in classified_data:
        if "🔴" in item["tier"]:
            markdown.append(f"#### {item['idx']}. {item['niche_en']} ({item['niche_cn']})\n")
            markdown.append(f"*   **核心数据**：月销量 `{item['sales']}` 件 | 平均客单价 `{item['price']}` | 退货率 `{item['ret_rate']}`\n")
            markdown.append(f"*   **物流优势**：平均重量 `{item['weight']}` | 平均体积 `{item['volume']}`\n")
            markdown.append(f"*   **红线警告**：{item['reason']}\n")
            
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown))
    print(f"Report successfully generated at: {output_path}")

if __name__ == "__main__":
    parse_results()
