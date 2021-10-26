def factorial(value):
    if value == 0 or value == 1:
        return 1
    if value < 0 :
        return 0
    else:
        fact = value * factorial(value - 1)
        return fact

def factorial_iter(val):
    result = 1
    if val >= 0:
        for i in range(1, val+1):
            result = result*i
        return result
    else:
        return 0
print("The factorial of 5 is ",factorial(5))
print(factorial_iter(5))