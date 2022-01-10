from itertools import combinations_with_replacement as comp
dic = {'3060Ti': 73000, '3070Ti': 92000, '3070': 82000, '2060':50199,
       '3060':59000}
l1 = [i for i in dic.keys()]
print(l1)
max = 600000

max_pos = max//50199
min_pos = max//92000
l4 = []
for i in range(min_pos, max_pos+1):
    a = comp(l1, r= i)
    for j in a:
        l4.append(j)

print(l4)

def sum_val(l5):
    sum = 0
    for i in l5:
        sum += dic[i]
    return sum

l7 = []

for index, value in enumerate(l4):
    if sum_val(value) < max:
        l7.append(index)

print(l7)
l8 = []

dic2 = {'3060Ti': 27, '3070Ti': 39.5, '3070': 27.60, '2060': 18, '3060':22}

for i in l7:
    l8.append(l4[i])

print(l8)
def sum_val1(l5):
    sum = 0
    for i in l5:
        sum += dic2[i]
    return sum

l9 = sorted(l8, key=sum_val1, reverse=True)

print(l9)

l10 = []

for i in l9:
    l10.append([i, sum_val1(i), sum_val(i)])

print(l10)
dic4 = {}
def dic_par(li):
    tsmp_set = set(li[0])
    dic5 ={}
    for i in tsmp_set:
        dic5[i] = list(li[0]).count(i)
    return dic5



l11 = [[dic_par(i), i[1],i[2]] for i in l10[:3]]
print(l11[:3])

