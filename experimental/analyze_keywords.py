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
    # Search for first percentage
    match = re.search(r'([\d\.]+)%', val)
    return float(match.group(1)) if match else 0.0

def parse_price_reviews(val):
    if not val:
        return 0.0, 0, 0.0
    price_val = 0.0
    reviews_val = 0
    rating_val = 0.0
    
    # Price
    price_match = re.search(r'\$\s*([\d\.,]+)', val)
    if price_match:
        price_val = float(price_match.group(1).replace(',', ''))
        
    # Reviews & Rating
    # E.g. "240 (4.9)" or "165 (4.5)"
    rev_match = re.search(r'([\d\.,]+)\s*\(([\d\.]+)\)', val)
    if rev_match:
        reviews_val = int(rev_match.group(1).replace(',', ''))
        rating_val = float(rev_match.group(2))
    else:
        # Just reviews
        digits = re.findall(r'\d+', val)
        if len(digits) >= 2:
            # check if last looks like rating
            pass
            
    return price_val, reviews_val, rating_val

def parse_bid(val):
    if not val:
        return 0.0
    # e.g. "$0.50\n$0.64\n$0.82" -> returns average ($0.64)
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

def clean_details(details_str):
    # Remove newlines and format nicely
    return details_str.replace('\n', ' ').strip()

def process_keywords(raw_list):
    processed = []
    for item in raw_list:
        kw = item['keyword'].replace('\n', ' ').strip()
        kw_en = re.sub(r'[\u4e00-\u9fa5]+', '', kw).strip()
        kw_zh = ''.join(re.findall(r'[\u4e00-\u9fa5]+', kw)).strip()
        
        searches = parse_num(item['searches'])
        
        # Purchases & Purchase Rate
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
        
        # Extract SPR & Title Density
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
            'details': clean_details(details),
            'target_niche': item.get('target_niche', 'N/A'),
            'seed_term': item.get('seed_term', 'N/A')
        })
    return processed

