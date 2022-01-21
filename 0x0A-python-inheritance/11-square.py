#!/usr/bin/python3
"""
Square subclass that inherits from Rectangle and Base Geometry
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    "Square Subclass, inheriting from Rectangle"
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        "return width and height of square along with area"
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
