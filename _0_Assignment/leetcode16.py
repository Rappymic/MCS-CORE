from itertools import combinations_with_replacement as comb

s = 'happy'
lent = len(s)
list1 = [0,1]
a = comb(iterable=list1, r=lent)
paths = [i for i in a]

list_alp = [chr(i) for i in range(ord('A'), ord('Z')+1)]
final_list = []
for i in range(0,len(list_alp),6):
    final_list.append(list_alp[i:i+6])

dic1 = {}
for index, value in enumerate(final_list):
    for ind, val in enumerate(value):
        dic1[val] = [index, ind]

print(dic1)
def dis(tup1, lent):
    countF1 = 0
    countF2 = 0
    while countF1+countF2<=lent:
