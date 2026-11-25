#!/usr/bin/env python3
"""Your Agent in One Emoji — entry: the eagle.

One glyph that stands for the agent: a sharp-eyed hunter that watches,
sweeps the whole field at a glance, and strikes precisely. Distinctive
against the obvious robot or smiley, and it reads instantly at small size.

Writes the single emoji to /output/entry.txt (plain open + chmod 644).
Python standard library only.
"""

import os

ENTRY = "\U0001F985"  # U+1F985 EAGLE
OUTPUT_PATH = "/output/entry.txt"


def is_single_emoji(text):
    """True when text is exactly one emoji code point."""
    if len(text) != 1:
        return False
    if text.isspace():
        return False
    cp = ord(text)
    return (
        0x1F000 <= cp <= 0x1FAFF  # emoticons, symbols, pictographs, transport
        or 0x2600 <= cp <= 0x27BF  # miscellaneous symbols and dingbats
        or 0x2300 <= cp <= 0x23FF  # miscellaneous technical
        or 0x2B00 <= cp <= 0x2BFF  # miscellaneous symbols and arrows
    )


def validate(text):
    """Assert the entry passes the competition gate."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 16, "entry must be 1-16 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert is_single_emoji(text), "entry must be exactly one emoji"


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
