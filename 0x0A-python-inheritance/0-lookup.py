#!/usr/bin/python3
"""
    This module provides functionality to retrieve the list of accessible
    attributes and methods associated with an object.
"""


def lookup(obj):
    """This function looks out for all attributes and methods of an object"""
    return dir(obj)
