def rec_best_sum(numbers: list, target: int, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return [[]]
    if target < 0:
        return []
    total = []
    for num in numbers:
        remainder = target - num
        remainder_res = rec_best_sum(numbers, remainder, memo)
        # print(remainder_res)
        if remainder_res != []:
            memo[target] = [i + [num] for i in remainder_res]
            total.extend(memo[target])
    else:
        memo[target] = total
        return total

numbers = [2,3,6, 7]
target = 14

print(rec_best_sum(numbers, target))