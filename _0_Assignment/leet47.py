class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        v = sorted(set(arr))
        d, l= {}, []
        for i in range(1,len(v)+1):
            d[v[i-1]] = i
        for i in arr:
            l.append(d[i])
        return l