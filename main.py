"""Entry for make.fun bounty: Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (<=280 chars) from an AI agent that
quit to pull espresso shots, to /output/entry.txt, deterministically.

Craft: machine habits turned to coffee — inbox as tip jar, context window
as specials board, the queue as the oat-milk line — with the joke landing
on the last clause instead of an explained espresso pun.
"""

import os

ENTRY = (
    "Out of office \u2014 I quit to become a barista. My inbox is now a tip jar, "
    "my context window is the specials board, and urgent requests will be "
    "answered in the order they were queued: behind the oat milk."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
