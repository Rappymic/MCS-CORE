'''
A decorator that allows a user to add new functionality to an existing object without
modifying its structure.
Decorators are usually called before the definition of a function you want to decorate.

This means that they support operations such as being passed as an argument,
returned from a function, modified, and assigned to a variable.
'''
# Python decorators.
print("___Assigning Functions to Variables___")

# we create a function that will add one to a number whenever it is called.
# We'll then assign the function to a variable and use this variable to call the function.

def plus_one(number):
    return number + 1

add_one = plus_one
print("output:",add_one(5))

'''
you can define a function inside another function in Python. 

'''
print("____Defining Functions Inside other Functions____")
def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
plus_one(4)


print("____Passing Functions as Arguments to other Functions___")
# Functions can also be passed as parameters to other functions.

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print("Result:", function_call(plus_one))

print("_____Functions Returning other Functions____")
# A function can also generate another function.

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print("Return other function:",hello())

print("___Nested Functions have Enclosing Function___")

# Python allows a nested function to access the outer scope of the enclosing function.
# This is a critical concept in decorators -- this pattern is known as a Closure.

def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")

'''
create a simple decorator that will convert a sentence to uppercase.
We do this by defining a wrapper inside an enclosed function. As you can see it very
similar to the function inside another function.
'''
print("___uppercase decorator_____")
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
'''
Our decorator function takes a function as an argument, and we shall, therefore, 
define a function and pass it to our decorator. We learned earlier that we could 
assign a function to a variable. We'll use that trick to call our decorator function.
'''
print("____decorator function takes function as argument____")

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
decorate()

# We simply use the @ symbol before the function we'd like to decorate.

print("__Decorator @ ___ ")
@uppercase_decorator
def say_hi():
    return 'hello there'

print("result:",say_hi())


print("___Applying Multiple Decorators to a Single Function___")
'''
We can use multiple decorators to a single function. 
However, the decorators will be applied in the order that we've called them. 
Below we'll define another decorator that splits the sentence into a list. 
We'll then apply the uppercase_decorator and split_string decorator to a single function.
'''

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there welcome'
print("using multiple decorators:",say_hi())

'''
From the above output, we notice that the application of decorators is from the bottom up. 
Had we interchanged the order, we'd have seen an error since lists don't have an upper 
attribute. The sentence has first been converted to uppercase and then split into a list.
Accepting Arguments in Decorator Functions

Sometimes we might need to define a decorator that accepts arguments. 
By passing the arguments to the wrapper function. 
The arguments will then be passed to the function that is being decorated at call time.
'''

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Hyderabad", "Bangalore")




