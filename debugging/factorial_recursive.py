#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculates the factorial of a given number recursively.

    Parameters:
        n (int): The number whose factorial is to be calculated.

    Returns:
        int: The factorial of the input number.
    """
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive call to calculate factorial

# Read the command-line argument and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)

