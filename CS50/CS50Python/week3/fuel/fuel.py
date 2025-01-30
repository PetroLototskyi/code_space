while True:
    fuel= input("Fraction: ")

    try:
        x, y =fuel.split("/")
        gas = round((int(x)/int(y))*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if gas <= 1:
            print("E")
        elif gas > 100:
            continue
        elif gas >= 99:
            print("F")
        else:
            print (gas,"%", sep="")
        break



