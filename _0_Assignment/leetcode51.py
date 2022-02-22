class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        num_middle = numRows - 2
        str_list = [i for i in s]
        result_list = []
        a = 1
        while len(s_copy) > 0:
            if a == 1:
                s_copy = s_copy[:numRows]
                a = 0
            else:
                s_copy = s_copy[:]



s = 'PAYPALISHIRING'
num = 3

print(Solution.convert(s, 3))