'''
we can use else block with try and except block or with one try block also. else block should
be used after all except blocks and before finally block.
if the try block throws the exception then the statements in respective exception handling block
will get executed or if try block doesn't throws a exception and code in try block executed successfully
then all the statements in the else block will be getting executed.
'''

try:
    x = int(input('enter a number:'))

except ValueError:
    print('enter valid input')

else:
    l = []
    for i in range(x):
        l.append(i)
    print(l)

finally:
    print('---file has closed---')  # the statements written here will be get executed either exception occurs or not
