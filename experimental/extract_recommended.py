import json
import os

def generate_all_niches_report():
    json_path = "/Users/zhoufan/Public/workspace/amazon/shipping_restricted_results.json"
    output_path = "/Users/zhoufan/Public/workspace/amazon/recommended_niches_metrics.md"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Process all 30 niches
    markdown = []
    markdown.append("# 亚马逊跨境电商：全类目轻小件（物流/仓储限制）新手友好筛选结果汇总报告\n")
    markdown.append("本报告汇总了在卖家精灵【选市场】工具中进行**全球/全类目检索**，且**完全符合以下全部过滤条件**的 **30 个细分市场**及其关键指标数据：\n")
    
    markdown.append("### 1. 检索条件汇总\n")
    markdown.append("*   **物流硬限制**：平均重量 $\le 2.0$ 磅（约 900克），且平均体积 $\le 500$ 立方英寸。\n")
    markdown.append("*   **新手运营指标**：月销量 `100` ~ `10000` 件，平均价格 $\ge \\$30$，商品数 $\ge 50$，平均卖家数 $\le 60$，品牌集中度 $\le 60\\%$，卖家集中度 $\le 60\\%$，亚马逊自营占比 $\le 30\\%$，新品占比 $\ge 8\\%$，新品平均星级 $\le 4.5$ 星。\n")
    
    markdown.append("---\n")
    markdown.append("## 一、 全 30 个符合条件细分市场关键数据汇总表\n")
    markdown.append("| 序号 | 英文品类名 | 中文品类名 | 月销量 | 平均价格 | 平均毛利率 | 平均重量 | 平均体积 | 平均退货率 | 品牌集中度 | 中国卖家比例 | 类别推荐度与风险分级 |\n")
    markdown.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    
    processed_list = []
    
    for item in data:
        idx = item["index"]
        niche_raw = item["niche"].replace("\n", " ")
        niche_en = niche_raw
        niche_cn = ""
        if "(" in niche_raw:
            parts = niche_raw.split("(")
            niche_en = parts[0].strip()
            niche_cn = parts[1].replace(")", "").strip()
            
        sales = item["monthlySales"]
        price_raw = item["avgSellersPrice"].split("\n")[-1]
        ret_rate_raw = item["returnRate"].replace("\n", " / ")
        
        concen = item["concentration"].split("\n")
        brand_concen = ""
        for c in concen:
            if "品牌" in c:
                brand_concen = c.split(":")[-1].strip()
                
        details = item["details"]
        path_cn = details.get("市场路径(中文)", "").replace("市场分析", "").strip()
        weight = details.get("平均重量", "").split("(")[0].strip()
        volume = details.get("平均体积", "").split("(")[0].strip()
        margin = details.get("平均毛利率", "")
        origin = details.get("卖家所属地", "")
        
        # Categorize
        path_lower = details.get("完整市场路径", "").lower()
        niche_lower = niche_en.lower()
        
        tier = ""
        badge = ""
        reason = ""
        
        if "diet & sports nutrition" in path_lower or "testosterone boosters" in niche_lower or "appetite" in niche_lower or "alternative medicine" in niche_lower:
            tier = "🔴 避坑 (口服/FDA监管)"
            badge = "★☆☆☆☆"
            reason = "属于膳食补充剂或口服药物。亚马逊类目审核极严，需 FDA 证书及第三方检测报告，新手极难通过，且容易面临安全赔偿责任。"
        elif "beneficial insects" in niche_lower or "live" in niche_lower:
            tier = "🔴 避坑 (活体生物)"
            badge = "★☆☆☆☆"
            reason = "活体昆虫，物流运输死亡率极高，且动植物进口检验监管极严，跨境卖家无法操作。"
        elif "battery packs" in niche_lower or "battery chargers" in niche_lower or "vehicle batteries" in niche_lower:
            tier = "🔴 避坑 (带电危险品)"
            badge = "★★☆☆☆"
            reason = "纯锂电池或带强电产品，属于带电危险品 (Hazmat)，空运受限且需要 MSDS / UN38.3 复杂认证，头程运费高。"
        elif "clothing, shoes & jewelry" in path_lower:
            if "handbags" in path_lower or "clutches" in niche_lower or "bags" in niche_lower:
                tier = "🟡 谨慎 (中度退货/时尚)"
                badge = "★★★☆☆"
                reason = "箱包品类。退货率（约 13-16%）比普通衣服稍低，无尺码纠纷，但款式流行快，对选品审美和供应链反应速度有要求。"
            else:
                tier = "🔴 避坑 (服装高退货率)"
                badge = "★☆☆☆☆"
                reason = "服装类产品（连衣裙、马甲、夹克等）。退货率极高 (15% - 31%)，且尺码和颜色变体极多，极易造成库存积压。"
        elif "electronics" in path_lower or "electric massagers" in path_lower or "gps" in niche_lower or "detectors" in niche_lower:
            if "headlights" in niche_lower:
                tier = "🟢 终极推荐 (轻小运动配件)"
                badge = "★★★★★"
                reason = "自行车头灯/骑行灯。虽带USB充电但体积极小（32 in³），重量极轻（0.47 lbs），退货率在 5% 左右，非常适合空运。"
            else:
                tier = "🟡 谨慎 (电子电器认证)"
                badge = "★★★☆☆"
                reason = "电子安防/探测仪器或按摩器。需 FCC/UL 认证，退货率中等（6-10%），品控要求高，售后技术支持可能占用新手精力。"
        elif "health & household" in path_lower and ("massage" in path_lower or "bladder" in niche_lower or "acoustics" in niche_lower):
            if "bladder" in niche_lower:
                tier = "🟡 谨慎 (个人医疗器械)"
                badge = "★★★☆☆"
                reason = "膀胱控制/失禁仪。可能涉及医疗器械等级划定，需要 FDA 注册资质，新手准入门槛较高。"
            else:
                tier = "🟡 谨慎 (个护健康设备)"
                badge = "★★★☆☆"
                reason = "个人护理仪器，涉及人体接触及 FCC 等基本电子电器认证。"
        else:
            tier = "🟢 终极推荐 (轻小物理标品)"
            badge = "★★★★★"
            if "preserved flowers" in niche_lower:
                reason = "永生花/保鲜花。礼品属性，退货率极低 (仅 2.75%)。毛利率高达 63.76%，非常适合精细化 Listing 运营。"
            elif "grill brushes" in niche_lower:
                reason = "烤炉清洁刷。结构简单无电子元器件，重量仅 0.94 lbs。退货率极低 (仅 2.25%)，新品占比高达 25%，市场接受度极好。"
            elif "fuel pumps" in niche_lower:
                reason = "手动燃油泵。汽配工具，纯机械结构无复杂认证，重量 1.58 lbs。退货率低 (4.23%)，竞争相对温和。"
            elif "electrical system tools" in niche_lower:
                reason = "汽车电气检测工具。客单价 $31+，重量仅 0.99 lbs，退货率仅 2.38%。属于低退货、重专业壁垒的优质标品。"
            else:
                reason = "结构简单，重量体积符合 FBA 轻小限制，退货率相对较低，适合新手切入。"
                
        processed_list.append({
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
            "reason": reason,
            "full_path": details.get("完整市场路径", "").replace(" 市场分析", "").strip()
        })
        
        markdown.append(f"| {idx} | **{niche_en}** | {niche_cn} | {sales} | {price_raw} | {margin} | {weight} | {volume} | {ret_rate_raw} | {brand_concen} | {origin} | {badge}<br>{tier.split()[0]} |\n")
        
    markdown.append("\n---\n")
    markdown.append("## 二、 30个细分市场全部关键指标与风险画像 (详细数据)\n")
    
    for item in processed_list:
        markdown.append(f"### 【{item['idx']}】 {item['niche_en']} ({item['niche_cn']}) —— 推荐等级：{item['badge']}\n")
        markdown.append(f"*   **中文路径**：{item['path_cn']}\n")
        markdown.append(f"*   **完整市场路径**：`{item['full_path']}`\n")
        markdown.append(f"*   **核心运营指标**：\n")
        markdown.append(f"    *   **月销量**：`{item['sales']}` 件 | **平均客单价**：`{item['price']}` | **平均毛利率**：`{item['margin']}`\n")
        markdown.append(f"    *   **平均重量**：`{item['weight']}` | **平均体积**：`{item['volume']}` | **退货率**：`{item['ret_rate']}`\n")
        markdown.append(f"    *   **中国卖家比例**：`{item['origin']}`\n")
        markdown.append(f"*   **分级建议**：**{item['tier']}**\n")
        markdown.append(f"*   **实操与评估依据**：{item['reason']}\n\n")
        
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown))
    print(f"All 30 niches report successfully generated at: {output_path}")

if __name__ == "__main__":
    generate_all_niches_report()
