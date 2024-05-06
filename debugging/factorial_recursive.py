#!/usr/bin/python3
import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Read the command-line argument and calculate the factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
