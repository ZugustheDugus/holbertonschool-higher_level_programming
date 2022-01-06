#!/usr/bin/python3
def raise_exception():
    x = 0
    if not type(x) is int:
        raise Exception()
