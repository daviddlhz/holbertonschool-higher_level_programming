#!/usr/bin/python3
"""Rectangule class
"""


class Rectangle:
    """Initialization variables
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        type(self).number_of_instances = type(self).number_of_instances + 1

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
        simb = str(self.print_symbol)
        a = ""
        for h in range(self.__height):
            for w in range(self.__width):
                a = a + simb
            if h != self.__height - 1:
                a = a + '\n'
        return a

    def __repr__(self):
        """[Method repre]

        Returns:
            [string] -- [Print with format]
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """[Final method delete]
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''return the biggest rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''return a new rectangle instance with
           width == height == size
        '''
        return cls(size, size)
