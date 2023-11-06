#!/usr/bin/python3
"""Verifies if object is a class instance"""


def is_same_class(obj, a_class):
    """function returns true if object is an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
