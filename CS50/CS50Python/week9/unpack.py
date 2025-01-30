# Unpacks a list
'''
first, _ = input("What's yor name? ").split(" ")
print(f"hello, {first}")'''

# Passes positional arguments as usual
# https://harrypotter.fandom.com/wiki/Wizarding_currency


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins =[100, 50,25]

print(total(coins[0], coins[1], coins[2]), "Knuts")

 #Unpacks a list
print(total(*coins), "Knuts") # "*" unpack list

# Passes named arguments as usual
print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# Indexes into a dict

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# Unpacks a dict
coins={"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") # "**" unpack dictionary
