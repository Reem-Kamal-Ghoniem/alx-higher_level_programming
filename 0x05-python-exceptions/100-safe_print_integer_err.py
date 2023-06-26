#!/usr/bin/python3
def safe_print_integer(value):
    """a function that prints an intege"""
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return (False)
