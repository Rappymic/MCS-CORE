from math import comb

n = 5
m = 4

k = 2

def total_comb(row, col, c):
    sum1 = 0
    for i in range(1, c+1):
        sum1 += comb(row, i)
    return sum1*col

print('{:e}'.format(total_comb(row=n, col=m, c=k)))