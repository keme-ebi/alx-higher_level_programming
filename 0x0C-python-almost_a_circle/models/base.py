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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            j_string = "[]"
        else:
            j_string = json.dumps(list_dictionaries)

        return j_string

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        to_json = cls.to_json_string([li.to_dictionary() for li in list_objs])

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(to_json)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON sring representation"""
        if json_string is None:
            f_jstring = []
        else:
            f_jstring = json.loads(json_string)

        return f_jstring
