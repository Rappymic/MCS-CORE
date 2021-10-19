list1 = [1,2,3,4,5,6,7,8]
print("---------------------------------------------")
print("Original List                :", list1)
print("Sliced list                  :", list1[1:4])
print("Sliced List with steps       :", list1[::2])
print("Reversed list with slicing   :", list1[::-1])
print("Reversed list with steps     :", list1[::-2])
print("---------------------------------------------")
list1 = [1, 2, 3, 4, [5, 6, 7], (8, 9, 10)]

print("Original List                :", list1)
print("Sliced list                  :", list1[1:4])
print("Sliced List with steps       :", list1[::2])
print("Reversed list with slicing   :", list1[::-1])
print("Reversed list with steps     :", list1[::-2])

print("---------------------------------------------")


print("list element with index      :", list1[3])

print("Unmodified List              :", list1)
list1[3] = "RTR"
print(f"List element of index 3 is replaced")
print("Final list                   :", list1)

print("---------------------------------------------")
list1 = [1, 2, 3, 4, 5]
list2 = [10,11,12,13]
print(f"Addition of {list1} and {list2}")
print(list1+list2)
