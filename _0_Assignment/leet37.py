class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        a = 1
        while True:
            if a not in nums:
                return a
            else:
                a += 1