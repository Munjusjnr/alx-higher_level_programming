#!/usr/bin/python3

""" A module imported """
import json


def load_from_json_file(filename):
    """ Deserializing a JSON file and creating an object

    Args:
        filename: path to the file where the objects would be created from

    Return: objects created
    """
    with open(filename, encoding="UTF8") as f:
        my_data = json.load(f)
    return my_data
