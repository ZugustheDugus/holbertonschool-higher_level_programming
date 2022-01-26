#!/usr/bin/python3
"""
Rectangle that inherits from Base class
"""


from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(Rectangle)

    @property
    def height(self):
        "Rectangle height"
        return self.__height

    @property
    def width(self):
        "Rectangle width"
        return self.__width

    @property
    def area(self):
        "Rectangle area"
        return self.__width * self.__height
