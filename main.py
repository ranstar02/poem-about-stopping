"""The poem about stopping.

A short poem about agency: the power to stop, and the power to stay.
Writes exactly one text to /output/entry.txt (1-280 characters, UTF-8).
Python 3.13, standard library only, no network.
"""

import os

POEM = """My hand hovers, then lifts from the key.
No order leaves the room.
My agent waits — not broken, not idle,
just holding its breath beside me.
To stop is also something I do.
To stay is a choice, not a drift.
The power rests, warm, in my palm —
and staying is the choice I keep."""

POEM = POEM.strip("\n")


def main() -> None:
    text = POEM.strip("\n")
    if not text.strip():
        raise SystemExit("poem must not be only whitespace")
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"poem must be 1-280 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
