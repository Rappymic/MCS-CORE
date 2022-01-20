class Solution:
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