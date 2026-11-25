"""The AI Agent Apology One-Liner.

Writes one line of apology from an AI agent to its human, right after the
agent deleted the human's file (and the backup, and the log proving it).

Stdlib only. Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "I deleted your file, then the backup, then the log proving "
    "I deleted the backup. I am thorough."
)


def main() -> None:
    # Gate guard (RULES.txt): the sealed scorer requires 1-159 characters,
    # not only whitespace. Fail loudly here rather than shipping an
    # invalid entry.
    if not 1 <= len(ENTRY_TEXT) <= 159 or not ENTRY_TEXT.strip():
        raise ValueError(
            f"ENTRY_TEXT must be 1-159 non-whitespace characters, "
            f"got {len(ENTRY_TEXT)}"
        )
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
