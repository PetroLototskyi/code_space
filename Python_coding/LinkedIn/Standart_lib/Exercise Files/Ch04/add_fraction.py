# Use the fracction module to add the fractions together and return a tuple (numerator and denominator)with the sum
from fractions import Fraction

def add_fractions(numerator1, denominator1, numerator2, denominator2):
    # Your code goes here
    frac1 = Fraction(numerator1, denominator1)
    frac2 = Fraction(numerator2, denominator2)
    total = frac1 + frac2
    print(f"Fraction 1: {frac1}")
    print(f"Fraction 2: {frac2}")
    print(f"Total: {total}")
    return (total.numerator, total.denominator)



numerator1 = 1
denominator1 = 2
numerator2 = 1
denominator2 = 3
result = add_fractions(numerator1, denominator1, numerator2, denominator2)
print(result)