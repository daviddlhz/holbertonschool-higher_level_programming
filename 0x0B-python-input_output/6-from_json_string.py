#!/usr/bin/python3
"""From JSON string to Object"""
import json


def from_json_string(my_str):
    """from json to object
    Arguments:
        my_str {json} -- object to convert
    Returns:
        object -- object representation
    """
    return json.loads(my_str)
