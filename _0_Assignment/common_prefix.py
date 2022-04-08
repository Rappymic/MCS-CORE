def flower(strs: str):
    strs = sorted(strs, key=lambda x: len(x))
    start = strs[0]
    while True:
        for index in range(len(strs)):
            if strs[index].startswith(start) == False:
                start = start[:-1]
                break
            if start == '':
                return start
        else:
            return start


st = ["flower","flow","flight"]
# st = ["dog","racecar","car"]
print(flower(st))