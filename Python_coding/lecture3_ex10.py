
# Write a program to determine the length of a ladder required to reach a
# given height when leaned against a house. The height and angle of the
# ladder are given as inputs. To compute length use:
# length=heiht/sin angle­
# sin angle
# Note: The angle must be in radians. Prompt for an angle in degrees and
# use this formula to convert:
# radians = p/180 degrees"

import math

def convert(angle):
    radiant=(math.pi/180)*angle

    return radiant

def main():
    print("This program to determine the length of a ladder")
    print()
    
    height=float(input("Enter the ladder height: "))
    angle=float(input("Enter angle in degree: "))

    radiant=convert(angle)
    length=height/math.sin(radiant)

    print(f"The length of the ladder is: {length: .2f}")



main()