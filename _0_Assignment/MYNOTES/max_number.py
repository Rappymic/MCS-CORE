list1= []
inin = 0
while inin <5:
        num = float(input("Enter the num: "))
        list1.append(num)
        inin += 1
result = 0
for i in range(len(list1)-1):
    if list1[i] > list1[i+1]:
        result = list1[i]
    else:
        result = list1[i+1]

print("The largest value is :", result)