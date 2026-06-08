import json
import re
import os
import time
import datetime
import urllib.parse
import argparse
import subprocess

# Pre-defined known niche seeds to guarantee specific high-quality queries
KNOWN_NICHE_SEEDS = {
    "Wood Burning Tools": "wood burning",
    "Gaiters": "gaiters",
    "Seat Covers": "seat cover",
    "Alarms & Anti-Theft": "motorcycle alarm",
    "Optics Accessories": "scope mount",
    "Food Processor Parts & Accessories": "food processor",
    "Car Rack Parts & Accessories": "roof rack",
    "Fuel": "fuel gauge",
    "Tap Extractors": "tap extractor",
    "Decorative Boxes": "decorative box",
    "Herb & Spice Mills": "herb grinder",
    "Dash Covers": "dash cover",
    "Bladder Control Devices": "bladder control",
    "Feeders": "bird feeder",
    "Plaques & Wall Art": "wall art plaque",
    "Hands Free Leashes": "hands free leash",
    "Honey Jars": "honey jar",
    "Tattoo Kits": "tattoo kit",
    "Cookbook Stands": "cookbook stand",
    "Pond Lights": "pond lights",
    "Brake Controls": "brake control"
}

def clean_name(niche_str):
    if not niche_str:
        return ""
    name = niche_str.replace('\n', ' ').strip()
    return re.sub(r'\s*\(.*?\)\s*', '', name).strip()

def get_seed_term(niche_en):
    if niche_en in KNOWN_NICHE_SEEDS:
        return KNOWN_NICHE_SEEDS[niche_en]
    
    # Default cleaning fallback for new niches
    term = niche_en
    for suffix in ["Parts & Accessories", "Accessories", "Supplies", "Tools", "Products", "Devices", "Equipment", "Kits", "Stands", "Parts"]:
        if term.endswith(" " + suffix):
            term = term[:-len(" " + suffix)].strip()
            
    term = term.replace('&', ' ')
    term = re.sub(r'\s+', ' ', term).strip()
    return term.lower()

def run_opencli_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def classify_niche(niche_en_name, path, avg_return, weight_lbs, reviews_val, rules):
    # Risk classification rules matching select_market.py
    level = 'green'
    red_reasons = []
    
    red_rules = rules['red']
    if avg_return > red_rules['max_return_rate']:
        red_reasons.append(f"退货率过高 (>{red_rules['max_return_rate']}%)")
    if weight_lbs > red_rules['max_weight_lbs']:
        red_reasons.append(f"重量超标 (>{red_rules['max_weight_lbs']} lbs)")
    if reviews_val > red_rules['max_reviews']:
        red_reasons.append(f"Review护城河太深 (>{red_rules['max_reviews']})")
    if any(x in niche_en_name for x in red_rules['excluded_keywords']):
        red_reasons.append("排除类关键字过滤")
    if any(x in path for x in red_rules['excluded_paths']):
        red_reasons.append("高风险类目路径过滤")
        
    yellow_reasons = []
    yellow_rules = rules['yellow']
    if not red_reasons:
        if avg_return > yellow_rules['max_return_rate']:
            yellow_reasons.append(f"退货率偏高 (>{yellow_rules['max_return_rate']}%)")
        if weight_lbs > yellow_rules['max_weight_lbs']:
            yellow_reasons.append(f"重量偏重 (>{yellow_rules['max_weight_lbs']} lbs)")
        if reviews_val > yellow_rules['max_reviews']:
            yellow_reasons.append(f"Reviews偏高 (>{yellow_rules['max_reviews']})")
        if any(x in path for x in yellow_rules['excluded_paths']):
            yellow_reasons.append("谨慎认证类目路径")
        if any(x in niche_en_name for x in yellow_rules['excluded_keywords']):
            yellow_reasons.append("带电/合规资质敏感关键字")
            
    if red_reasons:
        level = 'red'
    elif yellow_reasons:
        level = 'yellow'
        
    return level

