amount = 50
while True:
    print("Amount Due:", amount)
    coin = int (input("Insert Coin: "))
    if coin in [25, 10, 5] :
        amount -=coin
        if amount <=0:
            amount*=-1
            break

print("Change Owed:", amount)

