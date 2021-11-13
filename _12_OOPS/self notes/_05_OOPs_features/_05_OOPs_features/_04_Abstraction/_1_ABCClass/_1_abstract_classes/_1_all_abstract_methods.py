from abc import ABC, abstractmethod
'''
Access modifiers:  private public default protected
_ __




4. ABSTRACTION :
===================
Hiding the implementation details i.e, method body

Class, Abstract Class, Interface


Inheritance: Super class Sub class
           : When all sub classes has common features ==> Define Methods Super class with body
		   : When all sub classes has unique implementation ==> 
		               - Make class as Abstract class(super class)
		               - Define abstract methods* in super class
Abstraction : 0 to 100%
0%   -- In super abstract class,all are concrete methods      define - class
50%  -- 10 methods - 5 abstract methods + 5 concrete methods  define - abstract class
100% -- In super abstract class, all are abstract methods     define - interface

Employee emp = new SoftwareEmployee() 
Polygon poly = new Triangle()
poly.noofsides()
poly.get_data()

'''
class Polygon(ABC):  # Polygon is Abstract Class

    @abstractmethod
    def noofsides(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Triangle with 3 sides")

    # overriding abstract method
    def get_data(self):
        print("Quadrilateral data")



class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I am Quadrilateral with 4 sides")

    # overriding abstract method
    def get_data(self):
        print("Quadrilateral data")

# Here define Polygon as Interfeace instead of Abstrct class


'''
Polygon --> m1() m2()
Triangle --> m1() m2() m3()

Triangle t1 = new Triangle()  # 2L can <--- 2L water
    ==> We can create our own methods in sub class

t1.m1()
t1.m2()
t1.m3()


Polygon --> m1() m2()
Triangle --> m1() m2() m3()

Polygon p1 = new Triangle()   # 5L can <---- 2L water
    - Create object for sub class, and give reference to super class
    - creating our own methods in sub class ---> NO USE

p1.m1()  
p1.m2()
p1.m3()  # ERROR


'''