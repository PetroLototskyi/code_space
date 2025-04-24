def count_valid(numbers, lower, upper):
    # Your code goes here
    pos_num=[]
    for i in numbers:
        pos_num.append(abs(i))
    # print(pos_num)

    count = 0

    for num in pos_num:
        if num >= lower and num <= upper:
            count+=1



    return count

numbers = [-2, 5, -20, 30, -56]
lower = 1
upper = 30
result = count_valid(numbers, lower, upper)

print(result)