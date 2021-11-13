class Fan:
    def __init__(self, name, type, rpm):
        self.name = name
        self.type = type
        self.rpm = rpm

    def uses(self):
        if self.rpm > 1000:
            return f"{self.name} is fast and have {self.rpm} RPM"
        else:
            return f"{self.name} is slow anf have {self.rpm} RPM"

    def type_(self):
        if self.type == "AC":
            return "This is a normal Fan"
        else:
            return "This is a specialised Fan"


fan1 = Fan("Khaitan", "AC", 2000)
fan2 = Fan("CoolerMaster", "DC", 500)

print(fan1.type_())
print(fan1.uses())
print(fan2.uses())
print(fan2.type_())

