class Chair:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def is_soft(self):
        if self.type == "Cushioned":
            return f"it is a comfortable chair"
        else:
            return f"it isn't a comfortable chair"

sofa = Chair("sofa", "Cushioned")

plastic_chair = Chair("Plastic Chair", "Not Cushioned")

print(f"{sofa.name} is a {sofa.type} chair, thats why", sofa.is_soft())
print(f"{plastic_chair.name} is a {plastic_chair.type} chair, thats why",
      plastic_chair.is_soft())