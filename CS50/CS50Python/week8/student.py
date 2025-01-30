# Returns student as tuple, unpacking it
'''

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Revenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]
'''
# Stores student as dict


def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    # alternative:
    '''name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}'''




if __name__ == "__main__":
    main()
