# Prompt for height
while True:
    try:
        height = int(input("Height: "))
        if 0 < height <= 8:
            break
    except ValueError:
        print ("Not an intager")

# Creating main loop for rows
for i in range(1, height + 1):
    # Print white spaces
    print(" " * (height - i), end="")

    # Print "#" characters
    print("#" * i, end="  ")

    # Print the same amount of "#" as before two spaces
    print("#" * i)
