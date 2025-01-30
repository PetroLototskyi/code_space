# Adds validation in __init__ using raise


class Student:
    def __init__(self, name, house, patronus): #if you give None value like house = None, then house field become optional
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus # Prompts for patronus too, but doesn't display yet

    #  Adds __str__
    def __str__(self):
        return f"{self.name} from {self.house}"

    # Adds charm method to cast a charm
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") # Prompts for patronus too
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
