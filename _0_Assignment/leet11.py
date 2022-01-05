def countAndSay( n: int) -> str:
    if n == 1:
        return '1'
    varA = [i for i in countAndSay(n-1)]
    dic1 = {}
    for i in varA:
        if i not in dic1:
            dic1[i] = varA.count(i)
    lis1 = []
    for i in dic1:
        a = str(dic1[i]) + i
        lis1.append(a)
    print(lis1)
    return ''.join(lis1)


print(countAndSay(n = 5))
