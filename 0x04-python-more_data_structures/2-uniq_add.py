#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set()  # Create an empty set to store unique integers
    result = 0  # Initialize the result variable to 0

    # Iterate through the elements of the list
    for num in my_list:
        if num not in unique_set:
            result += num
            unique_set.add(num)  # Add the unique integer to the set

    return result
