nums = [3,2,4]
nums = tuple(nums)
target = 6

def fun(num, targ):
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            if num[i] + num[j] == targ:
                return [i,j]

print(fun(nums, target))
