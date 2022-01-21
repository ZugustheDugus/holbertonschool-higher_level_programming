#!/usr/bin/python3
"""
I/O Function that reads a file
"""


def read_file(filename=""):
    """read a file and print"""
    with open(filename, encoding="utf-8") as UTF8:
        print(UTF8.read())
