#!/usr/bin/python3
"""module with a class ``Base``"""

import json


class Base:
    """a class that manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is None:
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

        if list_obj is None:
            to_json = []

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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if not filename:
            return []
        else:
            with open(filename, encoding='utf-8') as f:
                l_file = cls.from_json_string(f.read())
                return ([cls.create(**dic) for dic in l_file])

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(4, 5)
        dummy.x = 0
        dummy.y = 0
        dummy.update(**dictionary)
        return dummy
