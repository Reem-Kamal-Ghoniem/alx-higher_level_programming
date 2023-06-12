#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """sum of arguments"""

    args = sys.argv[1:]
    total = 0
    total = sum(int(arg) for arg in args)

    print(total)
