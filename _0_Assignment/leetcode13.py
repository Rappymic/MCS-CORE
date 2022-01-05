nums = [-2, 0 , 0]
nums = sorted(nums, reverse=True)
print(nums)
a = '2'
lent = len(nums)
for i in nums:
    if a == i:
        continue
    if nums.count(i) > lent / 2:
        print(i)
        break
    else:
        a = i