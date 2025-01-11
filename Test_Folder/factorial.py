import math


def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = 5
print(f"The factorial of {n} is: {factorial_iterative(n)}")


def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage
n = 5
print(f"The factorial of {n} is: {factorial_recursive(n)}")


import math

n = 5
print(f"The factorial of {n} is: {math.factorial(n)}")
