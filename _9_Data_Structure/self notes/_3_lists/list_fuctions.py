print("Append Operation".center(80, "-"))
l1 = [1, 2, 3, 4]
x = id(l1)
print("\n")
print("original list and its id".ljust(40, "-"), l1, x)
l1.append(5)
y = id(l1)
print("modified list and its id".ljust(40, "-"), l1, y)
print("is the id same".ljust(40, "-"), x == y, "\n")

print("Insert operation".center(80, "-"))
print("\n")
print("list and its id".ljust(40, "-"), l1, id(l1))
l1.insert(2, 90)
print("list and its id".ljust(40, "-"), l1, id(l1))
print("\n")
print("Sorting Reverse".center(80, "-"))
print("\n")
print("original list".ljust(40, "-"), l1)
l1.sort(reverse=True)
print("reversed list".ljust(40, "-"), l1)
print("original list".ljust(40, "-"), l1)
print("\n")
print("Sorted Function".center(80, "-"))
print("\n")
print("original list".ljust(40, "-"), l1)
l2 = sorted(l1)
print("sorted list".ljust(40, "-"), l2)
print("original list".ljust(40, "-"), l1)
print("\n")
print("shallow copy".center(80, "-"))
print("\n")
new_list = [1, 2, 3, [4, 5, 6, 7]]
copied_list = new_list.copy()
print("Original List".ljust(40, "-"), new_list)
print("copied list".ljust(40, "-"), copied_list)
print("element [3][2] is being modified")
new_list[3][2] = "mdr"
print("Original List".ljust(40, "-"), new_list)
print("copied list".ljust(40, "-"), copied_list)

from copy import deepcopy
print("\n")
print("Deep Copy".center(80, "-"))
print("\n")
new_list = [1, 2, 3, [4, 5, 6, 7]]
copied_list = deepcopy(new_list)
print("Original List".ljust(40, "-"), new_list)
print("copied list".ljust(40, "-"), copied_list)
print("element [3][2] is being modified")
new_list[3][2] = "mdr"
print("Original List".ljust(40, "-"), new_list)
print("copied list".ljust(40, "-"), copied_list)
