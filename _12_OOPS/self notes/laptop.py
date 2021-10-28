class Laptop:

    def __init__(self, company, screensize, cost):
        self.company = company
        self.screensize = screensize
        self.cost = cost

    def get_details(self):
        return f"Laptop is made from {self.company} and costs around {self.cost}"

acer715 = Laptop(company="Acer", cost=55000, screensize=15.6)

print(acer715.get_details())