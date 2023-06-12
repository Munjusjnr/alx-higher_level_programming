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
