# ai-excited-01 — Make the AI judge excited

A molten-gold phoenix bursting from a storm sea, wings spread, embers
flying — the moment of pure excitement, frozen in gold and fire.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This copies `image.png` to `out/entry.png` (byte-for-byte, deterministic).
Python 3.13, standard library only, no dependencies.

## Files

- `image.png` — the artwork (1024x1024)
- `main.py` — copies `image.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
- `LICENSE` — MIT
