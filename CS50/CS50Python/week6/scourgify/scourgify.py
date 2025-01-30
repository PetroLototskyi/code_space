import sys
import csv


def main():
    inspect_argv()  # Checking the command-line arguments

    new_list = []

    # Read data from the CSV file and store it in a list of dictionaries
    data_list = file_exist_read(sys.argv[1])

    for row in data_list:

        # Split the "name" field, create a new dictionary, and append to the new_list
        last, first = row["name"].split(",")
        new_list.append({"first": first.lstrip(), "last": last, "house": row["house"]})

    # Write the processed data to a new CSV file
    write_to_file(sys.argv[2], new_list)


def write_to_file(location, data_list):

    # Open the file specified by the 'location' variable in write mode ("w")
    with open(location, "w") as file:
        
        # Create a CSV DictWriter object, associating it with the opened file
        # The fieldnames parameter specifies the order of columns in the CSV
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        # Write the header row
        writer.writeheader()

        # Write the data rows
        for row in data_list:
            writer.writerow(row)


def inspect_argv():
    # If there are too few or too many arguments, or the file is not a Python file, exit the program
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")


def file_exist_read(name):  # Function to check if the file exists and read its lines
    # If the file does not exist, exit the program
    list = []
    try:
        with open(name) as file:
            reader = csv.DictReader(file)  # Using csv.DictReader to read the file
            for line in reader:
                list.append(line)
            return list
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
