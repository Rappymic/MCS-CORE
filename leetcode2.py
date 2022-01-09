from itertools import combinations
nums = [2,7,11,15]
target = 9

# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     pass

temp_list = [i for i in range(len(nums))]

print(temp_list)

def comb_gen(list1 , n ):
    a = combinations(list1, n)