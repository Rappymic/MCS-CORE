def count_char(char, strng):
    return strng.count(char)


str1 = "abc"
str2 = "defg"
print(str1 + str2)

str1 = "karnatajjdjdhasiregqeugrka"
for x in [chr(i) for i in range(ord('a'), ord('z'))]:
    if count_char(x, str1) != 0:
        print(f"The character {x} in {str1} is ", count_char(x, str1))

l1 = []
for i in str1:
    if i not in l1:
        l1.append(i)
l1.sort()
for i in l1:
    if l1.count(i) != 0:
        print(f"the char {i} in {str1} is repeated ", str1.count(i))

dict1 = {'a': 99, b'': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
l2 = []
for value in dict1.values():
    l2.append(value)

l2.sort(reverse=True)

print(f"the largest 3 values in {dict1} are:")
for i in l2[:3]:
    print(i)
