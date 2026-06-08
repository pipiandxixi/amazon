import json
import subprocess
import time
import urllib.parse

# List of seed keywords for our recommended green niches
seeds = [
    {"niche": "Wood Burning Tools", "term": "wood burning"},
    {"niche": "Gaiters", "term": "gaiters"},
    {"niche": "Seat Covers", "term": "seat cover"},
    {"niche": "Alarms & Anti-Theft", "term": "motorcycle alarm"},
    {"niche": "Optics Accessories", "term": "scope mount"},
    {"niche": "Food Processor Parts & Accessories", "term": "food processor"},
    {"niche": "Car Rack Parts & Accessories", "term": "roof rack"},
    {"niche": "Fuel", "term": "fuel gauge"}
]

# Base URL with NO filters for targeted niche keyword extraction
base_url_template = (
    "https://www.sellersprite.com/v2/keyword-research?station=US&order.field=searches&order.desc=true"
    "&supplement=N&usestatic=R&exportGkImages=false&marketId=1&limitUserStatic=true&adminDes=N"
    "&presetMode=&itemImageRange=2&keywordBidMatchType=exact&month=202605"
    "&includeKeywords={include_kw}"
)

js_scrape_code = """
(() => {
  const items = [];
  const rows = document.querySelectorAll('table#table-condition-search tbody tr');
  for (let i = 0; i < rows.length; i += 3) {
    const r1 = rows[i];
    const r2 = rows[i + 1];
    if (!r1 || !r2) continue;
    const cells = Array.from(r1.querySelectorAll('td')).map(td => td.innerText.trim());
    const details = r2.innerText.trim();
    items.push({
      index: cells[1],
      keyword: cells[2],
      searches: cells[5],
      purchases: cells[6],
      clicks: cells[7],
      growth: cells[8],
      monopoly: cells[10],
      products: cells[11],
      bid: cells[13],
      price_reviews: cells[16],
      details: details
    });
  }
  return JSON.stringify(items);
})()
"""

def run_opencli_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def main():
    aggregated_results = []
    
    for item in seeds:
        niche = item["niche"]
        term = item["term"]
        encoded_term = urllib.parse.quote_plus(term)
        url = base_url_template.format(include_kw=encoded_term)
        
        print(f"\nTargeting Niche: '{niche}' with seed term: '{term}'")
        
        # 1. Open the URL
        print(f"Opening URL for '{term}'...")
        open_cmd = ["opencli", "browser", "ss", "open", url]
        run_opencli_cmd(open_cmd)
        time.sleep(3)
        
        # 2. Click the search button
        print("Clicking submit button...")
        click_cmd = ["opencli", "browser", "ss", "click", "--nth", "0", "button[type=submit]"]
        run_opencli_cmd(click_cmd)
        time.sleep(3)
        
        # 3. Wait for the table to load
        print("Waiting for results table...")
        loaded = False
        for attempt in range(5):
            eval_cmd = ["opencli", "browser", "ss", "eval", "document.querySelectorAll('table#table-condition-search tbody tr').length"]
            eval_res = run_opencli_cmd(eval_cmd)
            try:
                # Parse stdout
                output = eval_res.stdout.strip()
                # Find number
                num_str = "".join([c for c in output if c.isdigit()])
                row_count = int(num_str) if num_str else 0
                if row_count > 0:
                    print(f"Table loaded with {row_count} rows ({row_count // 3} items)")
                    loaded = True
                    break
            except Exception as e:
                pass
            time.sleep(2)
            
        if not loaded:
            print(f"No results found or table did not load for seed: '{term}'")
            continue
            
        # 4. Scrape the data
        print("Scraping results...")
        scrape_cmd = ["opencli", "browser", "ss", "eval", js_scrape_code]
        scrape_res = run_opencli_cmd(scrape_cmd)
        
        if scrape_res.returncode == 0:
            try:
                output = scrape_res.stdout.strip()
                start_idx = output.find('[')
                end_idx = output.rfind(']')
                if start_idx != -1 and end_idx != -1:
                    json_str = output[start_idx:end_idx+1]
                    keywords = json.loads(json_str)
                    
                    # Annotate keywords with the target niche
                    for kw in keywords:
                        kw["target_niche"] = niche
                        kw["seed_term"] = term
                        
                    aggregated_results.extend(keywords)
                    print(f"Scraped {len(keywords)} matching keywords for '{niche}'")
                else:
                    print("Invalid JSON returned by scraper.")
            except Exception as e:
                print("Error parsing scraped data:", e)
        else:
            print("Error running scraper:", scrape_res.stderr)
            
    # Save aggregated results
    output_file = "/Users/zhoufan/Public/workspace/amazon/results/keyword_results_targeted_2026_06_08.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(aggregated_results, f, ensure_ascii=False, indent=2)
        
    print(f"\nDone! Aggregated {len(aggregated_results)} keywords across all niches and saved to {output_file}")

if __name__ == "__main__":
    main()
