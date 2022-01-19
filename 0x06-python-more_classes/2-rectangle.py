#!/usr/bin/python3
"""
Class for a rectangle
"""


class Rectangle:
    "Rectangle class with a private width and height"
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        "Width of the rectangle"
        return self.__width

    @property
    def height(self):
        "Height of the rectangle"
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "Area of the Rectangle"
        return self.__width * self.__height

    def perimeter(self):
        "Perimeter of the Rectangle"
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Print the rectangle out of #'s
        """

        string = ""
        if self.__width != 0 and self.__height != 0:
            for i in range (self.height):
                for j in range(self.width):
                    string += '#'
                if i != self.__height - 1:
                    string += '\n'
        return string
