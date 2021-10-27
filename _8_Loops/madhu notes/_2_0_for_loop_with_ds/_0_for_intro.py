# Data types
x = 10   # integer
x = 10.5  # float
x = True   # boolean
msg = 'Hello World'  # string

# Data structures
msg = 'Hello World'         # string
list1 = [1, 2, 3, 4, 5]     # list
tup1 = (1, 2, 3, 4, 5)      # tuple
dict1 = {1: 1, 2: 2, 3: 3}  # dictionary
set1 = {1, 2, 3, 4, 5, 6}   # set

# while
i = 10
while i <= 10:
    print(i)
    i += 1


# for loop
'''
# Maths  :  collection of elements   : set   sequence    matrix
# Python :  sequence in python       : string list tuple  range   
                                       <bytearrays, buffers>

for <var> in <sequence>:
    # perform business logic
'''
print("--------For loop with String-------")
# Print each character of string
course = 'PYTHON PROGRAMMING'
for char in course:  # char = 'P'
    print(char)
print("----------End-----------------------")
print(10)

x = 10
print(x)

msg = 'Python world'
for element in msg:
    print("Character : ", element)
# further business logic

# String with for loop
for char in 'Welcome to Python':
    print("Char : ", char)

for char in 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@':
    print("Char : ", char)

# List with for loop
for val in [1, 2.5, True, 'Madhu', 5.0, False, 7]:
    print("List data :", val)

for val in [1, 2, 3, 4, 5, 6, 7]:
    print("List data :", val)

# Tuple with for loop
for val in (1, 2, 3, 4, 5, 6, 7):
    print("Tuple data :", val)
print("----------------------------")
# Dictionary with for loops
e_data = {'eid': 100, 'name': 'Madhu Nettem', 'sal': 10000}
for val in e_data:
    print("Dict data :", val)
print("--------------------------------")
for key in e_data.keys():
    print("Dict key :", key)
print("--------------------------------")
for val in e_data.values():
    print("Dict val :", val)
print("--------------SET---------------------")
# set with for loop
set1 = {1, 2, 3, 4, 5, 6}
for val in set1:
    print("Set value : ", val)

# Decimal number   0 to 255 1 byte
'''
    
    -----------------------
    -----------------------
    7  6  5  4  3  2  1  0

0 to 255 -  ASCII TABLE    A 65  a 97
367  ---     10000001 
'''