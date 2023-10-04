#!/usr/bin/python3
# 9-print_last_digit.py
def print_last_digit(number):
    # Ensure the number is positive or zero
    number = abs(number)

    # Calculate the last digit using modulo 10
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end="")

    # Return the last digit value
    return last_digit
