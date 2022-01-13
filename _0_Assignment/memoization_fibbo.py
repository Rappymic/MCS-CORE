def fibb(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        return 1
    else:
        memo[n] = fibb(n-1, memo) + fibb(n-2, memo)
        return memo[n]

def fiib1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fiib1(n-1) + fiib1(n-2)




print(fibb(998))
print(fiib1(10))