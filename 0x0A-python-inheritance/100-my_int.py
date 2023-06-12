#!/usr/bin/python3

""" A class that inherits from the builtin int """


class MyInt(int):
    """ An alternate version of int """
    def __eq__(self, other):
        """ A function that alternates the equal to sign """
        return super().__ne__(other)

    def __ne__(self, other):
        """ A function that alternates the not equal to sign """
        return super().__eq__(other)
