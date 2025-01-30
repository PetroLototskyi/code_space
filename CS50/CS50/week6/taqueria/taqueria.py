# Menu with item prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize an empty order list and total cost
order = []
total_cost = 0.0

# Function to display the current order and total cost
def display_order():
    print("\nCurrent Order:")
    for item in order:
        print(item)
    print("Total: ${:.2f}\n".format(total_cost))

try:
    while True:
        # Prompt for item input
        item_input = input("Enter an item (Ctrl-D to finish): ").title()

        # Check if item is in the menu
        if item_input in menu:
            order.append(item_input)
            total_cost += menu[item_input]
            display_order()
        else:
            print("Item not found on the menu. Please try again.")

except EOFError:
    # Handle Ctrl-D (EOF) input to exit the loop
    print("\nOrder completed. Thank you!")
