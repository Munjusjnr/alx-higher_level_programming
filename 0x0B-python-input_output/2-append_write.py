#!/usr/bin/python3

""" A function that appends a string to a file """


def append_write(filename="", text=""):
    """ Append the text to the file instead of overwriting its content

    Args:
        filename: The path to the file where contents will be written
        text: The content to be appended to the file
    """
    with open(filename, mode='a', encoding="UTF8") as f:
        f.write(text)
