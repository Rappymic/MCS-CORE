class Solution:
    @staticmethod
    def findRelativeRanks(score: list):
        e = len(score)
        score1 = sorted(score)
        a = score.index(score1[0])
        b = score.index(score1[1])
        c = score.index(score1[2])
        score[a] = 'Gold Metal'
        score[b] = 'Silver Medal'
        score[c] = 'Bronze Medal'
        for i in range(0,e+1,-1):
            if i != a or i != b or i != c:
                z = score.index(score1[i])
                score[z] = str(i+1)
        return score


