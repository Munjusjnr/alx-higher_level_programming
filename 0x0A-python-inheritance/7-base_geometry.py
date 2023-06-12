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
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than zero".format(name))
