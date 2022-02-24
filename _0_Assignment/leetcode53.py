class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        l = len(s)
        if len(s) < 27:
            arr = set(list(s))
            if len(arr) == l:
                return l
        cur_count = 0
        final_count = 0
        i = 0
        start = 0
        while i < l:
            i += 1
            memb = set()
            for j in s[start:]:
                if j not in memb:
                    memb.add(j)
                    cur_count += 1
                else:
                    start = i
                    if cur_count > final_count:
                        final_count = cur_count
                    cur_count = 0
                    break
        return final_count

s = "aabc"
print(Solution.lengthOfLongestSubstring(s))