import re
import cProfile, pstats, io
from functools import lru_cache


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
def countandsay(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    temp_str = countandsay(n-1)
    matcher = re.compile(r'(.)\1*')
    out = [match.group() for match in matcher.finditer(temp_str)]
    list1 = []
    for index, value in enumerate(out):
        list1.extend([str(len(value)), value[0]])
    return ''.join(list1)

print(countandsay(7))