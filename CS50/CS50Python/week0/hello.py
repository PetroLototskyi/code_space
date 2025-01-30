# Demonstrates defining a function without parameters

def main():
    name = input("What's your name? ")
    hello(name)




def hello(to = "world"):
    print("hello,", to)


main()

# print(name)


# # Split user's name into first and last name
# first, last = name.split(" ")

# # Say hello to user
# print (f"hello, {first}")
