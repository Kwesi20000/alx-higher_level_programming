#!/usr/bin/python3
"""This is a module that defines a Python class-to-JSON function"""


def class_to_json(obj):
    """this returns a dictionary representation of a simple data structure"""
    return obj.__dict__
