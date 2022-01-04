import cProfile, pstats, io


def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profile
def fuc(str1, n):
    list1 = []
    j = 0
    lent = len(str1)
    if n == lent or n == 1:
        return str1
    for i in range(2, lent + 3):
        if j > lent:
            break
        if i % 2 == 0:
            a = str1[j: j + n]
            list1.append(a)
            j = j + n
        elif n != 2:
            a = str1[j: j + n - 2]
            if len(a) < n - 2:
                a = a.ljust(n - 1, ' ')
            else:
                a = a.center(n, ' ')
            list1.append(a[::-1])
            j = j + n - 2
            # list1[-1] = list1[-1].ljust(n, '-')
    list1 = (list1)
    list2 = []
    for index in range(min(n, len(str1))):
        for i in list1:
            if len(i) > index:
                list2.append(i[index])
    str2 = ''.join(list2)
    str2 = str2.replace(' ', '')
    return str2
str1 = 'PAYPALISHIRING'
n= 4
print(fuc(str1,n))
