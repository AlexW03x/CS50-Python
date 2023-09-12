import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    try:
        img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    shirtsize = shirt.size
    candidate = ImageOps.fit(img, shirtsize)
    candidate.paste(shirt, shirt)
    candidate.save(sys.argv[2])

def isvalid(x):
    if x in [".jpg", ".png", ".jpeg"]:
        return True
    else:
        return False


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif isvalid(splitext(sys.argv[1])[1]) == False:
    sys.exit("Invalid input")
elif isvalid(splitext(sys.argv[2])[1]) == False:
    sys.exit("Invalid output")
elif splitext(sys.argv[1])[1].lower() != splitext(sys.argv[2])[1].lower():
    sys.exit("Input and output have different extensions")
else:
    main()
