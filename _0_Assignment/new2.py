def arr(targetsum, numbers: list, memo={}):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    short_comb = None
    for num in numbers:
        remainder = targetsum - num
        remainder_result = arr(remainder, numbers, memo)
        if remainder_result != None:
            memo[targetsum] = remainder_result + [num]
            if short_comb == None or len(short_comb) < len(memo[targetsum]):
                short_comb = memo[targetsum]
    else:
        memo[targetsum] = short_comb
        return short_comb


print(arr(800, [201, 301, 55, 12]))
