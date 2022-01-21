from itertools import combinations

str1 = 'hello'
str1 = str1.replace(' ','')
str1 = str1.casefold()
vowels = ('a','e','i','o','u')
list1 = [i for i in str1]
def sum_dict(dic1):
    a = 0
    for key, value in dic1.items():
        a += value
    return a

def str_count(sub_str, str1):
    count = 0
    while str1.find(sub_str) != -1:
        a = str1.find(sub_str)
        str1 = str1.replace(str1[a], '@', 1)
        count += 1
    return count

def comb_gener(li, n):
    a = combinations(li,n)
    list2 = [i for i in a]
    return list2

temp_list = []

for i in range(1, len(list1)+1):
    temp_list.extend(comb_gener(list1, i))
# print(temp_list)
final_list = [''.join(i) for i in temp_list]
# print(final_list)
final_list_update = []
for i in final_list:
    if i in str1:
        final_list_update.append(i)

vowel_list = [i for i in final_list_update if i[0] in vowels]
consonent_list = [i for i in final_list_update if i[0] not in vowels]


vowel_dict = {}
consonent_dict = {}

for i in vowel_list:
    vowel_dict[i] = str_count(sub_str=i, str1=str1)
for i in consonent_list:
    consonent_dict[i] = str_count(sub_str=i, str1=str1)

# for i in final_list_update:
#     if i[0] in vowels:
#         if i in vowel_dict.keys():
#             vowel_dict[i] = vowel_dict[i] + 1
#         else:
#             vowel_dict[i] = 1
#     else:
#         if i in consonent_dict.keys():
#             consonent_dict[i] = consonent_dict[i]+ 1
#         else:
#             consonent_dict[i] = 1
print(vowel_dict, sum_dict(vowel_dict))
print(consonent_dict, sum_dict(consonent_dict))
