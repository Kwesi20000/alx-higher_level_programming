#!/usr/bin/python3

def remove_char_at(input_str, n):
    # Check if n is a valid index
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if n is out of range

    # Create a new string by excluding the character at position n
    new_str = ""
    for i in range(len(input_str)):
        if i != n:
            new_str += input_str[i]

    return new_str
