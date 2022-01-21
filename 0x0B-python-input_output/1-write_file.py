#!/usr/bin/python3
"""
I/O Function that writes a file
"""


def write_file(filename="", text=""):
    """ Write to a file """
    with open(filename, mode="w+", encoding="utf-8") as UTF8:
        return(UTF8.write(text))
