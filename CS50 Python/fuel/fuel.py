def main():
    while True:
        ins = input("Fraction: ")
        findsplit = 0
        part1 = ""
        part2 = ""
        part1check = 0
        part2check = 0
        if(ins.find("/") == -1):
            print("Invalid Fraction!")
            continue
        else:
            location = ins.find("/")
            for i in range(0, location):
                part1 = part1 + ins[i]
                part1 = str.replace(part1, "/", "")

            for i in range(location, len(ins)):
                part2 = part2 + ins[i]
                part2 = str.replace(part2, "/", "")

            if(part1.isnumeric() and part2.isnumeric()):

                if(int(part1) > int(part2)):
                    print("Invalid Fraction!")
                    continue

                if(int(part1) < 0 or int(part2) <= 0):
                    print("Invalid Fraction!")
                    continue

                x = int(part1) / int(part2)
                if(x == 1 or x >= 0.99):
                    print("F")
                    break
                elif(x == 0 or x <= 0.01):
                    print("E")
                    break
                else:
                    print(str(int(round(x*100)))+"%")
                    break
            else:
                print("Invalid Fraction!")
                continue


main()
