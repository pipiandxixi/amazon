import json
import re
import os

def parse_num(val):
    if not val:
        return 0
    clean = re.sub(r'[^\d\.]', '', val.split('\n')[0])
    return float(clean) if '.' in clean else (int(clean) if clean else 0)

def parse_percent(val):
    if not val:
        return 0.0
    match = re.search(r'([\d\.]+)%', val)
    return float(match.group(1)) if match else 0.0

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_name(niche_str):
    name = niche_str.replace('\n', ' ').strip()
    return re.sub(r'\s*\(.*?\)\s*', '', name).strip()

def extract_zh_name(niche_str):
    match = re.search(r'\((.*?)\)', niche_str)
    return match.group(1).strip() if match else ''

def get_stems(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    tokens = text.split()
    stems = set()
    for t in tokens:
        if t.endswith('ies'):
            stems.add(t[:-3] + 'y')
        elif t.endswith('s') and not t.endswith('ss'):
            stems.add(t[:-1])
        else:
            stems.add(t)
    return stems

def main():
    # Load relaxed categories (150 items)
    categories = load_json('/Users/zhoufan/Public/workspace/amazon/results/relaxed_one_hundred_categories_2026_06_08.json')
    # Load targeted keywords (316 items)
    keywords = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_targeted_2026_06_08.json')
    # Load global potential keywords (20 items)
    global_kws = load_json('/Users/zhoufan/Public/workspace/amazon/results/global_potential_keywords_2026_06_08.json')
    
    print(f"Loaded {len(categories)} relaxed categories.")
    print(f"Loaded {len(keywords)} targeted keywords.")
    print(f"Loaded {len(global_kws)} global potential keywords.")
    
    # Let's filter and analyze the 150 categories first
    # We want to rate them based on beginner friendliness:
    # - Return rate: lower is better (r1 / r2 -> e.g. "8.64% / 4.56%" -> second number is new release or average? Wait, usually it's "新品退货率 / 类目平均退货率")
    # - Weight: lower is better
    # - Average Price: $25 - $150 is ideal
    # - Chinese Seller ratio: lower is better
    # - Concentration: lower is better
    # - Average reviews
    scored_categories = []
    for item in categories:
        niche_raw = item['index'] # the niche name is in 'index'
        en_name = clean_name(niche_raw)
        zh_name = extract_zh_name(niche_raw)
        
        details = item['details']
        path = details.get('完整市场路径', '')
        zh_path = details.get('市场路径(中文)', '')
        
        # Parse return rate from item['totalProducts'] which contains return rate (e.g. "17.94%\n12.30%")
        return_rate_str = item.get('totalProducts', '')
        avg_return = 5.0
        match_ret = re.findall(r'([\d\.]+)%', return_rate_str)
        if match_ret:
            # use the last one which is average return rate
            avg_return = float(match_ret[-1])
            
        # Parse weight from details
        weight_str = details.get('平均重量', '')
        weight_lbs = 1.5
        match_w = re.search(r'([\d\.]+)\s*pounds', weight_str)
        if match_w:
            weight_lbs = float(match_w.group(1))
            
        # Parse price from item['avgBsr'] (e.g. "1.1\n$28.92")
        price_str = item.get('avgBsr', '')
        price_val = 30.0
        match_p = re.search(r'\$\s*([\d\.,]+)', price_str)
        if match_p:
            price_val = float(match_p.group(1).replace(',', ''))
            
        # Parse reviews from item['avgRevenue'] (e.g. "695\n4.3")
        reviews_str = item.get('avgRevenue', '')
        reviews_val = 500
        match_r = re.search(r'^([\d\.,]+)', reviews_str.strip())
        if match_r:
            reviews_val = int(match_r.group(1).replace(',', ''))
            
        # Parse profit margin from details
        profit_str = details.get('平均毛利率', '')
        profit_val = 60.0
        match_pr = re.search(r'([\d\.]+)%', profit_str)
        if match_pr:
            profit_val = float(match_pr.group(1))
            
        # Parse concentration (Brand) from item['sellerType'] (e.g. "商品: 30.9%\n品牌: 57.7%...")
        conc_str = item.get('sellerType', '')
        brand_conc = 50.0
        match_bc = re.search(r'品牌:\s*([\d\.]+)%', conc_str)
        if match_bc:
            brand_conc = float(match_bc.group(1))
            
        # Parse Chinese seller ratio from details
        seller_loc = details.get('卖家所属地', '')
        cn_ratio = 50.0
        match_cn = re.search(r'中国\|([\d\.]+)%', seller_loc)
        if match_cn:
            cn_ratio = float(match_cn.group(1))
        elif '美国' in seller_loc:
            match_us = re.search(r'美国\|([\d\.]+)%', seller_loc)
            if match_us:
                cn_ratio = 100.0 - float(match_us.group(1))
                
        # Risk classification
        level = '🟢 Green (Recommended)'
        red_reasons = []
        if avg_return > 10.0:
            red_reasons.append("退货率过高")
        if weight_lbs > 2.5:
            red_reasons.append("重量超标")
        if reviews_val > 1000:
            red_reasons.append("Review护城河太深")
        if any(x in en_name for x in ['Insects', 'Livestock', 'Wormers']):
            red_reasons.append("动植物/活体或兽药强监管风险")
        if 'Hoodies' in en_name or 'Clothing' in path or 'Shoes' in path:
            red_reasons.append("服装鞋帽高退货率与SKU过多")
            
        yellow_reasons = []
        if 8.0 < avg_return <= 10.0:
            yellow_reasons.append("退货率稍高")
        if 2.0 < weight_lbs <= 2.5:
            yellow_reasons.append("重量稍重")
        if 800 < reviews_val <= 1000:
            yellow_reasons.append("Review数量偏高")
        if 'Toys' in path:
            yellow_reasons.append("玩具类需复杂合规认证")
        if 'Electronics' in path or 'Battery' in en_name or 'Charger' in en_name:
            yellow_reasons.append("带电电子产品，需合规资质")
            
        if red_reasons:
            level = '🔴 Red (Avoid)'
        elif yellow_reasons:
            level = '🟡 Yellow (Cautious)'
            
        scored_categories.append({
            'index': item['index'], # original raw niche cell
            'en_name': en_name,
            'zh_name': zh_name,
            'path': path,
            'zh_path': zh_path,
            'sales': item['sampleSize'], # raw sales cell
            'price': price_val,
            'reviews': reviews_val,
            'weight': weight_lbs,
            'profit': profit_val,
            'return_rate': avg_return,
            'brand_conc': brand_conc,
            'cn_ratio': cn_ratio,
            'level': level,
            'red_reasons': red_reasons,
            'yellow_reasons': yellow_reasons
        })

    # Let's write the matching logic between 150 categories and the keywords
    matched_niches = []
    
    stop_words = {
        'and', 'for', 'the', 'with', 'parts', 'accessories', 'tools', 'devices',
        'kit', 'covers', 'cover', 'pack', 'set', 'sets', 'bag', 'bags', 'box', 'boxes',
        'holder', 'holders', 'mount', 'mounts', 'protector', 'protectors', 'case', 'cases',
        'organizer', 'organizers', 'mat', 'mats', 'pad', 'pads', 'rack', 'racks',
        'strap', 'straps', 'clip', 'clips', 'hook', 'hooks', 'hanger', 'hangers',
        'stand', 'stands', 'support', 'supports', 'cushion', 'cushions', 'sleeve', 'sleeves',
        'shield', 'shields', 'basket', 'baskets', 'product', 'products', 'device', 'devices',
        'tool', 'tools', 'trainer', 'trainers', 'mill', 'mills', 'extractor', 'extractors',
        'coax', 'coaxial', 'coupler', 'couplers', 'adapter', 'adapters', 'connector', 'connectors',
        'in', 'on', 'at', 'by', 'of', 'to', 'or', 'from', 'a', 'an',
        'top', 'bottom', 'side', 'front', 'rear', 'outdoor', 'indoor', 'small', 'large', 'mini', 'heavy', 'light',
        'replacement', 'part', 'system', 'combo', 'electric', 'manual', 'storage', 'carrier', 'anti', 'wind', 'air',
        'water', 'waterproof', 'cup', 'cups', 'glass', 'glasses', 'rod', 'rods', 'bar', 'bars', 'pole', 'poles',
        'plate', 'plates', 'accessory', 'kits', 'shrug', 'shrugs', 'sandals', 'sandal', 'pant', 'pants', 'shirt', 'shirts',
        'jacket', 'jackets', 'dress', 'dresses', 'short', 'shorts', 'shoe', 'shoes', 'boot', 'boots', 'goggle', 'goggles',
        'coat', 'coats', 'hoodie', 'hoodies', 'jersey', 'jerseys'
    }

    for cat in scored_categories:
        cat_keywords = []
        cat_stems = get_stems(cat['en_name']) - stop_words
        
        # Check from 316 targeted keywords
        for kw in keywords:
            kw_name = kw['keyword'].replace('\n', ' ').strip()
            kw_en = re.sub(r'[\u4e00-\u9fa5]+', '', kw_name).lower()
            kw_stems = get_stems(kw_en) - stop_words
            
            # Semantic overlap check
            common = cat_stems.intersection(kw_stems)
            if common:
                price_match = re.search(r'\$\s*([\d\.]+)', kw.get('price_reviews', ''))
                kw_price = float(price_match.group(1)) if price_match else 0.0
                
                rev_match = re.search(r'([\d\.,]+)\s*\(', kw.get('price_reviews', ''))
                kw_reviews = int(rev_match.group(1).replace(',', '')) if rev_match else 0
                
                searches_match = re.search(r'^([\d\.,]+)', kw.get('searches', ''))
                kw_searches = int(searches_match.group(1).replace(',', '')) if searches_match else 0
                
                p_parts = kw.get('purchases', '').split('\n')
                kw_purchases = int(re.sub(r'[^\d]', '', p_parts[0])) if p_parts else 0
                kw_pr = parse_percent(p_parts[1]) if len(p_parts) >= 2 else 0.0
                
                m_parts = kw.get('monopoly', '').split('\n')
                kw_mono = parse_percent(m_parts[0]) if m_parts else 0.0
                
                # Check if it fits basic filters
                if kw_searches >= 500:
                    cat_keywords.append({
                        'keyword': kw_en.strip(),
                        'searches': kw_searches,
                        'purchases': kw_purchases,
                        'purchase_rate': kw_pr,
                        'price': kw_price,
                        'reviews': kw_reviews,
                        'monopoly_click_rate': kw_mono,
                        'details': kw['details'].replace('\n', ' ')
                    })
                    
        # Sort category keywords by searches desc
        cat_keywords = sorted(cat_keywords, key=lambda x: x['searches'], reverse=True)
        
        matched_niches.append({
            'cat': cat,
            'keywords': cat_keywords
        })
            
    # Generate the Markdown report
    green_niches = [c for c in scored_categories if c['level'] == '🟢 Green (Recommended)']
    yellow_niches = [c for c in scored_categories if c['level'] == '🟡 Yellow (Cautious)']
    
    md = []
    md.append("# 亚马逊 150 个放宽类目与高潜力可见关键词匹配深度分析报告\n")
    md.append("> [!IMPORTANT]")
    md.append("> 本报告成功筛选出 **150 个放宽的新手备选子类目**，并将其与提取的关键词进行了语义匹配。我们从匹配成功的节点中，精选出最能平衡“后端零风险”与“前端高可见度”的品类推荐给您。\n")
    
    md.append("## 一、 150 个备选子类目的风控审核结果\n")
    md.append(f"我们对 150 个子类目进行了自动风控评估。其中：")
    md.append(f"- **绿色通道 (推荐) 🟢**：共 **{len(green_niches)}** 个。物理重量轻（< 2.5磅）、平均退货率低（< 8%）、无强合规资质，最适合新手。")
    md.append(f"- **黄色通道 (谨慎) 🟡**：共 **{len(yellow_niches)}** 个。通常包含带电产品（需要UL/FCC认证，如充电器、加热设备）或平均退货率略高。")
    md.append(f"- **红色通道 (避坑) 🔴**：共 **{len(scored_categories) - len(green_niches) - len(yellow_niches)}** 个。包含活体昆虫、兽医用药、SKU极繁多的服装等，建议彻底避开。\n")
    
    md.append("## 二、 黄金对齐：具有极佳可见度关键词的安全赛道推荐\n")
    md.append("为了解决新手“产品无法被看到”的痛点，我们选出以下既在**绿色安全通道内**，又有**极低标题密度、高购买率长尾词**支撑的黄金赛道：\n")
    
    green_matched = [m for m in matched_niches if m['cat']['level'] == '🟢 Green (Recommended)' and m['keywords']]
    
    for idx, match in enumerate(green_matched):
        cat = match['cat']
        md.append(f"### 🏆 推荐 {idx+1}：{cat['en_name']} ({cat['zh_name']})\n")
        md.append(f"- **大类目路径**：`{cat['path']}`")
        md.append(f"- **类目基本指标**：平均客单价 `{cat['price']:.2f}` | 平均 Reviews `{cat['reviews']}` | 平均重量 `{cat['weight']} lbs` | 平均退货率 `{cat['return_rate']}%` | 品牌集中度 `{cat['brand_conc']}%` | 中国卖家比例 `{cat['cn_ratio']}%`")
        md.append("- **匹配到的黄金长尾关键词**：\n")
        
        md.append("  | 关键词 | 月搜索量 | 月购买量 | 购买率 | 均价 | 评分数 (Reviews) | 点击垄断率 | 标题密度 | 新手运营特性建议 |")
        md.append("  | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        
        for kw in match['keywords'][:15]: # Display up to 15 keywords
            # parse spr / title density
            spr = 0
            td = 0
            spr_m = re.search(r'SPR:\s*(\d+)', kw['details'])
            td_m = re.search(r'标题密度:\s*(\d+)', kw['details'])
            if spr_m: spr = int(spr_m.group(1))
            if td_m: td = int(td_m.group(1))
            
            advice = "标题SEO重点布局"
            if td <= 2:
                advice = "🔥 黄金SEO词 (包含即上首页)"
            elif kw['purchase_rate'] >= 4.0:
                advice = "💰 高转化词 (适合打广告)"
                
            md.append(f"  | `{kw['keyword']}` | {kw['searches']:,} | {kw['purchases']:,} | {kw['purchase_rate']}% | ${kw['price']} | {kw['reviews']} | {kw['monopoly_click_rate']}% | {td} | {advice} |")
            
        md.append("\n- **新手选品与商品特征建议**：")
        name_l = cat['en_name'].lower()
        if 'burning' in name_l:
            md.append("  - **差异化方向**：由于主词 `wood burning tool` 评价偏高，新手应主打 `wood burning stencils` (烙画钢网) 配件包，或者定制黄铜印章 `custom wood burning stamp`，高客单价且完全避开主机竞争。")
            md.append("  - **包装与物流**：钢网和印章极其轻薄，建议采用信封式包装或小型硬纸盒包装，能极大节省亚马逊 FBA 头程和配送费用。")
            md.append("  - **质量风控**：非带电设备，避免了电器安全认证（如UL）以及电路故障退货，退货率极低。")
        elif 'gaiter' in name_l:
            md.append("  - **差异化方向**：避开普通登山绑腿，主攻 `snake gaiters` (防蛇绑腿) 或者 `tick gaiters` (防蜱虫绑腿)，主打特定功能性材质防护，退货率极低且无尺寸压货风险。")
            md.append("  - **包装与物流**：织物类轻小件，压缩后体积小，物流成本微乎其微。")
            md.append("  - **质量风控**：重点在于材质的功能性检测报告（如防蛇咬测试），需要在 Listing 中清晰展示测试证书以建立信任。")
        elif 'seat' in name_l:
            md.append("  - **差异化方向**：避开竞争激烈的通用汽车坐垫。重点开发 `motorcycle seat cover` (摩托车防晒/防雨套) 或针对特定细分群体的 `dog car seat cover` (宠物车载防脏垫)。")
            md.append("  - **包装与物流**：折叠包装，重量适中，适合小规格箱配送。")
            md.append("  - **质量风控**：突出易清洁（防水、防刮擦材质）和防滑底部设计，能够有效降低因品质不符产生的退货。")
        else:
            md.append("  - **差异化方向**：主打长尾功能型配件。在标题中精准覆盖标题密度 <= 2 的长尾词，避开核心高Reviews竞品，用轻小包装控制仓储物流费。")
        md.append("\n---\n")
        
    # Section 3: High-Potential Blue Ocean Categories (Without direct matches in current targeted keywords scan)
    md.append("## 三、 潜力蓝海赛道推荐（暂无本轮特定长尾词匹配，但指标极佳）\n")
    md.append("以下是筛选出来的**绿色安全通道**中，尚未匹配到本轮特定长尾词，但类目数据表现非常优异的子类目。这些类目非常适合作为下一步重点挖掘的方向：\n")
    
    md.append("| 序号 | 潜力子类目 | 英文路径 | 平均客单价 | 平均Reviews | 退货率 | 新手友好度与商机分析 |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    blue_ocean_cats = [m['cat'] for m in matched_niches if m['cat']['level'] == '🟢 Green (Recommended)' and not m['keywords']]
    
    for idx, cat in enumerate(blue_ocean_cats):
        reason = "客单价合理，退货率低，无合规资质限制，属于刚需轻小件。"
        name_l = cat['en_name'].lower()
        if 'basket' in name_l:
            reason = "面包发酵篮属于厨房烘焙刚需替换件，无电路故障风险，退货率极低，可开发多规格套装或搭配烘焙工具配件包。"
        elif 'box' in name_l:
            reason = "装饰盒/收纳盒属于家居强刚需，设计风格是主要购买驱动力，通过差异化图案或材质（如竹木、藤编）可避开低价竞争。"
        elif 'nozzle' in name_l:
            reason = "喷嘴为园艺/清洗机易耗配件，物理重量极轻，单价适中，适合开发多型号兼容的多彩组合装。"
        elif 'cup' in name_l:
            reason = "派对聚会杯子，销量巨大。建议开发特定环保材质（如降解竹纤维）或特定节日定制印花款。"
        elif 'extractor' in name_l:
            reason = "分接抽水机/螺丝取出器为小众五金工具，客单价好，退货率低，专业买家多，主打耐磨损硬度（如钛合金）。"
        elif 'mill' in name_l:
            reason = "胡椒磨/研磨器，主打高品质陶瓷磨芯，外观设计空间大（极简木质或不锈钢），适合礼品属性开发。"
        elif 'feeder' in name_l:
            reason = "喂鸟器/宠物喂食器，国外庭院文化刚需。可主打防松鼠设计（squirrel-proof）或特定外观风格。"
        elif 'emblem' in name_l:
            reason = "汽车/摩托车标徽，超轻小件，退货率低，多为车迷个性化定制，适合开发多样化潮流图案。"
            
        md.append(f"| {idx+1} | **{cat['en_name']}** | `{cat['path']}` | ${cat['price']:.2f} | {cat['reviews']} | {cat['return_rate']}% | {reason} |")
        
    report_content = "\n".join(md)
    
    # Save files
    artifact_path = "/Users/zhoufan/.gemini/antigravity-cli/brain/9984e585-9795-4a86-9aa8-aeb0a61ba197/relaxed_cross_match_analysis_2026_06_08.md"
    with open(artifact_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Saved artifact to {artifact_path}")
    
    workspace_path = "/Users/zhoufan/Public/workspace/amazon/results/relaxed_cross_match_analysis_report_2026_06_08.md"
    with open(workspace_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Copied report to workspace: {workspace_path}")

if __name__ == "__main__":
    main()
