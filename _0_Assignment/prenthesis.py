from itertools import permutations
str1 = '()'
n = int(input("Enter the number: "))
str2 = str1*n

li1 = [i for i in str2]

list2 = permutations(li1)
list3 = []
for i in list2:
    a = "".join(i)
    list3.append(a)
li4 = []
for i in list3:
    if i not in li4:
        li4.append(i)
li5 = []
for value in (li4):
    if value.startswith(')') or value.endswith('('):
        pass
    else:
        li5.append(value)

print(li5)
