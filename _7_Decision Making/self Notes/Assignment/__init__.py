list1 = [1, 34, 646, 5677, 5, 567, 565, 777, 8, 88888888, 9767, 5454, 6767, 44
    , 66, 6]
x = list1[0]
for i in range(0, len(list1) - 1):
    if x < list1[i + 1]:
        x = list1[i + 1]

print(x)

var = dir()
var1 = [i for i in var if not i.startswith("__")]
print(var1)

if 3 == 2:
    print("exceuted")

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

num = int(input("enter number: "))
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

print("Select your ride:")
print("1. Bike")
print("2. Car")
print("3. SUV")

choice = int(input())

if choice == 1:
    print("You have selected Bike")
elif choice == 2:
    print("You have selected Car")
elif choice == 3:
    print("You have selected SUV")
else:
    print("Wrong choice!")

num1 = int(input())
num2 = int(input())

if num1 >= num2:
    if num1 == num2:
        print(f'{num1} and {num2} are equal')
    else:
        print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is smaller than {num2}')
