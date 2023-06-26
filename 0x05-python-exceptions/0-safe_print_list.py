#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """a function that prints x elements of a list"""
    c = 0
    x -= 1
    tmp = 0
    while tmp <= x:
        try:
            print(my_list[tmp], end="")
            tmp += 1
            c += 1
        except IndexError:
            break

    print()
    return (c)
