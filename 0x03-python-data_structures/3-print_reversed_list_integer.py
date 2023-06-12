#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print elements in a reversed way"""
    for num in reversed(my_list):
        print("{:d}".format(num))
