# we can use one try with multiple except and then else and at end we can use finally block

print("press '0' to add number or '1' to add any two strings")
try:
    def inp(x):
        if x == 0:
            num1 = int(input('enter a number:'))
            num2 = int(input('enter a number:'))
            return num1, num2
        elif x == 1:
            string1 = str(input('enter a string:'))
            string2 = str(input('enter a string:'))
            return string1, string2
        else:
            print('please enter valid option only')
            return inp(int(input('enter 0 or 1 : ')))


    A, B = inp(int(input('enter your choice 0 or 1:')))
except ValueError:
    print('Please enter valid input:')
    print("press '0' to add number or '1' to add any two strings")
    A, B = inp(int(input('enter your choice 0 or 1:')))


    def add(a, b):
        if type(a) == int and type(b) == int:
            print('Addition of two integers:',a + b)
        if type(a) == str and type(b) == str:
                    print('Addition of two strings:',a + b)


    add(A, B)
except Exception:
    print('Please enter valid input:')
    print("press '0' to add number or '1' to add any two strings")
    A, B = inp(int(input('enter your choice 0 or 1:')))


    def add(a, b):
        if type(a) == int and type(b) == int:
            print('Addition of two integers:',a + b)
        if type(a) == str and type(b) == str:
                    print('Addition of two strings:',a + b)


    add(A, B)


else:
    def add(a, b):
        if type(a) == int and type(b) == int:
            print('Addition of two integers:',a + b)
        if type(a) == str and type(b) == str:
                    print('Addition of two strings from else:',a + b)


    add(A, B)

finally:
    print('---end of the program----')
