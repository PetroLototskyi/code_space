 import csv

# Open CSV file
with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["problem"]

        if favorite in counts:
            counts[favorite] += 1
        else:
            counts [favorite] = 1


favorite = input("Favorite: ").title()
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")





