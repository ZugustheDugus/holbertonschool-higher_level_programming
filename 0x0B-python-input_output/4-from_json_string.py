#!/usr/bin/python3
"""
Function to convert obj from JSON to normal
"""

import json


def from_json_string(my_str):
    """Convert from JSON"""
    return json.loads(my_str)
