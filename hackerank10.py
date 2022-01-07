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
list1.sort()
print(list1)

path_list = [[] for i in range(len(list1))]
start_list = [i[0] for i in list1]
end_list = [i[1] for i in list1]

start_list = start_list[1:]
end_list = end_list[:-1]


print(start_list)
print(end_list)


i = 0
while i < len(start_list):
    i+=1
    for j in start_list:
        if end_list[i-1] < j:
            pass