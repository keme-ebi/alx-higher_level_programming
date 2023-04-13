#!/usr/bin/python3
"""a module with one function that writes an object to a file using JSON"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using JSON representation
       Args:
            my_obj: object to be written as JSON rep.
            filename: text file to be written to
    """
    to_json = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(to_json)
