'''

we can use finally at the end of all blocks to close files or like database connections.
whether the exception occur or not the statement in the finally block will get executed
'''

try:
    z = open('E:\hrcallmynotes', 'r')

except FileNotFoundError:
    print('file has not found')

finally:
    print('---file has been closed---')
