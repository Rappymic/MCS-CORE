# import csv
#
# data = open('E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\phone_dataset.csv', 'r')
# read = csv.reader(data)
# list1 = []
# list2 = []
# for i in read:
#     # for j in range(len(i)):
#     #     # i = i[j].strip(" ' ")
#     # x = i.split(',')
#     list1.extend(i)
# print(list1)
# data1 = open('E:\MCS-0040_MCS_shiva_Corepython\_15_File_Handling\Self-notes\query - Copy.txt', 'r')
# for data in data1.readlines():
#     data = data.strip('\n')
#     list2.append(data)
# list1.sort()
# print(list1)
# print(list2)
#
# for i in list2:
#     for j in range(len(list1)):
#         if i in list1[j]:
#             print(f'matches {i} : details {list1[j]}')


import csv

csv_data = []

file2 = open('file2.txt','w')


with open("phone_dataset.csv", 'r') as phone_data:

    my_csv = csv.reader(phone_data, delimiter=',')
    for i in my_csv:
        csv_data.append(i)
    with open("query - Copy.txt", "r") as query_data:
        input_data = query_data.read()
        input_data = input_data.splitlines()

    for inpt in input_data:
        count = 1
        matches = False
        file2.write(f"matches for {inpt} \n")
        for csv_d in csv_data:
            temp_csv = csv_d
            csv_d = csv_d[0].split(',')
            if csv_d[0].strip().lower() == inpt.lower() or csv_d[1].strip().lower() == inpt.lower():
                file2.write(f"Result {count} : {temp_csv} \n")
                count = count + 1
                matches = True
        if matches == False:
            file2.write("No Result Found \n")
file2.close()