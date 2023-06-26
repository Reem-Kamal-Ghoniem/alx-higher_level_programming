#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """a function that prints the first x elements
    of a list and only integers."""
    if x == 0:
        print("")
        return (0)
    c = 0
    x -= 1
    tmp = 0
    while tmp <= x:
        try:
            print("{:d}".format(my_list[tmp]), end="")
            tmp += 1
            c += 1
        except (ValueError, TypeError):
            continue
    print()
    return (c)
