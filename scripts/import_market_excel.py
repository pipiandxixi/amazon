import argparse
import re
from pathlib import Path
from xml.etree import ElementTree
from zipfile import ZipFile


XML_NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
SECTION_TITLE = "## 四、SellerSprite Excel 导出完整字段"


def column_index(reference):
    letters = re.match(r"[A-Z]+", reference).group(0)
    result = 0
    for letter in letters:
        result = result * 26 + ord(letter) - ord("A") + 1
    return result - 1


def read_sheet(path):
    with ZipFile(path) as workbook:
        shared_root = ElementTree.fromstring(workbook.read("xl/sharedStrings.xml"))
        shared_strings = [
            "".join(node.text or "" for node in item.findall(".//x:t", XML_NS))
            for item in shared_root.findall("x:si", XML_NS)
        ]
        sheet_root = ElementTree.fromstring(workbook.read("xl/worksheets/sheet1.xml"))

    rows = []
    for row in sheet_root.findall(".//x:sheetData/x:row", XML_NS):
        values = {}
        for cell in row.findall("x:c", XML_NS):
            value_node = cell.find("x:v", XML_NS)
            value = "" if value_node is None else value_node.text
            if cell.get("t") == "s" and value:
                value = shared_strings[int(value)]
            values[column_index(cell.get("r"))] = value
        rows.append(values)
    return rows


def build_headers(group_row, header_row):
    max_column = max(header_row)
    headers = []
    current_group = ""
    for index in range(max_column + 1):
        if group_row.get(index):
            current_group = group_row[index]
        label = header_row.get(index, f"Column {index + 1}")
        headers.append(f"{current_group} / {label}" if current_group else label)
    return headers


def clean(value):
    return str(value or "-").replace("\n", " <br> ").replace("|", "\\|").strip()


def category_names_from_report(report):
    names = set()
    for match in re.finditer(r"^\| \d+ \| \*\*(.+?)\*\* \|", report, re.MULTILINE):
        names.add(match.group(1).strip())
    return names


def main():
    parser = argparse.ArgumentParser(description="Append SellerSprite Excel fields to market report")
    parser.add_argument("excel", help="Path to SellerSprite market-research XLSX export")
    parser.add_argument("--report", default="results/categories/market_scan_report_2026_06_08.md")
    args = parser.parse_args()

    rows = read_sheet(args.excel)
    headers = build_headers(rows[0], rows[1])
    data_rows = rows[2:]

    report_path = Path(args.report)
    report = report_path.read_text(encoding="utf-8")
    report = report.split(SECTION_TITLE, 1)[0].rstrip()
    report_names = category_names_from_report(report)
    excel_names = {row.get(0, "").strip() for row in data_rows if row.get(0, "").strip()}
    matched = len(report_names & excel_names)

    output = [
        report,
        "",
        SECTION_TITLE,
        "",
        f"> 来源：`{Path(args.excel).name}`",
        f"> Excel 包含 **{len(data_rows)}** 个类目、**{len(headers)}** 个字段；其中 **{matched}** 个类目名称可与当前市场报告直接匹配。",
        "",
    ]
    for row in data_rows:
        name = row.get(0, "").strip() or "Unknown"
        translated = row.get(1, "").strip()
        output.append(f"### {name} ({translated})")
        output.append("")
        output.append("| 字段 | 值 |")
        output.append("| :--- | :--- |")
        for index, header in enumerate(headers):
            output.append(f"| {clean(header)} | {clean(row.get(index, ''))} |")
        output.append("")

    report_path.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")
    print(f"Appended {len(data_rows)} categories and {len(headers)} fields to {report_path}")
    print(f"Matched report category names: {matched}")


if __name__ == "__main__":
    main()
