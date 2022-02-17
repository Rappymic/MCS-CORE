class Solution:
    @staticmethod
    def longestCommonPrefix(strs):
        strs.sort(key=len)
        first_str = strs[0]
        possible_substrings = []
        # for i in reversed(range(0, len(first_str))):
        #     possible_substrings.append(first_str[0:i+1])
        result = []
        for k in reversed(range(0, len(first_str))):
            temp = first_str[0:k+1]
            for i in strs:
                if i.startswith(temp):
                    result.append(True)
                else:
                    result.append(False)
            if False not in result:
                return temp
            result = []
        else:
            return ''



strs = ["flower","flow","flight"]

print(Solution.longestCommonPrefix(strs))

