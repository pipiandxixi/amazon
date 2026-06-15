#!/usr/bin/env python3
"""Find qualified products inside one exact SellerSprite leaf category."""

from __future__ import annotations

import argparse
import datetime
import json
import re
import time
from pathlib import Path

from scan_common import OpenCliError, check_browser_ready, dated_results_dir, eval_browser, extract_json_array, open_browser
from aggregate_top_picks import parse_product_file, score_product, write_top_picks

try:
    from deep_translator import GoogleTranslator as _GoogleTranslator
    def _translate_batch(texts: list[str]) -> list[str]:
        tr = _GoogleTranslator(source="en", target="zh-CN")
        return [tr.translate(t) or t for t in texts]
except ImportError:
    def _translate_batch(texts: list[str]) -> list[str]:  # type: ignore[misc]
        return [""] * len(texts)


INPUT_INDEXES = {
    "min_monthly_sales": 1,
    "max_monthly_sales": 2,
    "min_sales_growth": 7,
    "max_sales_growth": 8,
    "max_leaf_bsr": 12,
    "min_bsr_growth_count": 13,
    "max_bsr_growth_count": 14,
    "min_bsr_growth_rate": 15,
    "max_bsr_growth_rate": 16,
    "min_variants": 17,
    "max_variants": 18,
    "min_price": 19,
    "max_price": 20,
    "max_reviews": 24,
    "min_monthly_new_reviews": 25,
    "max_monthly_new_reviews": 26,
    "min_rating": 27,
    "max_rating": 28,
    "min_profit_margin": 33,
    "max_fba_fee": 32,
    "max_package_weight_g": 39,
    "min_sellers": 44,
    "max_sellers": 45,
}


def values(section: dict) -> dict:
    return {
        key: item.get("value") if isinstance(item, dict) and "value" in item else item
        for key, item in section.items()
    }


_CURRENT_NODE_ID_PATH = None
_ONLY_LEAF_RANK = True


def use_category_node(node_id_path: str, only_leaf_rank: bool) -> str:
    """Use a previously resolved SellerSprite node ID path without opening the modal."""
    global _CURRENT_NODE_ID_PATH, _ONLY_LEAF_RANK
    if not node_id_path:
        raise ValueError("Category node ID path is empty.")
    _CURRENT_NODE_ID_PATH = node_id_path
    _ONLY_LEAF_RANK = only_leaf_rank
    return node_id_path


