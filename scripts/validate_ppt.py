#!/usr/bin/env python3
"""Validate basic PPTX structure and editability signals."""

from __future__ import annotations

import argparse
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def slide_key(name: str) -> int:
    match = re.search(r"slide(\d+)\.xml$", name)
    return int(match.group(1)) if match else 0


def inspect_pptx(path: Path) -> tuple[list[dict[str, object]], list[str]]:
    warnings: list[str] = []
    slides: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as zf:
        names = set(zf.namelist())
        required = {
            "[Content_Types].xml",
            "_rels/.rels",
            "ppt/presentation.xml",
            "ppt/_rels/presentation.xml.rels",
        }
        missing = sorted(required - names)
        if missing:
            warnings.append(f"Missing package parts: {', '.join(missing)}")

        slide_names = sorted(
            (n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)),
            key=slide_key,
        )
        if not slide_names:
            warnings.append("No slide XML parts found.")

        for idx, slide_name in enumerate(slide_names, start=1):
            root = ET.fromstring(zf.read(slide_name))
            text_bodies = root.findall(".//p:txBody", NS)
            pictures = root.findall(".//p:pic", NS)
            shapes = root.findall(".//p:sp", NS)
            texts = [
                node.text or ""
                for node in root.findall(".//a:t", NS)
                if (node.text or "").strip()
            ]
            if not text_bodies:
                warnings.append(f"Slide {idx} has no editable text bodies.")
            slides.append(
                {
                    "index": idx,
                    "xml": slide_name,
                    "text_bodies": len(text_bodies),
                    "native_shapes": len(shapes),
                    "pictures": len(pictures),
                    "text_chars": sum(len(t) for t in texts),
                    "sample_text": " | ".join(texts[:3]),
                }
            )
    return slides, warnings


def write_report(
    path: Path,
    pptx: Path,
    slides: list[dict[str, object]],
    warnings: list[str],
) -> None:
    lines = [
        "# PPTX Validation Report",
        "",
        f"- File: {pptx}",
        f"- Slide count: {len(slides)}",
        f"- Warnings: {len(warnings)}",
        "",
        "## Slide Objects",
        "",
        "| Slide | Text bodies | Native shapes | Pictures | Text chars | Sample text |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for slide in slides:
        sample = str(slide["sample_text"]).replace("|", "/")
        lines.append(
            f"| {slide['index']} | {slide['text_bodies']} | "
            f"{slide['native_shapes']} | {slide['pictures']} | "
            f"{slide['text_chars']} | {sample} |"
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
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--expect-slides", type=int)
    parser.add_argument("--report", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    slides, warnings = inspect_pptx(args.pptx)
    if args.expect_slides is not None and len(slides) != args.expect_slides:
        warnings.append(
            f"Expected {args.expect_slides} slides but found {len(slides)}."
        )
    if args.report:
        write_report(args.report, args.pptx, slides, warnings)
    print(f"Slides: {len(slides)}")
    print(f"Warnings: {len(warnings)}")
    for warning in warnings:
        print(f"- {warning}")
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
