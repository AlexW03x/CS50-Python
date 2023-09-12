def main():
    ins = input("Greeting: ")
    string = value(ins)
    print(f"${string}")

def value(greeting):
    greeting = greeting.lower().strip()
    if 'hello' in greeting:
        return 0
    elif 'h' in greeting:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()