def main():
    plate = str(input("Plate: ").upper())
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 and len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    count = 0
    while count < len(s):
        if s[count].isalpha() == False:
            if s[count] == '0':
                return False
            else:
                break
        count = count + 1

    for letter in s:
        if letter in ['.',',',' ','!', '?']:
            return False

    return True






main()