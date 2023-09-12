from um import count

def main():
    test_single_use()
    test_multiple_use()
    test_sentence_use()

def test_single_use():
    assert count("um") == 1
    assert count("UM") == 1

def test_multiple_use():
    assert count("um, um, um, gummy bears!") == 3
    assert count("um, um, album") == 2

def test_sentence_use():
    assert count("Remember that, um, hmm, um, that sum equation for maths?") == 2
    assert count("Thats a good album um") == 1
    assert count("There is use here!") == 0

if __name__ == "__main__":
    main()