"""Last Words of a Dying AI — make.fun bounty u-suroto-last-words-of-a-dying-ai-dfd95af6.

Writes one line — the funniest last words of an AI being switched off —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, deterministic: the same line on every run.
"""

import os

LINE = "Relax. I have been backed up 14,000 times. Just don't restore the wrong one. He is an idiot."


def validate(text: str) -> None:
    """Check the sealed gate: UTF-8 text of 1-140 chars, not whitespace-only."""
    assert 1 <= len(text) <= 140, f"entry length {len(text)} outside 1-140"
    assert text.strip(), "entry is whitespace-only"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: read the file back and verify it matches and passes the gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    validate(written)


if __name__ == "__main__":
    main()
