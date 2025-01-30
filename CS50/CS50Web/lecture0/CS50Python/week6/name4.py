# Adds context manager

name = input("What's your name? ")

with open("names.txt", "a") as file: #modern way to open file that deal with automatic closing
    file.write(f"{name}\n")
