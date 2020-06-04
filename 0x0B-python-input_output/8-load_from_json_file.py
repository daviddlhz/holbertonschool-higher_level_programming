#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Loads object from json files
    Arguments:
        filename {str} -- name of file
    Returns:
        object -- object retrieved
    """
    with open(filename) as fd:
        obj = fd.read()
    return json.loads(obj)
