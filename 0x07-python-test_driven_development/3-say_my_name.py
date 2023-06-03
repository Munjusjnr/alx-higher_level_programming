#!/usr/bin/python3

""" A function that prints your name """


def say_my_name(first_name, last_name=""):
    """
    A function that basically prints your first and last name

    Parameter:
        first_name: Individual's maiden name
        last_name: Individual's surname

    Raise:
        TypeError: Should the name not be a string

    Return:
        The message with the person's full name

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
