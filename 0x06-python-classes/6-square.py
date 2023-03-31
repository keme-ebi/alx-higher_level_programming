#!/usr/bin/python3
"""Defines a class Square by private instance attribute"""


class Square:
    """a class with private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiation with optional size
        Args:
            size(int)=0: size of the square
            position(int)=(0, 0): position of square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value(int): number to be put into size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter
        Args:
            value(tuple of int): tuple of integers
        """
        if (not isinstance(value, tuple)
                or not (isinstance(v, int) for v in value)
                or not (i >= 0 for i in value)
                or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """public instance method that returns tbe area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """public instance method that prints in
            stdout the square with character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for n in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
