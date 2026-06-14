import json
import re
import time
import datetime
import argparse
from pathlib import Path

from scan_common import OpenCliError, check_browser_ready, dated_results_dir, eval_browser, open_browser

def values(section):
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }

def clean_name(niche_str):
    if not niche_str:
        return ""
    name = niche_str.replace('\n', ' ').strip()
    return re.sub(r'\s*\(.*?\)\s*', '', name).strip()

def extract_zh_name(niche_str):
    if not niche_str:
        return ""
    match = re.search(r'\((.*?)\)', niche_str)
    return match.group(1).strip() if match else ''

def select_departments_market(department_label: str) -> None:
    """Set the departmentKeyword input to filter results to one top-level department.

    The v2 market research page uses a text input (name=departmentKeyword) rather
    than checkboxes. Setting this field before form submission restricts results to
    sub-categories within that department.
    """
    if not department_label:
        return
    js = f"""
    (() => {{
      const input = document.querySelector('input[name="departmentKeyword"]');
      if (!input) return JSON.stringify({{error: 'departmentKeyword input not found'}});
      input.value = {json.dumps(department_label)};
      input.dispatchEvent(new Event('input', {{ bubbles: true }}));
      input.dispatchEvent(new Event('change', {{ bubbles: true }}));
      return JSON.stringify({{set: input.value}});
    }})()
    """
    result = eval_browser(js)
    print(f"  Department filter: {result}")


def _load_config(config_source):
    if isinstance(config_source, dict):
        return config_source
    with open(config_source, 'r', encoding='utf-8') as f:
        return json.load(f)


