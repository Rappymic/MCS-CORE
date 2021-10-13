# list1 = [1, 34, 646, 5677, 5, 567, 565, 777, 8, 88888888, 9767, 5454, 6767, 44
#     , 66, 6]
# x = list1[0]
# for i in range(0, len(list1) - 1):
#     if x < list1[i + 1]:
#         x = list1[i + 1]
#
# print(x)
#
# var = dir()
# var1 = [i for i in var if not i.startswith("__")]
# print(var1)
#
# if 3 == 2:
#     print("exceuted")
#
# num = 3
# if num > 0:
#     print(num, "is a positive number.")
# print("This is always printed.")
#
# num = -1
# if num > 0:
#     print(num, "is a positive number.")
# print("This is also always printed.")
#
# num = int(input("enter number: "))
# if num >= 0:
#     print("Positive or Zero")
# else:
#     print("Negative number")
#
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")
#
# num = float(input("Enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")
#
# print("Select your ride:")
# print("1. Bike")
# print("2. Car")
# print("3. SUV")
#
# choice = int(input())
#
# if choice == 1:
#     print("You have selected Bike")
# elif choice == 2:
#     print("You have selected Car")
# elif choice == 3:
#     print("You have selected SUV")
# else:
#     print("Wrong choice!")
#
# num1 = int(input())
# num2 = int(input())
#
# if num1 >= num2:
#     if num1 == num2:
#         print(f'{num1} and {num2} are equal')
#     else:
#         print(f'{num1} is greater than {num2}')
# else:
#     print(f'{num1} is smaller than {num2}')
#

# num = input("Enter the no:")
#
# num_list = []
# for i in range(0,len(num)):
#     num_list.append(num[i])
# print(num_list)

"""Write an if statement that asks for the user's name via input() function.
If the name is "Bond" make it print "Welcome on board 007." Otherwise make it
print "Good morning NAME". (Replace Name with user's name)"""

# name = input("Enter your Name: ")
#
# if name.casefold() == "Bond".casefold():
#     print("Welcome on board 007")
# else:
#     print(f"Good Morning {name.title()}")

"""Write a function named "thedecimal" which returns the decimal part of a 
number. If decimal part is zero function should return this string: "INTEGER"."""

# num = float(input("Enter the Number "))
# diff = (float(num)-int(num))
# if num == int(num):
#     print("You have entered an Integer")
# else:
#     print(f"The Decimal part is {round(diff,2)}")

"""treepersqkm is a dictionary showing the tree number of countries per square 
kilometer for random countries with sizeable population numbers. Write a function
 named "moretrees" that returns a list of country names with more than 20.000 
 trees per square kilometer."""

treepersqkm = {"Finland": 90652, "Taiwan": 69593, "Japan": 49894, "Russia": 41396,
               "Brazil": 39542, "Canada": 36388, "Bulgaria": 24987, "France": 24436,
               "Greece": 24323, "United States": 23513, "Turkey": 11126, "India": 11109,
               "Denmark": 6129, "Syria": 534, "Saudi Arabia": 1}
#Type your answer here.

list_20treepersqm = []

for country, trees in treepersqkm.items():
    if trees>20:
        list_20treepersqm.append(country)
print(list_20treepersqm)

"""counts the number of words that contain the letter: "l" in a given string."""
str = "Oranges and lemons, Say the bells of St. Clement's. You owe me three " \
      "farthings, Say the bells of St. Martin's "
a = str.count("l")
b = 0
for l in range(len(str)):
    if str[l] == "l":
        b+=1
print(a)
print(b)

"""the number of words that start with letter "A" in a string. 
(Make sure it counts lower case a's as well.)"""
a = str.casefold().count(" a") # will not work if string starts with a

print(a)
count = 0
for i in range(1,len(str.rstrip())):
    if str[0].casefold() == "a":
        count+=1
        str[0] = "b"
    if str[i] == " ":
        if str[i+1].casefold() == "a":
            count+=1
print(count)
