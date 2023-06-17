#!/usr/bin/python3

""" Defining a class inheriting another class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class representing square inheriting from another class

        Attributes:
            size: size of the square
            x: A private attribute method with optional type
            y: A private attribute method with optional type
            id: A private attribute method with None optiona type

    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing the class with a class instructor """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ method that returns the string representation of a square """
        return ("[Square] {(:d)} {:d}/{:d} - {:d]".format(self.id, self.x,
                self.y, self.width))

    def update(self, *args, **kwargs):
        """ public instance method that assigns arguments to attributes """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return the dictionary representation of a square """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
