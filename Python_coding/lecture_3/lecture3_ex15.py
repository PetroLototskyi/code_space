# Write a program that approximates the value of pi by summing the terms
# of this series: 4/1- 4/3+4/5- 4/7+4/9- 4/11+. . . The program should
# prompt the user for n, the number of terms to sum, and then output the
# sum of the first n terms of this series. Have your program subtract the
# approximation from the value of math.pi to see how accurate it is.

import math

def main():
    n=int(input("Enter how many series you want to aproximate: "))
    pi_approx = 0

    for i in range(n):
        term = 4/(2*i+1) # Compute the next term in the series: 4 / (odd denominator)
        if i%2==1: # Check if the term index 'i' is odd
            term=-term  # Alternate signs (+, -, +, -, ...) for correct series computation
        pi_approx+=term

    print(f"\nApproximation of π using {n} terms: {pi_approx}")
    print(f"Actual value of π: {math.pi}")

    # print(0%2)
    # print(1%2)
    # print(2%2)
    # print(3%2)

 
if __name__=="__main__":
    main()
