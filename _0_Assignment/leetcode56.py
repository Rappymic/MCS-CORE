class Solution:
    @staticmethod
    def wiggleMaxLength(nums) -> int:
        nums1 = nums[:]
        if nums[0] < nums[1]:
            mul = 1
        else:
            mul = -1
        for index, value in enumerate(nums[:-1], 1):
            if index % 2 == 0:
                if value * mul < nums[index] * mul:
                    mul *= -1
                else:
                    del nums[index-1]
            else:
                if value *mul > nums[index]*mul:
                    mul*=-1
                else:
                    del nums[index-1]
        return len(nums)







nums = [1,7,4,9,2,5]
print(nums[:-1])
print(Solution.wiggleMaxLength(nums))
