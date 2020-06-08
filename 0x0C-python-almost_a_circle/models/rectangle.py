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
    """ width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    """ height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    """ x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    """ y"""
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
