'''
# Catches a ValueError

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
    '''

'''
# Demonstrates a NameError
try:
    x=int (input("What's x? "))
except ValueError:
    print("x is not an inteher")

print(f"x is {x}")
'''
'''
# Demonstrates else
try:
    x=int (input("What's x? "))
except ValueError:
    print("x is not an inteher")
else:
    print(f"x is {x}")
'''

# Adds a loop

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