def select_category(path: list[str], only_leaf_rank: bool) -> str:
    """Resolve the category path to a SellerSprite node ID path using the search modal.

    Returns the resolved node ID path (e.g. '3375251:10971181011:...').
    """
    global _CURRENT_NODE_ID_PATH, _ONLY_LEAF_RANK
    _ONLY_LEAF_RANK = only_leaf_rank

    leaf_category = path[-1]
    print("  [nav-search] Resolving category '" + leaf_category + "' via search modal...")
    time.sleep(1.0)  # Settle delay to let any previous page load/dialog transition finish

    # 1. Trigger Dialog Open
    trigger_js = """
    (() => {
      const dialogs = Array.from(document.querySelectorAll('.el-dialog__wrapper, .el-dialog'));
      const isVisible = dialogs.some(d => d.offsetParent !== null && d.offsetWidth > 0);
      if (isVisible) {
        return 'already_opened';
      }

      const trigger = Array.from(document.querySelectorAll('*')).find(
        x => x.children.length === 0 && x.textContent.trim() === '选择一个或多个类目和子类目'
      );
      if (!trigger) return 'category trigger not found';
      trigger.click();
      return 'opened';
    })()
    """
    output = eval_browser(trigger_js)
    if "opened" not in output and "already_opened" not in output:
        raise ValueError("Failed to open category dialog: " + str(output))

    time.sleep(1.5)  # Wait for category modal dialog DOM to render

    # 2. Trigger Search in Dialog
    search_js = """
    (() => {
      const wrapper = Array.from(document.querySelectorAll('.el-dialog__wrapper, .el-dialog')).find(x => x.offsetParent !== null);
      if (!wrapper) return 'no_visible_dialog';

      // Clear any pre-selected items to start fresh
      const buttons = Array.from(wrapper.querySelectorAll('button'));
      const clearBtn = buttons.find(b => b.textContent.includes('清空'));
      if (clearBtn) clearBtn.click();

      const input = wrapper.querySelector('input[placeholder*="Node ID"]') ||
                    wrapper.querySelector('input[placeholder*="类目"]');
      if (!input) return 'search input not found';

      const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      setter.call(input, '');
      input.dispatchEvent(new Event('input', { bubbles: true }));
      setter.call(input, """ + json.dumps(leaf_category) + """);
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));

      const searchIcon = input.parentElement.querySelector('.el-icon-search');
      if (searchIcon) {
        searchIcon.click();
      }
      return 'search_triggered';
    })()
    """
    res_input = eval_browser(search_js)
    if "error" in res_input or "no_visible_dialog" in res_input:
        raise ValueError("Failed to input category search: " + str(res_input))

    time.sleep(2.0)  # Wait for search results tree to populate

    # 3. Retrieve Node ID Path and Close Dialog
    retrieve_js = """
    (() => {
      const targetLeaf = """ + json.dumps(leaf_category) + """;
      const wrapper = Array.from(document.querySelectorAll('.el-dialog__wrapper, .el-dialog')).find(x => x.offsetParent !== null);
      if (!wrapper) return 'error:no_visible_dialog';

      const treeNodes = Array.from(wrapper.querySelectorAll('.el-tree-node'));
      const matchedNodes = treeNodes.filter(node => {
        if (node.offsetParent === null) return false;
        const textNode = node.querySelector('.label') || node.querySelector('.el-tree-node__label') || node;
        const text = textNode.textContent.trim();
        const cleanText = text.split(' (')[0];
        const leafName = cleanText.split('>').at(-1).trim().split(':').at(-1).trim();
        return leafName.toLowerCase() === targetLeaf.toLowerCase();
      });

      let nodeEl = null;
      if (matchedNodes.length > 0) {
        nodeEl = matchedNodes[0];
      } else {
        // Try fallback label matching
        const allLabels = Array.from(wrapper.querySelectorAll('.el-checkbox, label, span')).filter(el => {
          if (el.offsetParent === null) return false;
          const cleanText = el.textContent.split(' (')[0];
          return cleanText.toLowerCase().includes(targetLeaf.toLowerCase());
        });
        if (allLabels.length > 0) {
          nodeEl = allLabels[0].closest('.el-tree-node') || allLabels[0];
        }
      }

      if (!nodeEl) return 'error:category not found in search results';

      let nodeId = null;
      if (nodeEl.__vue__) {
        const vue = nodeEl.__vue__;
        nodeId = (vue.node && vue.node.data) ? vue.node.data.id : null;
      }

      if (!nodeId) {
        // Try searching vue instances of all tree nodes
        for (let i = 0; i < treeNodes.length; i++) {
          const tn = treeNodes[i];
          if (tn.__vue__ && tn.__vue__.node && tn.__vue__.node.data) {
            const data = tn.__vue__.node.data;
            const cleanLabel = (data.label || '').split(':').at(-1).split('(')[0].trim();
            if (cleanLabel.toLowerCase() === targetLeaf.toLowerCase()) {
              nodeId = data.id;
              break;
            }
          }
        }
      }

      if (!nodeId) return 'error:node id not found in Vue component';

      // Close the dialog
      const closeBtn = wrapper.querySelector('.el-dialog__close') || wrapper.querySelector('button[aria-label="Close"]') || wrapper.querySelector('.el-icon-close');
      if (closeBtn) closeBtn.click();

      return 'node_id:' + nodeId;
    })()
    """
    res_retrieve = eval_browser(retrieve_js)
    print("  [DEBUG] res_retrieve: " + str(res_retrieve))

    if not res_retrieve.startswith("node_id:"):
        raise ValueError("Could not resolve category node ID: " + str(res_retrieve))

    resolved_id = res_retrieve.split(":", 1)[1].strip()
    print("  [nav-search] Successfully resolved '" + leaf_category + "' to node ID: " + resolved_id)

    return use_category_node(resolved_id, only_leaf_rank)


def build_search_url(node_id_path: str, filters: dict, only_leaf_rank: bool) -> str:
    import urllib.parse

    # Default query parameters matching SellerSprite's URL structure
    query_params = {
        "market": "US",
        "page": "1",
        "size": "60",
        "symbolFlag": "false",
        "monthName": "bsr_sales_nearly",
        "selectType": "2",
        "filterSub": "true" if only_leaf_rank else "false",
        "weightUnit": "g",
        "order[field]": "total_amount",
        "order[desc]": "true",
        "productTags": "[]",
        "nodeIdPaths": json.dumps([node_id_path]),
        "sellerTypes": "[]",
        "eligibility": "[]",
        "pkgDimensionTypeList": "[]",
        "sellerNationList": "[]",
        "lowPrice": "N",
        "video": ""
    }

    # Map pipeline config filter keys to SellerSprite URL parameters
    key_mapping = {
        "min_monthly_sales": "minSales",
        "max_monthly_sales": "maxSales",
        "min_sales_growth": "minTotalUnitsGrowth",
        "max_sales_growth": "maxTotalUnitsGrowth",
        "max_leaf_bsr": "maxSubBsrRank",
        "min_bsr_growth_count": "minRankingCv",
        "max_bsr_growth_count": "maxRankingCv",
        "min_bsr_growth_rate": "minRankingCr",
        "max_bsr_growth_rate": "maxRankingCr",
        "min_variants": "minVariations",
        "max_variants": "maxVariations",
        "min_price": "minPrice",
        "max_price": "maxPrice",
        "max_reviews": "maxReviews",
        "min_monthly_new_reviews": "minReviewsGrouth",
        "max_monthly_new_reviews": "maxReviewsGrouth",
        "min_rating": "minReviewRating",
        "max_rating": "maxReviewRating",
        "min_profit_margin": "minProfit",
        "max_fba_fee": "maxFba",
        "max_package_weight_g": "maxWeights",
        "min_sellers": "minSellers",
        "max_sellers": "maxSellers",
    }

    for config_key, url_key in key_mapping.items():
        val = filters.get(config_key)
        if val is not None and val != "":
            query_params[url_key] = str(val)

    # Map fulfillment filter (FBA/FBM/AMZ)
    fulfillment = filters.get("fulfillment")
    if fulfillment == "FBA":
        query_params["sellerTypes"] = json.dumps(["FBA"])
    elif fulfillment == "FBM":
        query_params["sellerTypes"] = json.dumps(["FBM"])
    elif fulfillment == "AMZ":
        query_params["sellerTypes"] = json.dumps(["AMZ"])

    # Construct the query string and final URL
    query_string = urllib.parse.urlencode(query_params)
    return "https://www.sellersprite.com/v3/product-research?" + query_string


