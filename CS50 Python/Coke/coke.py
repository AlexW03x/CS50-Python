def main():
    firsttry = 0
    cokevalue = 0
    inputtedcoins = 0
    while True:
        if(firsttry == 0):
            ins = input("Insert change: ")
            if("10" in ins or "25" in ins or "50" in ins or "5" in ins):
                num = ""
                for i in range(0, len(ins)):
                    if(ins[i].isnumeric()):
                        num = num + ins[i]
                num = int(num)
                cokevalue = 50
                inputtedcoins = num
                cokevalue = cokevalue - inputtedcoins
                firsttry = 1
            elif(("1" in ins or "2" in ins or "3" in ins or "4" in ins or "6" in ins or "7" in ins or "8" in ins or "9" in ins)):
                print("Amount Due: 50")
                continue
        if(cokevalue > 0):
            print("Amount Due: " + str(cokevalue))
        if(cokevalue == 0):
            print("Change owed: 0")
            break
        elif(cokevalue < 0):
            print("Change owed: " + str.replace(str((cokevalue - inputtedcoins) + inputtedcoins), "-", ""))
            break
        else:
            ins2 = input("Insert change: ")
            num2 = ""
            for i in range(0, len(ins2)):
                if(ins2[i].isnumeric()):
                    num2 = num2 + ins2[i]
            num2 = int(num2)
            inputtedcoins = num2
            cokevalue = cokevalue - inputtedcoins
            continue

main()
