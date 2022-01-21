#!/usr/bin/python3
"""
Base Geometry class with integer validation and no area
implementation
"""

class BaseGeometry:
    def area(self):
        "Area implementation"
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        "Method validates value"
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
