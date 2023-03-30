#!/usr/bin/python3
"""Defines a square by private instance attribute"""


class Square:
    """a class Square"""

    def __init__(self, size=0):
        """docstring for __init__ method
        Args:
            size(int)=0: value for size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
