from pyfiglet import Figlet
import sys
import random

# Create a Figlet instance
figlet = Figlet()

# Check command-line arguments for font selection
if len(sys.argv) == 1:
    # If no arguments provided, choose a random font
    font_name = random.choice(figlet.getFonts())

# If using the -f or --font option, use the specified font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font_name = sys.argv[2]

try:
    # Set the selected font
    font = figlet.setFont(font=font_name)
except NameError:
    # Handle exeption and exit the program
    print("Invalid usage")
    sys.exit(1)

# Get user input for the text to render
str = input("Input: ")

# Render and print the output using the selected font
print(f"Output:\n {figlet.renderText(str)}")
