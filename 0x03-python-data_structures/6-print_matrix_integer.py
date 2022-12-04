#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for val in row:
            if val != 0:
                print(" ", end="")
            print("{:d}".format(val, end=""))
        print()
