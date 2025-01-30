def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")

    # print(x)
    # print(y)
    # print(z)
    print(calculate(x, y, z))


def calculate(x, y, z):
    match y:
        case "+":
            return float(x) + float(z)
        case "-":
            return float(x) - float(z)
        case "*":
            return float(x) * float(z)
        case "/":
            return float(x) / float(z)


main ()

