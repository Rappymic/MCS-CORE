class Vehicle: # initialization of class
    have_tires = True

    def __init__(self, no_tyres, seats, range, name):
        self.no_tyres = no_tyres
        self.seats = seats
        self.range = range
        self.name = name

    def print_details(self):
        print(f"The vehicle name is {self.name} and has a range of {self.range} km")

v8 = Vehicle(4, 4, 500, "V8")

v8.print_details()
