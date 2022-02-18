class Solution:
    @staticmethod
    def checkPossibility(nums: list[int]):
        count = 0
        current = nums[0]
        for index, value in enumerate(nums[:-1]):
            if value > nums[index+1] or current > nums[index+1]:
                count += 1
            elif current < value:
                current = value
        print(count)
        if count > 1:
            return False
        else:
            return True



nums = [4,2,3]
print(Solution.checkPossibility(nums))

