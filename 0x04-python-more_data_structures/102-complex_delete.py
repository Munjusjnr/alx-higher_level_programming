#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary:
        return a_dictionary
    else:
        del a_dictionary[value]
        return a_dictionary
