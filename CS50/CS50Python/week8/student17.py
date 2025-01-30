# Removes patronus for simplicy, circumvents error-checking by setting attribute


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter
    @property # Adds @property for name
    def name(self):
        return self._name

    #Setter
    @name.setter # Adds @property for name
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name


    # Getter
    @property # Adds @property for house
    def house(self):
        return self._house

    #Setter
    @house.setter # Adds @property for house
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
