class Light:
    def __init__(self, name, type, lumens):
        self.name = name
        self.type = type
        self.lumens = lumens

    def uses(self):
        if self.lumens >1000:
            return f"{self.name} is bright light with {self.lumens} lumens"
        else:
            return f"{self.name} is a night light with {self.lumens} lumens"
    def type_(self):
        if self.type == "AC":
            return "This is a normal light"
        else:
            return "This is a specialised light"

cfl = Light("CFL","AC", 3000)

led = Light("LED", "DC", 100)

print(cfl.uses())
print(cfl.type_())
print(led.uses())
print(led.type_())