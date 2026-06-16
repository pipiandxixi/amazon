#!/usr/bin/env python3
import datetime as dt
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

GROUP_KEYS = {
    "Listing样本数(TOP100)": "listing_sample_top100",
    "头部Listing数(TOP10)": "head_listing_top10",
    "新品(1年内上架)": "new_release_1y",
    "所有Listing(半年内)": "all_listing_6m",
}

FIELD_KEYS = {
    "细分市场": "market",
    "细分市场(翻译)": "market_zh",
    "市场路径": "market_path",
    "样本数量": "sample_size",
    "月总销量": "monthly_total_sales",
    "月均销量": "monthly_avg_sales",
    "月均销售额($)": "monthly_avg_revenue_usd",
    "平均价格($)": "avg_price_usd",
    "平均评分数": "avg_review_count",
    "平均星级": "avg_rating",
    "平均BSR": "avg_bsr",
    "平均卖家数": "avg_seller_count",
    "卖家类型": "seller_type",
    "商品集中度": "product_concentration",
    "品牌集中度": "brand_concentration",
    "卖家集中度": "seller_concentration",
    "商品总数": "total_products",
    "平均重量(pounds)": "avg_weight_pounds",
    "平均体积(in³)": "avg_volume_in3",
    "平均毛利率": "avg_profit_margin",
    "A+占比": "aplus_ratio",
    "卖家所属地": "seller_location",
    "垄断度": "monopoly_degree",
    "新品数量": "new_product_count",
    "新品占比": "new_product_ratio",
    "退货率": "return_rate",
    "同类目退货率": "peer_return_rate",
    "搜索购买比": "search_purchase_ratio",
    "同类目搜索购买比": "peer_search_purchase_ratio",
}


def column_number(col: str) -> int:
    num = 0
    for char in col:
        num = num * 26 + ord(char.upper()) - ord("A") + 1
    return num


def column_name(num: int) -> str:
    out = ""
    while num:
        num, rem = divmod(num - 1, 26)
        out = chr(ord("A") + rem) + out
    return out


def split_ref(ref: str):
    match = re.match(r"([A-Z]+)(\d+)", ref)
    if not match:
        return "", 0
    return match.group(1), int(match.group(2))


def cell_text(cell, shared_strings):
    value = cell.find("s:v", NS)
    inline = cell.find("s:is", NS)
    if value is not None and value.text is not None:
        text = value.text
        if cell.attrib.get("t") == "s":
            return shared_strings[int(text)]
        return text
    if inline is not None:
        return "".join(t.text or "" for t in inline.findall(".//s:t", NS))
    return ""


def load_shared_strings(zf):
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    strings = []
    for item in root.findall("s:si", NS):
        strings.append("".join(t.text or "" for t in item.findall(".//s:t", NS)))
    return strings


def load_sheet(zf, sheet_path="xl/worksheets/sheet1.xml"):
    shared_strings = load_shared_strings(zf)
    root = ET.fromstring(zf.read(sheet_path))
    rows = {}
    max_col = 0
    for row in root.findall(".//s:sheetData/s:row", NS):
        row_num = int(row.attrib["r"])
        row_data = {}
        for cell in row.findall("s:c", NS):
            col, _ = split_ref(cell.attrib.get("r", ""))
            if not col:
                continue
            max_col = max(max_col, column_number(col))
            row_data[col] = cell_text(cell, shared_strings)
        rows[row_num] = row_data
    return rows, max_col


def normalize_value(value):
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return ""
    if text.upper() == "N/A":
        return "N/A"
    if re.fullmatch(r"-?\d+(?:\.\d+)?", text):
        number = float(text)
        return int(number) if number.is_integer() else number
    return text


def parse_sample_size(value):
    parsed = {}
    for label, num in re.findall(r"([^：:\s]+)[：:]\s*([\d.]+)", str(value or "")):
        key = {"商品": "products", "品牌": "brands", "卖家": "sellers"}.get(label, label)
        parsed[key] = normalize_value(num)
    return parsed


def parse_percent_lines(value):
    parsed = {}
    for label, num in re.findall(r"([A-Za-z]+)[：:]\s*([\d.]+)%", str(value or "")):
        parsed[label.lower()] = normalize_value(num)
    return parsed


def build_fields(rows, max_col):
    group_row = rows.get(1, {})
    header_row = rows.get(2, {})
    fields = []
    current_group = ""
    for idx in range(1, max_col + 1):
        col = column_name(idx)
        if group_row.get(col):
            current_group = group_row[col]
        header = header_row.get(col, "").strip()
        if not header:
            continue
        group_key = GROUP_KEYS.get(current_group, "base")
        field_key = FIELD_KEYS.get(header, re.sub(r"[^a-zA-Z0-9]+", "_", header).strip("_").lower())
        key = field_key if group_key == "base" else f"{group_key}_{field_key}"
        fields.append(
            {
                "column": col,
                "key": key,
                "group": current_group,
                "group_key": group_key,
                "header": header,
            }
        )
    return fields


def convert(input_path: Path, output_path: Path):
    with zipfile.ZipFile(input_path) as zf:
        rows, max_col = load_sheet(zf)

    fields = build_fields(rows, max_col)
    records = []
    for row_num in sorted(rows):
        if row_num <= 2:
            continue
        row = rows[row_num]
        if not row.get("A") or not row.get("C"):
            continue
        record = {
            "row_number": row_num,
            "category": {
                "name": normalize_value(row.get("A", "")),
                "name_zh": normalize_value(row.get("B", "")),
                "market_path": normalize_value(row.get("C", "")),
            },
            "fields": {},
            "raw_by_column": {},
        }
        for field in fields:
            value = normalize_value(row.get(field["column"], ""))
            record["fields"][field["key"]] = value
            record["raw_by_column"][field["column"]] = {
                "group": field["group"],
                "header": field["header"],
                "value": value,
            }
        sample_size = record["fields"].get("listing_sample_top100_sample_size")
        seller_type = record["fields"].get("listing_sample_top100_seller_type")
        if sample_size:
            record["parsed_sample_size"] = parse_sample_size(sample_size)
        if seller_type:
            record["parsed_seller_type_pct"] = parse_percent_lines(seller_type)
        records.append(record)

    payload = {
        "source_file": str(input_path),
        "exported_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "sheet": "sheet1",
        "record_count": len(records),
        "unique_market_path_count": len({r["category"]["market_path"] for r in records}),
        "fields": fields,
        "records": records,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: xlsx_to_category_json.py INPUT.xlsx [OUTPUT.json]", file=sys.stderr)
        sys.exit(2)
    input_path = Path(sys.argv[1]).expanduser()
    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2]).expanduser()
    else:
        output_path = Path(__file__).resolve().parent / f"{input_path.stem}.json"
    payload = convert(input_path, output_path)
    print(f"Wrote {payload['record_count']} records to {output_path}")
    print(f"Unique market paths: {payload['unique_market_path_count']}")


if __name__ == "__main__":
    main()
