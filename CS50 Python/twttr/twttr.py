def main():
    ins = input("Word/Sentence: ")
    print(shorten(ins))


def shorten(word):
    w = word
    final = ""
    for i in w:
        if i.upper() in ('A','E','I','U','O'):
            pass
        else:
            final = final + i

    return final


if __name__ == "__main__":
    main()