#!/usr/bin/python3
"""
Student class defined by public first_name, last_name, age)
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of Student instance"""
        if attrs is None:
            return vars(self)
        neu_dict = {}
        for i in attrs:
            try:
                neu_dict[i] = vars(self)[i]
            except Exception:
                pass
        return neu_dict

    def reload_from_json(self, json):
        """Replace attributes"""
        self.__dict__.update(json)
