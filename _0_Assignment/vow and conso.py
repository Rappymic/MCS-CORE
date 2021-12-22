from itertools import combinations
def gen_comb(li, r):
    list3 = []
    a = combinations(li, r=r)
    for i in a:
        b = ''.join(i)
        list3.append(b)
    return list3
str1 = 'kartik'
str1 = str1.casefold()

vowel = ['a', 'e', 'i', 'o', 'u']


list1 = [i for i in str1]
list5 = []
for i in range(1,len(list1)+1):
    a = gen_comb(list1, i)
    list5.extend(a)
list6 = []
for i in list5:
    if i in str1:
        list6.append(i)

# print(list6)

groupA = []
groupB = []

for e in list6:
    for i in vowel:
        if len(e) != 1:
            if e.startswith(i):
                groupA.append(e)

for i in list6:
    if i not in groupA and len(i) != 1:
        groupB.append(i)
# print('Group A',groupA)
# print('Group B',groupB)

dictA = {}
for i in groupA:
    if i not in dictA:
        dictA[i] = 1
    else:
        dictA[i] = dictA[i] + 1
dictB = {}
for i in groupB:
    if i not in dictB:
        dictB[i] = 1
    else:
        dictB[i] = dictB[i] + 1

print(dictA)
print(dictB)

if len(groupA)>len(groupB):
    print('Vowels has more strings by ', len(groupA)-len(groupB))
else:
    print('Consonants have more strings by ',len(groupB)-len(groupA))