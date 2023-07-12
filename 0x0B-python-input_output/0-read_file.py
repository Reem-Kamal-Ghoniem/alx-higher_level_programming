#!/usr/bin/python3

"""python file has a function that reads a file"""

def read_file(filename=""):
    """ a function that reads a text file
    (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
