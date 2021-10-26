
print("------------- 1. capitalize() -----------------")

print("capitalize() : capitalizes first letter of given input string")

str1 = 'hello world'
print("Normal string           :", str1)

print(100)

x = 100
print(x)

300

print("------1 time usage-----------")
str1.capitalize()  # Hello world  returning the value
print("String after capitalize :", str1)
print("String after capitalize :", str1.capitalize())
print("-----------------------------------------------")

print("------Both strings usage-----------")
str1 = 'hello world'
print("String before capitalize :", str1)
str2 = str1.capitalize()
print("String after capitalize  :", str2)


str1 = 'hello world'
print("String before capitalize :", str1)
str1 = str1.capitalize()
print("String after capitalize  :", str1)


print(10)

# OR

x = 10
print(x)
print(x+20)
print(x+30)

print(10+20)
# OR
x = 10 + 20
print(x)
print("Value is : ", x)

def get(val):
    pass

get(x)


print("--------Return types------------")
'''
Here sum function is taking 2 responsibilities
    1. Implementing the business logic
    2. Handling the end result/output
'''
# Without return types
def sum(n1, n2):
    result = n1 + n2  # business logic
    print("Addition : ", result)  # responsibility

sum(100, 200)       # returns None
print("Function call  :", sum(100, 200)) # returns None

x = 10

output = sum(100, 200)
print("Function call : ", output)

# with return type
def sum(n1, n2):
    result = n1 + n2
    return result  # int float bool string list tuple dict set


sum(11, 22)   #  int float bool string list tuple dict set
10000
x = 10000

output = sum(25, 10)              # x = 10    print(x)
print("Addition1 is  :: ", output)

print("Addition2 is  :: ", sum(25, 10))  # print(10)

print("----Return type examples----")

list1 = [1, 2, 3, 4, 5]
print("Before append : ", list1)
list1.append(50)  # It will append 50 to list1 and returns nothing
print("Append 51 :", list1.append(100))

app = list1.append(200)
print("Append 54 :", app)

print("After append  : ", list1)

print("-----Pop operations-------")
list1 = [1, 2, 43, 65, 23, 46, 78, 29, 83, 23, 3, 4]
print(list1.pop())  # It will remove last element and returns the element to us
print("Removed values is :", list1.pop())
print("LIST : ", list1)

val = list1.pop(5)
print("Values is :", val)
print(val)
print()
print("Removed value is : ", val)

print("Remove func :", list1.remove(65))

print("Index is : ", list1.index(29))

