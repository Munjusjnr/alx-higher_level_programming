#!/usr/bin/python3

""" A function that returns the dictionary with simple data structure """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Returns: the dictionary
    """
    return obj.__dict__
