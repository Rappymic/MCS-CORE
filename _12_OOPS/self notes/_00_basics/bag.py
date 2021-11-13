class Bag:
    def __init__(self, type, storage_volume, no_pockets, name):
        self.type = type
        self.storage_volume = storage_volume
        self.no_pockets = no_pockets
        self.name = name

    def uses(self):
        if self.storage_volume > 3:
            return f"{self.name}, carry clothes"
        else:
            return f"{self.name}, carry books"


backpack = Bag("Back Pack", 7, 3, "back pack")
saddle_bag = Bag("saddle_bag", 2, 5, "saddle bag")

print(backpack.uses())
print(saddle_bag.uses())
