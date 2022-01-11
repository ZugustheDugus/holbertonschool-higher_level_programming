#!/usr/bin/python3
"Class for a square with attributes"


class Square:
    "Attributes for the square"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        "area of the square"
        self.__size ** 2
