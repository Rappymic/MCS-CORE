str1 = 'Welcome to Python'

def reverse_str(s : str):
    l1 = s.split(' ')
    l2 = [i[::-1] for i in l1]
    s = ' '.join(l2)
    return s

print(reverse_str(str1))