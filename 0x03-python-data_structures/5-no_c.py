#!/usr/bin/python3

def no_c(my_string):
    # Create a new string without 'C' or 'c'
    result = ''.join(char for char in my_string if char not in ('C', 'c'))
    return result
