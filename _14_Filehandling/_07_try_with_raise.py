'''
we can raise the exception where we want inside the try block and when the raise statement executes
the statements inside the concerned exception block will get executed
'''


def add():
    try:
        age = int(input('enter a number:'))
        if age < 0:
            raise ValueError('please enter number above 0')
        elif age > 100:
            raise OverflowError('please enter below 100')
        elif age < 18:
            print('you are not eligible to vote')
        elif age >= 18:
            print('you are eligible to vote')
        else:
            pass
    except ValueError as v:
        print(v)
        add()
    except OverflowError as o:
        print(o)
        add()
    except Exception as e:
        print('unexpected error')
        add()


add()
