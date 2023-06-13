#!/usr/bin/python3

""" A module imported """
import json


def from_json_string(my_str):
    """ Object represented by a JSON string

    Args:
        my_str: The object to be deserialized

    Return:
        an object represented by a JSON string
    """
    return json.loads(my_str)
