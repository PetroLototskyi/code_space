# TODO
# Prompt for height
while True:
    height = int(input("Height: "))
    if 0 < height <= 8:
        break

# Creating main loop for rows
for i in range(1, height+1):

    # Loop for white spaces
    for j in range(i, height, +1):
        print(" ", end="")

    # Loop for "#"
    for k in range(j, height -1 - i, -1):
        print("#", end="")

    # Print two spases after "#"
    print("  ", end="");

    # Print same amount of "#"  as before two white spaces
    for k in range(j, height -1 - i, -1):
        print("#", end="")

    # Jump to new raw
    print();
