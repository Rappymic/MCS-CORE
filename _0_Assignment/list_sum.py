list1 = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6]

def return_sum(l1: list):
    dict1 = {}
    for i in l1:
        if i not in dict1:
            dict1[i] = l1.count(i)
    final_list = []
    for key, value in dict1.items():
        a = [key for _ in range(value)]
        final_list.append(a)
    dict2 = {}
    def mul_val(l2):
        mul = 1
        for i in l2:
            mul *= i
        return mul
    for i in final_list:
        dict2[tuple(i)] = mul_val(i)
    sum = 0
    print(dict2)
    for key, value in dict2.items():
        sum += value
    return sum


def ret_sum1(l1):
    l2 = set(l1)
    dict1 = {}
    mul = 0
    for i in l2:
        a = l1.count(i)
        temp = [i for _ in range(a)]
        dict1[tuple(temp)] = i**a
        mul += dict1[tuple(temp)]
    print(dict1)
    return mul
    # print(dict1)
    # for key, value in dict1.items():
    #     mul += value
    # return mul


print(return_sum(list1))
print(ret_sum1(list1))