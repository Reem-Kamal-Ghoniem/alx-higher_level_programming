#!/usr/bin/python3
"""a module that contains the class
Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculating area"""
        return self.width * self.height

    def display(self):
        """drawing the rectangle"""
        r = "\n" * self.y
        for _ in range(self.height):
            r += " " * self.x
            r += "#" * self.width + "\n"

        print(r, end="")

    def __str__(self):
        """returning the rectangle as a string"""
        str_wh = "{}/{}".format(self.width, self.height)
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - str_wh"

    def update(self, *args, **kwargs):
        """using args, and kwargs"""
        if args and len(args) is not 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """describing the rectangle as a dictionary"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
