

class Item:
    def __init__(self, item_type, price):
        self.item_type = item_type
        self._price = price

    @property
    def price(self):
        return self._price

class Cake(Item):
    def __init__(self, kind, price, slices):
        super().__init__("cake", price)
        self.kind = kind
        self.slices = slices

spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)



result1 = isinstance(spice_cake, Cake)
result2 = issubclass(Cake, Item)
result3 = hasattr(spice_cake, "price")
result4 = spice_cake.item_type == "cake"

try:
    # Attempt to set the price attribute.
    spice_cake.price = 17
except AttributeError:
    # Return True if the price attribute cannot be set.
    print("error ocures")

print(result1)
print(result2)
print(result3)
print(result4)