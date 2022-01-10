s = 'abdabsdhiabfiy'
li = []
for i in range(len(s)+1):
    for j in range(i+1, len(s) +1):
            a = s[i:j]
            li.append(a)
print(li)
li = set(li)
def check_padd(str1):
    for i in range(1, len(str1)+1):
        if str1[i-1] != str1[-i]:
            return False
    else:
        return True
print(li)
l1 = [check_padd(i) for i in li]
print(l1.count(True))