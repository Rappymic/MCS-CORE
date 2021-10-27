list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 12.5, 12]
print("\n")
print("Addition".center(40, "-"))
print(f"list1 is {list1}\nlist2 is {list2}")
print(f"Addition is {list1 + list2}\n")

print("Multiplication with a Number".center(40, "-"))
print(f"{list1} X 3 :\n", list1 * 3)
print("Membership".center(40, "-"))
print(f"is 3 in {list1}:", 3 in list1)
print(f"is 9 in {list1}:", 9 in list1)

print("Membership with slicing".center(40, "-"))
print(f"is 1 in {list1} from index 2:", 1 in list1[2:])
list3 = list1[:]

print("Appending list inside a list".center(40, "-"))
print(f"appending {list3} and {list2}")
list3.append(list2)

print(list3)

print("Length of a list".center(40, "-"))
print(f"the length of {list3} is : ",len(list3))
print("Max value of the List".center(40, "-"))
print(f"Max value inside {list2} is :", max(list2))
print("Min value of the List".center(40, "-"))
print(f"Min value inside {list2} is :", min(list2))