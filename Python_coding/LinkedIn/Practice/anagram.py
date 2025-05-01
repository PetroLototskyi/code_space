def is_anagram(first_string, second_string):
    # Your code goes here
    first=""
    second=""
    for char in first_string.lower():
        if char.isalnum():
            first+=char
    for char in second_string.lower():
        if char.isalnum():
            second+=char

    return sorted(first) == sorted(second)


str1 = "Eleven plus two?"
str2 = "One plus twelve!"
str3 = "A cinnamon roll?"
str4 = "No canola oil, Mr.!"
result1 = is_anagram(str1, str2)
result2 =is_anagram(str3, str4) 

print(result1)
print(result2)
