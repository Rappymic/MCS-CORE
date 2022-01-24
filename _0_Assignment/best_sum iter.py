def best_sum(target, number: list):
    result_list = [[] for _ in range(target + 1)]
    result_list[0] = [[]]
    for index, value in enumerate(result_list):
        for num in number:
            if value:
                if index + num <= target:
                    result_list[index + num] += [i + [num] for i in value]
    print(len(result_list))
    return result_list


t = 30
num1 = [2, 3, 5]
a = best_sum(t, num1)