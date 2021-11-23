'''
To define a decorator that can be applied to any function
we use args and **kwargs. It collect all positional and keyword arguments
and stores them in the args and kwargs variables.
args and kwargs allow us to pass as many arguments as we would like during function calls.
'''
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

# Let's see how we'd use the decorator using positional arguments.
print("___using decorator___")
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)

print("____Keyword arguments are passed using keywords___")

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")

print("___Passing Arguments to the Decorator___")
'''
Now let's see how we'd pass arguments to the decorator itself. 
In order to achieve this, we define a decorator maker that accepts arguments 
then define a decorator inside it. We then define a wrapper function inside the 
decorator as we did earlier.
'''
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

print("Result: ",decorated_function_with_arguments(pandas, "Science", "Tools"))


print("___Debugging Decorators____")
'''
As we have noticed, decorators wrap functions. 
The original function name, its docstring, and parameter list are all hidden by the 
wrapper closure: 
For example, when we try to access the decorated_function_with_arguments metadata, 
we'll see the wrapper closure's metadata. This presents a challenge when debugging.

# decorated_function_with_arguments.__name__
'wrapper'

decorated_function_with_arguments.__doc__

'This is the wrapper function'

Python provides a functools.wraps decorator. 
This decorator copies the lost metadata from the undecorated function to the 
decorated closure. 
'''
print("using functools")
import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    "This will say hi"
    return 'hello there'

print(say_hi())


'''

It is advisable and good practice to always use functools.wraps when defining decorators. 
It will save you a lot of headache in debugging.
Python Decorators Summary

Decorators dynamically alter the functionality of a function, method, or class without 
having to directly use subclasses or change the source code of the function being decorated.
Using decorators in Python also ensures that your code is DRY(Don't Repeat Yourself). 
Decorators have several use cases such as:

    Authorization in Python frameworks such as Flask and Django
    Logging
    Measuring execution time
    Synchronization'''