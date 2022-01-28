#!/usr/bin/python3
"""
Square class which draws from Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        id = self.__id
        size = self.__size
        x = self.__x
        y = self.__y
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(Square)

    def update(self, *args, **kwargs):
        "assigns each element to an arg"
        args = (self.__id, self.__x, self.__y, self.__size)
        update(*args)
        kwargs = {self.__id, self.__x, self.__y, self.__size}

    def to_dictionary(self):
        Dict = {self.__id, self.__size, self.__x, self.__y}

    def __repr__(self):
        return "Square({:d}, {:d})".format(self.__width, self.__height)
