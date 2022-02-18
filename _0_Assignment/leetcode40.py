class Solution:
    @staticmethod
    def threeSum(A ):
        if len(A) < 3: return
        from collections import Counter

        counts = Counter(A)  ## for the First part (twice)
        uniq = list(counts)  ## for the Second part(three)
        uIndex = {v: i for i, v in enumerate(uniq)}  ##cuz lookup O(1)
        ret = []

        ## First part: twice plus sth
        for twice in (k for k, v in counts.items() if v >= 2):
            for once in uniq:
                if once + twice * 2 == 0:
                    ret.append((once, twice, twice))
        if counts.get(0) == 2: ret.remove((0, 0, 0))  ## ad-hoc correct fault

        ## Second part: three things; no need to count
        size = len(uniq)
        for i in range(size - 2):
            one = uniq[i]
            del uIndex[one]  ##Optional optimize
            for j in range(i + 1, size - 1):
                two = uniq[j]
                need = -one - two
                if need in uIndex and uIndex[need] > j:
                    ret.append((one, two, need))
        return ret

print(Solution.threeSum([1,-1,0,2,4]))