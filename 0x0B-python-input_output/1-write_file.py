#!/usr/bin/python3

""" A function that writes a string to text file """


def write_file(filename="", text=""):
    """ writing to a file then returning the number of characters written

        Args:
            filename: file to contain contents
            text: content to be appended to the file
    """
    with open(filename, mode='w', encoding="UTF8") as f:
        f.write(text)
        return len(text)
