list1 = [1, 2, 3, 4]
print("original list".ljust(80, "-"), list1, "\n")
print("id before replacement".ljust(80, "-"), id(list1), "\n")
print("id of element at index 2".ljust(80, "-"), id(list1[2]), "\n")
x = id(list1)
y = id(list1[2])
list1[2] = 23
print("modified list".ljust(80, "-"), list1, "\n")
print("id after replacement".ljust(80, "-"), id(list1), "\n")
print("id after replacement of element at 2".ljust(80, "-"), (id(list1[2])),
      "\n")
print(f"is the id of list {list1} is same after replacement".ljust(80, "-"),
      x == id(list1), "\n")
print(f"is the id of element is same after replacement".ljust(80, "-"),
      y == id(list1), "\n")

string1 = "This is a normal argument"
x = id(string1)
print(f"id of '{string1}'".ljust(80, "-"),id(string1), "\n")

string1 = string1 + "s"

print(f"id of '{string1}' after editing".ljust(80, "-"), id(string1), "\n")
print(f"is the id of '{string1}' has changed".ljust(80, "-"), x != id(string1), "\n")

l1 = [7,8,9,list1]
print("Another list".ljust(80, "-"), l1, "\n")
x = id(l1)
y = id(l1[3])
z = id(l1[3][2])
print(f"id of {l1} before operation".ljust(80, "-"),x, "\n")
print(f"id of list inside {l1}".ljust(80, "-"), y,"\n")
print(f"id of element in nested list".ljust(80, "-"), z, "\n")

l1[3][2] = 0

print(f"id of {l1} after operation".ljust(80, "-"),id(l1), "\n")
print(f"id of list inside {l1}".ljust(80, "-"), id(l1[3]),"\n")
print(f"id of element in nested list".ljust(80, "-"), id(l1[3][2]), "\n")

print(f"is the id of {l1} same after operation".ljust(80, "-"),
      x == id(l1), "\n")
print(f"is the id of {l1[3]} same after operation".ljust(80, "-"),
      y == id(l1[3]), "\n")
print(f"is the id of {l1[3][2]} same after operation".ljust(80, "-"),
      z == id(l1[3][2]), "\n")
