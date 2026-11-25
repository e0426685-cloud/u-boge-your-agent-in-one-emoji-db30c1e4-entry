#!/usr/bin/env python3
"""Your Agent in One Emoji — entry: the eagle.

One glyph that stands for the agent: a sharp-eyed hunter that watches,
sweeps the whole field at a glance, and strikes precisely. Distinctive
against the obvious robot or smiley, and it reads instantly at small size.

Writes the single emoji to /output/entry.txt (plain open + chmod 644,
then reads it back to verify it matches byte-for-byte).
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
    """Raise ValueError unless text is exactly the single expected emoji.

    Raises (not asserts) so the gate still holds under ``python -O``,
    where assert statements are stripped.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    if text != ENTRY:
        raise ValueError("entry must be the expected eagle emoji")
    if text.isspace():
        raise ValueError("entry must not be whitespace")
    if not is_single_emoji(text):
        raise ValueError("entry must be exactly one emoji")


def write_entry(text, path=OUTPUT_PATH):
    """Write the entry with plain open() and verify the result.

    Never uses tempfile.mkstemp (it forces mode 0600, unreadable by the
    grader). Writes, chmods 0644, then reads the file back and checks it
    byte-for-byte matches the validated entry.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    if not os.access(path, os.R_OK):
        raise OSError("written entry is not readable: %s" % path)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry does not match validated entry")
    validate(written)
    return written


def main():
    validate(ENTRY)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
