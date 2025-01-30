# TODO
# Promt for input card number
while True:
    try:
        number = int(input("Number: "))
        if number > 0:
            break
    except ValueError:
        pass

modulo, sumEven, sumOdd = 0, 0, 0
count, verdict, beforeLast = 0, 0, 0

# Calculating of two sums (od and even)
while number > 0:
    modulo = number % 10
    remainder = number // 10
    if 10 < remainder < 100:
        beforeLast = remainder

    number = remainder
    # Calculation the sum of odd numbers
    if count % 2 == 0:
        sumOdd += modulo
    # Calculating the sum of Even numbers whick are *2
    else:
        if modulo < 5:
            sumEven += modulo * 2
        # In case mpodule of number *2 is >9 the perfor this calculation
        else:
            sumEven += (modulo * 2) % 10 + (modulo * 2) // 10
    count += 1
# Check if cad has legit number
verdict = (sumEven + sumOdd) % 10

if verdict == 0 and modulo == 4 and count in (13, 16):
    print("VISA")
elif verdict == 0 and count == 15 and (beforeLast == 34 or beforeLast == 37):
    print("AMEX")
elif (
    verdict == 0
    and count == 16
    and modulo == 5
    and beforeLast % 10 != 0
    and beforeLast % 10 < 6
):
    print("MASTERCARD")
else:
    print("INVALID")
