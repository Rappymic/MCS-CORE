str1 = '{{[[[(((uhfw)))]]]}}'

def valid_str(s: str):
    open = {'{':'}','[':']','(':')'}
    close = {'}', ']', ')'}
    l1 = []
    for index, value in enumerate(s[:len(s)//2], 1):
        if value in close:
            return False
        elif value in open and s[-index] == open[value]:
            l1.append(True)
        elif value in open and s[-index] != open[value]:
            l1.append(False)
    if False in l1:
        return False
    else:
        return True




print(valid_str(str1))