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
        super().__init__(Rectangle)
