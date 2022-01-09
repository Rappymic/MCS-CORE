def merge_sort(l):
    if len(l) <=1:
        return l

    left_half, right_half = split(l)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(li):
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    return left, right

def merge(left, right):
    l = []
    i = 0
    j = 0
    while 1<len(left) and j <len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

list1 = [i for i in range(0,100)][::-1]

l = merge_sort(list1)

print(l)