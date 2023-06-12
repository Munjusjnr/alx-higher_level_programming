#!/usr/bin/python3

""" A function that uses boolean mode to determine an instance of a class """


def inherits_from(obj, a_class):
    """ Checking if an object is an instance of a class inherited directly
    or indirectly
    Return:
       - True if it is directly or indirectly
       - False if it is not
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
