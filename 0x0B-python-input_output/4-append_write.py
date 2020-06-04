#!/usr/bin/python3
"""Apeend to a file"""


def append_write(filename="", text=""):
    """appends at the end of file
    Keyword Arguments:
        filename {str} -- name of file (default: {""})
        text {str} -- text to append (default: {""})
    Returns:
        [type] -- [description]
    """
    with open(filename, mode="a", encoding="utf-8") as fd:
        fd.write(text)
    return len(text)
