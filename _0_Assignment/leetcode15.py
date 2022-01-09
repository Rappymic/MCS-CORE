def nearestValidPoint(x: int, y: int, points):
    list1=[]
    for index, value in enumerate(points):
        if value[0] == x or value[1] == y:
            list1.append([value[0], value[1], index])
    print(list1)
    if list1 == []:
        return 0
    list2 = [[val, abs(x-val[0])+abs(y-val[1])] for val in
             list1]
    list2 = sorted(list2, key= lambda x:x[1])
    print(list2)
    return list2[0][0][2]


po = [[1,2],[3,1],[2,4],[2,3],[4,4]]
nearestValidPoint(x = 3, y=4, points=po)
print(float('inf'))