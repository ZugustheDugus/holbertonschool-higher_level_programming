#!/usr/bin/python3
"""
Return dictionary description with sample data structure
"""


def class_to_json(obj):
    """
    Return dictionary description with simple data structure
    """
    return vars(obj)
