#!/usr/bin/python3
"""1-my_list module that has a class and one public instance method"""


class MyList(list):
    """a class that inherits from list"""
    def __init__(self):
        """initialisation of inheritance"""
        list.__init__(self)

    def print_sorted(self):
        """public instance method that prints the list in ascending order"""
        print(sorted(self))
