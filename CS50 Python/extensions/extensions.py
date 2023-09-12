def sort():
    file = str(input("File Name and Extension: ").lower())
    if(".gif" in file):
        print("image/gif")
    elif(".jpg" in file):
        print("image/jpeg")
    elif(".jpeg" in file):
        print("image/jpeg")
    elif(".png" in file):
        print("image/png")
    elif(".zip" in file):
        print("application/zip")
    elif(".pdf" in file):
        print("application/pdf")
    elif(".txt" in file):
        print("text/plain")
    else:
        print("application/octet-stream")

sort()
