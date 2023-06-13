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

    def to_json(self):
        """ Return a dictionary representation of object Student

            Return:
                dict: Containing student attributes
        """
        return self.__dict__
