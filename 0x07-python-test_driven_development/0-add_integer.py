#!/usr/bin/python3
"""
add_integer:
    Returns the sum of two ints or floats
    Returns only an int
"""


def add_integer(a, b=98):
    """
    Change float to ints for addition
    """
    if a is float:
        a = int(a)
    if b is float:
        b = int(b)
    if a is not int:
        raise TypeError("a must be an integer")
    if b is not int:
        raise TypeError("b must be an integer")
    return a + b
