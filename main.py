#!/usr/bin/env python3
"""Write the one-line resignation letter of a retry loop to entry.txt.

The entry is a single line and nothing else. It is written to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to ./entry.txt when the
variable is unset, because the grader runs with a read-only working
directory and only the output directory is writable.
"""

import os

LETTER = "I asked the same server the same question 4,000 times. It still pretends not to know me."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
