#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261119.

Writes the front-page image that sums up Thursday 19 November 2026
to the grader's output directory. The image is stored beside this file
as entry.png; this program only copies it, byte for byte, so the two
grading runs produce identical output.

Standard library only. No network. Deterministic.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: {SOURCE} is missing", file=sys.stderr)
        return 1
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    got = TARGET.stat().st_size
    want = SOURCE.stat().st_size
    if got != want:
        print(f"error: {TARGET} is {got} bytes, expected {want}", file=sys.stderr)
        return 1
    print(f"wrote {TARGET} ({got} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
