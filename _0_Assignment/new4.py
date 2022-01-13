def allconstruc(target, wordbank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    total = []
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            resultant = allconstruc(suffix, wordbank, memo)
            targetways = [[word] + i for i in resultant]
            memo[target] = targetways
            total.extend(targetways)
    else:
        memo[target] = total
        return total


# print(allconstruc('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef']))

print(allconstruc('eeeeeeeef', ['ka','rt' ,'i' ,'k', 'ee', 'eeee', 'eee', 'eeeeeee']))

