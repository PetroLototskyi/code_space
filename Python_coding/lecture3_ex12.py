# Write a program to find the sum of the cubes of the first n natural numbers
# where the value of n is provided by the user.

import math

def main():

    print("text")

    n=int(input("Enter n number: "))
    sum=0

    while(n>0):
        sum=sum+ n**3
        n-=1

    print ("The sum is", sum)

if __name__ == "__main__":
    main()


