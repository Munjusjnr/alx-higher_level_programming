#!/usr/bin/python3

""" Defining the first class, Base, for other classes """


class Base:
    """ A class representing Base that will be the base of all classes

        Attributes:
            id: A private instance with optional type
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            base.__nb_object += 1
            self.id = self.__nb_object
