
'''
'''
'''
SC1: As a sub class, I. inherit all super class methods
                     II.create your own methods
'''
# SC 1
class A:
    def __init__(self):
        print("SUPER : A constr")

    def read(self):
        print("A reading")

# A has one behavior read()
class B(A):

    def __init__(self):
        print("SUB : B constr")

    def write(self):
        print("B writing")

'''
B has two behaviors 
       read()   - inherited method
       write()  - own method

'''
a1 = A()
a1.read()

b1 = B()
b1.read()   # inherited method
b1.write()  # sub class specific method

# SC2
'''
SC2: As a sub class, I. inherit all super class methods,override if required
                     II.create your own methods
'''
class A: # A has 2 behaviors read() execute()
    def __init__(self):
        print("SUPER : A constr")

    def read(self):
        print("A reading")

    def execute(self):
        print("A executing")

class B(A):

    def __init__(self):
        print("SUB : B constr")

    def read(self):  # method overriding
        print("B reading")

    def write(self):
        print("B writing")

'''
B has 3 behaviors   - execute() from super class through inheritance
                    - read() i.e, from sub class overriden method
                    - write() from sub class(its  own method)
                    
a1 = A()
a1.read()
a1.execute()

b1 = B()
b1.read()
b1.write()
b1.execute()

Inherited method  : execute()
Overriden method  : read()
Own method        : write()

'''