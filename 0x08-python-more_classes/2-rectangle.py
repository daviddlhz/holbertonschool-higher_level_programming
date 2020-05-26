#!/usr/bin/python3
"""Rectangule class
"""


class Rectangle:
    """Initialization variables
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

        """[Get and setters]

        Atributtes:
            private: width
            private: heigth

        Raises:
            TypeError: [width must be an integer]
            ValueError: [width must be >= 0]
            TypeError: [height must be an integer]
            ValueError: [width must be >= 0]

        Returns:
            [Getters] -- [Access all values of the variables or atributtes]
            [area] -- [area of rectangle]
            [perimeter] -- [perimeter of rectangle]
        """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__height = height

    def area(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
