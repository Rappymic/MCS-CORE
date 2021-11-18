
'''
we can use multiple try and multiple except blocks according to our logic

'''

try:
    x = int(input('enter a number:'))
except ValueError:
    print('enter valid number')
l1 = []
l2 = []
try:
    for i in range(x):
        l1.append(i)
    print(l1)
except NameError:
    print('You have passed string instead of number')
try:
    for i in range(len(l1)):
        x = l1[i ] *2
        l2.append(x)
    print(l2)
except IndexError:
    print('you have missed the logic')

except Exception:
    print('Unexpected error')

finally:
    print('--- program ended ---')
