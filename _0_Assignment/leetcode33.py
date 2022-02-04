class Solution:
<<<<<<< HEAD
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
=======
    @staticmethod
    def minEatingSpeed(piles: list, h: int) -> int:
        l = len(piles)
        if l == 1:
            return abs(-piles[0]//h)
        piles.sort()
        if l == h:
            return max(piles)
        av = sum(piles) // l
        def reu(pile: list, hr, av):
            banana_speed = [0 for _ in range(l)]
            for index, value in enumerate(pile):
                banana_speed[index] = abs(-value//av)
            return sum(banana_speed)
        var1 = reu(piles, h , av)
        if var1 < h:
            while var1 != h:
                var1 = reu(piles, h, av)
                av -= 1
        elif var1 > h:
            while var1 > h:
                av += 1
                var1 = reu(piles, h, av)
        av1 = av - 1
        if h == reu(piles, h, av1):
            return av1
        return av


piles = [312884470]
h = 312884469


print(Solution.minEatingSpeed(piles,h))
print([i for i in range(1)])
>>>>>>> c9ac1b11d4c80c63700f1022a84f57e5e62cc552
