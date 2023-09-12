import sys
import time

def init():
    height  = 0
    print("Hey There, how tall should the pyramid be 1-8?\n")
    while True:#
        height  =  input("Height: ")
        if(height.isnumeric()):
            height = int(height)
        else:
            print("That is not a number!")
            continue#
        
        if(height <  1):
            height = 0
            print("Thats below the minimum value!")
            continue#
        elif(height  >  8):
            height = 0
            print("Thats above maximum value!")
            continue#
        else:
            break

    a = ["       #  #", "      ##  ##", "     ###  ###", "    ####  ####", "   #####  #####", "  ######  ######", " #######  #######", "########  ########"]
    b = ["      #  #", "     ##  ##", "    ###  ###", "   ####  ####", "  #####  #####", " ######  ######", "#######  #######"]
    c = ["     #  #", "    ##  ##", "   ###  ###", "  ####  ####", " #####  #####", "######  ######"]
    d = ["    #  #", "   ##  ##", "  ###  ###", " ####  ####", "#####  #####"]
    e = ["   #  #", "  ##  ##", " ###  ###", "####  ####"]
    f = ["  #  #", " ##  ##", "###  ###"]
    g = [" #  #", "##  ##"]
    h = ["#  #"]

    for i in range(height):
        if(height==1):
            print(h[i])
        if(height==2):
            print(g[i])
        if(height==3):
            print(f[i])
        if(height==4):
            print(e[i])
        if(height==5):
            print(d[i])
        if(height==6):
            print(c[i])
        if(height==7):
            print(b[i])
        if(height==8):
            print(a[i])
init()













