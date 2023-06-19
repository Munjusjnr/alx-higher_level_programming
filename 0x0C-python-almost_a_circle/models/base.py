#!/usr/bin/python3

""" Defining the first class, Base, for other classes """
import json


class Base:
    """ A class representing Base that will be the base of all classes

        Attributes:
            id: A private instance with optional type
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the json string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ A class method that writes the JSON string rep. to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding="UTF8") as f:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in
                                          list_objs])
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ A static method that returns the list of JSON string rep. """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returning a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding="UTF8") as f:
                t = cls.from_json_string(f.read())
                instance = [cls.create(**dictionary) for dictionary in t]
                return instance
        except FileNotFoundError:
            return []
