str1 = 'ablhP09'
#
'''At least one numeric digit
At Least one Small/Lowercase Letter
At Least one Capital/Uppercase Letter
Must not have space 
Must not have slash (/)
At least 6 characters'''
con_list = []
if len(str1) < 6:
    con_list.append(0)

def number_check(st):
    for i in st:
        if str(i).isdigit():
            return 1
    else:
        return 0

def cap_check(st):
    for i in st:
        if str(i).isupper():
            return 1
    else:
        return 0

def lower_check(st):
    for i in st:
        if str(i).islower():
            return 1
    else:
        return 0

def spac_check(st):
    for i in st:
        if i == '/' or i == ' ':
            return 0
    else:
        return 1

if number_check(str1) == 1 and cap_check(str1) == 1 and lower_check(str1) == 1 and spac_check(str1) == 1:
    con_list.append(1)
else:
    con_list.append(0)

if 0 in con_list:
    print("Invalid Password")
else:
    print('Valid password')

