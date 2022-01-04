lists = [[1,4,5],[1,3,4],[2,6]]

list1 = [lists[0].extend(i) for i in lists[1:]]

print(list1)