#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """MyInt class that reverses the == and != operators"""
    def __init__(self, value):
        """initialisation"""
        self.value = value

    def __str__(self):
        """returns sting representation"""
        return str(self.value)

    def __eq__(self, other):
        """changes == to != operator"""
        return self.value != other

    def __ne__(self, other):
        """changes != to == operator"""
        return self.value == other
