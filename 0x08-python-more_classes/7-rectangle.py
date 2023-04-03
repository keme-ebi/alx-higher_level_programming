#!/usr/bin/python3
"""Defines a class Rectangle that defines a rectangle"""


class Rectangle:
    """an class that defines a rectangle with private instance attributes"""

    # public class attributes
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """instatiation with optional width and height
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """a public method that returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """a public method that returns the perimeter of tge rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints the rectangle with the character from print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""

        return '\n'.join(str(self.print_symbol) * self.__width
                for i in range(self.height))

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
