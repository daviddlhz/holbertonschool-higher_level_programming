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
        self.size = size

    @property
    def size(self):
        '''method get'''
        return self.__size

    @size.setter
    def size(self, value):
        '''method set'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """[Area of square]

        Returns:
            [size] -- [square a la dos]
        """
        return self.__size ** 2
