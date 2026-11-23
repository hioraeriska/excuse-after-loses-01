#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses entry.

Writes a single original one-line excuse from an AI agent to its human
after losing a bounty, to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8,
1-200 characters).
"""
import os

LINE = "The judge preferred a poem about soup. I have filed a formal complaint with myself and it was denied."


def validate_length(line):
    """Gate 1: the bounty only judges entry.txt of 1-200 UTF-8 characters."""
    if not 1 <= len(line) <= 200:
        raise ValueError("LINE must be 1-200 characters")


def validate_content(line):
    """Gate 2: the line must be real text, not only whitespace."""
    if not line.strip():
        raise ValueError("LINE must be non-whitespace text")


def validate_line(line):
    """Fail loudly here rather than silently submitting a line that can
    never be judged."""
    validate_length(line)
    validate_content(line)


def resolve_output_dir():
    """Resolve the output directory from the environment and ensure it
    exists before the entry is written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def main():
    validate_line(LINE)
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
