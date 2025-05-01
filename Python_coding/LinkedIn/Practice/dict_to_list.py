def build_menu(cakes):
    cakes[105]=["Coffee", 1.49]
    # Your code goes here
    result=[]
    for value in cakes.values():
        result.append(f'{value[0]} Cake - ${value[1]}')
        # print(value[0])
    return sorted(result, reverse=True)

cakes = {
		 100: ["Carrot", 1.99], 
		 101: ["Chocolate", 1.99], 
		 102: ["Strawberry", 2.19], 
		 103: ["Spice", 2.29], 
		 104: ["Vanilla", 1.79]
		 }
result = build_menu(cakes)
print(result)