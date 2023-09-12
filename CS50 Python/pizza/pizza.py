import sys
from tabulate import tabulate
import csv



def main():
    t = []
    try:
        with open(sys.argv[1], "r") as f:
            r = csv.reader(f)
            for row in r:
               t.append(row)
        print(t)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(t[1:], headers=t[0], tablefmt="grid"))

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")
else:
    main()