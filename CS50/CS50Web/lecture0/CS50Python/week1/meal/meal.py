def main():
    time = input ("What time is it? ")

    if 7.00 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.00 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.00 <= convert(time) <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    min_float = float(minutes)/60
    return float(hours)+min_float


if __name__ == "__main__":
    main()
