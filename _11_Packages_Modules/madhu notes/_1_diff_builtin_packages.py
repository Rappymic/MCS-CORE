'''

builtins.py
# STATE  : builtin data types  -- classes in
#             numbers (int float  complex)
#             string list tuple dict set

# Behavior : functions id() input() len() max() min()
#                      print()  type()
#                      int() float() long() str() list() tuple() dict() set()
'''
list1 = list([1, 2, 3, 4])
print(list1, type(list1), id(list1))
x = 10
list1.append(10)
print(list1, type(list1), id(list1))

# Generate a random number between 1 to 100

from random import randint
print("Random number : ", randint(1, 100))

# Function definition exists in random.py module
# randint(1,100) : function call