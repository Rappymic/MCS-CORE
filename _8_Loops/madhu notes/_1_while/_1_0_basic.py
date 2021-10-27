# I REQ. Gathering : Print numbers from 100 to 200

# Code duplication,we can't extend when requirement changes
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# 1 to 10  - 1 2 ... 10

#print numbers from 1 to 5
'''
while <condition>:
    <statements body> 
'''
print("--------------")
x = 1
while x <= 10:
    print(x)
    x = x + 1   # Assignment operator += -=   x += 1
print("End of program")
'''
1. Data initialization     x = 1
2. Condition verification  while x <= 5
3. Business logic          print(x)
4. Data operation          x = x + 1
'''

print("--------------")



'''
# II - ANALYSIS
        1. Functional analysis : We need to print the numbers between starting and 
                                 ending number given by customer
        2. Technical analysis  : STATE    :  input: st_num end_num (int)
                                 BEHAVIOR :  Loops : while  
III.  Design : NA
'''
# IV. DEVELOPMENT
    #STATE
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
    #BEHAVIOR
while num1 <= num2:
    print(num1)
    num1 += 1
print("***** End of program *****")

# V. TESTING validation is missing

num1 = 500
num2 = 100
if num1 <= num2:
    while num1 <= num2:
        print(num1)
        num1 += 1
else:
    print("### num1 should be less than num2  ###")
print("***** End of program *****")









