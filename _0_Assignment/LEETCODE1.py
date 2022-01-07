def fuct(list1, list2):
    list1.extend(list2)
    list1.sort()
    if len(list1) % 2 == 0:
        a = list1[len(list1)/2] + list1[len(list1)/2 - 1]
        return a/2
    else:
        a = list1[len(list1)//2]
        return a