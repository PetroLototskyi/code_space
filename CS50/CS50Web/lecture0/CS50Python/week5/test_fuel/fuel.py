def main():
    converted = convert(input("Fraction: "))
    print(gauge(converted))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            gas = round((int(x) / int(y)) * 100)
            if gas > 100:
                fraction=input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            raise
        else:
            return gas


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
