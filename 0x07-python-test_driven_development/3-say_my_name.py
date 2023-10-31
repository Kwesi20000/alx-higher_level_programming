#!/usr/bin/python3
"""

A module that prints a message

"""


def say_my_name(first_name, last_name=""):
    """ A function that prints "My name is <first name> <last name>"

    Args:
        first_name: the first name
        last_name: the last name

    Returns:
        Does not return anything

    Raises:
        TypeError: If first_name or last_name is not a string


    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
