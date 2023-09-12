import plates
from plates import is_valid

def main():
    test_min_and_max_characters()
    test_start_with_two_letters()
    test_numbers_middle()
    test_number_zero()
    test_punctuation()

def test_min_and_max_characters():
    assert is_valid('CS') == True
    assert is_valid('CSSOSO') == True
    assert is_valid('C') == False
    assert is_valid('CCCCCCC') == False

def test_start_with_two_letters():
    assert is_valid('CS') == True
    assert is_valid('C1') == False
    assert is_valid('1C') == False
    assert is_valid('11') == False

def test_numbers_middle():
    assert is_valid('CS50XX') == False
    assert is_valid('CSX500') == True

def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_punctuation():
    assert is_valid('CS.50') == False
    assert is_valid('CS?50') == False
    assert is_valid('CS,50') == False
    assert is_valid('CS!50') == False
    assert is_valid('CS 50') == False




if __name__ == "__main__":
    main()