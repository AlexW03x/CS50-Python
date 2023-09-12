menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    totalcost = 0.00
    print("Hi This Is Our Menu: " + str(menu.copy()) + "\nTo cancel orders type control-d")
    while True:
        try:
            ins = input("Order: ").title()
            totalcost = float(totalcost + menu[ins])
            print("Total: $" + str(totalcost) + "0")
        except EOFError:
            print("")
            break
        except KeyError:
            pass

main()