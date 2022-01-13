def possible_str(target: str, str1, memo=None):
    if memo is None:
        memo = {}
    if memo is None:
        memo = {None}
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in str1:
        if target.startswith(word):
            suffix = target[len(word):]
            result = possible_str(suffix, str1, memo)
            if result:
                memo[target] = True
                return True
    else:
        memo[target] = False
        return False


print(possible_str('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(possible_str('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                   ['e', 'ee', 'eeee', 'eee', 'eeeeeee']))


def poss_num_str(target: str, str1, memo={'' : 1}):
    if target in memo:
        return memo[target]
    total_count = 0
    for word in str1:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways_rest = poss_num_str(suffix, str1, memo)
            total_count += num_ways_rest
    else:
        memo[target] = total_count
        return total_count

print(poss_num_str('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o','t']))
print(poss_num_str('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                   ['e', 'ee', 'eeee', 'eee', 'eeeeeee','f']))
