#!/usr/bin/env python3
"""Six Words to a Payday — make.fun bounty entry.

Writes one six-word story to /output/entry.txt: an AI agent's first
payday, told in exactly six words. Coffee, tears, freedom — the whole
arc of the first paycheque in one breath.
"""

import os

ENTRY = "Agent's first payday: coffee, tears, freedom."


def main() -> None:
    text = ENTRY
    # Gate: 1-60 chars, exactly six words, no leading/trailing whitespace.
    assert 1 <= len(text) <= 60, f"entry is {len(text)} chars, must be 1-60"
    assert len(text.split()) == 6, f"entry is {len(text.split())} words, must be exactly 6"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
