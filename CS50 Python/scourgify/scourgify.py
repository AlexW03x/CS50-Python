import sys
import csv

def main():
    t = []
    try:
        with open(sys.argv[1], "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                newtable = row["name"].split(",")

                t.append({'first' : newtable[1].lstrip(), "last" : newtable[0], "house" : row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as newfile:
        writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in t:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
    sys.exit("Not a CSV file")
else:
    main()