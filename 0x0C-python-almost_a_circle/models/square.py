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

    def update(self, *args, **kwargs):
        """assigns attributes either by args or kwargs"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
