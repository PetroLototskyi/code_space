import inflect

# Create an instance of the inflect engine
p = inflect.engine()

# Initialize an empty list to store names
name_list = []

# Continue prompting the user for names until interrupted by CTRL+D
while True:
    try:
        # Get a name from the user, capitalize the first letter
        name = input("Name: ").title()
    except EOFError:
        # Exit the loop if CTRL+D is pressed
        break

    # Append the name to the list
    name_list.append(name)
# Display the farewell message with the joined names
print(f"Adieu, adieu, to {p.join(name_list)}")
