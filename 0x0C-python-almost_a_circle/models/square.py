#!/usr/bin/python3
"""square model"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size

        Rectangle.__init__(self, size, size, x, y, id)

    # override __str__ from Rectangle
    def __str__(self):
        """returns the square description"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,\
            self.size)

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """property setter
        Arg:
            size: size of the square
        """
        self.width = value
        self.height = value
