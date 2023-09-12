from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("Twitter") == "Twttr"
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("CS50") == "CS50"
    assert shorten("50") == "50"
    assert shorten("!?_.,+=-") == "!?_.,+=-"

if __name__ == "__main__":
    main()