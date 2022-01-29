#!/usr/bin/python3
"""
Rectangle class, inheriting from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class which inherits its attrs from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Check for correct initialization input"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """Return the area of Rectangle"""
        return self.__height * self.__width

    def display(self):
        """Prints Rectangle out of #s"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Override the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update an object's attrs"""
        flag = 0
        if args is not None:
            flag = 1
        if len(args) > 0 and flag == 1:
            self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle's attributes"""
        attrs = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return attrs

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
