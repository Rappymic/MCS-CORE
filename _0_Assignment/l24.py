class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(1, len(x) // 2 + 1):
            if x[i - 1] != x[-i]:
                return False
        else:
            return True
