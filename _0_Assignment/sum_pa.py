tar = 300
num = [7, 14]

def sum_pat(target, num: list):
    list1 = [None for _ in range(target + 1)]
    list1[0] = []
    for index, value in enumerate(list1):
        if value != None:
            for j in num:
                if index + j <= target:
                    list1[index + j] = value + [j]
    return list1[target]
print(sum_pat(tar, num))