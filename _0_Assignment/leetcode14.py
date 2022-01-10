str1 = '-2147483648'

str1 = str1.lstrip(' ')
b = 1
if str1[0] == '-':
    b = -1
    str1 = str1.lstrip('-')
    str1 = str1.lstrip('+')
str2 = ''
for i in str1:
    if i.isdecimal():
        str2+=i
    else:
        break

final_int = int(str2)*b
print(final_int)
if -2**31<=final_int<=2**31-1:
    print(final_int)
elif -2**31>final_int:
    print(-2**31)
else:
    print(2**31-1)
