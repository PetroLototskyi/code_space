# Adds functions, uses break and return
'''
def main():
    x = get_int()
    print(f" x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break

    return x

main ()
'''

# Removes else
def main():
    x = get_int()
    print(f" x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main ()
