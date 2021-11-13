'''

'''
'''
                           Animal
                             eating()
                  Cat    Dog   Tiger    Lion

Here eating() is required for all sub classes
But each animal want their own implementation

Method :  signature
          body

'''

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self):
        print("In Animal object")

    @abstractmethod
    def eating(self):  # Generic behavior
        pass


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # method overriding  is mandatory here
    def eating(self):
        print("Cat is Eating")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

cat = Cat()
cat.sleeping()
cat.eating()

# SCENARIOS
print("--------------------------")


class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # method overriding  is mandatory here
    def eating(self):
        print("DOG is Eating")

    # Specific behavior
    def barking(self):
        print("DOG is barking")




dog = Dog()
dog.barking()
dog.eating()
