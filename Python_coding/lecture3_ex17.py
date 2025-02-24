# You have seen that the math library contains a function that computes 
# the square root of numbers. In this exercise, you are to write your own 
# algorithm for computing square roots. One way to solve this problem 
# is to use a guess-and -check approach. You first guess what the square 
# root might be, and then see how close your guess is. You can use this 
# information to make another guess and continue guessing until you have 
# found the square root (or a close approximation to it). One particularly 
# good way of making guesses is to use Newton's method. Suppose x is the 
# number we want the root of, and guess is the current guessed answer. The 
# guess can be improved by using computing the next guess as: 
# guess+ gu�ss 
# 2 
# Write a program that implements Newton's method. The program 
# should prompt the user for the value to find the square root of (x) and 
# the number of times to improve the guess. Starting with a guess value 
# of x/2, your program should loop the specified number of times applying 
# Newton's method and report the final value of guess. You should also 
# subtract your estimate from the value of math. sqrt (x) to show how close 
# it is.

# A Fibonacci sequence is a sequence of numbers where each successive 
# number is the sum of the previous two. The classic Fibonacci sequence 
# begins: 1, 1, 2, 3, 5, 8, 13, . . .
#  . Write a program that computes the nth 
# Fibonacci number where n 
# is a value input by the user. For example, if 
# 6, then the result is 8. 

import math

def main():
    x=int(input("Enter the number you want a square root of: "))
    gues=float(input("Enter your square quess: "))
    n=int(input("Enter the number of time for gues improving: "))
    # result=1

    for i in range(1, n+1): 
        print(i)
        gues = (gues+(x/gues))/2
        print(f"Guess {i} is: {gues:.6f}")

    print(f"The math sqr of {x} is: {math.sqrt(x)}")


      
if __name__=="__main__":
    main()
