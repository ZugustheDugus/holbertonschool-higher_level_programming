#!/usr/bin/python3
"""
I/O Function that appends to a file
"""


def append_write(filename="", text=""):
    """write and then append to file"""
    with open(filename, mode="a+", encoding="utf-8") as UTF8:
        return(UTF8.write(text))
