class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, no_tyres, name):
        self.name = name
        self.no_tyres = no_tyres

volvo = Bus(no_tyres=6, name="Volvo")

print(volvo.name)