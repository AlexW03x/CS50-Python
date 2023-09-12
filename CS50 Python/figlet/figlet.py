from pyfiglet import Figlet
import sys
import random
import math

figlet = Figlet()
fonts = figlet.getFonts()
#figlet.setFont(font=f)

if len(sys.argv) == 1:
    figlet.setFont(font=choice(fonts))
    ins = input("Text: ")
    print(figlet.renderText(ins))
elif len(sys.argv) == 2:
    sys.exit("Invalid Command Usage!")
elif len(sys.argv) == 3:
    if((sys.argv[1] in "-f" or sys.argv[1] in "--font") and sys.argv[2] in fonts):
        figlet.setFont(font=sys.argv[2])
        ins = input("Text: ")
        print(figlet.renderText(ins))
    else:
        sys.exit("Invalid Command Usage!")
else:
    sys.exit("Invalid Command Usage!")
