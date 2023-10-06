#!/usr/bin/python3

if __name__ == "__main__":
    # Import necessary functions from calculator_1 module and sys module.
    from calculator_1 import add, sub, mul, div
    import sys

    # Check if the number of command-line arguments is correct.
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Define a dictionary to map operators to functions.
    ops = {"+": add, "-": sub, "*": mul, "/": div}

    # Check if the provided operator is valid.
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Convert command-line arguments to integers.
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # Perform the specified operation and print the result.
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
