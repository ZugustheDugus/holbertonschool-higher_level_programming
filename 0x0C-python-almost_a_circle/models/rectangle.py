#!/usr/bin/python3
"""
Rectangle that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from Basse class and validating
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value

    def area(self):
        """Rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle dimensions in #s"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update object attributes"""
        attrs, i = ['id', 'width', 'height', 'x', 'y'], 0
        for value in args:
            setattr(self, attrs[i], value)
            i += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary of  attributes"""
        Dict = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return Dict
