#!/usr/bin/python3
"""read file and prints specified lines"""


def read_lines(filename="", nb_lines=0):
    """reads lines
    Keyword Arguments:
        filename {str} -- name of file (default: {""})
        nb_lines {int} -- number of lines to read (default: {0})
    """
    with open(filename, encoding="utf-8") as fd:
        if nb_lines <= 0:
            print(fd.read(), end="")
        for i in range(nb_lines):
            print(fd.readline(), end="")
