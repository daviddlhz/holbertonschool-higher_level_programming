#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square is a special Rectangle, inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        method constructor class Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Print str method
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Get square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set square
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.width = value
            self.height = value
