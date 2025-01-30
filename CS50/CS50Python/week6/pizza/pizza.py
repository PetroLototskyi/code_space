import sys
from tabulate import tabulate
import csv


def main():
    inspect_argv()  # Checking the command-line arguments
    
    # Read data from the CSV file and store it in a list of dictionaries
    data_list = file_exist_read(sys.argv[1])

    # Print the data in a tabular format using the tabulate library
    print(tabulate(data_list, headers="keys", tablefmt="grid"))


def inspect_argv():
    # If there are too few or too many arguments, or the file is not a Python file, exit the program
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def file_exist_read(name):  # Function to check if the file exists and read its lines
    # If the file does not exist, exit the program
    list = []
    try:
        with open(name) as file:
            reader = csv.DictReader(file) # Using csv.DictReader to read the file
            for line in reader:
                list.append(line)
            return list
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
