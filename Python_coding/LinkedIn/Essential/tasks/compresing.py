# Python code​​​​​​‌‌​‌​​‌​‌​‌​‌‌​​​‌​​​‌​​‌ below
import json 
import os

def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

# The filename that will be passed to this function
# is 10_04_challenge_art.txt
def encodeFile(filename, newFilename):
    # Your code goes here.
    with open(filename, 'r') as file:
        content = file.read()

    encoded = encodeString(content)

    with open(newFilename, 'w') as file:
        for char, count in encoded:
            file.write(f'{repr(char)}\t{count}\n')

def decodeFile(filename):
    # Your code also goes here.
    encodedList = []
    with open(filename, 'r') as file:
        for line in file:
            char_repr, count = line.strip().split('\t')
            char = eval(char_repr) 
            encodedList.append((char, int(count)))

    return decodeString(encodedList)

    

original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize}')
encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

new_filesize = os.path.getsize("10_04_challenge_art_encoded.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('10_04_challenge_art_encoded.txt')
print(decoded)