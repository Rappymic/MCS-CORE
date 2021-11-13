'''

        def eating(self):
            print("SUPER :: Animal : eating")
            ....

Method:
        I.  Method signature   ==> def eating(self):
        II. Method body(impl.) ==> print("SUPER :: Animal : eating") ...

Code resuability :  1. Signature + Body (Implementation)
                    2. Only signature

'''

'''  REUSE*
I: All sub classes required 
                common - method signature  
                common - method body(implementation)
                
                        Animal
                          - eating()
                Tiger   Lion     Cat   Dog
'''
class Animal:

    def __init__(self):
        pass
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")

class Tiger(Animal):

    def __init__(self):
        pass
        print("SUB  :: Tiger constructor")

class Lion(Animal):

    def __init__(self):
        pass
        print("SUB  :: Lion constructor")

class Cat(Animal):

    def __init__(self):
        pass
        print("SUB  :: Cat constructor")

class Dog(Animal):

    def __init__(self):
        pass
        print("SUB  :: Dog constructor")

ani = Animal()
ani.eating()
print("----------")
tiger = Tiger()
tiger.eating()
print("----------")
lion = Lion()
lion.eating()
print("----------")
cat = Cat()
cat.eating()
print("----------")
dog = Dog()
dog.eating()
print("----------")