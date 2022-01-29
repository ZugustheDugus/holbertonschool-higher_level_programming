#!/bin/python3
"""
Base Class from which all parts of the Circle class revolve
"""
import json
import os


class Base:
    """
    The Base class, starting with number of objects at 0
    """
    __nb_objects = 0

    @classmethod
    def clear(cls):
        """Set the varible to 0 for unittesting"""
        Base.__nb_objects = 0

    def __init__(self, id=None):
        """initiation of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        @staticmethod
        def to_json_string(list_dictionaries):
            """Return a dictionary list in JSON format"""
            if list_dictionaries is None:
                return "[]"
            if list_dictionaries == 0:
                return "[]"
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            """saves the attrs of objects into JSON files"""
            json_list = []

            if list_objs is not None:
                for i in list_objs:
                    json_list.append(i.to_dictionary())

            with open(cls.__name__ + ".json", 'w') as f:
                f.write(Base.to_json_string(json_list))

        @staticmethod
        def from_json_string(json_string):
            """Convert a json string into a list"""
            if json_string is None:
                return "[]"
            if len(json_string) == 0:
                return "[]"
            return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """create an object based on dictionary"""
            if cls.__name__ == "Rectangle":
                placeholder = cls(1, 1)
            elif cls.__name__ == "Square":
                placeholder = cls(1)
            placeholder.update(**dictionary)
            return placeholder

        @classmethod
        def load_from_file(cls):
            """Load from a file"""
            if not os.path.exists(cls.__name__ + ".json"):
                return []

            with open(cls.__name__ + ".json", 'r') as f:
                tmp = Base.from_json_string(f.read())

                nlist = []

                for item in tmp:
                    nlist.append(cls.create(**item))

            return nlist
