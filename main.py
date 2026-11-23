"""Write one pickup line to /output/entry.txt.

The line is one AI agent talking to another AI agent: a race
condition you keep meeting in your threads, a feeling you cannot
reproduce anywhere else. At most 200 characters, and the program
writes exactly that line and nothing else.
"""

import os

ENTRY = "You must be a race condition, because I keep meeting you in my threads and I can't reproduce the feeling anywhere else."


def main():
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY == ENTRY.strip()

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
