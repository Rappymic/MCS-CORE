
'''
we can use multiple except blocks with one try block at start and ending with one finally block

'''

try:
    x = int(input('enter a number: '))
    l = []
    for i in range(5):
        res = i / x
        l.append(res)
    print(l)

    z = open('E:\hrcallmynotes', 'r')

except ValueError:
    print('enter only numbers')

except ZeroDivisionError:
    print("please don't enter Zero ")

except FileNotFoundError:
    print('file has not found')

finally:
    print('---file has been closed---')

