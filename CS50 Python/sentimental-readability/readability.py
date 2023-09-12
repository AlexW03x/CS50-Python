import sys
import time

def main():
    while True:#
        text = input("Enter your text: ")
        if(text.isnumeric()):
            print("Please enter some texts instead of all numbers.")
            continue#
        else:
            break

    #calculations

    letters = get_l(text)
    words = get_w(text)
    sentences = get_s(text)

    lets = (letters/words)*100
    sens = (sentences/words)*100
    index = 0.0588 * lets - 0.296 * sens - 15.8
    equation = round(index)

    if(equation < 1):
        print("Before Grade 1\n")
    elif(equation >= 16):
        print("Grade 16+\n")
    else:
        print("Grade " + str(round(equation)) + "\n")


def get_w(word):
    wordcount = 1
    for i in range(len(word)):
        if(word[i] == " " or word[i] == "\n" or word[i] == "\t"):
            wordcount = wordcount + 1

    print(str(wordcount) + "words\n")
    return wordcount

def get_l(word):
    letters = 0
    for i in range(len(word)):
        if((word[i] >= 'a' and word[i] <= 'z') or (word[i] >= 'A' and word[i] <= 'Z')):
            letters = letters + 1

    print(str(letters) + "Letters\n")
    return letters

def get_s(word):
    sentences = 0
    for i in range(len(word)):
        if(word[i] == "." or word[i] == "!" or word[i] == "?"):
            sentences = sentences + 1

    print(str(sentences) + "sentences\n")
    return sentences
main()
