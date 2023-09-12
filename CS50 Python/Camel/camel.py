def main():
    ins = input("Variable Name: ")

    variable = ""
    for i in range(0, len(ins)):
        if(ins[i].isupper()):
            variable = variable + "_" + ins[i]
        else:
            variable = variable + ins[i]

    print(variable.lower())

main()
