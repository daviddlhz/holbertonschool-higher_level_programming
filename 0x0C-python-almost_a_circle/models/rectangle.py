#!/usr/bin/python3
'''rectangle module'''


from models.base import Base


class Rectangle(Base):
    '''class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set attribute value'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set attribute height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set attribute x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set attribute y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''return area'''
        return (self.__width * self.__height)

    def display(self):
        '''print a rectangle with '#' character'''
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                if j != self.__width - 1:
                    print('#', end="")
                else:
                    print("#")

    def __str__(self):
        '''return an argument to each attribute'''
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''assign argument each attribute'''
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                if arg == 1:
                    self.__width = args[arg]
                if arg == 2:
                    self.__height = args[arg]
                if arg == 3:
                    self.__x = args[arg]
                if arg == 4:
                    self.__y = args[arg]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        '''return a dictionary'''
        new_dict = {}
        new_dict['id'] = self.id
        new_dict['width'] = self.width
        new_dict['height'] = self.height
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
