def main():
    ins = input("Fraction: ")
    part1 = convert(ins)
    part2 = gauge(part1)
    print(part2)


def convert(fraction):
    while True:
        try:
            num, den = fraction.split("/")
            num = int(num)
            den = int(den)
            ans = num / den
            if ans <= 1:
                ans = ans * 100
                return ans
            else:
                fraction = input("Fraction: ")
                pass
        except ValueError:
            raise
        except ZeroDivisionError:
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()