#!/usr/bin/python3
"""a module containing a class that inherits from ``9-rectangle``"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from ``9-rectangle``"""
    def __init__(self, size):
        """instantiation with size and invoking the subclass"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    # override area from grandparent class
    def area(self):
        """returns the area"""
        return (self.__size * self.__size)
