#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mtrx = [[0 for a in range(len(matrix))] for b in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sqr_mtrx[i][j] = matrix[i][j]**2
    return sqr_mtrx
