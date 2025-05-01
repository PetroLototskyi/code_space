from string import ascii_lowercase

show_expected_result = False
show_hints = False

def check_string(my_string):
    # Your code goes here
    str_lower=my_string.lower()
    remain=""
    for i in ascii_lowercase:
        if i not in str_lower:
            remain+=i
    if remain=="":
        return "The string contains all the letters of the alphabet."
    else:
        return f"The string is missing the following letters: {remain}"


str1 = "How quickly jumping zebras vex."
str2 = "Sphinx of black quartz, judge my vow."
result1 = check_string(str1)
result2 = check_string(str2)

print(result1)
print(result2)
    