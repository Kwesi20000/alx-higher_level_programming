#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate through the original list and replace the specified element
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)

    return new_list
