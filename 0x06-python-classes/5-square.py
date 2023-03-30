#!/usr/bin/python3
"""Defines a class Square by private instance attribute"""


class Square:
    """a class with private instance attribute"""

    def __init__(self, size=0):
        """instantiation with optional size
        Args:
            size(int)=0: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter
        Args:
            value(int): number to be put into size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance method that returns tbe area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """public instance method that prints in
            stdout the square with character #
        """
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__size == 0:
                    print()
                else:
                    print("#", end="")
            print()
