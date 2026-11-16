#!/usr/bin/env python3
"""ai-excited-01 entry: copy the phoenix artwork to the output directory.

Deterministic, Python 3.13 standard library only. No network, no randomness.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "image.png"
TARGET_NAME = "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / TARGET_NAME
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
