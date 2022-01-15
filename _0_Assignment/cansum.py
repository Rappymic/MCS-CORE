tar = 300

num = [7,14]

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