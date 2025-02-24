# Write a program to sum a series of numbers entered by the user. The
# program should first prompt the user for how many numbers are to be
# summed. The program should then prompt the user for each of the numbers in turn and print out a total sum after all the numbers have been
# entered. Hint: Use an input statement in the body of the loop.

import math

def main():

    n=int(input("Enter how many numbers you want to enter: "))
    sum=0

    while(n>0):
        number=int(input("Enter the number: "))
        sum=sum+ number
        n-=1

    print ("The sum is", sum)

if __name__ == "__main__":
    main()
