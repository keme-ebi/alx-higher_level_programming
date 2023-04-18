#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """a class that inherits another class ``Base`` from the base module"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter
        Arg:
            width: width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter
        Arg:
            height: height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x private instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y private instance attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with the character ``#``"""
        for s in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j < self.x:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,\
                    self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an attribute to each argument and makes id the 1st arg\
            if *args, and no order if **kwargs"""
        if args or len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == 'y':
                    self.y = value
                if key == 'id':
                    self.id = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,\
                    "height": self.height, "width": self.width}
