#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}  # Create a new dictionary to store the results

    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2  # Multiply each value by 2

    return new_dictionary
