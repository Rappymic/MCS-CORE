class Solution:
    @staticmethod
    def largeGroupPositions(s: str):
        ind = []
        a = s[0]
        s += '.'
        index1 = s.index('a')
        for index, value in enumerate(s):
            if value != a:
                if index - index1 > 2:
                    ind.append([index1,index-1])
                a = value
                index1 = index
        print(ind)
        return ind

str2 = 'aaaaaa'

Solution.largeGroupPositions(str2)