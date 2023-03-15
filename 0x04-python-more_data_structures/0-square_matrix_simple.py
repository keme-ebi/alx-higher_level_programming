#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    new = [[i**2 for i in x] for x in new]
    return new
