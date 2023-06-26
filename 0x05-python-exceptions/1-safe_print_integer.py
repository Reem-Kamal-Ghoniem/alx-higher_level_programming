#!/usr/bin/python3
def safe_print_integer(value):
    """a function that prints an integer with "{:d}".format()."""
    try:
        print("value = {:d}".format())
        return (True)
    except ValueError:
        return (False)
