#!/usr/bin/python3

""" A function that checks if object is of a specified class """


def is_kind_of_class(obj, a_class):
    """ This checks if an instance is an isinstance of or inherited from
    a specified class

    Boolean value:
        True: if it is
        False: if it is not

    Return: Either True or False
    """
    return True if isinstance(obj, a_class) else False

