def allconstruc(target, numbers):
    def new(target, numbers, memo={}):
        if target in memo:
            return memo[target]
        if target < 0:
            return -1
        if target == 0:
            return [[]]
        total = []
        for num in numbers:
            # if target.startswith(word):
            remainder = target - num
            resultant = new(remainder, numbers, memo)
            if type(resultant) == list:
                targetways = [[num] + i for i in resultant]
                # print(targetways)
                memo[target] = targetways
                total.extend(targetways)
        else:
            memo[target] = total
            return total

    temp = []
    b = new(target, numbers)
    for i in b:
        i.sort()
    for i in b:
        if i not in temp:
            temp.append(i)
    return len(temp)


print(allconstruc(26, [1,2,3]))