#!/usr/bin/python3
"""Defines a class Rectangle that defines a rectangle"""


class Rectangle:
    """an class that defines a rectangle with private instance attributes"""

    def __init__(self, width=0, height=0):
        """instatiation with optional width and height
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter
        Args:
            value(int): value for rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter
        Args:
            value(int): value for rectangle height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
