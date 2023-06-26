#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list"""
    c = 0
    x -= 1
    while x >= 0:
        try:
            print(my_list[x], end="")
            x -= 1
            c += 1
        except IndexError:
            break

    print()
    return (c)
