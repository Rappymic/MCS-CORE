def check_paranthesis(str1):
    l1 = []
    pointer_open = 0
    for i in str1:
        if i == '(' or i == ')':
            l1.append(i)
    print(l1)
    if l1 == []:
        return True
    if l1[0] == ')' or l1[-1] == '(' or len(l1)%2 != 0:
        return False
    for i in l1:
        if pointer_open < 0:
            return False
        elif i == '(':
            pointer_open += 1
        else:
            pointer_open -= 1
    if pointer_open == 0:
        return True
    else:
        return False

str1 = '(())((()())())'
str1 = 'he(llo)'
print(check_paranthesis(str1))