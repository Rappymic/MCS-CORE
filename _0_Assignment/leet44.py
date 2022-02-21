class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        non_rep_sub_str = ""
        for i in s:
            if i in non_rep_sub_str:
                non_rep_sub_str = non_rep_sub_str.split(i)[1] + i
            else:
                non_rep_sub_str += i
                max_length = max(max_length, len(non_rep_sub_str))
        return max_length