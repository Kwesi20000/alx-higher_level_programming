#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            try:
                value = int(item)  # Try to convert the item to an integer
                print("{:d}".format(value), end=' ')
                count += 1
                if count >= x:
                    break
            except (ValueError, TypeError):
                continue
        print()  # Add a new line after printing all integers
    except IndexError:
        pass
    return count
