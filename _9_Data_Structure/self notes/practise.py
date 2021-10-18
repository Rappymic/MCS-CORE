"""String Operations"""

str1 = "A smartphone is a portable device that combines mobile telephone and " \
       "computing functions into one unit. "
print("The original string:\n", str1)
print("__________________")
print("Is the given string is in title case: \n", str1.istitle())
str2 = str1.title()
print("__________________")
print("After title operation: \n", str2)
print("__________________")
str2 = str2.casefold()
print("After case fold operation:\n", str2)
str2 = str2.upper()
print("__________________")
print("Upper casing the entire string:\n", str2)
print("__________________")
print("Slicing the string and printing it at the center:\n")
str1 = str2[0:12]
print(str1.center(20, "-"))
print("__________________")

print("The star pattern using center and multiplication operation")
for i in range(6):
    x = ' x ' * i
    print(x.center(24))
for i in range(1, 5):
    x = " x " * (5 - i)
    print(x.center(24))
print("__________________")
str2 = str2.capitalize()  # original string was in sentence case
print("Original String \n", str2)
print("__________________")
print("Find operation")
print('Getting the index of "that" in the string')
print(str2.find("that"))
print("__________________")

print('Getting the index of "That" in the string')
print(str2.find("That"))  # title case That doesn't exist that does
print('"That" doesn\'t exist')
print("__________________")

print("Finding the index of a with slicing of all cases")
print(str2.casefold().find("a"))
print("__________________")
print("find index of a in the string")
print(str2.find("a"))
print("__________________")
str3 = "This is a normal argument"
str4 = "**"
print(f"join operation b/w '{str3}' and '{str4}' ")
print(str3.join(str4))

print("__________________")
print(f"the length of string '{str3}' is : ", len(str3))

print("__________________")

print(f"split function on '{str3}'\n", str3.split(" "))
print(f"split function on with max split of 2 '{str3}'\n",
      str3.split(" ", maxsplit=2))
print("__________________")

print("Original string:", str3)

print("__________________")
print("String replacement with case fold to match all possible cases")

str4 = str3.casefold().replace("this", "that")
print('Here "this" is replaced with "that"\n', str4)

print("__________________")