#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Example usage:
my_dictionary = {'apple': 3, 'banana': 1, 'cherry': 5}

# Replace the value for an existing key
update_dictionary(my_dictionary, 'apple', 6)

# Add a new key/value pair
update_dictionary(my_dictionary, 'date', 2)

print(my_dictionary)
