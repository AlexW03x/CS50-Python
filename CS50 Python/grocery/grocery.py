groceries = {
}

def main():
    while True:
        try:
            ins = input("").upper()
            if(ins in groceries):
                groceries[ins] = groceries[ins] + 1
            else:
                groceries[ins] = 1

        except EOFError:
            for i in sorted(groceries):
                print(str(groceries[i]) + " " + str(i))
            break
        except KeyError:
            pass

main()