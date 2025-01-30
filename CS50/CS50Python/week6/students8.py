# Reads a CSV file using csv.reader
'''
import csv # import csv library

students = []

with open("students.csv") as file:
    reader = csv.reader(file) #use csv method to read the file. reder return list
    # print (reader)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

    #alternavive way
    # for name, home in reader:
        # students.append({"name": name, "home": home})


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
'''
# Reads a CSV file using csv.DictReader

import csv

students = []

with open("students_d.csv") as file:
    reader = csv.DictReader(file) #iterate through file and create a dictionary
    for row in reader:
        # print(row)
        students.append({"name": row["name"], "home": row["home"]})
        #can be simle as bellow as well
        # students.append(row)
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
