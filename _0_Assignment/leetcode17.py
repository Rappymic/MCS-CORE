nums = [1,1,4,2,3]
x = 5
count = 0


class Solution:
    @staticmethod
    def minOperations( nums, x: int) -> int:
        total_sum = sum(nums)
        if total_sum == x:
            return len(nums)
        n = len(nums)
        target = total_sum - x
        ht = {}
        ht[0] = -1
        rs = 0
        ans = float('inf')
        for i in range(n):
            rs += nums[i]
            if rs - target in ht:
                ans = min(ans, n - (i - ht[rs - target]))
            ht[rs] = i
        return ans if ans != float('inf') else -1

print(Solution.minOperations(nums,x))