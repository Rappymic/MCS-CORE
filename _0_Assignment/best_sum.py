tar = 302
num = [101, 7,2]

def best_sum(tar, num: list):
    list1 = [None for _ in range(tar + 1)]
    list1[0] = []
    for index, value in enumerate(list1):
        if value != None:
            for j in num:
                if index + j <= tar:
                    if list1[index + j] == None or len(list1[index + j]) > len(value + [j]):
                        list1[index + j] = value + [j]

    return list1[tar]

print(best_sum(tar, num))