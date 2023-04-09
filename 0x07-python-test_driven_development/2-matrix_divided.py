#!/usr/bin/python3
"""Module for 2-matrix_divided and it has only one function in it"""


def matrix_divided(matrix, div):
    """This function divides a matrix and returns the answer of the division
       Args:
            matrix(list of list, int or float): matrix to be divided
            div(int or float): number that divides the matrix
       Return:
            a new matrix
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(msg)
    if not isinstance(matrix, list):
        raise TypeError(msg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    first = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first:
            raise TypeError("Each row of the matrix must have the same size")
    new = matrix[:]
    new = [[round(j / div, 2) for j in i] for i in matrix]
    return new
