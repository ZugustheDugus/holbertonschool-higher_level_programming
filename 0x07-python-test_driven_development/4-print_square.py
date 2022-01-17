#!/usr/bin/python3
"""
Prints "Prints a square"
"""


def print_square(size):
    """
    Check to make sure size is int >0, then print a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#", end="")
    print()
