#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Return list of pascal's triangle
    """
    pas_list = []
    if n <= 0:
        return pas_list
    list = [1]
    for i in range(n):
        pas_list.append(list)
        new_list = []
        new_list.append(list[0])
        for i in range(len(list) - 1):
            new_list.append(list[i] + list[i + 1])
        new_list.append(list[-1])
        list = new_list
    return pas_list
