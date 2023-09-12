#mm--dd--yyyy
months = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

def main():
    while True:
        try:
            ins = input("Date [MM/DD/YYYY]: ").title()
            if("/" in ins):
                numcount = 0
                passed = False
                for i in range(0, len(ins)):
                    if(ins[i].isnumeric()):
                        numcount = numcount + 1
                    if(numcount >= 6 and numcount <= 8):
                        passed = True
                if(passed == True):
                    ins = str.split(ins, "/")
                    month = int(ins[0])
                    day = int(ins[1])
                    year = int(ins[2])
                    if(month > 12 or month < 1):
                        continue
                    elif(day > 31 or day < 1):
                        continue
                    else:
                        if(day < 10):
                            day = "0"+str(day)
                        if(month < 10):
                            month = "0"+str(month)
                        print(str(year)+"-"+str(month)+"-"+str(day))
                        break
            elif("," in ins):
                ins = str.replace(ins, ",", "")
                ins = str.split(ins, " ")
                found = False
                for i in months:
                    if i == ins[0]:
                        found = True

                if(found == True):
                    mm = str(months[ins[0]])
                    mm2 = int(mm)
                    day = int(ins[1])
                    year = int(ins[2])
                    if(mm2 > 12 or mm2 < 1):
                        continue
                    elif(day > 31 or day < 1):
                        continue
                    else:
                        if(day < 10):
                            day = "0"+str(day)
                        if(mm2 < 10):
                            addon = "0"
                        else:
                            addon = ""
                        print(str(year)+"-"+addon+str(months[ins[0]])+"-"+str(day))
                        break
                else:
                    continue

        except EOFError:
            print("")
            break
        except KeyError:
            pass
    #print(ins) - prints date as array
    #print(ins[0]) -array 0 to 2 0 being month, 1 being day and 2 being year
    #print(ins[1])
    #print(ins[2])

main()