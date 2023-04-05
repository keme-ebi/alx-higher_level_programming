#!/usr/bin/python3
"""a class LockedClass with no class or object attribute"""


class LockedClass:
    """stops user from dynamically creating new instance attributes"""
    __slots__ = ['first_name']