def parse_category_data(item):
    # Robust Python value auto-detection
    all_vals = []
    for k, v in item.items():
        if k != 'details' and isinstance(v, str):
            all_vals.append((k, v))
            
    niche_raw = ""
    avg_reviews_star_str = ""
    return_rate_str = ""
    
    for k, v in all_vals:
        v_stripped = v.strip()
        if not v_stripped:
            continue
        if '%' in v_stripped and '\n' in v_stripped and 'FBA' not in v_stripped and '商品' not in v_stripped:
            return_rate_str = v_stripped
        elif '\n' in v_stripped and re.match(r'^\d+(?:\,\d+)*\n\d+\.\d+$', v_stripped):
            avg_reviews_star_str = v_stripped
        elif '\n(' in v_stripped or (any(c.isalpha() for c in v_stripped) and not any(x in v_stripped for x in ['商品', 'FBA', 'AMZ', '$', '%'])):
            niche_raw = v_stripped

    if not niche_raw:
        idx_val = item.get('index', '')
        niche_val = item.get('niche', '')
        if niche_val.startswith('商品:'):
            niche_raw = idx_val
        elif idx_val.isdigit():
            niche_raw = niche_val
        else:
            niche_raw = niche_val if niche_val else idx_val

    en_name = clean_name(niche_raw)
    details = item.get('details', {})
    path = details.get('完整市场路径', '')
    
    if not return_rate_str:
        return_rate_str = item.get('returnRate', '')
    avg_return = 0.0
    match_ret = re.findall(r'([\d\.]+)%', return_rate_str)
    if match_ret:
        avg_return = float(match_ret[0])
        
    weight_str = details.get('平均重量', '')
    weight_lbs = 0.0
    match_w = re.search(r'([\d\.]+)\s*pounds', weight_str)
    if match_w:
        weight_lbs = float(match_w.group(1))
    else:
        match_kg = re.search(r'([\d\.]+)\s*g', weight_str)
        if match_kg:
            weight_lbs = float(match_kg.group(1)) / 453.59
            
    if not avg_reviews_star_str:
        avg_reviews_star_str = item.get('avgReviewsStar', '')
    reviews_val = 0
    if avg_reviews_star_str:
        first_line = avg_reviews_star_str.split('\n')[0].strip()
        first_line_clean = re.sub(r'[^\d]', '', first_line)
        if first_line_clean:
            reviews_val = int(first_line_clean)
            
    return en_name, path, avg_return, weight_lbs, reviews_val

# Scraper JS with header text dynamic mapping
js_scrape_code = """
(() => {
  const items = [];
  const table = document.querySelector('table#table-condition-search');
  if (!table) return JSON.stringify([]);
  
  const headers = Array.from(table.querySelectorAll('thead th')).map(th => th.innerText.trim());
  
  let keywordIdx = -1;
  let searchesIdx = -1;
  let purchasesIdx = -1;
  let clicksIdx = -1;
  let growthIdx = -1;
  let monopolyIdx = -1;
  let productsIdx = -1;
  let bidIdx = -1;
  let priceReviewsIdx = -1;
  
  headers.forEach((h, idx) => {
    if (h.includes('关键词')) keywordIdx = idx;
    else if (h.includes('搜索量')) searchesIdx = idx;
    else if (h.includes('购买量')) purchasesIdx = idx;
    else if (h.includes('点击量')) clicksIdx = idx;
    else if (h.includes('增长率') || h.includes('增速')) growthIdx = idx;
    else if (h.includes('集中度') || h.includes('占比') || h.includes('垄断')) monopolyIdx = idx;
    else if (h.includes('商品数') || h.includes('竞争')) productsIdx = idx;
    else if (h.includes('竞价') || h.includes('广告')) bidIdx = idx;
    else if (h.includes('价格') || h.includes('Review')) priceReviewsIdx = idx;
  });
  
  if (keywordIdx === -1) keywordIdx = 2;
  if (searchesIdx === -1) searchesIdx = 5;
  if (purchasesIdx === -1) purchasesIdx = 6;
  if (clicksIdx === -1) clicksIdx = 7;
  if (growthIdx === -1) growthIdx = 8;
  if (monopolyIdx === -1) monopolyIdx = 10;
  if (productsIdx === -1) productsIdx = 11;
  if (bidIdx === -1) bidIdx = 13;
  if (priceReviewsIdx === -1) priceReviewsIdx = 16;
  
  const rows = table.querySelectorAll('tbody tr');
  for (let i = 0; i < rows.length; i += 3) {
    const r1 = rows[i];
    const r2 = rows[i + 1];
    if (!r1 || !r2) continue;
    const cells = Array.from(r1.querySelectorAll('td')).map(td => td.innerText.trim());
    const details = r2.innerText.trim();
    
    items.push({
      index: cells[1] || '',
      keyword: cells[keywordIdx] || '',
      searches: cells[searchesIdx] || '',
      purchases: cells[purchasesIdx] || '',
      clicks: cells[clicksIdx] || '',
      growth: cells[growthIdx] || '',
      monopoly: cells[monopolyIdx] || '',
      products: cells[productsIdx] || '',
      bid: cells[bidIdx] || '',
      price_reviews: cells[priceReviewsIdx] || '',
      details: details
    });
  }
  return JSON.stringify(items);
})()
"""

