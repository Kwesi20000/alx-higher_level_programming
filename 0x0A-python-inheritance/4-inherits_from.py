#!/usr/bin/python3
"""Checks if object is an inherited class instance"""


def inherits_from(obj, a_class):
    """function returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
