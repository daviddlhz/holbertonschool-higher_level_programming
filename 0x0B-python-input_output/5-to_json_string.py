#!/usr/bin/python3
"""To JSON string"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object
    Arguments:
        my_obj {str} -- [description]
    Returns:
        json -- representation of a string
    """
    return json.dumps(my_obj)
