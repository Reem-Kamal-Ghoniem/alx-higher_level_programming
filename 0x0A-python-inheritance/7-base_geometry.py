#!/usr/bin/python3

"""file that wil Improve Geometry"""


class BaseGeometry:
    """class for the basegeometry"""

    def area(self):
        """function for area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method  that validates value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
