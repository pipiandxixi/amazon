#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)


SESSION = "products"
PRODUCT_URL = "https://www.sellersprite.com/v3/product-research"


def extract_json_object(output: str) -> dict:
    start = output.find("{")
    end = output.rfind("}")
    if start == -1 or end < start:
        raise ValueError("Browser output did not contain a JSON object")
    return json.loads(output[start:end + 1])


def _calc_listing_age(listing_date: str) -> str:
    try:
        date = dt.date.fromisoformat(listing_date)
        today = dt.date.today()
        months = (today.year - date.year) * 12 + (today.month - date.month)
        if months < 1:
            return "<1个月"
        if months < 12:
            return f"{months}个月"
        years, rem = divmod(months, 12)
        return f"{years}年 {rem}个月" if rem else f"{years}年"
    except (TypeError, ValueError):
        return ""


def parse_product(main: str, detail: str, img_url: str = "") -> dict[str, str]:
    if not detail and re.search(r"(?m)^B0[A-Z0-9]{8}$", main):
        lines = [line.strip() for line in main.splitlines() if line.strip()]
        asin_idx = next((i for i, line in enumerate(lines) if re.match(r"^B0[A-Z0-9]{8}$", line)), -1)
        title = lines[asin_idx - 1] if asin_idx > 0 else ""
        asin = lines[asin_idx] if asin_idx >= 0 else ""
        brand_m = re.search(r"品牌:\s*\n\s*(.+)", main) or re.search(r"品牌:([^\n]+)", main)
        sales_m = re.search(r"销量\(父\):\s*([\d,]+)", main)
        revenue_m = re.search(r"销售额:\s*\$?([\d,]+)", main)
        variants_m = re.search(r"变体数:\s*(\d+)", main)
        price_m = re.search(r"价格:\s*\$([\d.]+)", main)
        rr_m = re.search(r"评分/评分数:\s*([\d.]+)/([\d,]+)", main)
        date_m = re.search(r"上架时间:\s*(\d{4}-\d{2}-\d{2})", main)
        sellers_m = re.search(r"FBA卖家:\s*(\d+)", main)
        ml_ranks = re.findall(r"#([\d,]+)\s*\n\s*in\s*\n\s*([^\n]+)", main)
        if ml_ranks:
            leaf_rank, leaf_cat = ml_ranks[0][0], ml_ranks[0][1].strip()
        else:
            il_ranks = re.findall(r"#([\d,]+) in ([^\n#]{3,80})", main)
            leaf_rank, leaf_cat = (il_ranks[-1][0], il_ranks[-1][1].strip()) if il_ranks else ("", "")
        listing_date = date_m.group(1) if date_m else ""
        return {
            "asin": asin,
            "parent_asin": "",
            "title": title,
            "brand": brand_m.group(1).strip() if brand_m else "",
            "monthly_sales": sales_m.group(1).replace(",", "") if sales_m else "",
            "sales_growth": "-",
            "monthly_revenue": f"${revenue_m.group(1)}" if revenue_m else "",
            "variants": variants_m.group(1) if variants_m else "",
            "price": f"${price_m.group(1)}" if price_m else "",
            "reviews": rr_m.group(2).replace(",", "") if rr_m else "",
            "monthly_new_reviews": "",
            "rating": rr_m.group(1) if rr_m else "",
            "review_rate": "",
            "fba_fee": "",
            "profit_margin": "",
            "listing_date": listing_date,
            "listing_age": _calc_listing_age(listing_date),
            "leaf_rank": leaf_rank,
            "leaf_category": leaf_cat,
            "sellers": sellers_m.group(1) if sellers_m else "",
            "package_weight": "",
            "raw_metrics": main[:300],
            "image_url": img_url,
        }

    lines = [line.strip() for line in main.splitlines() if line.strip()]
    asin = re.search(r"ASIN:\s*([A-Z0-9]+)", main)
    parent = re.search(r"父ASIN\s*:\s*([A-Z0-9]+)", main)
    brand = re.search(r"品牌:([^\n]+)", main)
    title_index = next((i for i, line in enumerate(lines) if "ASIN:" in line), 0)
    title = lines[title_index - 1] if title_index else ""
    brand_index = next((i for i, line in enumerate(lines) if line.startswith("品牌:")), -1)
    metrics = lines[brand_index + 1:] if brand_index >= 0 else []
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