def main():
    parser = argparse.ArgumentParser(description="Amazon Keyword Scan Script")
    parser.add_argument('--config', type=str, default='scripts/keyword_config.json', help='Path to configuration JSON')
    parser.add_argument('--market-config', type=str, default='scripts/market_config.json', help='Path to market config JSON for risk rules')
    parser.add_argument('--categories-json', type=str, default='', help='Path to category results JSON to pull seeds dynamically')
    parser.add_argument('--seeds', type=str, default='', help='Override seeds list, comma separated')
    parser.add_argument('--date', type=str, default='', help='Date override YYYY_MM_DD')
    
    args = parser.parse_args()
    date_str = args.date if args.date else datetime.date.today().strftime('%Y_%m_%d')
    
    # 1. Load config
    print("Loading config from " + args.config + "...")
    with open(args.config, 'r', encoding='utf-8') as f:
        config = json.load(f)
    keyword_params = config.get('filter_params', {})
    
    # Load market rules for classification
    rules = {}
    if os.path.exists(args.market_config):
        print("Loading market rules from " + args.market_config + "...")
        with open(args.market_config, 'r', encoding='utf-8') as f:
            market_config = json.load(f)
        rules = market_config.get('risk_rules', {})
    
    # 2. Extract seeds
    seeds = []
    if args.seeds:
        for s in args.seeds.split(','):
            term = s.strip()
            if term:
                seeds.append({"niche": term, "term": term})
    else:
        # Load from categories json if available
        json_path = args.categories_json
        if not json_path:
            json_path = f"/Users/zhoufan/Public/workspace/amazon/results/categories/market_scan_results_{date_str}.json"
            
        if os.path.exists(json_path):
            print("Extracting seeds dynamically from " + json_path + "...")
            with open(json_path, 'r', encoding='utf-8') as f:
                categories = json.load(f)
            for item in categories:
                en_name, path, avg_return, weight_lbs, reviews_val = parse_category_data(item)
                level = classify_niche(en_name, path, avg_return, weight_lbs, reviews_val, rules)
                # We only scan keywords for candidate niches (Green and Yellow)
                if level in ['green', 'yellow']:
                    term = get_seed_term(en_name)
                    if term and not any(s['term'] == term for s in seeds):
                        seeds.append({"niche": en_name, "term": term})
            print("Found " + str(len(seeds)) + " candidate niches to scan.")
        else:
            print("Warning: Categories results JSON not found at " + json_path)
            # Default fallbacks if no dynamic json exists
            for niche_en, seed in KNOWN_NICHE_SEEDS.items():
                seeds.append({"niche": niche_en, "term": seed})
            print("Loaded " + str(len(seeds)) + " fallback known seeds.")
            
    if not seeds:
        print("No seeds to scan. Exiting.")
        return
        
    print("Opening Keyword Research page...")
    run_opencli_cmd(["opencli", "browser", "ss", "open", "https://www.sellersprite.com/v2/keyword-research"])
    time.sleep(4)
    
    aggregated_results = []
    
    for item in seeds:
        niche = item["niche"]
        term = item["term"]
        print("\nScanning niche: '" + niche + "' using seed keyword: '" + term + "'...")
        
        # Prepare parameters to fill
        fill_params = {}
        for k, v in keyword_params.items():
            fill_params[k] = v
        fill_params["includeKeywords"] = term
        
        # Javascript form-filler
        fill_js = """
        (() => {
          // 1. Expand advanced options
          const toggle = document.querySelector('a[name=switchVisible]');
          if (toggle && toggle.innerText.includes('展开')) {
            toggle.click();
          }
          
          // 2. Reset other input elements to default/empty
          Array.from(document.querySelectorAll('input[name]')).forEach(input => {
            if (input.name !== 'station' && input.name !== 'order.field' && input.name !== 'order.desc') {
              input.value = '';
              input.dispatchEvent(new Event('input', { bubbles: true }));
            }
          });
          
          // 3. Fill parameters
          const params = """ + json.dumps(fill_params) + """
          Array.from(document.querySelectorAll('input[name]')).forEach(input => {
            if (params[input.name] !== undefined) {
              input.value = params[input.name];
              input.dispatchEvent(new Event('input', { bubbles: true }));
              input.dispatchEvent(new Event('change', { bubbles: true }));
            }
          });
          
          // 4. Submit
          const btn = document.querySelector('button[type=submit]');
          if (btn) {
            btn.click();
            return "submitted";
          }
          return "submit button not found";
        })()
        """
        
        res = run_opencli_cmd(["opencli", "browser", "ss", "eval", fill_js])
        time.sleep(5)
        
        # Wait for table to load
        loaded = False
        for attempt in range(5):
            eval_res = run_opencli_cmd(["opencli", "browser", "ss", "eval", "document.querySelectorAll('table#table-condition-search tbody tr').length"])
            try:
                output = eval_res.stdout.strip()
                num_str = "".join([c for c in output if c.isdigit()])
                row_count = int(num_str) if num_str else 0
                if row_count > 0:
                    loaded = True
                    break
            except Exception:
                pass
            time.sleep(2)
            
        if not loaded:
            print("No keyword search results loaded for seed: '" + term + "'")
            continue
            
        # Scrape page
        scrape_res = run_opencli_cmd(["opencli", "browser", "ss", "eval", js_scrape_code])
        if scrape_res.returncode == 0:
            try:
                output = scrape_res.stdout.strip()
                start_idx = output.find('[')
                end_idx = output.rfind(']')
                if start_idx != -1 and end_idx != -1:
                    json_str = output[start_idx:end_idx+1]
                    keywords = json.loads(json_str)
                    
                    for kw in keywords:
                        kw["target_niche"] = niche
                        kw["seed_term"] = term
                        
                    aggregated_results.extend(keywords)
                    print("Scraped " + str(len(keywords)) + " keywords for '" + niche + "'")
                else:
                    print("Could not parse JSON array from scraper output.")
            except Exception as e:
                print("Error parsing scraped output: ", e)
        else:
            print("Error running scraper: " + scrape_res.stderr)
            
    # Save aggregated JSON
    output_json = f"/Users/zhoufan/Public/workspace/amazon/results/keywords/keyword_scan_results_{date_str}.json"
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(aggregated_results, f, ensure_ascii=False, indent=2)
    print("\nSaved raw JSON to " + output_json)
    
    # Generate structured markdown report (no hardcoded reasoning)
    md = []
    md.append(f"# 亚马逊选产品：候选品类关键字扫描与分析报告 ({date_str.replace('_', '-')})\n")
    md.append("> [!IMPORTANT]")
    md.append(f"> 本报告基于配置文件 `scripts/market_config.json` 的 `keyword_filter_params` 对候选品类对应的关键字进行了全面扫描。")
    md.append(f"> 今日扫描配置规则：月搜索量 $\\ge {keyword_params.get('minSearches', 'N/A')}$，月购买量 $\\ge {keyword_params.get('minPurchases', 'N/A')}$，购买率 $\\ge {keyword_params.get('minPurchaseRate', 'N/A')}$%，最大垄断点击率 $\\le {keyword_params.get('maxMonopolyClickRate', 'N/A')}$%。")
    md.append("> 报告仅展示真实客观抓取的数据指标，供您直接导入大模型分析其市场深度与长尾词开发机会。\n")
    
    md.append("## 一、 各类目关联潜力关键字列表\n")
    
    # Group keywords by niche
    grouped = {}
    for kw in aggregated_results:
        niche = kw.get("target_niche", "Unknown")
        if niche not in grouped:
            grouped[niche] = []
        grouped[niche].append(kw)
        
    for niche, kw_list in grouped.items():
        md.append(f"### 📦 类目赛道：{niche} (共 {len(kw_list)} 个候选词)\n")
        md.append("| 序号 | 英文关键字 | 中文含义 / 详情 | 月搜索量 | 月购买量 (购买率) | 月点击量 | 点击集中度 | 竞争商品数 | 广告竞价 | 平均价格 / Reviews |")
        md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        for idx, k in enumerate(kw_list):
            kw_clean = k.get("keyword", "").replace('\n', ' ').strip()
            # Split out Chinese characters if any
            zh_trans = "".join(re.findall(r'[\u4e00-\u9fa5]+', kw_clean)).strip()
            en_kw = re.sub(r'[\u4e00-\u9fa5]+', '', kw_clean).strip()
            if not zh_trans:
                zh_trans = "-"
            
            # Helper to clean newlines in cell values (replace with <br> to preserve MD table structure)
            def clean_val(val):
                if not val:
                    return "-"
                return str(val).replace('\n', ' <br> ').strip()
            
            md.append(
                f"| {idx+1} | **{en_kw}** | {zh_trans} | "
                f"{clean_val(k.get('searches'))} | "
                f"{clean_val(k.get('purchases'))} | "
                f"{clean_val(k.get('clicks'))} | "
                f"{clean_val(k.get('monopoly'))} | "
                f"{clean_val(k.get('products'))} | "
                f"{clean_val(k.get('bid'))} | "
                f"{clean_val(k.get('price_reviews'))} |"
            )
        md.append("\n---\n")
        
    report_file = f"/Users/zhoufan/Public/workspace/amazon/results/keywords/keyword_scan_report_{date_str}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(md))
    print("Report successfully written to " + report_file)

if __name__ == "__main__":
    main()
