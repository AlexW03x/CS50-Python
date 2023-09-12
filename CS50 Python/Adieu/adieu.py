import inflect
p = inflect.engine()

names = {

}
def sorting(c):
    string = ""
    count = 0
    for i in names:
        count=count+1
        if(count < c):
            string = string + str(i)
        if(c == 2 and count == 2):
            string = string + " and " + str(i)
        if(c > 2 and count < c-1):
            string = string + ", "
        if(c > 2 and count == c):
            string = string + ", and " + str(i)

    print("Adieu, adieu, to " + string)

def main():
    c = 0
    while True:
        try:
            name = input("Name: ").lower().title()
            c = c + 1
            if(name in names):
                names[name] = names[name] + 1
            else:
                names[name] = 1
        except EOFError:
            if c == 1:
                for i in names:
                    print("Adieu, adieu, to " + str(i))
            else:
                sorting(c)
            break
        except KeyError:
            pass

main()
