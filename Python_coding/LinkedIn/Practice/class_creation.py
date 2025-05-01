class Cake:
    def __init__(self, kind, price, slice):
        self.kind=kind
        self.price=price
        self.slice=slice

    def describe(self):
        return f"The {self.kind} cake cost ${self.price} and is divided into {self.slice} slices."


spice_cake =Cake("spice", 18, 8)
chocolate_cake=Cake("chocolate", 24, 6)


result1 = [spice_cake.describe(), isinstance(spice_cake, Cake)]
result2 = [chocolate_cake.describe(), isinstance(chocolate_cake, Cake)]

print(result1)
print(result2)