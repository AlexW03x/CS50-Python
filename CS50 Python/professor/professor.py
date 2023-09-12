import random
import sys

score = 0
done = 0
level = 0
def main():
    global score
    global done
    global level
    if level == 0:
        level = get_level()
        a = level
    else:
        a = level
    x = generate_integer(a)
    y = generate_integer(a)

    o = littleprofessor(x,y)
    if o == False:
        done = done + 1
        if done == 10:
            print(f"Score: {score}")
            sys.exit(0)
        else:
            return main()
    if o == True:
        score = score + 1
        done = done + 1
        if done == 10:
            print(f"Score: {score}")
            sys.exit(0)
        else:
            return main()


def get_level():
    while True:
        try:
            ins = int(input("Level: "))
            if(ins in (1,2,3)):
                break
        except EOFError:
            break
        except ValueError:
            pass
    return ins

def generate_integer(level):
    if(level == 1):
        return random.randint(0,9)
    if(level == 2):
        return random.randint(10,99)
    if(level == 3):
        return random.randint(100,999)


def littleprofessor(x,y):
    attempts = 1
    while attempts <= 3:
        try:
            ans = int(input(f"{x} + {y} ="))
            if(ans == (x+y)):
                return True
            else:
                attempts += 1
                print("EEE")
        except:
            print("EEE")
            attempts += 1

    print(f"{x} + {y} = {x+y}")
    return False

if __name__ == "__main__":
    main()