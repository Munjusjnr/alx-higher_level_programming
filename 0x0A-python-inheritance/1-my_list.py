#!/usr/bin/python3

""" Defining a class Mylist """


class MyList(list):
    """ A class that inherits from another list
    and outputs a sorted list
    """
    def print_sorted(self):
        """ sorted list ouput """
        print(sorted(self))
