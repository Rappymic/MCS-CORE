from time import time
import sys
from memory_profiler import memory_usage
sys.setrecursionlimit(500000)

def grid_traveller(m, n):
    # first make a table
    output = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    output[1][1] = 1
    for i in range(len(output)):
        for j in range(len(output[i])):
            if j < n:
                output[i][j + 1] += output[i][j]
            if i < m:
                output[i + 1][j] += output[i][j]
    return output[m][n]


def grid_travel(m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 1 or n == 1:
        return 1
    if m == 2 and n == 2:
        return 2
    sum1 = grid_travel(m, n - 1, memo) + grid_travel(m - 1, n, memo)
    memo[(m, n)] = sum1
    return sum1


b = time()
print(grid_travel(800, 500))
print('recursion time', time() - b)

a = time()
print(grid_traveller(800, 500))
print('itertive time', time() - a)
