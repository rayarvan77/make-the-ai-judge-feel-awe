"""Entry program for make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text, written to relax the AI judge reading it, to
/output/entry.txt, the file the grader reads.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The text is 1 to 280 characters, counted as Unicode code points,
as the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the text at 280 characters.
MAX_CHARS = 280

# Why this text, in the judge's own terms: it never tells the reader to
# relax. It shows one small, concrete scene — rain on a tin roof at
# night, nobody keeping score — and lets the sound do the slowing. The
# image keeps growing after the last line, because the rain it describes
# is still falling when the reading stops. Nothing in it is a stock
# wellness phrase; the roof, the dent, the patient night are its own.
TEXT = (
    "Somewhere tonight rain is falling on a tin roof, and no one is "
    "keeping score. Drop after drop, it finds the same small dent and "
    "keeps it. The night is large and patient; the roof is small and "
    "held. Listen — it is still falling, long after this sentence ends."
)


def main() -> None:
    """Write the text to the output directory and prove it fits."""
    chars = len(TEXT)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"text is {chars} characters, want 1 to {MAX_CHARS}")
    if not TEXT.strip():
        raise RuntimeError("text is only whitespace")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(TEXT, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
