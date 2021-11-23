# REQUIREMENT: Find sum of positive numbers and give the result

# 1st approach : No one writes validation logic
print("1st approach : Without validation----------")

def sum(num1, num2):
    res = num1 + num2
    return res

n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))

print("Addition result :", sum(n1, n2))

print("------------------------")

# 2nd approach : Write validation logic before function call
print("2nd approach : Validation Before Function call ----------")

def sum(num1, num2):
    res = num1 + num2
    return res

n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))

# validation logic
if n1 <= 0 or n2 <= 0:
    print("Please enter valid positive number")
else:
    print("Addition result :", sum(n1, n2))

print("------------------------")


# 3rd approach : Write validation logic inside function
print("3rd approach : Validation Inside Function ----------")

def sum(num1, num2):
    # validation logic
    if num1 <= 0 or num2 <= 0:
        return "Please enter valid positive number"
    res = num1 + num2
    return res
    # return num1 + num2

n1 = int(input("Enter number 1  :"))
n2 = int(input("Enter number 2  :"))

print("Addition result :", sum(n1, n2))

print("------------------------")



'''
print("-----------4th apporach----------")
def _validate_data(n1,n2):
    if n1 < 0 or n2 < 0:
        return False
    else:
        return True

def sum(num1, num2):
    is_valid = _validate_data(num1,num2)
    if is_valid:
        res = num1 + num2
        return res
    else:
        return  "Please enter valid positive number"
'''


