# Demonstrates import and random.choice
# import random
# coin=random.choice(["heads","tails"])

# Demonstrates from
# from random import choice

# coin = choice(["heads","tails"])
# print(coin)

# Demonstrates randint
import statistics
import random

number = random.randint(1, 10)
print(number)

print("_________________________")

# Demonstrates shuffle

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

print("_________________________")
print(statistics.mean([100, 90]))
