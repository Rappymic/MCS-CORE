"""Problem Statement -:  You are given an array, You have to choose a
contiguous subarray of length ‘k’, and find the minimum of that segment,
return the maximum of those minimums.

Sample input 0

1 →  Length of segment x =1

5 →  size of space n = 5

1 → space = [ 1,2,3,1,2]

2

3

1

2

Sample output

3

Explanation

The subarrays of size x = 1 are [1],[2],[3],[1], and [2],Because each
subarray only contains 1 element, each value is minimal with respect to the
subarray it is in. The maximum of these values is 3. Therefore, the answer
is 3 """


def return_min(list1):
    a = list1[0]
    for i in list1:
        if i < a:
            a = i
    return a


def return_max(list1):
    a = list1[0]
    for i in list1:
        if i > a:
            a = i
    return a


input1 = [2, 5, [1, 2], [2, 3], [4, 5], [5, 4], [6, 7]]

len_sub_seg = input1[0]
no_seg = input1[1]

final_list = input1[2:]

temp_min_list = []

for i in final_list:
    a = return_min(i)
    temp_min_list.append(a)

result = return_max(temp_min_list)

print(result)
