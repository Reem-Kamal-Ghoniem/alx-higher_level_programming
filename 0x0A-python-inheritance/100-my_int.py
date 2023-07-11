#!/usr/bin/python3

"""a files conatians an integer subclass"""


class MyInt(int):
    """a class MyInt that inherits from int"""

    def __eq__(self, value):
        """Override =="""
        return self.real != value

    def __ne__(self, value):
        """Override !="""
        return self.real == value
