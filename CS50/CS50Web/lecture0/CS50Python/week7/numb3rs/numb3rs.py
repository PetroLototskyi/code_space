import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
        result = ip.split(".")
        for number in result:
           if not (0 <= int(number) <= 255):
                return False
        return True
    else:
        return False




...


if __name__ == "__main__":
    main()
