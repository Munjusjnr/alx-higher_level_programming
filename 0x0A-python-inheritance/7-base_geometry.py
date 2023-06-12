#!/usr/bin/python3

""" Defining a class BaseGeometry """


class BaseGeometry:
    """ A BaseGeometry class for geometry calculations and validations """

    def area(self):
        """ Calculating the area of the geometry

        A method that provide specific implementation for calculating the area

        Raises:
            Exception: The method is not implement in the base class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ A public  instance that validates value as an integer

        Args:
            name: The name argument will always be a string
            value: The value to be validated

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is zero or negative
        """

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
