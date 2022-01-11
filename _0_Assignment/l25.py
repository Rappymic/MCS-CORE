class Solution:
    def maxArea(self, nums) -> int:
        left, right = 0, len(nums)-1
        res = float('-inf')
        while left < right:
            res = max(res, min(nums[left], nums[right])*(right-left))
            if nums[left] < nums[right]:
                left+=1
            else:
                right-=1
        return res