#!/usr/bin/python3
"""class to JSON"""


def class_to_json(obj):
    """Converts an object to a dictionary description
    Arguments:
        obj {object} -- object to convert
    Returns:
        dict -- dictionary description of object
    """
    return obj.__dict__
