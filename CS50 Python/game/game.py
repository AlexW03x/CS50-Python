import sys
import math
import random

def main():
        global m
        m = 0
        isValid = False
        try:
            ins = int(input("Level: "))
            if(ins > 0):
                isValid = True
            else:
                main()
        except ValueError:
            print("That is not a whole number!")
            main()

        if(isValid == True):
            m = random.randrange(1, ins+1)
            nextpart(m)

def nextpart(m2):
    ans = m2
    yourans = 0
    try:
        yourans = int(input("Guess: "))
        if(yourans > ans):
            print("Too large!")
            nextpart(m)
        elif(yourans < ans):
            print("Too small!")
            nextpart(m)
    except ValueError:
        nextpart(m)
    print("Just right!")
    exit()

main()