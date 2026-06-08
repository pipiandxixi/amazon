#!/usr/bin/env python3
"""Find qualified products inside one exact SellerSprite leaf category."""

from __future__ import annotations

import argparse
import datetime
import json
import re
import time
from pathlib import Path

from scan_common import RESULTS_DIR, OpenCliError, eval_browser, extract_json_array, open_browser


INPUT_INDEXES = {
    "min_monthly_sales": 1,
    "max_monthly_sales": 2,
    "min_sales_growth": 7,
    "max_sales_growth": 8,
    "max_leaf_bsr": 12,
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


def select_category(path: list[str], only_leaf_rank: bool) -> None:
    output = eval_browser(
        """
        (() => {
          const trigger = Array.from(document.querySelectorAll('*')).find(
            x => x.children.length === 0 && x.textContent.trim() === '选择一个或多个类目和子类目'
          );
          if (!trigger) return 'category trigger not found';
          trigger.click();
          return 'opened';
        })()
        """
    )
    if "opened" not in output:
        raise ValueError(output)

    for index, category in enumerate(path):
        time.sleep(1)
        category_json = json.dumps(category)
        is_leaf = index == len(path) - 1
        output = eval_browser(
            f"""
            (() => {{
              const target = {category_json};
              const visible = Array.from(
                document.querySelectorAll('.category-tree .custom-tree-node .label')
              ).filter(
                x => x.textContent.trim().startsWith(target) && x.offsetParent !== null
              );
              if (!visible.length) return 'not found: ' + target;
              const content = visible[0].closest('.el-tree-node__content');
              if (!content) return 'row not found: ' + target;
              if ({str(is_leaf).lower()}) {{
                const checkbox = content.querySelector('input[type=checkbox]');
                if (!checkbox) return 'checkbox not found: ' + target;
                if (!checkbox.checked) checkbox.click();
              }} else {{
                const expand = content.querySelector('.el-tree-node__expand-icon');
                if (!expand) return 'expand control not found: ' + target;
                if (!expand.classList.contains('expanded')) expand.click();
              }}
              return 'clicked: ' + visible[0].textContent.trim();
            }})()
            """
        )
        if "clicked:" not in output:
            raise ValueError(
                f"Could not select category path item '{category}'. "
                "Open SellerSprite once and confirm the category tree is available."
            )

    output = eval_browser(
        """
        (() => {
          const confirm = Array.from(document.querySelectorAll('button')).find(
            x => x.innerText.includes('确认选择') && x.offsetParent !== null
          );
          if (!confirm) return 'confirm not found';
          confirm.click();
          return 'confirmed';
        })()
        """
    )
    if "confirmed" not in output:
        raise ValueError(output)
    time.sleep(2)

    if only_leaf_rank:
        eval_browser(
            """
            (() => {
              const x = document.querySelector('input[value="只看该子类目排名"]');
              if (x && !x.checked) x.click();
              return x ? x.checked : false;
            })()
            """
        )


def apply_filters(filters: dict[str, str]) -> None:
    indexed = {
        str(INPUT_INDEXES[key]): value
        for key, value in filters.items()
        if key in INPUT_INDEXES and value != ""
    }
    fba = filters.get("fulfillment") == "FBA"
    output = eval_browser(
        f"""
        (() => {{
          const values = {json.dumps(indexed)};
          const inputs = Array.from(document.querySelectorAll('input'));
          const setter = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
          for (const [index, value] of Object.entries(values)) {{
            const input = inputs[Number(index)];
            if (!input) return 'missing input index ' + index;
            setter.call(input, String(value));
            input.dispatchEvent(new Event('input', {{ bubbles: true }}));
            input.dispatchEvent(new Event('change', {{ bubbles: true }}));
          }}
          const fba = inputs.find(x => x.value === 'FBA');
          if (fba && fba.checked !== {str(fba).lower()}) fba.click();
          const submit = Array.from(document.querySelectorAll('button')).find(
            x => x.innerText.includes('开始筛选')
          );
          if (!submit) return 'submit not found';
          submit.click();
          return 'submitted';
        }})()
        """
    )
    if "submitted" not in output:
        raise ValueError(output)


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
          const rows = Array.from(document.querySelectorAll('table tbody tr'));
          const products = [];
          for (let i = 0; i < rows.length && products.length < {limit}; i += 2) {{
            const main = rows[i]?.innerText || '';
            const detail = rows[i + 1]?.innerText || '';
            if (!main.includes('ASIN:')) continue;
            products.push({{ main, detail }});
          }}
          return JSON.stringify(products);
        }})()
        """
    )
    raw_products = extract_json_array(output)
    return [parse_product(item["main"], item["detail"]) for item in raw_products]


def parse_product(main: str, detail: str) -> dict[str, str]:
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
    }


def write_report(config: dict, products: list[dict[str, str]], date_str: str) -> Path:
    category = config["category"]["name"]
    slug = re.sub(r"[^a-z0-9]+", "_", category.lower()).strip("_")
    path = RESULTS_DIR / f"product_scan_{slug}_{date_str}.md"
    filters = values(config["filters"])
    md = [
        f"# {category} 合格产品扫描 ({date_str.replace('_', '-')})",
        "",
        f"> 精确类目路径：`{' › '.join(config['category']['path'])}`",
        f"> 筛选参数：`{json.dumps(filters, ensure_ascii=False)}`",
        f"> 共抓取 **{len(products)}** 个独立候选商品。",
        "",
        "| # | ASIN | 商品 | 月销量 / 增长率 | 月销售额 | 价格 | Reviews / 月新增 | 评分 | FBA / 毛利率 | 变体 | 小类排名 | 卖家数 | 包装重量 | 上架时间 |",
        "|---:|---|---|---|---:|---:|---|---:|---|---:|---:|---:|---|---|",
    ]
    for index, product in enumerate(products, 1):
        clean = {k: str(v).replace("|", "\\|").replace("\n", " ") for k, v in product.items()}
        md.append(
            f"| {index} | `{clean['asin']}` | {clean['title']} | "
            f"{clean['monthly_sales']} / {clean['sales_growth']} | {clean['monthly_revenue']} | "
            f"{clean['price']} | {clean['reviews']} / {clean['monthly_new_reviews']} | "
            f"{clean['rating']} | {clean['fba_fee']} / {clean['profit_margin']} | "
            f"{clean['variants']} | {clean['leaf_rank']} | {clean['sellers']} | "
            f"{clean['package_weight']} | {clean['listing_date']} {clean['listing_age']} |"
        )
    md.extend(["", "## 原始数值", ""])
    for product in products:
        md.append(f"- `{product['asin']}`: {product['raw_metrics']}")
    path.write_text("\n".join(md) + "\n", encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="scripts/product_config.json")
    parser.add_argument("--date", default="")
    args = parser.parse_args()
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    date_str = args.date or datetime.date.today().strftime("%Y_%m_%d")
    policy = values(config.get("scan_policy", {}))
    filters = values(config["filters"])

    open_browser("https://www.sellersprite.com/v3/product-research")
    time.sleep(5)
    select_category(config["category"]["path"], policy.get("only_leaf_category_rank", True))
    apply_filters(filters)
    time.sleep(float(policy.get("wait_seconds", 5)))
    if policy.get("hide_variants", True):
        hide_variants()
        time.sleep(3)
    products = scrape_products(int(policy.get("max_products", 20)))
    report = write_report(config, products, date_str)
    print(f"Wrote {len(products)} products to {report}")


if __name__ == "__main__":
    try:
        main()
    except (OpenCliError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Product scan failed: {exc}")
