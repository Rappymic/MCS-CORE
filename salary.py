emp_name = input("Enter name of the employee: ")
emp_id = input("Enter ID of the employee: ")
emp_basesalary = []
emp_HRA = []
month = int(input("Enter the no of months you want to calculate: "))
for i in range(month):
    emp_basesalary.append(float(input(f"Enter Base pay for month {i+1}: ")))
    emp_HRA.append(float(input(f"Enter HRA for month {i+1}: ")))

tax = float(input("Enter the tax value in percentage: ").rstrip("%"))/100
emp_total_salary = []
emp_net = []
emp_saving = []
for index, value in enumerate(emp_basesalary):
    emp_total_salary.append(emp_basesalary[index] + emp_HRA[index])
for i in emp_total_salary:
    emp_net.append(i - i*tax)

emp_expenditure = []
print("Enter q in there is no expenditure")
while True:
    for i in range(month):
        a = input(f"Enter the expenditure for month {i+1}:")
        if a == "q":
            break
        else:
            emp_expenditure.append(int(a))
    break
sum = 0
if len(emp_expenditure) == 0:
    print("End of program")
else:
    for index, value in enumerate(emp_net):
        emp_saving.append(emp_net[index] - emp_expenditure[index])
    for index, value in enumerate(emp_saving):
        sum = sum + value
    if sum > 0:
        print(f"Winner!, total saving is ₹ {sum}")
        for index, value in enumerate(emp_saving):
            print(f"The saving for month {index+1} is: {emp_saving[index]}")
    else:
        print(f"Loser!, total balance is {sum}")
        for index, value in enumerate(emp_saving):
            print(f"The saving for month {index+1} is: {emp_saving[index]}")