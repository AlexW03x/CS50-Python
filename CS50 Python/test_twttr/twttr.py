def main():
    t = input("text: ")
    print(shorten(t))

def shorten(word):
    t = ""
    array = ["a", "e", "i", "o", "u"]

    for i in range(len(word)):
        if word[i].lower() not in array:
            t = t + word[i]
    return t

if __name__ == "__main__":
    main()