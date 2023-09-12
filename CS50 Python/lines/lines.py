import sys

def main():
    try:
        f = open(sys.argv[1], "r")
        l = f.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")
    count = 0
    for lines in l:
        if(lines.isspace()):
            count = count
        elif(lines.lstrip().startswith('#')):
            count = count
        else:
            count = count + 1

    print(str(count))

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif ".py" not in sys.argv[1]:
    sys.exit('Not a Python file')
else:
    main()