def best_sum(number: list, target: int):
    temp_list = [[] for _ in range(target+1)]
    temp_list[0] = [[]]
    for index, value in enumerate(temp_list):
        if value != []:
            for num in number:
                if index + num <= target:
                    temp_list[index + num].extend([i + [num] for i in temp_list[index]])
                    print(temp_list)
    # print(temp_list)
    return temp_list[-1]



numbers = [2,3,6,7]

target = 7

print(best_sum(numbers, target))