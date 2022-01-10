#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [[0 for a in range(len(matrix[0]))] for b in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            square[i][j] = (matrix[i][j])**2
    return square
