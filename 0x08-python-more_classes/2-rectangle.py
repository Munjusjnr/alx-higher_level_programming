#!/usr/bin/python3

""" Defining a class """


class Rectangle:
    """ A class representing rectangle

        Attributes:
            width: A private instance with optional type
            height: A private instance with optional type

    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        """
        condition to check whether height or width meets int criteria

        Also checking the value to be a real number

        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """ width getter
            Return:
                width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
            Return:
                the value of the rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter
            Return:
                height of the the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
            Return:
                the value of the rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ A public instance that returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ A public instance that returns the perimeter of the rectangle """
        return self.__width + self.__height + self.__width + self.__height
