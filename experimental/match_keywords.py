import json
import re

# Load candidate categories
with open('/Users/zhoufan/Public/workspace/amazon/results/twenty_two_beginner_results_2026_06_07.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

# Load keyword search results
with open('/Users/zhoufan/Public/workspace/amazon/results/keyword_search_results_2026_06_08.json', 'r', encoding='utf-8') as f:
    keywords = json.load(f)

# Let's map each of the 22 categories to their recommendation levels and paths
cat_info = {}
for item in categories:
    niche_name = item['niche'].replace('\n', ' ')
    clean_name = re.sub(r'\s*\(.*?\)\s*', '', niche_name).strip()
    zh_name = re.search(r'\((.*?)\)', niche_name)
    zh_name = zh_name.group(1) if zh_name else ''
    
    # Extract recommendation level from the main markdown table or set based on our report
    # 1: Beneficial Insects - Red
    # 2: Wrinkle & Anti-Aging Devices - Green
    # 3: Livestock Health Supplies - Red
    # 4: Headlights - Green
    # 5: Remote & App Controlled Vehicle Batteries - Red
    # 6: Battery Chargers - Yellow
    # 7: Hearing Amplifiers - Red
    # 8: Wood Burning Tools - Green
    # 9: Sound Therapy - Green
    # 10: Scoreboards & Timers - Green
    # 11: Gaiters - Green
    # 12: Hoodies - Red
    # 13: Brake Controls - Green
    # 14: Wormers - Red
    # 15: Seat Covers - Green
    # 16: Alarms & Anti-Theft - Green
    # 17: Optics Accessories - Green
    # 18: Leak Detection Tools - Yellow
    # 19: Food Processor Parts & Accessories - Green
    # 20: Car Rack Parts & Accessories - Green
    # 21: Night Vision Binoculars & Goggles - Yellow
    # 22: Fuel - Green
    
    idx = int(item['index'])
    level = '🟢 Green (Recommended)'
    if idx in [1, 3, 5, 7, 12, 14]:
        level = '🔴 Red (Avoid)'
    elif idx in [6, 18, 21]:
        level = '🟡 Yellow (Cautious)'
        
    cat_info[idx] = {
        'name': clean_name,
        'zh_name': zh_name,
        'path': item['details'].get('完整市场路径', ''),
        'zh_path': item['details'].get('市场路径(中文)', ''),
        'level': level
    }

print("Loaded 22 candidate categories.")

# Let's process the keywords
matched_results = []
for kw in keywords:
    kw_name = kw['keyword'].replace('\n', ' ').strip()
    kw_en = re.sub(r'[\u4e00-\u9fa5]+', '', kw_name).strip()
    kw_zh = ''.join(re.findall(r'[\u4e00-\u9fa5]+', kw_name)).strip()
    
    details_str = kw.get('details', '')
    
    # Parse sub-categories
    # e.g., "所属类目:\nClothing, Shoes & Jewelry(52%)\nHealth, Household & Baby Care(24%)"
    dep_matches = re.findall(r'([A-Za-z &,\']+)\((\d+)%\)', details_str)
    departments = {dep.strip(): int(pct) for dep, pct in dep_matches}
    
    # Let's find matches
    matches = []
    
    # Strategy 1: String matching on English and Chinese names
    for idx, cat in cat_info.items():
        # Clean tokens
        cat_tokens = set(re.findall(r'\w+', cat['name'].lower()))
        kw_tokens = set(re.findall(r'\w+', kw_en.lower()))
        
        # Intersection of tokens
        intersect = cat_tokens.intersection(kw_tokens)
        
        # Remove common stopwords/very short words
        intersect = {t for t in intersect if len(t) > 2 and t not in ['and', 'for', 'the', 'with', 'parts', 'accessories', 'tools', 'devices']}
        
        token_match = len(intersect) > 0
        
        # Check Chinese character matches
        zh_match = False
        if kw_zh and cat['zh_name']:
            # look for overlapping characters
            kw_zh_set = set(kw_zh)
            cat_zh_set = set(cat['zh_name'])
            overlap = kw_zh_set.intersection(cat_zh_set)
            # ignore very general terms like '器', '套', '具', '车', '防', '件'
            overlap = {c for c in overlap if c not in ['器', '套', '具', '车', '防', '件', '用', '品', '装', '备', '控', '制']}
            if len(overlap) >= 2 or (len(overlap) >= 1 and len(cat['zh_name']) <= 3):
                zh_match = True
                
        # Classify based on category path overlap
        path_match = False
        cat_root = cat['path'].split('›')[0].strip() if '›' in cat['path'] else cat['path'].strip()
        # Map common aliases between search root category and Sellersprite categories
        # e.g. "Beauty & Personal Care" -> "Beauty & Personal Care", "Automotive Parts & Accessories" -> "Automotive", "Arts, Crafts & Sewing" -> "Arts, Crafts & Sewing"
        for dep, pct in departments.items():
            if pct >= 10:  # significant share
                dep_lower = dep.lower()
                cat_root_lower = cat_root.lower()
                # Check for broad match
                if (cat_root_lower in dep_lower) or (dep_lower in cat_root_lower) or \
                   ('automotive' in cat_root_lower and 'automotive' in dep_lower) or \
                   ('sports' in cat_root_lower and 'sports' in dep_lower) or \
                   ('crafts' in cat_root_lower and 'crafts' in dep_lower) or \
                   ('home & kitchen' in cat_root_lower and 'home' in dep_lower):
                    path_match = True
                    
        if token_match or zh_match:
            matches.append({
                'cat_index': idx,
                'cat_name': cat['name'],
                'cat_zh_name': cat['zh_name'],
                'cat_level': cat['level'],
                'match_type': 'Text/Token Match'
            })
        elif path_match:
            # Only list if it's a category/department match and we don't have direct text match
            # Let's check how relevant it is
            pass

    # Clean up display values
    avg_price_reviews = kw.get('price_reviews', '').replace('\n', ' ')
    price_match = re.search(r'\$\d+(?:\.\d+)?', avg_price_reviews)
    price_val = price_match.group(0) if price_match else 'N/A'
    reviews_match = re.search(r'(\d+)\s*\((.*?)\)', avg_price_reviews)
    reviews_val = reviews_match.group(1) if reviews_match else 'N/A'
    rating_val = reviews_match.group(2) if reviews_match else 'N/A'

    searches_val = kw.get('searches', '').replace('\n', ' / ')
    purchases_val = kw.get('purchases', '').replace('\n', ' / ')
    monopoly_val = kw.get('monopoly', '').replace('\n', ' / ')
    bid_val = kw.get('bid', '').replace('\n', ' / ')

    matched_results.append({
        'index': kw['index'],
        'keyword': kw_name,
        'searches': searches_val,
        'purchases': purchases_val,
        'monopoly_click_rate': monopoly_val,
        'bid': bid_val,
        'price': price_val,
        'reviews': reviews_val,
        'rating': rating_val,
        'details': kw['details'].replace('\n', ' '),
        'matches': matches
    })

# Output matched list
print("\n--- KEYWORDS MATCHED TO 22 NICHES ---")
for kw in matched_results:
    if kw['matches']:
        print(f"Keyword #{kw['index']}: {kw['keyword']}")
        print(f"  Price: {kw['price']}, Reviews: {kw['reviews']}, Rating: {kw['rating']}")
        print(f"  Searches: {kw['searches']}, Purchases: {kw['purchases']}")
        print(f"  Matches:")
        for m in kw['matches']:
            print(f"    -> [{m['cat_index']}] {m['cat_name']} ({m['cat_zh_name']}) - {m['cat_level']}")
        print()

print("\n--- OTHER INTERESTING NEWBIE KEYWORDS (NOT IN 22 NICHES) ---")
for kw in matched_results:
    if not kw['matches']:
        # Filter out obvious big brands or poor niches
        kw_lower = kw['keyword'].lower()
        is_junk = any(brand in kw_lower for brand in ['lego', 'raspberry pi', 'women', 'men', 'woman', 'toddler', 'kids', 'couch', 'halloween', 'wedding'])
        if not is_junk:
            print(f"Keyword #{kw['index']}: {kw['keyword']}")
            print(f"  Price: {kw['price']}, Reviews: {kw['reviews']}, Rating: {kw['rating']}")
            print(f"  Searches: {kw['searches']}, Purchases: {kw['purchases']}, Click Monopoly: {kw['monopoly_click_rate']}")
            print(f"  Details: {kw['details']}")
            print()
