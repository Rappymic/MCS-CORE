def minCut(self, s: str) -> int:
    # helper 1
    def isPalindrome(s):
        return s == s[::-1]

    # helper 2
    def f(l, r):
        if l > r:
            memo[(l, r)] = 0
            return memo[(l, r)]

        if isPalindrome(s[l:r + 1]):
            memo[(l, r)] = 0
            return memo[(l, r)]

        if (l, r) in memo:
            return memo[(l, r)]

        minCuts = r - l  # originalSize -1
        for i in range(l, r):
            if isPalindrome(s[l:i + 1]):
                minCuts = min(minCuts, 1 + f(i + 1, r))
        memo[(l, r)] = minCuts
        return memo[(l, r)]

    # main
    memo = {}
    return f(0, len(s) - 1)