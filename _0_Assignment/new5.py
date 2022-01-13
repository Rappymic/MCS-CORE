from time import time
import sys
sys.setrecursionlimit(500000)
def grid_traveller(m, n):
    # first make a table
    output = [[0 for j in range(n+1)] for i in range(m+1)]
    output[1][1] = 1
    for i in range(len(output)):
        for j in range(len(output[i])):
            if j < n :
                output[i][j+1] += output[i][j]
            if i < m :
                output[i+1][j] += output[i][j]
    return output[m][n]

a = time()
print(a)
print(grid_traveller(500,100))
print('itertive time', time() -a)
def grid_travel(m, n, memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 1 or n == 1:
        return 1
    if m == 2 and n == 2:
        return 2
    sum = grid_travel(m, n-1, memo) + grid_travel(m-1, n, memo)
    memo[(m,n)] = sum
    return sum
b = time()
print(grid_travel(500,100))
print('recursion time', time() - b)


