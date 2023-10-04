#!/usr/bin/python3
# 8-uppercase.py
def uppercase(input_str):
    result = ""
    for char in input_str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase using ord() and chr() functions
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    print(result)
