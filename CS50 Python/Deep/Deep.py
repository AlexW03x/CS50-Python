def fortytwo():
    stringpu = input("Input: ").lower()
    stringput = str.replace(stringpu, " ", "")
    if("42" in stringput):
        print("Yes")
    elif("fortytwo" in stringput):
        print("Yes")
    elif("forty-two" in stringput):
        print("Yes")
    elif("forty two" in stringput):
        print("Yes")
    else:
        print("No")

fortytwo()
