# Filters by house using loop

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Filters by house using loop
'''
gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])
        '''

# Filters by house using list comprehension
print("_________________Filters by house using list comprehension___________________")
gryffindors = [
student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

# Uses filter and key with lambda
print("_________________Uses filter and key with lambda___________________")

def is_gryffindor(s):
    return s["house"] == "Gryffindor"


gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]): # this is sort by name dict: key=lambda s: s["name"]
    print(gryffindor["name"])

# Uses filter with lambda
print("_________________Uses filter with lambda___________________________")

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]): # this is sort by name dict: key=lambda s: s["name"]
    print(gryffindor["name"])
