from itertools import permutations
input = [4,900,1030,100,1000,1200,500,1100,1200,300,1050,1530,500]

no_jobs = input[0]
input.remove(no_jobs)

def return_job(list1):
    temp_list = []
    for i in list1[0:3]:
        temp_list.append(i)
        list1.remove(i)
    return temp_list

list1 = [return_job(input) for i in range(no_jobs)]

del input
print(list1)

path_list = [[] for i in range(len(list1))]


for index in range(len(list1)-1):
    if list1[index][1] < list1[index+1][0]:
        if index == 0:
            path_list[0].append(index)
            path_list[0].append(index+1)
        for ind, value in enumerate(path_list):
            if index in path_list[ind]:
                path_list[ind].append(index+1)
    else:
        if index == 0:
            path_list[0].append(index)
            path_list[1].append(index+1)
        for ind, value in enumerate(path_list):
            if index not in path_list[ind]:
                path_list[ind].append(index+1)
                break
print(path_list)