def apply_filters(filters: dict[str, str]) -> None:
    """Constructs the search URL and navigates directly, bypassing manual input form-filling."""
    global _CURRENT_NODE_ID_PATH, _ONLY_LEAF_RANK
    if not _CURRENT_NODE_ID_PATH:
        raise ValueError("No category has been resolved yet. Please run select_category first.")

    target_url = build_search_url(_CURRENT_NODE_ID_PATH, filters, _ONLY_LEAF_RANK)
    print("  [nav-search] Navigating directly to filtered URL: " + target_url[:120] + "...")

    open_browser(target_url)
    # Wait for the search results to populate
    time.sleep(5)


def hide_variants() -> None:
    eval_browser(
        """
        (() => {
          const label = Array.from(document.querySelectorAll('label')).find(
            x => x.innerText.includes('展示所有变体')
          );
          const input = label?.querySelector('input');
          if (input?.checked) input.click();
          return input ? input.checked : null;
        })()
        """
    )


def scrape_products(limit: int) -> list[dict[str, str]]:
    output = eval_browser(
        f"""
        (() => {{
          // New layout: div.relation-card (card-based, no table)
          const cards = Array.from(document.querySelectorAll('div.relation-card'));
          if (cards.length > 0) {{
            const products = [];
            for (let i = 0; i < cards.length && products.length < {limit}; i++) {{
              const card = cards[i];
              const text = card.innerText;
              if (!/\\bB0[A-Z0-9]{{8}}\\b/.test(text)) continue;
              const imgDiv = card.querySelector('.img');
              const style = imgDiv ? imgDiv.getAttribute('style') || '' : '';
              const urlM = style.match(/url\\(["']?([^"')]+)["']?\\)/);
              const imgUrl = urlM ? urlM[1] : '';
              products.push({{ main: text, detail: '', imgUrl }});
            }}
            return JSON.stringify(products);
          }}
          // Fallback: legacy table layout
          const rows = Array.from(document.querySelectorAll('table tbody tr'));
          const products = [];
          for (let i = 0; i < rows.length && products.length < {limit}; i += 2) {{
            const main = rows[i]?.innerText || '';
            const detail = rows[i + 1]?.innerText || '';
            if (!main.includes('ASIN:')) continue;
            const imgDiv = rows[i].querySelector('.asin-img .img');
            const style = imgDiv ? imgDiv.getAttribute('style') || '' : '';
            const urlM = style.match(/url\\(["']?([^"')]+)["']?\\)/);
            const imgUrl = urlM ? urlM[1] : '';
            products.push({{ main, detail, imgUrl }});
          }}
          return JSON.stringify(products);
        }})()
        """
    )
    raw_products = extract_json_array(output)
    return [parse_product(item["main"], item.get("detail", ""), item.get("imgUrl", ""))
            for item in raw_products]


def inspect_result_state() -> dict:
    output = eval_browser(
        """
        (() => {
          const cards = Array.from(document.querySelectorAll('div.relation-card'));
          const rows = Array.from(document.querySelectorAll('table tbody tr'));
          const visibleItems = cards.length || rows.filter(row => row.innerText.includes('ASIN:')).length;
          const text = document.body.innerText;
          const totalMatch = text.match(/(?:共|总计|总共)\\s*([\\d,]+)\\s*(?:条|个|件)/);
          const emptyMessage = [
            '没有找到', '暂无数据', '暂无符合', '未找到符合', '无符合条件'
          ].some(message => text.includes(message));
          const accessError = !!document.querySelector(
            '.login-form, form[action*="login"], input[type="password"]'
          ) || [
            '访问受限', '请求失败', '系统繁忙', '网络错误'
          ].some(message => text.includes(message));
          const resultSurface = !!document.querySelector(
            'div.relation-card, table, .el-pagination, .pagination, [class*="empty"]'
          );
          const nextBtn = document.querySelector('button.btn-next, .pagination .next a, .el-pagination .btn-next');
          const parent = nextBtn?.closest('li, button');
          const nextAvailable = !!nextBtn && !nextBtn.disabled
            && nextBtn.getAttribute('aria-disabled') !== 'true'
            && !parent?.classList.contains('disabled');
          return JSON.stringify({
            visible_items: visibleItems,
            reported_total: totalMatch ? Number(totalMatch[1].replaceAll(',', '')) : null,
            next_available: nextAvailable,
            empty_message: emptyMessage,
            access_error: accessError,
            result_surface: resultSurface,
            free_limit_message: text.includes('当前的会员版本无法查看全部结果')
              || text.includes('升级套餐后可查看全部')
          });
        })()
        """
    )
    start = output.find("{")
    end = output.rfind("}")
    return json.loads(output[start:end + 1])


