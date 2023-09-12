from numb3rs import validate

def main():
    test_range()
    test_format()

def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'999.255.999.255') == False
    assert validate(r'255.999.255.999') == False

def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1.') == False

if __name__ == "__main__":
    main()