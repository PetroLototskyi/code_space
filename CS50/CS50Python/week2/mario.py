# for _ in range (3):
#     print("#"*3)

def main():
    print_column(3)
    print("_______________")
    print_row(4)
    print("_______________")
    print_square(3)
    print("_______________")
    print_square2(3)
'''
def print_column(height):
    for _ in range(height): # Prints column of bricks using a function with a loop
        print("#")
'''

def print_column(height):
    print("#\n" * height, end="") # Prints column of bricks using a function with str multiplication

def print_row(width):
    print("?" * width)

def print_square(size): # Prints square of bricks using a function with nested loops
    #For each row in square
    for i in range (size):
        #For each brick in row
        for j in range (size):
            #Print the brik
            print("#", end="")
        #Jump to new line
        print()

def print_square2(size):# Prints square of bricks using a function with a loop and str multiplication
    for i in range (size):
        print("#" * size)


main()
