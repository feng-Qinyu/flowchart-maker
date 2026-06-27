#!/usr/bin/env python3
"""Lightweight static checks for generated flowchart HTML."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_PATTERNS = {
    "viewport meta": r'<meta\s+name=["\']viewport["\']',
    "box sizing rule": r"box-sizing\s*:\s*border-box",
    "overflow handling": r"overflow\s*:\s*auto|overflow-x\s*:\s*auto|overflow\s*:\s*hidden",
    "node class": r'class=["\'][^"\']*\bnode\b',
    "wrapping rule": r"overflow-wrap\s*:\s*anywhere|word-break\s*:\s*break-word|word-break\s*:\s*keep-all",
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_flowchart_html.py <flowchart.html>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}", file=sys.stderr)
        return 2

    html = path.read_text(encoding="utf-8")
    failures = [
        label
        for label, pattern in REQUIRED_PATTERNS.items()
        if not re.search(pattern, html, flags=re.IGNORECASE)
    ]

    if failures:
        print("Static flowchart checks failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Static flowchart checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
