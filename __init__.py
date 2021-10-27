list1 = [1, 2, 3, 'worse', 56, 78, 45, 342, 'good', 'bad']
temp_list_int = []
temp_list_string = []
for i in list1:
    if type(i) == int:
        temp_list_int.append(i)
    else:
        temp_list_string.append(i)

final_list = temp_list_string + temp_list_int
print(final_list)


string1 = "abc"
string2 = "defg"
# output = adbecfg
string3 = string1[0] +string2[0] + string1[1] + string2[1:]
print(string3)
# for item in list1:
#     # print(item)
#     if type(item) == int and item > 10:
#         print(item)

# while True:
#     i = int(input("Enter a no.: "))
#     if i <100:
#         continue
#     else:
#         print("You successfully enter the no larger than 100: ")
#         break
#
# list1 = [1, 2, 3, 56, 78, 45, 342, 'good', 'bad']
# for item, lola in enumerate(list1):
#     print("The stored item in the list at index", lola, "is", item)
