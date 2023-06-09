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

    def area(self):
        """ Area of the rectangle being implemented """
        return self.__width * self.__height

    def __str__(self):
        """ A string message to be printed out"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
