#!/usr/bin/python3
"""Class with atributte private"""


class Square:
    """Square class with initialization
    """
    def __init__(self, size=0, position=(0, 0)):
        """Init

        Arguments:
            size {[private]} -- [size of square, value default = 0]
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """[Area of square]

        Returns:
            [size] -- [square a la dos]
        """
        return self.__size ** 2

    def my_print(self):
        """[Print a square]
        """
        self.row = 0
        if self.__size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            while self.row < self.size:
                print("{}{}".format(" " * self.position[0], "#" * self.size))
                self.row += 1
