import sys
import time

sys.setrecursionlimit(100000)

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

def fib(n):
    a = 0
    b = 1
    c = 1
    for i in range(n+1):
        c = b
        b += a
        a = c
    return b






a = time.time()
print(fibb(9000))
print(time.time() - a)
b = time.time()
print(fib(8999))
print(time.time() - b)