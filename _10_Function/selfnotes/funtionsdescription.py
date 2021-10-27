"""
Python Functions is a block of related statements designed to perform a
computational, logical, or evaluative task; they are commonly repeated tasks
that are put into functions and can be called for different computation of
same nature.

there are two types of function on the basis of definition:

1. Built-in functions: Functions that are pre defined by python programming
    language itself. The functions include sum, sorted, etc.

2. User defined functions: These functions are defined by the user, and can
    include input parameters or not. Usually function have a return statement
    which returns the value when the function is called after performing some
    business logic.

    function can be with or without input and with or without return and
    combination between them.

    Parameters and arguments
    ------------------------
    parameters are defined in the function and have scope within the function
    itself only. They can be assigned a default value in case the argument that
    is passed doesn't have any assigned value for a that particular parameter

    Arguments are usually literals or variables or any value that is passed to
    the parameter to perform some business logic.

    Anonymous Function
    ------------------
    When function is defined only to be used and stored in one variable that
    function has no real use after the assignment of that variable is called
    anonymous function. It is defined by lambda

    Scopes of variable
    __________________

    Local Scope: A defined variable that is only accessible by the local
    function in the business logic have local scope. These variables can't be
    accessed outside the function.

    Global Scope: A variable that can be accessed outside the function and
    inside a function (assigned no new variable of same name is defined in the
    function) have global scope.
"""