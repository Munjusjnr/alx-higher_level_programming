#!/usr/bin/python3

""" Defining a class lockedclass """


class LockedClass:
    """ A class representing LockClass with no class or  object attributes
    unless it is a new instance called first_name
    """

    __slots__ = ["first_name"]
