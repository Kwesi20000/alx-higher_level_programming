#!/usr/bin/python3
"""
    This module extends list class
"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """this prints a sorted list"""
        print(sorted(self))
