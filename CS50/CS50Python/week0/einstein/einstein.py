def calculate(mass):
    return mass*(pow(300000000, 2))

def main():
    mass = int(input ("Enter mass: "))
    print(calculate(mass))

main()
