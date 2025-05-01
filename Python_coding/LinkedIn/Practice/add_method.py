class Cake:
    def __init__(self, flavor, price, slices):
        self.flavor = flavor
        self.price = price
        self.slices = slices

    def print_description(self):
        print(f"The {self.flavor} cake costs {self.price} and is divided into {self.slices} slices.")

    def sell(self, n):
        if n <=0:
            return f'Cannot sell zero or negative slices!'
        if n>self.slices:
            return f'Cannot sell more slices than we have ({self.slices})!'
        else:
            self.slices=self.slices-n
            return f'This cake has {self.slices} slices remaining.'

spice_cake = Cake("spice", 18, 8)
chocolate_cake = Cake("chocolate", 24, 6)

result1 = spice_cake.sell(5)
result2 = spice_cake.sell(4)
result3 = chocolate_cake.sell(-1)
result4 = chocolate_cake.sell(0)
print(result1)
print(result2)
print(result3)
print(result4)