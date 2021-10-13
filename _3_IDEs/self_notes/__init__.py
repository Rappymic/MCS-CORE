"""
IDE stands for Integrated Development Environment. An IDE have source code
editor, build automation tools,and a debugger. it also contains features like
syntax highlighting intelligent code completion.
------------------------------------------------------------------------------
features:
-   syntax highlighting
-   code completion
-   building executable
-   debugging

# 1. IDLE:
-----------------
Best for beginers

# 2. Pycharm
-----------------
The most notable features of PyCharm include:

-   Support for JavaScript, CSS, and TypeScript
-   Smart code navigation
-   Quick and safe code refactoring
-   Support features like accessing databases directly from the IDE

# 3. visual studio code by microsoft
------------------------------------
-   lightweight
The most notable features of Visual Studio Code include:

-    One of the best smart code completion is based on various factors
-   Git integration
-   Code debugging within the editor
-   code linting, themes, and other services

4. spyder
___________
-   scientific development
The most notable features of Spyder include:

-   Support for automatic code completion and splitting
-   Supports plotting different types of charts and data manipulation
-   Integration of data science libraries like NumPy, Pandas, and Matplotlib

5. Jupyter
___________
-   mostly used in data science
   The most notable features of Jupyter include:
-   Machine learning workflow
-   Numerical Calculations
-   Combine code, text images
-   data science libraries like numpy, pandas, and Matplotlib

"""
a = 999999
while True:
    a += 2
    b = a // 2
    for i in range(2, b):
        if a % i == 0:
            break
    else:
        print(a)
