'''

'''
'''
                           Animal
                  Cat    Dog   Tiger    Lion
                  
Here eating() is required for all sub classes
But each animal want their own implementation

Method :  signature
          body

'''

class Animal:
    def __init__(self):
        print("In Animal object")

    # Generic behavior
    def eating(self):
        print("Animal Eating")  # Here we are writing body for eating() unncesarily


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

    # method overriding
    def eating(self):
        print("Cat is Eating")

cat = Cat()
cat.sleeping()
cat.eating()


# SCENARIOS
print("--------------------------")
class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # Specific behavior
    def barking(self):
        print("DOG is barking")

    # method overriding
    def eating(self):
        print("DOG is Eating")

dog = Dog()
dog.barking()
dog.eating()
