# Reads from a file
'''
with open("names.txt") as file:
    lines = file.readlines()  #reed all lines from file and returning them as list

for line in lines:
    print("hello,", line.rstrip()) #strip end of the line (white spaces and  new lines)
'''
# Reads from a file, one line at a time
'''
with open("names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())
'''
# Appends names to a list for sorting

names = [] #create empty list

with open("names.txt") as file: #id you open file to "read" you do not need specifird "r"
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True): #sort list before iteration.Sort in revers order
    print(f"hello, {name}")


#even more simpler way:
'''
with open("names.txt") as file: #id you open file to "read" you do not need specifird "r"
    for line in sorted(file):
        print("hello,", line.rstrip())'''
