#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_integer = True
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        is_integer = False
    return is_integer
