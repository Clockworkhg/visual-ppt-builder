#!/usr/bin/env python3
"""Validate visual draft images before PPT reconstruction."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def parse_ratio(value: str) -> float:
    if ":" in value:
        left, right = value.split(":", 1)
        return float(left) / float(right)
    return float(value)


def inspect_drafts(
    drafts_dir: Path,
    expected_ratio: float,
    tolerance: float,
) -> tuple[list[dict[str, object]], list[str]]:
    warnings: list[str] = []
    rows: list[dict[str, object]] = []
    files = sorted(p for p in drafts_dir.iterdir() if p.suffix.lower() in IMAGE_EXTS)
    if not files:
        warnings.append(f"No draft images found in {drafts_dir}.")
    for path in files:
        with Image.open(path) as image:
            width, height = image.size
        ratio = width / height if height else 0
        ok = abs(ratio - expected_ratio) <= tolerance
        if not ok:
            warnings.append(
                f"{path.name}: ratio {ratio:.4f} is outside tolerance "
                f"for expected {expected_ratio:.4f}."
            )
        rows.append(
            {
                "file": path.name,
                "width": width,
                "height": height,
                "ratio": ratio,
                "ok": ok,
            }
        )
    return rows, warnings


def write_report(path: Path, rows: list[dict[str, object]], warnings: list[str]) -> None:
    lines = [
        "# Visual Draft Validation Report",
        "",
        f"- Draft count: {len(rows)}",
        f"- Warnings: {len(warnings)}",
        "",
        "| File | Width | Height | Ratio | OK |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            f"| {row['file']} | {row['width']} | {row['height']} | "
            f"{float(row['ratio']):.4f} | {row['ok']} |"
        )
    lines.append("")
    if warnings:
        lines.append("## Warnings")
        lines.extend(f"- {warning}" for warning in warnings)
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drafts_dir", type=Path)
    parser.add_argument("--expect-count", type=int)
    parser.add_argument("--ratio", default="16:9")
    parser.add_argument("--tolerance", type=float, default=0.015)
    parser.add_argument("--report", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    expected_ratio = parse_ratio(args.ratio)
    rows, warnings = inspect_drafts(args.drafts_dir, expected_ratio, args.tolerance)
    if args.expect_count is not None and len(rows) != args.expect_count:
        warnings.append(
            f"Expected {args.expect_count} draft images but found {len(rows)}."
        )
    if args.report:
        write_report(args.report, rows, warnings)
    print(f"Drafts: {len(rows)}")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"- {warning}")
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
