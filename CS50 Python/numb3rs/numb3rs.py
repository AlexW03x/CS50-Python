import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        separate = ip.split(".")
        for i in separate:
            if int(i) < 0 or int(i) > 255:
                return False

        return True
    else:
        return False


if __name__ == "__main__":
    main()