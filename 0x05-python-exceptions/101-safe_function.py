#!/usr/bin/python3
def safe_function(fct, *args):
    """a function that executes a function safely."""
    import sys
    try:
        fun = fct(*args)
        return fun
    except Exception as out:
        print("Exception:", out, file=sys.stderr)
        return None
