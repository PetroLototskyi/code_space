# Numerologists claim to be able to determine a person's character traits
# based on the "numeric value" of a name. The value of a name is determined
# by summing up the values of the letters of the name where "a" is 1
# "b" is 2 "c" is 3 up to "z" being 26 For example the name "Zelle"
# would have the value 26 + 5 + 12 + 12 + 5 =
# 60 (which happens to be a
# very auspicious number, by the way). Write a program that calculates the
# numeric value of a single name provided as input.


def main():
    print("This program converts a textual message into numbers and sum them later")
    print("of numbers representing the Unicode encoding of the message.\n")
    name = input("Enter your name: ").lower()
    # print(name)
    sum = 0
    for ch in name:
        sum += ord(ch) - 96

    print(sum)
main()
