#!/usr/bin/python3
"""
Function for obj to inherit methods from a_class
"""
def inherits_from(obj, a_class):
    """
    Return true if obj inherits from a_class
    else return false
    """
    if type(obj) == a_class:
        return False
    return(issubclass(type(obj), a_class))
