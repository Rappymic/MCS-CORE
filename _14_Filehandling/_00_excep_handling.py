'''
Errors in python are three types
1. compile time error
2. Run time error
3. Logical error

compile time errors are nothing but syntax error which occurs when we not follow indentation, : etc
fails to compile. these error are detected by python compiler

runtime error are occurred when pvm is not able to execute some statement in the program. these error
is detected by pvm at run time only

logical errors occur due to flaws in logic of the program. logical errors are not detected by pvm or
python compiler as it logical code mistake made by programmer and programmer is responsible for it.

Exception:
Exceptions are the unusual event that occurs during the execution of the program that interrupts the
normal flow of the program.
Generally, exceptions occur when the code written encounters a situation it cannot cope with.
Whenever an exception is raised, the program stops the execution, and thus the further code is not executed.
Therefore, an exception is a python object that represents a run-time error.
An exception is a Python object that represents an error.
To handle the exceptions we use Try and except block
 The try block has the code to be executed and if any exception occurs then the action to perform is written
 inside the Except block.

 syntax:
 try:
    statements to be executed
 except:
    statements to be executed if exception occurs
'''


try:
    a = int(input('enter a number:'))  # these statements are executed first
    b = int(input('enter a number'))   # if user enters invalid details it goes to except block


    def sum(x,y):
        res = x + y
        return res


    sum(a, b)

except ValueError:
    print('enter only numbers')     # this statement will get execute and user get message of enter num only

print('---end of the program---')  # whether exception occurs or not this statement will execute as we are handling the
                                   # the exception


'''
in the above program we are handling the exception using try and except block. so if the code in try blocks throws any
exception then python will check whether the programmer is handling this exception or not. if yes then python 
will execute the statements present in that except block and also remaining statements ,if no the python will 
throw an exception and the statements after that exception will not get executed. 
'''



