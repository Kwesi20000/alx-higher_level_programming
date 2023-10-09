#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements
    a = tuple_a + (0, 0)  # Add (0, 0) if tuple_a has fewer than 2 elements
    b = tuple_b + (0, 0)  # Add (0, 0) if tuple_b has fewer than 2 elements

    # Perform addition of corresponding elements
    result = (a[0] + b[0], a[1] + b[1])

    return result
