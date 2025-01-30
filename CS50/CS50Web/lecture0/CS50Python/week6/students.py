# Reads a CSV file
'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") #row is the list with two values, automatecly created
        print(f"{row[0]} is in {row[1]}") #crea
        # print (row)
'''
# Sorts a list of strings
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") #assign two varible at ones
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''
# Reads a CSV file into a list of dict objects, creating empty dict first
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["house"] = house
        # students.append(student)
        students.append({"name": name, "house": house})
        # print(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key = get_name): #use "key" parameter on created variable to sort
    print(f"{student['name']} is in {student['house']}") # use sinle quotte ' becouse outside " already used
'''
# Sorts a list of dictionaries using a lambda function

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

#lambda is like anonomus function that has no name
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
