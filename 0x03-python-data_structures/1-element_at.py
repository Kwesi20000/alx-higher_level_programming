#!/usr/bin/python3

# Function retrieves an element from the list
def element_at(my_list, idx):
    if  idx < 0 or idx >= len(my_list):
        return (None)
    else:
        return (my_list[idx])
