#!/usr/bin/python3
"""Defines a square by private instance atrribute """


class Square:
    """a class Square"""

    def __init__(self, size):
        """__init__ method doctstring
        Args:
            size(int): value for size of the square
        """
        self.__size = size
