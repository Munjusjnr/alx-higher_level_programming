#!/usr/bin/python3

""" Defining another class inheriting a class """
from models.base import Base


class Rectangle(Base):
    """ A class representing rectangle with base being inherited

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter
        Return:
            width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """ height getter
        Return:
            height of the rectangle
        """
        return self.__height

    @property
    def x(self):
        """ getter of x """
        return self.__x

    @property
    def y(self):
        """getter of y """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter
            Return:
                value of rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
            Return:
                value of rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter
            Return:
                 the value of x
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter
            Return:
                the value of y
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ A public instance method that returns area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ A public instance method that use # to print out  a rectangle """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print( " " * self.__x + "#" * self.__width)

    def __str__(self):
        """ method that returns the string representation of the rectangle """
        return ("[Rectangle] {(:d)} {:d}/{:d} - {:d}/{:d}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))
