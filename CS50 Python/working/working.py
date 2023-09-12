import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    var = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if var:
        if int(var.groups()[1]) > 12 or int(var.groups()[5]) > 12:
            raise ValueError
        part1 = return_time(var.groups()[1], var.groups()[2], var.groups()[3])
        part2 = return_time(var.groups()[5], var.groups()[6], var.groups()[7])
        return part1 + " to " + part2
    else:
        raise ValueError

def return_time(h, m, f):
    if f == "PM":
        if int(h) == 12:
            hour = int(h)
        else:
            hour = int(h) + 12
    else:
        if int(h) == 12:
            hour = int(h) - 12
        else:
            hour = int(h)
    if m == None:
        mins = ":00"
        time = f"{hour:02}" + mins
    else:
        time = f"{hour:02}" + ":" + m
    return time

if __name__ == "__main__":
    main()