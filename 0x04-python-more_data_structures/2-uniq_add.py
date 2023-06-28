#!/usr/bin/python3
def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list
    (only once for each integer)"""
    sum = 0
    for i in (my_list):
        sum += my_list[i]
    return sum
