class Shape:
    def __init__(self, name, no_sides):
        self.name = name
        self.no_side = no_sides

    def identify(self):
        if self.no_side == 4:
            return f"the {self.name} is a quardilateral"
        elif self.no_side == 5:
            return f"the {self.name} is a pentagon"
        else:
            return f"the {self.name} is a general polygon"

square = Shape("square", 4)
rhombus = Shape("Rhombus", 4)

pentt = Shape("Five sides", 5)

triangle = Shape("Triangle", 3)

print(square.identify())
print(rhombus.identify())
print(pentt.identify())
print(triangle.identify())

