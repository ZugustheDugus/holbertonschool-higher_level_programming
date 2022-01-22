#!/usr/bin/python3
"""
Class for Student that defines by pbulc firstname, listname, age
"""


class Student():
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation of instance of Student Class"""
        return vars(self)
