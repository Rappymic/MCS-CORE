list1 = [i for i in range(1,101)]

print(list1)

li1 = []

for i in range(0, len(list1),5):
    j = i+5
    li1.append(list1[i:j])

print(li1)