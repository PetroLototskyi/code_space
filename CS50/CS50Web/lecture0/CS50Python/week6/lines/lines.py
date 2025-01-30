import sys


def main():
    inspect_argv()  # Checking the command-line arguments
    lines = file_exist_read(sys.argv[1])  # Reading the lines from the file

    count = len(lines)  # Counting the total number of lines
    for line in lines:  # Looping through each line
        if line.lstrip().startswith("#"):  # If the line is a comment
            count -= 1  # Decrease the count
        if len(line.strip()) == 0:  # If the line is empty
            count -= 1  # Decrease the count

    print(count)  # Printing the count of non-comment and non-empty lines


def inspect_argv():
    # If there are too few or too many arguments, or the file is not a Python file, exit the program
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


def file_exist_read(name):  # Function to check if the file exists and read its lines
    # If the file does not exist, exit the program
    try:
        with open(name) as file:
            lines = (
                file.readlines()
            )  # reed all lines from file and returning them as list
            return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
