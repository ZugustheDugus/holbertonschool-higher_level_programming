#!/usr/bin/python3
"""
save data to a JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """save my_obj to filename in JSON"""
    with open(filename, "w+", encoding="utf-8") as JSON:
        return json.dump(my_obj, JSON)