def main():
    # Load raw datasets
    kws_a = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_methodology_a_2026_06_08.json')
    kws_b = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_methodology_b_2026_06_08.json')
    kws_c = load_json('/Users/zhoufan/Public/workspace/amazon/results/keyword_results_targeted_2026_06_08.json')
    
    proc_a = process_keywords(kws_a)
    proc_b = process_keywords(kws_b)
    proc_c = process_keywords(kws_c)
    
    # Write analysis markdown
    md_content = []
    md_content.append("# 卖家精灵关键词选品与 22 个候选品类深度匹配分析报告\n")
    md_content.append("> [!NOTE]")
    md_content.append("> 本报告基于卖家精灵网页端 May 2026 核心数据，采用三种不同的选词过滤机制进行检索，并将匹配到的关键词与我们之前的全类目 22 个新手友好精选赛道进行横向对齐。\n")
    
    md_content.append("## 一、 关键词选品的三大筛选维度与数据成果\n")
    md_content.append("为了能够多角度挖掘适合新手开店的利基需求，我们执行了以下三种完全不同的关键词检索模式：\n")
    
    md_content.append("1. **【维度 A：高转化收割流】** (Scraped 50 keywords)")
    md_content.append("   - **核心逻辑**：寻找“搜索即买”的高购买率词，控制广告转化成本。")
    md_content.append("   - **过滤参数**：月搜索量 2k-20k，购买量 $\ge 150$，购买率 $\ge 4.0\%$，点击集中度 $\le 45\%$，需供比 $\le 0.04$，价格 $\ge \$35$，平均 Reviews $\le 400$，PPC 竞价 $\le \$1.20$。\n")
    
    md_content.append("2. **【维度 B：蓝海低竞争流】** (Scraped 21 keywords)")
    md_content.append("   - **核心逻辑**：寻找供求极度不平衡（供不应求）且基本没有精准竞争对手的词。")
    md_content.append("   - **过滤参数**：月搜索量 2k-20k，购买量 $\ge 100$，购买率 $\ge 3.0\%$，点击集中度 $\le 50\%$，需供比 $\le 0.02$ (极低)，标题密度 $\le 3$ (即首页几乎没有标题精准包含该词的Listing)，PPC 竞价 $\le \$1.00$。\n")
    
    md_content.append("3. **【维度 C：定向品类拉词流】** (Scraped 316 keywords across 8 niches)")
    md_content.append("   - **核心逻辑**：直接针对我们 22 个品类中推荐星级最高 (★★★★★) 的 8 个物理硬件及配件品类，不设置任何前置筛选条件拉出全部包含特定词根的核心搜索词，以分析真实的市场竞争和长尾结构。\n")
    
    # Part 2: Analysis of Methodology A
    md_content.append("## 二、 维度 A (高转化收割流) 优质新手词及分类对齐\n")
    md_content.append("以下是在 50 个高转化搜索词中，过滤掉大品牌词（如 lego, raspberry pi等）和服装、玩具等高风险品类后，最适合新手的优质词：\n")
    
    md_content.append("| 关键词 | 中文翻译 | 月搜索量 | 月购买量 | 购买率 | 均价 | 评分数 | 点击垄断率 | 标题密度 | 匹配 22 个候选品类 |")
    md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    for kw in proc_a:
        # Filter out junk
        kw_l = kw['keyword'].lower()
        is_junk = any(x in kw_l for x in ['lego', 'raspberry', 'toddler', 'couch', 'kids', 'women', 'men', 'woman', 'halloween', 'wedding'])
        if is_junk:
            continue
        
        # Check matching 22 categories
        match_cat = "无直接对应 (可做独立新市场)"
        if 'detail' in kw_l or 'car' in kw_l or 'clean' in kw_l:
            match_cat = "【汽车货架/防盗】"
        elif 'safe' in kw_l:
            match_cat = "【家居安防】"
        elif 'resin' in kw_l:
            match_cat = "【工艺品/水过滤】"
            
        md_content.append(f"| `{kw['keyword']}` | {kw['zh_translation']} | {kw['searches']:,} | {kw['purchases']:,} | {kw['purchase_rate']}% | ${kw['price']} | {kw['reviews']} | {kw['monopoly_click_rate']}% | {kw['title_density']} | {match_cat} |")
        
    md_content.append("\n> [!TIP]")
    md_content.append("> **重点词汇分析：**")
    md_content.append("> - `detail kit` (汽车细节清洁工具包)：均价 $39.99，Reviews 仅 416，且标题密度为 0 (代表首页没有 Listing 的标题精准包含该词)。这是一个非常典型的新手汽车配件/清洁套件赛道，可以直接和我们的第 20 项 (Car Rack Parts) 以及整体汽配板块融合。")
    md_content.append("> - `di resin` (去离子树脂)：用于高档洗车防止留下水斑，均价 $49.99，Reviews 125 极其低，购买率高达 8.98% (极高)。虽然属于消耗品类，但高毛利和极低的 Reviews 门槛对新手吸引力极强。")
    md_content.append("> - `floor safe` (地板保险箱)：均价 $85.00，属于重型安防，但 Reviews 383，点击垄断仅 24.25%，也是一个可关注的细分品类。\n")
    
    # Part 3: Analysis of Methodology B
    md_content.append("## 三、 维度 B (蓝海低竞争流) 优质新手词及分类对齐\n")
    md_content.append("在 21 个低竞争、低竞价的蓝海词中，排除服装/配件后的精品词：\n")
    
    md_content.append("| 关键词 | 中文翻译 | 月搜索量 | 月购买量 | 购买率 | 均价 | 评分数 | 点击垄断率 | 标题密度 | 匹配 22 个候选品类 |")
    md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    
    for kw in proc_b:
        kw_l = kw['keyword'].lower()
        is_junk = any(x in kw_l for x in ['lego', 'raspberry', 'toddler', 'couch', 'kids', 'women', 'men', 'woman', 'halloween', 'wedding'])
        if is_junk:
            continue
            
        match_cat = "无直接对应"
        if 'bike' in kw_l:
            match_cat = "【4】 Headlights (骑行车灯)"
            
        md_content.append(f"| `{kw['keyword']}` | {kw['zh_translation']} | {kw['searches']:,} | {kw['purchases']:,} | {kw['purchase_rate']}% | ${kw['price']} | {kw['reviews']} | {kw['monopoly_click_rate']}% | {kw['title_density']} | {match_cat} |")
        
    md_content.append("\n> [!TIP]")
    md_content.append("> **重点词汇分析：**")
    md_content.append("> - `bike lights for night riding` (夜间骑行车灯)：搜索量 3,500+，虽然有一些自行车车灯大词，但此长尾词代表了极度具体的夜间骑行防水、安全警示场景。它能完美对应我们 22 个品类中评级为 Green (★★★★★) 的 **【4】 Headlights (自行车车头灯)**。新手通过在标题中精准包含此词，极易在无广告情况下冲上首页。\n")
    
    # Part 4: Analysis of Methodology C (Targeted matching)
    md_content.append("## 四、 维度 C (定向品类拉词)：8 大核心品类的真实长尾词匹配与过滤诊断\n")
    md_content.append("在维度 C 中，我们对 top 推荐的 8 个赛道进行了全面的流量词拉取，共获取 316 个词。")
    md_content.append("通过分析这些原始流量词，我们得出了**为什么这些优质品类在最初的“新手严格过滤”中被漏掉的真实原因**，并筛选出了实际适合新手关注的长尾出单词：\n")
    
    # We will loop through each niche and list top keywords
    grouped_c = {}
    for kw in proc_c:
        niche = kw['target_niche']
        if niche not in grouped_c:
            grouped_c[niche] = []
        grouped_c[niche].append(kw)
        
    for niche, kws in grouped_c.items():
        md_content.append(f"### 🟢 赛道：{niche}\n")
        md_content.append(f"共抓取到该赛道核心词 **{len(kws)}** 个。以下为最具代表性的长尾/核心搜索词：\n")
        
        md_content.append("| 关联搜索词 | 中文翻译 | 月搜索量 | 月购买量 | 购买率 | 均价 | 评分数 | 点击垄断率 | 标题密度 | 诊断：为何此前被过滤？ |")
        md_content.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        
        # Sort keywords by searches desc and show top 5-6
        kws_sorted = sorted(kws, key=lambda x: x['searches'], reverse=True)
        for kw in kws_sorted[:6]:
            # diagnose why it was filtered by original newbie template:
            # searches: 2000-20000, purchases >= 100, price >= 30, reviews <= 500, monopoly <= 50, bid <= 1.50, purchase_rate >= 3.0, supply_demand <= 0.05
            reasons = []
            if kw['searches'] < 2000:
                reasons.append("搜索量<2k")
            elif kw['searches'] > 20000:
                reasons.append("搜索量>20k")
            if kw['purchases'] < 100:
                reasons.append("购买量<100")
            if kw['price'] < 30.0:
                reasons.append(f"价格 ${kw['price']}<$30")
            if kw['reviews'] > 500:
                reasons.append(f"评价 {kw['reviews']}>500")
            if kw['monopoly_click_rate'] > 50.0:
                reasons.append(f"垄断率 {kw['monopoly_click_rate']}%>50%")
            if kw['purchase_rate'] < 3.0:
                reasons.append(f"购买率 {kw['purchase_rate']}%<3%")
                
            reason_str = "、".join(reasons) if reasons else "符合新手指标"
            
            md_content.append(f"| `{kw['keyword']}` | {kw['zh_translation']} | {kw['searches']:,} | {kw['purchases']:,} | {kw['purchase_rate']}% | ${kw['price']} | {kw['reviews']} | {kw['monopoly_click_rate']}% | {kw['title_density']} | {reason_str} |")
            
        md_content.append("\n")
        
    # Summarize and give action plan
    md_content.append("## 五、 总结与新手开店实操行动建议\n")
    md_content.append("1. **选品与选词的结合**：")
    md_content.append("   - 如果您选择 **【4】 Headlights (车头灯)** 赛道，核心词 `bike lights` 竞争剧烈，但长尾词 `bike lights for night riding` 或 `waterproof bike lights` 是极其完美的流量切入点。")
    md_content.append("   - 如果您选择 **【8】 Wood Burning Tools (木材燃烧工具)** 赛道，虽然主词 `wood burning kit` 评价数较高（1,030），但其衍生词 `wood burning tool for beginners` (月搜 1,500+) 竞争极低，价格和利润空间依然完美符合新手标准。\n")
    
    md_content.append("2. **过滤条件“松绑”的必要性**：")
    md_content.append("   - 在数据分析中我们发现，很多优质的长尾蓝海产品（如汽配的 `fuel gauge`、户外运动的 `gaiters`）其主词因为历史积累使得平均 Reviews 略微超标（在 500-1000 之间），或者主词单价刚好在 $25-$29 之间（如 `wood burning tool` 价格为 $22.99）。")
    md_content.append("   - **建议**：在后续选品中，不要将 Reviews 限制在 500 以内作为一刀切的硬性指标。对于物理配件类长尾产品，Reviews 限制放宽到 1000 依然是绝对安全的蓝海；价格放宽到 $20-$25 也是完全能保障毛利率的。")
    
    # Save files
    report_content = "\n".join(md_content)
    
    # Conversation Artifact
    artifact_path = "/Users/zhoufan/.gemini/antigravity-cli/brain/9984e585-9795-4a86-9aa8-aeb0a61ba197/keyword_matching_analysis_report.md"
    with open(artifact_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Saved artifact to {artifact_path}")
    
    # Workspace results
    workspace_path = "/Users/zhoufan/Public/workspace/amazon/results/keyword_matching_analysis_report_2026_06_08.md"
    with open(workspace_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    print(f"Copied report to workspace: {workspace_path}")

if __name__ == "__main__":
    main()
