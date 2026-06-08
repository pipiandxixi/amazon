import json
import subprocess
import sys

def scrape_current_page(output_file):
    # Javascript code to extract table details
    js_code = """
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
      return JSON.stringify(items, null, 2);
    })()
    """
    
    # Execute opencli browser ss eval
    print("Executing Javascript scraper via opencli...")
    cmd = ["opencli", "browser", "ss", "eval", js_code]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error executing opencli command:", result.stderr)
        return False
        
    try:
        # The output of opencli browser ss eval is the raw string returned by JS
        # Let's clean the output (it might contain some shell warnings or opencli update notices at the end)
        output = result.stdout.strip()
        
        # Look for the JSON list array
        start_idx = output.find('[')
        end_idx = output.rfind(']')
        
        if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
            print("Could not find valid JSON array in output. Raw output:")
            print(output[:1000])
            return False
            
        json_str = output[start_idx:end_idx+1]
        data = json.loads(json_str)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully scraped {len(data)} keywords and saved to {output_file}")
        return True
    except Exception as e:
        print("Failed to parse output or save JSON:", e)
        print("Raw output sample:")
        print(result.stdout[:500])
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scrape_sellersprite.py <output_file>")
        sys.exit(1)
    scrape_current_page(sys.argv[1])
