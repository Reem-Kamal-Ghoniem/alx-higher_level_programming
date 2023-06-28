#!/usr/bin/python3
def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list
    (only once for each integer)."""
    new = []
    for item in my_list:
        for x in new:
            if x == item:
                check = False
            else:
                check = True
        if check:
            new.append[item]
