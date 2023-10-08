#!/usr/bin/python3

# Iterate through the list
def print_list_integer(my_list=[]):
    if len(my_list) == 0:
        print("Empty list")
    else:
        for i in my_list:
            print("{:d}".format(i))
