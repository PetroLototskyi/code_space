'''#  Writes to a file
name = input("What's your name? ")

file = open("name.txt" , "w") # it would overite existing file
file.write(name)
file.close()'''

# Appends to a file

name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")#write new line after each name
file.close()
