test_str = 'banana'
# res = [test_str[i: j] for i in range(len(test_str)) for j in range(i+1, len(
res = []
for i in range(len(test_str)):
    j = len(test_str)
    while j > i:
        res.append(test_str[i:j])
        j -= 1

def pallindrome(str1):
    for i in range(1, len(str1) + 1):
        if str1[i - 1] != str1[i * -1]:
            return False
    else:
        return True
print(res)
# result = [pallindrome(i) for i in res]
for index, value in enumerate([pallindrome(i) for i in res]):
    if value == True:
        print(res[index])