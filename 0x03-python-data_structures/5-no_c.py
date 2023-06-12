#!/usr/bin/python3
def no_c(my_string):
    """remove Cs"""
    new_string = ''
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
