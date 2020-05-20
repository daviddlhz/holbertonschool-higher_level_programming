#!/usr/bin/python3
"""Class with atributte private"""


class Square:
    """Square class with initialization
    """
    def __init__(self, size=0):
        """Init

        Arguments:
            size {[private]} -- [size of square, value default = 0]
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """[Area of square]

        Returns:
            [size] -- [square a la dos]
        """
        return self.__size**2
