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

def parse_price_reviews(val):
    if not val:
        return 0.0, 0, 0.0
    price_val = 0.0
    reviews_val = 0
    rating_val = 0.0
    
    price_match = re.search(r'\$\s*([\d\.,]+)', val)
    if price_match:
        price_val = float(price_match.group(1).replace(',', ''))
        
    rev_match = re.search(r'([\d\.,]+)\s*\(([\d\.]+)\)', val)
    if rev_match:
        reviews_val = int(rev_match.group(1).replace(',', ''))
        rating_val = float(rev_match.group(2))
            
    return price_val, reviews_val, rating_val

def parse_bid(val):
    if not val:
        return 0.0
    parts = val.split('\n')
    if len(parts) >= 2:
        return parse_num(parts[1])
    elif len(parts) == 1:
        return parse_num(parts[0])
    return 0.0

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def process_keywords(raw_list, source_name):
    processed = []
    for item in raw_list:
        kw = item['keyword'].replace('\n', ' ').strip()
        kw_en = re.sub(r'[\u4e00-\u9fa5]+', '', kw).strip()
        kw_zh = ''.join(re.findall(r'[\u4e00-\u9fa5]+', kw)).strip()
        
        searches = parse_num(item['searches'])
        
        purchases = 0
        purchase_rate = 0.0
        p_parts = item['purchases'].split('\n')
        if len(p_parts) >= 1:
            purchases = parse_num(p_parts[0])
        if len(p_parts) >= 2:
            purchase_rate = parse_percent(p_parts[1])
        else:
            purchase_rate = parse_percent(item['purchases'])
            
        clicks = parse_num(item['clicks'])
        monopoly = parse_percent(item['monopoly'])
        products = parse_num(item['products'])
        bid = parse_bid(item['bid'])
        
        price, reviews, rating = parse_price_reviews(item['price_reviews'])
        
        spr = 0
        title_density = 0
        details = item['details']
        spr_match = re.search(r'SPR:\s*(\d+)', details)
        if spr_match:
            spr = int(spr_match.group(1))
        td_match = re.search(r'标题密度:\s*(\d+)', details)
        if td_match:
            title_density = int(td_match.group(1))
            
        processed.append({
            'keyword': kw_en,
            'zh_translation': kw_zh,
            'searches': searches,
            'purchases': purchases,
            'purchase_rate': purchase_rate,
            'monopoly_click_rate': monopoly,
            'products': products,
            'avg_bid': bid,
            'price': price,
            'reviews': reviews,
            'rating': rating,
            'spr': spr,
            'title_density': title_density,
            'source': source_name,
            'target_niche': item.get('target_niche', 'N/A')
        })
    return processed

def is_junk_keyword(kw_l):
    # Filter out big brands, irrelevant terms, seasonal costumes, or massive furniture
    junk_patterns = ['lego', 'raspberry', 'toddler', 'couch', 'kids', 'women', 'men', 'woman', 'halloween', 'wedding', 'table set', 'dining room', 'prophecy', 'the greeks', 'sex books', 'gameing pc', 'faithful']
    return any(x in kw_l for x in junk_patterns)

