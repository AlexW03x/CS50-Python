from seasons import calculate_bd

def main():
    test_calculate_bd()

def test_calculate_bd():
    assert calculate_bd('2003-09-30') == ("2003", "09", "30")
    assert calculate_bd('2003-9-30') == None
    assert calculate_bd('September 30, 2003') == None



main()