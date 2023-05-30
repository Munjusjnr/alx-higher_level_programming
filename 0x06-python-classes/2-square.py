#!/usr/bin/python3

""" Defining a class square """


class Square:
    """
    A class representing a square

    Attributes:
        size: A private instance attribute with an optional type
    """
    def __init__(self, size=0):
        """
        condition to check instantiation with optional meets int criteria.

        Another condition to check for negative value and act against it.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
