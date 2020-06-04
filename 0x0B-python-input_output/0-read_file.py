#!/usr/bin/python3
"""[function that reads a text file]
"""


def read_file(filename=""):
    """[read_file - read a content in the file]

    Args:
        filename (str): [route of the file]. Defaults to "".
    """

    with open(filename, 'r') as f:
        text_read = f.read()
        print(text_read)
