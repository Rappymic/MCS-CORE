'''
# Without EH
print("Start of program")
x = int(input("Enter numerator value :"))   # ValueError
y = int(input("Enter denominator value:"))  # ValueError
li = [1,2,3,4]
print(li[2])   # IndexError
print("Division :", x / y)  # ZeroDivisionError
print("Hello world")
print("---------------------------------")
'''
# Handling multiple exceptions
'''
HANDLING MULTIPLE EXCETIONS

To handle multiple exceptions,write mulitple except blocks
Below code is not proper 
'''
print("Start of program")
try:
    # print("----While Exception handling----")
    x = int(input("Enter numerator value :"))  # ValueError("invalid literal for int() with base 10: 'rewrew'")
    y = int(input("Enter denominator value:"))
    li = [5, 12, 23, 32]
    print("List val:", li[2])  # IndexError("list index out of range")
    print("Division :", x / y)  # ZeroDivisionError("division by zero")
    print("Hello world")
    print("---------------------------------")
except Exception as obj:  # Exception obj = ValueError()
    print("** Error occured :  ==> ", obj)
print("----REMAINING CODE-------")
# Always create object for sub class and give reference to super class
'''
Aniaml a = Tiger()
Employee emp = SoftEmployee()
Exception e = ValueError()
Exception e = KeyError()
Exception e = ZeroDivisionError()




'''