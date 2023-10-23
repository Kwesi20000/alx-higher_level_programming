#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            num1 = float(my_list_1[i])
            num2 = float(my_list_2[i])
            if num2 == 0:
                raise ZeroDivisionError("division by 0")
            division_result = num1 / num2
            result.append(division_result)
        except (ValueError, ZeroDivisionError):
            result.append(0)
            print("wrong type" if isinstance(my_list_1[i], (int, float)) or 
                    isinstance(my_list_2[i], (int, float)) else "division by 0")
        except IndexError:
            result.append(0)
            print("out of range")

    return result
