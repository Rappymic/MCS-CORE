class Cycle: # initialization of class

    def __init__(self, no_tyres, range, name):
        self.no_tyres = no_tyres
        self.range = range
        self.name = name

    def print_details(self):
        print(f"The vehicle name is {self.name} and has a range of {self.range} km")

    def type_vehicle(self):
        if self.no_tyres == 2:
            return f"this {self.name} is common bycycle"
        elif self.no_tyres == 3:
            return f"this {self.name} is a tricycle"
        else:
            return f"this {self.name} is a show unicycle"

bycycle = Cycle(2,100,"Hero")
tricycle = Cycle(3,100, "Hercules")
unicycle = Cycle(1, 20, "Orange")

bycycle.print_details()
print(bycycle.type_vehicle())

tricycle.print_details()
print(tricycle.type_vehicle())

unicycle.print_details()
print(tricycle.type_vehicle())