def scrape_market(config_source, department_label=None):
    """Scrape the SellerSprite market research page and return raw category items.

    department_label: optional department name string (e.g. "Sports & Outdoors") to
    pre-filter the page via the departmentKeyword input before form submission. When
    None or empty, all departments are included (default SellerSprite behaviour).
    """
    print("Loading market configuration...")
    config = _load_config(config_source)
    params = values(config['filter_params'])
    scan_policy = values(config.get('scan_policy', {}))
    max_pages = int(scan_policy.get('max_pages', 5))

    print("Opening Market Research page...")
    open_browser("https://www.sellersprite.com/v2/market-research")
    time.sleep(4)

    # Pre-filter by department before submitting the search form
    if department_label:
        print(f"  Filtering by department: {department_label}")
        select_departments_market(department_label)
        time.sleep(1)
    
    # Generate form fill JS
    fill_form_js = """
    (() => {
      // 1. Expand advanced options
      const toggle = document.querySelector('a[name=switchVisible]');
      if (toggle && toggle.innerText.includes('展开')) {
        toggle.click();
      }
      
      // 2. Fill parameters
      const params = """ + json.dumps(params) + """
      Array.from(document.querySelectorAll('input[name]')).forEach(input => {
        if (params[input.name] !== undefined) {
          input.value = params[input.name];
          input.dispatchEvent(new Event('input', { bubbles: true }));
          input.dispatchEvent(new Event('change', { bubbles: true }));
        }
      });
      
      // 3. Click submit
      const btn = document.querySelector('button[type=submit]');
      if (btn) {
        btn.click();
        return "submitted";
      }
      return "submit button not found";
    })()
    """
    
    print("Filling form and submitting search...")
    res = eval_browser(fill_form_js)
    print("Submission status:", res)
    time.sleep(6)
    
    # Scrape JS using cell auto-detection logic
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
      
      let index = '';
      let niche = '';
      let sampleSize = '';
      let monthlySales = '';
      let avgSales = '';
      let avgRevenue = '';
      let avgReviewsStar = '';
      let avgBsr = '';
      let avgSellersPrice = '';
      let sellerType = '';
      let concentration = '';
      let newCountRatio = '';
      let totalProducts = '';
      let returnRate = '';
      
      cells.forEach((cell, idx) => {
        if (!cell) return;
        
        // 1. Index
        if (/^\\d+$/.test(cell) && parseInt(cell) <= 100 && idx <= 1) {
          index = cell;
          return;
        }
        
        // 2. Sample size
        if (cell.includes('商品:') && cell.includes('品牌:') && !cell.includes('%')) {
          sampleSize = cell;
          return;
        }
        
        // 3. Concentration
        if (cell.includes('商品:') && cell.includes('品牌:') && cell.includes('%')) {
          concentration = cell;
          return;
        }
        
        // 4. Seller type
        if (cell.includes('FBA:') || cell.includes('AMZ:') || cell.includes('FBM:')) {
          sellerType = cell;
          return;
        }
        
        // 5. Return rate
        if (cell.includes('%') && cell.includes('\\n') && !cell.includes('FBA') && !cell.includes('商品')) {
          returnRate = cell;
          return;
        }
        
        // 6. New count ratio
        if (cell.includes('%') && (cell.includes('\\n') || cell.length < 10) && !returnRate && !sellerType && !concentration) {
          newCountRatio = cell;
          return;
        }
        
        // 7. Average price
        if (cell.includes('$')) {
          avgSellersPrice = cell;
          return;
        }
        
        // 8. Niche name
        if (/\\n\\(.*?\\)/.test(cell) || (/[a-zA-Z]/.test(cell) && /[\\u4e00-\\u9fa5]/.test(cell))) {
          niche = cell;
          return;
        }
        
        // 9. Average sales
        if (/\\(\\d+(\\.\\d+)?\\)/.test(cell)) {
          avgSales = cell;
          return;
        }
        
        // 10. Average reviews & star
        if (cell.includes('\\n') && /^\\d+(\\,\\d+)*\\n\\d+\\.\\d+$/.test(cell)) {
          avgReviewsStar = cell;
          return;
        }
        
        // 11. Average revenue
        if (cell.includes('\\n') && /^\\d+(\\,\\d+)*\\n\\d+(\\,\\d+)*$/.test(cell)) {
          avgRevenue = cell;
          return;
        }
        
        // 12. Average BSR
        if (cell.includes('\\n') && !avgRevenue && !avgReviewsStar && !avgSales && !avgSellersPrice) {
          avgBsr = cell;
          return;
        }
        
        // 13. Total products
        if (/^\\d+(\\,\\d+)*$/.test(cell) && !index) {
          totalProducts = cell;
          return;
        }
        
        // 14. Monthly sales
        if (/^\\d+(\\,\\d+)*$/.test(cell) && !totalProducts && !index) {
          monthlySales = cell;
          return;
        }
      });
      
      if (!niche) {
        niche = cells[2] || cells[1] || '';
      }
      
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
        index: index || (items.length + 1).toString(),
        niche: niche,
        sampleSize: sampleSize,
        monthlySales: monthlySales,
        avgSales: avgSales,
        avgRevenue: avgRevenue,
        avgReviewsStar: avgReviewsStar,
        avgBsr: avgBsr,
        avgSellersPrice: avgSellersPrice,
        sellerType: sellerType,
        concentration: concentration,
        newCountRatio: newCountRatio,
        totalProducts: totalProducts,
        returnRate: returnRate,
        details: parsedDetails
      });
    }
    return JSON.stringify(items);
    })()
    """
    
    all_categories = []
    seen_pages = set()
    scan_meta = {
        "pages_scanned": 0,
        "stop_reason": "",
        "possible_truncation": False,
        "reported_total": None,
        "free_limit_message": False,
    }
    
    for page in range(1, max_pages + 1):
        print(f"\nScraping page {page}...")
        time.sleep(2)
        
        output = eval_browser(scrape_page_js)
        start_idx = output.find('[')
        end_idx = output.rfind(']')
        if start_idx != -1 and end_idx != -1:
            json_str = output[start_idx:end_idx+1]
            page_items = json.loads(json_str)
            print(f"Scraped {len(page_items)} categories on page {page}")
            if len(page_items) == 0:
                print("No items found on this page, stopping pagination.")
                scan_meta["stop_reason"] = "页面未返回类目"
                break
            page_signature = json.dumps(page_items, ensure_ascii=False, sort_keys=True)
            if page_signature in seen_pages:
                print("Page content repeated, stopping pagination to avoid duplicate results.")
                scan_meta["stop_reason"] = "下一页内容重复"
                break
            seen_pages.add(page_signature)
            scan_meta["pages_scanned"] = page
            known_items = {json.dumps(item, ensure_ascii=False, sort_keys=True) for item in all_categories}
            all_categories.extend(
                item for item in page_items
                if json.dumps(item, ensure_ascii=False, sort_keys=True) not in known_items
            )
        else:
            print("Scraper output did not contain valid JSON.")
            scan_meta["stop_reason"] = "页面未返回有效 JSON"
            break
            
        print("Clicking next page...")
        click_next_js = """
        (() => {
          const nextBtn = document.querySelector('button.btn-next') || document.querySelector('.pagination .next a') || document.querySelector('.pagination li:last-child a');
          if (nextBtn) {
            const parent = nextBtn.closest('li, button');
            const disabled = nextBtn.disabled
              || nextBtn.getAttribute('aria-disabled') === 'true'
              || parent?.classList.contains('disabled');
            if (disabled) return "disabled";
            nextBtn.click();
            return "clicked";
          }
          return "not found";
        })()
        """
        click_res = eval_browser(click_next_js)
        print("Click next status:", click_res)
        if "not found" in click_res or "disabled" in click_res:
            scan_meta["stop_reason"] = "已到最后一页"
            break
        time.sleep(4)
        
    print(f"\nDone! Successfully collected {len(all_categories)} categories.")
    completeness_output = eval_browser(
        """
        (() => {
          const text = document.body.innerText;
          const total = text.match(/找到的细分行业\\s*[:：]\\s*([\\d,]+)/);
          return JSON.stringify({
            reported_total: total ? Number(total[1].replaceAll(',', '')) : null,
            free_limit_message: text.includes('升级套餐后可查看全部')
          });
        })()
        """
    )
    completeness = json.loads(
        completeness_output[completeness_output.find("{"):completeness_output.rfind("}") + 1]
    )
    scan_meta.update(completeness)
    if scan_meta["free_limit_message"] or (
        scan_meta["reported_total"] is not None
        and scan_meta["reported_total"] > len(all_categories)
    ):
        scan_meta["possible_truncation"] = True
        scan_meta["stop_reason"] = (
            f"免费套餐仅展示 {len(all_categories)} 个，页面提示共有 "
            f"{scan_meta['reported_total'] or '更多'} 个类目"
        )
    if not scan_meta["stop_reason"]:
        scan_meta["stop_reason"] = "扫描正常结束"
    return all_categories, scan_meta

def generate_report(
    config_source, categories, date_str, output_dir=None, scan_meta=None,
    return_candidates=False, write_report_file=True,
):
    config_label = config_source if isinstance(config_source, str) else "unified pipeline config"
    print(f"Generating market report using configuration rules from {config_label}...")
    config = _load_config(config_source)
    rules = {
        level: values(rule)
        for level, rule in config['risk_rules'].items()
    }
    scan_policy = values(config.get('scan_policy', {}))
        
    scored_categories = []
    for item in categories:
        # Robust Python value auto-detection logic
        all_vals = []
        for k, v in item.items():
            if k != 'details' and isinstance(v, str):
                all_vals.append((k, v))
                
        niche_raw = ""
        sample_size_str = ""
        avg_sales_str = ""
        avg_revenue_str = ""
        avg_reviews_star_str = ""
        avg_price_str = ""
        seller_type_str = ""
        concentration_str = ""
        return_rate_str = ""
        
        for k, v in all_vals:
            v_stripped = v.strip()
            if not v_stripped:
                continue
            # Sample size
            if '商品:' in v_stripped and '品牌:' in v_stripped and '%' not in v_stripped:
                sample_size_str = v_stripped
            # Concentration
            elif '商品:' in v_stripped and '品牌:' in v_stripped and '%' in v_stripped:
                concentration_str = v_stripped
            # Seller type
            elif 'FBA:' in v_stripped or 'AMZ:' in v_stripped or 'FBM:' in v_stripped:
                seller_type_str = v_stripped
            # Return rate
            elif '%' in v_stripped and '\n' in v_stripped and 'FBA' not in v_stripped and '商品' not in v_stripped:
                return_rate_str = v_stripped
            # Price
            elif '$' in v_stripped:
                avg_price_str = v_stripped
            # Avg sales
            elif re.search(r'\(\d+(\.\d+)?\)', v_stripped):
                avg_sales_str = v_stripped
            # Avg reviews & star
            elif '\n' in v_stripped and re.match(r'^\d+(?:\,\d+)*\n\d+\.\d+$', v_stripped):
                avg_reviews_star_str = v_stripped
            # Avg revenue
            elif '\n' in v_stripped and re.match(r'^\d+(?:\,\d+)*\n\d+(?:\,\d+)*$', v_stripped):
                avg_revenue_str = v_stripped
            # Niche name
            elif '\n(' in v_stripped or (any(c.isalpha() for c in v_stripped) and not any(x in v_stripped for x in ['商品', 'FBA', 'AMZ', '$', '%'])):
                niche_raw = v_stripped

        # Fallbacks to direct keys if auto-detection was not matched
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
        zh_name = extract_zh_name(niche_raw)
        
        details = item.get('details', {})
        path = details.get('完整市场路径', '')
        zh_path = details.get('市场路径(中文)', '')
        
        # Parse return rate from returnRate
        if not return_rate_str:
            return_rate_str = item.get('returnRate', '')
        avg_return = 0.0
        match_ret = re.findall(r'([\d\.]+)%', return_rate_str)
        if match_ret:
            avg_return = float(match_ret[0])
            
        # Parse weight — SellerSprite returns "X pounds" or "X lbs"; grams as fallback
        weight_str = details.get('平均重量', '')
        weight_lbs = 0.0
        match_w = re.search(r'([\d\.]+)\s*(?:pounds|lbs)', weight_str)
        if match_w:
            weight_lbs = float(match_w.group(1))
        else:
            match_g = re.search(r'([\d\.]+)\s*g(?:rams?)?', weight_str)
            if match_g:
                weight_lbs = float(match_g.group(1)) / 453.59
            
        # Parse price
        if not avg_price_str:
            avg_price_str = item.get('avgSellersPrice', '')
        price_val = 0.0
        match_p = re.search(r'\$\s*([\d\.,]+)', avg_price_str)
        if match_p:
            price_val = float(match_p.group(1).replace(',', ''))
        else:
            p_str_detail = details.get('新品平均价格', '')
            match_pd = re.search(r'\$\s*([\d\.,]+)', p_str_detail)
            if match_pd:
                price_val = float(match_pd.group(1).replace(',', ''))
            
        # Parse reviews
        if not avg_reviews_star_str:
            avg_reviews_star_str = item.get('avgReviewsStar', '')
        reviews_val = 0
        if avg_reviews_star_str:
            first_line = avg_reviews_star_str.split('\n')[0].strip()
            first_line_clean = re.sub(r'[^\d]', '', first_line)
            if first_line_clean:
                reviews_val = int(first_line_clean)
            
        # Parse profit margin
        profit_val = 0.0
        profit_str = details.get('平均毛利率', '')
        match_pr = re.search(r'([\d\.]+)%', profit_str)
        if match_pr:
            profit_val = float(match_pr.group(1))
            
        # Parse concentration
        if not concentration_str:
            concentration_str = item.get('concentration', '')
        brand_conc = 0.0
        match_bc = re.search(r'品牌:\s*([\d\.]+)%', concentration_str)
        if match_bc:
            brand_conc = float(match_bc.group(1))
            
        # Parse Chinese seller ratio
        seller_loc = details.get('卖家所属地', '')
        cn_ratio = 0.0
        match_cn = re.search(r'中国\|([\d\.]+)%', seller_loc)
        if match_cn:
            cn_ratio = float(match_cn.group(1))
        else:
            match_us = re.search(r'美国\|([\d\.]+)%', seller_loc)
            if match_us:
                cn_ratio = 100.0 - float(match_us.group(1))
                
        # Risk classification
        level = '🟢 Green (Recommended)'
        red_reasons = []
        
        red_rules = rules['red']
        if avg_return > red_rules['max_return_rate']:
            red_reasons.append(f"退货率过高 (>{red_rules['max_return_rate']}%)")
        if weight_lbs > red_rules['max_weight_lbs']:
            red_reasons.append(f"重量超标 (>{red_rules['max_weight_lbs']} lbs)")
        if reviews_val > red_rules['max_reviews']:
            red_reasons.append(f"Review护城河太深 (>{red_rules['max_reviews']})")
        if any(x in en_name for x in red_rules['excluded_keywords']):
            red_reasons.append("排除类关键字过滤")
        allowed_path_kw = red_rules.get('allowed_path_keywords', [])
        if any(x in path for x in red_rules['excluded_paths']):
            # Check allowlist against sub-category segments only (skip top-level dept name)
            sub_segments = [s.strip() for s in path.split('›')][1:]
            path_allowed = any(x in seg for x in allowed_path_kw for seg in sub_segments)
            if not path_allowed:
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
            if any(x in en_name for x in yellow_rules['excluded_keywords']):
                yellow_reasons.append("带电/合规资质敏感关键字")
            
        if red_reasons:
            level = '🔴 Red (Avoid)'
        elif yellow_reasons:
            level = '🟡 Yellow (Cautious)'
            
        scored_categories.append({
            'en_name': en_name,
            'zh_name': zh_name,
            'path': path,
            'zh_path': zh_path,
            'price': price_val,
            'reviews': reviews_val,
            'weight': weight_lbs,
            'return_rate': avg_return,
            'brand_conc': brand_conc,
            'cn_ratio': cn_ratio,
            'level': level,
            'red_reasons': red_reasons,
            'yellow_reasons': yellow_reasons,
            'profit': profit_val,
            'details': details
        })
        
    green_niches = [c for c in scored_categories if c['level'] == '🟢 Green (Recommended)']
    yellow_niches = [c for c in scored_categories if c['level'] == '🟡 Yellow (Cautious)']
    red_niches = [c for c in scored_categories if c['level'] == '🔴 Red (Avoid)']
    
    print(f"Scored categories: {len(green_niches)} Green, {len(yellow_niches)} Yellow, {len(red_niches)} Red")
    candidate_count = len(green_niches) + len(yellow_niches)
    target_min = int(scan_policy.get('target_candidate_min', 8))
    target_max = int(scan_policy.get('target_candidate_max', 15))
    if candidate_count > target_max:
        threshold_advice = (
            f"当前候选类目有 {candidate_count} 个，超过目标上限 {target_max}。"
            "建议提高基础过滤门槛或收紧黄色/绿色风控规则，而不是截断为固定 Top-K。"
        )
    elif candidate_count < target_min:
        threshold_advice = (
            f"当前候选类目仅有 {candidate_count} 个，低于目标下限 {target_min}。"
            "建议适度放宽基础过滤门槛，并保留风险规则作为最终约束。"
        )
    else:
        threshold_advice = f"当前候选类目有 {candidate_count} 个，位于目标区间 {target_min}-{target_max}。"
    
    # Generate Markdown Report (no hardcoded/arbitrary reasonings)
    md = []
    md.append(f"# 亚马逊选市场扫描与评估报告 ({date_str.replace('_', '-')})\n")
    md.append("> [!IMPORTANT]")
    md.append(f"> 本报告基于 `{config_label}` 中设定的过滤与风控规则进行生成。今日共分析了 **{len(categories)}** 个符合基本条件的子类目，其中最终筛选出 **{len(green_niches)}** 个适合新手的 🟢 绿色推荐赛道。")
    if scan_meta:
        md.append(
            f"> **抓取完整性**：扫描 **{scan_meta['pages_scanned']}** 页；"
            f"页面总数提示：**{scan_meta['reported_total'] if scan_meta['reported_total'] is not None else '未识别'}**；"
            f"停止原因：{scan_meta['stop_reason']}；"
            f"免费套餐截断风险：**{'可能存在' if scan_meta['possible_truncation'] else '未检测到'}**。"
        )
    md.append(f"> **数量审计**：{threshold_advice}")
    md.append("> 本报告仅输出真实抓取的指标数据，没有任何人工猜测或硬编码的推荐理由。您可以直接复制本报告的详细数据到大模型中，让其结合具体品类特性为您分析入选原因及每个指标的指导含义。\n")
    
    md.append("## 一、 风控分类结果概览\n")
    md.append(f"- **绿色通道 (推荐) 🟢**：共 **{len(green_niches)}** 个。满足所有风控参数，建议重点关注。")
    md.append(f"- **黄色通道 (谨慎) 🟡**：共 **{len(yellow_niches)}** 个。包含带电电子产品或物理退货率偏高的类目，建议深入调研。")
    md.append(f"- **红色通道 (避坑) 🔴**：共 **{len(red_niches)}** 个。触发硬风控规则，已自动排除。\n")
    
    md.append("## 二、 推荐与候选子类目核心列表\n")
    md.append("### 1. 🟢 绿色推荐类目\n")
    md.append("| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 品牌集中度 | 中国卖家比例 |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for idx, c in enumerate(green_niches):
        md.append(f"| {idx+1} | **{c['en_name']}** | {c['zh_name']} | ${c['price']:.2f} | {c['reviews']} | {c['weight']:.2f} lbs | {c['return_rate']}% | {c['brand_conc']}% | {c['cn_ratio']}% |")
        
    md.append("\n### 2. 🟡 黄色候选类目\n")
    md.append("| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 平均Reviews | 物理重量 | 退货率 | 触发警示规则 |")
    md.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
    for idx, c in enumerate(yellow_niches):
        reasons_str = ", ".join(c['yellow_reasons'])
        md.append(f"| {idx+1} | **{c['en_name']}** | {c['zh_name']} | ${c['price']:.2f} | {c['reviews']} | {c['weight']:.2f} lbs | {c['return_rate']}% | {reasons_str} |")

    md.append("\n### 3. 🔴 红色排除类目摘要\n")
    md.append("| 序号 | 子类目英文名 | 中文名 / 路径 | 平均价格 | 排除原因 |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")
    for idx, c in enumerate(red_niches):
        reasons_str = ", ".join(c['red_reasons'])
        md.append(f"| {idx+1} | **{c['en_name']}** | {c['zh_name']} | ${c['price']:.2f} | {reasons_str} |")
        
    md.append("\n## 三、 候选类目详细数据指标画像 (供大模型分析使用)\n")
    md.append("以下为入选的绿色与黄色子类目的完整数据指标。您可以将这些数据输入大模型（如 Gemini、Claude），让其结合具体品类特性进行深入的入选原因、产品特征及商业机会评估。\n")
    
    md.append("### 🟢 绿色类目详情列表\n")
    for idx, c in enumerate(green_niches):
        md.append(f"#### 🏆 🟢-{idx+1}. {c['en_name']} ({c['zh_name']})\n")
        md.append(f"- **完整市场路径**：`{c['path']}`")
        md.append("- **核心数据特征**：")
        md.append(f"  *   **平均客单价 (Avg Price)**：`${c['price']:.2f}`")
        md.append(f"  *   **平均 Reviews (Avg Reviews)**：`{c['reviews']} 个`")
        md.append(f"  *   **物理重量 (Weight)**：`{c['weight']:.2f} lbs`")
        md.append(f"  *   **平均退货率 (Return Rate)**：`{c['return_rate']}%`")
        md.append(f"  *   **平均毛利率 (Profit Margin)**：`{c['profit']}%`")
        md.append(f"  *   **品牌集中度 (Brand Concentration)**：`{c['brand_conc']}%`")
        md.append(f"  *   **中国卖家比例 (Chinese Seller Ratio)**：`{c['cn_ratio']}%`")
        
        md.append("- **Sellersprite 抓取原始细节 (Scraped Details)**：")
        for key, val in c['details'].items():
            val_clean = val.replace('\n', ' ').strip()
            md.append(f"  *   **{key}**：`{val_clean}`")
        md.append("\n---\n")

    md.append("### 🟡 黄色类目详情列表\n")
    for idx, c in enumerate(yellow_niches):
        md.append(f"#### 🏆 🟡-{idx+1}. {c['en_name']} ({c['zh_name']})\n")
        md.append(f"- **完整市场路径**：`{c['path']}`")
        md.append(f"- **触发警示项**：`{', '.join(c['yellow_reasons'])}`")
        md.append("- **核心数据特征**：")
        md.append(f"  *   **平均客单价 (Avg Price)**：`${c['price']:.2f}`")
        md.append(f"  *   **平均 Reviews (Avg Reviews)**：`{c['reviews']} 个`")
        md.append(f"  *   **物理重量 (Weight)**：`{c['weight']:.2f} lbs`")
        md.append(f"  *   **平均退货率 (Return Rate)**：`{c['return_rate']}%`")
        md.append(f"  *   **平均毛利率 (Profit Margin)**：`{c['profit']}%`")
        md.append(f"  *   **品牌集中度 (Brand Concentration)**：`{c['brand_conc']}%`")
        md.append(f"  *   **中国卖家比例 (Chinese Seller Ratio)**：`{c['cn_ratio']}%`")
        
        md.append("- **Sellersprite 抓取原始细节 (Scraped Details)**：")
        for key, val in c['details'].items():
            val_clean = val.replace('\n', ' ').strip()
            md.append(f"  *   **{key}**：`{val_clean}`")
        md.append("\n---\n")
        
    # Explicit output directories keep pipeline behavior. Standalone runs always
    # write below results/YYYY_MM_DD/ instead of the results root.
    out = Path(output_dir) if output_dir else dated_results_dir(date_str)
    out.mkdir(parents=True, exist_ok=True)
    json_dir = out / "json"
    json_dir.mkdir(parents=True, exist_ok=True)
    report_file = out / "market_scan_report.md"
    sidecar_file = json_dir / "market_scan_results.json"

    market_content = "\n".join(md)
    if write_report_file:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(market_content)
        print(f"Report successfully written to {report_file}")

    def _clean_path(raw: str) -> str:
        # Strip scraping artifact " 市场分析" appended by SellerSprite market page
        # Normalize › (U+203A) to > so downstream code can split consistently
        path = re.sub(r'\s*市场分析\s*$', '', raw).strip()
        return path.replace('›', '>')

    category_map: dict = config.get("category_map", {})

    def _to_sidecar(c: dict) -> dict:
        clean = _clean_path(c["path"])
        parts = [s.strip() for s in re.split(r'[>›]', clean) if s.strip()]
        top_level = parts[0] if parts else ""
        mapping = category_map.get(top_level)
        dept = mapping.get("department") if mapping else None
        return {
            "en_name": c["en_name"], "zh_name": c["zh_name"],
            "path": clean, "level": c["level"],
            "price": c.get("price"), "reviews": c.get("reviews"),
            "weight_lbs": c.get("weight"), "return_rate": c.get("return_rate"),
            "brand_conc": c.get("brand_conc"), "cn_ratio": c.get("cn_ratio"),
            "product_path": parts,
            "departments": [int(dept)] if dept is not None else [],
        }

    sidecar_items = [_to_sidecar(c) for c in green_niches + yellow_niches]
    with open(sidecar_file, 'w', encoding='utf-8') as f:
        json.dump(sidecar_items, f, ensure_ascii=False, indent=2)
    print(f"JSON sidecar written to {sidecar_file}")
    if return_candidates:
        return market_content, sidecar_items
    return market_content

def main():
    parser = argparse.ArgumentParser(description="Amazon Market Research Selection Script")
    parser.add_argument('--config', type=str, default='scripts/market_config.json',
                        help='Path to configuration JSON')
    parser.add_argument('--date', type=str, default='', help='Date format YYYY_MM_DD')
    parser.add_argument('--output-dir', type=str, default='', dest='output_dir',
                        help='Directory to write report and sidecar (pipeline mode); '
                             'defaults to results/YYYY_MM_DD/')
    parser.add_argument('--departments', nargs='*', default=[], metavar='DEPT',
                        help='Top-level Amazon category names to pre-filter the market '
                             'scan (e.g. "Sports & Outdoors"). Resolved to SellerSprite '
                             'department numbers via category_map in market_config.json.')

    args = parser.parse_args()

    date_str = args.date if args.date else datetime.date.today().strftime('%Y_%m_%d')

    # Resolve department names → numbers using category_map from config
    dept_numbers: list[int] = []
    if args.departments:
        with open(args.config, 'r', encoding='utf-8') as f:
            _cfg = json.load(f)
        category_map = _cfg.get("category_map", {})
        unknown = []
        for name in args.departments:
            mapping = category_map.get(name)
            if mapping and mapping.get("department") is not None:
                dept_numbers.append(int(mapping["department"]))
            else:
                unknown.append(name)
        if unknown:
            print(f"WARNING: no department mapping for: {unknown} — those will be skipped")
        print(f"Departments: {args.departments} → numbers {dept_numbers}")

    check_browser_ready()
    # standalone: join department names as a comma-separated string if multiple
    dept_label = ", ".join(args.departments) if args.departments else None
    categories, scan_meta = scrape_market(args.config, department_label=dept_label)
    generate_report(args.config, categories, date_str,
                    output_dir=args.output_dir or None, scan_meta=scan_meta)

if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Scan failed: {exc}")
