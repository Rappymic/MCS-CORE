def binary_search(li: list, target):
    first = 0
    last = len(li) - 1
    while first <= last:
        midpoint = (first + last)//2
        if li[midpoint] == target:
            return midpoint
        elif li[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

num = [i for i in range(1,11)]
tar = 9

result = binary_search(num,6)

print(result)