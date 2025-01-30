import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Convert the input time format to a 24-hour format
    result = take_input(s)

    # Adjust hours based on AM/PM
    if result[2] == "PM" and result[0] < 12:
        result[0] += 12
    if result[2] == "AM" and result[0] == 12:
        result[0] = 0
    if result[5] == "PM" and result[3] < 12:
        result[3] += 12
    if result[5] == "AM" and result[3] == 12:
        result[3] = 0

    # Format and return the result
    return f"{result[0]:02}:{result[1]:02} to {result[3]:02}:{result[4]:02}"


def take_input(s):
    # Extract and validate time components from the input string
    result = []
    matches1 = re.search(
        r"^(\d{1,2}):*(\d{2})*\s+([APM]{2})?\s*to\s*(\d{1,2}):*(\d{2})*\s+([APM]{2})?$",
        s,
    )
    if matches1:
         # Hour, Minute, and AM/PM for both start and end times
        result.append(int(matches1.group(1)))
        result.append(0 if ":" not in s else int(matches1.group(2)))
        result.append(matches1.group(3))
        result.append(int(matches1.group(4)))
        result.append(0 if ":" not in s else int(matches1.group(5)))
        result.append(matches1.group(6))

        # Check for valid hour values
        if result[0] > 12 or result[3] > 12:
            raise ValueError

        # Check for valid minute values
        if result[1] >= 60 or result[4] >= 60:
            raise ValueError
        return result

    else:
        raise ValueError


if __name__ == "__main__":
    main()
