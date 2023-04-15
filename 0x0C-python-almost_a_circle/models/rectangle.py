#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """a class that inherits another class ``Base`` from the base module"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """property setter
        Arg:
            width: width of the rectangle
        """
        self.__width = width

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """property setter
        Arg:
            height: height of the rectangle
        """
        self.__height = height

    @property
    def x(self):
        """x private instance attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """property setter for x
        """
        self.__x = x

    @property
    def y(self):
        """y private instance attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """property setter for y
        """
        self.__y = y
