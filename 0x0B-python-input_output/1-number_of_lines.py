#!/usr/bin/python3
"""Number of lines function
"""


def number_of_lines(filename=""):
    """[number of lines]

    Args:
        filename (str): [nubers of lines]. Defaults to "".
    """

    with open(filename, encoding="utf-8") as f:
        return(len(f.readlines()))
