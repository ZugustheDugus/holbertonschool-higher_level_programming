#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Return list of pascal's triangle
    """
    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            if j == i or j == 0:
                triangle.append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        return triangle
