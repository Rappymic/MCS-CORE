
# REQ: Find square of given value

# 1mark : Find square of given value 5
print("Square of value : ", 5*5)
# 2 mark : Find square of given value 5
val = 5
print("Square of value : ", val*val)

# 5 marks : Find square of given value 5
val = int(input("Enter value : "))

def find_square(num):
    return num*num
    '''
    sq_val = num * num
    return sq_val
    '''
sq_val = find_square(val)
print("Square of value : ", sq_val)

'''
Syntax: lambda arguments: expression
'''
in_no = input("Enter value to hanlde mult :: ")
vals = in_no.split('-')
print(vals)

sq_val = lambda num: num * num
in_no = int(input("Enter value for lambda :: "))
print("Lambda  : Square of value : ", sq_val(in_no))

sq_val = lambda x,y: x*y
print("Lambda  : Square of value : ", sq_val(10,20))


# Covert to function
def sq_val(num):
    return num*num

print("Function : Square of value : ", sq_val(5))

# Use lambda functions  ==> map filter reduce
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

# map:

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print("Using map: ", final_list)


# filter:
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

def filter_list(li1):
    li2 = []
    for val in li1:
        if val%2 == 0:
            li2.append(val)
    return li2
print("Even numbers1: ", filter_list(li))


print("Even numbers2: ", list(filter(lambda x: (x % 2 == 0), li)))

ev_list = list(filter(lambda x: (x % 2 == 0), li))
print("Even numbers3: ", ev_list)


# reduce:

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print("Reduce data ", sum)


