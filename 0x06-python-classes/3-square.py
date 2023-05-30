#!/usr/bin/python3

""" Defining a class square """


class Square:
    """
    A class representing a square

    Attributes:
        size: A private instance with an optional type
    """
    def __init__(self, size=0):
        """
        condition to check instantiation with optional meets int criteria

        Another condition to check whether value is a real number

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ A public instance method that returns the area of the square """
        return self.__size * self.__size
