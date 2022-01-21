#!/usr/bin/python3
"""
Load from a JSON obj
"""


import json


def load_from_json_file(filename):
    """load from filename"""
    with open(filename, mode="r", encoding="utf-8") as LOAD:
        return json.load(LOAD)
