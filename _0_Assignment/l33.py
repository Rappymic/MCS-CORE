class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0: return -1
        n = 1
        for i in range(k):
            R = n % k
            if R == 0: return i+1
            n = R * 10 + 1