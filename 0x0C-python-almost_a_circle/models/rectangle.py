#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation with width and height
        width: width of rectangle
        height: height of rectangle
        """
        self.__width = width
        self.__height = height
        self.__X = x
        self.__y = y
        super().__init__(id)

    """[Getters and setters]
    """

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ height"""
    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ x"""
    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    """ y"""
    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
