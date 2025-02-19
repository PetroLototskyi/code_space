# Write a program that finds the average of a series of numbers entered by
# the user. As in the previous problem, the program will first ask the user
# how many numbers there are. Note: The average should always be a float,
# even if the user inputs are all ints.

import math

def main():

    n=int(input("Enter how many numbers you want to enter: "))
    n_copy=n
    sum=0

    while(n>0):
        number=float(input("Enter the number: "))
        sum=sum+ number
        n-=1

    avg=sum/n_copy
    print ("The average is", avg)

if __name__ == "__main__":
    main()
