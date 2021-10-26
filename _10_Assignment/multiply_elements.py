count = 0
no_elements = 0
while count < 1:
    try:
        no_elements = int(
            input("Enter the number of elements you want to multiply: "))
        if no_elements > 1:
            count += 1
        else:
            print("Enter a valid positive integer, greater than 1")
    except Exception as e:
        print("Enter a valid positive integer")

list_of_no = []
count = 1
while count <= no_elements:
    try:
        temp_num = float(input(f"Enter the {count} number: "))
        list_of_no.append(temp_num)
        count += 1
    except Exception as e:
        print("Enter a valid No.")

multiply = 1
for i in list_of_no:
    multiply = multiply * i
print("The numbers being multiplied are:", list_of_no)
if int(multiply) == multiply:
    print("The multiplication of the given numbers is :", int(multiply))
else:
    print("The multiplication of the given numbers is :", multiply)