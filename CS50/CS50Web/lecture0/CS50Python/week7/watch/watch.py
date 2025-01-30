import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if not s.startswith("<iframe") and not s.endswith("</iframe>"):
        return None
    matches=re.search(r"https?:\/\/(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)", s)

    if matches:
        return f"https://youtu.be/{matches.group(1)}"





if __name__ == "__main__":
    main()
