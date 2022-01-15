import sys

sys.setrecursionlimit(500000)

def arr(targetsum, numbers: list, memo={}):
    numbers.sort(reverse=True)
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return -1
    for num in numbers:
        remainder = targetsum - num
        remainder_result = arr(remainder, numbers, memo)
        if remainder_result != -1:
            memo[targetsum] = remainder_result + [num]
            return memo[targetsum]
    else:
        memo[targetsum] = -1
        return -1


tar = 5000

num = [4,5]

def cansum(target, num: list):
    list1 = [False for _ in range(target + 1)]
    list1[0] = True
    for index, value in enumerate(list1):
        if value == True:
            for j in num:
                if index + j <= target:
                    list1[index + j] = True
    # print(list1)
    return list1[target]

print(cansum(tar, num))

print(arr(5000,[4,5]))