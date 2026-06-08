#!/usr/bin/env python3
"""Merge non-empty targeted keyword results into matching market-report details."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


KEYWORD_BLOCK_RE = re.compile(
    r"\n*<!-- KEYWORDS_START -->.*?<!-- KEYWORDS_END -->\n*",
    re.DOTALL,
)
KEYWORD_SECTION_RE = re.compile(
    r"^## (?P<name>.+?) \((?P<captured>\d+) captured; query total "
    r"(?P<total>\d+)\)\n(?P<body>.*?)(?=^## |\Z)",
    re.MULTILINE | re.DOTALL,
)
MARKET_DETAIL_RE = re.compile(
    r"(?P<body>^#### 🏆 🟢-\d+\. (?P<name>.+?) \([^\n]*\)\n.*?)"
    r"(?P<separator>\n---\n)",
    re.MULTILINE | re.DOTALL,
)


def latest_report(directory: Path, pattern: str) -> Path:
    reports = sorted(directory.glob(pattern))
    if not reports:
        raise FileNotFoundError(f"No report matching {directory / pattern}")
    return reports[-1]


def parse_keyword_sections(report: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for match in KEYWORD_SECTION_RE.finditer(report):
        captured = int(match.group("captured"))
        if captured == 0:
            continue

        body_lines = match.group("body").strip().splitlines()
        seeds = next((line for line in body_lines if line.startswith("> Seeds:")), "")
        table_start = next(
            (index for index, line in enumerate(body_lines) if line.startswith("| 序号 |")),
            None,
        )
        if table_start is None:
            raise ValueError(f"Missing keyword table for {match.group('name')}")

        table_lines: list[str] = []
        for line in body_lines[table_start:]:
            if not line.startswith("|"):
                break
            table_lines.append(line)

        sections[match.group("name")] = "\n".join(
            [
                "<!-- KEYWORDS_START -->",
                "##### 推荐关键词（定向扫描）",
                "",
                seeds,
                f"> 当前筛选条件下推荐 **{captured}** 个关键词。",
                "",
                *table_lines,
                "<!-- KEYWORDS_END -->",
            ]
        )
    return sections


def merge_reports(market_report: str, keyword_sections: dict[str, str]) -> tuple[str, set[str]]:
    market_report = KEYWORD_BLOCK_RE.sub("\n\n", market_report)
    merged: set[str] = set()

    def add_keywords(match: re.Match[str]) -> str:
        name = match.group("name")
        block = keyword_sections.get(name)
        if not block:
            return match.group(0)
        merged.add(name)
        return f"{match.group('body').rstrip()}\n\n{block}{match.group('separator')}"

    return MARKET_DETAIL_RE.sub(add_keywords, market_report), merged


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge non-empty keyword recommendations into market category details."
    )
    parser.add_argument("--market-report", type=Path)
    parser.add_argument("--keyword-report", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parents[1]
    market_path = args.market_report or latest_report(
        root / "results", "market_scan_report_*.md"
    )
    keyword_path = args.keyword_report or latest_report(
        root / "results/keywords", "keyword_scan_report_*.md"
    )

    keyword_sections = parse_keyword_sections(keyword_path.read_text(encoding="utf-8"))
    merged_report, merged = merge_reports(
        market_path.read_text(encoding="utf-8"), keyword_sections
    )
    market_path.write_text(merged_report, encoding="utf-8")

    unmatched = sorted(set(keyword_sections) - merged)
    print(f"Merged {len(merged)} keyword groups into {market_path}")
    if unmatched:
        print(f"Unmatched keyword groups ({len(unmatched)}): {', '.join(unmatched)}")


if __name__ == "__main__":
    main()
