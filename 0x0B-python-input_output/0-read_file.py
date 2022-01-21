#!/usr/bin/python3
"""
I/O Function that reads a file
"""


def read_file(filename=""):
    """read a file"""
    with open("my_file_0.txt", encoding="utf-8") as UTF8:
        text = UTF8.read()
        print("{}".format(text))
