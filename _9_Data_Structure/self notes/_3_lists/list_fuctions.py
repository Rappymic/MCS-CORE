print("Append Operation".center(80, "-"))
l1 = [1,2,3,4]
x = id(l1)

print("original list and its id".ljust(40, "-"), l1, x)
l1.append(5)
y = id(l1)
print("modified list and its id".ljust(40, "-"), l1, y)
print("is the id same".ljust(40, "-"),x==y, "\n")

print("Insert operation".center(80, "-"))
print("list and its id".ljust(40, "-"), l1, id(l1))
l1.insert(2, 90)
print("list and its id".ljust(40, "-"), l1, id(l1))
