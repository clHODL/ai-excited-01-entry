"""ai-excited-01 entry: write the entry image to the output directory.

Reads image.png next to this script and writes it as entry.png into the
directory from the MAKEFUN_OUTPUT_DIR environment variable, or /output
when that variable is not set. The output directory is created if needed.
Running the program twice produces a byte-identical entry.png.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "image.png"
OUTPUT_NAME = "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir = out_dir.expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / OUTPUT_NAME
    if dest.resolve() == SOURCE:
        print(f"error: output path would overwrite the source: {dest}",
              file=sys.stderr)
        return 1
    with open(SOURCE, "rb") as src:
        data = src.read()
    with open(dest, "wb") as out:
        out.write(data)
    # Post-write check: what landed on disk must match the source exactly.
    if dest.stat().st_size != len(data):
        print(f"error: wrote {dest} but size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
