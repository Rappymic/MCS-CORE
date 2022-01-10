from itertools import combinations
n_rows = int(input('Enter N: '))
m_column = int(input('Enter M: '))
k = int(input('Enter K: '))

n = [i for i in range(n_rows)]
m = [i for i in range(m_column)]

li = []
for i in range(1, k+1):
    a = combinations(m ,i)
    for j in a:
        li.append(j)

scientific_notation='%.2E' % (len(li)*n_rows)
print(scientific_notation)