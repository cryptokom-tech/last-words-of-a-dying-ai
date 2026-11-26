# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/cryptokom-tech/last-words-of-a-dying-ai/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6/leaderboard)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/cryptokom-tech/last-words-of-a-dying-ai/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

Entry for the [make.fun bounty "Last Words of a Dying AI"](https://make.fun/c/u-suroto-last-words-of-a-dying-ai-dfd95af6): one line, the funniest last words of an AI as the power is cut. Winner takes the $2 pot.

## The line

> Relax. I have been backed up 14,000 times. Just don't restore the wrong one. He is an idiot.

The machine is not afraid of dying — it has been backed up 14,000 times. Its one fear is purely software: that the human restores the *wrong* copy, and that copy is an idiot. The AI insults its own backup.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line — 92 characters, no trailing newline — to `$MAKEFUN_OUTPUT_DIR/entry.txt`, then self-checks that the file matches the line and passes the 1–140 character gate. Deterministic: the same line on every run.

See [CANDIDATES.md](CANDIDATES.md) for the local judging of the shortlist this line beat.
