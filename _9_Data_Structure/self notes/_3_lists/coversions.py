str1 = "This is a normal argument"
list1=[]
print("type casting the string into list".center(40, "-"))
print("Original string: ",str1)
print(list(str1))
print("List to string using loop".center(40, "-"))
list1 = list(str1)
print(list1)
str2 = str()
for element in list1:
    str2 = str2+str(element)

print("After conversion")
print(str2)

print("List conversion to string".center(40, "-"))
print("original list\n", list1)
str2 = "".join(list1)
print("Converted to string\n", str2)
print("-".center(40, "-"))
print("Type of all Data types used".center(40, "-"))
print(f"Datatype of String {str2} is :", type(str2))
print(f"Datatype of list {list1} is :", type(list1))
