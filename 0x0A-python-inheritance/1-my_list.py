#!/usr/bin/python3
"""
Class for My List
"""


class MyList(list):
    """
    inherit from list
    """
    def __init__(self):
        "initialize the object"
        super().__init__()

    def print_sorted(self):
        "Print the class sorted"
        print(sorted(self))
