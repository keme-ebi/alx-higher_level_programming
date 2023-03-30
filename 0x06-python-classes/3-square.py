#!/usr/bin/python3
"""Defines a class Square by private instance attribute"""


class Square:
    """a class with private instance attribute"""

    def __init__(self, size):
        """instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """public instance method that returns tbe area of the square"""
        return (self.__size * self.__size)
