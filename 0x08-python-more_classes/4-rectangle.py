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
        """[getter: width]

        Returns:
            [int] -- [width of rectangle]
        """
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
        """[area]

        Returns:
            [int] -- [area of a rectangle]
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__width * self.__height

    def perimeter(self):
        """[Method perimeter]

        Returns:
            [int] -- [Permiter of rectangle]
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """[Method str]

        Returns:
            [string] -- [print a # or print rectangle]
        """
        a = ""
        for h in range(self.__height):
            for w in range(self.__width):
                a = a + "#"
            if h != self.__height - 1:
                a = a + '\n'
        return a

    def __repr__(self):
        """[Method repre]

        Returns:
            [string] -- [Print with format]
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
