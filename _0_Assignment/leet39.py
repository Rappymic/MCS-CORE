class Solution:
    @staticmethod
    def letterCombinations( digits: str):
        phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
                 '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        for i in digits:
            result.append([j for j in phone[i]])
        print(result)
        for _ in range(4):
            b = result[-1]
            try:
                a = result[-2]
                c = [a[i] + b[j] for j in range(len(b)) for i in range(len(a))]
            except:
                pass
            del result[-1]

dig = '2349'
print(Solution.letterCombinations(dig))