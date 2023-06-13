#!/usr/bin/python3

""" Defining a class Student """


class Student:
    """ A class representing a class """
    def __init__(self, first_name, last_name, age):
        """ Initializing a new object student

        Args:
            first_name: student's first name
            last_name: student's surname
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return a dictionary representation of object Student

        Args:
            attrs: relates to attributes of the dict-list class
            Return:
                dict: Containing student attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """ Replacing all attributes of the Student instance

        Args:
            json: A dictionary containing its own keys(name) and values(value)
                    to replace the attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
