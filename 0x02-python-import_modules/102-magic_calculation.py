#!/usr/bin/python3

def magic_calculation(a, b):
    add, sub = None, None

    if a < b:
        add, sub = magic_calculation_102.add, magic_calculation_102.sub
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c
    else:
        return magic_calculation_102.sub(a, b)
