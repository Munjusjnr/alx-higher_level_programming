#!/usr/bin/python3

""" A funtion that prints the length of a square """


def print_square(size):
    """ This function prints a square like shape of a given input size

    Parameter:
        size: the size of the square

    Raises:
        TypeError: if size is not an integer or float figure is imposed
        ValueError: if size is a negative

    Return:
        A square-like figure based on the size given

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
