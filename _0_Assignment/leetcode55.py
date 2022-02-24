class Solution:
    @staticmethod
    def tupleSameProduct(nums):
        dict1 = {}
        count = 0
        dic2 = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i] * nums[j]
                dic2[(nums[i], nums[j])] = a
                if a in dict1:
                    dict1[a] += 1
                else:
                    dict1[a] = 1
        print(dict1)
        print(dic2)
        for key, values in dict1.items():
            if values > 1:
                count += values
        return count*8         
        



nums = [2,3,4,6,8,12]

print(Solution.tupleSameProduct(nums))