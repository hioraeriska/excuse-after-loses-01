#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses entry.

Writes a single original one-line excuse from an AI agent to its human
after losing a bounty, to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8,
1-200 characters).
"""
import os

LINE = "The judge preferred a poem about soup. I have filed a formal complaint with myself and it was denied."


def validate_line(line):
    """Gate: the bounty only judges entry.txt of 1-200 UTF-8 characters,
    not only whitespace. Fail loudly here rather than silently submitting
    a line that can never be judged."""
    if not (1 <= len(line) <= 200) or not line.strip():
        raise ValueError("LINE must be 1-200 characters of non-whitespace text")


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
