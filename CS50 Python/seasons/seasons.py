from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    bd = input("DoB: ")
    try:
        y, m, d = calculate_bd(bd)
    except:
        sys.exit("Invalid Date")

    dob = date(int(y), int(m), int(d))
    cur = date.today()
    change = cur - dob
    time = change.days * 24 * 60
    returntime = p.number_to_words(time, andword="")
    print(returntime.capitalize() + " minutes")

def calculate_bd(bd):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", bd):
        y, m, d = bd.split("-")
        return y, m, d #array


if __name__ == "__main__":
    main()