from datetime import date
import inflect
import re
import sys

p = inflect.engine()


def main():
    # Prompt the user for their date of birth
    promt = input("Date of Birth: ")

    # Obtain user's date of birth
    year, month, day = obtain_DOB(promt)

    try:
        # Create a date object from the obtained date of birth
        DOB=date (year, month, day)

    except (ValueError):
        # Handle the case where the date of birth is invalid
        sys.exit("Invalid date")

    # Get today's date
    today_day = date.today()

    # Calculate the difference in days
    substraction_days= today_day-DOB

    # Convert days to minutes
    minutes = substraction_days.days * 24 * 60

    # Convert minutes to words using inflect
    result = p.number_to_words(minutes, andword="")
    print(f"{result.capitalize()} minutes")

def obtain_DOB(DOB):



     # Validate the input format using a regular expression
    if re.search(r"^\d{4}-\d{2}-\d{2}$", DOB):

        # Extract year, month, and day from the input
        year = int(DOB[0:4])
        month = int(DOB[5:7])
        day = int(DOB[8:10])
    else:
         # Handle the case where the input format is invalid
         sys.exit("Invalid date")

    return year, month, day



if __name__ == "__main__":
    main()
