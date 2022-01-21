dic1 = {}
def tribo(n):
    if n in dic1:
        return dic1[n]
    if n < 2:
        return n
    elif n == 2:
        return 1
    else:
        a = tribo(n-1) + tribo(n-2) - tribo(n-3)
        dic1[n] = a
        return a