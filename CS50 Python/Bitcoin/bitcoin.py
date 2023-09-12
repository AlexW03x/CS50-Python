import requests
import sys
import math
import random
import time
import json

def main():
    try:
        btc = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        print("Error")
        sys.exit(1)

    bitcoin_price = float( btc.json()['bpi']['USD']['rate_float'])
    calculator = bitcoin_price * float(sys.argv[1])
    print(f"${calculator:,.4f}")



def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if len(sys.argv) == 2:
    if(isfloat(sys.argv[1])==True):
        main()
    else:
        sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")
