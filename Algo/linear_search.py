def linear_search(list1 : list, target):
    '''
    Returns the index position of target if found, else return None
    '''

    for i in range(0, len(list1)):
        if list1[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print('Target found at at Index: ',index)
    else:
        print('Target not found')


num = [i for i in range(1,11)]
tar = 6

result = linear_search(num, tar)

verify(result)

