#!/usr/bin/python3
"""module with a class ``Base``"""


class Base:
    """a class that manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
