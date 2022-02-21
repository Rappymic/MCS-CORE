def firstMissingPositive(self, nums: List[int]) -> int:
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if 0 <= j < len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i, x in enumerate(nums):
        if i != x - 1:
            return i + 1

    return len(nums) + 1