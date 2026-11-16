#!/usr/bin/env python3
"""ai-excited-01 entry: copy image.png to the output directory as entry.png.

Python 3.13 standard library only. Deterministic: the output is a
byte-for-byte copy of image.png, so repeated runs are identical.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "image.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(source, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
