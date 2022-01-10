class Solution:
    @staticmethod
    def numSteps(s: str) -> int:
        a = int(s, 2)
        def check_prime(no):
            if no % 2 ==0:
                return True
            else:
                return False
        count = 0
        while a != 1:
            if check_prime(a) == True:
                a /= 2
                count += 1
            else:
                a += 1
                count += 1
        return count

s = '1111011110000011100000110001011011110010111001010111110001'
print(int(s, 2))
print(Solution.numSteps(s))


print(s.index('G'))