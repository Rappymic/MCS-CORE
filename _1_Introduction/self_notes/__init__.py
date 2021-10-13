"""
python is an interpreted language unlike c which is compiled language
-- Interpreter - Interprets single line of code
    No intermediate object code
    compilation and execution takes place simultaneously
    slower
    less memory is required (single line at a time)
    error line by line easy to find
    conditional statements are slower
-- Compiler - Compiles the whole code at the same time'
    Intermediate object code is generated
    compilation of whole code takes place before execution
    more memory is required
    display all errors at the same time

Python was created by Guido van Rossum during 1985- 1990
Python is a general-purpose interpreted, interactive, object-oriented,
and high-level programming language
 Has broad standard library
 gui
 databases
 oops
 dynamically typed (int is not required for type casting)
 automatic garbage collection
 web development -- Django and flask
 erp

 Bytecode, also termed portable code or p-code, is a form of
 instruction set designed for efficient execution by a software interpreter

Cpython is the most widely used interpreter and is written in C, it also the
official version downloaded from python.org its a mixture of both compiler
and interpreter and convert the program into byte code, its a byte code that
is executed in Cpython virtual machine

Jython is for python implementation written in java language it converts the
source code to bytecode. In jython these are written in java and can run on
java virtual machine, which is the same environment java uses. it can access
functions and classes of java directly from jython without any additional
effort the same is true on the opposite end.

ironpython python implementation written in C Sharp and has been designed to
run on .NET platforms. Similarly, it can access .net libraries and
frameworks directly from Iron python.

Python is a dynamically typed language. It doesn't know about the type of
the variable until the code is run. So declaration is of no use. What it
does is, It stores that value at some memory location and then binds that
variable name to that memory container

Adding directories to this environment variable adds them to Python's search
path when it is looking for modules. That means you can add a directory with
a module in it anywhere on your computer to PYTHONPATH, and Python will be
able to find it

Compiler compiler is a computer program that translates computer code
written in one programming language (the source language) into another
language (the target language). The name "compiler" is primarily used for
programs that translate source code from a high-level programming language
to a lower level language (e.g. assembly language, object code, or machine
code) to create an executable program """
# The garbage collector attempts to reclaim memory which was allocated by
# the program, but is no longer referenced—also called garbage
