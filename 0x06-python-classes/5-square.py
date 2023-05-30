#!/usr/bin/python3

""" Defining a class square """


class Square:
    """
    A class representing a square

    Attributes:
        size: A private instance with an optional type
    """
    def __init__(self, size=0):
        self.__size = size
        """
        condition to check instantiation with optional meets int criteria

        Another condition to check whether value is a real number

        """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ A public instance method that returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ A public instance method that prints character # when called """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
