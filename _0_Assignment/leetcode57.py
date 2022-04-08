

class Solution:
    @staticmethod
    def reorganizeString(s: str) -> str:
        from collections import Counter
        char_count = Counter(s)
        most_common = char_count.most_common(26)
        print(most_common)
        

str1 = 'aabccc'
print(Solution.reorganizeString(str1))
