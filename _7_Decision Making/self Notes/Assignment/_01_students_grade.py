"""Determine the grades of student"""

marks = float(input("Enter the final Marks: "))  # user input of marks
common_message = "You have passed with grade"
if marks < 0:
    print("Invalid Input")
elif marks >= 80:
    if 90 <= marks <= 100:  # checking if marks is above 90
        print("Congratulations! You have scored above 90, your grade is A+")
    elif marks > 100:
        print("Invalid Input")
    else:
        print(common_message, " A+")
elif marks >= 60:  # no need to give upper limit, already checked
    print(common_message, " A")
elif marks >= 50:
    print(common_message, " B")
elif marks >= 40:
    print(common_message, " C")
elif marks >= 35:
    print("You have barely passed with D grade")
else:  # if none of the above conditions are satisfied
    print("You have failed the exam")
