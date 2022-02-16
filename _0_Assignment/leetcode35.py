class Solution:
    @staticmethod
    def decodeCiphertext(encodedText: str, rows: int):
        col = len(encodedText)// rows
        print(col)
        result = []
        for i in range(0, len(encodedText)-rows+2, col):
            result.append([i for i in encodedText[i:i + col]])
        str1 = ''
        print(result)
        a = 1
        while a <= col:
            for index, value in enumerate(result):
                try:
                    str1 += result[index][index]
                    print('111',result[index][index])
                    print(str1)
                    del result[index][index]
                except:
                    continue
            a += 1
        print('----------',str1)
        return str1




encodedText = "ch   ie   pr"
rows = 3
result = []
print(len(encodedText)//4)
for i in range(0, len(encodedText)-3, 4):
    result.append(encodedText[i:i+4])
a = 1
result = [[i for i in str1] for str1 in result]
str1 = ''
while a < 5:
    for index, value in enumerate(result):
        try:
            str1 += result[index][index]
            del result[index][index]
        except:
            continue
    a += 1
print(str1)

print(Solution.decodeCiphertext(encodedText, rows))

text = "a "
ro = 2
print(len(text))
print(Solution.decodeCiphertext(text, ro))

from itertools import permutations