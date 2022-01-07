k = int(input("Divisor :"))
def check(k):
    n_str = 1
    while len(str(n_str)) <= k:
        if k % 2 == 0 or k % 5 == 0 or str(k)[-1] == 0:
            n_str = -1
            return n_str
        if int(n_str) % k == 0:
            return len(str(n_str))
        else:
            n_str += n_str*10 +1

print(check(k))