def _calc_listing_age(listing_date: str) -> str:
    """Calculate age string like '8个月' or '1年 3个月' from a YYYY-MM-DD date."""
    import datetime
    try:
        d = datetime.date.fromisoformat(listing_date)
        today = datetime.date.today()
        months = (today.year - d.year) * 12 + (today.month - d.month)
        if months < 1:
            return "<1个月"
        if months < 12:
            return f"{months}个月"
        y, m = divmod(months, 12)
        return f"{y}年 {m}个月" if m else f"{y}年"
    except (ValueError, TypeError):
        return ""


def parse_product(main: str, detail: str, img_url: str = "") -> dict[str, str]:
    # ── New card layout (SellerSprite v3 post-redesign) ───────────────────────
    # Identified by: ASIN appears as bare value on its own line (no "ASIN: " prefix)
    # and combined "评分/评分数: X.X/NNN" field.
    if not detail and re.search(r"(?m)^B0[A-Z0-9]{8}$", main):
        lines = [l.strip() for l in main.splitlines() if l.strip()]
        asin_idx = next((i for i, l in enumerate(lines) if re.match(r'^B0[A-Z0-9]{8}$', l)), -1)
        title = lines[asin_idx - 1] if asin_idx > 0 else ""
        asin = lines[asin_idx] if asin_idx >= 0 else ""

        brand_m = re.search(r'品牌:\s*\n\s*(.+)', main) or re.search(r'品牌:([^\n]+)', main)
        sales_m = re.search(r'销量\(父\):\s*([\d,]+)', main)
        revenue_m = re.search(r'销售额:\s*\$?([\d,]+)', main)
        variants_m = re.search(r'变体数:\s*(\d+)', main)
        price_m = re.search(r'价格:\s*\$([\d.]+)', main)
        rr_m = re.search(r'评分/评分数:\s*([\d.]+)/([\d,]+)', main)
        date_m = re.search(r'上架时间:\s*(\d{4}-\d{2}-\d{2})', main)
        sellers_m = re.search(r'FBA卖家:\s*(\d+)', main)

        # Leaf rank: multiline "#N\nin\nCategory" is the leaf rank
        ml_ranks = re.findall(r'#([\d,]+)\s*\n\s*in\s*\n\s*([^\n]+)', main)
        if ml_ranks:
            leaf_rank, leaf_cat = ml_ranks[0][0], ml_ranks[0][1].strip()
        else:
            il_ranks = re.findall(r'#([\d,]+) in ([^\n#]{3,50})', main)
            leaf_rank, leaf_cat = (il_ranks[-1][0], il_ranks[-1][1].strip()) if il_ranks else ("", "")

        listing_date = date_m.group(1) if date_m else ""
        return {
            "asin": asin,
            "parent_asin": "",
            "title": title,
            "brand": brand_m.group(1).strip() if brand_m else "",
            "monthly_sales": sales_m.group(1).replace(',', '') if sales_m else "",
            "sales_growth": "-",
            "monthly_revenue": f"${revenue_m.group(1)}" if revenue_m else "",
            "variants": variants_m.group(1) if variants_m else "",
            "price": f"${price_m.group(1)}" if price_m else "",
            "reviews": rr_m.group(2).replace(',', '') if rr_m else "",
            "monthly_new_reviews": "",
            "rating": rr_m.group(1) if rr_m else "",
            "review_rate": "",
            "fba_fee": "0",        # not shown in new layout; use 0 as placeholder
            "profit_margin": "50%",  # SellerSprite filter guarantees ≥50%; use as floor
            "listing_date": listing_date,
            "listing_age": _calc_listing_age(listing_date),
            "leaf_rank": leaf_rank,
            "leaf_category": leaf_cat,
            "sellers": sellers_m.group(1) if sellers_m else "",
            "package_weight": "",
            "raw_metrics": main[:300],
            "image_url": img_url,
        }

    # ── Legacy table layout ───────────────────────────────────────────────────
    lines = [line.strip() for line in main.splitlines() if line.strip()]
    asin = re.search(r"ASIN:\s*([A-Z0-9]+)", main)
    parent = re.search(r"父ASIN\s*:\s*([A-Z0-9]+)", main)
    brand = re.search(r"品牌:([^\n]+)", main)
    title_index = next((i for i, line in enumerate(lines) if "ASIN:" in line), 0)
    title = lines[title_index - 1] if title_index else ""
    brand_index = next((i for i, line in enumerate(lines) if line.startswith("品牌:")), -1)
    metrics = lines[brand_index + 1 :] if brand_index >= 0 else []
    value = lambda index: metrics[index] if len(metrics) > index else ""
    tail = lambda offset: metrics[offset] if len(metrics) >= abs(offset) else ""
    has_full_metrics = len(metrics) >= 21
    leaf_rank = re.search(r"#([\d,]+) in ([^\n]+)", detail)
    sellers = re.search(r"卖家:\s*(\d+)\s*家", detail)
    package_weight = re.search(r"包装重量:\s*(.+?)\s+包装尺寸:", detail)
    return {
        "asin": asin.group(1) if asin else "",
        "parent_asin": parent.group(1) if parent else "",
        "title": title,
        "brand": brand.group(1).strip() if brand else "",
        "monthly_sales": value(3),
        "sales_growth": value(4),
        "monthly_revenue": value(5),
        "variants": tail(-13) if has_full_metrics else value(7),
        "price": tail(-12) if has_full_metrics else value(8),
        "reviews": tail(-10) if has_full_metrics else value(10),
        "monthly_new_reviews": tail(-9) if has_full_metrics else value(11),
        "rating": tail(-8) if has_full_metrics else value(12),
        "review_rate": tail(-7) if has_full_metrics else value(13),
        "fba_fee": tail(-6) if has_full_metrics else value(14),
        "profit_margin": tail(-5) if has_full_metrics else "",
        "listing_date": tail(-4) if has_full_metrics else value(15),
        "listing_age": tail(-3) if has_full_metrics else value(16),
        "leaf_rank": leaf_rank.group(1) if leaf_rank else "",
        "leaf_category": leaf_rank.group(2).strip() if leaf_rank else "",
        "sellers": sellers.group(1) if sellers else "",
        "package_weight": package_weight.group(1).strip() if package_weight else "",
        "raw_metrics": " | ".join(metrics),
        "image_url": img_url,
    }


