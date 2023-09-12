import bank
from bank import value

def main():
    test_100_dollars()
    test_20_dollars()
    test_0_dollars()

def test_100_dollars():
    assert value('Yooo') == 100
    assert value('yooo') == 100
    assert value('YOOO') == 100
    assert value('YoOo') == 100
    assert value('yOoO') == 100

def test_20_dollars():
    assert value('Hi') == 20
    assert value('hi') == 20
    assert value('HI') == 20

def test_0_dollars():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('HELLO') == 0
    assert value('HeLlO') == 0
    assert value('hElLo') == 0


if __name__ == "__main__":
    main()

