str1 = 'How long do you have to sit dear ?'

list1 = str1.split(" ")


def return_value(li):
    a = len(li) / 2
    if int(a) == a:
        return int(a)
    else:
        if str(li[-1]).isalpha():
            return int(a) + 1
        else:
            return int(a)

print(return_value(list1))