_FILTER_RATIONALE: dict[str, str] = {
    "min_monthly_sales":       "确保产品有稳定市场需求，低于此销量视为市场过小",
    "max_monthly_sales":       "避开竞争过于激烈的大爆款，聚焦中等规模机会",
    "max_reviews":             "评价数低说明竞争护城河浅，新卖家仍有进入机会",
    "min_rating":              "过滤质量差评产品，只关注消费者认可的品类",
    "max_rating":              "评分上限（通常无需限制，保留作兜底）",
    "min_profit_margin":       "确保覆盖 FBA 费用、广告成本后仍有合理利润空间",
    "min_price":               "低价品利润薄、运营容错率低，过滤不符合要求的产品",
    "max_price":               "客单价过高会拉长消费者决策周期并增加资金压力",
    "max_package_weight_g":    "重量直接决定 FBA 头程和月租费，轻量化是新卖家核心竞争力",
    "max_sellers":             "卖家少说明市场未饱和，存在空白或新兴机会",
    "min_sellers":             "至少有一家卖家说明品类已有验证，排除无人做的死角",
    "min_variants":            "排除变体结构过于单一的产品",
    "max_variants":            "变体过多会拉高库存管理复杂度和资金占用",
    "max_fba_fee":             "FBA 费用直接影响毛利，设置上限保护利润",
    "max_leaf_bsr":            "小类 BSR 越小说明销量越靠前，限制范围聚焦头部产品",
    "fulfillment":             "FBA 配送是新卖家标准模式，确保物流体验和搜索权重",
}


def _explain_filters(config_filters: dict) -> list[str]:
    """Generate selection principle lines from raw config filter dict (with label/value)."""
    lines: list[str] = []
    for key, raw in config_filters.items():
        value = raw.get("value", raw) if isinstance(raw, dict) else raw
        label = raw.get("label", key) if isinstance(raw, dict) else key
        if value == "" or value is None:
            continue
        rationale = _FILTER_RATIONALE.get(key, "")
        suffix = f"　*{rationale}*" if rationale else ""
        lines.append(f"- **{label}** ≥/≤/= `{value}`{suffix}")
    return lines


_CN_NUMS = ["一", "二", "三", "四", "五", "六", "七"]


def _est_cogs(price_str: str, fba_fee_str: str, margin_str: str) -> str:
    """Estimate COGS from SellerSprite margin model: cogs = price*(1-margin) - fba_fee."""
    try:
        price = float(re.sub(r"[^0-9.]", "", price_str))
        fba = float(re.sub(r"[^0-9.]", "", fba_fee_str))
        margin = float(re.sub(r"[^0-9.]", "", margin_str)) / 100
        if price <= 0 or not (0 < margin < 1):
            return "-"
        cogs = price * (1 - margin) - fba
        ratio = cogs / price * 100
        return f"${cogs:.2f} ({ratio:.0f}%)"
    except (ValueError, ZeroDivisionError):
        return "-"


