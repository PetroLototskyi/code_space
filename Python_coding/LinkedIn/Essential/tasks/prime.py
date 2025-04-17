
def allPrimesUpTo(num):
    # Your code goes here.
    numbers=[2]
    # for number in range(2, num):
    #     for factor in range(2, int(number ** 0.5) + 1):
    #         if number % factor == 0:
    #             break
    #     else:
    #         numbers.append(number)
    for number in range(3, num):
        sqrt_num=number**0.5
        for factor in numbers:
            if number % factor == 0:
                break #no prime
            if factor > sqrt_num:
               numbers.append(number)
               break
    return numbers

num = 100
result = allPrimesUpTo(num)
print(result)