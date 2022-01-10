class Solution:
    @staticmethod
    def minOperations(nums1, nums2) -> int:
        act_sum1 = sum(nums1)
        act_sum2 = sum(nums2)
        if act_sum1 < act_sum2:
            nums1, nums2 = nums2, nums1
            act_sum1,act_sum2 = act_sum2,act_sum1
        if act_sum1 == act_sum2:
            return 0
        len1 = len(nums1)
        len2 = len(nums2)
        max_sum1 = len1*6
        min_sum1 = len1
        max_sum2 = len2*6
        min_sum2 = len2
        if max_sum2 < min_sum1:
            return -1
        diff = (act_sum1 - act_sum2)*-1
        print(diff)
        i = 5
        j = 6
        k = 1
        while diff < 0:
            if i*(nums1.count(j) + nums1.count(k)) > abs(diff):
                return -result
            else:
        result = diff//5
        return -result

nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,2,2]

n3 = [3,3,2,4,2,6,2]
n4 = [6,2,6,6,1,1,4,6,4,6,2,5,4,2,1]
n3.sort()
n4.sort(reverse=True)
print(n3)
print(n4)
print(f'sum 3: {sum(n3)}')
print(f'sum 4: {sum(n4)}')
print(Solution.minOperations(n3,n4))
n3 = [2, 2, 2, 3, 3, 4, 6]
n4 = [1, 1, 1, 1, 1, 5, 4, 4, 4, 2, 2, 2, 1, 1, 1]
print(f'sum 3: {sum(n3)}')
print(f'sum 4: {sum(n4)}')

