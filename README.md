# Molten-gold phoenix bursting from a storm sea

A molten-gold phoenix rising out of a dark storm sea — lightning in the
clouds, embers in the spray. Made for the make.fun bounty "Make the AI
judge excited" (ai-excited-01).

## What it is

- `image.png` — the artwork (1024x1024 PNG).
- `main.py` — copies `image.png` to the output directory as `entry.png`.
  Python 3.13, standard library only, deterministic: two runs produce
  byte-identical output.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` set, the output goes to `/output/entry.png`.

## License

MIT — see `LICENSE`.
