#!/usr/bin/python3

""" Defining a class based on the Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class Square based on another class

    Attribute:
        size: the size of a square
    """
    def __init__(self, size):
        """ Initializing with a single argument class circle """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ A string message to be printed out """
        return ("[Square] {}/{}".format(self.__size, self.__size))
