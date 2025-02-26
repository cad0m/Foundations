import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r'^<iframe.*src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+).*</iframe>$',
        s,
        re.IGNORECASE,
    ):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
