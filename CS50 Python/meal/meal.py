def main():
    ins = input("What Time Is It? ").lower()
    maths = converttonum(ins)

    if("am" in ins):
        if(maths >= 700 and maths <= 800):
            print("breakfast time")
    elif("pm" in ins):
        if(maths >= 1200 and maths <= 1300):
            print("lunch time")
        elif(maths >= 600 and maths <= 700):
            print("dinner time")
    else:
        if(maths >= 1800 and maths <= 1900):
            print("dinner time")
        elif(maths >= 1200 and maths <= 1300):
            print("lunch time")
        elif(maths >= 700 and maths <= 800):
            print("breakfast time")

def converttonum(d):
    newstr = ""
    for i in range(0, len(d)):
        if(d[i].isnumeric()):
            newstr = newstr + d[i]

    integer = int(newstr)
    return integer

main()