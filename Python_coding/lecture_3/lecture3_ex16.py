# A Fibonacci sequence is a sequence of numbers where each successive 
# number is the sum of the previous two. The classic Fibonacci sequence 
# begins: 1, 1, 2, 3, 5, 8, 13, . . .
#  . Write a program that computes the nth 
# Fibonacci number where n 
# is a value input by the user. For example, if 
# 6, then the result is 8. 

import math

def main():
    n=int(input("Enter the number for the Fibonacci sequence: "))
    fibonachi=0
    temp =0
    # Start with the first two Fibonacci numbers
    prev = 0  # First number
    curr = 1  # Second number

    if n==0:
        fibonachi=0
    elif n==1:
        fibonachi=1
    
    else:

    # Loop to calculate the next Fibonacci numbers
        for i in range(2, n+1): # Start from 2 because 0 and 1 are already known
            next_num = prev + curr  # Add the previous two numbers
            prev = curr  # Move 'curr' to 'prev'
            curr = next_num  # Move 'next_num' to 'curr'
            fibonachi=curr
                      
            

    print(f"\nFibbonachi sequence number of number n is: {fibonachi}")
     
 
if __name__=="__main__":
    main()
