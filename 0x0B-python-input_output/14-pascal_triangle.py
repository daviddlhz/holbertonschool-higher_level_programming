#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Pascal's triangle
    Arguments:
        n {int} -- height of triangle
    Returns:
        list -- list of lists of numbers
    """
    ls = []
    for i in range(n):
        ls.append([])
        ls[i].append(1)
        for j in range(1, i):
            num = ls[i - 1][j - 1] + ls[i - 1][j]
            ls[i].append(num)
        if(len(ls) > 1):
            ls[i].append(1)
    return ls
