#!/usr/bin/python3
"""this is a module that defines a class MyInt that inherits from int"""


class MyInt(int):
    """this invert int operators == and !="""

    def __eq__(self, value):
        """this override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """this override != operator with == behavior"""
        return self.real == value
