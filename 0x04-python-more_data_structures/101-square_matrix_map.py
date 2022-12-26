#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda num: list(map(lambda x: x ** 2, num)), matrix))
