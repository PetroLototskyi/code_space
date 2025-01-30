class Jar:
    def __init__(self, capacity=12):
        if not isinstance (capacity, int) or capacity < 0:
            raise ValueError ("You entered an invalid value")
        self._capacity = capacity
        self.cookies = 0


    def __str__(self):
        return "🍪"*self.cookies


    def deposit(self, n):
        if self.cookies +n > self._capacity:
            raise ValueError("Adding cookies would exceed the capacity of the jar")
        self.cookies += n


    def withdraw(self, n):
         if self.cookies - n < 0:
            raise ValueError("There are not enough cookies in the jar")
         self.cookies -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

def main():
    jar = Jar()
    print(jar.capacity)
    jar.deposit(2)
    print(str(jar))
    jar.withdraw(1)
    print(str(jar))
    jar.deposit(7)
    print(jar)
    print(str(jar))

if __name__ == "__main__":
    main()