def run_opencli(args: list[str], timeout: int = 60) -> str:
    result = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "unknown error"
        raise RuntimeError(f"Command failed ({result.returncode}): {message}")
    return result.stdout.strip()


def open_browser(url: str) -> str:
    return run_opencli(["opencli", "browser", SESSION, "open", url], timeout=60)


def eval_browser(js: str, timeout: int = 60) -> str:
    return run_opencli(["opencli", "browser", SESSION, "eval", js], timeout=timeout)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_") or "category"


def load_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_category_pool(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("target_pool", data if isinstance(data, list) else [])


def split_market_path(path: str) -> list[str]:
    return [p.strip() for p in re.split(r"[:>›]", path or "") if p.strip()]


def build_product_url(node_id_paths: list[str], filters: dict) -> str:
    query = dict(filters)
    query["nodeIdPaths"] = json.dumps(node_id_paths, separators=(",", ":"))
    return PRODUCT_URL + "?" + urlencode(query)


def resolve_node_id_path(category: dict, cache: dict) -> str:
    path = category["path"]
    if path in cache:
        return cache[path]

    parts = split_market_path(path)
    leaf = parts[-1] if parts else category["name"]
    print(f"  resolving nodeIdPath: {leaf}")
    open_browser(PRODUCT_URL)
    time.sleep(4)

    js = f"""
    (() => {{
      const leaf = {json.dumps(leaf)};
      const trigger = Array.from(document.querySelectorAll('*')).find(
        el => el.children.length === 0 && el.textContent.trim() === '选择一个或多个类目和子类目'
      );
      if (!trigger) return JSON.stringify({{error: 'category trigger not found'}});
      trigger.click();
      return JSON.stringify({{opened: true}});
    }})()
    """
    state = extract_json_object(eval_browser(js))
    if state.get("error"):
        raise RuntimeError(state["error"])
    time.sleep(2)

    search_js = f"""
    (() => {{
      const leaf = {json.dumps(leaf)};
      const wrapper = Array.from(document.querySelectorAll('.el-dialog__wrapper, .el-dialog'))
        .find(x => x.offsetParent !== null);
      if (!wrapper) return JSON.stringify({{error: 'no visible category dialog'}});
      const clearBtn = Array.from(wrapper.querySelectorAll('button')).find(b => b.textContent.includes('清空'));
      if (clearBtn) clearBtn.click();
      const input = wrapper.querySelector('input[placeholder*="Node ID"]') ||
        wrapper.querySelector('input[placeholder*="类目"]');
      if (!input) return JSON.stringify({{error: 'search input not found'}});
      const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      setter.call(input, '');
      input.dispatchEvent(new Event('input', {{bubbles: true}}));
      setter.call(input, leaf);
      input.dispatchEvent(new Event('input', {{bubbles: true}}));
      input.dispatchEvent(new Event('change', {{bubbles: true}}));
      const icon = input.parentElement.querySelector('.el-icon-search');
      if (icon) icon.click();
      return JSON.stringify({{searched: leaf}});
    }})()
    """
    state = extract_json_object(eval_browser(search_js))
    if state.get("error"):
        raise RuntimeError(state["error"])
    time.sleep(3)

    retrieve_js = f"""
    (() => {{
      const leaf = {json.dumps(leaf)};
      const fullPath = {json.dumps(path)};
      const wrapper = Array.from(document.querySelectorAll('.el-dialog__wrapper, .el-dialog'))
        .find(x => x.offsetParent !== null);
      if (!wrapper) return JSON.stringify({{error: 'no visible category dialog'}});
      const nodes = Array.from(wrapper.querySelectorAll('.el-tree-node'));
      const candidates = [];
      for (const node of nodes) {{
        if (node.offsetParent === null) continue;
        const vue = node.__vue__;
        const data = vue && vue.node && vue.node.data ? vue.node.data : null;
        const label = data && data.label ? data.label : node.innerText;
        const id = data && data.id ? String(data.id) : '';
        const cleanLabel = String(label || '').split('(')[0].trim();
        const cleanLeaf = cleanLabel.split('>').at(-1).split(':').at(-1).trim();
        if (cleanLeaf.toLowerCase() === leaf.toLowerCase() || cleanLabel.toLowerCase().includes(leaf.toLowerCase())) {{
          candidates.push({{id, label: cleanLabel}});
        }}
      }}
      if (!candidates.length) return JSON.stringify({{error: 'category not found', leaf, sample: wrapper.innerText.slice(0, 500)}});
      let chosen = candidates[0];
      const pathParts = fullPath.split(':').map(x => x.trim().toLowerCase()).filter(Boolean);
      for (const c of candidates) {{
        const text = c.label.toLowerCase();
        const matched = pathParts.filter(p => text.includes(p)).length;
        c.matched = matched;
      }}
      candidates.sort((a, b) => (b.matched || 0) - (a.matched || 0));
      chosen = candidates[0];
      let chosenNode = null;
      for (const node of nodes) {{
        if (node.offsetParent === null) continue;
        const vue = node.__vue__;
        const data = vue && vue.node && vue.node.data ? vue.node.data : null;
        const id = data && data.id ? String(data.id) : '';
        if (id === chosen.id) {{
          chosenNode = node;
          break;
        }}
      }}
      if (chosenNode) {{
        const checkboxInput = chosenNode.querySelector('input[type="checkbox"]');
        const checkboxBox = chosenNode.querySelector('.el-checkbox__input, .el-checkbox, label');
        const checked = checkboxInput ? checkboxInput.checked : chosenNode.classList.contains('is-checked');
        if (!checked) {{
          (checkboxInput || checkboxBox || chosenNode).click();
        }}
      }}
      const selectedText = wrapper.innerText;
      const closeBtn = wrapper.querySelector('.el-dialog__close, button[aria-label="Close"], .el-icon-close');
      if (closeBtn) closeBtn.click();
      return JSON.stringify({{
        node_id_path: chosen.id,
        label: chosen.label,
        selected: !!chosenNode,
        selected_text_sample: selectedText.slice(0, 300),
        candidates: candidates.slice(0, 5)
      }});
    }})()
    """
    state = extract_json_object(eval_browser(retrieve_js))
    if state.get("error"):
        raise RuntimeError(f"{state['error']}: {state.get('leaf', '')}")
    node_id_path = state["node_id_path"]
    cache[path] = node_id_path
    print(f"  nodeIdPath: {node_id_path} ({state.get('label', '')})")
    return node_id_path


def scrape_products(limit: int) -> tuple[list[dict], dict]:
    js = f"""
    (() => {{
      const cards = Array.from(document.querySelectorAll('div.relation-card'));
      const rows = Array.from(document.querySelectorAll('table tbody tr'));
      const bodyText = document.body.innerText;
      const products = [];
      if (cards.length > 0) {{
        for (const card of cards) {{
          if (products.length >= {limit}) break;
          const text = card.innerText || '';
          if (!/\\bB0[A-Z0-9]{{8}}\\b/.test(text)) continue;
          const img = card.querySelector('.img');
          const style = img ? img.getAttribute('style') || '' : '';
          const m = style.match(/url\\(["']?([^"')]+)["']?\\)/);
          products.push({{main: text, detail: '', imgUrl: m ? m[1] : ''}});
        }}
      }} else {{
        for (let i = 0; i < rows.length && products.length < {limit}; i += 2) {{
          const main = rows[i]?.innerText || '';
          const detail = rows[i + 1]?.innerText || '';
          if (!main.includes('ASIN:')) continue;
          const img = rows[i].querySelector('.asin-img .img');
          const style = img ? img.getAttribute('style') || '' : '';
          const m = style.match(/url\\(["']?([^"')]+)["']?\\)/);
          products.push({{main, detail, imgUrl: m ? m[1] : ''}});
        }}
      }}
      const totalMatch = bodyText.match(/(?:共|总计|总共)\\s*([\\d,]+)\\s*(?:条|个|件)/);
      const next = document.querySelector('button.btn-next, .pagination .next a, .el-pagination .btn-next');
      const parent = next?.closest('li, button');
      return JSON.stringify({{
        products,
        state: {{
          url: location.href,
          title: document.title,
          visible_items: products.length,
          card_count: cards.length,
          row_count: rows.length,
          reported_total: totalMatch ? Number(totalMatch[1].replaceAll(',', '')) : null,
          next_available: !!next && !next.disabled && next.getAttribute('aria-disabled') !== 'true' && !parent?.classList.contains('disabled'),
          empty_message: ['没有找到','暂无数据','暂无符合','未找到符合','无符合条件'].some(x => bodyText.includes(x)),
          login_required: !!document.querySelector('.login-form, form[action*="login"], input[type="password"]')
        }}
      }});
    }})()
    """
    payload = extract_json_object(eval_browser(js, timeout=60))
    parsed = [
        parse_product(item["main"], item.get("detail", ""), item.get("imgUrl", ""))
        for item in payload.get("products", [])
    ]
    return parsed, payload.get("state", {})


def scan_category(category: dict, node_id_path: str, filters: dict, max_products: int, wait_seconds: float) -> dict:
    url = build_product_url([node_id_path], filters)
    print(f"  opening filtered product URL")
    open_browser(url)
    time.sleep(wait_seconds)
    products, state = scrape_products(max_products)
    return {
        "category": {
            "name": category["name"],
            "name_zh": category.get("name_zh", ""),
            "path": category["path"],
            "node_id_path": node_id_path,
            "score": category.get("score"),
            "risk_flags": category.get("risk_flags", []),
            "category_metrics": category.get("metrics", {}),
        },
        "filters": filters,
        "result_state": state,
        "product_count": len(products),
        "products": products,
    }


def scan_combined(
    categories: list[dict],
    node_cache: dict,
    filters: dict,
    max_products: int,
    wait_seconds: float,
    pages: int = 1,
) -> dict:
    node_id_paths = []
    included = []
    missing = []
    for category in categories:
        path = category["path"]
        node_id_path = node_cache.get(path)
        if node_id_path:
            node_id_paths.append(node_id_path)
            included.append({
                "name": category["name"],
                "name_zh": category.get("name_zh", ""),
                "path": path,
                "node_id_path": node_id_path,
                "score": category.get("score"),
                "risk_flags": category.get("risk_flags", []),
            })
        else:
            missing.append({
                "name": category["name"],
                "name_zh": category.get("name_zh", ""),
                "path": path,
            })

    if not node_id_paths:
        raise RuntimeError("No cached nodeIdPaths available. Run individual scans or --resolve-only first.")

    print(f"  combined categories: {len(included)} included, {len(missing)} missing")
    all_products = []
    seen_asins = set()
    page_states = []
    for page in range(1, max(1, pages) + 1):
        page_filters = dict(filters)
        page_filters["page"] = str(page)
        url = build_product_url(node_id_paths, page_filters)
        print(f"  opening combined filtered product URL page {page}; length={len(url)}")
        open_browser(url)
        time.sleep(wait_seconds)
        products, state = scrape_products(max_products)
        state["page"] = page
        page_states.append(state)
        added = 0
        for product in products:
            asin = product.get("asin") or product.get("parent_asin") or json.dumps(product, sort_keys=True)
            if asin in seen_asins:
                continue
            seen_asins.add(asin)
            product["source_page"] = page
            all_products.append(product)
            added += 1
        print(f"    page {page}: {len(products)} visible, {added} new")
        if not state.get("next_available") and page > 1:
            break
    return {
        "scanned_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "mode": "combined",
        "included_category_count": len(included),
        "missing_category_count": len(missing),
        "included_categories": included,
        "missing_categories": missing,
        "filters": filters,
        "page_states": page_states,
        "product_count": len(all_products),
        "products": all_products,
    }


def main() -> None:
    global SESSION
    parser = argparse.ArgumentParser(description="Scan SellerSprite product candidates for selected category pool.")
    parser.add_argument("--config", default="products/product_scan_config.json")
    parser.add_argument("--start", type=int, default=1, help="1-based category index in target_pool")
    parser.add_argument("--max-categories", type=int, default=0)
    parser.add_argument("--session", default=SESSION)
    parser.add_argument("--resolve-only", action="store_true")
    parser.add_argument(
        "--combined", action="store_true",
        help="Scan all selected categories in one product-research URL using cached nodeIdPaths.",
    )
    parser.add_argument(
        "--print-url", action="store_true",
        help="Print the combined product-research URL and exit. Used with --combined.",
    )
    parser.add_argument("--pages", type=int, default=1, help="Number of pages to fetch in --combined mode.")
    args = parser.parse_args()

    SESSION = args.session

    config_path = Path(args.config)
    config = load_config(config_path)
    policy = config["scan_policy"]
    filters = config["filters"]
    pool_path = (config_path.parent / config["source_category_pool"]).resolve()
    categories = load_category_pool(pool_path)
    start = max(args.start, 1) - 1
    max_categories = args.max_categories or int(policy.get("default_max_categories", 2))
    selected = categories[start:start + max_categories]
    if not selected:
        raise SystemExit("No categories selected.")

    node_cache_path = config_path.parent / policy.get("node_cache", "category_node_paths.json")
    if node_cache_path.exists():
        node_cache = json.loads(node_cache_path.read_text(encoding="utf-8"))
    else:
        node_cache = {}

    if args.combined:
        output_path = config_path.parent / policy.get("combined_output_json", "combined_product_candidates.json")
        if args.print_url:
            included_paths = []
            missing = []
            for category in selected:
                node_id_path = node_cache.get(category["path"])
                if node_id_path:
                    included_paths.append(node_id_path)
                else:
                    missing.append(category)
            if not included_paths:
                raise SystemExit("No cached nodeIdPaths available.")
            url = build_product_url(included_paths, filters)
            print(url)
            print(f"\nIncluded categories: {len(included_paths)}")
            print(f"Missing nodeIdPaths: {len(missing)}")
            for item in missing:
                print(f"  - {item['name']} | {item['path']}")
            return
        result = scan_combined(
            selected,
            node_cache,
            filters,
            int(policy.get("combined_page_size", policy.get("max_products_per_category", 60))),
            float(policy.get("wait_seconds", 8)),
            pages=args.pages,
        )
        output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  saved {result['product_count']} combined products")
        print(f"Products: {output_path}")
        if result["missing_category_count"]:
            print("Missing nodeIdPaths:")
            for item in result["missing_categories"]:
                print(f"  - {item['name']} | {item['path']}")
        return

    output_path = config_path.parent / policy.get("output_json", "product_candidates.json")
    if output_path.exists():
        output = json.loads(output_path.read_text(encoding="utf-8"))
    else:
        output = {
            "source_category_pool": str(pool_path),
            "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "updated_at": "",
            "scan_policy": policy,
            "filters": filters,
            "scans": [],
        }

    for offset, category in enumerate(selected, start=args.start):
        print(f"\\n[{offset}] {category['name']} / {category.get('name_zh', '')}")
        node_id_path = resolve_node_id_path(category, node_cache)
        node_cache_path.write_text(json.dumps(node_cache, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if args.resolve_only:
            continue
        result = scan_category(
            category,
            node_id_path,
            filters,
            int(policy.get("max_products_per_category", 60)),
            float(policy.get("wait_seconds", 8)),
        )
        output["scans"] = [
            scan for scan in output.get("scans", [])
            if scan.get("category", {}).get("path") != category["path"]
        ]
        output["scans"].append(result)
        output["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
        output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  saved {result['product_count']} products")

    print(f"\\nNode cache: {node_cache_path}")
    if not args.resolve_only:
        print(f"Products: {output_path}")


if __name__ == "__main__":
    main()
