#!/usr/bin/python3

""" The function returns the summation of integers """


def add_integer(a, b=98):
    """ This function seeks to add two numbers

    parameters:
        a: first parameter(integer or float)
        b: second parameter(integer or float)

    Return: the sum of the two parameters

    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        a = int(a) if isinstance(a, float) else a

        b = int(b) if isinstance(b, float) else b

        return a + b
    except TypeError as error:
        raise TypeError(error)
