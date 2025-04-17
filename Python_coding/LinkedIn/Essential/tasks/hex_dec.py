# Python code​​​​​​‌‌​‌​​‌​​‌‌​‌‌​​​​​‌‌​‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if len(hexNum)>3:
        return None
    for char in hexNum:
        if char not in hexNumbers:
            return None
        
    result = 0  
    multiply =  len(hexNum) -1
    for char in hexNum:
        value=hexNumbers[char]
        result+=value*(16**multiply)
        multiply-=1
        # print(value)
    
    # print(len(hexNum))
    # print(f"16**2= {16**2}")
    return result



# print(hexToDec('spam spam spam'))
print(hexToDec('A2'))