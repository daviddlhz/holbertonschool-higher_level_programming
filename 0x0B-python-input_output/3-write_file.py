#!/usr/bin/python3
"""write to a text file"""


def write_file(filename="", text=""):
    """writes to a file
    Keyword Arguments:
        filename {str} -- name of file (default: {""})
        text {str} -- text beingwritten (default: {""})
    Returns:
        int -- number of charaters
    """
    with open(filename, mode="w", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
