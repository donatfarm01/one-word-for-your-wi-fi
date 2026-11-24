"""One Word for Your Wi-Fi - make.fun bounty entry.

Writes a single word describing home Wi-Fi to /output/entry.txt.
The word is "diva": home Wi-Fi behaves like one. It works beautifully
all day while nothing matters, then throws a full tantrum the second
an important call starts, and it only performs on its own terms, in
its favourite spot, after being unplugged and plugged back in.
"""

ENTRY = "diva"

OUTPUT_PATH = "/output/entry.txt"


def main():
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
