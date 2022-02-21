class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for bit in range(32):
            cntBit = 0
            for i in nums:
                if (1<<bit)&abs(i)!=0:
                    cntBit+=1
            if cntBit%3!=0:
                result|=(1<<bit)
        cnt = nums.count(result)
        if cnt!=1:
            result=-result
        return result