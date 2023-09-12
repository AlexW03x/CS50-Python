def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    newvalue = str.replace(d, "$", "")
    newvalue2 = str.replace(newvalue, "£", "")
    newvalue3 = str.replace(newvalue2, "%", "")
    newvalue4 = float(newvalue3)
    print(str(newvalue4))
    return newvalue4


def percent_to_float(p):
    newvalue = str.replace(p, "%", "")
    newvalue2 = float(newvalue)/100
    print(str(newvalue2))
    return newvalue2


main()