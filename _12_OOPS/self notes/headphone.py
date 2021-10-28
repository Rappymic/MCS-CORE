class Headphone:
    def __init__(self, name, typ, cost):
        self.name = name
        self.typ = typ
        self.cost = cost

philips = Headphone("Phillips", "One the ear", 1000)
sony = Headphone("Sony", "In the year", 500)

print(philips.name)
print(philips.typ)