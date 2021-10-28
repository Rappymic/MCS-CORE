"""
Object Oriented Programming System
"""

'''
Class/Object
------------------
Encapsulation
Abstraction
Inheritance
Polymorphism
'''

# REQUIREMENT : Find Sum of  given two numbers
'''
1. CRUD
2. STATE
3. BEHAVIOR

'''
# STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  # int(input("Enter number1"))
n2 = 20  # int(input("Enter number2"))

# BEHAVIOR   - Implementation       ==>  Functions
def get_sum(num1, num2):
    result = num1 + num2
    return result

print("Sum of 2 numbers is : ", get_sum(n1, n2))

'''if elif else 
   for while 
   functions 
   class 
   try except else finally 
   with
'''



# class structure
'''
class <class-name>:
        #1. STATE
    n1 = 10
    n2 = 20
    
        #2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result
'''

# REQ : Display each employee information   CRUD -> RETRIEVAL
'''
CRUD 
Data type/structures
STATE
BEHAVIOR
'''
# A1 :: Using Functions
print("---------Using Functions-----------")

    # 1. STATE
empid = 100  # int(input("Enter empid :"))
name = 'Madhu Nettem'  # input("Enter name : ")
sal = 15000  # float(input("Enter sal :"))

    # 2. BEHAVIOR
def get_einfo(eid, ename, esal):
    print("Employee details are ", eid, ename, esal)

get_einfo(empid, name, sal)

# Using OOPs  -- Class
# Step 1:
class Employee:
    # 1. STATE
    empid = 100  # int(input("Enter empid :"))
    name = 'Madhu Nettem'  # input("Enter name : ")
    sal = 15000  # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(eid, ename, esal):
        print("Employee details are ", eid, ename, esal)

print("---------Using OOPs-----------")

# Step 2:
class Employee:
    # 1. STATE
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal
    # 2. BEHAVIOR
    def get_einfo(self):
        print("Employee details are ", self.empid, self.name, self.sal)

# object creation
madhu = Employee(100, 'Madhu Nettem', 15000)    # x = 10
madhu.get_einfo()
print("--------------Student example in OOPs-----------------")

class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)

ali = Student(23, 'Ali Hussain', 65)
ali.get_sinfo()

print("--------------Product example in OOPs-----------------")

class Product:
    # STATE
    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price
    # BEHAVIOR
    def get_pinfo(self):
        print("Product details are : ", self.pid, self.pname, self.price)

tv = Product('SAM001', 'SAMSUNG 32 INC.', 25000)
tv.get_pinfo()

# 20 to 30 classes
