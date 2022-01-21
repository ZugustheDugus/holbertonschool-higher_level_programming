#!/usr/bin/python3
"""
Function to return JSON representation of I/O string
"""

import json

def to_json_string(my_obj):
    """return JSON representation of object"""
    return json.dumps(my_obj)
