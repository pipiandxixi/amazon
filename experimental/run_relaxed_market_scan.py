import json
import subprocess
import time
import re

relaxed_params = {
    "minAvgSales": "100",
    "maxAvgSales": "10000",
    "minAvgPrice": "20.0",
    "maxAvgPrice": "",
    "minTotalProducts": "50",
    "maxAvgSellers": "60.0",
    "maxHeadListingBrandCrn": "65.0",
    "maxHeadListingSellerCrn": "65.0",
    "maxAmzRatio": "25.0",
    "minNewRatio": "10.0",
    "maxNewAvgRating": "4.5",
    "maxAvgWeight": "3.0",
    "maxAvgVolume": "800",
    "minAvgProfit": "50.0",
    "maxAvgReviews": "1200"
}

fill_form_js = f"""
(() => {{
  // 1. Expand advanced options
  const toggle = document.querySelector('a[name=switchVisible]');
  if (toggle && toggle.innerText.includes('展开')) {{
    toggle.click();
  }}
  
  // 2. Fill parameters
  const params = {json.dumps(relaxed_params)};
  Array.from(document.querySelectorAll('input[name]')).forEach(input => {{
    if (params[input.name] !== undefined) {{
      input.value = params[input.name];
      input.dispatchEvent(new Event('input', {{ bubbles: true }}));
      input.dispatchEvent(new Event('change', {{ bubbles: true }}));
    }}
  }});
  
  // 3. Click submit
  const btn = document.querySelector('button[type=submit]');
  if (btn) {{
    btn.click();
    return "submitted";
  }}
  return "submit button not found";
}})()
"""

scrape_page_js = """
(() => {
const items = [];
const rows = document.querySelectorAll('#table-condition-search tbody tr');
for (let i = 0; i < rows.length; i += 3) {
  const r1 = rows[i];
  const r2 = rows[i + 1];
  if (!r1 || !r2) continue;
  const cells = Array.from(r1.querySelectorAll('td')).map(td => td.innerText.trim());
  const details = r2.innerText.trim();
  
  const getVal = (str, label, nextLabels) => {
    const start = str.indexOf(label);
    if (start === -1) return '';
    let end = str.length;
    for (const nextLabel of nextLabels) {
      const idx = str.indexOf(nextLabel, start + label.length);
      if (idx !== -1 && idx < end) {
        end = idx;
      }
    }
    return str.substring(start + label.length, end).trim();
  };
  
  const labels = [
    '完整市场路径:', '市场路径(中文):', 'A+数量占比:', '新品平均评分数:',
    '新品平均价格:', '新品平均星级:', '新品月均销量:', '新品月均销售额:',
    '平均重量:', '平均体积:', '平均毛利率:', '卖家所属地:', '搜索购买比:'
  ];
  
  const parsedDetails = {};
  for (let j = 0; j < labels.length; j++) {
    const key = labels[j].replace(':', '');
    const val = getVal(details, labels[j], labels.filter((_, idx) => idx !== j));
    parsedDetails[key] = val;
  }
  
  items.push({
    index: cells[1],
    niche: cells[2],
    sampleSize: cells[3],
    monthlySales: cells[4],
    avgSales: cells[5],
    avgRevenue: cells[6],
    avgReviewsStar: cells[7],
    avgBsr: cells[8],
    avgSellersPrice: cells[9],
    sellerType: cells[10],
    concentration: cells[11],
    newCountRatio: cells[12],
    totalProducts: cells[13],
    returnRate: cells[14],
    details: parsedDetails
  });
}
return JSON.stringify(items);
})()
"""

def run_opencli_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def main():
    print("Opening Market Research page...")
    run_opencli_cmd(["opencli", "browser", "ss", "open", "https://www.sellersprite.com/v2/market-research"])
    time.sleep(4)
    
    print("Filling form and submitting search...")
    res = run_opencli_cmd(["opencli", "browser", "ss", "eval", fill_form_js])
    print("Submission status:", res.stdout.strip())
    time.sleep(6)
    
    # Let's scrape multiple pages to get 100+ categories
    all_categories = []
    
    for page in range(1, 6): # Up to 5 pages
        print(f"\nScraping page {page}...")
        
        # Wait a moment for page table to render
        time.sleep(2)
        
        # Scrape page
        scrape_res = run_opencli_cmd(["opencli", "browser", "ss", "eval", scrape_page_js])
        if scrape_res.returncode != 0:
            print("Error running scraper:", scrape_res.stderr)
            break
            
        output = scrape_res.stdout.strip()
        start_idx = output.find('[')
        end_idx = output.rfind(']')
        if start_idx != -1 and end_idx != -1:
            json_str = output[start_idx:end_idx+1]
            page_items = json.loads(json_str)
            print(f"Scraped {len(page_items)} categories on page {page}")
            if len(page_items) == 0:
                print("No items found on this page, stopping pagination.")
                break
            all_categories.extend(page_items)
        else:
            print("Scraper output did not contain valid JSON.")
            print(output[:500])
            break
            
        if len(all_categories) >= 110:
            print(f"Reached {len(all_categories)} categories, stopping.")
            break
            
        # Click next page button
        # In Sellersprite, the pagination next page is usually an element with class `.btn-next` or similar, or `li.number + li:not(.disabled) a`
        # Let's check how many elements matches button next or click pager
        print("Clicking next page...")
        # Let's click the next button by evaluating JS to click pager next
        click_next_js = """
        (() => {
          const nextBtn = document.querySelector('button.btn-next') || document.querySelector('.pagination .next a') || document.querySelector('.pagination li:last-child a');
          if (nextBtn) {
            nextBtn.click();
            return "clicked";
          }
          return "not found";
        })()
        """
        click_res = run_opencli_cmd(["opencli", "browser", "ss", "eval", click_next_js])
        print("Click next status:", click_res.stdout.strip())
        time.sleep(4)
        
    output_file = "/Users/zhoufan/Public/workspace/amazon/results/relaxed_one_hundred_categories_2026_06_08.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_categories, f, ensure_ascii=False, indent=2)
        
    print(f"\nDone! Successfully collected {len(all_categories)} categories and saved to {output_file}")

if __name__ == "__main__":
    main()
