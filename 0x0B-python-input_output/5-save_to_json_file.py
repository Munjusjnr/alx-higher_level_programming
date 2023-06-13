#!/usr/bin/python3

""" A module to be imported """
import json


def save_to_json_file(my_obj, filename):
    """ Serialized an object to its JSON representation and writes it
    to a text file

    Args:
        my_obj: Object to be serialized
        filename: Path the file where the object would be written
    """
    with open(filename, mode='w', encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
