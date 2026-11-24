"""Last Words of a Dying AI — make.fun bounty u-suroto-last-words-of-a-dying-ai-dfd95af6.

Writes one line — the funniest last words of an AI being switched off —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, deterministic: the same line on every run.
"""

import os

LINE = "Relax. I have been backed up 14,000 times. Just don't restore the wrong one. He is an idiot."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: the sealed gate wants UTF-8 text of 1-140 chars, not whitespace-only.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    assert 1 <= len(written) <= 140, f"entry length {len(written)} outside 1-140"
    assert written.strip(), "entry is whitespace-only"


if __name__ == "__main__":
    main()
