#!/usr/bin/python3
"""module with only one class in it"""


class BaseGeometry:
    """a class with a public instance method"""

    def area(self):
        """raises an exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public instance method that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.name = name
        self.value = value
