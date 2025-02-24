# Write a program to find the sum of the first n natural numbers, where the
# value of n is provided by the user

def main():
    n=int(input("Enter n number: "))
    # print (" This is n:", n)
    sum=0

    while(n>0):
        sum=sum +n
        n-=1


    print ("The sum of numbers is:" , sum)
if __name__ == "__main__":
    main()
