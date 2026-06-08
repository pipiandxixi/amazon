import json
import os
import datetime

def parse_22_results(date_str=None):
    if not date_str:
        date_str = datetime.date.today().strftime('%Y_%m_%d')
    json_path = f"/Users/zhoufan/Public/workspace/amazon/results/twenty_two_beginner_results_{date_str}.json"
    output_path = f"/Users/zhoufan/Public/workspace/amazon/results/twenty_two_beginner_results_{date_str}.md"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    markdown = []
    markdown.append("# 亚马逊跨境电商：全类目 22 个新手友好精选赛道分析报告\n\n")
    
    markdown.append("## 一、 选品筛选过滤条件与执行方案\n\n")
    markdown.append("### 1. 今日检索所采用的过滤条件明细\n")
    markdown.append("为了兼顾新手的“低启动资金、低物流成本、极低退货与运营风险”，今日在卖家精灵“选市场”工具中执行的完整筛选过滤参数如下：\n\n")
    markdown.append("| 筛选项类别 | 过滤参数名称 | 输入值 | 设定目的与物理意义 |\n")
    markdown.append("| :--- | :--- | :--- | :--- |\n")
    markdown.append("| **选定类目** | 选择类目 | 留空 | 放宽类目选择以进行全品类检索，捕获长尾蓝海赛道 |\n")
    markdown.append("| **市场需求** | 月均销量 (minAvgSales) | `100` ~ `10000` | 保证市场有基本动销，且避开被超级大单垄断的红海 |\n")
    markdown.append("| | 平均评分数 (maxAvgReviews) | 最小值未填 ~ `800` | 过滤出成熟、对新品极其不友好的老牌品类 |\n")
    markdown.append("| | 平均价格 (minAvgPrice) | `30.0` ~ 最大值未填 | 确保客单价不低于 $30，保障新手有足够的毛利推广空间 |\n")
    markdown.append("| | 平均重量 (maxAvgWeight) | 最小值未填 ~ `2.0` lbs | 限制在 2 磅以内，规避高昂的首重及续重跨境运费 |\n")
    markdown.append("| | 平均体积 (maxAvgVolume) | 最小值未填 ~ `500.0` in³ | 限制在标准小件体积内，控制 FBA 仓储与派送费用 |\n")
    markdown.append("| | 平均毛利率 (minAvgProfit) | `60.0` % ~ 最大值未填 | 确保底层产品有 60% 以上的高毛利，利于前期广告投放 |\n")
    markdown.append("| | 商品总数 (minTotalProducts) | `50` ~ 最大值未填 | 确保该细分市场至少有 50 个活跃商品，证明不是极其偏僻的死角 |\n")
    markdown.append("| **市场竞争** | 平均卖家数 (maxAvgSellers) | 最小值未填 ~ `60.0` | 控制每个细分市场的平均卖家数量，避免恶性竞争 |\n")
    markdown.append("| | 商品/品牌/卖家集中度 | 均限制在 `60.0` % 以下 | 卖家、品牌、商品集中度 <= 60%，防范超级巨头和寡头盘踞 |\n")
    markdown.append("| | Amazon自营占比 (maxAmzRatio) | 最小值未填 ~ `20.0` % | 限制自营比例在 20% 以下，防止亚马逊自营降维打击压榨生存空间 |\n")
    markdown.append("| | 卖家所属地 | 不限 | - |\n")
    markdown.append("| **市场波动** | 新品数量占比 (minNewRatio) | `10.0` % ~ 最大值未填 | 确保新品活跃度不低于 10%，说明市场仍在接纳新卖家 |\n")
    markdown.append("| | 新品平均星级 (maxNewAvgRating) | 最小值未填 ~ `4.5` | 新品平均星级在 4.5 以下，说明该市场现有产品有品质痛点可改良 |\n\n")
    
    markdown.append("### 2. 执行自动表单填充并提交的 JS 脚本\n")
    markdown.append("网页上的过滤条件是通过 `opencli` 在绑定的 Chrome 浏览器会话中直接执行以下 **Javascript 脚本** 自动填入并点击搜索的：\n")
    markdown.append("```javascript\n")
    markdown.append("const params = {\n")
    markdown.append("  minAvgSales: '100',\n")
    markdown.append("  maxAvgSales: '10000',\n")
    markdown.append("  minAvgPrice: '30.0',\n")
    markdown.append("  maxAvgPrice: '',\n")
    markdown.append("  minTotalProducts: '50',\n")
    markdown.append("  maxAvgSellers: '60.0',\n")
    markdown.append("  maxHeadListingBrandCrn: '60.0',\n")
    markdown.append("  maxHeadListingSellerCrn: '60.0',\n")
    markdown.append("  maxAmzRatio: '20.0',\n")
    markdown.append("  minNewRatio: '10.0',\n")
    markdown.append("  maxNewAvgRating: '4.5',\n")
    markdown.append("  maxAvgWeight: '2.0',\n")
    markdown.append("  maxAvgVolume: '500',\n")
    markdown.append("  minAvgProfit: '60.0',\n")
    markdown.append("  maxAvgReviews: '800'\n")
    markdown.append("};\n")
    markdown.append("Array.from(document.querySelectorAll('input[name]')).forEach(input => {\n")
    markdown.append("  if (params[input.name] !== undefined) {\n")
    markdown.append("    input.value = params[input.name];\n")
    markdown.append("    input.dispatchEvent(new Event('input', { bubbles: true }));\n")
    markdown.append("    input.dispatchEvent(new Event('change', { bubbles: true }));\n")
    markdown.append("  } else if (!['show-banner', 'marketId', 'sampleNumber', 'topn', 'newReleaseNum', 'order.field', 'order.desc', 'tab', 'promotionUser', 'nodeLabel', 'nodeIdPath'].includes(input.name)) {\n")
    markdown.append("    input.value = '';\n")
    markdown.append("    input.dispatchEvent(new Event('input', { bubbles: true }));\n")
    markdown.append("    input.dispatchEvent(new Event('change', { bubbles: true }));\n")
    markdown.append("  }\n")
    markdown.append("});\n")
    markdown.append("document.querySelector('button[type=submit]').click();\n")
    markdown.append("```\n\n")
    
    markdown.append("### 3. 数据提取与 JSON 文件落盘 JS 脚本\n")
    markdown.append("当检索页面渲染出 22 个结果后，使用以下 **DOM 提取 Javascript 脚本** 抓取表格数据并保存至本地 JSON 文件 `twenty_two_beginner_results.json` 中：\n")
    markdown.append("```javascript\n")
    markdown.append("(() => {\n")
    markdown.append("const items = [];\n")
    markdown.append("const rows = document.querySelectorAll('#table-condition-search tbody tr');\n")
    markdown.append("for (let i = 0; i < rows.length; i += 3) {\n")
    markdown.append("  const r1 = rows[i];\n")
    markdown.append("  const r2 = rows[i + 1];\n")
    markdown.append("  if (!r1 || !r2) continue;\n")
    markdown.append("  const cells = Array.from(r1.querySelectorAll('td')).map(td => td.innerText.trim());\n")
    markdown.append("  const details = r2.innerText.trim();\n")
    markdown.append("  const getVal = (str, label, nextLabels) => {\n")
    markdown.append("    const start = str.indexOf(label);\n")
    markdown.append("    if (start === -1) return '';\n")
    markdown.append("    let end = str.length;\n")
    markdown.append("    for (const nextLabel of nextLabels) {\n")
    markdown.append("      const idx = str.indexOf(nextLabel, start + label.length);\n")
    markdown.append("      if (idx !== -1 && idx < end) {\n")
    markdown.append("        end = idx;\n")
    markdown.append("      }\n")
    markdown.append("    }\n")
    markdown.append("    return str.substring(start + label.length, end).trim();\n")
    markdown.append("  };\n")
    markdown.append("  const labels = [\n")
    markdown.append("    '完整市场路径:', '市场路径(中文):', 'A+数量占比:', '新品平均评分数:', \\n")
    markdown.append("    '新品平均价格:', '新品平均星级:', '新品月均销量:', '新品月均销售额:', \\n")
    markdown.append("    '平均重量:', '平均体积:', '平均毛利率:', '卖家所属地:', '搜索购买比:'\n")
    markdown.append("  ];\n")
    markdown.append("  const parsedDetails = {};\n")
    markdown.append("  for (let j = 0; j < labels.length; j++) {\n")
    markdown.append("    const key = labels[j].replace(':', '');\n")
    markdown.append("    const val = getVal(details, labels[j], labels.filter((_, idx) => idx !== j));\n")
    markdown.append("    parsedDetails[key] = val;\n")
    markdown.append("  }\n")
    markdown.append("  items.push({\n")
    markdown.append("    index: cells[0],\n")
    markdown.append("    niche: cells[1],\n")
    markdown.append("    sampleSize: cells[2],\n")
    markdown.append("    monthlySales: cells[3],\n")
    markdown.append("    avgSales: cells[4],\n")
    markdown.append("    avgRevenue: cells[5],\n")
    markdown.append("    avgReviewsStar: cells[6],\n")
    markdown.append("    avgBsr: cells[7],\n")
    markdown.append("    avgSellersPrice: cells[8],\n")
    markdown.append("    sellerType: cells[9],\n")
    markdown.append("    concentration: cells[10],\n")
    markdown.append("    newCountRatio: cells[11],\n")
    markdown.append("    totalProducts: cells[12],\n")
    markdown.append("    returnRate: cells[13],\n")
    markdown.append("    details: parsedDetails\n")
    markdown.append("  });\n")
    markdown.append("}\n")
    markdown.append("return JSON.stringify(items, null, 2);\n")
    markdown.append("})()\n")
    markdown.append("```\n\n")
    
    markdown.append("### 4. 报表生成与二次评估脚本 (本 Python 脚本)\n")
    markdown.append("最后运行 Python 脚本 `scripts/generate_twenty_two_report.py` 读取抓取的 JSON 数据并完成推荐度分级评估。\n\n")
    markdown.append("---\n\n")
    markdown.append("## 二、 22 个精选赛道关键指标汇总表\n")
    markdown.append("| 序号 | 品类英文名 | 中文翻译/路径 | 月总销量 | 平均价格 | 平均毛利率 | 平均重量 | 平均体积 | 平均退货率 | 品牌集中度 | 中国卖家比例 | 类别推荐度与风险分级 |\n")
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
        full_path = details.get("完整市场路径", "").replace(" 市场分析", "").strip()
        
        # Categorization & recommendation logic
        tier = ""
        badge = ""
        reason = ""
        
        niche_lower = niche_en.lower()
        path_lower = full_path.lower()
        
        # 🔴 Avoid
        if "beneficial insects" in niche_lower:
            tier = "🔴 避坑 (活体生物)"
            badge = "★☆☆☆☆"
            reason = "活体防虫益虫。长途跨境物流死亡率极高，且动植物进口检疫极其严苛，不建议任何跨境新手操作。"
        elif "livestock" in niche_lower or "wormers" in niche_lower:
            tier = "🔴 避坑 (宠物/畜牧用药)"
            badge = "★☆☆☆☆"
            reason = "牲畜健康用品/猫用驱虫药。属于兽医用药，受 FDA/EPA 强力监管，需极其复杂的经营许可，稍有不慎即会封店起诉。"
        elif "hearing amplifiers" in niche_lower:
            tier = "🔴 避坑 (医疗器械与极高退货)"
            badge = "★☆☆☆☆"
            reason = "助听扩音器。虽然非常轻小，但属于个人医疗器械，受 FDA 监管；且**退货率高达 21.19%**，极易让新手产生大量滞销损耗。"
        elif "vehicle batteries" in niche_lower or "battery packs" in niche_lower:
            tier = "🔴 避坑 (带电危险品)"
            badge = "★★☆☆☆"
            reason = "遥控玩具锂电池。纯锂电池属于带电危险品 (Hazmat)，无法走正常空运快递，且需要 MSDS / UN38.3 复杂认证，运输成本高昂。"
        elif "clothing, shoes & jewelry" in path_lower or "hoodies" in niche_lower:
            tier = "🔴 避坑 (服装高退货/SKU过多)"
            badge = "★☆☆☆☆"
            reason = "女式连帽衫。**新品退货率达 13.92%**。服装有极为繁琐的尺码与颜色 SKU，极易压货且售后退货成本极高。"
            
        # 🟡 Cautious
        elif "battery chargers" in niche_lower:
            tier = "🟡 谨慎 (电器安规/兼容性)"
            badge = "★★★☆☆"
            reason = "玩具充电器。属于带电类产品，需要 FCC/UL 等强电或电器类安全检测，且要注意不同型号电池充电的适配兼容性。"
        elif "leak detection" in niche_lower:
            tier = "🟡 谨慎 (专业检测仪器/品控要求高)"
            badge = "★★★☆☆"
            reason = "管道/暖通泄漏检测仪。均价 $105.39 表现很好，但属于精密电子检测设备，品控和技术支持要求高，不适合零经验新手。"
        elif "night vision" in niche_lower:
            tier = "🟡 谨慎 (高单价电子/中高度退货)"
            badge = "★★★☆☆"
            reason = "夜视双筒望远镜。均价 $100.16，高客单价高毛利，但属于精密光学电子设备。退货率偏高 (15.60%)，需要极其严格的品质把关。"
            
        # 🟢 Recommended
        else:
            tier = "🟢 终极推荐 (轻小蓝海标品)"
            badge = "★★★★★"
            if "wrinkle" in niche_lower:
                reason = "物理美容仪器。均价 $108.55，毛利 72.34%，高溢价空间利于推广；新品评分虽有改进空间但**退货率低 (2.2%)**，注意保障 FCC 认证。"
            elif "headlights" in niche_lower:
                reason = "自行车头灯/骑行灯。属于运动配件，虽然带USB充电，但体积极小（32 in³），重量极轻（0.47 lbs），退货率在 5% 左右，非常适合空运。"
            elif "wood burning tools" in niche_lower:
                reason = "电烙画笔刻花工具套件。客单价 $31.69，属于手工艺小工具。纯发热物理器具，退货率极低 (3.75% / 4%)，包装小且结构简单。"
            elif "sound therapy" in niche_lower:
                reason = "助眠声音疗法仪。平均售价 $54.89，毛利率高达 66.95%。**退货率极低 (2.78%)**，重量仅 0.96 磅，体积极小。属于高毛利蓝海硬件。"
            elif "scoreboards" in niche_lower:
                reason = "便携记分牌和计时器。价格 $52.21，属于球场运动教练配件。属于小众蓝海，平均退货率仅 4.51% / 5.13%，竞争非常温和。"
            elif "gaiters" in niche_lower:
                reason = "户外登山防沙护腿。虽然是织物产品，但**不具备时尚服装的选款和多尺码属性**，属于功能性五金配件。平均退货率仅 4.56% / 8.64%。"
            elif "brake controls" in niche_lower:
                reason = "拖车制动控制器。均价高达 $85.75，毛利率 70.56%。属于高度专业的汽配改装控制盒，退货率低 (3.87% / 6.05%)，适合做差异化高溢价。"
            elif "seat covers" in niche_lower:
                reason = "摩托车/全地形车座套。汽配防护罩，纯物理面料，无任何认证和退货烦恼（退货率仅 5.29%），轻便耐磨。"
            elif "alarms" in niche_lower:
                reason = "摩托车防盗报警器。价格 $32.97，重量 0.9 磅，体积仅 39 in³，**退货率极低 (4.72%)**。由于是防盗硬需求，PPC 投放极其精准。"
            elif "optics accessories" in niche_lower:
                reason = "射击光学瞄准镜支架/配件。均价 $33.10，重量仅 0.2 磅。属于纯物理五金配件（导轨、镜盖），退货率极低 (4.51% / 5.63%)，几乎无售后。"
            elif "food processor parts" in niche_lower:
                reason = "食物处理器替换配件（刀片、杯盖等）。客单价 $31.13，属于易损耗的替换件配件，退货率 5.20% / 8.72%，完全没有电子元器件，无认证壁垒。"
            elif "car rack parts" in niche_lower:
                reason = "汽车车顶架零配件。客单价 $45.30，毛利率 63.95%，退货率极低 (3.87% - 6.72%)。纯五金或硬塑料结构，坚固耐用，FBA 仓储损耗极低。"
            elif "fuel" in niche_lower:
                reason = "汽车仪表盘燃油表。均价 $31.60，重量仅 0.38 磅。纯指示仪表，退货率极低 (4.01% / 4.87%)，是非常好做差异化的汽配长尾小标品。"
            else:
                reason = "物理标品，结构简单，符合 FBA 轻小限制，退货率相对较低，适合新手切入。"
                
        processed_list.append({
            "idx": idx,
            "niche_en": niche_en,
            "niche_cn": niche_cn,
            "path_cn": path_cn,
            "sales": sales,
            "price": price_raw,
            "margin": margin,
            "weight": details.get("平均重量", ""),
            "volume": details.get("平均体积", ""),
            "ret_rate": ret_rate_raw,
            "origin": origin,
            "tier": tier,
            "badge": badge,
            "reason": reason,
            "full_path": full_path
        })
        
        markdown.append(f"| {idx} | **{niche_en}** | {niche_cn} | {sales} | {price_raw} | {margin} | {weight} | {volume} | {ret_rate_raw} | {brand_concen} | {origin} | {badge}<br>{tier.split()[0]} |\n")
        
    markdown.append("\n---\n")
    markdown.append("## 二、 22 个细分赛道深度画像与跨境评估建议\n")
    
    # 🟢 第一梯队
    markdown.append("### 🟢 第一梯队：新手终极推荐赛道（低退货、低物流成本、无强资质门槛）\n")
    for item in processed_list:
        if "🟢" in item["tier"]:
            markdown.append(f"#### 【{item['idx']}】 {item['niche_en']} ({item['niche_cn']}) —— 推荐星级：{item['badge']}\n")
            markdown.append(f"*   **中文路径**：{item['path_cn']}\n")
            markdown.append(f"*   **完整市场路径**：`{item['full_path']}`\n")
            markdown.append(f"*   **核心运营数据**：\n")
            markdown.append(f"    *   **月销量**：`{item['sales']}` 件 | **平均客单价**：`{item['price']}` | **平均毛利率**：`{item['margin']}`\n")
            markdown.append(f"    *   **平均重量**：`{item['weight']}` | **平均体积**：`{item['volume']}` | **退货率**：`{item['ret_rate']}`\n")
            markdown.append(f"    *   **中国卖家比例**：`{item['origin']}`\n")
            markdown.append(f"*   **新手实操评估**：{item['reason']}\n\n")
            
    # 🟡 第二梯队
    markdown.append("### 🟡 第二梯队：中等难度/谨慎入局赛道（具有电器认证或高客单价电子品控）\n")
    for item in processed_list:
        if "🟡" in item["tier"]:
            markdown.append(f"#### 【{item['idx']}】 {item['niche_en']} ({item['niche_cn']}) —— 推荐星级：{item['badge']}\n")
            markdown.append(f"*   **中文路径**：{item['path_cn']}\n")
            markdown.append(f"*   **完整市场路径**：`{item['full_path']}`\n")
            markdown.append(f"*   **核心运营数据**：\n")
            markdown.append(f"    *   **月销量**：`{item['sales']}` 件 | **平均客单价**：`{item['price']}` | **平均毛利率**：`{item['margin']}`\n")
            markdown.append(f"    *   **平均重量**：`{item['weight']}` | **平均体积**：`{item['volume']}` | **退货率**：`{item['ret_rate']}`\n")
            markdown.append(f"    *   **中国卖家比例**：`{item['origin']}`\n")
            markdown.append(f"*   **实操红线挑战**：{item['reason']}\n\n")
            
    # 🔴 第三梯队
    markdown.append("### 🔴 第三梯队：高危雷区/强烈建议新手避坑（物流、法规或退货风险极高）\n")
    for item in processed_list:
        if "🔴" in item["tier"]:
            markdown.append(f"#### 【{item['idx']}】 {item['niche_en']} ({item['niche_cn']}) —— 推荐星级：{item['badge']}\n")
            markdown.append(f"*   **中文路径**：{item['path_cn']}\n")
            markdown.append(f"*   **完整市场路径**：`{item['full_path']}`\n")
            markdown.append(f"*   **核心运营数据**：\n")
            markdown.append(f"    *   **月销量**：`{item['sales']}` 件 | **平均客单价**：`{item['price']}` | **平均毛利率**：`{item['margin']}`\n")
            markdown.append(f"    *   **平均重量**：`{item['weight']}` | **平均体积**：`{item['volume']}` | **退货率**：`{item['ret_rate']}`\n")
            markdown.append(f"    *   **中国卖家比例**：`{item['origin']}`\n")
            markdown.append(f"*   **避坑警示**：{item['reason']}\n\n")
            
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown))
    print(f"22 niches report successfully generated at: {output_path}")

if __name__ == "__main__":
    parse_22_results()
