#!/usr/bin/python3
"""module with a class ``Base``"""

import json


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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"

        j_string = json.dumps(list_dictionaries)
        return j_string
