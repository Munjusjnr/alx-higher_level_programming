#!/usr/bin/python3

""" A module imported """
import json


def load_from_json_file(filename):
    """ Deserializing a JSON file and creating an object

    Args:
        filename: path to the file where the objects would be created from
    """
    with open(filename, encoding="UTF8") as f:
        """ looping through the file line by line """
        for line in f:
            data.append(json.loads(line))
    return data
