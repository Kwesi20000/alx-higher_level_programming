#!/usr/bin/python3
"""writing first docstring"""
import math


class MagicClass:
    """setting up the magic lol"""

    def __init__(self, radius=0):
        """ writing second docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """again with the docstring created"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """using such docstring"""
        return 2 * math.pi * self.__radius
