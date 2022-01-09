def recursive_binary_search(li, target):
    if len(li) == 0:
        return False
    else:
        midpoint = (len(li))//2
        if li[midpoint] == target:
            return True
        else:
            if li[midpoint] < target:
                return recursive_binary_search(li[midpoint+1:], target)
            else:
                return recursive_binary_search(li[:midpoint-1], target)

def verify(result):
    print('Target Found: ', result)

num = [i for i in range(1,11)]

result = recursive_binary_search(num, 34)

verify(result)