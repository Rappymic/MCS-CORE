count = 0
no_elements = 0
while count < 1:
    try:
        no_elements = int(
            input("Enter the number of elements you want to add: "))
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

addition = 0
for i, item in enumerate(list_of_no):
    addition = addition + item
print("The No. which are about to be added are:", list_of_no)
if int(addition) == addition:
    print("the sum of the elements are: ", int(addition))
else:
    print("the sum of the elements are: ", addition)
