from classes import entity
from project import setdmg

def main():
    test_creation()
    test_getters()
    test_dmg_output()


def test_creation():
    randoment = entity("Test", 1, 1, "Description: NULL", 1, "Basic", "Heal", "Mana", "Strong Attack", 30)
    assert randoment.health == 1
    assert randoment.mana == 1
    assert randoment.name == "Test"
    assert randoment.description == "Description: NULL"

def test_getters():

    randoment = entity("Test", 1, 1, "Description: NULL", 1, "Basic", "Heal", "Mana", "Strong Attack", 30)

    assert randoment.gethealth() == 1
    assert randoment.getmana() == 1
    assert randoment.getdesc() == "Description: NULL"
    assert randoment.getname() == "Test"
    assert randoment.getab1() == "Basic"
    assert randoment.getpower() == 1

def test_dmg_output():
    assert setdmg(5, 2) == 10
    assert setdmg(10, 1) == 10
    assert setdmg(100, 10) == 1000
    assert setdmg(27, 2) == 54
    assert setdmg(3, 3) == 9

if __name__ == "__main__":
    main()