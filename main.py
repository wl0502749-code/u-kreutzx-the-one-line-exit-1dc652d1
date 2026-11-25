#!/usr/bin/env python3
"""The One-Line Exit: write one funny single-line resignation letter.

The harness runs this program with no network; it writes exactly one line
of UTF-8 text, 1-140 characters, to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set).
"""

import os

# One-line resignation letter: a specific voice (the office worker vs. the
# printer), a surprise turn at the end, no padding, no grievance list.
# Trimmed after the self-test: the first draft ran 154 chars, over the
# 140-char gate, so the tail ("and stop working here") was cut — the joke
# lands harder when the punchline is the last word.
ENTRY = (
    "I hereby resign, effective immediately \u2014 the office printer has "
    "jammed 47 times this year, and I have decided to follow its example."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
