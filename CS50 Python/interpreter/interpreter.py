def maths():
    in2 = input("Calculation: ")
    in3 = str.replace(in2, " ", "")
    get = 0

    if "+" in in3 and "+" not in in3[0]:
        get = in3.index("+")
    elif "-" in in3 and "-" not in in3[0]:
        get = in3.index("-")
    elif "/" in in3 and "/" not in in3[0]:
        get = in3.index("/")
    elif "*" in in3 and "*" not in in3[0]:
        get = in3.index("*")
    else:
        get = 0

    num1 = ""
    for i in range(0,get):
        if i < 0:
            break
        num1 = num1 + in3[i]
        #print("Num1: " + num1)

    part1 = float(num1)

    num2 = ""
    for i in range(get+1, len(in3)):
        if i < 0:
            break
        num2 = num2 + in3[i]
        #print("Num2: " + num2)

    part2 = float(num2)


    output = 0.0
    if "+" in in3 and "+" not in in3[0]:
        output = part1 + part2
    elif "-" in in3 and "-" not in in3[0]:
        output = part1 - part2
    elif "*" in in3 and "*" not in in3[0]:
        output = part1 * part2
    elif "/" in in3 and "/" not in in3[0]:
        output = part1 / part2

    print(str(output))


maths()
