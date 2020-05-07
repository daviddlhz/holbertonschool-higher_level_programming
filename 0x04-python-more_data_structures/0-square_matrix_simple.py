#!/usr/bin/python3
def square(x):
    return x*x


def square_matrix_simple(matrix=[]):
    return [list(map(square, j)) for j in matrix]
