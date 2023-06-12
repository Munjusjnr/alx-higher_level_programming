#!/usr/bin/python3

""" Defining a class BaseGeometry """


class BaseGeometry:
    """ A class of BaseGeometry """
    def __init__(self):
        pass

    def area(self):
        """ A public instance method that raises an Exception message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A public  instance that validates value """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
