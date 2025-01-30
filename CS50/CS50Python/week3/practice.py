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

for index,i in enumerate(["a", "b", "c", "d"]):
    print(f"this is index -{index}, and this is i-{i}")

print("_" *10)

for index,i in enumerate(be_fruits):
    print(f"this is index -{index}, and this is i-{i}")

print("________________________________________")

for index,i in enumerate(be_fruits):
    print(f"this is index -{index}, and this is i-{be_fruits[i]}")

my_dict = {"a": 1, "b": 2, "c": 3}

# Access values using values() method
all_values = my_dict.values()
print(type(all_values))
print(all_values)

# Convert the view to a list if needed
values_list = list(all_values)

# Print the values
print(values_list)

s="Test this stafff!!!"
print(len(s))
for c in range(min(2, len(s))): # here "min" is use to pich what elnght we going to chose if string shorter then 2
   print(c)

tip = 40.47 * .67
print(f"Leave ${tip:.3f}")
