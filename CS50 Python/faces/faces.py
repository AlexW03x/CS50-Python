def init():
    inp = input("String with faces: ")
    inp2 = str.replace(inp, ":)", "🙂")
    inp3 = str.replace(inp2, ":(", "🙁")
    print(inp3)

init()