def _market_metric_str(entry: dict) -> str:
    """Format market metrics with qualitative labels based on risk thresholds."""
    def tag_reviews(v):
        if v <= 300:  return f"均Reviews {v}（低竞争）"
        if v <= 800:  return f"均Reviews {v}（中等）"
        return               f"均Reviews {v}（高竞争）"

    def tag_weight(v):
        if v <= 1.5:  return f"重量 {v:.2f}lbs（轻）"
        if v <= 2.0:  return f"重量 {v:.2f}lbs（偏重）"
        return               f"重量 {v:.2f}lbs（重）"

    def tag_return(v):
        if v <= 5:    return f"退货率 {v}%（低）"
        if v <= 8:    return f"退货率 {v}%（中）"
        return               f"退货率 {v}%（高）"

    def tag_brand(v):
        if v <= 40:   return f"品牌集中度 {v}%（分散）"
        if v <= 65:   return f"品牌集中度 {v}%（中等）"
        return               f"品牌集中度 {v}%（垄断）"

    parts = []
    if entry.get("price") is not None:
        parts.append(f"均价 ${entry['price']:.2f}")
    if entry.get("reviews") is not None:
        parts.append(tag_reviews(entry["reviews"]))
    if entry.get("weight_lbs") is not None:
        parts.append(tag_weight(entry["weight_lbs"]))
    if entry.get("return_rate") is not None:
        parts.append(tag_return(entry["return_rate"]))
    if entry.get("brand_conc") is not None:
        parts.append(tag_brand(entry["brand_conc"]))
    if entry.get("cn_ratio") is not None:
        parts.append(f"中国卖家 {entry['cn_ratio']}%")
    return "　".join(parts) if parts else "（指标不可用）"


def _short_title(title: str, max_len: int = 65) -> str:
    """Extract core product name: first segment before spec separators."""
    for sep in [" – ", " — ", " | ", ", ", " - "]:
        idx = title.find(sep)
        if 0 < idx <= max_len:
            return title[:idx]
    return title[:max_len].rstrip() + ("…" if len(title) > max_len else "")


def write_principles_file(config: dict, output_dir: Path, date_str: str) -> Path:
    """Write a shared scan_principles.md to output_dir (batch mode only)."""
    path = output_dir / "scan_principles.md"
    md = [
        f"# 选品原则 ({date_str.replace('_', '-')})\n",
        "本文件由批量产品扫描自动生成，同批次所有品类报告共享同一套筛选条件。\n",
        "本次产品扫描依据以下量化条件筛选候选商品，每项条件均有明确的选品逻辑：\n",
    ]
    for line in _explain_filters(config["filters"]):
        md.append(line)
    path.write_text("\n".join(md) + "\n", encoding="utf-8")
    return path


def format_report(
    config: dict,
    products: list[dict[str, str]],
    date_str: str,
    category_name: str | None = None,
    category_path: list[str] | None = None,
    batch_total: int = 0,
    include_principles: bool = True,
    market_entry: dict | None = None,
    result_state: dict | None = None,
) -> str:
    """Build and return the markdown content string for a product scan report."""
    category = category_name or config["category"]["name"]
    cat_path = category_path or config["category"]["path"]
    short_titles = [_short_title(p["title"]) for p in products]
    print(f"  Translating {len(short_titles)} product names to Chinese...")
    zh_names = _translate_batch(short_titles)
    sec = iter(_CN_NUMS)

    md = [
        f"# {category} 合格产品扫描 ({date_str.replace('_', '-')})\n",
        f"> **所在品类路径**：`{' › '.join(cat_path)}`",
        f"> 共抓取 **{len(products)}** 个通过全部筛选条件的候选商品。\n",
    ]
    if result_state:
        reported_total = result_state.get("reported_total")
        possible_truncation = (
            result_state.get("next_available", False)
            or result_state.get("visible_items", 0) > len(products)
            or (reported_total is not None and reported_total > len(products))
            or result_state.get("free_limit_message", False)
        )
        md.append(
            f"> **抓取完整性**：页面可见 **{result_state.get('visible_items', 0)}** 个；"
            f"页面总数提示 **{reported_total if reported_total is not None else '未识别'}**；"
            f"下一页 **{'可用' if result_state.get('next_available') else '不可用或未识别'}**；"
            f"免费套餐截断风险：**{'可能存在' if possible_truncation else '未检测到'}**。\n"
        )
    if market_entry:
        level = market_entry.get("level", "")
        md.append(f"> **市场评级**：{level}　{_market_metric_str(market_entry)}\n")

    if include_principles:
        md.append(f"## {next(sec)}、选品原则\n")
        md.append("本次产品扫描依据以下量化条件筛选候选商品，每项条件均有明确的选品逻辑：\n")
        for line in _explain_filters(config["filters"]):
            md.append(line)
        md.append("")

    md.append(f"## {next(sec)}、候选商品列表\n")
    md += [
        "| # | ASIN | 中文名称 | 核心名称 | 月销量 / 增长率 | 月销售额 | 价格 | 估算成本 / 占比 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |",
        "|---:|---|---|---|---|---:|---:|---:|---|---:|---|---:|---:|---:|---|---|",
    ]
    for index, (product, short, zh) in enumerate(zip(products, short_titles, zh_names), 1):
        clean = {k: str(v).replace("|", "\\|").replace("\n", " ") for k, v in product.items()}
        short_clean = short.replace("|", "\\|")
        zh_clean = (zh or "").replace("|", "\\|")
        asin_link = f"[{clean['asin']}](https://www.amazon.com/dp/{clean['asin']})"
        cogs = _est_cogs(clean["price"], clean["fba_fee"], clean["profit_margin"])
        md.append(
            f"| {index} | {asin_link} | {zh_clean} | {short_clean} | "
            f"{clean['monthly_sales']} / {clean['sales_growth']} | {clean['monthly_revenue']} | "
            f"{clean['price']} | {cogs} | {clean['reviews']} / {clean['monthly_new_reviews']} | "
            f"{clean['rating']} | {clean['fba_fee']} / {clean['profit_margin']} | "
            f"{clean['variants']} | {clean['leaf_rank']} | {clean['sellers']} | "
            f"{clean['package_weight']} | {clean['listing_date']} {clean['listing_age']} |"
        )
    md.append("")

    md.append(f"## {next(sec)}、完整商品标题\n")
    for index, product in enumerate(products, 1):
        asin_link = f"[{product['asin']}](https://www.amazon.com/dp/{product['asin']})"
        md.append(f"**{index}. {asin_link}** {product['title']}")
        md.append("")

    md.append(f"## {next(sec)}、下一步建议\n")
    md.append(
        "1. **深度调研候选商品**：对表格中评价数 ≤ 50、月销量 ≥ 200 的商品，"
        "在卖家精灵「产品详情」页核查供应链来源、头程成本、竞品广告投放强度。\n"
    )
    md.append(
        "2. **关键词验证**：统一流水线已对每个品类的头部商品批量反查拓展流量词，"
        "结果见同目录下 `category_keywords_*.md`，核对搜索量与购买率后再决定是否建 Listing。\n"
    )
    md.append(
        "3. **供应商询价**：以平均售价的 20%-30% 为目标采购成本，"
        "在 1688 / Alibaba 搜索对应品类，索取 MOQ 和含税价，核算实际利润率。\n"
    )

    md.append(f"## {next(sec)}、原始数值\n")
    for product in products:
        md.append(f"- `{product['asin']}`: {product['raw_metrics']}")

    return "\n".join(md) + "\n"


