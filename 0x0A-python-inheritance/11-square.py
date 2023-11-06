#!/usr/bin/python3
"""this is a module that defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this represent a square"""

    def __init__(self, size):
        """this initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
