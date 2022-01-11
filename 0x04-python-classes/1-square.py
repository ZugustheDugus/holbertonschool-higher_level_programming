#!/usr/bin/python3
"Class for a square with attributes"


class Square:
    "Square with private attribute for size and exception errors for size"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
