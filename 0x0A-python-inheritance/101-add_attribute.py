#!/usr/bin/python3

""" A function that adds new attributes to an object """


def add_attribute(obj, name, value):
    """ Add attributes else raise TypeError """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
