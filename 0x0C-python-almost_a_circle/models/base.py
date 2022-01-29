#!/bin/python3
"""
Base Class from which all parts of the Circle class revolve
"""
import json
import os


class Base:
    """Base class"""
    __nb_object = 0

    @classmethod
    def clear(cls):
        Base.__nb_object = 0

    def __init__(self, id=None):
        """
        initiation method
        """
        if id is None:
            Base.__nb_object += 1
            self.id = Base.__nb_object
        else:
            self.id = id

        @staticmethod
        def to_json_string(list_dictionaries):
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            return json.dumps(list_dictionaries)

        @classmethod
        def create(cls, **dictionary):
            placeholder = cls(1, 1)
            placeholder.update(**dictionary)
            return placeholder

        @classmethod
        def save_to_file(cls, list_objs):
            """saves the attrs of objects into JSON files"""
            json_list = []

            if list_objs is not None:
                for i in list_objs:
                    json_list.append(i.to_dictionary())

        @classmethod
        def load_from_file(cls):

            if not os.path.exists(cls.__name__ + ".json"):
                return []

            with open(cls.__name__ + ".json", 'r') as f:
                tmp = Base.from_json_string(f.read())

            nlist = []

            for item in tmp:
                nlist.append(cls.create(**item))

            return nlist
