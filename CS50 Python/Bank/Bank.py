def main():
    in2= input("Greetings: ").lower()
    print(value(in2))

def value(in2):
    if("hello" in in2):
        return "$0"
    elif("h" in in2[0]):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
