

class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        start = -1
        l = len(s)
        count = 0
        final = 0
        while start < l:
            start += 1
            temp_str = set()
            for index, value in enumerate(s[start:]):
                if value not in temp_str:
                    temp_str.add(value)
                    count = len(temp_str)
                else:
                    final = max(count, final)
                    count = 0
                    break
                print(temp_str)
            if index == len(s[start:]) -1:
                break
        return max(final, count)

s = 'aabbcc'

print(Solution.lengthOfLongestSubstring(s))



s = "aabc"