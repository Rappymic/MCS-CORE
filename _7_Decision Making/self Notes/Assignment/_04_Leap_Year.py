"""check for leap year from the given input"""

year = int(input("Enter the year value: "))  # string typecast into integer

if year % 100 == 0:
    if year % 400 == 0:
        # if year is divisible by 100 it must be divisible by 400
        print("This is a leap year")
    else:
        print("This is not a leap year")
elif year % 4 == 0:  # already checked for 100
    print("This is a leap Year")
else:
    print("This is not a leap year")