def write_report(
    config: dict,
    products: list[dict[str, str]],
    date_str: str,
    category_name: str | None = None,
    category_path: list[str] | None = None,
    batch_total: int = 0,
    output_dir: Path | None = None,
    include_principles: bool = True,
    market_entry: dict | None = None,
    result_state: dict | None = None,
) -> Path:
    category = category_name or config["category"]["name"]
    slug = re.sub(r"[^a-z0-9]+", "_", category.lower()).strip("_")
    if output_dir:
        path = output_dir / f"{slug}.md"
    else:
        path = dated_results_dir(date_str) / f"product_scan_{slug}_{date_str}.md"
    content = format_report(
        config, products, date_str,
        category_name=category_name, category_path=category_path,
        batch_total=batch_total, include_principles=include_principles,
        market_entry=market_entry, result_state=result_state,
    )
    path.write_text(content, encoding="utf-8")
    return path


def _parse_path(raw) -> list[str]:
    """Accept a path as list or ">"/›-separated string."""
    if isinstance(raw, list):
        return raw
    return [s.strip() for s in re.split(r'[>›]', str(raw)) if s.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/product_config.json")
    parser.add_argument("--date", default="")
    parser.add_argument(
        "--output-dir", default="", dest="output_dir",
        help="Directory to write product report(s) (pipeline mode); "
             "defaults to results/YYYY_MM_DD/",
    )
    parser.add_argument(
        "--keywords-file", default="", dest="keywords_file",
        help="JSON file with keyword string list; joined as includeKeywords filter",
    )
    parser.add_argument(
        "--categories-file", default="", dest="categories_file",
        help="JSON file with a list of category entries; triggers batch mode that scans "
             "each entry in sequence. Minimum fields: {en_name, path}. Pipeline mode "
             "supplies enriched entries with {product_path, departments, level} as well.",
    )
    parser.add_argument(
        "--market-sidecar", default="", dest="market_sidecar",
        help="market_scan_results JSON from select_market.py; used to compute the "
             "uncovered categories section in each report",
    )
    parser.add_argument(
        "--batch-size", type=int, default=0, dest="batch_size",
        help="Write top_picks.md after every N categories complete (0 = only at end). "
             "Requires --output-dir to be set.",
    )
    parser.add_argument(
        "--top-n", type=int, default=50, dest="top_n",
        help="Number of top picks to include in top_picks.md (default 50).",
    )
    args = parser.parse_args()
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    policy = values(config.get("scan_policy", {}))
    filters = values(config["filters"])
    output_dir = Path(args.output_dir) if args.output_dir else None
    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)

    # Load market sidecar for uncovered-categories context
    market_candidates: list[dict] = []
    if args.market_sidecar:
        ms_path = Path(args.market_sidecar)
        if ms_path.exists():
            market_candidates = json.loads(ms_path.read_text(encoding="utf-8"))

    # Apply keyword override from --keywords-file
    if args.keywords_file:
        kw_path = Path(args.keywords_file)
        if not kw_path.exists():
            raise SystemExit(f"--keywords-file not found: {kw_path}")
        kw_list: list[str] = json.loads(kw_path.read_text(encoding="utf-8"))
        filters["includeKeywords"] = ",".join(str(k) for k in kw_list if k)
        print(f"--keywords-file: includeKeywords = {filters['includeKeywords'][:80]}...")

    check_browser_ready()
    open_browser("https://www.sellersprite.com/v3/product-research")
    time.sleep(5)

    if args.categories_file:
        # Batch mode: scan each category from the file
        cats_path = Path(args.categories_file)
        if not cats_path.exists():
            raise SystemExit(f"--categories-file not found: {cats_path}")
        cats_data = json.loads(cats_path.read_text(encoding="utf-8"))
        print(f"Batch mode: {len(cats_data)} categories from {cats_path}")

        # Write shared principles file once for the whole batch
        principles_dir = output_dir if output_dir else dated_results_dir(date_str)
        principles_path = write_principles_file(config, principles_dir, date_str)
        print(f"  Principles: {principles_path}")

        results_summary: list[str] = []
        batch_total = len(cats_data)
        completed_count = 0
        asin_images: dict[str, str] = {}  # accumulated ASIN → image_url across all categories

        def _flush_top_picks(label: str) -> None:
            if not output_dir:
                return
            md_files = sorted(f for f in output_dir.glob("*.md") if f.stem != "scan_principles")
            all_products: list[dict] = []
            cat_names: list[str] = []
            for f in md_files:
                cat_en, products = parse_product_file(f)
                cat_names.append(cat_en)
                for p in products:
                    p["_score"] = score_product(p)
                all_products.extend(products)
            if all_products:
                write_top_picks(output_dir.parent, all_products, cat_names, args.top_n, date_str, label)
                print(f"  [top_picks] {label}: {len(all_products)} products across {len(cat_names)} categories")

        for entry in cats_data:
            cat_name = entry.get("en_name", "") or entry.get("zh_name", "unknown")
            # Prefer pre-built product_path array (from pipeline enrichment);
            # fall back to splitting path string for standalone use.
            cat_path = entry.get("product_path") or _parse_path(entry.get("path", ""))
            if not cat_path:
                print(f"  [SKIP] No path for category: {cat_name}")
                continue
            print(f"\n[CATEGORY] {cat_name}")
            try:
                select_category(cat_path, policy.get("only_leaf_category_rank", True))
                apply_filters(filters)
                time.sleep(float(policy.get("wait_seconds", 5)))
                if policy.get("hide_variants", True):
                    hide_variants()
                    time.sleep(3)
                result_state = inspect_result_state()
                products = scrape_products(int(policy.get("max_products", 20)))
                for p in products:
                    if p.get("image_url"):
                        asin_images[p["asin"]] = p["image_url"]
                mkt = next(
                    (c for c in market_candidates if c.get("en_name", "").lower() == cat_name.lower()),
                    None,
                )
                report = write_report(
                    config, products, date_str,
                    category_name=cat_name, category_path=cat_path,
                    batch_total=batch_total,
                    output_dir=output_dir, include_principles=False,
                    market_entry=mkt,
                    result_state=result_state,
                )
                print(f"  Wrote {len(products)} products to {report}")
                results_summary.append(f"  {cat_name}: {len(products)} products → {report}")
            except ValueError as exc:
                print(f"  [ERROR] {cat_name}: {exc}")
                results_summary.append(f"  {cat_name}: FAILED — {exc}")

            completed_count += 1
            if args.batch_size > 0 and completed_count % args.batch_size == 0:
                _flush_top_picks(f"第{completed_count // args.batch_size}批 {completed_count}/{batch_total}类目")

            # Reload page to reset state for next category
            open_browser("https://www.sellersprite.com/v3/product-research")
            time.sleep(5)

        # Save accumulated image URLs for use by generate_grid_image.py
        if output_dir and asin_images:
            img_map_path = output_dir / "json" / "asin_images.json"
            img_map_path.parent.mkdir(parents=True, exist_ok=True)
            img_map_path.write_text(json.dumps(asin_images, ensure_ascii=False, indent=2))
            print(f"  [images] Saved {len(asin_images)} image URLs → {img_map_path}")

        # Final flush after all categories complete
        _flush_top_picks(f"{completed_count}/{batch_total}类目完成")

        if not asin_images:
            raise SystemExit(
                f"\n[ERROR] 全部 {batch_total} 个类目均返回 0 产品，pipeline 终止。\n"
                "  → 检查 product_config.json 的 filters（max_reviews / max_sellers 等）是否过于严格\n"
                f"  → top_picks.md 未生成，后续步骤无法继续"
            )

        print("\n=== Batch Summary ===")
        for line in results_summary:
            print(line)
    else:
        # Single category mode (original behavior)
        scanned_path = config["category"]["path"]
        select_category(scanned_path, policy.get("only_leaf_category_rank", True))
        apply_filters(filters)
        time.sleep(float(policy.get("wait_seconds", 5)))
        if policy.get("hide_variants", True):
            hide_variants()
            time.sleep(3)
        result_state = inspect_result_state()
        products = scrape_products(int(policy.get("max_products", 20)))
        report = write_report(config, products, date_str,
                              output_dir=output_dir, result_state=result_state)
        print(f"Wrote {len(products)} products to {report}")


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Product scan failed: {exc}")
