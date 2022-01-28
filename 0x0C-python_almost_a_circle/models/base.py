#!/bin/python3
"""
Base Class from which all parts of the Circle class revolve
"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """
        initiation method
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base_nb_objects
        else:
            self.id = id
