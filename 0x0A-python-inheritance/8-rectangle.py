#!/usr/bin/python3
"""8-rectangle module that has one class that inherits from 7-base_geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """a class that inherits from ``BaseGeometry``"""

    def __init__(self, width, height):
        """instantiation with width and height and\
                invoking the __init__ of the parent class"""
        BaseGeometry.__init__(self)

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
