#!/usr/bin/python3

""" Defining a class based of BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class Rectangle based on another class

        Attributes:
            width: width of the rectangle
            height: height of the rectangle
    """
    def __init__(self, width, height):
        """ Initialize the class with given parameters """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
