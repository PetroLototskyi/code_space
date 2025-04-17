
def factorial(num):
    # Your code goes here.
    if type(num) != int or num < 0:
        return None
    
    if num ==0:
        return 1
    
    
    fac = 1
    while num>0:
        fac=fac*num

        print(f"factorias is: {fac}")
        print(num)
        num-=1
        print(num)
    return fac

#  another solution:
#       return num*factorial(num-1)


number = 5
result = factorial(number)
print(result)