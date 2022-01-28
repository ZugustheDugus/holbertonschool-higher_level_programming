#!/usr/bin/python3
"""
Rectangle that inherits from Base class
"""


from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        id = self.__id
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

    def area(self):
        "Rectangle area"
        return self.__width * self.__height

    def display(self):
        "Prints rectangle dimensions in #'s"
         string = ""
         if self.__width != 0 and self.__height != 0:
             for i in range(self.height):
                 for j in range(self.width):
                     string += '#'
                     if i != self.__height - 1:
                         string += '\n'
        return string

    def __str__(self):
        "__str__ method of the Rectangle"
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.__area, id, self.__x, self.__y, self.__height, self.__width))
    def update(self, *args, **kwargs):
        "assigns each element to an arg"
        args = (self.__id, self.__x, self.__y, self.__width, self.__height)
        update(*args)
        kwargs = {self.__id, self.__x, self.__y, self.__width, self.__height}

    def to_dictionary(self):
        Dict = {self.__id, self.__width, self.__height, self.__x, self.__y}

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
