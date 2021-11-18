'''
we create our own exception class and can use our own modified exception by simply raising with
exception class when ever required.
'''


class Shiva(Exception):
    def __init__(self,e):
        self.e =e
        print(self.e)

def add():
    try:
        num1 = int(input('enter a number:'))
        num2 = int(input('enter a number:'))
        if num1 < 0 or num2 < 0:
            raise Shiva('please enter both number greater than zero')

        else:
            print(num1 + num2)
    except ValueError:
        print('enter number only')
        add()
    except Shiva:
        add()

add()