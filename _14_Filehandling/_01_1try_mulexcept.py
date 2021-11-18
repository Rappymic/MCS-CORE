'''
we can use one try block with multiple except blocks. if try block doesn't throw exception the except block will
not execute. if it throws the exception then the except block with specific error will execute
'''
try:
    x = int(input('enter a number'))
    l = [10, 20, 26, 41, 33, 25, 44]
    l1 = []

    for i in l:
        if i % x == 0:
            l1.append(i)
        else:
            pass
    print('the value in list which are exactly divisble by given number:', l1)

except ValueError :
    print('enter numbers only')

except ZeroDivisionError:
    print("Don't enter zero")

except Exception as e:
    print('unexpected Error')


