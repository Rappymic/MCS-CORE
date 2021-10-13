"""Find the maximum number of given numbers"""

a, b, c = 10, 30, 20  # as given in the question

if a > b:
    if a > c:
        print("a is the largest of given 3")
    else:  # c is automatically larger than a
        print("c is the largest of given 3")
else:  # if the above condition fails b is automatically larger than a
    if b > c:
        print("b is the largest of given 3")
    else:  # c is automatically larger than b
        print("c is the largest of given 3")
