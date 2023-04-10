#!/usr/bin/python3
"""4-print module that has only one function in it"""


def print_square(size):
    """prints a square with the character #
       Args:
            size(int): size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
