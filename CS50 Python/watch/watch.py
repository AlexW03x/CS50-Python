import sys
import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search("<iframe(.)*><\/iframe>", s):
        youtube_url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s)
        if youtube_url:
            return "https://youtu.be/" + youtube_url.groups()[3]

if __name__ == "__main__":
    main()