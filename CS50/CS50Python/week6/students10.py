# Writes a CSV file using csv.writer
import csv
'''
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_w.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home]) #functiomn will write to file list of spesified names
'''
# Writes a CSV file using csv.DictWriter

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_w.csv", "a") as file:  #In this case, "a" stands for "append" mode. In "append" mode, if the file already exists, the new data will be appended to the end of the file.
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
