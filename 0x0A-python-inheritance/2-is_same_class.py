#!/usr/bin/python3

""" A function that uses boolean mode to determine a class """


def is_same_class(obj, a_class):
    """ Checking if object is an instance of a specified class
    Boolean values:
        True: if it is
        False: if otherwise
    """
    return True if type(obj) is a_class else False
