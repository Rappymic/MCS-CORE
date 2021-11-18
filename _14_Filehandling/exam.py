def print_details(query, data):
    print(f"Match for : {query}")
    list1 = []
    for value in data:
        if query in value:
            list1.append(value)
    list1.sort()
    if len(list1) == 0:
        print("No matches Found")
    else:            
        for i in range(0, len(list1)):
            print(f"Result {i+1}:", end=" ")
            split_print(list1[i])

def split_print(data):
    list1 = data.split(",")
    list2 = []
    for i in list1:
        i = i.replace(" ", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        i = i.replace("-", "")
        list2.append(i)
    for index, value in enumerate(list2):
        if value.isdigit():
            a = list2.pop(index)
            list2.append(a)
    print(f"{list2[0]}, {list2[1]}, {list2[2]}, {list2[3]}")

datasheet = "/Users/micron/Documents/Self/query - Copy.txt"

with open (datasheet, "r") as data:
    data = data.readlines()

phonedir = "/Users/micron/Documents/Self/phone_dataset - Copy.csv"
with open (phonedir, "r") as phone:
    phone = phone.readlines()
temp_query = [search.rstrip("\n") for search in data]
temp_data = []
for i in phone:
    i = i.rstrip('"\n')
    i = i.lstrip('"')
    temp_data.append(i)


for value in temp_query:
    print_details(value, temp_data)