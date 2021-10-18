"""First 10 natural no."""
print("The first 10 natural Number are: ")
for i in range(1, 11):
    print(i, end=" ")
print("\n----------------------")

"First 10 even No."
print("First 10 prime No.")
i = 1
count = 0
while True:
    if i % 2 == 0:
        print(i, end=" ")
        count += 1
    if count == 10:
        break
    i += 1
print("\n----------------------")

"""First 10 odd no"""
print("First 10 odd No.: ")
a = 1
i = 0
while a <= 10:
    i += 1
    if i % 2 != 0:
        print(i, end=" ")
        a += 1
print("\n----------------------")

"""First 10 even no in reverse order"""
print("First 10 even no in reverse order: ")
a = 0
list_num = []


def even_num(value):
    if value % 2 == 0:
        return value


count = 1
while count <= 10:
    a += 1
    if even_num(a) is not None:
        list_num.append(even_num(a))
        count += 1

list_num.sort(reverse=True)
for i in list_num:
    print(i, end=" ")
print("\n----------------------")

"""Print Table of number given by the user"""


def print_table(value, length):
    for test_num in range(1, length + 1):
        print(f"{value} X {test_num} = {value * test_num}")


a = 3
b = 10
print(f"The Table of {a} upto {b} is ")
print_table(a, b)
print("----------------------")

"""Product of digits"""
input_str = 24  # if input is used type cast to integer
print(f"The product of digits in {input_str} is: ")


def digit_product(value):
    result_ = 1
    while value != 0:  # until value reaches zero
        result_ = result_ * (value % 10)  # splitting and multiplying
        value //= 10
    return result_


print(digit_product(input_str))
print("----------------------")

"""Factorial"""

num_1 = 7  # if input is used type cast to integer
print(f"the factorial of {num_1} is :", end=" ")


def factorial(value):
    if value == 1:
        return 1
    else:
        return value * factorial(value - 1)


print(factorial(num_1))
print("----------------------")

"""Sum of all numbers in digit"""

digit = 123789
print(f"Sum of digit of number {digit} is : ")


def sum_digit(value):
    result_ = 0
    while value != 0:
        result_ = result_ + (value % 10)
        value //= 10
    return result_


print(sum_digit(digit))
print("----------------------")

"""Check for prime No."""
a = 21


def prime_check(value):
    if value == 2 or value == 3 or value == 1:
        return True

    for t in range(2, value // 2 + 1):
        if value % t == 0:
            return False
    else:
        return True


print(f"Is No. {a} a prime No.: ")
print(prime_check(a))
print("----------------------")

"""Pattern
1
1 2
1 2 3
1 2 3 4

"""
for i in range(1, 5):
    if i > 1:
        print("\n")
    for j in range(1, i + 1):
        print(j, end=" ")
print("\n----------------------")

"""Pattern
* * * *
* * *
* *
*
"""

max_stars = 4

for i in range(0, max_stars + 1):
    print((max_stars - i) * "* ")
print("----------------------")

"""Pattern
4 2 3 1
4 2 3
4 2
4 
"""

for i in range(1, 5):
    for j in range(0, 5 - i):
        print(4 - j, end=" ")
    print(" ")
print("----------------------")

"Accept 10 no and give their average"
list1 = [1, 2, 3]


# for i in range(0, 10):
#     list1.append(float(input(f"Enter the {i} No.: ")))


def average(value):
    sum_ = 0
    for index, _ in enumerate(value):
        sum_ = sum_ + value[index]
    return sum_ / len(value)


print(f"the average of {list1} is {average(list1)}")
print("----------------------")

"""Retrieve all prime between the given no"""

x = 1
y = 97
if 0 < x < y and y > 0:
    print(f"The prime nos between {x} and {y} is: ")
    for i in range(x, y + 1):
        if prime_check(i) is True:
            print(i, end=" ")
    print("\n----------------------")
else:
    print("Enter positive Numbers with second number larger than first")

"""Print the sum of even amd odd numbers"""


def sum_num(iterable):
    if iterable:
        result_ = 0
        for index, value in enumerate(iterable):
            result_ = result_ + iterable[index]
        return result_
    else:
        return "Invalid Numbers"


x = 12
y = 37
list_even = []
list_odd = []
if 0 < x < y:
    for i in range(x, y + 1):
        if even_num(i) is not None:
            list_even.append(i)
        else:
            list_odd.append(i)
if 0 < x < y:
    print(f"The sum of even nos between {x} and {y} is {sum_num(list_even)}")
    print(f"The sum of odd nos between {x} and {y} is {sum_num(list_odd)}")
else:
    print("Enter positive values in ascending order")
print("-------------------")

"""all the numbers which are divisible by 11 but not by 2 between 100 and 
    500."""

x = 100
y = 500
print(f"numbers which are divisible by 11 but not by 2 between 100 and 500")
if x > y:
    x, y = y, x
for i in range(x, y):
    if even_num(i) is None and i % 11 == 0:
        print(i, end=" ")
print("\n-------------------")

"""program to print numbers from 1 to 20 except multiple of 2 & 3"""
x = 1
y = 20
print("numbers from 1 to 20 except multiple of 2 & 3")
for i in range(x, y + 1):
    if i % 3 == 0 or i % 2 == 0:
        continue
    else:
        print(i, end=" ")
print("\n-------------------")

"""Decimal to Binary with loops"""
x = 45
print(f"binary of {x} is ")
z = 0
list3 = []
result = str()
while x > 0:
    z = x % 2
    list3.append(z)
    x //= 2
list3 = list3[::-1]
for item in list3:
    result += str(item)
result = int(result)
print(f"{result}")
print("-------------------")

"""Palindrome"""
x = 1221


def check_palindrome(x_):
    result_ = []
    x_ = str(x_)
    for i_, char in enumerate(x_):
        if x_[i_] == x_[-1 - i_]:
            result_.append(1)
        else:
            result_.append(2)
    for i_ in result_:
        if i_ != 1:
            return False
    else:
        return True


print(f"The No {x} is a palindrome: {check_palindrome(x)}")

