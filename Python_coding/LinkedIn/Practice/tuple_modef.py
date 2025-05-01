def insert_item(my_tuple, new_value, index):
    # Your code goes here
    part1=my_tuple[:index]
    part2=my_tuple[index:]
    new_tuple=part1+(new_value,)+part2
    return new_tuple


sports = ('football', 'basketball', 'cricket', 'hockey', 'tennis', 'volleyball')
new_value1 = 'baseball'
index1 = 2

numbers = (7, 17, 13, 19, 5)
new_value2 = 11
index2 = 3

result1 = insert_item(sports, new_value1, index1)
result2 = insert_item(numbers, new_value2, index2)

print(result1)
print(result2)