#!/usr/bin/python3

""" A functiontion that reads a file and outputs to stdout """


def read_file(filename=""):
    """ Reads a file and print to stdout

        Argument:
            filename: the name of the file for which its content
                        would be printed out
    """
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end='')
