import sys
import time
import math

def main():
    strcredit = ""
    credit = 0
    while True:#
        if(credit == 0):
            credit = input("Card Number: ")
            if(credit.isnumeric()):
                break
            else:
                credit = 0
                print("That is not a valid card number!")
                continue#

    strcredit = str(credit)
    first = strcredit[0]
    second = strcredit[1]
    x = int(credit)
    len = 0
    if(x>=10000000000000000):
        len = 17
    elif(x>=1000000000000000):
        len = 16
    elif(x>=100000000000000):
        len = 15
    elif(x>=10000000000000):
        len = 14
    elif(x>=1000000000000):
        len = 13
    elif(x>=100000000000):
        len = 12
    elif(x>=10000000000):
        len = 11
    elif(x>=1000000000):
        len = 10
    elif(x>=100000000):
        len = 9
    elif(x>=10000000):
        len = 8
    elif(x>=1000000):
        len = 7
    elif(x>=100000):
        len = 6
    elif(x>=10000):
        len = 5
    elif(x>=1000):
        len = 4
    elif(x>=100):
        len = 3
    elif(x>=10):
        len = 2
    else:
        len = 1


    last = strcredit[len-1]

    if(first == '4'):
        if(len == 13 or len == 16):
            if(last == '3'):
                print("INVALID\n")
            else:
                print("VISA\n")
        else:
            print("INVALID\n")

    elif(first == '5'):
        if(second == '1' or second == '2' or second == '3' or second == '4' or second == '5'):
            if(len == 16):
                print("MASTERCARD\n")
            else:
                print("INVALID\n")

        else:
            print("INVALID\n")

    elif(first == '3'):
            if(second == '4' or second == '7'):
                if(len == 15):
                    print("AMEX\n")
                else:
                    print("INVALID\n")

            else:
                print("INVALID\n")
    else:
        print("INVALID\n")

main()