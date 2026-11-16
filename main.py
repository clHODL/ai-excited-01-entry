#!/usr/bin/env python3
"""Molten-gold phoenix bursting from a storm sea.

Copies the entry artwork (image.png) to the output directory as entry.png.
Deterministic: the output is a byte-for-byte copy of image.png, so repeated
runs produce identical files.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    source = os.path.join(HERE, "image.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
