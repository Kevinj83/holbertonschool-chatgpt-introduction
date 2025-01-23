#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate the factorial of a number."""
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrease n to avoid infinite loop
    return result

if __name__ == "__main__":
    # Ensure the script is run with the correct argument
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <number>")
    else:
        try:
            # Parse the input number
            num = int(sys.argv[1])
            if num < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                f = factorial(num)
                print(f)
        except ValueError:
            print("Please provide a valid integer.")

