nums = [0,1,0,3,12]

zero = nums.count(0)

for i in range(len(nums)):
    if nums[i] == 0:
        del nums[i]
        nums.append(0)
print(nums)

list1 = [1,2,3,4]
list2 = [5,6,7]
list3 = [[list1[i], list2[j]] for j in range(len(list2)) for i in range(len(list1))]
print(list3)