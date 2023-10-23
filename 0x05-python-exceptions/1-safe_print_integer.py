#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to format and print the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If there's an error, return False
        return False
