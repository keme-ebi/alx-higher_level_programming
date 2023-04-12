#!/usr/bin/python3
"""module with only one class in it"""


class BaseGeometry:
    """a class with a public instance method"""

    def area(self):
        """raises an exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
