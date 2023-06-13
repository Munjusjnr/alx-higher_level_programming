#!/usr/bin/python3

""" module imported """
import json


def to_json_string(my_obj):
    """ The JSON representation of an object

        Args:
            my_obj: The object to be serialized into JSON
        Return:
            the JSON representation of an object
    """
    return json.dumps(my_obj)
