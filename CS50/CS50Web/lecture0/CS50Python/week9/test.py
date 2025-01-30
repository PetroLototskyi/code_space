fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew mellon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plumps": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

be_fruits = fruits.copy()
print("pear" in be_fruits)

for index,i in enumerate(be_fruits):
    print(f"this is index -{index}, and this is i-{i}")

print("________________________________________")

for index,i in enumerate(be_fruits):
    print(f"this is index -{index}, and this is i-{be_fruits[i]}")
