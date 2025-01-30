# Creates list of dicts using loop
print("__________________________Creates list of dicts using loop______________")
students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)


# Uses dictionary comprehension instead
print("__________________________Uses dictionary comprehension instead______________")

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)

# Uses dictionary comprehension instead
print("__________________________Uses dictionary comprehension instead______________")

gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

# Iterates over a list by index
print("__________________________Iterates over a list by index______________")

for i in range(len(students)):
    print(i+1, students[i])

# Uses enumerate instead
print("__________________________Uses enumerate instead______________")

for i, student in enumerate(students):  #enumerate(iterable, start=0)
    print(i+1, student)