def main():
    kws_a = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_methodology_a_2026_06_08.json')
    kws_b = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_methodology_b_2026_06_08.json')
    kws_c = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_targeted_2026_06_08.json')
    
    proc_a = process_keywords(kws_a, '维度 A: 高转化收割流')
    proc_b = process_keywords(kws_b, '维度 B: 蓝海低竞争流')
    proc_c = process_keywords(kws_c, '维度 C: 定向赛道拉词流')
    
    # 1. Gather all potential keywords
    potential_list = []
    
    # From A: filter out junk
    for kw in proc_a:
        if not is_junk_keyword(kw['keyword'].lower()):
            potential_list.append(kw)
            
    # From B: filter out junk, avoid duplicates
    existing_kws = {k['keyword'].lower() for k in potential_list}
    for kw in proc_b:
        if not is_junk_keyword(kw['keyword'].lower()):
            if kw['keyword'].lower() not in existing_kws:
                potential_list.append(kw)
                existing_kws.add(kw['keyword'].lower())
                
    # From C (Targeted): For each of the 8 niches, we want to extract actual longtail words with searches > 1000 and reviews < 1500
    # and sort by searches desc
    grouped_c = {}
    for kw in proc_c:
        niche = kw['target_niche']
        if niche not in grouped_c:
            grouped_c[niche] = []
        grouped_c[niche].append(kw)
        
    c_selected = []
    for niche, kws in grouped_c.items():
        # Filter for beginner potential: searches > 1000, reviews < 1500, price > $10
        kws_filtered = [k for k in kws if k['searches'] >= 1000 and k['reviews'] <= 1500 and k['price'] >= 10.0]
        # Sort by searches desc
        kws_sorted = sorted(kws_filtered, key=lambda x: x['searches'], reverse=True)
        # Avoid duplicates with A/B
        for k in kws_sorted:
            if k['keyword'].lower() not in existing_kws:
                c_selected.append(k)
                existing_kws.add(k['keyword'].lower())
                
    # Combine lists
    # Let's categorize them for clear presentation
    
    md_content = []
    md_content.append("# 亚马逊新手开店精选：高潜力蓝海/长尾关键词清单\n")
    md_content.append("> [!IMPORTANT]")
    md_content.append("> 本清单完整列出了我们通过三种选词方式（高转化收割、蓝海供求差、定向赛道挖掘）所找到的所有契合新手的潜在关键词。已剔除大牌、大件及服装鞋帽等高风险高退货率词汇。\n")
    
    # Section 1: Methodology A & B High-Conversion & Blue Ocean general list
    md_content.append("## 一、 全站大类目筛选挖掘出的高价值蓝海关键词\n")
    md_content.append("这批关键词是通过对全类目执行高转化率或超低供求比过滤得到的，在流量转化或竞争环境上具有天然优势，是極佳的独立切入点。")
    md_content.append("\n| 序号 | 关键词 | 中文意思 | 月搜索量 | 月购买量 | 购买率 | 平均价格 | 评分数 (Reviews) | 点击垄断率 | 标题密度 | 来源渠道 | 建议匹配赛道 |")
    md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    idx = 1
    for kw in potential_list:
        match_cat = "独立蓝海赛道 (推荐重点考察)"
        kw_l = kw['keyword'].lower()
        if 'detail' in kw_l or 'clean' in kw_l:
            match_cat = "汽配美容细节套件"
        elif 'resin' in kw_l:
            match_cat = "去离子树脂 / 纯水洗车"
        elif 'safe' in kw_l:
            match_cat = "重型地板保险箱 (安防)"
        elif 'wrench' in kw_l:
            match_cat = "薄扳手五金工具"
        elif 'table' in kw_l:
            match_cat = "便携折叠桌 (户外/小户型)"
        elif 'chair' in kw_l or 'cushion' in kw_l:
            match_cat = "防滑椅子坐垫 (家居配件)"
        elif 'frame' in kw_l:
            match_cat = "自定义相框/批量框架 (手工艺)"
        elif 'bag' in kw_l:
            match_cat = "大容量防漏水袋/储物袋"
            
        md_content.append(f"| {idx} | `{kw['keyword']}` | {kw['zh_translation']} | {kw['searches']:,} | {kw['purchases']:,} | {kw['purchase_rate']}% | ${kw['price']} | {kw['reviews']} | {kw['monopoly_click_rate']}% | {kw['title_density']} | {kw['source']} | {match_cat} |")
        idx += 1
        
    # Section 2: Targeted Niche Keywords
    md_content.append("\n## 二、 定向匹配我们 22 个精选赛道的高潜力长尾关键词\n")
    md_content.append("这批关键词是在我们之前评估出的 **Green (五星级推荐) 新手优秀赛道** 中，放宽硬性 Reviews 条件（放宽至 1500 以下）和价格条件（放宽至 $10 以上）后，挖掘出的实际出单词和高流量关联词。")
    md_content.append("\n| 序号 | 精选赛道 | 关联关键词 | 中文意思 | 月搜索量 | 月购买量 | 购买率 | 平均价格 | 评分数 (Reviews) | 点击垄断率 | 标题密度 | 赛道针对性建议 |")
    md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    idx_c = 1
    for kw in c_selected:
        advice = "建议作为 Listing 标题主打词"
        kw_l = kw['keyword'].lower()
        if 'beginner' in kw_l or 'for' in kw_l or 'kit' in kw_l:
            advice = "新手高转化主推词 (PPC核心词)"
        elif kw['reviews'] > 800:
            advice = "核心流量词 (注意避开头部直接对比)"
        elif kw['title_density'] <= 2:
            advice = "黄金SEO词 (标题包含即可得自然排名)"
            
        md_content.append(f"| {idx_c} | {kw['target_niche']} | `{kw['keyword']}` | {kw['zh_translation']} | {kw['searches']:,} | {kw['purchases']:,} | {kw['purchase_rate']}% | ${kw['price']} | {kw['reviews']} | {kw['monopoly_click_rate']}% | {kw['title_density']} | {advice} |")
        idx_c += 1
        
    report_content = "\n".join(md_content)
    
    # Save to files
    artifact_path = "/Users/zhoufan/.gemini/antigravity-cli/brain/9984e585-9795-4a86-9aa8-aeb0a61ba197/potential_keywords_list.md"
    with open(artifact_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Saved artifact to {artifact_path}")
    
    workspace_path = "/Users/zhoufan/Public/workspace/amazon/results/potential_keywords_list_2026_06_08.md"
    with open(workspace_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Copied report to workspace: {workspace_path}")

if __name__ == "__main__":
    main()
