#!/usr/bin/python3
"""
matrix_divided:
    Divides all spaces in a matrix by a number
    Returns new matrix of ints rounded to two dec
"""

def matrix_divided(matrix, div):
    """
    Check if a matrix is in a list
    Check if each row is the same
    Check if div is not 0
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lits) of integers/floats")
    size = len(matrix[0])
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in (int, float):
                raise TypeError("matrix must be a matrix (list off lists) of integers/floats")
    if type(dive) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
