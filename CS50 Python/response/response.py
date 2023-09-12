from validator_collection import validators

def main():
    ins = input("Email: ")
    try:
        check = validators.email(ins)
        print("Valid")
    except:
        print("Invalid")

main()