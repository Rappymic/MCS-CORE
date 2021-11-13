class Fridge:
    def __init__(self, name, doors):
        self.name = name
        self.doors = doors

    def capacity(self):
        if self.doors == 2:
            return f"The capacity of {self.name} is 300 lts and have {self.doors} doors"
        else:
            return f"The capacity of {self.name} is 165 lts and have {self.doors} doors"

samsung = Fridge("Samsung", 2)

whirlpool = Fridge("Whirlpool", 1)

print(samsung.capacity())
print(whirlpool.capacity())