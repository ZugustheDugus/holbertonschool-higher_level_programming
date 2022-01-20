#!/usr/bin/python3
"""
Function to determine if something is a class
"""


def is_kind_of_class(obj, a_class):
    """
    Return true if object is an instance of or inherited from a_class
    else return false
    """
    return(isinstance(obj, a_class))
