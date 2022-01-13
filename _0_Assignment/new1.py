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

print(arr(11,[4,5]))