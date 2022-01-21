def longestPalindrome( test_str: str) -> str:
    res = []
    for i in range(len(test_str)):
        j = len(test_str)
        while j > i:
            res.append(test_str[i:j])
            j -= 1
    res = sorted(res, key=lambda x: len(x), reverse=True)

    def pallindrome(str1):
        lent = len(str1)
        le = lent // 2
        if str1[:le:-1] == str1[lent - le:]:
            return True
        else:
            return False

    result = [pallindrome(i) for i in res]
    for index, value in enumerate(result):
        if value == True:
            return (res[index])

print(longestPalindrome("babad"))