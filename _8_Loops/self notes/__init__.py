a = 0
n = int(input("Enter the no of first even digits you want to print: "))
run = True  # using for infinite loop and manually ending the loop
while run:
    if a % 2 == 0 and a != 0:  # checking no should not be zero and
        # divisible by 2
        print(a)

    if a == 2 * n:  # control statement till reach n
        run = False
    a += 1

"""first 10 digits and their squares"""

a = 1

while a <= 10:
    print(f"the no is {a} and its square is {a ** 2}")
    a += 1

"""Write for loop statement to print the following series:
10, 20, 30 … … 300"""

# increment is done by 10 at each step

a = 10
while a <= 300:
    print(a, end=" ")
    a += 10

"""Write a while loop statement to print the following series
105, 98, 91 ………7"""

# decrement is done by 7

a = 105

while a >= 7:
    print(a, end=" ")
    a -= 7

"""Write a program to print sum of first 10 Even numbers"""
a, b = 0, 0
n = 10
run = True  # using for infinite loop and manually ending the loop
while run:
    if a % 2 == 0 and a != 0:  # checking no should not be zero and
        # divisible by 2
        b += a
    if a == 2 * n:  # control statement till reach n
        run = False
        print(f"the sum is {b}")
    a += 1

"""Write a program to print table of a number entered from the user."""

table_num = int(input("Enter the no whose table is to be printed: "))
a = 1
while a <= 10:
    print(f"{table_num} X {a} = {table_num * a}")
    a += 1

"""Q9. Write a program to find the sum of all even numbers that falls between
two numbers (exclusive both numbers) entered from the user using while loop."""

first_num = int(input("Enter the initial Value: "))
sec_num = int(input("Enter the last Value: "))
sum_ = 0
while first_num < sec_num - 1:
    first_num += 1
    if first_num % 2 == 0:
        sum_ += first_num
if sum_ == 0:
    print("There are no prime no between the limit")
else:
    print(sum_)

"""Write a program to reverse the number accepted from user using while 
loop"""
a = 0
b = 0
num = int(input("Enter the Number: "))
while num != 0:
    a = num % 10
    b = b * 10 + a
    num //= 10
print(b)

