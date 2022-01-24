class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr2 = []
        arr4 = []
        for x in arr:
            if x < 0:
                arr2.append(x)
            elif x >= 0:
                arr4.append(x)
        c = collections.Counter(arr4)
        if c[0] % 2:
            return False
        for x in sorted(c):
            if c[x] > c[2 * x]:
                return False
            else:
                if x:
                    c[2 * x] -= c[x]
                else:
                    c[2 * x] = int(c[2 * x] / 2)

        d = collections.Counter(arr2)
        for x in sorted(d, reverse=True):
            if d[x] > d[2 * x]:
                return False
            else:
                d[2 * x] -= d[x]
        return True
