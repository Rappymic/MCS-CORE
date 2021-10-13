"""Check for even or odd"""

num = int(input("Enter the number to be checked: "))
# type casted into integer as only integer can be even or odd

if num % 2 == 0:
    print("The Number", num, "is a prime number")
else:
    print("The Number", num, "is not a prime number")
