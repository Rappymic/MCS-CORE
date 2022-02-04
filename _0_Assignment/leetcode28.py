class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #Base Case
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [nums]
        #ToDo
        else:
            emptylist=[]
            for i in range(len(nums)):
                first_value=nums[i]
                rest_value=nums[:i]+nums[i+1:]
                for k in self.permuteUnique(rest_value):
                    emptylist.append([first_value]+k)
            newlist=[]
            for p in emptylist:
                if p not in newlist:
                    newlist.append(p)
            return newlist
