#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, v in a_dictionary.items():
        if k in a_dictionary and v not in a_dictionary:
            a_dictionary.update( {key: value} )
        elif k not in a_dictionary:
            a_dictionary.update( {key: value} )
        return a_dictionary
