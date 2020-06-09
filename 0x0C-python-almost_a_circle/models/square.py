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
